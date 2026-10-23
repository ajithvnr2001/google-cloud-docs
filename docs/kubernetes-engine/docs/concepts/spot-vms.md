---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms/
title: Spot VMs \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:15.989097+00:00
---

# Spot VMs  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Spot VMs Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains what Spot VMs are and how they work in Google Kubernetes Engine (GKE). For more information about using Spot VMs, see the following:

  * **Standard mode** : to create Standard node pools with Spot VMs, see [Run fault-tolerant workloads at lower costs with Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/spot-vms).
  * **Autopilot mode** : to request Spot Pods, see [Run fault-tolerant workloads at lower costs in Spot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-spot-pods).



You can request Spot VMs for your workloads in both Standard and Autopilot mode by using [ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#machinefamily-rule) or node selectors.

## Overview of Spot VMs in GKE

_Spot VMs_ are Compute Engine [virtual machine (VM) instances](https://docs.cloud.google.com/compute/docs/instances) that are priced lower than standard Compute Engine VMs and provide no guarantee of availability. Spot VMs offer the same [machine types](https://docs.cloud.google.com/compute/docs/machine-types) and options as standard VMs.

**Note:** For better availability, use smaller machine types.

You can use Spot VMs in your clusters and node pools to run stateless, batch, or fault-tolerant workloads that can tolerate disruptions caused by the ephemeral nature of Spot VMs.

Spot VMs remain available until Compute Engine requires the resources for standard VMs.

To learn more about Spot VMs, see [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) in the Compute Engine documentation.

## Benefits of Spot VMs

Spot VMs and preemptible VMs share many benefits, including the following:

  * Lower pricing than standard Compute Engine VMs.
  * Useful for stateless, fault-tolerant workloads that are resilient to the ephemeral nature of these VMs.
  * Works with the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) and [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning).



Spot VMs have the following additional benefits:

  * In contrast to preemptible VMs, which expire after 24 hours, Spot VMs have no expiration time. Spot VMs are only preempted when Compute Engine needs the resources elsewhere.
  * With Spot VMs, you can view real-time availability and expected uptime to help you decide where and how to provision resources. For more information, see [View the availability of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability).

**Note:** GKE continues to support using preemptible VMs in your clusters and node pools. However, Spot VMs are recommended and replace the need to use preemptible VMs.

## How Spot VMs work in GKE

When you create a cluster or node pool with Spot VMs, GKE creates underlying Compute Engine Spot VMs that behave like a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups). Nodes that use Spot VMs behave like standard GKE nodes, but with no guarantee of availability. When the resources used by Spot VMs are required to run standard VMs, Compute Engine terminates those Spot VMs to use the resources elsewhere.

When you request Spot Pods, Autopilot automatically provisions Spot VMs, adds taints and tolerations, and manages autoscaling and scheduling.

### Termination and graceful shutdown of Spot VMs

