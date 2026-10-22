---
url: https://docs.cloud.google.com/compute/docs/instance-groups/
title: Instance groups \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:05.664502+00:00
---

# Instance groups  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Instance groups Stay organized with collections  Save and categorize content based on your preferences. 

An instance group is a collection of virtual machine (VM) instances that you can manage as a single entity.

Compute Engine offers two kinds of VM instance groups, managed and unmanaged:

  * **Managed instance groups** (MIGs) let you operate apps on multiple identical VMs. You can make your workloads scalable and highly available by taking advantage of automated MIG services, including: autoscaling, autohealing, regional (multiple zone) deployment, and automatic updating.

  * **Unmanaged instance groups** let you load balance across a fleet of VMs that you manage yourself.




##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Compute Engine performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Compute Engine free ](https://console.cloud.google.com/freetrial)

## Managed instance groups (MIGs)

Use a managed instance group (MIG) for scenarios like these:

  * Stateless serving workloads, such as a website frontend
  * Stateless batch, high-performance, or high-throughput compute workloads, such as image processing from a queue
  * Stateful applications, such as databases, legacy applications, and long-running batch computations with checkpointing



Compute Engine maintains each of the MIG's [managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#what_is_a_managed_instance) based on the configuration that you specify in an [instance template](https://docs.cloud.google.com/compute/docs/instance-templates) and optional [stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#stateful_configuration).

For information about how to create a MIG, see [Creating managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).

### Benefits

MIGs offer the following advantages:

  * **High availability**. 
    * **Automatically repairing failed VMs**. If a VM in the group stops, crashes, gets preempted ([Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)), or is deleted by an action not initiated by the MIG, the MIG automatically recreates that VM based on its original configuration (same VM name, same template) so that the VM can resume its work.
    * **Application-based autohealing**. You can also set up an application-based health check, which periodically verifies that your application responds as expected on each of the MIG's instances. If an application is not responding on a VM, the MIG automatically recreates that VM for you. Checking that an application responds is more precise than simply verifying that a VM is up and running.
    * **Regional (multiple zone) coverage**. Regional MIGs let you spread app load across multiple zones. This replication protects against zonal failures. If that happens, your app can continue serving traffic from instances running in the remaining available zones in the same region.
    * **Load balancing**. MIGs work with load balancing services to distribute traffic across all of the instances in the group.
  * **Scalability**. When your apps require additional compute resources, autoscaled MIGs can automatically grow the number of instances in the group to meet demand. If demand drops, autoscaled MIGs can automatically shrink to reduce your costs.
  * **Automated updates**. The MIG automatic updater lets you safely deploy new versions of software to instances in your MIG and supports a flexible range of rollout scenarios, such as rolling updates and canary updates. You can control the speed and scope of deployment as well as the level of disruption to your service.
  * **Support for stateful workloads**. You can use MIGs for building highly available deployments and automating operation of applications with stateful data or configuration, such as databases, DNS servers, legacy monolith applications, or long-running batch computations with checkpointing. Stateful MIGs preserve each instance's unique state (instance name, attached persistent disks, and metadata) on machine restart, recreation, auto-healing, and update events.
  * **Create GPU VMs all at once**. When you have a batch job, such as an AI or ML training, that requires an exact number of GPU VMs, then creating a resize request in a MIG can help you to create the VMs all at once. You can specify the duration for which you want the VMs to run for, thereby improving the obtainability of highly-demanded resources such as GPUs.

