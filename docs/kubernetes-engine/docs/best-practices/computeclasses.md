---
url: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/computeclasses/
title: Best practices for ComputeClasses \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:09.004510+00:00
---

# Best practices for ComputeClasses  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/computeclasses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Best practices for ComputeClasses Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Platform engineers can use custom [ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes) to declaratively configure node settings and fallback priorities that Google Kubernetes Engine (GKE) uses to create nodes during autoscaling. You can create ComputeClasses based on specific strategies and workload requirements. This document provides best practices for designing and implementing ComputeClasses in your clusters. You should already be familiar with [custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes). For a consolidated overview of all GKE best practices, see [Best practices for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices). 

## ComputeClass design

The following sections provide best practices for designing and implementing ComputeClasses in your clusters based on goals like maximizing the flexibility, efficiency, availability, and performance of compute capacity. ComputeClasses work with both manually created and auto-created node pools.

### Design each ComputeClass based on a strategy

Design each ComputeClass to meet a specific goal for your workloads, teams, or organization. Use the fallback behavior of ComputeClasses and the ability to select both manually created and auto-created node pools to prioritize certain outcomes, such as reducing manual overhead or improving scheduling performance. The following sections describe common strategies.

#### Improve resource availability and reduce manual overhead

To delegate node pool creation to GKE, use only auto-created node pools in your ComputeClass. The autoscaler configures nodes based on hardware availability, Pod resource requirements, and zonal capacity. This strategy eliminates the need to manually create and tune node pools and can reduce the costs that are associated with idle, unused node capacity.

#### Improve scheduling performance and fine-tune nodes

To fine-tune your highest-priority nodes and reduce scheduling latency, use a mix of manually created and auto-created node pools in your ComputeClass. This hybrid strategy reduces how often Pods wait for GKE to create new node pools. Because your highest-priority node pools are manually created, you can fine-tune the hardware to meet the exact requirements of your Pods.

The hybrid strategy involves the following types of node pools in order of priority in the ComputeClass:

  1. **Manually created node pools** : these node pools have the exact specifications that you want most of your Pods to run on. Configure these node pools with specific node labels, node taints, capacity reservations, or special configurations such as `kubelet` parameters. Create these node pools with as many nodes as you estimate your Pods will need. In your ComputeClass, assign the highest priority to these node pools.
  2. **Auto-created node pools** : as a fallback measure, use the ComputeClass to request additional node pools that are still optimized for your Pods. Assign a lower priority to these auto-created node pools than for your manually created node pools.



The following example ComputeClass uses this hybrid strategy:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: hybrid-class
    spec:
      nodePoolAutoCreation:
        enabled: true
      priorities:
      - nodepools: ['manual-pool1']
      - machineFamily: n4
        minCores: 16
        minMemoryGb: 64
      whenUnsatisfiable: DoNotScaleUp
    

When you deploy a workload that uses this ComputeClass, GKE places Pods on available nodes in `manual-pool1`. GKE creates new node pools only when the manually created node pool has no available capacity. The scheduling latency decreases when the number of existing nodes in the manually created node pool increases, because GKE doesn't need to create new nodes as frequently.

### Explicitly define the last-resort scaling behavior

The `whenUnsatisfiable` field controls what happens if GKE can't meet the requirements of any of the priority rules in a ComputeClass. To avoid unexpected behavior after a version upgrade, explicitly specify a value for this field in every ComputeClass. Setting a value helps ComputeClass users to know what to expect when they select that ComputeClass in a workload. The recommended value for this field depends on the type of workload, as follows:

  * **General-purpose workloads** : if your workloads can run on any machine series, then specify a value of `ScaleUpAnyway`. If nodes that match a priority rule in the ComputeClass aren't available, GKE scales up nodes that use the default machine series of the cluster.
  * **Workloads that need specialized hardware** : for accelerators or high performance computing workloads that depend on specific hardware, such as GPUs or certain Compute Engine machine series, specify a value of `DoNotScaleUp`. If nodes that match a priority rule in the ComputeClass aren't available, the Pods remain in a `Pending` state until resources become available. This approach prevents Pods from running on incompatible hardware.



