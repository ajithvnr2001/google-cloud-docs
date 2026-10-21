---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/cluster-autoscaler/
title: About cluster autoscaler \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:51.692414+00:00
---

# About cluster autoscaler  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/cluster-autoscaler/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About cluster autoscaler

This document describes the cluster autoscaler, which automatically controls the size of your node pools. The cluster autoscaler is enabled when you specify minimum and maximum values for the number of nodes in a node pool. You specify those values when you [Create a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-node-pool) or [Update a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/update-node-pool).

GKE on Azure uses the open-source Kubernetes cluster autoscaler.

## Autoscale a node pool

The cluster autoscaler automatically resizes the number of nodes in a given node pool, based on the demands of your workloads. You don't need to manually add or remove nodes or over-provision your node pools. Instead, you specify a minimum and maximum size for the node pool, and the rest is automatic.

If resources need to be deleted or moved while autoscaling your cluster, your workloads might experience transient disruption. For example, if your workload consists of a controller with a single replica, that replica's Pod might be rescheduled onto a different node if its current node is deleted. Because of this, you must design your workloads to either tolerate potential disruption or ensure that critical Pods are not interrupted.

**Note:** For autoscaling to function correctly, GKE on Azure deploys the `metrics-server` Deployment with elevated [RBAC permissions](https://kubernetes.io/docs/reference/access-authn-authz/authorization/#determine-the-request-verb) to your nodes, such as the ability to patch and update itself. Additional components, such as `antrea`, `coredns`, and `konnectivity-agent` have specific autoscalers with permissions to scale their component up or down depending on need.

## How the cluster autoscaler works

The cluster autoscaler works on a per-node pool basis. When you use the cluster autoscaler to configure a node pool, you specify a minimum and maximum size for the node pool. You can change the minimum and maximum size when you [Create a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-node-pool) or [Update a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/update-node-pool).

The cluster autoscaler increases or decreases the size of the node pool automatically, based on the resource requests (rather than actual resource utilization) in that node pool. The cluster autoscaler adds nodes if Pod objects are unschedulable and there is not enough capacity in the node pool to meet requests.

The cluster autoscaler also removes nodes if they are underutilized and all Pod objects could be scheduled on a smaller number of nodes. If the node cannot be drained gracefully after 10 minutes, the node is forcibly terminated. This period is not configurable.

If a Pod requests too few resources (for example, if the defaults are insufficient), the cluster autoscaler does not correct the situation. You can help ensure that the cluster autoscaler works as accurately as possible by creating adequate resource requests for all of your workloads. For more information, see [Managing resources for containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).

## Pod annotations and cluster autoscaler behavior

The cluster autoscaler considers certain Pod annotations when making scaling decisions. For example, the cluster autoscaler supports Pod annotations such as `"cluster-autoscaler.kubernetes.io/safe-to-evict": "false"`. This annotation, when set to "false", prevents the Node hosting the Pod from being removed during a scale-down event. Understanding and using these annotations can help you fine-tune the autoscaler's behavior to meet your workload requirements.

For more information about Pod annotations and their effects on the cluster autoscaler, see the following resources:

  * [What types of pods can prevent CA from removing a node?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-types-of-pods-can-prevent-ca-from-removing-a-node) in the cluster autoscaler FAQ.
  * [Official Kubernetes Cluster Autoscaler documentation](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler#cluster-autoscaler)



## Operating criteria

The cluster autoscaler makes the following assumptions when resizing a node pool:

  * All replicated Pod objects can be restarted on some other node, possibly causing a brief disruption. If your workload doesn't tolerate disruption, configure the workload to run on a node pool with autoscaling disabled. For more information, see [Controlling scheduling with node taints](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-taints).
  * The cluster autoscaler can override any manual node management operations that you perform.
  * All nodes in a single node pool have the same set of labels.
  * The cluster autoscaler selects a node group that has the least idle CPU or unused memory after scaling up. This behavior affects which node pools are scaled up if you have different sizes of nodes (for example, high CPU or high memory nodes) in the same cluster.



## Minimum and maximum node pool size

You can specify the minimum and maximum size for each node pool in your cluster with the `min-nodes` and `max-nodes` flags. To disable auto scaling, set `min-nodes` and `max-nodes` to the same number. The cluster autoscaler makes scaling decisions within these size boundaries.

When you set the maximum size of your node pools, make sure that it is large enough to run all of your workloads. If the node pools in your cluster don't have enough memory and CPU available to run all of your workloads, outages might occur.

## Use a `PodDisruptionBudget` to protect workloads

You can configure GKE on Azure to protect against workload disruption with a `PodDisruptionBudget`. When you create a `PodDisruptionBudget`, you specify the minimum number of Pod replicas that should be available, or the maximum number of Pod replicas that can be unavailable at any given time. For more information, see [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb/).

## More information

To learn more about the cluster autoscaler and how to prevent disruptions, see the following resources:

  * [Kubernetes cluster autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md)
  * [How does scale-down work?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-does-scale-down-work)
  * [Does Cluster autoscaler work with `PodDisruptionBudget` in scale-down?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#does-ca-work-with-poddisruptionbudget-in-scale-down)



## What's next

  * [Create a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-node-pool).
  * [Update a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/update-node-pool).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
