---
url: https://docs.cloud.google.com/vmware-engine/docs/concepts-storage-only-nodes/
title: Storage-only nodes \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:39.209927+00:00
---

# Storage-only nodes  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/concepts-storage-only-nodes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Storage-only nodes

A storage-only node, also known as storage node, is a VMware Engine node type that does not have any customer-usable cores and only has customer-usable storage. These nodes can be added to a cluster of VMware Engine hyper converged nodes to increase the storage capacity of the cluster without adding cores to the cluster.

**Note:** A cluster can consist of a maximum of **50%** storage-only nodes. A dedicated cluster made up entirely of storage-only nodes is not supported because the workload VMs can't run on storage-only nodes.

Storage-only nodes can only be added to a management cluster with a minimum of three HCI nodes and a workload cluster that has at least two HCI nodes.

Storage-only nodes are available using the Google Cloud console, Google Cloud CLI and VMware Engine API. The storage nodes don't contribute cores or memory to the private cloud and cluster and can't run VMs. You can use the Google Cloud CLI and VMware Engine API to query the number of storage-only nodes in a cluster.

By accessing the vCenter UI, you can identify which ESXi hosts are configured as storage-only nodes by looking at tags assigned to ESXi hosts. You can query for the tag `storage_only_node` in vCenter and find all ESXi hosts that have this tag.

## Limitations

  * When using a cluster made up of two HCI and one storage node, if there's an HCI node failure, there might be only one available HCI node in the cluster to run VMs. This scenario can remain until the cluster adds a replacement node, at which time your cluster is restored back to resilience.

  * You won't be able to use vMotion on a VM to a storage node within a cluster. If you try to perform this action, you may see a vCenter error stating that there are insufficient resources on the storage node. Instead, you can use the vCenter interface to query the "storage-only" tag to find all ESXi hosts that are configured as storage nodes.

  * Converting a storage node to an HCI node and the other way around is not supported.

  * When a cluster contains storage-only nodes, the vCenter cluster summary reports physical CPU and memory for all nodes of the cluster, including compute capacity from storage-only nodes which is unavailable for running VMs. For an accurate view of available compute resources, use vSphere Distributed Resource Scheduler (DRS) stats for CPU and memory utilization. To manually calculate available compute resources from cluster summary metrics, exclude compute capacity proportional to the percentage of storage-only nodes in your vSphere cluster.




## What's next

  * Learn how to [use storage only nodes](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-use-storage-only-nodes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
