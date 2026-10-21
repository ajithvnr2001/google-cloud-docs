---
url: https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape/
title: Regional MIG target distribution shape \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:43:34.589992+00:00
---

# Regional MIG target distribution shape  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Regional MIG target distribution shape Stay organized with collections  Save and categorize content based on your preferences. 

By default, a [regional managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs) distributes its managed virtual machine (VM) instances evenly across selected zones. But if you need hardware that is not available in all zones or that might be temporarily unavailable in selected zones, or if you need to prioritize the use of zonal reservations, you might prefer a different distribution.

To configure how a regional MIG distributes your [managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#what_is_a_managed_instance) across [selected zones](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#selectingzones) within a region, [set the MIG's target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape). The following options are available:

  * **EVEN** (default): the group creates and deletes VMs to achieve and maintain the same number of VMs across the selected zones. In an `EVEN` distribution, the number of VMs does not differ by more than 1 between any two zones. Recommended for highly available serving workloads. 
  * **BALANCED** : the group prioritizes creation of VMs in zones where resources are available, while distributing VMs as evenly as possible across selected zones to minimize the impact of zonal failure. Recommended for highly available serving or batch workloads. 
  * **ANY** : the group picks zones for creating VM instances to fulfill the requested number of VMs within present resource constraints and to maximize utilization of unused zonal reservations. Recommended for batch workloads that do not require high availability. 
  * **ANY SINGLE ZONE** : the group creates all VM instances within a single zone. The zone is chosen based on hardware support, current resource and quota availability, and matching reservations. Recommended in combination with a [ compact instance placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies) for workloads that require extensive communication between VMs. 



Choose an option based on your workload requirements and which MIG capabilities you need. See the comparison table, use cases, and how distribution shapes work.

## Comparison of shapes

For each possible target shape, the following table describes its intended workloads, purpose, distribution of managed instances, feature support, and a brief description of MIG behavior when faced with unavailable resources.

| **`EVEN`** (default) | **`BALANCED`** | **`ANY`** | **`ANY_SINGLE_ZONE`**  
---|---|---|---|---  
Intended workloads | Highly available serving workloads (stateless or stateful)  | Highly available serving workloads (stateless or stateful)  
  
Highly available batch workloads | Batch workloads | Batch workloads requiring extensive communication between VMs  
Purpose | Minimize the impact of zone-level failure, assuming sufficient availability of resources in each zone. | Minimize the impact of zone-level failure as much as possible considering availability of resources in each zone.  | Prioritize resource acquisition and utilization of unused [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview). | Minimize network latency and [costs](https://docs.cloud.google.com/vpc/network-pricing#egress-within-gcp) between VMs by keeping all VMs in one zone.  
Target distribution of [managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances) across zones | Even.  
  
The number of managed instances does not differ by more than 1 between any two zones, regardless of resource availability.*  
  
Some managed instances might not be up and running in case of zonal capacity constraints. | As even as possible.  
  
No guarantee on discrepancies in the number of VMs across zones, which depends on current resource availability.  
  
When resources are available, the distribution is similar to `EVEN`. In the worst case of resource constraints, the distribution can take any shape. | Any.  
  
Each zone can have a different number of managed instances (including all or none). | Single zone.  
  
All instances are created within one zone. The MIG chooses the zone whenever it scales out from zero VMs.  
**Feature support** | **`EVEN`** (default) | **`BALANCED`** | **`ANY`** | **`ANY_SINGLE_ZONE`**  
[Autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler) |  |  |  |   
[Canary updates](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#canary_updates) |  |  |  |   
[Instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility) |  |  |  |   
[Proactive instance redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#proactive_instance_redistribution) |  |  | Not applicable |   
[Reservations](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources) | Maximally utilized within each zone independently.   
  
Reservations don't impact how instances are distributed. | Maximally utilized within each zone independently.   
  
If reservations are present they might help arriving at a balanced distribution. | Maximally utilized within the region.   
  
The group prioritizes using up reservations in the region. | Maximally utilized within the chosen zone.  
  
Whenever the group has no VMs and needs to create one or more VMs, the group prioritizes the zone with the most reservations if that zone also has sufficient resources and supports the hardware to fulfill the request.  
Instance template and stateful configuration hardware requirements (machine type, CPU, GPU, existing disks) | Selected hardware must be [available](https://docs.cloud.google.com/compute/docs/regions-zones#available) in all selected zones. | Selected hardware must be [available](https://docs.cloud.google.com/compute/docs/regions-zones#available) in at least one selected zone. | Selected hardware must be [available](https://docs.cloud.google.com/compute/docs/regions-zones#available) in at least one selected zone. | Selected hardware must be [available](https://docs.cloud.google.com/compute/docs/regions-zones#available) in at least one selected zone.  
[Sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes) |  |  |  |   
**Handling failures** | **`EVEN`** (default) | **`BALANCED`** | **`ANY`** | **`ANY_SINGLE_ZONE`**  
Temporary unavailability of resources in a zone | Exposed  
  
Creates new managed instances in zones with fewer managed instances. Keeps retrying to create VM instances in a zone where resources are unavailable until it succeeds.  
  
Risk: Can't create VMs in a zone with limited resources. | Resilient  
  
Creates new managed instances in zones where resources are available, while distributing instances as evenly as possible across zones.  
  
Risk: VMs might not be distributed evenly across zones. | Resilient  
  
Creates new managed instances in zones where resources are available and to maximize utilization of unused reservations.  
  
Risk: VMs might not be distributed evenly across zones. | Resilient on group creation and resizes from zero  
  
Creates new VM instances within a single zone, where resources are available.  
  
Risk: Can't guarantee all additional instances are successfully created during scale-out requests if the chosen zone does not have enough resources.  
Zone-level failure | Resilient  
  
Impact is minimized because instances in healthy zones keep serving.   
  
Impact is further minimized if you [provision extra](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#overprovision) instances, sufficient to tolerate losing one zone. | Resilient  
  
Impact is minimized because instances in healthy zones keep serving.   
  
Impact is further minimized if you [provision extra](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#overprovision) instances, sufficient to tolerate losing one zone. | Exposed  
  
Outage might happen if the majority or all instances are concentrated in a failed zone. | Exposed  
  
Outage is inevitable if the failure happens in the chosen zone.  
  
*You might see an uneven distribution of instances if you add or remove instances when proactive instance redistribution is disabled. Uneven distribution might also happen in an autoscaled MIG if a zone fails or lacks capacity.

## Use cases

Review the feature support, then choose a distribution shape based on your use case.

### Prioritize workload resilience with an even distribution

If you run a highly available serving application that must survive zone-level failure without degraded performance, use the `EVEN` target distribution shape with an [over-provisioned group size](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#overprovision). Overprovisioning the number of instances in a group protects your workload from zone-level failure.

Depending on your workload, consider [creating an autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#create_an_autoscaler) to automatically add or remove instances to your group when load increases or decreases.

To learn more about the `EVEN` target distribution shape, see the comparison of target shapes and read How the `EVEN` target shape works.

For more information about deploying highly available workloads on regional MIGs, see the following sections:

  * If you need special hardware that is only available in specific zones, [select zones for your VMs](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#selectingzones).
  * [Provision the correct managed instance group size](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#overprovision).
  * If you want to prevent unintended deletion of instances when you manually delete or abandon instances from a regional group, [turn off cross-zone instance redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution).
  * [Configure autoscaling for a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#autoscaling_a_regional_mig), which tries to preserve an even balance across zones on group resizes and scales out to available zones in case of zone-level failure.
  * [Configure load balancing](https://docs.cloud.google.com/load-balancing/docs), which shifts load to healthy zones in case of zone-level failure and, if autoscaling is configured, leads to an increase in the number of VMs in zones where load grows.
  * [Configure a stateful regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs), which can preserve the unique state of each of your MIG's instances, including VM instance name, persistent disks, and metadata, on machine restart, recreation, autohealing, or update events.



### Balance resource acquisition with an even distribution

If you run a highly available serving or batch workload and need to balance acquisition of resources against an even distribution of VM instances across selected zones in a region, use the `BALANCED` target distribution shape.

The `BALANCED` shape prioritizes acquisition of resources—the group creates instances in zones where resources are available—while distributing instances as evenly as possible across zones to minimize the impact of zone-level failure.

If you run a batch workload that doesn't need to be protected against zone-level failure, use the `ANY` target shape instead. The `ANY` shape prioritizes acquisition of resources as well as use of zonal reservations.

With the shape set to `BALANCED` or to `ANY`, you don't need to manually verify whether specific hardware is [available](https://docs.cloud.google.com/compute/docs/regions-zones#available) in a particular zone. You can [select](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#selectingzones) all zones in a region and the group automatically deploys instances in zones where your required hardware is available.

To learn more about the `BALANCED` target distribution shape, see the comparison of target shapes and read How the `BALANCED` target distribution shape works.

**Caution:** If you set the distribution shape to `BALANCED`, the MIG attempts to spread instances evenly across selected zones. But an even distribution might not be achieved due to constraints in resource availability. This can be especially true for large machines, or [specialized hardware](https://docs.cloud.google.com/compute/docs/regions-zones#available) (such as GPU or CPU platforms). In case of resource constraints, your group might deploy the majority of your instances in a single zone or in two zones. If a zone-level failure happens in this zone, your workload might lose the majority of serving VMs, causing an outage. We advise you to monitor your setups and when observing substantial imbalance, try to configure your workload in another region or pick hardware configurations that are more commonly available.

### Prioritize resource acquisition

If you run batch workloads and if getting the requested number of instances to perform the processing is more important for you than [workload resilience to zone-level failures](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#overprovision), use the `ANY` target distribution shape.

If you have matching [reservations](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources), set your target shape to `ANY` to prioritize the use of zones that contain the matching reservations. To learn how to configure reservations in an instance template, see [Consuming instances from a specific reservation](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources#consuming_instances_from_a_specific_reservation).

Similar to the `BALANCED` target shape, the `ANY` shape is useful when your batch workload requires any of the following features:

  * **VMs with special hardware** , such as a specific CPU platform or GPU model. The group will deploy instances to the zones that support the requested hardware, according to [resource availability](https://docs.cloud.google.com/compute/docs/regions-zones#available), and with a preference for zones that have matching reservations.
  * **Preemptible VMs**. You won't need to explore which zones have preemptible capacity available. The group will deploy to zones with preemptible capacity automatically.
  * **VMs with a large number of cores**. The group will get large machines where they are available, with a preference for zones that have matching reservations.



You don't need to manually verify whether specific hardware is available in a particular zone. You can [select](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#selectingzones) all zones in a region and the group automatically deploys instances in zones where your required hardware is available.

**Note:** Availability of preemptible capacity is not guaranteed within a region.

You can [selectively delete](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) batch job worker instances that have completed calculations without affecting other workers. Unlike a group with an `EVEN` target shape and proactive redistribution, a group with `ANY` target shape doesn't have to achieve an even balance and won't trigger redistribution.

**Caution:** Don't use the `ANY` target distribution shape for services and highly available workloads. When the target shape is set to `ANY`, your regional group might deploy the majority of your instances in a single zone. If a zone-level failure happens in this zone, your workload will lose the majority of serving VMs, causing an outage. To minimize the impact of zone-level failure, use an `EVEN` or `BALANCED` target distribution shape.

To learn more details about the `ANY` target distribution shape, see the comparison of target shapes and read how the `ANY` target distribution shape works.

### Minimize networking across VMs

If you run a batch workload and want to place all VMs in a single zone to reduce VM-to-VM network latency and costs, and if you don't have a specific zone requirement, set the group's target shape to `ANY_SINGLE_ZONE`. You can also [create a compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies#create-compact-policy) and [apply it](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies#apply-mig) to your MIG so that the VMs in the MIG are located closer to each other and on the same network infrastructure.

When you create a MIG with at least one VM, and whenever a MIG with no VMs needs to scale out again, the `ANY_SINGLE_ZONE` shape picks the optimal zone based on your reservations, quotas, and hardware requirements.

Similar to the `BALANCED` and `ANY` target shapes, the `ANY_SINGLE_ZONE` shape is useful when your batch workload requires any of the following features:

  * **VMs with special hardware** , such as a specific CPU platform or GPU model. The group will deploy instances to a zone that supports the requested hardware, according to [resource availability](https://docs.cloud.google.com/compute/docs/regions-zones#available), and with a preference for the zone that has matching reservations.
  * **Preemptible VMs**. You won't need to explore which zones have preemptible capacity available. The group will deploy to a zone with preemptible capacity automatically.
  * **VMs with a large number of cores**. The group will get large machines where they are available, with a preference for the zone that has matching reservations.



You don't need to manually verify whether specific hardware is available in a particular zone. When creating the MIG, [select](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#selectingzones) all zones in a region and the group automatically deploys instances in a zone where your required hardware is available.

To learn more details about the `ANY_SINGLE_ZONE` target distribution, see the comparison of target shapes and read how the `ANY_SINGLE_ZONE` target distribution shape works.

If you have specific zone requirements and don't want your MIG to switch zones under any circumstance, use a [zonal MIG](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig) instead.

**Caution:** Don't use the `ANY_SINGLE_ZONE` target distribution shape for services and highly available workloads. When the target shape is set to `ANY_SINGLE_ZONE`, your regional group deploys all of your instances in a single zone. If a zone-level failure happens in this zone, your workload will lose all serving VMs, causing an outage. The MIG does not attempt to recreate any unreachable VMs in another zone. To minimize the impact of zone-level failure, use an `EVEN` or `BALANCED` target distribution shape instead.

## How it works

This section describes how each target distribution shape works in the following situations:

  * When you resize the MIG
  * In case resources are temporarily unavailable in a zone
  * In case of zonal failure



### The `EVEN` distribution shape

With a target distribution shape set to `EVEN` and proactive redistribution enabled, the number of managed instances in a regional MIG does not differ by more than 1 between any two zones, regardless of resource availability. But a managed instance might not be up and [running](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_instances) if its zone lacks the resources to provision an actual VM. If the initial creation of an instance fails, then the MIG continuously retries to create the instance in the same zone.

#### Resizing a MIG that has an `EVEN` distribution shape

A group with an `EVEN` target shape picks zones for adding or deleting instances in a way that preserves or converges to an even balance of managed instances across zones.

For example, the following diagram shows how a group adds and removes managed instances.

[ ![The even target shape evenly adds and removes instances across zones.](https://docs.cloud.google.com/static/compute/images/rmig-target-shape-even-resizing.svg)](https://docs.cloud.google.com/static/compute/images/rmig-target-shape-even-resizing.svg) Resizing a MIG that has an `EVEN` distribution

#### Impact of temporarily unavailable resources

Resources might be temporarily unavailable in a zone when you create the group or increase the number of instances. For example, if you request preemptible instances or specialized hardware in a limited supply, those resources might not be available at the time of your request.

With the goal of maintaining an even distribution of instances across zones, the group continues attempting to create VM instances in zones where the resources are temporarily unavailable. Eventually, the group does acquire the full number of running VM instances after the resources become available.

For example, the following diagram shows what happens in a MIG if one of the zones can't fulfill your request due to a temporary unavailability of resources.

[ ![With an even target shape, if VMs are not available, autohealing continuously attempts to create them until they are available.](https://docs.cloud.google.com/static/compute/images/rmig-target-shape-even-unavailable.svg)](https://docs.cloud.google.com/static/compute/images/rmig-target-shape-even-unavailable.svg) Impact of temporarily unavailable resources on a MIG that has an `EVEN` distribution

However, if you've configured autoscaling in the MIG, then the MIG creates instances in the zones where capacity is available. This might result in an uneven distribution of instances across zones. This behavior is similar to MIGs with the `BALANCED` distribution shape.

#### Impact of zone-level failure

If you use the `EVEN` (or `BALANCED`) target distribution shape, you can [provision extra instances](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#overprovision) to minimize impact of a zone-level failure.

In case of zone-level failure, a regional MIG that is deployed to 3 zones with an `EVEN` (or `BALANCED`) target distribution shape might lose 1/3 of its instances. You can ensure sufficient capacity to serve your load in case of zone-level failure by provisioning more VMs, 2/3 of which are required by the load.

For example, if you require 8 instances to process requests across 3 zones and you want to protect your workload against zone-level failure, you should create a regional group with 12 instances. The following diagram shows what happens if one zone fails.

[ ![With an even target shape, overprovisioning the MIG maintains a sufficient number of VMs in case of zonal failure.](https://docs.cloud.google.com/static/compute/images/rmig-target-shape-even-zonal-failure.svg)](https://docs.cloud.google.com/static/compute/images/rmig-target-shape-even-zonal-failure.svg) Impact of zonal failure on a MIG that has an `EVEN` distribution

The `EVEN` target distribution shape works well with autoscaling and load balancing under such circumstances. In case of a zone-level failure, the load balancer starts sending traffic to instances in the two remaining zones to accommodate traffic from the failed zone. With autoscaling, the MIG tries to protect your workload by creating instances in zones where capacity is available. This might result in an uneven distribution of instances across zones.

For more information about how a regional MIG works with an autoscaler, see [Autoscaling a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#autoscaling_a_regional_mig).

### The `BALANCED` distribution shape

A regional MIG with a `BALANCED` target shape might not achieve an even distribution across zones, specifically when the requested resources are not available in a zone.

The MIG prioritizes provisioning the requested number of VMs by creating VMs in zones where resources are available. If the initial creation of a VM fails, then the MIG automatically attempts to create the VM in the other selected zones where capacity is available. When resources are available, the distribution is similar to `EVEN`. In the worst case of resource constraints, the distribution can take any shape.

#### Resizing a MIG that has a `BALANCED` distribution shape

**Increasing group size**

With a `BALANCED` target shape, the group chooses zones for creating new instances based on the current availability of the resources that you specified in the MIG's instance template.

  * When resources are sufficiently available in all selected zones, the group maintains an even distribution across zones on size increases, the same way as the `EVEN` target shape.
  * When zonal capacity constraints make it impossible to achieve an even distribution, the group creates instances in the zones where resources are available, while still trying to maximize balance.



For example, you might observe capacity constraints and an uneven distribution if you request a specialized CPU platform, GPU model, or preemptible VMs that are not uniformly available in all zones.

[ ![The balanced target shape adds and removes instances as evenly as possible across zones based on current capacity.](https://docs.cloud.google.com/static/compute/images/rmig-target-shape-balanced-resizing.svg)](https://docs.cloud.google.com/static/compute/images/rmig-target-shape-balanced-resizing.svg) Resizing a MIG that has a `BALANCED` distribution

**Decreasing group size**

When decreasing its size, a Regional MIG with a `BALANCED` target shape removes instances in the following sequence in order to limit disruption to your workload:

  1. Instances that are not running; that is, instances that for any reason can't be created or are being created or autohealed.
  2. Instances in zones where the group has more VMs, to converge to an evenly distributed state.



#### Impact of temporarily unavailable resources or zonal failure

With a `BALANCED` target distribution shape, the group deploys instances to zones where capacity is available. During temporary zonal capacity constraints, this can lead to an uneven distribution of instances across zones.

If in such a situation a zone with the largest number of VM instances fails, your workload might lose a significant share of your serving capacity. If the healthy zones have temporary capacity constraints, the group tries to recreate failed instances in the original location (a failed zone) and this attempt might fail.

To protect your workload against such an extreme case:

  * [Overprovision](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#overprovision) the size of your regional MIG, so that your workload has sufficient serving capacity in the case of a zonal failure.
  * [Reserve](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources) a sufficient amount of resources in each zone to cover peak load, to overprovision, and to maintain an even distribution across zones. This tactic helps ensure that you can get an even distribution of instances across zones, which minimizes capacity loss in case of a zonal failure.



The following diagram shows how a scenario with temporary zonal capacity constraints, followed by a zonal failure, might evolve.

[ ![With a balanced target shape, if VMs are not available the distribution can be uneven. In case of a subsequent zonal failure, autohealing continuously attempts to create failed VMs until they are available.](https://docs.cloud.google.com/static/compute/images/rmig-target-shape-balanced-unavailable.svg)](https://docs.cloud.google.com/static/compute/images/rmig-target-shape-balanced-unavailable.svg) Impact of temporarily unavailable resources, followed by a zonal failure, on a MIG that has a `BALANCED` distribution

If your request can't be fulfilled in any zone in the region, the group schedules VM creation in zones with temporarily unavailable resources. The group continues attempting to create the scheduled instances within the zones where their creation was originally scheduled. If the resources become available in other zones sooner than in the original zone where a VM was scheduled, the group won't try creation in those other zones. You can schedule new instances in zones with available capacity manually by deleting the managed instances that failed to create and resizing the group up to its target size.

If VM creation is unsuccessful, you can [list managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#listing_a_migs_managed_instances) to review the error message in the corresponding managed VM instance or [list recent errors](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#listing_instance_errors).

In case of a zonal failure, the `BALANCED` target distribution shape works well with autoscaling and load balancing. To accommodate traffic from the failed zone, the load balancer sends traffic to instances in the remaining zones. An autoscaler responds to the increased utilization in the zones and automatically creates capacity in healthy zones. For more information, see [Autoscaling a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#autoscaling_a_regional_mig).

### The `ANY` distribution shape

With a target distribution shape set to `ANY`, a regional MIG prioritizes resource acquisition by creating managed instances in zones where resources are available. This means that all of the instances might be created in one zone, or evenly distributed across all zones, or anything between those two scenarios. If the initial creation of an instance fails, then the MIG automatically attempts to create the instance in the other selected zones where capacity is available.

#### Resizing a MIG that has an `ANY` distribution shape

**Increasing group size**

When you increase group size, the group picks any zone where capacity is available.

If you have matching reservations in one or more zones, the group prioritizes utilization of those reservations. However, if you decrease the group size, it might take a few minutes for any [consumed reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_reserved_instances) to be available again for consumption. During this period when previously consumed reservations are not available yet, if you increase the group size and there are no matching reservations, then the group creates VM instances in a zone where resources are available.

**Decreasing group size**

When you decrease group size, the group deletes the VM instances in the following order:

  1. VMs that are not running for any reason
  2. VMs that are not yet updated to the intended version
  3. VMs chosen nondeterministically



If you need to decrease group size in specific zones or remove specific VM instances, for example workers that finished their job, you can [delete specific instances](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) from the group.

#### Impact of temporarily unavailable resources

With a target distribution shape set to `ANY`, the group schedules VM instance creation in zones where the requested resources are available and avoids zones with temporarily unavailable resources.

If your request can't be fulfilled in any zone in the region, the group schedules VM creation in zones with temporarily unavailable resources. The group will keep trying to create the scheduled instances within the zones where their creation was originally scheduled. If the resources become available in other zones sooner than in the original zone where a VM was scheduled, the group won't try creation in those other zones. You can manually schedule new instances in zones with available capacity by deleting the non-running managed instances and resizing the group up to its target size.

If VM creation is unsuccessful, you can [list managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#listing_a_migs_managed_instances) to review the error message in the corresponding VM instance or [list recent errors](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#listing_instance_errors).

For example, the following diagram shows how a regional group schedules instances when a zone can't fulfill your request.

[ ![With a target distribution shape set to ANY, the group creates VMs in zones where the requested resources are available and avoids zones with temporarily unavailable resources.](https://docs.cloud.google.com/static/compute/images/rmig-target-shape-any-unavailable.svg)](https://docs.cloud.google.com/static/compute/images/rmig-target-shape-any-unavailable.svg) Impact of temporarily unavailable resources on a MIG that has an `ANY` distribution

#### Impact of zone-level failure

With its target distribution shape set to `ANY`, the group might deploy the majority or all of its instances in a single zone. In the event of failure in that zone, most or all of the group's instances could become unavailable for the duration of the failure.

In case of a zone-level failure or resources becoming temporarily unavailable, or when for any reason your VM instances are not running, you can delete the individual non-running instances then resize the group back to its necessary size in order to try to get replacement instances in zones with available capacity.

[ ![With a target distribution shape set to ANY, the group creates VMs in zones where the requested resources are available. If resources are not available for any reason, you can decrease the size of the group, then increase the size of the group to try to get the VMs in a different zone.](https://docs.cloud.google.com/static/compute/images/rmig-target-shape-any-zonal-failure.svg)](https://docs.cloud.google.com/static/compute/images/rmig-target-shape-any-zonal-failure.svg) Deleting and recreating instances in a MIG that has an `ANY` distribution, in case of temporarily unavailable resources**Note:** If your workload must survive zone-level failure without temporarily degraded performance, use an `EVEN` or `BALANCED` target distribution shape, and [provision extra capacity](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#overprovision).

### The `ANY_SINGLE_ZONE` distribution shape

A regional MIG with the `ANY_SINGLE_ZONE` target distribution shape automatically selects the optimal zone when the first VM in the group is created. After the first VM is created, all other VMs are created in the same zone. If the initial creation of a VM fails, then the MIG continuously retries to create the VM in the same zone.

The MIG can select a different zone only when it is scaled back to zero VMs and it starts creating its first VM again.

#### Choosing the optimal zone

When only one of the selected zones supports the group's hardware requirements then Compute Engine chooses this zone.

When multiple selected zones support the group's hardware requirements then Compute Engine chooses a zone that has enough available resources to fit all of the regional MIG's VMs, with a preference for the zone with the most matching reservations.

If none of the selected zones has enough available resources or matching reservations to accommodate all VMs then, in order to create as many VMs as possible, Compute Engine chooses the zone with the most available resources and matching reservations, with a preference for the zone with the most matching reservations. The group continues to try to create the remainder of the VMs in the same zone even if resources become available sooner in another zone.

#### Resizing a MIG that has an `ANY_SINGLE_ZONE` distribution shape

**Increasing group size**

If a MIG already has VMs in it and has its target distribution shape set to `ANY_SINGLE_ZONE`, then for all scale-out operations, the MIG places new VMs within the same zone as existing VMs. If there are not enough available resources or reservations to accommodate all additional VMs, the MIG creates as many as possible.

If the MIG has no VMs, then when it is scaled out, it chooses the optimal zone that supports the group's hardware requirements and that utilizes matching reservations.

**Decreasing group size**

When scaling in, a regional MIG with the `ANY_SINGLE_ZONE` distribution shape removes VMs in the following order:

  * VMs that are not in `RUNNING` state are removed first to limit the disruption to your workload. A not-running VM is a VM that for any reason can't be created or is being created or repaired.
  * VMs that don't use the group's latest configuration.
  * VMs chosen nondeterministically



#### Impact of temporarily unavailable resources

A regional MIG with its target distribution shape set to `ANY_SINGLE_ZONE` is susceptible to resource shortages in the selected zone.

If resources become temporarily unavailable in the MIG's chosen zone, the MIG does not automatically switch zones. This means that scale-out and update processes can become disrupted until sufficient resources become available.

#### Impact of zone-level failure

A regional MIG with its target distribution shape set to `ANY_SINGLE_ZONE` is susceptible to zonal failures.

In the unlikely event of a zonal failure in the zone that hosts your regional MIG's VMs, all of the MIG's VMs might become unable to process your workload.

## Monitor target distribution shapes and zonal balance

To observe how your target distribution shape (`EVEN`, `BALANCED`, `ANY`, or `ANY_SINGLE_ZONE`) affects the real-time allocation of instances across zones over time, you can use the **GCE MIG Instance Distribution Monitoring** dashboard in Cloud Monitoring.

This preconfigured dashboard helps you to verify that your instance distribution is working as intended. You can use these insights to monitor and investigate issues during capacity shifts or outages, and identify potential adjustments to optimize your infrastructure or troubleshoot problems.

To learn how to access the monitoring dashboard, see [Monitor instance distribution in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution).

## What's next

  * To learn how to set the target shape on a MIG, see [Setting a policy for distributing VMs across zones](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape).
  * [Monitor instance distribution in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution).
  * Read more about [Regional MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs).
  * Learn about [zonal reservations](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources) of Compute Engine resources.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
