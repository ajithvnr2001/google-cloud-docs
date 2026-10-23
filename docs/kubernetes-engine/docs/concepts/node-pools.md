---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools/
title: About node pools \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:22.052700+00:00
---

# About node pools  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About node pools Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how node pools work in Google Kubernetes Engine (GKE). A _node pool_ is a group of [nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes) within a Standard cluster that all have the same configuration. In GKE Standard mode, you can choose from a number of options for your node pools to meet your workload needs. If you choose to use Autopilot, you don't need to configure node pools: GKE manages the nodes for you, although you can manually upgrade Autopilot-managed node pools in Standard clusters if needed.

To learn more about creating Standard mode clusters, see [Create a regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster) and [Create a zonal cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster). To learn how to manage node pools in existing Standard clusters, see [Adding and managing node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools).

## Overview

A node pool is a group of [nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes) within a cluster that all have the same configuration. Node pools use a [NodeConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig) specification. Each node in the pool has a Kubernetes node label, `cloud.google.com/gke-nodepool`, which has the node pool's name as its value.

When you create a Standard mode [cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture), the number of nodes and type of nodes that you specify are used to create the first node pool of the cluster. By default, this first node pool (known as the _default node pool_) consists of three nodes in each of the cluster's compute zones, with the default [node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images) `cos_containerd`, and a general-purpose [machine type](https://docs.cloud.google.com/compute/docs/machine-types). You can specify a variety of properties for the node pool, depending on your workload requirements. For example, you might create a node pool in your cluster with [local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd), a [minimum CPU platform](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/min-cpu-platform), [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms), a different node image, different [machine types](https://docs.cloud.google.com/compute/docs/machine-types), or a more efficient [virtual network interface](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-gvnic).

You can then add additional node pools of different sizes and types to your cluster. All nodes in any given node pool are identical to one another.

Custom node pools are useful when you need to schedule Pods that require more resources than others, such as more memory or more local disk space. If you need more control of where Pods are scheduled, you can use [node taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).

You can [create, upgrade, and delete node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools) individually without affecting the whole cluster. You cannot configure a single node in a node pool; any configuration changes affect all nodes in the node pool.

You can resize node pools in a cluster by [adding or removing nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#resizing_a_node_pool).

By default, all new node pools run the same version of Kubernetes as the control plane. Existing node pools can be [manually upgraded](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster#manually_upgrading_your_nodes) or [automatically upgraded](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-upgrade). You can also run multiple Kubernetes node versions on each node pool in your cluster, upgrade each node pool independently, and target different node pools for specific deployments.

### Autopilot-managed node pools

In Standard clusters, in addition to the Standard node pools described in this document, you can also have Autopilot-managed node pools, which are created and managed by GKE for Autopilot ComputeClasses. For more information, see [About Autopilot mode workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters).

You can [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_nodes) this type of node pool. However, you can't perform [other types of updates](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#upgrades-updates) beyond upgrades (version changes). You also can't delete the node pool.

## Deploying Services to specific node pools

When you define a [Service](https://kubernetes.io/docs/concepts/services-networking/service/), you can indirectly control which node pool it is deployed into. The node pool is _not_ dependent on the configuration of the Service, but on the configuration of the [Pod](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod).

  * You can explicitly deploy a Pod to a specific node pool by setting a [`nodeSelector`](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) in the Pod manifest. This forces a Pod to run only on nodes in that node pool. For an example see, [Deploying a Pod to a specific node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#deploy).

  * You can [specify resource requests for the containers](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/). The Pod only runs on nodes that satisfy the resource requests. For example, if the Pod definition includes a container that requires four CPUs, the Service does not select Pods running on nodes with two CPUs.




## Nodes in multi-zonal clusters

If you created a [multi-zonal](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#multi-zonal_clusters) cluster, all of the node pools are replicated to those zones automatically. Any new node pool is automatically created in those zones. Similarly, any deletions delete those node pools from the additional zones as well.

Note that because of this multiplicative effect, this may consume more of your project's [quota](https://docs.cloud.google.com/kubernetes-engine/quotas) for a specific region when creating node pools.

## Deleting node pools

When you [delete a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#deleting_a_node_pool), GKE drains all the nodes in the node pool, deleting and rescheduling all Pods. The draining process involves GKE deleting Pods on each node in the node pool. GKE does both of the following when deleting nodes:

  * GKE drains each node in a node pool by deleting Pods with an allotted graceful termination period of `MAX_POD`. `MAX_POD` is the maximum [`terminationGracePeriodSeconds`](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination) set on the Pods scheduled on the node, with a cap of one hour.
  * GKE, by default, doesn't honor [`PodDisruptionBudget`](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) (PDB) settings during node pool deletion. However, you can update the configuration of the node pool to have GKE respect PDBs during node pool deletion, also with a cap of one hour. Respecting PDBs gives workloads the opportunity to move to other nodes in the cluster. For more information about configuring this setting, see [Update a node pool to respect PDBs during node pool deletion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#respect-pdb-delete).



If the Pods have specific node selectors, the Pods might remain in an unschedulable condition if no other node in the cluster satisfies the criteria.

**Warning:** Essential `kube-system` Pods, such as `kube-dns` and `konnectivity-agent`, must be schedulable to maintain GKE cluster stability. Before you delete the default node pool or apply restrictive taints to all node pools, ensure that at least one node pool remains available to host these critical system Pods. We recommend maintaining at least one node pool without custom `NoSchedule` or `NoExecute` taints. Failure to schedule `kube-system` Pods can cause severe cluster disruptions, including DNS resolution failures and control plane communication problems.

When a cluster is deleted, GKE does not follow this process of gracefully terminating the nodes by draining them. If the workloads running on a cluster must be gracefully terminated, use [`kubectl drain`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#drain) to clean up the workloads before you delete the cluster.

To delete a node pool, see [Delete a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#deleting_a_node_pool). You can't delete Autopilot-managed node pools.

## What's next

  * [Learn about the cluster architecture in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture). 
    * [Learn how to add and manage node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools).
  * [Learn how to auto-provision nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
