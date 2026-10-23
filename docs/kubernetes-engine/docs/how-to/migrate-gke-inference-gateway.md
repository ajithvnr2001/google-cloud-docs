---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-gke-inference-gateway/
title: Migrate GKE Inference Gateway from v1alpha2 to v1 \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:38.805436+00:00
---

# Migrate GKE Inference Gateway from v1alpha2 to v1  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-gke-inference-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Migrate GKE Inference Gateway from v1alpha2 to v1 Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to migrate your GKE Inference Gateway setup from the preview `v1alpha2` API to the generally available `v1` API.

This document is intended for platform administrators and networking specialists who are using the `v1alpha2` version of the GKE Inference Gateway and want to upgrade to the v1 version to use the latest features.

Before you start the migration, ensure you are familiar with the concepts and deployment of the GKE Inference Gateway. We recommend you review [Deploy GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-gke-inference-gateway).

## Before you begin

Before you start the migration, determine if you need to follow this guide.

### Check for existing v1alpha2 APIs

To check if you're using the `v1alpha2` GKE Inference Gateway API, run the following commands:
    
    
    kubectl get inferencepools.inference.networking.x-k8s.io --all-namespaces
    kubectl get inferencemodels.inference.networking.x-k8s.io --all-namespaces
    

The output of these commands determines if you need to migrate:

  * If either command returns one or more `InferencePool` or `InferenceModel` resources, you are using the `v1alpha2` API and must follow this guide.
  * If both commands return `No resources found`, you are not using the `v1alpha2` API. You can proceed with a fresh installation of the `v1` GKE Inference Gateway.



## Migration paths

There are two paths for migrating from `v1alpha2` to `v1`:

  * **Simple migration (with downtime):** this path is faster and simpler but results in a brief period of downtime. It is the recommended path if you don't require a zero-downtime migration.
  * **Zero-downtime migration:** this path is for users who cannot afford any service interruption. It involves running both `v1alpha2` and `v1` stacks side-by-side and gradually shifting traffic.



## Simple migration (with downtime)

This section describes how to perform a simple migration with downtime.

  1. **Delete existing`v1alpha2` resources**: to delete the `v1alpha2` resources, choose one of the following options:

**Option 1: Uninstall using Helm**
         
         helm uninstall HELM_PREVIEW_INFERENCEPOOL_NAME
         

**Option 2: Manually delete resources**

If you are not using Helm, manually delete all resources associated with your `v1alpha2` deployment:

     * Update or delete the `HTTPRoute` to remove the `backendRef` that points to the `v1alpha2` `InferencePool`.
     * Delete the `v1alpha2` `InferencePool`, any `InferenceModel` resources that point to it, and the corresponding Endpoint Picker (EPP) Deployment and Service.

After all `v1alpha2` custom resources are deleted, remove the Custom Resource Definitions (CRD) from your cluster:
    
    kubectl delete -f https://github.com/kubernetes-sigs/gateway-api-inference-extension/releases/download/v0.3.0/manifests.yaml
    

  2. **Install v1 resources** : after you clean up the old resources, install the `v1` GKE Inference Gateway. This process involves the following:

     1. Install the new `v1` Custom Resource Definitions (CRDs).
     2. Create a new `v1` `InferencePool` and corresponding `InferenceObjective` resources. The `InferenceObjective` resource is still defined in the `v1alpha2` API.
     3. Create a new `HTTPRoute` that directs traffic to your new `v1` `InferencePool`.
  3. **Verify the deployment** : after a few minutes, verify that your new `v1` stack is correctly serving traffic.

     1. Confirm that the Gateway status is `PROGRAMMED`:
            
            kubectl get gateway -o wide
            

The output should look similar to this:
            
            NAME                CLASS                            ADDRESS        PROGRAMMED   AGE
            inference-gateway   gke-l7-regional-external-managed   <IP_ADDRESS>   True         10m
            

     2. Verify the endpoint by sending a request:
            
            IP=$(kubectl get gateway/inference-gateway -o jsonpath='{.status.addresses[0].value}')
            PORT=80
            curl -i ${IP}:${PORT}/v1/completions -H 'Content-Type: application/json' -d '{"model": "<var>YOUR_MODEL</var>","prompt": "<var>YOUR_PROMPT</var>","max_tokens": 100,"temperature": 0}'
            

     3. Ensure you receive a successful response with a `200` response code.




