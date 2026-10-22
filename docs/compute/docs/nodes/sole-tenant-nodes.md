---
url: https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes/
title: Sole-tenancy overview \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:04.160639+00:00
---

# Sole-tenancy overview  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Sole-tenancy overview Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Sole-tenancy provides exclusive access to a _sole-tenant node_ , a physical Compute Engine server that is dedicated to hosting only your project's VMs. Use sole-tenant nodes to keep your VMs physically separated from VMs in other projects, or to group your VMs together on the same host hardware as shown in the following diagram. You can also create a sole-tenant node group and specify whether you want to [share it with other projects or with the entire organization](https://docs.cloud.google.com/compute/docs/nodes/share-node-groups).

![A multi-tenant host versus a sole-tenant node.](https://docs.cloud.google.com/static/compute/images/sole-tenancy/multi-tenant-versus-sole-tenant.svg)**Figure 1** : A multi-tenant host versus a sole-tenant node.

VMs running on sole-tenant nodes can use the same Compute Engine features as other VMs, including transparent scheduling and block storage, but with an added layer of hardware isolation. To give you full control over the VMs on the physical server, each sole-tenant node maintains a one-to-one mapping to the physical server that is backing the node.

Within a sole-tenant node, you can provision multiple VMs on machine types of various sizes, which lets you efficiently use the underlying resources of the dedicated host hardware. Also, if you choose not to share the host hardware with other projects, you can meet security or compliance requirements with workloads that require physical isolation from other workloads or VMs. If your workload requires sole tenancy only temporarily, you can modify [VM tenancy](https://docs.cloud.google.com/compute/docs/nodes/updating-vm-tenancy) as necessary.

Sole-tenant nodes can help you meet dedicated hardware requirements for [bring your own license (BYOL)](https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses) scenarios that require per-core or per-processor licenses. When you use sole-tenant nodes, you have some visibility into the underlying hardware, which lets you track core and processor usage. To track this usage, Compute Engine reports the ID of the physical server on which a VM is scheduled. Then, by using [Cloud Logging](https://docs.cloud.google.com/logging/docs), you can [view the historical server usage of a VM](https://docs.cloud.google.com/compute/docs/nodes/determining-server-usage).

To optimize the use of the host hardware, you can do the following:

  * [Overcommit CPUs on sole-tenant VMs](https://docs.cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-vms)


  * [Share sole-tenant node groups](https://docs.cloud.google.com/compute/docs/nodes/share-node-groups)

  * [Manually live migrate sole-tenant VMs](https://docs.cloud.google.com/compute/docs/nodes/manually-live-migrate)




Through a configurable host maintenance policy, you can control the behavior of sole-tenant VMs while their host is undergoing maintenance. You can specify when maintenance occurs, and whether the VMs maintain affinity with a specific physical server or are moved to other sole-tenant nodes within a node group.

## Workload considerations

The following types of workloads might benefit from using sole-tenant nodes:

  * Gaming workloads with performance requirements

  * Finance or healthcare workloads with security and compliance requirements

  * Windows workloads with licensing requirements

  * Machine learning, data processing, or image rendering workloads. For these workloads, consider [reserving GPUs](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).

  * Workloads requiring increased I/O operations per second (IOPS) and decreased latency, or workloads that use temporary storage in the form of caches, processing space, or low-value data. For these workloads, consider reserving Local SSD disks.




## Node templates

A node template is a regional resource that defines the properties of each node in a node group. When you create a node group from a node template, the properties of the node template are immutably copied to each node in the node group.

When you create a node template you must specify a node type. You can optionally specify node affinity labels when you create a node template. You can only specify node affinity labels on a node template. You can't specify node affinity labels on a node group.

## Node types

When configuring a node template, specify a node type to apply to all nodes within a node group created based on the node template. The sole-tenant node type, referenced by the node template, specifies the total amount of vCPU cores and memory for nodes created in node groups that use that template. For example, the `n2-node-80-640` node type has 80 vCPUs and 640 GB of memory.

The VMs that you add to a sole-tenant node must have the same machine type as the node type that you specify in the node template. For example, `n2` sole-tenant node types are only compatible with VMs created with the `n2` machine type. You can add VMs to a sole-tenant node until the total amount of vCPUs or memory exceeds the capacity of the node.

When you create a node group using a node template, each node in the node group inherits the node template's node type specifications. A node type applies to each individual node within a node group, not to all of the nodes in the group uniformly. So, if you create a node group with two nodes that are both of the `n2-node-80-640` node type, each node is allocated 80 vCPUs and 640 GB of memory.

Depending on your workload requirements, you might fill the node with multiple smaller VMs running on machine types of various sizes, including [predefined machine types](https://docs.cloud.google.com/compute/docs/machine-resource#predefined-types), [custom machine types](https://docs.cloud.google.com/compute/docs/machine-resource#custom-types), and [machine types with extended memory](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#extendedmemory). When a node is full, you cannot schedule additional VMs on that node.

The following table displays the available node types. To see a list of the node types available for your project, run the [`gcloud compute sole-tenancy node-types list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-types/list) command or create a [`nodeTypes.list`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeTypes/list) REST request.

A3A2C4C4AC4DC4NC3C3DC2G4G2H4DH3M4M3M2M1N4AN4N2N2DN1

Clear all

Node type | Processor | vCPU | GB | vCPU:GB | Sockets | Cores:Socket | Total cores | Max VMs allowed  
---|---|---|---|---|---|---|---|---  
`a2-highgpu-node-96-680` | Cascade Lake | 96 | 680 | 1:7.08 | 2 | 24 | 48 | 8  
`a2-megagpu-node-96-1360` | Cascade Lake | 96 | 1360 | 1:14.17 | 2 | 24 | 48 | 1  
`a2-ultragpu-node-96-1360-lssd` 1 | Cascade Lake | 96 | 1360 | 1:14.17 | 2 | 24 | 48 | 1  
`a3-highgpu-node-208-1872-lssd` 1 | Sapphire Rapids | 208 | 1872 | 1:9 | 2 | 56 | 112 | 8  
`a3-megagpu-node-208-1872-lssd` 1 | Sapphire Rapids | 208 | 1872 | 1:9 | 2 | 56 | 112 | 1  
`c2-node-60-240` | Cascade Lake | 60 | 240 | 1:4 | 2 | 18 | 36 | 15  
`c3-node-176-352` | Sapphire Rapids | 176 | 352 | 1:2 | 2 | 56 | 112 | 44  
`c3-node-176-704` | Sapphire Rapids | 176 | 704 | 1:4 | 2 | 56 | 112 | 44  
`c3-node-176-704-lssd` | Sapphire Rapids | 176 | 704 | 1:4 | 2 | 56 | 112 | 40  
`c3-node-176-1408` | Sapphire Rapids | 176 | 1408 | 1:8 | 2 | 56 | 112 | 44  
`c3d-node-360-708` | AMD EPYC Genoa | 360 | 708 | 1:2 | 2 | 96 | 192 | 34  
`c3d-node-360-1440` | AMD EPYC Genoa | 360 | 1440 | 1:4 | 2 | 96 | 192 | 40  
`c3d-node-360-2880` | AMD EPYC Genoa | 360 | 2880 | 1:8 | 2 | 96 | 192 | 40  
`c4-node-192-384` | Emerald Rapids | 192 | 384 | 1:2 | 2 | 60 | 120 | 26  
`c4-node-192-720` | Emerald Rapids | 192 | 720 | 1:3.75 | 2 | 60 | 120 | 26  
`c4-node-192-1488` | Emerald Rapids | 192 | 1,488 | 1:7.75 | 2 | 60 | 120 | 26  
`c4a-node-72-144` | Google Axion | 72 | 144 | 1:2 | 1 | 80 | 80 | 22  
`c4a-node-72-288` | Google Axion | 72 | 288 | 1:4 | 1 | 80 | 80 | 22  
`c4a-node-72-576` | Google Axion | 72 | 576 | 1:8 | 1 | 80 | 80 | 36  
`c4d-node-384-720` | AMD EPYC Turin | 384 | 720 | 1:2 | 2 | 128 | 256 | 24  
`c4d-node-384-1488` | AMD EPYC Turin | 384 | 1488 | 1:4 | 2 | 128 | 256 | 25  
`c4d-node-384-3024` | AMD EPYC Turin | 384 | 3024 | 1:8 | 2 | 128 | 256 | 25  
`c4n-node-192-384` | Emerald Rapids | 192 | 384 | 1:2 | 2 | 60 | 120 | 26  
`c4n-node-192-720` | Emerald Rapids | 192 | 720 | 1:3.75 | 2 | 60 | 120 | 26  
`c4n-node-192-1488` | Emerald Rapids | 192 | 1,488 | 1:7.75 | 2 | 60 | 120 | 26  
`g2-node-96-384` | Cascade Lake | 96 | 384 | 1:4 | 2 | 28 | 56 | 8  
`g4-node-384-1440` | AMD EPYC Turin | 384 | 1440 | 1:3.75 | 2 | 96 | 192 | 64  
`g2-node-96-432` | Cascade Lake | 96 | 432 | 1:4.5 | 2 | 28 | 56 | 8  
`h3-node-88-352` | Sapphire Rapids | 88 | 352 | 1:4 | 2 | 56 | 112 | 1  
`h4d-node-192-720` | AMD EPYC Turin | 192 | 720 | 1:4 | 2 | 128 | 256 | 1  
`h4d-node-192-1488` | AMD EPYC Turin | 192 | 1488 | 1:8 | 2 | 128 | 256 | 1  
`h4d-node-192-3024` | AMD EPYC Turin | 192 | 3024 | 1:16 | 2 | 128 | 256 | 1  
`h4d-node-192-3024-lssd` | AMD EPYC Turin | 192 | 3024 | 1:16 | 2 | 128 | 256 | 1  
`m1-node-96-1433` | Skylake | 96 | 1433 | 1:14.93 | 2 | 28 | 56 | 1  
`m1-node-160-3844` | Broadwell E7 | 160 | 3844 | 1:24 | 4 | 22 | 88 | 4  
`m2-node-416-8832` | Cascade Lake | 416 | 8832 | 1:21.23 | 8 | 28 | 224 | 1  
`m2-node-416-11776` | Cascade Lake | 416 | 11776 | 1:28.31 | 8 | 28 | 224 | 2  
`m3-node-128-1952` | Ice Lake | 128 | 1952 | 1:15.25 | 2 | 36 | 72 | 2  
`m3-node-128-3904` | Ice Lake | 128 | 3904 | 1:30.5 | 2 | 36 | 72 | 2  
`m4-node-224-2976` | Emerald Rapids | 224 | 2976 | 1:13.3 | 2 | 60 | 120 | 12  
`m4-node-224-5952` | Emerald Rapids | 224 | 5952 | 1:26.7 | 2 | 60 | 120 | 1  
`n1-node-96-624` | Skylake | 96 | 624 | 1:6.5 | 2 | 28 | 56 | 96  
`n2-node-80-640` | Cascade Lake | 80 | 640 | 1:8 | 2 | 24 | 48 | 80  
`n2-node-128-864` | Ice Lake | 128 | 864 | 1:6.75 | 2 | 36 | 72 | 128  
`n2d-node-224-896` | AMD EPYC Milan | 224 | 896 | 1:4 | 2 | 64 | 128 | 108  
`n2d-node-224-1792` | AMD EPYC Milan | 224 | 1792 | 1:8 | 2 | 64 | 128 | 112  
`n4-node-224-1372` | Emerald Rapids | 224 | 1372 | 1:6 | 2 | 60 | 120 | 90  
`n4a-node-96-624` | Google Axion | 96 | 624 | 1:6.5 | 1 | 96 | 96 | 72  
  
1**Node types with Local SSD** : The `-lssd` suffix indicates that Local SSD disks are attached to the node. For A3 High, A3 Mega, and A2 Ultra node types, Local SSD disks are also attached by default when no suffix is specified. To provision these node types without Local SSD disks, use the `-nolssd` suffix (for example, `a3-megagpu-node-208-1872-nolssd` or `a2-ultragpu-node-96-1360-nolssd`).

For information about the prices of these node types, see [sole-tenant node pricing](https://cloud.google.com/compute/sole-tenant-pricing).

All nodes let you schedule VMs of different shapes. Node `n` type are general-purpose nodes, on which you can schedule [custom machine type](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types) instances. For recommendations about which node type to choose, see [Recommendations for machine types](https://docs.cloud.google.com/compute/docs/machine-resource#recommendations_for_machine_types). For information about performance, see [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).

## Node groups and VM provisioning

To provision VMs on sole-tenant nodes, complete the following tasks in order:

  1. [Create a sole-tenant node template](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-node-templates).
  2. [Create a sole-tenant node group](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-node-groups).
  3. [Provision VMs on sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms).



A node group is a homogeneous set of sole-tenant nodes in a specific zone. Node groups inherit properties from the node template they are based on, and can contain multiple VMs from the same [machine series](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) running on machine types of various sizes, as long as the machine type has 2 or more vCPUs.

When you create a node group, you specify its host maintenance policy, [sharing settings](https://docs.cloud.google.com/compute/docs/nodes/share-node-groups), and size. A node group can have zero or more nodes. You can manage the size of the node group manually, or you can [enable autoscaling](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups#enabling) to adjust the size automatically based on your workload.

After creating a node group, you can provision VMs onto specific nodes within that group. Use node affinity labels for fine-grained control over VM placement. After provisioning, you can also use [resource labels](https://docs.cloud.google.com/compute/docs/labeling-resources) to organize and manage your VMs for purposes such as billing or inventory.

### Host maintenance policy

Depending on your licensing scenarios and workloads, you might want to limit the number of physical cores used by your VMs. The host maintenance policy you choose might depend on, for example, your licensing or compliance requirements, or, you might want to choose a policy that lets you limit usage of physical servers. With all of these policies, your VMs remain on dedicated hardware.

When you schedule VMs on [sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes), you can choose from the following three different host maintenance policy options, which let you determine how and whether Compute Engine [live migrates](https://docs.cloud.google.com/compute/docs/instances/live-migration-process) VMs during [host events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#host_events), which occur approximately every 4 to 6 weeks. During maintenance, Compute Engine live migrates, as a group, all of the VMs on the host to a different sole-tenant node, but, in some cases, Compute Engine might break up the VMs into smaller groups and live migrate each smaller group of VMs to separate sole-tenant nodes.

#### Default host maintenance policy

This is the default host maintenance policy, and VMs on node groups configured with this policy follow [traditional maintenance behavior for non-sole-tenant VMs](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents). That is, depending on the on-host maintenance setting of the VM's host, VMs [live migrate](https://docs.cloud.google.com/compute/docs/instances/live-migration-process) to a new sole-tenant node in the node group before a host maintenance event, and this new sole-tenant node only runs the customer's VMs.

This policy is most suitable for per-user or per-device licenses that require live migration during host events. This setting doesn't restrict migration of VMs to within a fixed pool of physical servers, and is recommended for general workloads without physical server requirements and that don't require existing licenses.

Because VMs live migrate to any server without considering existing server affinity with this policy, this policy is not suitable for scenarios requiring minimization of the use of physical cores during host events.

The following figure shows an animation of the **Default** host maintenance policy.

![Animation of the default host maintenance policy.](https://docs.cloud.google.com/static/compute/images/sole-tenancy/maintenance-policies/default.gif)**Figure 2** : Animation of the **Default** host maintenance policy.

#### VMs that don't support live migration

For VMs that don't support live migration (such as some Confidential VMs), during a host maintenance event, Compute Engine allocates a fresh sole-tenant node, terminates the VMs on the old node, and then automatically restarts them on the new node. The disruption to your VM is comparable to a standard restart.

If there are both VMs that can live migrate and VMs that don't support live migration running on a single host, then, during a maintenance event, the VMs that support live migration migrate to a new host, while the other VMs terminate and restart.

To minimize downtime, set the sole-tenant node maintenance policy to **Default** and configure your VMs to terminate on host maintenance with automatic restart (`onHostMaintenance=TERMINATE` and `automaticRestart=true`).

#### Restart in place host maintenance policy

When you use this host maintenance policy, Compute Engine stops VMs during host events, and then restarts the VMs on the same physical server after the host event. You must set the VM's on host maintenance setting to `TERMINATE` when using this policy.

This policy is most suitable for workloads that are fault-tolerant and can experience approximately one hour of downtime during host events, workloads that must remain on the same physical server, workloads that don't require live migration, or if you have licenses that are based on the number of physical cores or processors.

With this policy, the instance can be assigned to the node group using `node-name`, `node-group-name`, or node affinity label.

If you have VMs that don't support live migration, use the **Restart in place** policy only if you require physical server affinity. Otherwise, use the **Default** policy to minimize downtime.

The following figure shows an animation of the **Restart in place** maintenance policy.

![Animation of the restart in place host maintenance policy](https://docs.cloud.google.com/static/compute/images/sole-tenancy/maintenance-policies/restart-in-place.gif)**Figure 3** : Animation of the **Restart in place** host maintenance policy.

#### Migrate within node group host maintenance policy

When using this host maintenance policy, Compute Engine live migrates VMs within a fixed-sized group of physical servers during host events, which helps limit the number of unique physical servers used by the VM.

This policy is most suitable for high-availability workloads with licenses that are based on the number of physical cores or processors, because with this host maintenance policy, each sole-tenant node in the group is pinned to a fixed set of physical servers, which is different than the default policy that lets VMs migrate to any server.

Because this policy relies on live migration to move VMs to holdback nodes, VMs that don't support live migrate can't use this policy. If your VMs can't live migrate and you don't have software licenses that require physical server affinity within a node group (such as Windows Server BYOL), then there is no benefit to using this policy and you will incur the cost of the reserved holdback nodes.

With this policy, you can't assign or [manually live migrate](https://docs.cloud.google.com/compute/docs/nodes/manually-live-migrate) a VM to a specific node using the `node-name` affinity label. You can use any custom node affinity labels for your VMs as long as you also specify the `node-group-name` affinity label and not `node-name`.

To confirm the capacity for live migration, Compute Engine reserves 1 holdback node for every 20 nodes that you reserve. The following figure shows an animation of the **Migrate within node group** host maintenance policy.

![Animation of the migrate within a node group host maintenance policy.](https://docs.cloud.google.com/static/compute/images/sole-tenancy/maintenance-policies/migrate-within-node-group.gif)**Figure 4** : Animation of the **Migrate within node group** host maintenance policy.

The following table shows how many holdback nodes Compute Engine reserves depending on how many nodes you reserve for your node group.

Total nodes in group | Holdback nodes reserved for live migration  
---|---  
1 | Not applicable. Must reserve at least 2 nodes.  
2 to 20 | 1  
21 to 40 | 2  
41 to 60 | 3  
61 to 80 | 4  
81 to 100 | 5  
  
This policy requires at least one empty holdback node at all times for live migrations. If you try to delete the only empty node in the group, then the operation fails with an `insufficient holdback` error. To consolidate VMs onto fewer nodes and delete excess empty nodes, stop and restart VMs on sparsely populated nodes or [manually live migrate the VMs](https://docs.cloud.google.com/compute/docs/nodes/manually-live-migrate) to the node group.

**Pin an instance to multiple node groups**

You can pin an instance to multiple node groups using the `node-group-name` [affinity label](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_affinity_and_anti-affinity) under the following conditions:

  * The instance that you want to pin is using a [default host maintenance policy (_Migrate VM instance_)](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#default_host_maintenance_policy).
  * The host maintenance policy of all the node groups that you want to pin the instance to is _migrate within node group_. If you try to pin an instance to node groups with different host maintenance policies, the operation fails with an error.



For example, if you want to pin an instance `test-node` to two node groups `node-group1` and `node-group2`, verify the following:

  * The host maintenance policy of `test-node` is _Migrate VM instance_.
  * The host maintenance policy of `node-group1` and `node-group2` is _migrate within node group_.

**Note:** If the instance's on host maintenance policy is _Terminate_ , you can pin the instance to only a single node group.

### Maintenance windows

If you are managing workloads—for example—finely tuned databases, that might be sensitive to the performance impact of [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process), then you can determine when maintenance begins on a sole-tenant node group by specifying a maintenance window when you create the node group. You can't modify the maintenance window after you create the node group.

Maintenance windows are 4-hour blocks of time that you can use to specify when Google performs maintenance on your sole-tenant nodes. The maintenance window defines when the node maintenance is allowed to begin, which then triggers live migration or terminate and restart actions at the VM level. Maintenance events occur [approximately once every 4 to 6 weeks](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents).

The maintenance window applies to all VMs in the sole-tenant node group, and it only specifies when the maintenance begins. Maintenance is not guaranteed to finish during the maintenance window, and there is no guarantee on how frequently maintenance occurs. Maintenance windows are not supported on node groups with the **Migrate within node group** host maintenance policy.

### Simulate a host maintenance event

You can [simulate a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance#testpoliciesonsoletenants) to test how your workloads that are running on sole-tenant nodes behave during a host maintenance event. This lets you see the effects of the sole-tenant VM's host maintenance policy on the applications running on the VMs.

### Host errors

When there is a rare critical hardware failure on the host—sole-tenant or multi-tenant—Compute Engine does the following:

  1. Retires the physical server and its unique identifier.

  2. Revokes your project's access to the physical server.

  3. Replaces the failed hardware with a new physical server that has a new unique identifier.

  4. Moves the VMs from the failed hardware to the replacement node.

  5. Restarts the affected VMs if you configured them to automatically restart.




## Node affinity and anti-affinity

Sole-tenant nodes make sure that your VMs don't share host with VMs from other projects unless you use shared sole-tenant node groups. With [shared sole-tenant node groups](https://docs.cloud.google.com/compute/docs/nodes/share-node-groups), other projects within the organization can provision VMs on the same host. However, you still might want to group several workloads together on the same sole-tenant node or isolate your workloads from one another on different nodes. For example, to help meet some compliance requirements, you might need to use affinity labels to separate sensitive workloads from non-sensitive workloads.

When you create a VM, you request sole-tenancy by specifying node affinity or anti-affinity, referencing one or more node affinity labels. You specify custom node affinity labels when you create a node template, and Compute Engine automatically includes some default affinity labels on each node. By specifying affinity when you create a VM, you can schedule VMs together on a specific node or nodes in a node group. By specifying anti-affinity when you create a VM, you can make sure that certain VMs are not scheduled together on the same node or nodes in a node group.

Node affinity labels are key-value pairs assigned to nodes, and are inherited from a node template. Affinity labels let you:

  * Control how individual VM instances are assigned to nodes.
  * Control how VM instances created from a template, such as those created by a managed instance group, are assigned to nodes.
  * Group sensitive VM instances on specific nodes or node groups, separate from other VMs.



### Default affinity labels

Compute Engine assigns the following default affinity labels to each node:

  * A label for the node group name: 
    * Key: `compute.googleapis.com/node-group-name`
    * Value: Name of the node group.
  * A label for the node name: 
    * Key: `compute.googleapis.com/node-name`
    * Value: Name of the individual node.
  * A label for the projects the node group is shared with: 
    * Key: `compute.googleapis.com/project`
    * Value: Project ID of the project containing the node group.

**Note:** Default affinity labels are system-managed labels used for VM scheduling and node affinity configurations. They don't appear in the Google Cloud console's custom affinity labels list for a node group.

### Custom affinity labels

You can create custom node affinity labels when you [create a node template](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms#create_a_sole-tenant_node_template). These affinity labels are assigned to all nodes in node groups created from the node template. You can't add more custom affinity labels to nodes in a node group after the node group has been created.

For information about how to use affinity labels, see [Configuring node affinity](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms#configure_node_affinity_labels).

## Pricing

  * To help you to minimize the cost of your sole-tenant nodes, Compute Engine provides [committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview) and [sustained use discounts (SUDs)](https://docs.cloud.google.com/compute/docs/sustained-use-discounts). Note that for sole-tenancy premium charges, you can receive only flexible CUDs and SUDs, but not resource-based CUDs.

  * Because you are already billed for the vCPU and memory of your sole-tenant nodes, you don't pay extra for the VMs that you create on those nodes.

  * If you provision sole-tenant nodes with GPUs or Local SSD disks, you are billed for all of the GPUs or Local SSD disks on each node that you provision. The sole-tenancy premium is based only on the vCPUs and memory that you use for the sole-tenant node, and doesn't include GPUs or Local SSD disks.




For more information, see [Sole-tenant node pricing](https://cloud.google.com/compute/sole-tenant-pricing).

## Availability

  * Sole-tenant nodes are [available in select zones](https://docs.cloud.google.com/compute/docs/regions-zones#available). To verify high-availability, schedule VMs on sole-tenant nodes in different zones.

  * Before using GPUs or Local SSD disks on sole-tenant nodes, make sure you have enough GPU or Local SSD [quota](https://docs.cloud.google.com/compute/resource-usage) in the zone where you are reserving the resource.

  * Compute Engine supports GPUs on `n1`, `g2`, `g4`, `a2-highgpu`, `a2-megagpu`, `a2-ultragpu`, `a3-highgpu`, and `a3-megagpu` sole-tenant node types that are in [zones with GPU support](https://docs.cloud.google.com/compute/docs/regions-zones#available). The following table shows the types of GPUs that you can attach to `n1`, `g2`, `g4`, `a2`, and `a3` nodes and how many GPUs you must attach when you create the node template.

GPU type | GPU quantity | Sole-tenant node type  
---|---|---  
NVIDIA A100 40GB | 8 | `a2-highgpu`  
NVIDIA A100 40GB | 16 | `a2-megagpu`  
NVIDIA A100 80GB | 8 | `a2-ultragpu`  
NVIDIA H100 | 8 | `a3-highgpu`  
NVIDIA H100 | 8 | `a3-megagpu`  
NVIDIA L4 | 8 | `g2`  
NVIDIA RTX PRO 6000 | 8 | `g4`  
NVIDIA P4 | 4 | `n1`  
NVIDIA T4 | 4 | `n1`  
NVIDIA V100 | 8 | `n1`  
  * Compute Engine supports Local SSD disks on `n1`, `n2`, `n2d`, `g2`, `g4`, `a2-ultragpu`, `a3-highgpu`, and `a3-megagpu` sole-tenant node types that are used in [zones that support those machine series](https://docs.cloud.google.com/compute/docs/regions-zones#available).




## Restrictions

  * You can't use sole-tenant VMs with the following machine series and types: [T2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2d_machines), [T2A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines), [E2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2_machine_types), [C2D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#c2d_machine_types), [A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms), [A3 Edge](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-edge-vms), [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms), [A4X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms), or bare metal instances.

  * Sole-tenant VMs can't [specify a minimum CPU platform](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform).

  * You can't [migrate a VM to a sole-tenant node](https://docs.cloud.google.com/compute/docs/nodes/updating-vm-tenancy) if that VM specifies a minimum CPU platform. To migrate a VM to a sole-tenant node, [remove the minimum CPU platform specification by setting it to automatic](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform) before updating the VM's node affinity labels.

  * Sole-tenant nodes don't support [preemptible VM instances](https://docs.cloud.google.com/compute/docs/instances/preemptible).

  * For information about the limitations of using Local SSD disks on sole-tenant nodes, see [Local SSD data persistence](https://docs.cloud.google.com/compute/docs/disks/local-ssd#data_persistence).

  * For information about how using GPUs affects live migration, see the [limitations of live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process#limitations).

  * Confidential VMs that don't support live migration have different behavior and restrictions with the three types of sole-tenant node maintenance policies. For more information, see Host maintenance policy and [troubleshoot live migration for Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/troubleshoot-live-migration).

  * Sole-tenant nodes with GPUs don't support VMs without GPUs.

  * Only N1, N2, N2D, and N4 sole-tenant nodes support overcommitting CPUs.

  * C3, C3D, C4, C4A, C4D, G4, N4, and M4 VMs are scheduled with alignment to the underlying NUMA architecture of the sole-tenant node. Scheduling full and sub-NUMA VM shapes on the same node might lead to fragmentation, whereby a larger shape can't be run while several smaller shapes totaling the same resource requirements can.

  * C3 and C4 sole-tenant nodes require that VMs have the same vCPU-to-memory ratio as the node type—for example—you can't place a `c3-standard` VM on a `-highmem` node type.

  * You can't update the maintenance policy on a live node group.




## What's next

  * Learn how to [create, configure, and consume your sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms).

  * Learn how to [overcommit CPUs on sole-tenant VMs](https://docs.cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-vms).

  * Learn how to [bring your own licenses](https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses).

  * Review our [best practices for using sole-tenant nodes to run VM workloads](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-best-practices).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
