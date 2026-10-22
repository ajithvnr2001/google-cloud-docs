---
url: https://docs.cloud.google.com/compute/docs/about-infrastructure-flexibility/
title: Optimize compute provisioning \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:55.963311+00:00
---

# Optimize compute provisioning  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/about-infrastructure-flexibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Optimize compute provisioning Stay organized with collections  Save and categorize content based on your preferences. 

Configuring your workloads to rely on a single machine type or zone can limit your ability to access available resources during demand spikes. To optimize compute provisioning and help keep your workloads running during demand spikes, you must design a flexible Compute Engine infrastructure. Infrastructure flexibility lets you specify multiple zones, machine types, or start times instead of one fixed configuration. Compute Engine automatically selects from your preferred options, helping you maximize resource availability, improve price-performance, and safely adopt the latest hardware.

This document explains the dimensions of infrastructure flexibility, its benefits, and how to choose the right approach for your workload. It also describes the relevant Compute Engine features, design considerations, and steps for adoption. This document is intended for solution architects, infrastructure operators, and cloud engineers who design or manage compute infrastructure.

## Infrastructure flexibility

You can design infrastructure flexibility across the following three dimensions:

  * **Location flexibility (where)** : spread Compute Engine instances across multiple zones in a region to maximize access to available resources, or automatically select a single zone with available capacity for latency-sensitive workloads.

  * **Machine type flexibility (what)** : specify a ranked list of compatible machine types, letting your workload use alternatives when needed.

  * **Time flexibility (when)** : queue requests for high-demand resources, such as accelerators, instead of requiring immediate provisioning for workloads that don't need to start immediately.




## Benefits of a flexible infrastructure

Adopting a flexible Compute Engine infrastructure provides the following benefits:

  * **Automates capacity management during demand spikes.** Your workloads automatically find and use resources across multiple machine types and zones. This approach helps ensure that your scaling requests succeed, even if your preferred hardware is temporarily unavailable.

  * **Simplifies capacity management.** You can reduce the operational overhead of manually searching for available hardware. Compute Engine automatically redirects your requests based on your fallback preferences, reducing operational bottlenecks.

  * **Mitigates capacity risks during transition to the latest hardware.** You can configure your deployments to prioritize the latest hardware generations and retain older generations as a fallback. This setting makes it less risky to adopt the latest and highly demanded machines because if the latest ones are unavailable, then your deployment can still automatically request capacity for older machines.

  * **Optimizes cost for baseline and peak traffic.** You can reserve capacity only for your known, baseline traffic and use machine type fallbacks to handle unpredictable spikes. This approach reduces the expense of idle backup capacity. You can also maintain discount coverage across machine series and regions by using compute flexible committed use discounts (CUDs), which prevent on-demand pricing when your workload switches machine series or regions.




## Comparison of flexibility dimensions

You can combine location flexibility with either machine type or time flexibility. However, machine type flexibility and time flexibility are incompatible in a single deployment. You must choose between hardware fallback options or waiting in a queue for resources to become available.

To help you evaluate these options, the following table compares how each flexibility dimension works. For guidance on which approach fits your specific use case, see Workload suitability and recommendations.

| Location flexibility (where) | Machine type flexibility (what) | Time flexibility (when)  
---|---|---|---  
**How it improves availability** | Maximizes access to available resources across multiple zones in a region. | Reduces chances of encountering unavailable resource errors by falling back to alternative, compatible machine types. | Obtains high-demand resources by placing requests in a queue to wait for capacity to become available.  
**Provisioning timeline** | Immediate | Immediate | Queued  
**Provisioning method** | Provisions compute instances based on availability across selected zones. | Provisions compute instances based on availability across selected machine types. | Provisions compute instances when all of the requested capacity is available.  
**Machine type support** | Supports single or multiple machine types across zones. | Uses multiple machine types. | Supports a single machine type only.  
  
## Workload suitability and recommendations

Adopting infrastructure flexibility depends on your workload's architecture and performance requirements. To help you choose the best approach, the following table summarizes the recommended flexibility dimensions and configurations for some common workload types.

Workload type | Flexibility recommendation  
---|---  
Stateless batch processing, Decoupled high-throughput computing (HTC) |  **Location and machine type flexibility** : use instance flexibility policy with one of the following:

  * A regional managed instance group (MIG) with `ANY` distribution shape
  * A regional bulk compute instance creation configured with minimum count to allow partial fulfillment and with `ANY` distribution shape

