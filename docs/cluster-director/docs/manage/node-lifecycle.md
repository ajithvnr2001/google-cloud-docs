---
url: https://docs.cloud.google.com/cluster-director/docs/manage/node-lifecycle/
title: Node lifecycle \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:00.777394+00:00
---

# Node lifecycle  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/manage/node-lifecycle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Node lifecycle Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the lifecycle of a cluster node in Cluster Director.

A node in a cluster transitions through various states from its creation to its deletion. Understanding these states lets you do the following:

  * **Manage resources and costs** : understand when Cluster Director provisions and stops dynamic nodes to run queued jobs and reduce unnecessary charges.

  * **Minimize disruptions** : anticipate planned host maintenance events.

  * **Troubleshoot errors** : identify why a node fails to boot, restart, or resume.




To check the current state of a node, [view the details of your cluster](https://docs.cloud.google.com/cluster-director/docs/manage/view-clusters#describe).

## Node states

The following diagram shows the different states that Cluster Director can set a node to:

[ ![A flowchart of the different states that a node can go through in Cluster Director.](https://docs.cloud.google.com/static/cluster-director/images/node-states-lifecycle.png)](https://docs.cloud.google.com/static/cluster-director/images/node-states-lifecycle.png)

The states shown in the preceding diagram are as follows:

  * Unprovisioned state

  * Creating state

  * Active state

  * Suspending state

  * Suspended state

  * Repairing state

  * Failed state

  * Deleting state




### Unprovisioned state

When Cluster Director creates a dynamic node, the node starts in the `UNPROVISIONED` state. From this state, a dynamic node can transition to one of the following states:

  * **`CREATING`** : when you submit a job that requires more compute resources than the ones in your static nodes, Cluster Director attempts to allocate resources to create the dynamic node.

  * **`DELETING`** : when you reduce the dynamic node count in the cluster by modifying or deleting it, the delete operation for the node starts.




### Creating state

When a node is in the `CREATING` state, Cluster Director attempts to allocate resources to boot, restart, or resume your node.

From this state, the node can transition to one of the following states:

  * **`ACTIVE`** : when Cluster Director allocates resources for your node, the node boots up and starts running.

  * **`FAILED`** : the node encounters a host error.




### Active state

When a node is in the `ACTIVE` state, the node is healthy, running, and ready to run Slurm jobs.

From this state, the node can transition to one of the following states:

  * **`SUSPENDING`** : you stop or suspend the node.

  * **`REPAIRING`** : planned or unplanned host maintenance for the node starts.

  * **`UNPROVISIONED`** : Slurm deletes the node after it has been in the `idle` state for some time, or Cluster Director deletes the node after you reduce the number of dynamic nodes in the cluster.

  * **`DELETING`** : a delete operation starts after one of the following occurs:

    * The reservation that you used to create the node has reached its end time. Cluster Director deletes the node if it was created by using the reserved resources for a future reservation in calendar mode, or if you configured the node to be deleted when the reservation reaches its end time.

    * You manually delete the node.

    * You reduce the static node count (`staticNodeCount`) or maximum dynamic node count (`maxDynamicNodeCount`) in a nodeset.

    * You delete the cluster.

  * **`FAILED`** : the node encounters a host error.




### Suspending state

When a node is in the `SUSPENDING` state, Cluster Director is stopping or suspending the node. You can only suspend nodes that use N2 machine types. For more information, see [Suspend, stop, or reset Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview).

From this state, when the stop or suspend operation completes, the node transitions to the `SUSPENDED` state.

### Suspended state

When a node is in the `SUSPENDED` state, the stop or suspend operation completes.

From this state, the node transitions to one of the following states:

  * **`CREATING`** : when you resume or restart the node.

  * **`DELETING`** : when you delete the node or the cluster.




### Repairing state

When a node is in the `REPAIRING` state, Cluster Director stops the node to perform host maintenance on the node's underlying Compute Engine infrastructure. Only GPU nodes enter this state. Nodes that use N2 machine types keep running during maintenance as Cluster Director [_live migrates_ them](https://docs.cloud.google.com/compute/docs/instances/live-migration-process).

From this state, the node transitions to one of the following states:

  * **`ACTIVE`** : when host maintenance completes, the node restarts. Cluster Director helps ensure that the resources needed to restart the node are available.

  * **`FAILED`** : the node encounters a host error.




### Failed state

When a node is in the `FAILED` state, the node is unhealthy or encountered a host error. To help you troubleshoot the issue, Cluster Director provides details about the error in [Logs Explorer](https://docs.cloud.google.com/cluster-director/docs/monitor/view-audit-logs#custom-logs), or in the `stateMessage` field when you use the Google Cloud CLI or REST API.

**Note:** If your node encounters an unexpected error, then contact your account team or support for help.

From this state, when you delete the node or cluster, the node transitions to the `DELETING` state.

### Deleting state

When a node is in the `DELETING` state, Cluster Director is deleting the node and releasing its resources. A node enters the `DELETING` state after one of the following occurs:

  * The reservation that you used to create the node has reached its end time. Cluster Director deletes the node if it was created by using the reserved resources for a future reservation in calendar mode, or if you configured the node to be deleted when the reservation reaches its end time.

  * You manually delete the node.

  * You reduce the static node count (`staticNodeCount`) or maximum dynamic node count (`maxDynamicNodeCount`) in a nodeset.

  * You delete the cluster.




When the deletion operation ends, Cluster Director permanently deletes the node and all of its attached resources.

## Pricing for clusters and nodes

When you create a cluster, you incur charges for the underlying Google Cloud resources that your cluster uses:

  * **Nodes** : you incur charges for vCPUs, memory, and any attached GPUs when the node is running, which is when the node is in the `ACTIVE` state. For any disks and external IP addresses that are attached to the node, you incur charges for these resources as long as the node exists, regardless of the node state. For more information, see [Virtual machines pricing](https://cloud.google.com/compute/pricing).

  * **Networking resources** : you incur charges for data transfer (_egress_) and any additional networking features that your cluster uses. For more information, see [All networking pricing](https://cloud.google.com/vpc/network-pricing).

  * **Storage resources** : you incur charges for the storage resources that your cluster uses, as long as those resources exist. For more information, see the following:

    * [Cloud Storage pricing](https://cloud.google.com/storage/pricing)

    * [Filestore pricing](https://cloud.google.com/filestore/pricing)

    * [Google Cloud Managed Lustre pricing](https://cloud.google.com/products/managed-lustre/pricing)




For more information, review the [pricing for Cluster Director](https://cloud.google.com/products/cluster-director#pricing).

## What's next

  * [Modify a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/modify-cluster)

  * [Delete a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/delete-cluster)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
