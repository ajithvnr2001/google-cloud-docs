---
url: https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs/
title: About regional MIGs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:24.534022+00:00
---

# About regional MIGs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About regional MIGs Stay organized with collections  Save and categorize content based on your preferences. 

A [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) that spreads its VMs across multiple zones in a [region](https://docs.cloud.google.com/docs/geography-and-regions) is also known as a _regional MIG_. A MIG that is confined to a single zone is also known as a _zonal MIG_.

You can use a regional MIG to increase the resilience of your MIG-based workload. Spreading your workload across multiple zones in a region helps protect you from extreme cases where all instances in a single zone fail.

This document contains conceptual information about regional MIGs:

  * Why to choose a regional MIG instead of a zonal MIG
  * Regional configuration options
  * Behavior differences from zonal MIGs
  * How to increase availability by overprovisioning



To learn how to create a regional MIG, see [Creating a MIG in multiple zones](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups).

## Why choose regional managed instance groups?

Google recommends regional MIGs over zonal MIGs for the following reasons:

  * You can use regional MIGs to manage up to 2,000 instances, twice as many as zonal MIGs. If you need more, you can further [increase the size limit](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#increase_the_groups_size_limit) of a regional MIG to 4,000 instances.
  * You can use regional MIGs to spread your application load across multiple zones, rather than confining your application to a single zone or managing multiple zonal MIGs across different zones.



Using multiple zones protects against zonal failures and unforeseen scenarios where an entire group of instances in a single zone malfunctions. If that happens, your application can continue serving traffic from instances running in another zone in the same region.

In the case of a zonal failure, or if a group of instances in a zone stops responding, a regional MIG continues supporting your instances as follows:

  * The number of instances that are part of the regional MIG in the remaining zones continue to serve traffic. No new instances are added and no instances are redistributed (unless you set up autoscaling).

  * After the failed zone has recovered, the MIG starts serving traffic again from that zone.




When designing for robust and scalable applications, use regional MIGs.

## Additional configuration options for regional MIGs

Creating a regional MIG is similar to [creating a zonal MIG](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig), except that you have additional options:

  * You can select which zones within a region to create VMs in.
  * You can choose a target distribution shape to determine how to distribute instances across selected zones.
  * You can choose to disable or re-enable proactive instance redistribution, which attempts to evenly spread the group's VMs across selected zones.



These options are described in the following sections.

### Zone selection

By default, a regional MIG distributes its [managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#what_is_a_managed_instance) evenly across three zones. For various reasons, you might want to select specific zones for your application. For example, if you require GPUs for your instances, you might only select [zones](https://docs.cloud.google.com/compute/docs/regions-zones#available) that support GPUs, or you might have existing persistent disks or [reservations](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources) that are only available in certain zones.

If you want to choose the number of zones or choose the specific zones the group runs in, you must do that when you first create the group. After you choose specific zones during creation, you can't change or update the zones later.

If you want your MIG to automatically use zones that support the hardware that you specify in your [MIG's configuration](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#configuration_components_for_vms_in_a_mig), you can set the MIG's target distribution shape to `BALANCED`, `ANY`, or `ANY_SINGLE_ZONE` and select all zones in a region. The MIG automatically checks for resource availability and schedules instances only in zones that have the resources. For more information, see [Target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape).

  * To select more than three zones within a region, you must explicitly specify the individual zones. For example, to select all four zones within a region, you must provide all four zones explicitly in your request. If you don't, Compute Engine selects three zones by default.

  * To select two or fewer zones in a region, you must explicitly specify the individual zones. Even if the region only contains two zones, you must still explicitly specify the zones in your request.




Google regularly expands its infrastructure by making specialized hardware available in more zones. A regional MIG periodically checks hardware availability and automatically starts scheduling instances in zones which support required machines. If for any reason you don't want to run your instances in some zones, don't select those zones when creating your group.

To learn how to create a regional MIG and select zones, see [Creating a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups).

### Target distribution shape

By default, a regional MIG distributes its [managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#what_is_a_managed_instance) evenly across selected zones. But if you need hardware that is not available in all zones, or if you need to prioritize the use of zonal [reservations](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources), you might prefer a different distribution.

To configure how your regional MIG distributes its instances across selected zones within a region, [set the MIG's target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape). The following options are available:

  * **EVEN** (default): the group creates and deletes VMs to achieve and maintain the same number of VMs across the selected zones. In an `EVEN` distribution, the number of VMs does not differ by more than 1 between any two zones. Recommended for highly available serving workloads. 
  * **BALANCED** : the group prioritizes creation of VMs in zones where resources are available, while distributing VMs as evenly as possible across selected zones to minimize the impact of zonal failure. Recommended for highly available serving or batch workloads. 
  * **ANY** : the group picks zones for creating VM instances to fulfill the requested number of VMs within present resource constraints and to maximize utilization of unused zonal reservations. Recommended for batch workloads that do not require high availability. 
  * **ANY SINGLE ZONE** : the group creates all VM instances within a single zone. The zone is chosen based on hardware support, current resource and quota availability, and matching reservations. Recommended in combination with a [ compact instance placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies) for workloads that require extensive communication between VMs. 



When you create your MIG, if you set its shape to `BALANCED`, `ANY`, or `ANY_SINGLE_ZONE`, you don't need to manually verify which zones support the hardware that you specify in the [MIG's configuration](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#configuration_components_for_vms_in_a_mig). You can select all zones in a region and, with its shape set to `BALANCED`, `ANY`, or `ANY_SINGLE_ZONE`, your regional MIG checks resource availability for you and schedules instances only in zones that have the resources.

Choose an option based on your workload requirements and which MIG capabilities you need. For more information, see the [comparison table](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape#comparison_of_shapes) and [use cases](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape#use_cases).

To learn how to configure the target shape for a new or existing MIG, see [Setting a policy for distributing instances across zones](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape).

### Proactive instance redistribution

By default, a regional MIG attempts to maintain an even distribution of instances across zones in the region to maximize the availability of your application in the event of a zone-level failure.

If you [delete](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) or [abandon](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#abandoning_instances) instances from your group, causing uneven distribution across zones, the group proactively redistributes instances to reestablish an even distribution.

To reestablish an even distribution across zones, the group deletes instances in zones with more instances, and adds instances to zones with fewer instances. The group automatically picks which instances to delete.

**Caution:** Automatic redistribution happens immediately and might lead to a temporary loss of capacity.[ ![Proactive redistribution reestablishes even distribution across zones.](https://docs.cloud.google.com/static/compute/images/rmig-proactive-redistribution-enabled.svg)](https://docs.cloud.google.com/static/compute/images/rmig-proactive-redistribution-enabled.svg) **Example of proactive redistribution**

For example, suppose you have a regional MIG with 12 instances spread across 3 zones: `a`, `b`, and `c`. If you delete 3 managed instances in `c`, the group attempts to rebalance so that the instances are again evenly distributed across the zones. In this case, the group deletes 2 instances (one from `a` and one from `b`) and creates 2 instances in zone `c`, so that each zone has 3 instances and even distribution is achieved. There is no way to selectively determine which instances are deleted. The group temporarily loses capacity while the new instances start up.

To prevent automatic redistribution of your instances, you can [turn off proactive instance redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution).

Turning off proactive instance redistribution is useful when you need to:

  * Delete or abandon instances from the group without affecting other running instances. For example, you can delete a batch worker instance after job completion without affecting other workers.
  * Protect instances with stateful workloads from undesirable automatic deletion due to proactive redistribution.
  * Set the MIG's target distribution shape to `BALANCED` or `ANY_SINGLE_ZONE`

**Caution:** If you turn off proactive instance redistribution and manually delete managed instances, which can result in an uneven distribution across zones, your regional MIG might not have sufficient capacity to handle failover traffic in case of zonal failure.[ ![Disabling proactive redistribution can affect capacity during a
            zonal failure.](https://docs.cloud.google.com/static/compute/images/rmig-proactive-redistribution-disabled.svg)](https://docs.cloud.google.com/static/compute/images/rmig-proactive-redistribution-disabled.svg) _Uneven distribution after disabling proactive redistribution_

If you turn off proactive instance redistribution, a MIG does not proactively add or remove instances to achieve balance but still opportunistically converges toward balance during resize operations, treating each resize operation as an opportunity to balance the group. For example, when scaling in, the group automatically uses the rescaling as an opportunity to remove instances from bigger zones; when scaling out, the group uses the opportunity to add instances to smaller zones.

## MIG behavior when an initial instance creation fails

If a regional MIG fails to create an instance during the initial attempt, then the MIG finds alternative capacity depending on the target distribution shape as follows:

  * For a MIG with `BALANCED` or `ANY` target distribution shape, the MIG automatically attempts to find capacity in other selected zones. This can help improve the obtainability of resources for your workloads. When you configure different machine types in your MIG using [instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility), this default behavior further improves your chances to obtain capacity, because the MIG can search for available capacity across various machine types and zones.

  * For a MIG with `EVEN` or `ANY_SINGLE_ZONE` target distribution shape, or with a stateful configuration, the MIG continues to retry creating the instance in the same zone where the initial attempt failed. It does not search for capacity in other selected zones. To improve your chances to obtain capacity, you can configure instance flexibility in the MIG. With instance flexibility, if the initial instance creation fails, then the MIG tries creating the instance with other machine types specified in the instance flexibility policy.




## Behavior differences from zonal MIGs

The main difference between a zonal MIG and a regional MIG is that a regional MIG can use more than one zone.

Because a regional MIG's [managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#what_is_a_managed_instance) are distributed across zones within a region, the following MIG features behave a bit differently.

  * Autoscaling
  * Automatic updates



### Autoscaling a regional MIG

Compute Engine offers [autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler) for MIGs, which allows your groups to automatically add VMs (scale out) or remove VMs (scale in) based on increases or decreases in load.

If you enable autoscaling for a regional MIG, then the feature behaves as follows:

  * The autoscaler distributes VMs across the zones based on the target distribution shape that you set.

  * The autoscaler is aware of the resource availability across zones. The autoscaler proactively creates VMs only in zones that have enough quota and capacity for VMs as specified in the [MIG's configuration](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#configuration_components_for_vms_in_a_mig). This behavior might cause an uneven distribution of VMs in the case of `EVEN` target distribution shape.

  * If a VM creation fails due to lack of capacity in a zone, then the MIG creates the VM in a zone where capacity is available.




### Updating a regional MIG

You can't change or update the zones for a regional MIG after the group is created. But you can [set the group's target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape) to prioritize the use of different zones—for example, if you have reserved resources or need hardware that is not available in all zones.

If you want to apply a new template to a regional MIG, see [Updating a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#updating_a_regional_managed_instance_group).

If you want to add or remove instances in a MIG, the process is similar for regional and zonal MIGs. See [Add and remove VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig).

If you're interested in configuring stateful disks or stateful metadata in a MIG, see [Configuring stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs).

## How to increase availability by overprovisioning

A variety of events might cause one or more instances to become unavailable, and you can help mitigate this issue by using multiple Google Cloud services:

  * Use a regional MIG with an `EVEN` or `BALANCED` target distribution shape to distribute your application across multiple zones.
  * Use application-based [autohealing](https://docs.cloud.google.com/compute/docs/instance-groups#autohealing) to recreate instances with failed applications.
  * Use [load balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) to automatically direct user traffic away from unavailable instances.



However, even if you use these services, your users might still experience issues if too many of your instances are simultaneously unavailable.

To be prepared for the extreme case where one zone fails or an entire group of instances stops responding, Google strongly recommends overprovisioning your MIG. Depending on your application needs, overprovisioning your group prevents your system from failing entirely if a zone or group of instances becomes unresponsive.

Google makes recommendations for overprovisioning with the priority of keeping your application available for your users. These recommendations include provisioning and paying for more instances than your application might need on a day-to-day basis. Base your overprovisioning decisions on application needs and cost limitations.

You can set your MIG's size when [creating it](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups), and you can [add or remove](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig) instances after you've created it.

You can configure an autoscaler to automatically add and remove instances in the group based on the load.

### Estimating the recommended group size

We recommend that you provision enough instances so that, if all of the instances in any one zone become unavailable, your remaining instances would still meet the minimum number of instances that you require.

**Note:** The following recommendations for group size assume that your regional MIG uses proactive instance redistribution, which is enabled by default. 

If you [disable proactive instance redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution), the instances in your group might not be evenly distributed across zones. In case of a zonal failure, your group might not have sufficient capacity in remaining zones to handle failover traffic. 

Use the following table to determine the minimum recommended size for your group:

Number of zones | Additional VM instances | Recommended total VM instances | 2 | +100% | 200%  
---|---|---  
3 | +50% | 150%  
4 | +33% | 133%  
  
### Provisioning a regional MIG in three or more zones

When you create a regional MIG in a region with at least three zones, Google recommends overprovisioning your group by at least 50%. By default, a regional MIG creates instances in three zones. Having instances in three zones already helps you preserve at least 2/3 of your serving capacity, and if a single zone fails, the other two zones in the region can continue to serve traffic without interruption. By overprovisioning to 150%, you can ensure that if 1/3 of the capacity is lost, 100% of traffic is supported by the remaining zones.

For example, if you need 20 instances in your MIG across three zones, we recommend, at a minimum, an additional 50% of instances. In this case, 50% of 20 is 10 more instances, for a total of 30 instances in the group. If you create a regional MIG with a size of 30, the group distributes your VMs across the three zones, like so:

Zone | Number of VM instances | example-zone-1 | 10  
---|---  
example-zone-2 | 10  
example-zone-3 | 10  
  
If any single zone fails, you still have 20 instances serving traffic.

### Provisioning a regional MIG in two zones

To provision your instances in two zones instead of three, Google recommends doubling the number of instances. For example, if you need 20 instances for your service, distributed across two zones, we recommend that you configure a regional MIG with 40 instances, so that each zone has 20 instances. If a single zone fails, you still have 20 instances serving traffic.

Zone | Number of VM instances | example-zone-1 | 20  
---|---  
example-zone-2 | 20  
  
If the number of instances in your group is not equally divisible across two zones, Compute Engine evenly divides the group of VMs and randomly puts the remaining instances in one of the zones.

### Provisioning a regional MIG in one zone

You can create a regional MIG with just one zone. This is similar to creating a [zonal MIG](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig).

Creating a single-zone regional MIG is not recommended because it offers the minimum guarantee for highly available applications. If the zone fails, your entire MIG is unavailable, potentially disrupting your users.

## Monitor instance distribution across zones

To observe how your regional MIG allocates and balances instances across zones over time, you can use the **GCE MIG Instance Distribution Monitoring** dashboard in Cloud Monitoring. This preconfigured dashboard helps you to verify that your instance distribution is working as intended. You can use these insights to identify potential adjustments to optimize your infrastructure.

To learn how to access the monitoring dashboard, see [Monitor instance distribution in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution).

## What's next

  * [Create a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups)
  * [Monitor instance distribution in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution).
  * Learn how to build [scalable and resilient web applications](https://docs.cloud.google.com/solutions/scalable-and-resilient-apps).
  * Learn about [disaster recovery on Google Cloud Platform](https://docs.cloud.google.com/solutions/disaster-recovery-cookbook).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
