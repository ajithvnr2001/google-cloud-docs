---
url: https://docs.cloud.google.com/config-connector/docs/how-to/customize-controller-manager-rate-limit/
title: Configure the controller manager rate limit \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:21:03.739470+00:00
---

# Configure the controller manager rate limit  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/how-to/customize-controller-manager-rate-limit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure the controller manager rate limit

This pages describes how to configure the overall rate limit (token bucket rate limit) for the controller manager in Config Connector.

The rate limit controls how many requests Config Connector makes to the Kubernetes API server. There are two settings:

  * The `qps` (queries per second) setting determines the average rate at which Config Connector can make requests to the Kubernetes API server.

  * The `burst` value allows for more requests than the `qps` limit for short periods. This helps Config Connector to reconcile quickly, even during times which require more queries to the Kubernetes API server, such as when applying a new batch of configuration using GitOps.




You can think of the "token bucket" algorithm for rate limiting like this: imagine a bucket of capacity `burst` tokens, being refilled at the `qps` rate. Each request requires one token from the bucket. If the bucket is empty, requests are delayed until tokens become available.

## Configure the rate limit for namespaced controller manager

If Config Connector is configured to run in [namespaced mode](https://docs.cloud.google.com/config-connector/docs/how-to/install-namespaced), you can use the `NamespacedControllerReconciler` custom resource to configure the rate limit of the `cnrm-controller-manager` controller's Kubernetes client in your designated namespace. You can configure rate limit for this controller in Config Connector version 1.119 and later.

  1. Create a file named `configure-rate-limit.yaml` and copy the following YAML into it:
         
         apiVersion: customize.core.cnrm.cloud.google.com/v1beta1
         kind: NamespacedControllerReconciler
         metadata:
           name: cnrm-controller-manager # name must not contain the namespace ID suffix
           namespace: NAMESPACE
         spec:
           rateLimit:
             qps: 80 # the default value is 20
             burst: 40 # the default value is 30
         

Replace `NAMESPACE` with the name of your namespace.

  2. Use `kubectl apply` to apply the rate limit configuration to your cluster:
         
         kubectl apply -f configure-rate-limit.yaml

  3. Verify the configuration is successful by running the following command:
         
         kubectl get namespacedcontrollerreconciler cnrm-controller-manager -n NAMESPACE -o jsonpath='{.status.healthy}'

The output should display `status.healthy` field set to `true`.

  4. Verify that the `--qps` and `--burst` flags are added to the `cnrm-controller-manager` controller's manager container by running the following command:
         
         kubectl describe statefulsets -n cnrm-system -l "cnrm.cloud.google.com/scoped-namespace=NAMESPACE"

The output should contain the following:
         
         Containers:
         manager:
           Image:      gcr.io/gke-release/cnrm/controller:fd4c42c
           Port:       23232/TCP
           Host Port:  0/TCP
           Command:
             /configconnector/manager
           Args:
             **--qps=80**
             **--burst=40**
             --scoped-namespace=config-control
             --prometheus-scrape-endpoint=:8888
         




## Configure the rate limit in cluster mode

Starting in version 1.125, if Config Connector is configured to run in cluster mode, you can configure the rate limit of the `cnrm-controller-manager` controller's Kubernetes client using the `ControllerReconciler` custom resource. The usage is similar to the namespaced mode, but in this case, you should use the `ControllerReconciler` CR instead of `NamespacedControllerReconciler`, as in the following example:
    
    
    apiVersion: customize.core.cnrm.cloud.google.com/v1alpha1
    kind: ControllerReconciler
    metadata:
      name: cnrm-controller-manager
    spec:
      rateLimit:
        qps: 80 # the default value is 20
        burst: 40 # the default value is 30
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
