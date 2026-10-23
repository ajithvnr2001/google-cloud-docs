---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gke-inference-gateway-rollout-operations/
title: Perform roll out operations for GKE Inference Gateway \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:07.490350+00:00
---

# Perform roll out operations for GKE Inference Gateway  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gke-inference-gateway-rollout-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Perform roll out operations for GKE Inference Gateway Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to perform incremental roll out operations, that gradually deploy new versions of your inference infrastructure, for GKE Inference Gateway. This gateway lets you perform safe and controlled updates to your inference infrastructure. You can update nodes, base models, and LoRA adapters with minimal service disruption. This page also provides guidance on traffic splitting and rollbacks to ensure reliable deployments.

This page is for GKE Identity and account admins and Developers who want to perform roll out operations for GKE Inference Gateway.

The following use cases are supported:

  * Node (compute, accelerator) update roll out
  * Base model update roll out



## Update a node roll out

Node updates safely migrate inference workloads to new node hardware or accelerator configurations. This process occurs in a controlled manner without interrupting model service. Use node updates to minimize service disruption during hardware upgrades, driver updates, or security issue resolution.

  1. **Create a new`InferencePool`**: deploy an `InferencePool` configured with the updated node or hardware specifications.

  2. **Split traffic using an`HTTPRoute`**: configure an `HTTPRoute` to distribute traffic between the existing and new `InferencePool` resources. Use the `weight` field in `backendRefs` to manage the traffic percentage directed to the new nodes.

  3. **Maintain a consistent`InferenceObjective`**: retain the existing `InferenceObjective` configuration to ensure uniform model behavior across both node configurations.

  4. **Retain original resources** : keep the original `InferencePool` and nodes active during the roll out to enable rollbacks if needed.




For example, you can create a new `InferencePool` named `llm-new`. Configure this pool with the same model configuration as your existing `llm` `InferencePool`. Deploy the pool on a new set of nodes within your cluster. Use an `HTTPRoute` object to split traffic between the original `llm` and the new `llm-new` `InferencePool`. This technique lets you incrementally update your model nodes.

The following diagram illustrates how GKE Inference Gateway performs a node update roll out.

![Node update rollout process](https://docs.cloud.google.com/static/kubernetes-engine/images/node-roll-out.png)**Figure:** Node update roll out process

To perform a node update roll out, follow these steps:

  1. Save the following sample manifest as `routes-to-llm.yaml`:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: HTTPRoute
         metadata:
           name: routes-to-llm
         spec:
           parentRefs:
             - name: my-inference-gateway
               group: gateway.networking.k8s.io
               kind: Gateway
           rules:
           - backendRefs:
             - name: llm
               group: inference.networking.k8s.io
               kind: InferencePool
               weight: 90
             - name: llm-new
               group: inference.networking.k8s.io
               kind: InferencePool
               weight: 10
         

  2. Apply the sample manifest to your cluster:
         
         kubectl apply -f routes-to-llm.yaml
         




The original `llm` `InferencePool` receives most of the traffic, while the `llm-new` `InferencePool` receives the rest. Increase the traffic weight gradually for the `llm-new` `InferencePool` to complete the node update roll out.

## Roll out a base model

Base model updates roll out in phases to a new base LLM, retaining compatibility with existing LoRA adapters. You can use base model update roll outs to upgrade to improved model architectures or to address model-specific issues.

To roll out a base model update:

  1. **Deploy new infrastructure** : create new nodes and a new `InferencePool` configured with the new base model that you chose.
  2. **Configure traffic distribution** : use an `HTTPRoute` to split traffic between the existing `InferencePool` (which uses the old base model) and the new `InferencePool` (using the new base model). The `backendRefs weight` field controls the traffic percentage allocated to each pool.
  3. **Maintain`InferenceObjective` integrity**: keep your `InferenceObjective` configuration unchanged. This approach helps ensure that the system applies the same LoRA adapters consistently across both base model versions.
  4. **Preserve rollback capability** : retain the original nodes and `InferencePool` during the roll out to facilitate a rollback if necessary.



You create a new `InferencePool` named `llm-pool-version-2`. This pool deploys a new version of the base model on a new set of nodes. By configuring an `HTTPRoute`, as shown in the provided example, you can incrementally split traffic between the original `llm-pool` and `llm-pool-version-2`. This lets you control base model updates in your cluster.

To perform a base model update roll out, follow these steps:

  1. Save the following sample manifest as `routes-to-llm.yaml`:
         
         apiVersion: gateway.networking.k8s.io/v1
         kind: HTTPRoute
         metadata:
           name: routes-to-llm
         spec:
           parentRefs:
             - name: my-inference-gateway
               group: gateway.networking.k8s.io
               kind: Gateway
           rules:
           - backendRefs:
             - name: llm-pool
               group: inference.networking.k8s.io
               kind: InferencePool
               weight: 90
             - name: llm-pool-version-2
               group: inference.networking.k8s.io
               kind: InferencePool
               weight: 10
         

  2. Apply the sample manifest to your cluster:
         
         kubectl apply -f routes-to-llm.yaml
         




The original `llm-pool` `InferencePool` receives most of the traffic, while the `llm-pool-version-2` `InferencePool` receives the rest. Increase the traffic weight gradually for the `llm-pool-version-2` `InferencePool` to complete the base model update roll out.

## What's next

  * [Customize GKE Inference Gateway configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-gke-inference-gateway-configurations)
  * [Serve an LLM with GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-with-gke-inference-gateway)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