For more information, see [Define scaling behavior when no priority rules apply](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#define-scaling-no-rules).

### Set a cluster-level default ComputeClass for most workloads

If most of your workloads have the same hardware requirements, then [configure a default ComputeClass for the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-pods-default-compute-classes#cluster-default-computeclass). GKE applies the default ComputeClass to any workloads that don't explicitly select a ComputeClass. By setting a default ComputeClass, application operators don't need to change node selectors or manually request specific node pools and hardware in individual Pods. If you set a cluster-level default ComputeClass, then don't add node labels and taints for other ComputeClasses to existing node pools in the cluster. During scheduling for the cluster-level default ComputeClass, GKE ignores any node pools that have node labels or node taints for other ComputeClasses.

### Set default ComputeClasses for namespaces to separate tenants

In addition to a cluster-level default ComputeClass, you can [set a default ComputeClass for specific namespaces](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-pods-default-compute-classes#namespace-default-computeclass). If you have multi-tenant environments or you want to separate workloads that run on specialized hardware, then configure default ComputeClasses for those namespaces. To prevent system Pods from running on specialized hardware like GPU nodes, add a general-purpose ComputeClass as the default ComputeClass for system namespaces.

### Run low-interaction workloads in Autopilot mode

If you have workloads that don't require manual interaction or management, then run those workloads in Autopilot mode by using ComputeClasses. You can enable Autopilot mode in any ComputeClass even when you have a Standard cluster. GKE runs the workloads that select an Autopilot ComputeClass on fully managed nodes that implement the security, scaling, and billing features of GKE Autopilot. For more information, see [About Autopilot mode workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters).

## Stateful workloads

The following sections provide best practices for reducing disruptions or unexpected behavior in stateful workloads that rely on persistent data.

### Disable active migration

[Active migration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#active-migration) automatically moves Pods to new nodes that have a higher priority in the ComputeClass or have the capacity to run unscheduled DaemonSet Pods. During active migration, GKE terminates Pods on existing nodes and creates new Pods on higher-priority nodes. If you have workloads that rely on data in local persistent storage, moving the Pods to new nodes might cause disruptions because the Pods lose access to persistent data. To avoid this issue, disable active migration for ComputeClasses that are intended for stateful workloads.

### Improve scheduling reliability by using StorageClasses

Use StorageClasses to improve scheduling reliability for stateful workloads in the following ways:

  * **Create volumes only after Pod creation** : if you use dynamic volume provisioning, then specify a value of [`WaitForFirstConsumer` in the `volumeBindingMode` field](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#waitforfirstconsumer) in a StorageClass. This volume binding mode prevents the creation of a PersistentVolume until after GKE creates a Pod that uses the corresponding PersistentVolumeClaim. GKE provisions the PersistentVolume in the same zone as the node that runs the Pod.
  * **Use topology-aware StorageClasses:** if your ComputeClass spans multiple generations of machine series, use a StorageClass that has [automatic disk type selection](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk#automated_disk_type_selection) (`parameters.type: dynamic`) enabled and that schedules only on nodes that support your specified disk types. For example, your ComputeClass falls back from Hyperdisk-only series such as C4, C4D, or N4 to Persistent Disk series such as N2 or N2D during zonal capacity constraints. You can use the built-in `dynamic-rwo` StorageClass or a custom StorageClass. Your stateful workloads can then fail over across multiple Compute Engine instance generations, because the cluster autoscaler dynamically chooses a compatible disk type (`hyperdisk-balanced` or `pd-balanced`) for whichever fallback node is provisioned.



## Design your infrastructure for flexibility, efficiency, and availability of compute capacity

The following sections provide best practices for improving flexibility, efficiency, and availability of compute capacity in ComputeClasses, so that your Pods spend less time in a `Pending` state.

### Request machine series instead of machine types

You can request a Compute Engine machine series or specific machine types in ComputeClass priority rules. Unless you have a strict dependency on a specific machine type, select a machine series by using the [`machineFamily` field](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#machinefamily-rule). During a scaling operation, GKE can create nodes that use any viable machine type in that machine series, which improves the likelihood of your Pods running on your most preferred node configuration.

### Use capacity reservations for in-demand hardware

If your workloads rely on in-demand hardware, such as TPUs or high-performance GPUs, then create Compute Engine capacity reservations for the hardware and consume those reservations in your ComputeClasses. Capacity reservations improve the likelihood of hardware being available in your region or zone, which helps you to increase flexibility, efficiency, and availability of compute capacity. To consume a reservation in a ComputeClass without affecting fallback behavior, use the `Specific` or `AnyThenFail` reservation affinity. If you use the `AnyBestEffort` or `Automatic` affinity and there's no available reserved capacity, then Compute Engine might bypass the ComputeClass priority rules and fall back to on-demand hardware. For more information, see [Consuming reserved zonal resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations).

### Don't consume new reservations for at least one hour

The cluster autoscaler stores information about capacity reservations in a cache. When you create a new capacity reservation, the autoscaler might take up to one hour to discover that reservation. After you create a reservation, wait for at least one hour before you consume that reservation in a workload. If you deploy a workload that uses the reservation before the autoscaler stores the reservation in the cache, then the autoscaling operation might fail.

## Security

The following sections provide best practices for improving the security of the ComputeClasses in your clusters. These measures are important because ComputeClasses can be used to create and configure nodes that use hardware that's expensive or has limited availability. Intentional or accidental misuse might result in workload disruptions, unplanned resource usage charges, and quota exhaustion.

### Restrict API access to ComputeClass configurations

Workloads can use ComputeClasses to create nodes that run specialized hardware, including GPUs and TPUs. Restrict the access to create, modify, and delete ComputeClasses to the same principals who can create, modify, and delete nodes in your clusters. To control access to ComputeClasses, [use RBAC policies](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/restrict-computeclass-usage-admission#configure-rbac).

### Restrict ComputeClass availability by namespace

GKE customers often separate different teams or workload types by Kubernetes namespace. ComputeClasses are a cluster-scoped resource, which means that any workload in any namespace can select any ComputeClass by default. To avoid intentional or accidental misuse, use ValidatingAdmissionPolicies to control the set of ComputeClasses that workloads in each namespace can select. For example, you might prevent Pods in your web frontend namespace from being able to select ComputeClasses that create accelerators. Verify that your ValidatingAdmissionPolicies check for the following common configurations:

  * **Check all selection fields:** a workload can select a ComputeClass by using the `nodeSelector`, `nodeAffinity`, or `tolerations` field in the Pod specification. To avoid unintended ComputeClass selection, check all of these fields in your ValidatingAdmissionPolicy expressions.
  * **Check for wildcard toleration bypasses:** explicitly block or validate wildcard tolerations (for example, the `operator: Exists` toleration with no key). These wildcard selectors can encompass most node taints, including ComputeClass taints.
  * **Check all workload controllers:** configure the policy's `matchConstraints` to cover all workload controller resources (such as `Deployment`, `StatefulSet`, `DaemonSet`, `Job`, and `CronJob`). Don't scope your checks to only `Pod` resources.



For more information, see [Restrict access to modify and select ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/restrict-computeclass-usage-admission#create-validatingadmissionpolicy).

## Reliability

The following sections provide best practices for improving the reliability of autoscaling and Pod migration for ComputeClasses, which reduces the risk of disruptions or stuck Pods.

### Prevent the use of conflicting node selectors

Node selectors in your Pods affect where GKE places those Pods and, in Autopilot mode or with node pool auto-creation, might trigger the creation of new node pools in your cluster. If you have Pods that select a ComputeClass and use node selectors to request nodes that conflict with the ComputeClass configuration, then GKE might not schedule the Pods at all.

For example, consider a ComputeClass that requests only on-demand instances. If a Pod selects that ComputeClass and selects Spot VMs in a node selector, GKE can't schedule the Pod because the ComputeClass and node selector conflict with each other. To avoid this issue, use methods like ValidatingAdmissionPolicies to prevent Pods that select ComputeClasses from also selecting system node labels. For more information, see [Node selectors for system node labels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#system-label-selectors).

### Test all changes to active migration and autoscaling settings

The active migration and autoscaling settings in a ComputeClass directly affect how frequently GKE terminates your Pods to perform tasks like moving Pods to more preferred hardware and consolidating underutilized nodes. Modifications to these settings in an existing ComputeClass might result in unexpected workload disruptions. Before you apply any modifications to these settings in existing ComputeClasses, test the changes in a staging environment. You can also use annotations to protect critical workloads from eviction during scaling.

### Test ComputeClass CRD updates before cluster upgrades

GKE regularly updates the ComputeClass CustomResourceDefinition (CRD) to add fields, modify field behavior, and fix issues. Field additions and modifications typically become effective in specific GKE versions. Before you upgrade your production clusters to new minor versions or patch versions, check whether changes to the CRD cause workload issues by using the following guidelines:

  * Test the upgrade in a staging environment.
  * Check the [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) for changes or additions to the ComputeClass CRD.
  * Check the [ComputeClass CRD reference page](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass) for field updates in your target upgrade version.



### Use PodDisruptionBudgets to improve workload availability

ComputeClass operations that cause Pod evictions, such as active migration, respect any configured [PodDisruptionBudgets](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#pod-disruption-budgets). For example, you can configure an inference Deployment to have a PodDisruptionBudget that requires more than 70% of the Pods to be available. During active migration, if a Pod eviction violates that budget, then GKE doesn't evict the Pod. Specify PodDisruptionBudgets for workloads like the following:

  * Stateless workloads, such as inference Deployments.
  * Replicated stateful workloads, such as highly-available database applications.



Don't rely on PodDisruptionBudgets to protect workloads that need to run to completion, have only one instance, or rely on local persistent data. Specify a budget that balances between workload availability and allows functions like upgrades to complete.

### Protect critical workloads from eviction

If you have workloads where each Pod must run to completion before being terminated, then add the `cluster-autoscaler.kubernetes.io/safe-to-evict: "false"` annotation to the Pod specification. This annotation prevents GKE from evicting Pods during autoscaling operations. Use this annotation to protect Pods that can't tolerate disruptions, such as single-instance stateful workloads and long-running batch Jobs.

## Summary of best practices

This document has the following best practices for ComputeClasses:

Design each ComputeClass based on a strategy

Explicitly define the last-resort scaling behavior

Set a cluster-level default ComputeClass for most workloads

Set default ComputeClasses for namespaces to separate tenants

Run low-interaction workloads in Autopilot mode

Disable active migration

Improve scheduling reliability by using StorageClasses

Request machine series instead of machine types

Use capacity reservations for in-demand hardware

Don't consume new reservations for at least one hour

Restrict API access to ComputeClass configurations

Restrict ComputeClass availability by namespace

Prevent the use of conflicting node selectors

Test all changes to active migration and autoscaling settings

Test ComputeClass CRD updates before cluster upgrades

Use PodDisruptionBudgets to improve workload availability

Protect critical workloads from eviction

## What's next

  * View the other [best practices for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices).
  * Learn how to [create a ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-attributes-compute-classes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