When Compute Engine needs to reclaim the resources used by Spot VMs, a [preemption notice](https://docs.cloud.google.com/compute/docs/instances/spot#preemption) is sent to GKE. After the preemption notice is sent, Compute Engine sends an [ACPI G2 Soft Off](https://en.wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface#Power_states) signal to start the shutdown period for the VM.

By default, GKE clusters have a 30-second graceful termination period for Pods to shut down after the preemption notice is received. This period is split into 15 seconds for your Pods to shut down, after which critical system Pods have 15 seconds to shut down.

You can optionally extend the duration of the graceful termination period to 120 seconds. How you configure this duration depends on whether you create node pools manually or use custom ComputeClasses, as follows:

  * **Standard node pools** : to configure this duration for Standard node pools, your cluster's control plane must run GKE version 1.35.0-gke.1171000 or later. You can extend the duration by customizing the node system configuration to set the values for specific Standard node pools. For more information about the specific fields, see [Graceful termination of Spot VMs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#spot-graceful-termination).

You can configure this duration using any of the following methods:

    * **New Standard node pools** : [provision Spot VMs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/spot-vms#use-spot) during cluster creation or node pool creation using either the Google Cloud console or Google Cloud CLI. The values are stored in the node system configuration.
    * **Existing Standard node pools** : you can update the graceful termination period for existing Standard node pools by updating the node system configuration. For more information, see [Edit by updating an existing node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#editing_by_updating_an_existing_node_pool).
  * **Custom ComputeClasses** : to configure this duration for Spot VMs associated with [custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes), use the `shutdownGracePeriodSeconds` and `shutdownGracePeriodCriticalPodsSeconds` fields in the [`kubeletConfig`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#kubeletConfig) object in the ComputeClass specification. Your cluster's control plane must run GKE version 1.36.0-gke.3204000 or later.




By default, clusters use [graceful node shutdown](https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/#graceful-node-shutdown) over a default period of 30 seconds between the termination notice and shutdown. Regular Pods get 15 seconds to shut down, after which system Pods (with the `system-cluster-critical` or `system-node-critical` priorityClasses) get 15 seconds to shut down. You can extend the grace period by using the following fields:

  * `shutdownGracePeriodSeconds`: extend the total grace period for Pods to 120 seconds, or 0 seconds if you don't require time for graceful termination.
  * `shutdownGracePeriodCriticalPodsSeconds`: extend the grace period for critical system Pods to terminate. This field is valid only if you also specify the `shutdownGracePeriodSeconds` field. The value in this field must be less than the value in the `shutdownGracePeriodSeconds` field. For example, if you specify a value of `30` in the `shutdownGracePeriodCriticalPodsSeconds` field and a value of `120` in the `shutdownGracePeriodSeconds` field, regular Pods get 90 seconds to terminate and system Pods get 30 seconds to terminate.



During graceful termination, if the Pods are part of a managed workload, such as a Deployment, the controller creates and schedules new Pods to replace the terminated Pods. Specifying a value greater than the set graceful termination period in the `terminationGracePeriodSeconds` field of your Pod manifest doesn't extend the graceful termination period. The maximum total grace period that any Pod can get is 120 seconds.

## Scheduling workloads on Spot VMs

GKE automatically adds both the `cloud.google.com/gke-spot=true` and `cloud.google.com/gke-provisioning=spot` (for nodes running GKE version 1.25.5-gke.2500 or later) [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) to nodes that use Spot VMs. You can schedule specific Pods on nodes that use Spot VMs using the [nodeSelector](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) field in your Pod spec. The following examples use the `cloud.google.com/gke-spot` label:
    
    
    apiVersion: v1
    kind: Pod
    spec:
    ** nodeSelector:
        cloud.google.com/gke-spot: "true"**
    

Alternatively, you can use [node affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity) to tell GKE to schedule Pods on Spot VMs, similar to the following example:
    
    
    apiVersion: v1
    kind: Pod
    spec:
    ...
    ** affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: cloud.google.com/gke-spot
                operator: In
                values:
                - "true"**
    ...
    

You can also use `nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution` to _prefer_ that GKE places Pods on nodes that use Spot VMs. Preferring Spot VMs is not recommended, because GKE might schedule the Pods onto existing viable nodes that use standard VMs instead.

**Note:** The cluster autoscaler and node auto-provisioning are unaffected by `preferredDuringSchedulingIgnoredDuringExecution` when making autoscaling decisions.

### Using taints and tolerations for scheduling

To avoid system disruptions, use a [node taint](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to ensure that GKE doesn't schedule critical workloads onto Spot VMs. When you taint nodes that use Spot VMs, GKE only schedules Pods that have the corresponding [toleration](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) onto those nodes.

If you use node taints, ensure that your cluster also has at least one node pool that uses standard Compute Engine VMs. Node pools that use standard VMs provide a reliable place for GKE to schedule critical system components like DNS.

For information on using a node taint for Spot VMs, see [Use taints and tolerations for Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/spot-vms#use_taints_and_tolerations_for).

### Using Spot VMs with GPU node pools

Spot VMs support using [GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus). When you create a new GPU node pool, GKE automatically adds the `nvidia.com/gpu=present:NoSchedule` taint to the new nodes. Only Pods with the corresponding toleration can run on these nodes. GKE automatically adds this toleration to Pods that request GPUs.

Your cluster must have at least one existing non-GPU node pool that uses standard VMs before you create a GPU node pool that uses Spot VMs. If your cluster only has a GPU node pool with Spot VMs, GKE doesn't add the `nvidia.com/gpu=present:NoSchedule` taint to those nodes. As a result, GKE might schedule system workloads onto the GPU node pools with Spot VMs, which can lead to disruptions because of the Spot VMs and can increase your resource consumption because GPU nodes are more expensive than non-GPU nodes.

## Cluster autoscaler and node auto-provisioning

You can use the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler) and [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) to automatically scale your clusters and node pools based on the demands of your workloads. Both the cluster autoscaler and node auto-provisioning support using Spot VMs.

### Spot VMs and node auto-provisioning

Node auto-provisioning automatically creates and deletes node pools in your cluster to meet the demands of your workloads. When you schedule workloads that require Spot VMs by using a `nodeSelector` or node affinity, node auto-provisioning creates new node pools to accommodate the workloads' Pods. GKE automatically adds the `cloud.google.com/gke-spot=true:NoSchedule` taint to nodes in the new node pools. Only Pods with the corresponding toleration can run on nodes in those node pools. You must add the corresponding toleration to your deployments to allow GKE to place the Pods on Spot VMs:
    
    
       tolerations:
       - key: cloud.google.com/gke-spot
         operator: Equal
         value: "true"
         effect: NoSchedule
    

**Caution:** If you do not specify a toleration and your deployment requires Spot VMs, your Pods remain in an unschedulable state.

You can ensure that GKE **only** schedules your Pods on Spot VMs by using **both** a toleration and either a `nodeSelector` or node affinity rule to filter for Spot VMs.

If you schedule a workload using only a toleration, GKE can schedule the Pods onto either Spot VMs or existing standard VMs with capacity. If you require a workload to be scheduled on Spot VMs, use a `nodeSelector` or a node affinity in addition to a toleration. To learn more, see Scheduling workloads on Spot VMs.

### Spot VMs and cluster autoscaler

[Cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) automatically adds and removes nodes in your node pools based on demand. You can configure cluster autoscaler to add new nodes with a preference for Spot VMs. To learn more, see [Spot VMs and cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#spot-vms).

### Default policy

Starting in GKE version 1.24.1-gke.800, you can define the autoscaler location policy. Cluster autoscaler attempts to provision Spot VMs node pools when resources are available and the default location policy is set to `ANY`. With this policy, Spot VMs have a lower risk of being preempted. For other VM types, the default cluster autoscaler distribution policy is `BALANCED`.

## Upgrade Standard node pools using Spot VMs

If your Standard cluster node pools using Spot VMs are configured to use surge upgrades, GKE creates surge nodes with Spot VMs. However, GKE doesn't wait for the Spot VMs to be ready before cordoning and draining the existing nodes, as Spot VMs provide no guarantee of availability. To learn more, see [Surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge).

## Modifications to Kubernetes behavior

Using Spot VMs on GKE modifies some guarantees and constraints that Kubernetes provides, such as the following:

  * Reclamation of Spot VMs is involuntary and is not covered by the guarantees of [`PodDisruptionBudgets`](https://kubernetes.io/docs/tasks/run-application/configure-pdb/). You might experience greater unavailability than your configured `PodDisruptionBudget`.



## Best practices for Spot VMs

When designing a system that uses Spot VMs, you can avoid major disruptions by using the following guidelines:

  * Spot VMs have no availability guarantees. Design your systems under the assumption that GKE might reclaim any or all your Spot VMs at any time, with no guarantee of when new instances become available.
  * Before you create Spot VMs, we recommend that you do the following. These actions help ensure that the machine type that you want your Spot VMs to use is available, as well as that it fits your workload and cost needs. 
    * [View the real-time availability of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability).
    * [View the preemption rate and pricing for Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-spot-preemption-price)
  * To ensure that your workloads and Jobs are processed even when no Spot VMs are available, ensure that your clusters have a mix of node pools that use Spot VMs and node pools that use standard Compute Engine VMs.
  * Ensure that your cluster has at least one non-GPU node pool that uses standard VMs before you add a GPU node pool that uses Spot VMs.
  * While the node names don't usually change when nodes are recreated, the internal and external IP addresses used by Spot VMs might change after recreation.
  * Use node taints and tolerations to ensure that critical Pods aren't scheduled onto node pools that use Spot VMs.
  * To run stateful workloads on Spot VMs, test to ensure that your workloads can gracefully terminate within 25 seconds of shutdown to minimize the risk of persistent volume data corruption.
  * Follow the [Kubernetes Pod termination best practices](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-terminating-with-grace).

**Warning:** Data on nodes that use Spot VMs is deleted when Google Cloud preempts the instance. Local SSD disks that are attached to these VMs don't persist after deletion. We recommend that you use Spot VMs only for fault-tolerant workloads, such as batch processing, stateless applications, or jobs that frequently save their progress.

## What's next

  * [Learn how to use Spot VMs in your node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/spot-vms).
  * [Learn about autoscaling your clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).
  * [Learn how to scale your deployed apps](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/scaling-apps).
  * [Learn more about Spot VMs in the Compute Engine documentation](https://docs.cloud.google.com/compute/docs/instances/spot).
  * [Take a tutorial about deploying a batch workload using Spot VMs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/batch-ml-workload).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
