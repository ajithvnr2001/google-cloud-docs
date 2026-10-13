---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/secure-with-gke-sandbox/
title: Secure With GKE Sandbox \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:43.518936+00:00
---

# Secure With GKE Sandbox  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/securing/secure-with-gke-sandbox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Secure With GKE Sandbox Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure Knative serving running on Google Kubernetes Engine (GKE) to use GKE Sandbox for improved workload isolation from the host kernel.

## Objectives

  * Learn how to enable GKE Sandbox on your Knative serving cluster.
  * Deploy a service specified to run on sandboxed nodes.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Knative serving](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  * This tutorial assumes that you have Knative serving [installed and configured on your cluster](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install).
  * Ensure that your command-line environment is set up and the tools are up-to-date: 
    * [GKE clusters on Google Cloud](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/command-line-tools)
    * [GKE clusters outside Google Cloud](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/outside-gcp/command-line-tools)



## Add GKE Sandbox node pool to an existing Knative serving Cluster

Follow the [steps to add a node pool enabled to use GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods#enabling-existing) to your existing Knative serving cluster. This is where workloads that you opt in to use GKE Sandbox run.

## Deploy a workload on the GKE Sandbox node pool

Once you have a GKE cluster with a GKE Sandbox-enabled node pool, update your Knative serving configuration. Also, update each service specification to make use of the new nodes. These updates are required just one time.

### Enable the runtime class feature flag

In this section, you enable the Kubernetes runtime class by using Knative feature and extension flags in the `config-features` ConfigMap in the `knative-serving` namespace. To enable the runtime class, you set the ConfigMap flag `kubernetes.podspec-runtimeclassname` to `enabled`. For more information, see [Kubernetes runtime class](https://knative.dev/docs/serving/feature-flags/#kubernetes-runtime-class) and [Configuring flags](https://knative.dev/docs/serving/configuration/feature-flags/#configuring-flags) in the Knative [Features and extensions](https://knative.dev/docs/serving/configuration/feature-flags/) documentation.

  1. Open the `config-features` ConfigMap for editing:
         
         kubectl edit configmap config-features -n knative-serving
         

  2. Add the `kubernetes.podspec-runtimeclassname: enabled` feature flag to the `data` field.

  3. As an alternative to the preceding steps, you can run the following command to patch this flag into your Knative features:
         
         kubectl patch configmap config-features \
             --type='json' \
             -p="[{'op': 'replace', 'path': '/data/kubernetes.podspec-runtimeclassname', 'value': 'enabled'}]" \
             -n knative-serving
         

  4. To verify your edits, run the following command to view the ConfigMap:
         
         kubectl get configmap config-features -n knative-serving -o yaml
         

The ConfigMap should resemble the following:
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
             name: config-features
             namespace: knative-serving
             labels:
                 serving.knative.dev/release: v0.22.0** data:
             kubernetes.podspec-runtimeclassname: enabled**
         




### Deploy a Service configured to run in GKE Sandbox

After you've enabled the runtime class feature flag, you can create Services that specify a `runtimeClassName` in the spec. Set the `runtimeClassName` to `gvisor` to indicate that a service should run on the GKE Sandbox node pool.

**Important:** Not all workloads are compatible with GKE Sandbox, [learn more about its limitations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#limitations).

  1. Deploy a "Hello World" Knative application by running the following command:
         
         cat <<EOF | kubectl apply -f -
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
             name: helloworld-go
         spec:
             template:
                 spec:
                     runtimeClassName: gvisor
                     containers:
                         -   image: gcr.io/knative-samples/helloworld-go
                             env:
                             -   name: TARGET
                                 value: "gVisor User"
         EOF
         

If the Kubernetes runtime class name feature is enabled, the command should finish without errors.

  2. Get the pods for your service running and their configured runtime class by running:
         
         kubectl get pods \
             -o=custom-columns='NAME:.metadata.name,RUNTIME CLASS:.spec.runtimeClassName,STATUS:.status.phase'
         

The output should resemble the following:
         
         NAME                                              RUNTIME CLASS   STATUS
         helloworld-go-00001-deployment-55f58477f-fxm6m    gvisor          Running
         




## What's next

After verifying that you can deploy untrusted apps on your newly created GKE Sandbox node pool, you're ready to add `runtimeClassName: gvisor` to the Kubernetes specs for other untrusted services you would like to execute on GKE Sandbox node pools.

Additional reading:

  * [GKE Sandbox documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) docs to understand limitations that may break compatibility with some services.
  * [gVisor docs on deploying Knative services](https://gvisor.dev/docs/tutorials/knative/) for a more detailed guide to deploying Knative apps on gVisor (also called GKE Sandbox).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
