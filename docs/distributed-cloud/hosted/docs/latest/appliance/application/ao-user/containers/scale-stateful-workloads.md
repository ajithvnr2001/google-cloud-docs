---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/scale-stateful-workloads/
title: Scale stateful workloads \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:30.589082+00:00
---

# Scale stateful workloads  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/scale-stateful-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Scale stateful workloads Stay organized with collections  Save and categorize content based on your preferences. 

Scale your stateful workloads to your evolving container workload requirements.

## Before you begin

To complete the tasks in this document, you must request the necessary permissions and prepare your environment.

### Request IAM roles

To create, delete, edit, or view stateful workloads in a Kubernetes cluster, ask your Organization IAM Admin to grant you the **Namespace Admin** (`namespace-admin`) role. This role is bound to your project namespace.

### Prepare your environment

To run commands against the pre-configured bare metal Kubernetes cluster, make sure you have the following resources:

  1. Locate the Kubernetes cluster name, or ask your Platform Administrator what the cluster name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#kubernetes-cluster-kubeconfig) the kubeconfig file for the Kubernetes cluster if you don't have one.

  3. Use the kubeconfig path of the Kubernetes cluster to replace `CLUSTER_KUBECONFIG` in these instructions.




## Scale a `StatefulSet` resource

Use the scaling functionality of Kubernetes to appropriately scale the amount of pods running in your `StatefulSet` resource.

### Manually scale the pods of a `StatefulSet` resource

To manually scale your `StatefulSet` resource, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG -n NAMESPACE \
        scale statefulset STATEFULSET_NAME \
        --replicas NUMBER_OF_REPLICAS
    

Replace the following:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster.

  * `NAMESPACE`: the project namespace.

  * `STATEFULSET_NAME`: the name of the `StatefulSet` object in which to scale.

  * `NUMBER_OF_REPLICAS`: the chosen number of replicated `Pod` objects in the `StatefulSet` object.




### Scale the pods by making an in-place update

To scale the pods of a `StatefulSet` resource directly in the manifest file, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG -n NAMESPACE \
        patch statefulsets STATEFULSET_NAME \
        -p '{"spec":{"replicas":NUMBER_OF_REPLICAS}}'
    

Replace the following:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster.

  * `NAMESPACE`: the project namespace.

  * `STATEFULSET_NAME`: the name of the `StatefulSet` object in which to scale.

  * `NUMBER_OF_REPLICAS`: the chosen number of replicated `Pod` objects in the `StatefulSet` object.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