## Zero-downtime migration

This migration path is designed for users who cannot afford any service interruption. The following diagram illustrates how GKE Inference Gateway facilitates serving multiple generative AI models, a key aspect of a zero-downtime migration strategy.

![Routing requests to different models based on model name and Priority](https://docs.cloud.google.com/static/kubernetes-engine/images/gen-ai-inference-namespace.png)**Figure:** GKE Inference Gateway routing requests to different generative AI models based on model name and priority

### Distinguishing API versions with kubectl

During the zero-downtime migration, both `v1alpha2` and `v1` CRDs are installed on your cluster. This can create ambiguity when using `kubectl` to query for `InferencePool` resources. To ensure you are interacting with the correct version, you must use the full resource name:

  * For `v1alpha2`:
        
        kubectl get inferencepools.inference.networking.x-k8s.io
        

  * For `v1`:
        
        kubectl get inferencepools.inference.networking.k8s.io
        




The `v1` API also provides a convenient short name, `infpool`, which you can use to query `v1` resources specifically:
    
    
    kubectl get infpool
    

### Stage 1: Side-by-side v1 deployment

In this stage, you deploy the new v1 InferencePool stack alongside the existing v1alpha2 stack, which allows for a safe, gradual migration.

After you finish all the steps in this stage, you have the following infrastructure in the following diagram:

![Routing requests to different models based on model name and Priority](https://docs.cloud.google.com/static/kubernetes-engine/images/gen-ai-inference-namespace-1.png)**Figure:** GKE Inference Gateway routing requests to different generative AI models based on model name and priority

  1. Install needed Custom Resource Definition (CRDs) in your GKE cluster:

     * For GKE versions earlier than `1.34.0-gke.1626000`, run the following command to install both the v1 `InferencePool` and alpha `InferenceObjective` CRDs:
    
    kubectl apply -f https://github.com/kubernetes-sigs/gateway-api-inference-extension/releases/download/v1.0.0/manifests.yaml
    

     * For GKE versions `1.34.0-gke.1626000` or later, install only the alpha `InferenceObjective` CRD by running the following command:
    
    kubectl apply -f https://github.com/kubernetes-sigs/gateway-api-inference-extension/raw/v1.0.0/config/crd/bases/inference.networking.x-k8s.io_inferenceobjectives.yaml
    

**Note:** Starting from GKE versions `1.34.0-gke.1626000`, Google Kubernetes Engine automatically manages the v1 `InferencePool` CRD. You need to install only the alpha `InferenceObjective` CRD Attempting to install the v1 `InferencePool` CRD might cause unexpected issues and results in a warning.
  2. Install the `v1 InferencePool`.

Use Helm to install a new `v1 InferencePool` with a distinct release name, such as `vllm-llama3-8b-instruct-ga`. The `InferencePool` must target the same Model Server pods as the alpha `InferencePool` using `inferencePool.modelServers.matchLabels.app`.

To install the `InferencePool`, use the following command:
         
         helm install vllm-llama3-8b-instruct-ga \
         --set inferencePool.modelServers.matchLabels.app=MODEL_SERVER_DEPLOYMENT_LABEL \
         --set provider.name=gke \
         --version RELEASE \
         oci://registry.k8s.io/gateway-api-inference-extension/charts/inferencepool
         

Replace the following:

     * `MODEL_SERVER_DEPLOYMENT_LABEL`: the label used by your existing Model Server Pods (for example, `vllm-llama3-8b-instruct-preview`).
     * `RELEASE`: the version of the v1 Gateway API Inference Extension Helm chart you want to install
  3. Create `v1alpha2 InferenceObjective` resources.

As part of migrating to the v1.0 release of Gateway API Inference Extension, we also need to migrate from the alpha `InferenceModel` API to the new `InferenceObjective` API.

     1. Apply the following YAML to create the `InferenceObjective` resources:
            
            kubectl apply -f - <<EOF
            ---
            apiVersion: inference.networking.x-k8s.io/v1alpha2
            kind: InferenceObjective
            metadata:
              name: food-review
            spec:
              priority: 2
              poolRef:
                group: inference.networking.k8s.io
                name: vllm-llama3-8b-instruct-ga
            ---
            apiVersion: inference.networking.x-k8s.io/v1alpha2
            kind: InferenceObjective
            metadata:
              name: base-model
            spec:
              priority: 2
              poolRef:
                group: inference.networking.k8s.io
                name: vllm-llama3-8b-instruct-ga
            ---
            EOF
            




### Stage 2: Traffic shifting

With both stacks running, you can start shifting traffic from `v1alpha2` to `v1` by updating the `HTTPRoute` to split traffic. This example shows a 50-50 split.

  1. Update HTTPRoute for traffic splitting.

To update the `HTTPRoute` for traffic splitting, run the following command:
         
         kubectl apply -f - <<EOF
         ---
         apiVersion: gateway.networking.k8s.io/v1
         kind: HTTPRoute
         metadata:
           name: llm-route
         spec:
           parentRefs:
           - group: gateway.networking.k8s.io
             kind: Gateway
             name: inference-gateway
           rules:
           - backendRefs:
             - group: inference.networking.x-k8s.io
               kind: InferencePool
               name: vllm-llama3-8b-instruct-preview
               weight: 50
             - group: inference.networking.k8s.io
               kind: InferencePool
               name: vllm-llama3-8b-instruct-ga
               weight: 50
         ---
         EOF
         

  2. Verify and monitor.

After applying the changes, monitor the performance and stability of the new `v1` stack. Verify that the `inference-gateway` gateway has a `PROGRAMMED` status of `TRUE`.




### Stage 3: Finalization and cleanup

Once you have verified that the `v1 InferencePool` is stable, you can direct all traffic to it and decommission the old `v1alpha2` resources.

  1. **Shift 100% of traffic to the`v1 InferencePool`.**

To shift 100 percent of traffic to the `v1 InferencePool`, run the following command:
         
         kubectl apply -f - <<EOF
         ---
         apiVersion: gateway.networking.k8s.io/v1
         kind: HTTPRoute
         metadata:
           name: llm-route
         spec:
           parentRefs:
           - group: gateway.networking.k8s.io
             kind: Gateway
             name: inference-gateway
           rules:
           - backendRefs:
             - group: inference.networking.k8s.io
               kind: InferencePool
               name: vllm-llama3-8b-instruct-ga
               weight: 100
         ---
         EOF
         

  2. **Perform final verification.**

After directing all traffic to the `v1` stack, verify that it is handling all traffic as expected.

     1. Confirm that the Gateway status is `PROGRAMMED`:
            
            kubectl get gateway -o wide
            

The output should look similar to this:
            
            NAME                CLASS                              ADDRESS           PROGRAMMED   AGE
            inference-gateway   gke-l7-regional-external-managed   <IP_ADDRESS>   True                     10m
            

     2. Verify the endpoint by sending a request:
            
            IP=$(kubectl get gateway/inference-gateway -o jsonpath='{.status.addresses[0].value}')
            PORT=80
            curl -i ${IP}:${PORT}/v1/completions -H 'Content-Type: application/json' -d '{
            "model": "YOUR_MODEL",
            "prompt": "YOUR_PROMPT",
            "max_tokens": 100,
            "temperature": 0
            }'
            

     3. Ensure you receive a successful response with a `200` response code.

  3. **Clean up v1alpha2 resources.**

After confirming the `v1` stack is fully operational, safely remove the old `v1alpha2` resources.

  4. **Check for remaining`v1alpha2` resources.**

Now that you've migrated to the `v1` `InferencePool` API, it's safe to delete the old CRDs. Check for existing v1alpha2 APIs to ensure you no longer have any `v1alpha2` resources in use. If you still have some remaining, you can continue the migration process for those.

  5. **Delete`v1alpha2` CRDs.**

After all `v1alpha2` custom resources are deleted, remove the Custom Resource Definitions (CRD) from your cluster:
         
         kubectl delete -f https://github.com/kubernetes-sigs/gateway-api-inference-extension/releases/download/v0.3.0/manifests.yaml
         

After completing all steps, your infrastructure should resemble the following diagram:

![Routing requests to different models based on model name and Priority](https://docs.cloud.google.com/static/kubernetes-engine/images/gen-ai-inference-namespace-2.png)**Figure:** GKE Inference Gateway routing requests to different generative AI models based on model name and priority



## What's next

  * Learn more about [Deploy GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-gke-inference-gateway). 
    * Explore other [GKE networking features](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
