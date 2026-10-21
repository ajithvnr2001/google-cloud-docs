---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/guardrails/
title: Diagnosing issues with guardrails \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:11:01.293684+00:00
---

# Diagnosing issues with guardrails  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/guardrails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Diagnosing issues with guardrails Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.12 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.12 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/guardrails.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/guardrails.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/guardrails.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/guardrails.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/guardrails.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/guardrails.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/guardrails.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/guardrails.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/guardrails.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/guardrails.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/guardrails.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/guardrails.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/guardrails.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/guardrails.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/guardrails.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/guardrails.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/guardrails.html)



## Guardrails overview

Apigee hybrid Guardrails is a mechanism that will alert customers to a potential issue before the issue can impact a Hybrid instance. In other words, Hybrid Guardrails will stop a command in its tracks if the command risks the stability of a Hybrid instance. Whether it's an incorrect configuration or some insufficient resource, Hybrid Guardrails will prevent any modifications to a Hybrid instance until the risk of the issue is removed. This saves the customer from spending time on issues that would normally take hours or days to resolve. 

## Using Guardrails with Apigee hybrid

To use Hybrid Guardrails, execute the same Hybrid Helm install or Hybrid Helm upgrade commands documented in the Hybrid installation instructions. No additional commands are needed to run Guardrails. 

When you issue a Helm command for Apigee hybrid, two things happen before the helm command applies the configuration to your hybrid instance: 

  * Helm creates a temporary Guardrails pod with your applied configuration. If the Guadrails pod spins up to a healthy state, the pod will test your hybrid instance against your applied configuration. If testing passes, the Guardrails pod is terminated and your configuration is then applied to your Apigee hybrid instance. 
  * If testing fails, the Guardails pod is left in an unhealthy state to allow diagnosis of the pod. The helm command will display an error message reporting the Guardrails pod has failed. 



The following example shows using Guardrails to test network connectivity from a Hybrid instance to the Apigee Control Plane as part of the installation of the `apigee-datastore` component. You can use the same sequence for all Apigee hybrid components: 

Install the apigee-datastore component using the following command: 
    
    
    helm upgrade datastore apigee-datastore/ \
      --install \
      --namespace apigee \
      --atomic \
      -f overrides.yaml
    

If there is an immediate error, the Helm command will also show an error message displaying the Guardrails checks failed as in the following example: 
    
    
     helm upgrade datastore apigee-datastore/ \
      --install \
      --namespace apigee \
      -f my-overrides.yaml
    
      . . .
        Error: UPGRADE FAILED: pre-upgrade hooks failed: 1 error occurred:
          * pod apigee-hybrid-helm-guardrail-datastore failed

To see what check has failed and why, check the Guardrails pod logs like the following example: 
    
    
    kubectl logs -n apigee apigee-hybrid-helm-guardrail-datastore
    {"level":"INFO","timestamp":"2024-02-01T20:28:55.934Z","msg":"logging enabled","log-level":"INFO"}
    {"level":"INFO","timestamp":"2024-02-01T20:28:55.935Z","msg":"","checkpoint":"upgrade","component":"apigee-datastore"}
    {"level":"INFO","timestamp":"2024-02-01T20:28:55.935Z","msg":"initiating pre-install checks"}
    {"level":"INFO","timestamp":"2024-02-01T20:28:55.935Z","msg":"check validation starting...","check":"controlplane_connectivity"}
    **{"level":"ERROR","timestamp":"2024-02-01T20:28:55.961Z","msg":"connectivity test failed","check":"controlplane_connectivity","host":"https://apigee.googleapis.com","error":"Get \"https://apigee.googleapis.com\": dial tcp: lookup apigee.googleapis.com on 10.92.0.10:53: no such host"}**

In this example, the actual test failure message is this part: 
    
    
    {"level":"ERROR","timestamp":"2024-02-01T20:28:55.961Z","msg":"connectivity test failed","check":"controlplane_connectivity","host":"https://apigee.googleapis.com","error":"Get \"https://apigee.googleapis.com\": dial tcp: lookup apigee.googleapis.com on 10.92.0.10:53: no such host"}

The Guardrails pod is automatically provisioned when you issue the helm command. If the Apigee Control Plane connectivity test passes, the Guardrails pod is terminated at the end of execution. 