These approaches let your workloads scale across diverse zones and machine types to maximize resource availability.  
AI/ML training, fine-tuning, and large-scale batch jobs | **Time flexibility** : use provisioning models that use Dynamic Workload Scheduler (DWS). This approach improves access to high-demand resources, such as accelerators, by placing requests in a queue rather than requiring immediate, on-demand provisioning.  
Microservices and web frontends | **Location and machine type flexibility** : use regional MIGs with the `BALANCED` target distribution shape and an instance flexibility policy. Select machine types with matching vCPU and memory counts for predictable autoscaling. Also, enable update on repair so that any recreated compute instance uses the latest instance flexibility configuration.  
High-availability databases | **Location flexibility and machine type flexibility** : use regional MIGs with `BALANCED` target distribution shape to spread replicas across multiple zones for high availability. Prevent performance variance between replicas by choosing machine types that have closely matching performance profiles. **Note:** Use reservations to secure physical capacity for deterministic hardware requirements.  
Strictly latency-bounded systems | **Location flexibility** : use regional MIGs with the `ANY_SINGLE_ZONE` distribution shape. This shape provides location flexibility by searching across all zones in the region to find sufficient capacity, while ensuring all instances are placed within the same zone to maintain low latency.  
  
Flexible configurations can introduce hardware variations that can affect application performance. When you design for flexibility, evaluate the trade-offs between maximizing resource availability and maintaining consistent performance. For guidance, see the following section on Evaluate and adopt flexible infrastructure.

## Core flexibility features in Compute Engine

To automate capacity management, you can implement flexibility across several layers of your infrastructure. Compute Engine provides features that enable location, machine type, and time flexibility. You can configure these features independently or combine them to match your workload requirements.

### Location flexibility features

Location flexibility features maximize resource availability by distributing compute instances across multiple zones in a region. To maximize this benefit, select regions where your preferred machine types are available in all zones.

You can apply location flexibility to the following deployment types:

  * **MIGs:** regional MIGs evaluate real-time capacity during both instance creation and maintenance to provision compute instances where resources are available. If a zone lacks capacity during an instance repair, then the MIGs using the `ANY` or `BALANCED` shapes can automatically recreate the failed compute instance in another zone. For best results, configure your target distribution shape based on your workload goal:

    * **`ANY`:** recommended for maximum availability. Use this shape to maximize resource availability. This shape allocates compute instances to any zone with available capacity and prioritizes unused reservations.

    * **`BALANCED`:** recommended for high availability. Use this shape for HA workloads. It spreads compute instances evenly across zones to protect against zonal outages, while still prioritizing zones where resources are available.

    * **`ANY_SINGLE_ZONE`:** recommended for low latency. Use this shape for strict latency bounds. It allocates all of the compute instances in a MIG into a single zone that has the most available resources.

For more information, see [About regional MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs).

  * **Unmanaged instance groups** : these groups don't natively support location flexibility. Instead, create compute instances in bulk by using the `regionInstances.bulkInsert` API, which can provision up to 5,000 standalone compute instances, with the `ANY_SINGLE_ZONE` target distribution shape. This request creates compute instances in a single zone and you can add them to your unmanaged group. Note that for standalone compute instances, Compute Engine evaluates capacity to select the zone only during the compute instance creation request.

For more information, see [Group unmanaged VMs together](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances).

  * **Standalone compute instances:** use the regional bulk instance creation request (`regionInstances.bulkInsert` API) with a target distribution shape (`ANY`, `BALANCED`, or `ANY_SINGLE_ZONE`) and set a minimum count. The minimum count lets your request provision as many compute instances as possible rather than failing entirely if full capacity isn't immediately available. For standalone compute instances, Compute Engine evaluates capacity to select the zone only during the instance creation request.

