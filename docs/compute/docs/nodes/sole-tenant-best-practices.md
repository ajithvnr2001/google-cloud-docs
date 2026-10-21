---
url: https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-best-practices/
title: Best practices for using sole-tenant nodes to run VM workloads \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:10.730404+00:00
---

# Best practices for using sole-tenant nodes to run VM workloads  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Best practices for using sole-tenant nodes to run VM workloads Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

When you're planning to run VM workloads on sole-tenant nodes, you must first decide how to deploy sole-tenant nodes. In particular, you have to decide how many node groups you need, and which maintenance policy the node groups should use:

  * **Node groups:** To choose the right number of node groups, you must weigh off availability and resource utilization. While a small number of node groups lets you optimize resource utilization and cost, it limits you to a single zone. Deploying node groups across multiple zones lets you improve availability, but can result in lower resource utilization.

  * **Autoscaling and maintenance policies:** Depending on licensing requirements of the operating systems and software that you're planning to run, node autoscaling and your choice of maintenance policy can impact your licensing cost and availability.




To make the right decision on how to use sole-tenant nodes, you must carefully consider your requirements.

## Assessing requirements

The following section lists several requirements that you should consider before deciding how many node groups you need, and which maintenance policy the node groups should use.

### BYOL and per-core licensing

If you're planning to [bring your own license](https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses) (BYOL) to Compute Engine, sole-tenant nodes can help you address the hardware requirements or constraints imposed by these licenses.