Check the status of the pods quickly after issuing the `helm install` command. The following example output shows the Guardrail pods in a healthy state, meaning the Control Plane connectivity test passed: 
    
    
    kubectl get pods -n apigee -w
    NAME                                      READY    STATUS             RESTARTS    AGE
    apigee-hybrid-helm-guardrail-datastore    0/1      Pending            0           0s
    apigee-hybrid-helm-guardrail-datastore    0/1      Pending            0           1s
    apigee-hybrid-helm-guardrail-datastore    0/1      ContainerCreating  0           1s
    apigee-hybrid-helm-guardrail-datastore    0/1      Completed          0           2s
    apigee-hybrid-helm-guardrail-datastore    0/1      Completed          0           3s
    apigee-hybrid-helm-guardrail-datastore    0/1      Terminating        0           3s
    apigee-hybrid-helm-guardrail-datastore    0/1      Terminating        0           3s

If the Apigee Control Plane connectivity test fails, the Guardrails pod will remain in Error state similar to the following example output: 
    
    
    kubectl get pods -n apigee -w
    NAME                                      READY    STATUS             RESTARTS    AGE
    apigee-hybrid-helm-guardrail-datastore    0/1      Pending            0           0s
    apigee-hybrid-helm-guardrail-datastore    0/1      Pending            0           0s
    apigee-hybrid-helm-guardrail-datastore    0/1      ContainerCreating  0           0s
    apigee-hybrid-helm-guardrail-datastore    0/1      Error              0           4s
    apigee-hybrid-helm-guardrail-datastore    0/1      Error              0           5s
    apigee-hybrid-helm-guardrail-datastore    0/1      Error              0           6s

## Temporarily disabling Guardrails

If you need to disable the Guardrails checks, add the `--no-hooks` flag to the Helm command. The following example shows the `--no-hooks` flag in a Helm command: 
    
    
    helm upgrade datastore apigee-datastore/ \
      --install \
      --namespace apigee \
      -f overrides.yaml \
      **--no-hooks**
    

## Configuring Guardrails in the overrides file

Starting in Apigee hybrid version 1.12, Guardrails are configured by default in each chart. You can override the **image URL** , **tag** , and **image pull policy** in your `overrides` file. 

For example, the Guardrails image url, tag, and pull policy below would be added to your overrides file:
    
    
    # Apigee Ingressgateway
    ingressGateway:
      image:
        pullPolicy: Always
    
    ## NOTE: The Guardrails config is below. The ingressgateway config above is for position reference only and is NOT required for Guardrails config.
    
    # Apigee Guardrails
    guardrails:
      image:
        url: "gcr.io/ng-hybrid/guardrails/apigee-watcher"
        tag: "12345_6789abcde"
        pullPolicy: Always
    

### Using Kubernetes tolerations with Guardrails

You can also add [tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to Guardrails in your `overrides` file. If no tolerations are defined under the Guardrails `overrides` configuration, Guardrails will use any globally defined tolerations.

For example, to include tolerations specifically in the Guardrails section of your `overrides` file, you would add something similar to the following stanza:
    
    
      # Apigee Guardrails
      guardrails:
        image:
          url: "gcr.io/ng-hybrid/guardrails/apigee-watcher"
          tag: "12345_6789abcde"
          pullPolicy: Always
        tolerations:
        - key: "say"
          operator: "Equal"
          value: "taunt"
          effect: "NoSchedule"
      

## Troubleshooting Guardrails

### Environment variable checkpoint missing or empty

If you are seeing the `Client.Timeout exceeded` error in the `apigee-operator` guradrails pod log, you can use the following troubleshooting steps to determine the source of the problem.

  1. Create a new YAML file with the following content. The name of the YAML file can be anything you want.
    
    apiVersion: v1
      kind: Pod
      metadata:
        labels:
        name: apigee-simple-client  
      spec:
        containers:
        - name: apigee-simple-client
          image: "gcr.io/apigee-release/hybrid/apigee-hybrid-cassandra-client:1.10.1"
          imagePullPolicy: Always
          command:
          - sleep
          - "3650d"
        restartPolicy: Never
        hostNetwork: false
    

  2. Apply the new YAML file with the following command:
    
    kubectl apply -n apigee-system -f NEW_YAML_FILE
    

  3. Pass command input to the pod with the `kubectl exec` command:
    
    kubectl exec -it -n apigee-system apigee-simple-client -- /bin/bash
      

  4. Run the following command inside the `apigee-simple-client` pod and check the output:
    
    curl -v -I --proxy http://forwarding-proxy.example.com:5678 \
        https://apigee.googleapis.com
      

If the curl command successfully connects to the http proxy and reaches `apigee.googleapis.com` then the curl command should return an HTTP response code. If the curl command cannot reach the proxy or cannot connect to `apigee.googleapis.com` through the proxy, the curl command should show an error. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