For more information, see [About bulk creation of VMs](https://docs.cloud.google.com/compute/docs/instances/multiple/about-bulk-creation).




### Machine type flexibility features

Machine type flexibility features let your deployment use a prioritized list of alternative machine types. If your primary choice is unavailable, then Compute Engine automatically falls back to your secondary machine types. You configure this capability by defining an _instance flexibility policy_ , which consists of a single or a ranked list of multiple _instance selections_.

You can apply an instance flexibility policy to the following deployment types:

  * **MIGs:** attach an instance flexibility policy to a MIG to let the group automatically fall back to alternative hardware during demand spikes. If your MIG uses Spot VMs, this policy automatically prioritizes fallback machine types that offer longer estimated uptimes and a lower risk of preemption. For more information, see [About instance flexibility in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility).

**Important:** The machine types that you specify in an instance flexibility policy overrides the one specified in the MIG's instance template. If you want Compute Engine to provision the machine type from the template, then you must include it in your policy's instance selection.
  * **Unmanaged instance groups:** because these groups don't natively support instance flexibility policies, you can provision the instances using the `regionInstances.bulkInsert` API and then add them to your group. In your API request, include an instance flexibility policy, and specify either a single zone (`locationPolicy.zones.zone`) or use the `ANY_SINGLE_ZONE` target distribution shape. Using the `ANY_SINGLE_ZONE` shape provides the added benefit of location flexibility by automatically selecting the zone with the most available resources. Note that for standalone instances, Compute Engine applies your flexibility policy only during the instance creation request.

For more information about creating compute instances in bulk, see [Create VMs in bulk with instance flexibility](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk-with-instance-flexibility), and to add them to a group, see [Group unmanaged VMs together](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances).

  * **Standalone compute instances:** for workloads that don't require instance groups, such as independent batch processing jobs, you can use the `regionInstances.bulkInsert` API with an instance flexibility policy to provision the compute instances. Note that for standalone instances, Compute Engine applies your flexibility policy only during the instance creation request.

For more information, see [About instance flexibility for VMs created in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/about-instance-flexibility-for-bulk-vms).




#### Scale seamlessly across different machine types

When you configure machine type flexibility, your fallback machine types might have different hardware architectures or disk specifications. If those specifications are incompatible for the machine types in an instance selection, then the provisioning can fail.

To use machine types with incompatible specifications, you must define property overrides in your instance flexibility policy. These overrides ensure that when Compute Engine falls back to an alternative machine type, it automatically applies the correct boot image, disk type, or processor baseline required for that specific hardware. This capability lets your deployment scale across different machine types seamlessly with higher chances of successful provisioning.

**Important:** When you configure machine type flexibility in a MIG, the machine types, disks, and CPU platforms that you specify in an instance flexibility policy override the ones specified in the MIG's instance template. The MIG continues to use the remaining instance properties from the template.

For more information, see [How disk and CPU platform overrides work](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility#overrides).

### Time flexibility features

**Important:** You can't combine time flexibility features with machine type flexibility in the same deployment.

Time flexibility features let your workloads that don't need to start immediately wait for high-demand resources, such as accelerators, instead of requiring immediate provisioning.

To implement time flexibility, depending on your workload requirements, use the following features that use DWS:

  * To queue your capacity requests until resources become available, use the [flex-start provisioning model](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms#limitations-for-machine-types).

  * To reserve future capacity for a specific planned date and time, use [future reservations in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).




## Evaluate and adopt flexible infrastructure

Before you configure location or machine type flexibility, you must verify that the location and the machine types that you choose are compatible with each other and with your workload requirements. To help you successfully design and implement your flexible infrastructure, the following sections provide key evaluation considerations and an incremental adoption strategy.

### Evaluation considerations

Some key considerations for evaluating a flexible infrastructure are as follows:

  * **Location flexibility:** distributing your workload across multiple zones might affect your network latency and increase cross-zone data transfer costs.

To learn more, see the following documents:

    * To view latency data for traffic across compute instances in zones, see [View Google Cloud latency dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-google-cloud-latency).
    * To calculate the data transfer costs associated with inter-zone traffic, review [VM-VM data transfer pricing within Google Cloud](https://cloud.google.com/vpc/pricing#egress-within-gcp)
  * **Machine type flexibility:** falling back to alternative machine types can introduce variations in application performance and costs. Machine type flexibility across generations often requires you to implement disk and CPU platform overrides. You must verify that the machine types that you want to use meet your application's technical prerequisites.

To learn more, see the following documents:

    * To compare specifications across machine series, see [Machine series comparison](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison).
    * To view pricing for compute instances, see [Virtual machines pricing](https://cloud.google.com/products/compute/pricing).



### Adoption strategy

Depending on whether you are designing a new deployment or migrating an existing one, choose the corresponding strategy as follows:

  * **For a new workload:** if you're designing a new deployment, then we recommend adopting flexibility in your infrastructure design. To identify the recommended flexibility dimensions for your workload type, follow the guidance in Workload suitability and recommendations. Then, choose the deployment type that best supports your workload. For more information about the deployment types and their flexibility setups, see Core flexibility features section.

  * **For an existing deployment:** if you want to migrate a deployment that uses a single zone or machine type to a flexible infrastructure, then we recommend adopting flexibility incrementally to minimize risk. You can use an incremental adoption strategy such as the following:

    1. **Add location flexibility.** Migrate zonal workloads to a regional MIG with the `BALANCED` or `ANY` distribution shape. If you use a regional MIG with the `EVEN` shape, then change it to `BALANCED`. This change is important for MIGs that are scaling out. A temporary capacity constraint in a zone won't block the scale-out operation. Alternatively, if you want to create standalone compute instances, then use the `regionInstances.bulkInsert` API.

    2. **Add alternative machine types that share the same architecture.** Attach an instance flexibility policy that specifies machine types that share the same CPU architecture and disk support—for example, `n2-standard-8` and `n2d-standard-8`.

    3. **Add alternative machine types from different generations and align CUDs.** Incorporate the latest machine generations, such as `n4-standard-8`, and use disk overrides as needed. Additionally, cover discounts for fallback usage with compute flexible CUDs.




To help ensure a safe and successful adoption for both new deployments and incremental migrations, we recommend the following rollout workflow:

  * **Validate and benchmark.** Test your application across all selected machine families, disk combinations, and zones in a non-production environment.

  * **Productionize and scale.** Progressively rollout your instance flexibility policies or regional MIG distribution shapes to a subset of your production fleet before scaling globally.

  * **Monitor and optimize.** Continuously monitor your fallback rates, performance metrics, and costs to refine your prioritized list of machine types. When using MIGs, to track real-time compute instance distribution across machine types and zones, use the MIG instance distribution monitoring dashboard. For instructions, see [Monitor instance distribution in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution).




## Best practices

To maximize the efficiency and resilience of your flexible infrastructure, use the best practices described in the following sections.

### Best practices for location flexibility

  * **Use capacity-aware regional placement.** Deploy workloads by using regional MIGs or regional bulk VM creation. Select the `BALANCED` or `ANY` distribution shape as these shapes let Compute Engine evaluate real-time capacity across all zones in the region to automatically place compute instances where resources are available.

  * **Choose regions that support the machine type in multiple zones:** Deploy workloads in regions where your selected machine types are supported across all zones. This approach ensures that location flexibility features have the maximum number of alternative zones to route requests during a temporary capacity limitation. For a list of regions and zones, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

  * **Check availability for Spot VM deployments.** If your deployment uses Spot VMs, then check the real-time availability and expected uptime of Spot VMs across multiple machine types and locations. Choose a region or zone with high available capacity and an uptime that fits your workload to reduce the risk of preemption. For more information, see [View the availability of Spot VMs (Preview)](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability).




### Best practices for machine type flexibility

  * **Diversify across machine families.** Avoid policies that vary only by CPU cores within a single family—for example, `n2-standard-4` and `n2-standard-8`. Localized capacity constraints can affect the entire machine family simultaneously. To improve availability, span multiple machine generations and architectures—for example, `n4-standard-8` and `n2-standard-8`.

  * **Adopt new machine types with older ones as fallbacks.** Incorporate the latest machine families into your instance flexibility policy alongside older families to maximize availability.

  * **Configure disk and CPU platform overrides.** Mixing machine types from different generations can involve differences in disks and CPU platforms. Define disk and CPU platform overrides in your flexibility policy to help ensure that your infrastructure scales across machine generations seamlessly. For example, configure Hyperdisk Balanced for N4 instances and Persistent Disk for N2 fallbacks.

  * **Prioritize smaller machine types.** Depending on your workload suitability, use machine types with lower vCPUs and memory. For example, rather than relying on a single machine type like `n2-standard-64`, evaluate whether your workload can scale across four compute instances that each use an `n2-standard-16` machine type. Smaller machine types generally have higher resource availability.

  * **Select machine types with similar performance.** Specify alternative machine types with similar sizes of vCPU and memory. For example, combine `n2d-standard-8`, `n4-standard-8`, and `n4a-standard-8` in your instance flexibility policy. This approach maintains consistent application performance while improving resource availability.

  * **Enable update on repair in MIGs.** By default, a MIG repairs a failed compute instance by using its original machine type, which can fail if that hardware is temporarily unavailable. Enable update on repair so repairs automatically fall back to available machine types in your flexibility policy. For details, see [Instance flexibility and VM repairs](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility#vm-repairs).

  * **Incorporate Spot VMs with fallbacks.** For fault-tolerant workloads, combine Spot VMs with location and machine type flexibility. If Compute Engine preempts a Spot VM, these flexibility features let your deployment automatically search for alternative machine types or zones. This strategy helps maintain resource availability for your workload at a lower cost than standard provisioning.




### Best practices for time flexibility

  * **Target the right workloads.** Implement time flexibility for workloads that have flexible start times but require high-demand resources like accelerators. This requirement includes small model pre-training, model fine-tuning, high performance computing (HPC) simulations, and batch inference.

  * **Select the appropriate feature for your timeline.** Use the [flex-start provisioning model](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms) to queue requests for defined-duration jobs running up to seven days. To obtain high-demand resources for up to 90 days or longer, use the [reservation-bound provisioning model](https://docs.cloud.google.com/compute/docs/instances/about-reservation-bound-instances).

  * **Optimize Flex-start VM wait times.** When you attempt to create Flex-start VMs, specify a longer wait time if your workload must run in a specific zone. Longer waits increase your chances that Compute Engine can provision your requested resources. If you want to create standalone Flex-start VMs and your workload can start in any zone within a region, then specify a wait time of zero seconds. If the creation request fails because resources are unavailable, then immediately attempt the creation request in a different zone.




## Align reservations and discounts with workload flexibility

To balance resource availability and costs, match your committed use discounts (CUDs) to the capacity strategy you chose for your workload:

  * **Steady usage across multiple machine types:** if your workload supports multiple machine types and has steady usage, then configure machine type flexibility and use compute flexible CUDs. Machine type flexibility improves provisioning success rates by using alternative hardware when your primary choice lacks capacity. Compute flexible CUDs are spend-based discounts that apply to your eligible compute spend, regardless of the specific machine series that Compute Engine provisions.

  * **Steady baseline with traffic peaks:** if your workload has a predictable baseline but can experience unpredictable spikes, then secure your predictable baseline with reservations and resource-based CUDs. To handle traffic spikes, configure machine type flexibility and use compute flexible CUDs to cover the alternative fallback machines. In your instance flexibility policy, assign the preferences as follows:

    * **Highest preference:** reserved machine types with resource-based CUDs

    * **Lower preferences:** alternative machine types and use compute flexible CUDs

Compute Engine uses your resource-based commitments first, and then uses your compute flexible commitments to cover the remaining eligible usage.

  * **Strictly fixed hardware workloads:** if your workload relies on a single machine type, then use reservations and resource-based CUDs. Reservations provide a high assurance of capacity for specific hardware and should be considered for business-critical workloads. Resource-based CUDs provide discounts for this steady-state, predictable usage.




For more information, see [Choose a reservation type](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type), and [Committed use discounts (CUDs) for Compute Engine](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview).

### Design considerations for reservations

If your strategy includes reservations, review the following design considerations:

  * **Prioritize reserved machine types.** If you use reservations with machine type flexibility, add your reserved machine types to the highest preference in the instance flexibility policy. This configuration helps Compute Engine prioritize your reservations over on-demand capacity.

  * **Evaluate the scope of your reservations.** Avoid creating reservations in response to temporary capacity constraints. If your workload uses location flexibility, such as regional MIGs, then Compute Engine might distribute instances to other zones in the region. A strict zonal reservation in this scenario can result in unused, idle resources.




## Limitations

When you design flexible infrastructure, the following general limitations apply. For more detailed limitations, see the Limitations sections on the respective feature pages.

  * **Feature incompatibility** : you can't combine machine type flexibility and time flexibility in a single deployment. Features that enable time flexibility support only a single machine type configuration per request.

  * **Flexibility during initial creation** : for compute instances created in bulk, capacity evaluation and instance flexibility policy apply only during the initial compute instance creation request. Compute instances created in bulk don't automatically redirect to alternative zones or machine types during repairs or when you scale your infrastructure.

  * **Deploying to a single zone** : zonal MIGs don't support flexibility features and aren't recommended. To adopt machine type flexibility for a single-zone design, create a regional MIG and explicitly select only one zone.




## What's next

  * Learn how to [use a MIG to spread VMs across multiple zones in a region](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs).
  * Learn how to [configure instance flexibility in Managed Instance Groups](https://docs.cloud.google.com/compute/docs/instance-groups/configure-instance-flexibility).
  * Learn how to [create VMs in bulk with instance flexibility](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk-with-instance-flexibility).
  * Learn more about [CUDs in Compute Engine](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
