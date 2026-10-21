---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/cluster-autoscaler/
title: Cluster autoscaler \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:55.443453+00:00
---

# Cluster autoscaler  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/cluster-autoscaler/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Cluster autoscaler Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/concepts/cluster-autoscaler)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/concepts/cluster-autoscaler)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



In Google Distributed Cloud version 1.10, cluster autoscaling for node pools in user clusters is GA. Cluster autoscaling resizes the number of nodes in a given node pool based on the demands of your workloads. You don't need to manually add or remove nodes, or over-provision your node pools. Instead, you specify a minimum and maximum size for the node pool, and the rest is automatic.

If resources are deleted or moved when autoscaling your cluster, your workloads might experience transient disruption. For example, if your workload is a single Pod, and its current node is deleted, the Pod is rescheduled onto a different node. Before you enable autoscaling, design your workloads to tolerate potential disruptions and to ensure that critical Pods are not interrupted.

Cluster autoscaling is disabled by default for node pools. You can enable and disable autoscaling on user cluster node pools either during cluster creation, or after cluster creation, using the `gkectl update` command.

## How cluster autoscaling works

The cluster autoscaler works on a per-node pool basis. When you configure a node pool with the cluster autoscaler, you specify a minimum and maximum size for the node pool.

The cluster autoscaler increases or decreases the size of the node pool automatically, based on the resource requests (rather than actual resource utilization) of Pods running on that node pool's nodes. It periodically checks the status of Pods and nodes, and takes action:

  * If Pods are unschedulable because there are not enough nodes in the node pool, cluster autoscaler adds nodes, up to the maximum size of the node pool.
  * If nodes are under-utilized, and all Pods could be scheduled even with fewer nodes in the node pool, the cluster autoscaler removes nodes, down to the minimum size of the node pool. If the node cannot be drained gracefully, the node is forcibly terminated and the attached Kubernetes-managed disk is safely detached.



If your Pods have requested too few resources (or haven't changed the defaults, which might be insufficient) and your nodes are experiencing shortages, the cluster autoscaler does not correct that situation. You can help ensure cluster autoscaler works as accurately as possible by making explicit resource requests for all of your workloads.

## Operating criteria

Cluster autoscaler makes the following assumptions when resizing a node pool:

  * All replicated Pods can be restarted on some other node, which might cause a brief disruption. If your services cannot tolerate disruption, using the cluster autoscaler is not recommended.
  * Users or administrators do not manually manage nodes. If the cluster autoscaler is turned on for a node pool, you cannot override the `replicas` field of the node pool.
  * All nodes in a single node pool have the same set of labels. 
  * The cluster autoscaler considers the relative cost of the instance types in the various node pools, and attempts to expand the node pool in a way that causes the least waste possible.



## Minimum and maximum node pool size

You can specify the minimum and maximum size for each node pool in your cluster with the `autoscaling.minReplicas` and `autoscaling.maxReplicas` values. The cluster autoscaler makes rescaling decisions within these boundaries. The node pool's `replicas` value, which is the default number of nodes without autoscaling, should be greater than the specified `minReplicas` value, and less than the specified `maxReplicas` value. When you enable autoscaling, the cluster autoscaler waits to take effect until a new node is needed in the node pool, or until a node can be safely deleted from the node pool.

### Considering Pod scheduling and disruption

When scaling down, the cluster autoscaler respects scheduling and eviction rules set on Pods. These restrictions can prevent a node from being deleted by the autoscaler. If a node has a Pod with any of the following conditions, it might not get deleted.

  * The Pod's [affinity or anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) rules prevent rescheduling.
  * The Pod has local storage.
  * The Pod is not managed by a [controller](https://kubernetes.io/docs/concepts/workloads/pods/#pods-and-controllers) such as a Deployment, StatefulSet, Job, or ReplicaSet.
  * The Pod is in kube-system namespace and does not have a [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#how-disruption-budgets-work).



An application's PodDisruptionBudget can also prevent autoscaling. If deleting nodes would cause the budget to be exceeded, the cluster does not scale down.

For more information about cluster autoscaler and preventing disruptions, see the following questions in the [Cluster autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md):

  * [How does scale-down work?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-does-scale-down-work)
  * [Does Cluster autoscaler work with PodDisruptionBudget in scale-down?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#does-ca-work-with-poddisruptionbudget-in-scale-down)
  * [What types of Pods can prevent Cluster autoscaler from removing a node?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-types-of-pods-can-prevent-ca-from-removing-a-node)



## Limitations

Cluster autoscaler has the following limitations:

  * Scaling down to zero replicas in the node pool is not allowed.
  * The sum of the user cluster worker nodes at any given time must be at least 3. This means the sum of the `minReplicas` values for all autoscaled node pools, plus the sum of the `replicas` values for all non-autoscaled node pools, must be at least 3.
  * Occasionally, the cluster autoscaler cannot scale down completely and an extra node exists after scaling down. This can occur when required system Pods are scheduled onto different nodes, because there is no trigger for any of those Pods to be moved to a different node. See [I have a couple of nodes with low utilization, but they are not scaled down. Why?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#i-have-a-couple-of-nodes-with-low-utilization-but-they-are-not-scaled-down-why). To work around this limitation, you can configure a [Pod disruption budget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/).
  * Custom scheduling with altered [filters](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/#filter) is not supported.
  * Nodes do not scale up if Pods have a [`PriorityClass`](https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/#priorityclass) value below `-10`. Learn more in [How does Cluster Autoscaler work with Pod Priority and Preemption?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-does-cluster-autoscaler-work-with-pod-priority-and-preemption)
  * Auto-scaling for Windows node pools is not supported.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
