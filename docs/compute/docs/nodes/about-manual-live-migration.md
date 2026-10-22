---
url: https://docs.cloud.google.com/compute/docs/nodes/about-manual-live-migration/
title: About manual live migration \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:42.764564+00:00
---

# About manual live migration  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/nodes/about-manual-live-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About manual live migration Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Sole-tenancy lets you create VMs on a specific sole-tenant node or in a group of nodes. If you create a VM in a group of nodes, Compute Engine optimizes the space available for VMs in the node group by using a bin-packing algorithm to determine the node to place the VM on. For information about sole-tenancy, see [Sole-tenancy overview](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).

As your workload runs, you might want to move VMs to a different node or node group. To move sole-tenant VMs to a different node or node group, you can manually initiate a live migration. You can also manually initiate a live migration to move a multi-tenant VM into sole-tenancy.

## Use cases for manual live migration

The following list shows some use cases for manually live migrating VMs:

  * **Increase utilization and optimize costs.** You might be able to consolidate VMs onto fewer sole-tenant nodes.

  * **Logically reorganize VMs.** Use different sole-tenant node groups or nodes to separate VMs based on their workload type.

  * **Isolate workloads to meet compliance standards or improve performance.** Manually live migrate multi-tenant workloads that require hardware isolation into sole-tenancy to meet compliance standards or to improve performance.

  * **Increase portability of VMs.** You can't modify certain node template settings, such as the maintenance policy, the maintenance window, and settings related to local SSD. By using manual live migration, you can migrate VMs to a node group with different settings.



  * **Improve performance by rebalancing oversubscribed sole-tenant nodes.** If you are [overcommitting CPUs on sole-tenant VMs](https://docs.cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-vms#optimizing_cpu_overcommit_levels), you can manually live migrate any VMs that are underperforming to other sole-tenant nodes.



### Examples

To understand how manual live migration supports the preceding use cases, review the following examples.

#### Manual bin packing

To more efficiently arrange VMs in a node group to fit additional VMs, you can use manual live migration to choose which nodes to put sole-tenant VMs on.

Consider a sole-tenant node group with the following initial state, on which you are trying to schedule an additional VM with 16 vCPUs:

Initial state | Node 1 | Node 2 | Total  
---|---|---|---  
vCPU capacity | 80 | 80 | 160  
VM vCPUs | 72 | 64, 8 | 144  
Unused capacity | 8 | 8 | 16  
  
There is not enough space on any node to schedule a VM with 16 vCPUs. However, there is enough aggregate space.

To make space for the 16 vCPU VM, initiate a live migration of the 8 vCPU VM from Node 2 to Node 1. The following table shows the new VM configuration:

Final state | Node 1 | Node 2 | Total  
---|---|---|---  
vCPU capacity | 80 | 80 | 160  
VM vCPUs | 72, 8 | 64, 16 | 160  
Unused capacity | 0 | 0 | 0  
  
The following figure summarizes this process:

![Manual bin packing of VMs to make room for a larger VM.](https://docs.cloud.google.com/static/compute/images/sole-tenancy/sole-tenant-node-live-migration-1.svg)**Figure 1** : Manual bin packing of VMs to make space for a VM that has more vCPUs.

#### Autoscale after bin packing

After bin packing, there might be sole-tenant nodes without any VMs. In this case, the sole-tenant node autoscaler can remove the empty node.

Consider a sole-tenant node group with the following initial state. If you move the 8 vCPU VM, the node group autoscaler can remove a node:

Initial state | Node 1 | Node 2 | Total  
---|---|---|---  
vCPU capacity | 80 | 80 | 160  
VM vCPUs | 8 | 72 | 80  
Unused capacity | 72 | 8 | 80  
  
To notify the node group autoscaler of an empty node, initiate a live migration of the 8 vCPU VM from Node 1 to Node 2. The following table shows the new VM configuration:

Final state | Node 1 | Node 2 | Total  
---|---|---|---  
vCPU capacity | 80 | 80 | 160  
VM vCPUs | 0 | 72, 8 | 80  
Unused capacity | 80 | 0 | 80  
  
Now that Node 1 is empty, the autoscaler can remove it from the node group. The following table shows the new VM configuration:

Final state | Node 1 | Node 2 | Total  
---|---|---|---  
vCPU capacity | - | 80 | 80  
VM vCPUs | - | 72, 8 | 80  
Unused capacity | - | 0 | 80  
  
The following figure summarizes this process:

![Manual bin packing of VMs to consolidate on one node. Then, the autoscaler can remove the empty node.](https://docs.cloud.google.com/static/compute/images/sole-tenancy/sole-tenant-node-live-migration-2.svg)**Figure 2** : Manual bin packing of VMs to consolidate nodes.

## Limitations

The following limitations apply when manually live migrating VMs:

  * **Capacity limitations.** During manual live migration of a VM within sole-tenancy, the VM consumes capacity from both the source sole-tenant node and the destination sole-tenant node until live migration completes. If there is not enough capacity on the destination host, Compute Engine does not move the VM.

  * **General limitations.** Manual live migration requests might fail if there are incompatible scheduling properties or other competing live migration requests. For information about how to troubleshoot this, see [VM scheduling failures](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-sole-tenancy#vm_scheduling_failures).

  * **Host maintenance policy limitations.** If a node group uses the [**Migrate within node group** (`MIGRATE_WITHIN_NODE_GROUP`) host maintenance policy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#migrate_within_node_group_host_maintenance_policy), then you can't manually live migrate and pin a VM to a specific node within that group. Doing so results in a scheduling compatibility constraint error. Instead, you must target the node group.

  * **Managed instance group (MIG) limitations.** You cannot manually live migrate VMs that are in a MIG to another sole-tenant node.

  * **VM instance lifecycle limitations.** You cannot update some properties of a VM, such as the machine type, without restarting the VM. Also, you cannot update these properties at the same time as you update node affinities. For more information about these properties, see [Updating instance properties](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties).




## Pricing

There are no additional charges for manually live migrating VMs. For more information about how you are billed for sole-tenant nodes, see [Sole-tenant node pricing](https://cloud.google.com/compute/sole-tenant-pricing).

If a sole-tenant node is empty after the migration and you have [enabled the sole-tenant node autoscaler](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups), manually live migrating VMs might lower your charges.

## What's next

  * [Learn how to manually live migrate VMs](https://docs.cloud.google.com/compute/docs/nodes/manually-live-migrate)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
