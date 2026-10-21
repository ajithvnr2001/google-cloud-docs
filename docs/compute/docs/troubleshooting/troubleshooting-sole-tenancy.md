---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-sole-tenancy/
title: Troubleshooting sole-tenancy \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:02:47.259293+00:00
---

# Troubleshooting sole-tenancy  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-sole-tenancy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting sole-tenancy Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This page describes how to troubleshoot some potential issues that might occur while using [sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).

## Node group size limitation

  * **Problem** : Size of a node group is limited to 100.

    * **Solution** : Create multiple node groups and use the same affinity label for each node group. Then, when scheduling VMs on these node groups, use the affinity label you assigned to the node groups.



## VM scheduling failures

  * **Problem** : Can't schedule a VM on a sole-tenant node.

    * **Solution** :

      * You can't schedule a sole-tenant VM if there's no node in the zone that matches the VM's [affinity or anti- affinity](https://docs.cloud.google.com/compute/docs/nodes#node_affinity_and_anti-affinity) specification. Check that you have specified the correct affinity labels. Also, check that you have not specified any conflicting affinity labels.

      * If you are using the restart in place maintenance policy, check that the VM's `OnHostMaintenance` setting is set to `terminate`.

      * If you are using the migrate within node group maintenance policy, check that you are scheduling VMs on a node group, not a specific node or by using an affinity label.

      * Check that the specified node name matches the name of a node in the zone.

      * Check that the specified node group name matches the name of a node group in the zone.

      * You can't schedule a sole-tenant VM if the VM's minimum CPU platform (`--min-cpu-platform`) is set to any value other than `AUTOMATIC`.




## VM tenancy

  * **Problem** : Can't move a VM to a sole-tenant node.

    * **Solution** :

      * A VM instance with a specified [minimum CPU platform](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform) can't be moved to a sole-tenant node by updating VM tenancy. To move a VM to a sole-tenant node, [remove the minimum CPU platform specification by setting it to `automatic`](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform).

      * Because each sole-tenant node uses a [specific CPU platform](https://docs.cloud.google.com/compute/docs/nodes#node_types), all VMs running on the node cannot specify a minimum CPU platform. Before you can move a VM to a sole-tenant node by [updating its tenancy](https://docs.cloud.google.com/compute/docs/nodes/updating-vm-tenancy), you must set the VM's [`--min-cpu-platform` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update#--min-cpu-platform) to `AUTOMATIC`.




## Autoscaling node groups

  * **Problem** : Can't enable the node group autoscaler.

    * **Solution** : You can only enable the node group autoscaler when you set the node group maintenance policy to the **Default** maintenance policy.
  * **Problem** : Want to retain already reserved nodes with the migrate within node group maintenance policy.

    * **Solution** : When using the **Migrate within node group** maintenance policy, set the node group autoscaler to only scale out, which adds nodes to the node group when it needs extra capacity.
  * **Problem** : No remaining CPU quota in the region.

    * **Solution** : Autoscaling might fail if you have no remaining CPU quota in the region, the number of nodes in a group is at the maximum number allowed, or there was a billing issue. Depending on the error, you might need to request an increase in CPU quota or create a new sole-tenant node group.



## Bringing your own licenses (BYOL)

  * **Problem** : Configuring the restart in-place maintenance policy.

    * **Solution** : If using the restart in-place maintenance policy, set the VM's `OnHostMaintenanceSetting` to `terminate`.
  * **Problem** : Scheduling VMs on node groups with the migrate within node group maintenance policy.

    * **Solution** :

      * Schedule VMs onto a node group, not on a specific node or by using a customized affinity label.

      * Create 2 nodes and enable the autoscaler; otherwise, if you create a node group of size 1, the node is reserved for holdback.




## Capacity issues

  * **Problem** : Not enough capacity on a node or in a node group.

    * **Solution** :

      * If you reschedule a VM onto a node that is scheduling VMs in parallel, in rare situations there might not be capacity.

      * If you reschedule a VM onto a node in a node group on which you haven't enabled [autoscaling](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups), there might not be capacity.

      * If you reschedule a VM onto a node in a node group on which you have enabled autoscaling but have exceeded your CPU quota, there might not be capacity.




## CPU overcommit

  * **Problem** : An error indicating that no sole-tenant node group was specified when you set the value for the minimum number of CPUs:
        
        Invalid value for field 'resource.scheduling.minNodeCpus': '2'. Node virtual
        CPU count may only be specified for sole-tenant instances.
        

    * **Solution** : Specify a sole-tenant node group when setting the value for the minimum number of CPUs
  * **Problem** : An error indicating that the total of the minimum number of CPUs for all sole-tenant VMs on a node is greater than the CPU capacity of the node type.
        
        Node virtual CPU count must not be greater than the guest virtual CPU count.
        
        
        No feasible nodes found for the instance given its node affinities and other
        constraints.
        

    * **Solution** : Specify values for the minimum number of CPUs for each VM so that the total for all VMs does not exceed the number of CPUs specified by the sole-tenant node type.
  * **Problem** : An error indicating that the total number of CPUs specified by the machine types for all VMs on a node is more than twice the minimum number of CPUs specified for all VMs on a node.
        
        Guest virtual CPU count must not be greater than [~2.0] times the node
        virtual CPU count.
        

    * **Solution** : Increase the value for the minimum number of CPUs for VMs on this node until the total minimum number of CPUs is greater than or equal to half the value for the total number of CPUs determined by the machine types.
  * **Problem** : An error indicating that the value for the minimum number of CPUs is not an even number greater than or equal to 2.
        
        Invalid value for field 'resource.scheduling.minNodeCpus': '3'. Node virtual
        CPU count must be even.
        

    * **Solution** : Specify a value for the minimum number of CPUs that is an even number greater than or equal to 2.



## GPUs

  * **Problem** : An error indicating that instance creation failed because of node property incompatibility.
        
        Instance could not be scheduled due to no matching node with property compatibility.
        

    * **Solution** : GPU-enabled sole-tenant nodes only support VMs that have GPUs attached. To resolve this issue, [Provision a sole-tenant VM](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms#provision_a_sole-tenant_vm) with GPUs.



## What's next

  * [Provisioning VMs on sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms)

  * [Bringing your own licenses](https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses)

  * [Analyzing sole-tenant node usage](https://docs.cloud.google.com/compute/docs/nodes/determining-server-usage)

  * [Autoscaling node groups](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups)

  * [Overcommitting CPUs on sole-tenant VMs](https://docs.cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-vms)

  * [Updating VM tenancy](https://docs.cloud.google.com/compute/docs/nodes/updating-vm-tenancy)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
