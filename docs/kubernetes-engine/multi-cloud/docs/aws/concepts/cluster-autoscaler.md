---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/cluster-autoscaler/
title: About cluster autoscaler \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:15:05.784119+00:00
---

# About cluster autoscaler  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/cluster-autoscaler/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  About cluster autoscaler Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the cluster autoscaler, which automatically controls the size of your node pools. The cluster autoscaler is enabled when you specify minimum and maximum values for the number of nodes in a node pool. You specify those values when you [Create a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-node-pool) or [Update a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/update-node-pool).

GKE on AWS uses the open-source Kubernetes cluster autoscaler.

## Autoscale a node pool

The cluster autoscaler automatically resizes the number of nodes in a given node pool, based on the demands of your workloads. You don't need to manually add or remove nodes or over-provision your node pools. Instead, you specify a minimum and maximum size for the node pool, and the rest is automatic.

If resources need to be deleted or moved while autoscaling your cluster, your workloads might experience transient disruption. For example, if your workload consists of a controller with a single replica, that replica's Pod might be rescheduled onto a different node if its current node is deleted. Because of this, you must design your workloads to either tolerate potential disruption or ensure that critical Pods are not interrupted.

**Note:** For autoscaling to function correctly, GKE on AWS deploys the `metrics-server` Deployment with elevated [RBAC permissions](https://kubernetes.io/docs/reference/access-authn-authz/authorization/#determine-the-request-verb) to your nodes, such as the ability to patch and update itself. Additional components, such as `antrea`, `coredns`, and `konnectivity-agent` have specific autoscalers with permissions to scale their component up or down depending on need.

## How the cluster autoscaler works

The cluster autoscaler works on a per-node pool basis. When you use the cluster autoscaler to configure a node pool, you specify a minimum and maximum size for the node pool. You can change the minimum and maximum size when you [Create a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-node-pool) or [Update a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/update-node-pool).

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

You can configure GKE on AWS to protect against workload disruption with a `PodDisruptionBudget`. When you create a `PodDisruptionBudget`, you specify the minimum number of Pod replicas that should be available, or the maximum number of Pod replicas that can be unavailable at any given time. For more information, see [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb/).

## Scale up from zero nodes

Starting with the following GKE on AWS versions, the cluster autoscaler supports scaling up node pools from zero nodes:

  * Version 1.29 and later
  * Versions of 1.28 from 1.28.8-gke.800 and later
  * Versions of 1.27 from 1.27.12-gke.800 and later



If you're using an earlier version, you need to upgrade your cluster to one of these versions to use this feature. To enable this feature for existing clusters, update your cluster to a supported version, and then perform a rolling update of your node pools by updating their Kubernetes version. For more information about updating your node pools, see [Update a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/update-node-pool).

The cluster autoscaler honors labels and taints you define on node pools when making scaling decisions, even when no nodes are available for reference. GKE on AWS automatically sets the necessary label and taint tags on the node pool's underlying [AWS Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html). For more information about these tags, see the [Auto-Discovery Setup](https://github.com/kubernetes/autoscaler/blob/df0ce2d99ab23b631b87a272eac7c2c552c198dc/cluster-autoscaler/cloudprovider/aws/README.md#auto-discovery-setup) section of the GitHub page describing cluster autoscaler configuration for AWS.

By setting these label and taint tags, GKE on AWS enables the cluster autoscaler to create accurate node templates. Node templates are virtual representations of nodes that include the correct node configuration, labels, and taints, even when there are no physical nodes present in the node pool. As a result of having these accurate node templates, the cluster autoscaler can make correct scale-up decisions.

When configuring taints on your node pools, be aware that AWS Auto Scaling groups have a limitation: if you apply multiple taints with the same key but different value-effect combinations, only the last applied taint with the duplicated key is considered by the cluster autoscaler.

## More information

To learn more about the cluster autoscaler and how to prevent disruptions, see the following resources:

  * [Kubernetes cluster autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md)
  * [How does scale-down work?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-does-scale-down-work)
  * [Does Cluster autoscaler work with `PodDisruptionBudget` in scale-down?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#does-ca-work-with-poddisruptionbudget-in-scale-down)



## What's next

  * [Create a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-node-pool).
  * [Update a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/update-node-pool).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