[ ![Use a managed instance group to build highly available deployments
            for stateless serving, stateful applications, or batch workloads.](https://docs.cloud.google.com/static/compute/images/mig-overview.svg)](https://docs.cloud.google.com/static/compute/images/mig-overview.svg) Overview of MIG capabilities and common workloads

### Automatic repair and autohealing

Managed instance groups maintain high availability of your applications by proactively keeping your instances available. A MIG automatically repairs failed instances by recreating them.

You might also want to repair instances when an application freezes, crashes, or runs out of memory. Application-based autohealing improves application availability by relying on a health checking signal that detects application-specific issues such as freezing, crashing, or overloading. If a health check determines that an application has failed on a VM, the group automatically recreates that VM instance.

For more information, see [About repairing VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/about-repair).

#### Health checking

The health checks used to monitor MIGs are similar to the health checks used for load balancing, with some differences in behavior. [Load balancing health checks](https://docs.cloud.google.com/compute/docs/load-balancing/health-checks) help direct traffic away from non-responsive instances and toward healthy instances; these health checks do not cause Compute Engine to recreate instances. On the other hand, [managed instance group health checks](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) proactively signal to delete and recreate instances that become `UNHEALTHY`.

For the majority of scenarios, use separate health checks for load balancing and for autohealing. Health checking for load balancing can and should be more aggressive because these health checks determine whether an instance receives user traffic. Because customers might rely on your services, you want to catch non-responsive instances quickly so you can redirect traffic if necessary. In contrast, health checking for autohealing causes MIGs to proactively replace failing instances, so this health check should be more conservative than a load balancing health check.

For more information, see [Set up an application health check and autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs).

### Regional or zonal groups

You can create two types of MIGs:

  * A [zonal MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances), which deploys instances to a single zone.
  * A [regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups), which deploys instances to multiple zones across the same region.



Both types offer all of the advantages of MIGs. Regional MIGs add higher availability by spreading application load across multiple zones, which protects your workload against zonal failure, and regional MIGs offer more capacity. By default, you can create up to 2,000 VMs in a regional MIG and 1,000 VMs in a zonal MIG. If you need more VMs, you can [increase the size limit of your MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#increase_the_groups_size_limit) or [contact support](https://cloud.google.com/support-hub/).

### Load balancing

Google Cloud load balancing can use instance groups to serve traffic. Depending on the type of load balancer you [choose](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer), you can add instance groups to a target pool or to a backend service.

For more information, see [Adding an instance group to a load balancer](https://docs.cloud.google.com/compute/docs/instance-groups/adding-an-instance-group-to-a-load-balancer).

### Autoscaling

MIGs support autoscaling that dynamically adds or removes VM instances from the group in response to increases or decreases in load. You can configure an autoscaling policy to specify how you want to scale the group. In your autoscaling policy, you can set one or more signals to scale the group based on CPU utilization, load balancing capacity, Cloud Monitoring metrics, schedules, or, for zonal MIGs, by using a queue-based workload like [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview).

For more information, read [Autoscaling groups of instances](https://docs.cloud.google.com/compute/docs/autoscaler).

### Automatic updating

You can easily and safely deploy new versions of software to instances in a MIG. The rollout of an update happens automatically based on your specifications: you can control the speed and scope of the update rollout in order to minimize disruptions to your application. You can optionally perform partial rollouts, which allows for canary testing.

See [Updating MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups).

### Support for stateful workloads

You can build highly available deployments of stateful workloads on VMs using stateful managed instance groups (stateful MIGs). Stateful workloads include applications with stateful data or configuration, such as databases, legacy monolith applications, and long-running batch computations with checkpointing.

You can improve uptime and resiliency of such applications with autohealing, [controlled updates](https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig), and multi-zone deployments, while preserving each instance's unique state, including customizable instance name, persistent disks, and metadata.

For more information, read [Stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs).

### Create GPU VMs all at once

You can create a resize request in a MIG with [GPU VMs](https://docs.cloud.google.com/compute/docs/gpus/about-gpus#gpu-machine-types) to create the requested VMs all at once when the requested capacity becomes available. When you create a resize request in a MIG, Compute Engine schedules the creation of the VMs based on the number of requested VMs, their requested run duration, and the availability of the requested resources in the zones of the MIG. Then, at the scheduled delivery of the resources, the MIG creates the requested number of VMs all at once. The VMs run until the end of their run duration or until you delete them.

For more information, see [About resize requests in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig).

### Groups of preemptible instances

For workloads where minimal costs are more important than speed of execution, you can reduce the cost of your workload by using [preemptible VM instances](https://docs.cloud.google.com/compute/docs/instances/preemptible#preemptible-with-instance-groups) in your instance group. Preemptible instances last up to 24 hours, and are preempted gracefully—your application has 30 seconds to exit correctly. Preemptible instances can be deleted at any time, but autohealing will bring the instances back when preemptible capacity becomes available again.

### Containers

You can simplify application deployment by deploying containers to instances in managed instance groups. When you specify a container image in an instance template and then use that template to create a managed instance group, each VM is created with a container-optimized OS that includes Docker, and your container starts automatically on each VM in the group. See [Deploying containers on VMs and MIGs](https://docs.cloud.google.com/compute/docs/containers/deploying-containers).

### Network and subnet

When you create a managed instance group, you must reference an existing instance template. The instance template defines the VPC network and subnet that member instances use. If you omit a VPC network, Google Cloud attempts to use the VPC network named `default` and the automatically-created subnet in the region specified in the template.

For more information, see [Networks and subnets](https://docs.cloud.google.com/vpc/docs/subnets#vpc_networks_and_subnets).

If you want your managed instance group to include VM instances that use IPv6 addressing, you must use either the dual-stack or IPv6-only setting when you create your instance template. For more information, see [Create an instance template with IPv6 addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address#template-ipv6).

### Demo of MIG capabilities

The following 45-minute video presentation, recorded at Google Cloud NEXT '18, contains demos and best practices for setting up, running, and updating scalable and highly available deployments using Compute Engine MIGs.

The video shows you how to deploy a container to a MIG, set up an autohealing policy, use a regional group to protect against a zonal failure, configure autoscaling to meet CPU targets and queue-based demands, and manage canary and rolling updates.

## Unmanaged instance groups

Unmanaged instance groups can contain heterogeneous instances that you can arbitrarily add and remove from the group. Unmanaged instance groups do not offer autoscaling, autohealing, rolling update support, multi-zone support, or the use of instance templates and are not a good fit for deploying highly available and scalable workloads. Use unmanaged instance groups if you need to apply [load balancing](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer) to groups of heterogeneous instances, or if you need to manage the instances yourself. You can add up to 2,000 VMs to a group. If you want to add more than 2,000 VMs to the group, [contact support](https://cloud.google.com/support-hub/).

If you must create unmanaged instance groups, see [Unmanaged instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances).

## Pricing

There is no additional charge for using managed or unmanaged instance groups. You are charged based on the resources that your group uses. For Compute Engine pricing information, see [Pricing](https://cloud.google.com/compute/all-pricing). 

## What's next

  * Learn more about [instance templates](https://docs.cloud.google.com/compute/docs/instance-templates) or [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates) that you can use to configure the VMs in a MIG.

  * Learn more about the [basic scenarios for creating a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#create_managed_group).

  * Learn about [updating MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs) to use a new configuration.

  * Try a tutorial:

    * [Using autohealing for highly available applications](https://docs.cloud.google.com/compute/docs/tutorials/high-availability-autohealing).

    * [Using load balancing for highly available applications](https://docs.cloud.google.com/compute/docs/tutorials/high-availability-load-balancing).

    * [Using autoscaling for highly scalable applications](https://docs.cloud.google.com/compute/docs/tutorials/high-scalability-autoscaling).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
