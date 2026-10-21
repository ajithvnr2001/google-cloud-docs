---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/extended-duration-pods/
title: Extend the run time of Autopilot Pods \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:50.969146+00:00
---

# Extend the run time of Autopilot Pods  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/extended-duration-pods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Extend the run time of Autopilot Pods Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to request extended run times for Pods before they're evicted by Google Kubernetes Engine (GKE).

## About GKE-initiated Pod eviction

Pod evictions are a normal part of running workloads on Kubernetes. GKE evicts workloads during scheduled events, such as automatic node upgrades and autoscaling scale-downs, to ensure that your nodes are up-to-date and optimized for efficient resource usage. By default, GKE sends a termination signal to the container as soon as the event occurs, after which the container has a grace period to terminate before Kubernetes evicts the Pod. For automatic node upgrades, the grace period can be up to one hour. For scale-down events, the grace period can be up to 10 minutes.

Kubernetes has built-in features that containers can use to gracefully handle evictions, such as [PodDisruptionBudgets](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) and [graceful termination periods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination/). However, some workloads, such as batch queues or multiplayer game servers, need to run for a longer period of time before being evicted. The default grace period that GKE grants during GKE-initiated evictions might not be enough for these workloads. In these situations, you can tell Autopilot to avoid evicting specific workloads for up to 7 days.

You can request extended run time for workloads running in Autopilot clusters, or [Autopilot mode workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters).

### Use cases

Some situations in which you might want to tell GKE to avoid evicting workloads include the following:

  * You run multiplayer game servers that would kick players out of their sessions if the servers terminated early.
  * You run audio or video conferencing software that would disrupt in-progress meetings if the servers terminated.
  * You run tasks that need time to complete, and early termination would cause a loss of in-progress work.
  * You run a stateful service that is less tolerant to disruption and you want to minimize how often disruptions occur.



## Pricing

You can request extended run times for your Pods at no additional charge. However, consider the following behavioral changes that might impact your pricing:

  * Autopilot enforces [higher minimum values](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#workload-separation) for the resource requests of extended duration Pods. Autopilot charges you for the resource requests of your running Pods. You're not charged for system overhead or for unused node capacity.
  * Using extended duration Pods might increase the number of nodes in your cluster, which might affect IP address usage and scalability. If you have DaemonSets that run on every node, this results in more DaemonSets in the cluster.



For pricing details, see [Autopilot pricing](https://cloud.google.com/kubernetes-engine/pricing#autopilot_mode).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing GKE cluster.



### Limitations

  * You can't request extended run times for your Spot Pods.
  * Image pull times are counted when calculating the extended run time.
  * You can have a maximum of 50 extended duration workloads (with different CPU requests) in each cluster. This means that up to 50 different sets of CPU request values, after passing Autopilot resource minimums, ratios, and increment size checks, can have extended duration in each cluster.
  * You can't use Kubernetes inter-Pod affinity in extended duration Pods.
  * Whenever possible, GKE places each extended run time Pod on its own node. This behavior helps ensure that nodes can scale down if they're under-utilized.
  * You can't request extended run times for Pods that target [custom compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).



## Request extended run time

To request extended run time for a Pod, set the Kubernetes `cluster-autoscaler.kubernetes.io/safe-to-evict` annotation to `false` in the Pod specification.

  1. Save the following manifest as `extended-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: extended-pods
           labels:
             duration: extended
         spec:
           selector:
             matchLabels:
               duration: extended
           template:
             **metadata :
               annotations:
                 cluster-autoscaler.kubernetes.io/safe-to-evict: "false"**
               labels:
                 duration: extended
             spec:
               containers:
               - name: example-container
                 image: registry.k8s.io/pause
                 resources:
                   requests:
                     cpu: 200m
         

  2. Create the Deployment:
         
         kubectl create -f extended-deployment.yaml
         




The Pods continue to run for at least 7 days before a scale-down or a node auto-upgrade can occur.

## Considerations and recommendations

When you use this functionality, consider the following:

  * Extended duration Pods aren't protected from priority-based eviction. If you use [Kubernetes PriorityClasses](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/capacity-provisioning), consider the following methods to minimize the probability of priority-based eviction: 
    * Ensure that your extended duration Pods use the highest priority PriorityClass, so that other user Pods don't evict your extended duration Pods.
    * Use [workload separation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation) to run extended duration Pods separately from other Pods.
  * System Pods run with the highest priority and will always be able to evict extended duration Pods. To minimize the probability of this, GKE schedules system Pods on the node before scheduling the extended duration Pod.
  * Extended duration Pods can still be evicted early in the following situations:

    * Eviction to make space for higher-priority user Pods (using a higher PriorityClass)
    * Eviction to make space for Kubernetes system components
    * [kubelet out-of-memory eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/) if the Pod uses more memory than it requested (OOMKill)
    * Compute Engine VM maintenance events. [Accelerator-optimized machine types](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) are more likely to be affected by these events because those machines don't support [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process).
    * Node auto-repairs
    * User-initiated events such as the following:

      * [Manual upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_nodes) for [Autopilot-managed node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools#autopilot-node-pools). GKE proceeds with the operation regardless of how the long the Pod has run for.
      * Draining a node.
  * You can use the `cluster-autoscaler.kubernetes.io/safe-to-evict` annotation in Standard clusters, but the result is not the same. Pods run indefinitely even if a scale-down event occurs, preventing deletion of underutilized nodes and resulting in you continuing to pay for those nodes. Pods also aren't protected from evictions caused by node auto-upgrades.




## What's next

  * [Use PriorityClasses to provision spare capacity in Autopilot for rapid Pod scaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/capacity-provisioning)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
