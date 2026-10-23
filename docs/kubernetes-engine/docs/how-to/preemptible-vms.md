---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/preemptible-vms/
title: Use preemptible VMs to run fault-tolerant workloads \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:13.579789+00:00
---

# Use preemptible VMs to run fault-tolerant workloads  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/preemptible-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Use preemptible VMs to run fault-tolerant workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to use preemptible VMs in Google Kubernetes Engine (GKE).

**Best practice** : 

Spot VMs are the latest version of preemptible VMs. Instead of preemptible VMs, we recommend that you use either [Spot Pods in Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-spot-pods) or [Spot VMs in Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/spot-vms). GKE continues to support preemptible VMs, which use the same pricing model as Spot VMs.

## Overview

Preemptible VMs are Compute Engine [VM instances](https://docs.cloud.google.com/compute/docs/instances/preemptible) that are priced lower than standard VMs and provide no guarantee of availability. Preemptible VMs offer similar functionality to [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot), but only last up to 24 hours after creation.

In some cases, a preemptible VM might last longer than 24 hours. This can occur when the new Compute Engine instance comes up too fast and Kubernetes doesn't recognize that a different Compute Engine VM was created. The underlying Compute Engine instance will have a maximum duration of 24 hours and follow the [expected preemptible VM behavior](https://docs.cloud.google.com/compute/docs/instances/preemptible).

**Note:** Preemptible VMs share the same pricing model as Spot VMs. For more information, see [Compute Engine Pricing](https://docs.cloud.google.com/compute/all-pricing#compute-engine-pricing).

### Comparison to Spot VMs

Preemptible VMs share many similarities with Spot VMs, including the following:

  * Terminated when Compute Engine requires the resources to run standard VMs.
  * Useful for running stateless, batch, or fault-tolerant workloads.
  * Lower pricing than standard VMs.
  * Graceful node shutdown is enabled by default. However, unlike Spot VMs, you can't modify the duration of the graceful termination period. For more information, see [Termination and graceful shutdown of Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms#termination-graceful-shutdown).
  * Works with the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) and [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning).



In contrast to Spot VMs, which have no maximum expiration time, preemptible VMs only last for up to 24 hours after creation.

You can enable preemptible VMs on new clusters and node pools, use `nodeSelector` or node affinity to control scheduling, and use taints and tolerations to avoid issues with system workloads when nodes are preempted.

### Termination and graceful shutdown of preemptible VMs

**Note:** With Spot VMs, you can optionally extend the duration of the graceful termination period. For more information, see [Termination and graceful shutdown of Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms#termination-graceful-shutdown).

When Compute Engine needs to reclaim the resources used by preemptible VMs, a [preemption notice](https://docs.cloud.google.com/compute/docs/instances/preemptible#preemption) is sent to GKE. Preemptible VMs terminate 30 seconds after receiving a termination notice.

By default, clusters use [graceful node shutdown](https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/#graceful-node-shutdown). The `kubelet` notices the termination notice and gracefully terminates Pods that are running on the node. If the Pods are part of a managed workload, such as a Deployment, the controller creates and schedules new Pods to replace the terminated Pods.

On a best-effort basis, the `kubelet` grants a graceful termination period of 15 seconds for non-system Pods, after which system Pods (with the `system-cluster-critical` or `system-node-critical` priorityClasses) have 15 seconds to gracefully terminate. During graceful node termination, the `kubelet` updates the status of the Pods and assigns a `Failed` phase and a `Terminated` reason to the terminated Pods.

The graceful termination period for non-system Pods has a maximum time of 15 seconds. Specifying a value greater than 15 seconds in the `terminationGracePeriodSeconds` field of your Pod manifest has no effect. The entire VM shuts down 30 seconds after the preemption notice.

### Modifications to Kubernetes behavior

Using preemptible VMs on GKE modifies the protections that are provided by Kubernetes `PodDisruptionBudgets`. The reclamation of preemptible VMs is involuntary and is not covered by the protections of [`PodDisruptionBudgets`](https://kubernetes.io/docs/tasks/run-application/configure-pdb/). You might experience greater unavailability than your configured `PodDisruptionBudget`.

### Limitations

  * Preemptible VMs don't support Windows Server node pools.
  * With preemptible VMs, you can't modify the 15-second grace period for non-system Pods and the subsequent 15-second period for system Pods. The underlying `shutdownGracePeriod` and `shutdownGracePeriodCriticalPods` `kubelet` configuration fields are immutable. However, Spot VMs do support modifying these settings. For more information, see [Termination and graceful shutdown of Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms#termination-graceful-shutdown).



## Create a cluster or node pool with preemptible VMs

You can use the Google Cloud CLI to create a cluster or node pool with preemptible VMs.

To create a cluster with preemptible VMs, run the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        **--preemptible**
    

Replace `CLUSTER_NAME` with the name of your new cluster.

To create a node pool with preemptible VMs, run the following command:
    
    
    gcloud container node-pools create POOL_NAME \
        --cluster=CLUSTER_NAME \
        **--preemptible**
    

Replace `POOL_NAME` with the name of your new node pool.

**Note:** If you use the Google Cloud console to duplicate an existing cluster that uses preemptible VMs, you must enable Spot VMs for each node pool and configure your workloads to use Spot VMs instead of preemptible VMs. For instructions, refer to [Use Spot VMs to run fault-tolerant workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/spot-vms).

## Use nodeSelector to schedule Pods on preemptible VMs

GKE adds the `cloud.google.com/gke-preemptible=true` and `cloud.google.com/gke-provisioning=preemptible` labels to nodes that use preemptible VMs. You can use a `nodeSelector` in your deployments to tell GKE to schedule Pods onto preemptible VMs.

For example, the following Deployment filters for preemptible VMs using the `cloud.google.com/gke-preemptible` label:
    
    
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
          containers:
          - name: hello-app
            image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
            resources:
              requests:
                cpu: 200m
          **nodeSelector :
            cloud.google.com/gke-preemptible: "true"**
    

## Use node taints for preemptible VMs

You can taint nodes that use preemptible VMs so that GKE can only place Pods with the corresponding toleration on those nodes.

To add a node taint to a node pool that uses preemptible VMs, use the `--node-taints` flag when creating the node pool, similar to the following command:
    
    
    gcloud container node-pools create POOL2_NAME \
        --cluster=CLUSTER_NAME \
        **--node-taints =cloud.google.com/gke-preemptible="true":NoSchedule**
    

Now, only Pods that tolerate the node taint are scheduled to the node.

To add the relevant toleration to your Pods, modify your deployments and add the following to your Pod specification:
    
    
    tolerations:
    - key: cloud.google.com/gke-preemptible
      operator: Equal
      value: "true"
      effect: NoSchedule
    

## Node taints for GPU preemptible VMs

Preemptible VMs support using [GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus). You should create at least one other node pool in your cluster that doesn't use preemptible VMs before adding a GPU node pool that uses preemptible VMs. Having a standard node pool helps ensure that GKE can safely place system components like DNS.

If you create a new cluster with GPU node pools that use preemptible VMs, or if you add a new GPU node pool that uses preemptible VMs to a cluster that does not already have a standard node pool, GKE does not automatically add the `nvidia.com/gpu=present:NoSchedule` taint to the nodes. GKE might schedule system Pods onto the preemptible VMs, which can lead to disruptions. This behavior also increases your resource consumption, because GPU nodes are more expensive than non-GPU nodes.

## What's next

  * [Learn how to run a GKE application on Spot VMs with on-demand nodes as fallback](https://cloud.google.com/blog/topics/developers-practitioners/running-gke-application-spot-nodes-demand-nodes-fallback).
  * [Learn more about Spot VMs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms).
  * [Learn about taints and tolerations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-taints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
