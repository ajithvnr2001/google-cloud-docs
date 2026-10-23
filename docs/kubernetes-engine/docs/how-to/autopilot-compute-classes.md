---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-compute-classes/
title: Choose compute classes for Autopilot Pods \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:24.958116+00:00
---

# Choose compute classes for Autopilot Pods  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-compute-classes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Choose compute classes for Autopilot Pods Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This document shows you how to select specific compute classes to run workloads that have unique hardware requirements in your Google Kubernetes Engine (GKE) Autopilot clusters. Before reading this document, ensure that you're familiar with the concept of [compute classes in GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes).

## Overview of Autopilot compute classes

Autopilot offers _compute classes_ that are designed to run workloads that have specific hardware requirements. These compute classes are useful for workloads such as machine learning and AI tasks, or running real-time high traffic databases.

These compute classes are a subset of the Compute Engine [machine series](https://docs.cloud.google.com/compute/docs/machine-types#machine_type_comparison), and offer flexibility beyond the default Autopilot general-purpose compute class. For example, the `Scale-Out` class turns off simultaneous multi-threading so that each vCPU is one physical core.

Based on your individual Pod needs, you can configure your regular Autopilot Pods or your Spot Pods to request nodes backed by these compute classes. You can also request specific CPU architecture, such as [Arm](https://www.arm.com/architecture), in compute classes that support that architecture.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * [Ensure that you have a GKE Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster) running GKE version 1.24.1-gke.1400 or later.



## Request a compute class in your Autopilot Pod

To tell Autopilot to place your Pods on a specific compute class, specify the `cloud.google.com/compute-class` label in a [nodeSelector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector) or a [node affinity rule](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity), such as in the following examples: 

### nodeSelector
    
    
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: hello-app
        spec:
          replicas: 3
          selector:
            matchLabels:
              app: hello-app
          template:
            metadata:
              labels:
                app: hello-app
            spec:
              nodeSelector:
                **cloud.google.com/compute-class : "COMPUTE_CLASS"**
              containers:
              - name: hello-app
                image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
                resources:
                  requests:
                    cpu: "2000m"
                    memory: "2Gi"
        

Replace `COMPUTE_CLASS` with the name of the [compute class](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/balanced-scale-out-autopilot#when-to-use) based on your use case, such as `Scale-Out`. If you select `Performance`, you can optionally select a Compute Engine machine series in the node selector. If you don't specify a machine series, GKE uses the C4 machine series depending on [regional availability](https://docs.cloud.google.com/compute/docs/regions-zones#available). For instructions, see [Run CPU-intensive workloads with optimal performance](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/performance-pods).

### nodeAffinity
    
    
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: hello-app
        spec:
          replicas: 3
          selector:
            matchLabels:
              app: hello-app
          template:
            metadata:
              labels:
                app: hello-app
            spec:
              terminationGracePeriodSeconds: 25
              containers:
              - name: hello-app
                image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
                resources:
                  requests:
                    cpu: "2000m"
                    memory: "2Gi"
                    ephemeral-storage: "1Gi"
              **affinity :
                nodeAffinity:
                  requiredDuringSchedulingIgnoredDuringExecution:
                    nodeSelectorTerms:
                    - matchExpressions:
                      - key: cloud.google.com/compute-class
                        operator: In
                        values:
                        - "COMPUTE_CLASS"**
          

Replace `COMPUTE_CLASS` with the name of the [compute class](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes#when-to-use) based on your use case, such as `Scale-Out`. If you select `Performance`, you can optionally select a Compute Engine machine series in the node selector. If you don't specify a machine series, GKE uses the C4 machine series depending on [regional availability](https://docs.cloud.google.com/compute/docs/regions-zones#available). For instructions, see [Run CPU-intensive workloads with optimal performance](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/performance-pods).

You can also request specific compute classes for your Spot Pods.

### Specify resource requests

When you choose a compute class, make sure that you specify resource requests for your Pods based on the [Minimum and maximum resource requests](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#min-max-requests) for your selected class. If your requests are less than the minimum, Autopilot automatically scales your requests up. However, if your requests are greater than the maximum, Autopilot does not deploy your Pods and displays an error message.

## Choose a CPU architecture

Some compute classes support multiple CPU architectures. For example, the `Scale-Out` class supports both Arm and x86 architectures. If you don't request a specific architecture, Autopilot provisions nodes that have the default architecture of the specified compute class. If your Pods need to use a different architecture, request that architecture in your node selector or node affinity rule, alongside your compute class request. The compute class that you request must support the CPU architecture you specify.

For instructions, refer to [Deploy Autopilot Pods on Arm architecture](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-arm-workloads).

## What's next

  * [Learn about best practices for ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/computeclasses).
  * [Learn more about Autopilot cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-architecture).
  * [Learn about the lifecycle of Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/).
  * [Learn about the available Autopilot compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes).
  * [Read about the default, minimum, and maximum resource requests for each platform](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