Some software and operating systems such as Windows Server can be [licensed by physical CPU core](https://docs.cloud.google.com/compute/docs/nodes/determining-server-usage) and might define limits on how frequently you are allowed to change the hardware underlying your virtual machines. Node autoscaling and the [default maintenance policy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#maintenance_policies) can lead to hardware being changed more often than your license terms permit, which can result in additional licensing fees.

To optimize for per-core BYOL, consider the following best practices:

  * **Find a balance between optimizing infrastructure cost and licensing cost** : To calculate the overall cost of running BYOL workloads on Compute Engine, you must consider both infrastructure cost and licensing cost. In some cases, minimizing infrastructure cost might increase licensing overhead, or vice versa. For example, using a node type with a high number of cores might be best from a cost/performance standpoint for certain workloads, but could lead to additional licensing cost if licenses are priced by core.

  * **Use separate node groups for BYOL and non-BYOL workloads:** To limit the number of cores you need to license, avoid mixing BYOL and non-BYOL workloads in a single node group and use separate node groups instead.

If you use multiple different BYOL licensing models (for example, Windows Server Datacenter and Standard), splitting node groups by licensing model can help simplify license tracking and reduce licensing cost.

  * **Use CPU overcommit and node types with a high core/memory ratio:** Node types [differ in their ratio between sockets, cores, and memory](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types). Using a node type with a higher core:memory ratio and [enabling CPU overcommit](https://docs.cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-vms) can help reduce the number of cores that you need to license.

  * **Avoid scale-in autoscaling:** [Node group autoscaling](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups) lets you automatically grow or shrink a node group based on current demand. Frequent growing and shrinking of a node group implies that you're frequently changing the hardware that your VMs run on.

If you're changing hardware more frequently that you're allowed to move licenses between physical machines, these hardware changes can lead to a situation where you have to license more cores that you're actually using.

If there are limits on how frequently you're allowed to move between physical machines, you can avoid excessive licensing cost by disabling autoscaling or by configuring autoscaling to [only scale out](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups#only_scale_out).

  * **Don't use the default maintenance policy:** The [default maintenance policy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#default_host_maintenance_policy) lets you optimize for VM availability, but can cause frequent hardware changes. To minimize hardware changes and optimize for licensing cost, use the [migrate within node group maintenance](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#migrate_within_node_group_host_maintenance_policy) or [restart in place](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#restart_in_place_host_maintenance_policy) policy instead.




For workloads that don't require per-core licensing, consider the following best practices instead:

  * **Use the default maintenance policy:** By using [live-migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process), the [default maintenance policy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#default_host_maintenance_policy) offers better availability than the [restart in place](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#restart_in_place_host_maintenance_policy) policy, and it avoids the extra infrastructure cost of the [migrate within node group maintenance](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#migrate_within_node_group_host_maintenance_policy) policy.



### Management

When you have more than one workload, or when you have both development and production workloads that need to run on sole-tenant nodes, consider the following best practices:

  * **Use separate node groups for development and production environments:** Using separate node groups helps you isolate environments from another and avoid situations such as the following:

    * A development VM might impact the performance of production VMs by excessively consuming CPU, disk, or network resources ("noisy neighbor").
    * A development workload might exhaust the capacity of a node group, preventing the creation of new production VMs.
  * **Limit the number of node groups in each environment:** If you run multiple node groups, it can be difficult to fully utilize each node group. To optimize utilization, combine workloads of each environment and schedule them on a small number of node groups.

  * **Use dedicated projects for managing node groups:** For each environment, create a dedicated project to manage node groups. Then [share the node groups](https://docs.cloud.google.com/compute/docs/nodes/share-node-groups) with projects that contain workloads.

This approach lets you simplify access control by using a separate project for each workload while also letting you optimize resource utilization by sharing node groups across workloads.

  * **Share node groups with individual projects:** Instead of sharing a node group with an entire organization, share it with individual projects only. Selecting projects individually helps you maintain a separation between environments, and avoids disclosing information about node groups to other projects.

  * **Establish a process for internal cost attribution:** The cost for running a node group is incurred in the project that contains the node group. If you need to attribute this cost to individual projects or workloads, consider [tracking the usage of your sole-tenant VMs](https://docs.cloud.google.com/compute/docs/nodes/determining-server-usage) and using this data to perform internal cost attribution.




### Availability

Your workloads might differ in their availability requirements, and whether high-availability can be achieved on the application layer or whether it needs to be implemented on the infrastructure layer:

  * **Clustered applications:** Some of your workloads might implement high availability in the application by using clustering techniques such as replication and load-balancing.

Examples for such workloads include Active Directory domain controllers, SQL Server Failover Cluster Instances and Availability Groups, or clustered load-balanced applications running in IIS.

Clustered applications can typically sustain individual VM outages as long as the majority of VMs remain available.

  * **Non-clustered applications:** Some of your workloads might not implement any clustering capabilities and instead require that the VM itself must be kept available.

Examples for such workloads include non-replicated database servers or stateful application servers.

To optimize the availability of individual VMs, you need to ensure that the VM can be [live-migrated](https://docs.cloud.google.com/compute/docs/instances/live-migration-process) in case of an upcoming node maintenance event.

Live migration is supported by the [default maintenance policy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#default_host_maintenance_policy) and the [migrate within node group](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#migrate_within_node_group_host_maintenance_policy) maintenance policy, but isn't supported if you use the [restart in place maintenance policy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#restart_in_place_host_maintenance_policy).

  * **Non-critical applications:** Batch workloads, development/test workloads, and other lower-priority workloads might have no particular availability requirements. For these workloads, it might be acceptable if individual VMs are unavailable during node maintenance.




To accommodate the availability requirements of your workloads, consider the following best practices:

  * **Use node groups in different zones or regions to deploy clustered workloads:** Sole-tenant nodes and node groups are a zonal resource. To protect against zonal outages, deploy multiple node groups in different zones or regions. Use [node affinity](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_affinity_and_anti-affinity) to schedule VMs so that each instance of your clustered application runs on a different node in a different zone or region.

If two or more of your node groups use the default or restart in place maintenance policy, configure maintenance windows so that they are unlikely to overlap.

If multiple instances of your clustered applications must run in a single zone, use anti-affinity to ensure that the VM instances are scheduled on different nodes or node groups.

  * **Avoid the restart in place maintenance policy for non-clustered workloads that require high availability:** Because the [restart in place](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#restart_in_place_host_maintenance_policy) maintenance policy shuts down VMs when the underlying node requires maintenance, prefer using different maintenance policy for node groups that run non-clustered workloads that require high availability.

  * **Use managed instance groups to increase resilience and availability of workloads:** You can further increase the resilience and availability of your deployment by using managed instance groups to monitor the health of your workloads and to [automatically recreate VM instances if necessary](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs). You can use managed instance groups for both [stateless](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) and [stateful workloads](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs).




### Performance

Your workloads might differ in their sensitivity to performance fluctuations. For certain internal applications or test workloads, optimizing cost might be more important than ensuring consistent performance throughout the day. For other workloads such as externally facing applications, performance might be critical and more important than resource utilization.

To make the best use of your sole-tenant nodes, consider the following best practices:

  * **Use dedicated node groups and CPU overcommit for performance-insensitive workloads:** [CPU overcommit](https://docs.cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-vms) lets you increase the VM density on sole-tenant nodes and can help reduce the number of sole-tenant nodes required.

To use CPU overcommit, you must use a [node type that supports CPU overcommit](https://docs.cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-vms#limitations). Enabling CPU overcommit for a node group causes additional charges per sole-tenant node.

CPU overcommit can be most cost-effective if you use a dedicated node group for workloads that are suitable for CPU overcommit and enable CPU overcommit for this node group only. Leave CPU overcommit disabled for any node groups that need to run performance-sensitive workloads.

  * **Use a node type with a high core:memory ratio for CPU overcommit:** While CPU overcommit lets you share cores between VMs, it doesn't let you share memory between VMs. Using a node type that has relatively more memory per CPU core helps you ensure that memory doesn't become a limiting factor.



  * **Use node autoscaling for performance-sensitive workloads:** To accommodate varying resource needs for workloads that are performance-sensitive, configure your node group to [use autoscaling](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups).



## Deployment patterns

The best way to use sole-tenant nodes depends on your individual requirements. The following section describes a selection of patterns that you can use as a starting point to derive an architecture that suits your individual requirements.

### Multiple node groups for mixed performance requirements

If you have a combination of workloads that are performance–sensitive (for example, customer-facing applications) and performance-insensitive (for example, internal applications), you can use multiple node groups that use different node types:

![Multiple node groups for mixed performance requirements](https://docs.cloud.google.com/static/compute/images/sole-tenant-pattern-mixed-performance.svg)

  * One node group uses CPU overcommit and a node type with a 1:8 vCPU:memory ratio. This node group is used for performance-insensitive workloads.
  * A second node group uses a compute-optimized node type with a 1:4 vCPU:memory ratio without CPU overcommit. This node group is used for performance-critical workloads and is configured to scale up and down on demand.



### Multi-zone high availability for clustered per-core licensed workloads

If you're running clustered workloads that use per-core licensing and need to minimize hardware changes, you can strike a balance between availability and licensing overhead by using multiple node groups with non-overlapping maintenance windows:

![Multi-zone high availability for clustered per-core licensed workloads](https://docs.cloud.google.com/static/compute/images/sole-tenant-pattern-multi-zone-clustered.svg)

  * Multiple node groups are deployed across different [zones or regions](https://docs.cloud.google.com/docs/geography-and-regions).
  * All node groups use the [restart](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#restart_in_place_host_maintenance_policy) maintenance policy. The node groups use non-overlapping maintenance windows so that no more than one node group should experience maintenance-related outages at a time.
  * VM instances that run clustered workloads use affinity labels so that each cluster node is scheduled on a node group in a different zone.



### Multi-zone high availability for mixed per-core licensed workloads

If you're using per-core licensing, but not all of your workloads are clustered, you can extend the previous pattern by using heterogeneous maintenance policies:

![Multi-zone high availability for mixed per-core licensed workloads](https://docs.cloud.google.com/static/compute/images/sole-tenant-pattern-multi-zone-non-clustered.svg)

  * The primary node group is deployed in zone `a` and runs both clustered and non-clustered workloads. To minimize outages caused by hardware maintenance, the node group uses the [migrate within node group](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#migrate_within_node_group_host_maintenance_policy) maintenance policy.
  * One or more secondary node groups are deployed in additional [zones or regions](https://docs.cloud.google.com/docs/geography-and-regions). These node groups use the [restart](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#restart_in_place_host_maintenance_policy) maintenance policy, but use non-overlapping maintenance windows.
  * VM instances that run clustered workloads use affinity labels so that each cluster node is scheduled on a node group in a different zone.
  * VM instances that run non-clustered workloads use affinity labels so that they are deployed on the primary node group.



By only scheduling clustered workloads on the secondary node groups, you can ensure that the temporary outages caused by the restart maintenance policy has minimal impact on overall availability. At the same time, you limit licensing and infrastructure overhead by using the [migrate within node group](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#migrate_within_node_group_host_maintenance_policy) maintenance policy for the primary node group only.

## What's next

  * Learn more about [sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).


  * Learn how to [overcommit CPUs on sole-tenant VMs](https://docs.cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-vms).


  * Learn how to [bring your own licenses](https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
