---
url: https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts/
title: Resource-based committed use discounts \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:12:55.397553+00:00
---

# Resource-based committed use discounts  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Resource-based committed use discounts Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine provides resource-based committed use discounts (CUDs) for your predictable workloads to help you cut costs on resources that you need. You can purchase resource-based committed use contracts, or _commitments_ , in return for heavily discounted prices for VM usage. 

This document provides an overview of resource-based commitments, including how they work, their properties, and how the resulting CUDs apply to your usage.

To learn about spend-based CUDs for Compute Engine, see [Compute flexible CUDs](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based).

Resource-based commitments are ideal for predictable and steady state usage. Depending on the resource type, Compute Engine offers the following categories of resource-based commitments:

  * **Hardware commitments** : You can purchase hardware commitments for a specific [machine configuration](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology). These commitments cover physical compute infrastructure resources, such as vCPUs, system memory, GPUs, and Local SSD disks. These resources are directly attached to or compose the Compute Engine instance itself.
  * **Software license commitments** : You can purchase license commitments for applicable premium operating system (OS) licenses. These commitments cover OS licenses that run on top of your compute instances.
  * **Block storage commitments** : You can purchase commitments only for [Hyperdisk Exapools](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-exapools) configurations. These commitments cover durable, network-attached block storage capacity in Hyperdisk pools, excluding Local SSD disks. These resources are independent of the compute instances themselves.



Commitments for hardware resources, commitments for OS licenses, and commitments for block storage are distinct from one another. Each category represents a fundamentally different resource type. Each category also has a distinct resource enforcement mechanism. You can purchase commitments from all three categories and use them to cover the usage of compute instances. However, you can't purchase a single commitment that covers resources from multiple categories. You must purchase and manage commitments for each category separately.

For example, suppose you purchase a 1-year commitment for 100 C4D vCPUs (hardware commitment) and a 1-year commitment for 100,000 GiB of Hyperdisk Throughput Exapools capacity (block storage commitment). Your block storage commitment can't be used to offset vCPU charges and your hardware commitment can't be used to offset block storage charges. Each commitment applies exclusively to eligible usage within its own category.

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## About resource-based commitments

When you purchase a resource-based commitment, you commit to purchasing a minimum amount of specific Compute Engine resources—such as vCPUs, memory, GPUs, Local SSD disks, and sole-tenant nodes—for a minimum of one or three years. In return for your commitment to pay for these resources, you receive these resources at discounted prices for the duration of your commitment's term. The percentage of discount that you receive off on-demand prices is also referred to as the committed use discount rate, or CUD rate. These discounts are as follows:

  * **vCPUs and memory** : You can receive up to 55% discount off on-demand prices for most machine types. For some machine types, you can receive up to 70% discount off on-demand prices.

  * **GPUs** : You can receive up to 55% discount off on-demand prices for most GPU types. For some GPU types, you can receive up to 65% discount off on-demand prices.

  * **Local SSD disks** : You can receive up to 55% discount off on-demand prices.

  * **OS licenses** : You can receive up to 79% discount off on-demand prices.




The exact discount rates and the duration for which you receive those discounts depend on the following properties that you specify when you purchase your commitment:

  * Commitment plan
  * Commitment term
  * The resource type, which is determined as follows: 
    * For hardware resources, the commitment type.
    * For software resources, the OS license type.



To compare on-demand and discounted rates of hardware resources, see [VM instances pricing](https://docs.cloud.google.com/compute/vm-instance-pricing). To compare on-demand and discounted rates of software OS licenses, see [Disk and image pricing](https://docs.cloud.google.com/compute/disks-image-pricing).

### Commitment lifecycle

You purchase a commitment by specifying the following properties, at a minimum:

  * Types and numbers of resources that you agree to pay for
  * Region where you agree to use the committed resources
  * The minimum time period for which you agree to pay for the resources



After you complete the purchase, you must wait until your commitment becomes active before you can start receiving CUDs. Your commitment becomes active at 12:00 AM US and Canadian Pacific Time the day after the purchase. Depending on daylight saving time, this time is equivalent to UTC-8 (Pacific Standard Time), or UTC-7 (Pacific Daylight Time). For example, suppose that you purchase your commitment at 3:45 PM US and Canadian Pacific Time (UTC-8) on December 1, 2024. In this scenario, your commitment becomes active at 12:00 AM US and Canadian Pacific Time (UTC-8) on December 2, 2024.

**Important:** Resource-based commitments are subject to Google Cloud [commitment-based pricing and billing](https://cloud.google.com/terms/service-terms#20-cloud-platform-commitment-based-pricing-and-billing). By purchasing a commitment, you agree to these terms. After you purchase a commitment, you can't cancel or delete it. The commitment remains active until its specified end date. For more information, see [Cancel a commitment](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#cancel-a-commitment).

Compute Engine [ maintains a lien on your project](https://docs.cloud.google.com/resource-manager/docs/project-liens) for each region in your project where you purchase a commitment. When you purchase a new commitment for any region in your project, Compute Engine associates the lien for that region with the newly created commitment. 

After your commitment becomes active, you start paying the discounted prices of your committed resources. You continue to pay these prices on an hourly basis until your commitment's end date, regardless of whether or not you use those resources. As you use Compute Engine resources, Google Cloud utilizes your commitment on an hourly basis to cover the costs of any eligible resource usage. Google Cloud continues to use your commitment either until the commitment expires or gets fully utilized.

### Commitment plan

When you purchase a commitment, you choose between a **1-year** or **3-year** plan. The plan functions as the commitment tier; it determines both the minimum period for which you must commit to paying for resources, and the CUD rate that you receive. A 3-year plan typically offers a higher CUD rate than a 1-year plan. Commitments are often referred to by their plan—for example, as _1-year commitments_ or _3-year commitments_.

### Commitment term

A commitment's term is the specific period during which the commitment is active. The duration of this term must be at least as long as the period defined by the commitment's plan (1 or 3 years), but can be longer. This duration represents the time for which you agree to pay for the committed resources.

By default, your commitment expires at the end of its term. However, you can automatically renew your commitment for additional terms by enabling [auto-renewal](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically). After you enable auto-renewal, at the end of each term, Compute Engine automatically renews the commitment for a new term. Your commitment continues to renew for new terms until you manually disable auto-renewal. By default, the duration of each renewed term matches the minimum duration required by the commitment's plan, either 1 or 3 years.

### Difference between term and plan

A commitment's _plan_ (1 year or 3 years) determines the preset time duration and the CUD rate, whereas its _term_ determines how long the commitment actually remains active. By default, a commitment's plan and term are identical. However, you can [extend the term](https://docs.cloud.google.com/compute/docs/committed-use-discounts/extend-commitment-term) beyond the preset duration specified by the plan. If you extend the term, then your commitment remains active for a custom duration, but retains the CUD rate associated with its plan. You can extend commitment terms as follows:

  * Commitments with a 1-year plan can have term durations starting from 1 year and less than 3 years.
  * Commitments with a 3-year plan can have term durations starting from 3 years and less than 6 years.



To summarize, your commitment's term and plan function as follows:

  * You get to use the committed resources _at discounted prices that are determined by your plan_.
  * You must pay these discounted prices _for the entire duration of your commitment's term_ , regardless of whether or not you use those resources.



### Start and end times of a commitment

A commitment's term represents the active lifecycle of a commitment and each term has a start time and an end time. Terms always start and end at 12:00 AM US and Canadian Pacific Time on their respective start and end dates. Depending on daylight saving time, this time is equivalent to UTC-8 (Pacific Standard Time), or UTC-7 (Pacific Daylight Time). The start time of a commitment's term can be one of the following, depending on whether it is a new or an existing commitment:

  * For **new commitments** , the start time is the same as the activation time, which is 12:00 AM US and Canadian Pacific Time on the day following your purchase.

For example, suppose that you purchase your commitment at 3:45 PM US and Canadian Pacific Time on January 1, 2025. In this scenario, your commitment starts at 12:00 AM US and Canadian Pacific Time on January 2, 2025.

  * For **an existing commitment that has auto-renewal enabled** , the start time of the new term is the same as the end time of the previous term: 12:00 AM US and Canadian Pacific Time.

For example, suppose that the end time of your commitment's ongoing term is 12:00 AM US and Canadian Pacific Time on January 1, 2026. If auto-renewal is enabled, then a new term automatically begins at 12:00 AM US and Canadian Pacific Time on January 1, 2026.




The end time of a commitment's term can be one of the following, depending on your commitment's configuration:

  * **Default:** When you don't extend a commitment's term or enable auto-renewal, the default end time for that term is at 12:00 AM US and Canadian Pacific Time, exactly one or three years after the start time, depending on whether you chose a 1-year or 3-year commitment plan.

For example, suppose that your commitment starts at 12:00 AM US and Canadian Pacific Time on January 1, 2025.

    * With a 1-year plan, the default end time is 12:00 AM US and Canadian Pacific Time on January 1, 2026.
    * With a 3-year plan, the default end time is 12:00 AM US and Canadian Pacific Time on January 1, 2028.
  * **Auto-renewal:** If you enable auto-renewal, then the commitment automatically renews for additional terms. Each renewed term has a duration equal to the commitment's plan (1 or 3 years), and the end time of each subsequent term is at 12:00 AM US and Canadian Pacific Time, one or three years after the start time of that renewed term.

For example, suppose that your 1-year commitment starts at 12:00 AM US and Canadian Pacific Time on January 1, 2025. With auto-renewal enabled, the commitment has its subsequent term ending at 12:00 AM US and Canadian Pacific Time on January 1 of each subsequent year.

  * **Extended term:** If you [extend the term](https://docs.cloud.google.com/compute/docs/committed-use-discounts/extend-commitment-term), then the end time is at 12:00 AM US and Canadian Pacific Time on the custom end date that you specify. This custom end date must be within the allowed range for your commitment's plan (for example, less than 3 years for a 1-year plan, or less than 6 years for a 3-year plan).

For example, you could extend a commitment with a 1-year plan to end 2 years after its start date, at 12:00 AM US and Canadian Pacific Time on that date.




### Commitment status

Depending on the stage of the commitment's lifecycle, your commitment can have one of the following statuses:

  * `CREATING`: The commitment is being created.
  * `NOT_YET_ACTIVE` or `PENDING`: The commitment has been created, but isn't yet active. Compute Engine creates your commitments with this status.

    * If you're using the gcloud CLI or REST to purchase your commitment, then this status value shows as `NOT_YET_ACTIVE`.
    * If you're using the Google Cloud console to purchase your commitment, then this status value shows as `PENDING`.
  * `ACTIVE`: The commitment is active.

  * `EXPIRED`: The commitment has expired. Compute Engine reserves the right to remove expired commitments that are older than 210 days from the expiration date.

  * `CANCELED`: Compute Engine canceled the commitment. Compute Engine changes the status of your commitments to `CANCELED` when you combine them to create a new [merged commitment](https://docs.cloud.google.com/compute/docs/instances/merge-and-split-commitments).




Between the time of your commitment purchase and its activation time, the status of your commitment remains as `NOT_YET_ACTIVE` (or as `PENDING` on the Google Cloud console). After activation, the status of your commitment changes to `ACTIVE`. For example, suppose that you purchase your commitment on January 20, 2024, at 10:00 PM US and Canadian Pacific Time (UTC-8 or UTC-7). Compute Engine creates your commitment immediately with its status as `NOT_YET_ACTIVE`. Your commitment becomes `ACTIVE` on January 21, 2024, at 12:00 AM US and Canadian Pacific Time (UTC-8 or UTC-7). 

When the commitment reaches its end date and expires, the status changes from `ACTIVE` to `EXPIRED`. Suppose that the commitment from the preceding example, which becomes active on January 21, 2024, has a 1-year term and you don't enable auto-renewal. Then, on January 21, 2025, at 12:00 AM US and Canadian Pacific Time (UTC-8 or UTC-7), the commitment expires and its status changes to `EXPIRED`.

## Pricing

You're billed monthly for your commitment and must pay your monthly commitment fee even if you don't use all of your committed resources. Your commitment fee is the sum of the discounted prices of all your committed resources. Compute Engine calculates the discounted price of each resource by using its prevailing on-demand price on the day that your commitment becomes active. Your monthly commitment fee and the discounted prices for your resources stay the same until the end of your commitment term, even if the on-demand prices change.

By default, Google Cloud enables CUD sharing for most Cloud Billing accounts. For more information, see [CUD scope and default configuration](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#cud-scope-configuration). When CUD sharing is enabled, your resource-based CUDs are pooled at the Cloud Billing account level. As a result, a single commitment can cover eligible resource usage in any project that is linked to the same Cloud Billing account. This distributed application of your CUDs helps you maximize commitment utilization across your organization.

If you use your commitments to run custom machine types, then Compute Engine charges a 5% premium over the commitment prices. Compute Engine charges this premium for the portion and duration of your commitment that you run these custom machine type VMs. When CUD sharing is enabled, Compute Engine credits CUDs to custom machine types across the Cloud Billing account before predefined machine types.

**Note:** If you merge or split your commitments, then the discounted prices for your committed resources might change on the day that your merged or split commitments become active.

The discounted pricing (also referred to as CUD pricing) for VM instances, with or without GPUs and Local SSD disks, differs depending on the region. For 1-year and 3-year commitment prices of various resources, see [the Compute Engine pricing page](https://cloud.google.com/products/compute/pricing).

If you move the project for which you purchased commitments to a different Cloud Billing account, then you continue to receive CUDs under the destination Cloud Billing account for the commitments associated with that project. For more information about how moving a project affects CUD sharing and attribution settings, see [Impact of changing a project's Cloud Billing account](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#moving-project-billing-account).

## Limitations

The following restrictions apply to resource-based CUDs.

### General limitations

  * Projects that are in the free tier period with free tier credit and projects that don't have any payment history don't qualify for committed use discounts.
  * You can purchase commitments only on a per-region basis.
  * Resource-based CUDs don't apply to [preemptible VM instances](https://docs.cloud.google.com/compute/docs/instances/create-use-preemptible), [N1 shared-core machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machine_types), or [extended memory](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#extendedmemory).
  * If you use your Compute Engine [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) with Managed Service for Apache Spark, then those reserved resources aren't eligible for resource-based CUDs.
  * If you use your reservations with Dataflow, then you can receive resource-based CUDs only for usage from [specifically targeted reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type) that specify accelerators (GPUs or TPUs).
  * Resource-based commitments for Cloud TPUs are available for purchase only through [future reservations for capacity blocks](https://docs.cloud.google.com/tpu/docs/long-term-reservation).
  * For commitments that you purchased through [future reservations for capacity blocks](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type#reserve-capacity-aihc), you can't perform the following operations: 
    * Enable auto-renewal on the commitment.
    * Extend the commitment's term.
    * Merge the commitments.
    * Split the commitment.
    * Upgrade the commitment.
  * Commitments for RHEL for SAP are unavailable for purchase as Google transitions into the [new RHEL pricing model](https://www.redhat.com/en/blog/red-hat-enterprise-linux-scalable-pricing-cloud-partners-announcement).
  * For machine types that support [per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration), the higher bandwidth SKUs are excluded from CUDs.
  * `f1-micro` and `g1-small` shared-core machines aren't eligible for CUDs.
  * You can't change the project for which you purchase a commitment. However, when CUD sharing is enabled, CUDs from a commitment are shared across other projects in the same Cloud Billing account. For more information, see [Share resource-based CUDs across projects](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects).



### Limitations specific to sharing resource-based CUDs

  * If you have a shared reservation in a project where [ CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects) is enabled, and you want usage from the shared projects to be eligible for the shared CUDs, then you must ensure that you share your reservation only with projects that are linked to the same Cloud Billing account. Otherwise, usage from the shared projects won't be eligible for the shared CUDs and you might be charged the on-demand rates.
  * When CUD sharing is enabled for a Cloud Billing account, if any portion of a commitment is unutilized, then the remaining commitment charge remains in the project where you purchased that commitment.
  * If you move the project for which you purchased commitments to a different Cloud Billing account, then you continue to receive CUDs under the destination Cloud Billing account for the commitments associated with that project. To learn more about how moving a project affects CUD sharing and attribution settings, see [Impact of changing a project's Cloud Billing account](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#moving-project-billing-account).



### Limitations specific to attached reservations

  * If the commitment specifies any GPUs, Local SSD disks, or both, then the attached reservation (or combination of attached reservations) must specify exactly the same numbers and types of those resources as the commitment. For more information, see [Attach reservations to resource-based commitments](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments#attach-reservations-to-resource-cuds).

**Note:** This restriction doesn't apply to local Titanium SSD disks that you specify for use with C4, C4A, C4D, C4N, G4, H4D, Z4D, Z4M, or Z3 instances. Because reservations are optional for these disks, you can purchase a commitment for the disks without attaching any reservations.
  * If your attached reservation is for a [resource type that requires attached reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments#committed_resources_that_require_attached_reservations), then you can't do the following:

    * Delete, resize, or modify the attached reservations throughout the commitment's lifecycle. However, you can [replace existing attached reservations with new ones](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments#modifying_reservations_that_are_attached_to_commitments).
    * Enable the auto-delete setting on those attached reservations. When commitments that specify these resource types expire, any attached reservations are automatically deleted.
  * You can't attach the same reservation to more than one commitment.




### Limitations specific to CUD recommendations

  * CUD recommendations aren't available for the A3 Ultra, A4, A4X, and A4X Max machine series.
  * CUD recommendations aren't available for Cloud TPUs.



### Limitations specific to software license commitments

  * You can't merge software license commitments.
  * You can't split software license commitments.
  * You can't upgrade software license commitments from a 1-year plan to a 3-year plan.
  * You can't extend the term of software license commitments.
  * You can't enable the auto-renewal setting for software license commitments. If you want a commitment for these resources for longer periods, then purchase a new commitment.
  * Attached reservations are not supported for software license commitments.



### Limitations specific to block storage commitments

  * You must contact your account team to purchase block storage commitments. Compute Engine doesn't support self-service purchase of these commitments through the Google Cloud console, the gcloud CLI, or REST.
  * Block storage commitments are available only for purchasing Exapool capacity. You can't purchase commitments for Persistent Disk, Hyperdisk, or Hyperdisk Storage Pools.
  * You can't merge block storage commitments.
  * You can't split block storage commitments.
  * You can't upgrade block storage commitments from a 1-year to a 3-year plan.
  * You can't extend the term of block storage commitments.
  * Attached reservations are not supported for block storage commitments.
  * CUD recommendations and [CUD analysis reports](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds) are not supported for block storage commitments.



## Hardware commitments

Hardware commitments apply only to the specific region and machine family series for which you purchase. In return, you receive discounts on the aggregate prices of all the eligible hardware resources for that machine series within that region. These hardware resources include vCPUs, memory, GPUs, and Local SSD disks.

The commitment that you purchase doesn't affect your VM configurations. Your CUDs apply to the aggregate number of vCPUs, memory, GPUs, and Local SSD disks of a specific machine series within a region. Consequently, the CUDs that you receive for a commitment aren't affected by changes to your VM's machine setup, as long as the resources are covered by that commitment.

When you purchase a commitment for a specific machine series, you are eligible for CUDs on all VM machine types regardless of the VM size or tenancy model, including all predefined and custom machine types and sole-tenant nodes. For more information about the eligible resource types for each machine series, see [Hardware commitment types](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#commitment-types-for-hardware-commitments).

### Efficient usage of your commitments

Purchase commitments only for the specific resources that you plan to use. After you purchase a commitment, you're billed for that commitment on a monthly basis, even if you don't use the commitment. For example, if you purchase a 3-year commitment for eight vCPUs, then you're charged the 3-year CUD rates for those vCPUs on a monthly basis. You are charged for usage for the entire month even if you use those vCPUs only for a part of the month.

It is to your advantage to purchase commitments only in increments that you know you will use. For example, suppose that you purchased a commitment for eight vCPUs and keep receiving CUDs for using eight vCPUs every month. Suppose that you then anticipate starting to use 24 vCPUs per month. In this scenario, the additional 16 vCPUs aren't covered by your existing commitment and are billed at on-demand rates. If you plan to use the 16 additional vCPUs per month on a recurring basis, then you benefit from purchasing an additional commitment for 16 vCPUs.

Commitments can't be stacked for burst scenarios. For example, if you purchase a commitment for 10 vCPUs, but run 20 vCPUs for only the first half of the month, then your commitment still covers only 10 vCPUs at any given time.

Because a month has roughly 730 hours, you might incorrectly assume that your burst usage is fully covered based on the following calculation:

  * **Commitment** : 10 vCPUs * 730 hours = covers 7,300 vCPU-hours of commitment.
  * **Usage** : 20 vCPUs * 365 hours (half the month) = 7,300 vCPU-hours of usage.
  * **Misconception** : 7,300 vCPU-hours of commitment = 7,300 vCPU-hours of usage, leading to the incorrect assumption that the commitment covers the entire usage perfectly.



In reality, commitments apply on a continuous second-by-second basis rather than as a monthly aggregate pool of hours. For this scenario, your billing breaks down as follows:

  * **First half of the month (365 hours)** : Your commitment covers 10 vCPUs and provides CUDs for 3,650 vCPU-hours of usage. The remaining 10 vCPUs exceed your commitment and are billed at standard on-demand rates, which is equivalent to 3,650 vCPU-hours of on-demand charges.
  * **Second half of the month (365 hours)** : Because you run 0 vCPUs, your commitment for 10 vCPUs goes unused throughout this period. As a result, 3,650 vCPU-hours of commitment are wasted.



### Usage overage

Any hourly resource usage that isn't covered by your commitments is charged at on-demand rates and might be eligible for applicable [sustained use discounts (SUDs)](https://docs.cloud.google.com/compute/docs/sustained-use-discounts). For example, consider a commitment for 2 vCPUs and 8 GB memory that belong to the N2 machine series. Suppose that you use this commitment to purchase and run an `n2-standard-2` (2 vCPUs and 8 GB memory) VM for a portion of the month and then run an `n2-standard-8` (8 vCPUs and 32 GB memory) VM for the remainder of the same month. In this scenario, Compute Engine combines the usage across both VMs and automatically applies the applicable SUDs to any resource usage that isn't covered by your commitment.

### Combine reservations with commitments

A commitment provides a 1- or 3-year discounted price agreement, but it doesn't reserve capacity in a specific zone. A reservation makes sure that capacity is held in a specific zone even if the reserved VMs aren't running. To get zonal resources at discounted prices and also make sure that capacity is reserved for them, you must both purchase commitments and create reservations for those zonal resources.

You can also attach reservations to your resource-based commitments at the time that you purchase your commitment. By attaching reservations to your commitments, you link the two entities together. This linkage helps you better identify and track which committed resources also have capacity reserved.

Attaching a reservation to your commitment is mandatory for some resource types and optional for others:

  * **vCPUs and memory** : Attaching reservations is optional. You can purchase commitments for vCPUs and memory without attaching any reservations.
  * **GPUs** : Attaching reservations is mandatory for resource-based commitments. When you purchase resource-based commitments for GPUs, you must reserve those GPUs and attach those reservations to your commitment. To receive CUDs for G2 and G4 GPUs without reservations, purchase [compute flexible commitments](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) instead.
  * **Local SSD disks** : Attaching reservations is mandatory for most machine series. However, if you specify local Titanium SSD disks in your commitment for use with C4, C4A, C4D, C4N, G4, H4D, Z4D, Z4M, or Z3 instances, then you don't need to reserve those disks.



For more information about attaching reservations to your commitments, see [Combine reservations with committed use discounts](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments).

### Commitment types for hardware commitments

When you purchase a commitment, you must choose the _commitment type_ that applies to your intended resource usage. The commitment type of the commitment determines the machine series—or in some cases, a specific collection of machine types—that is covered by your commitment. When you use instances belonging to these machine series or machine types, Google Cloud covers the eligible portions of that usage through your commitment. Most machine series use one specific commitment type for all machine types in that series. The following machine series are exceptions; they don't have a single commitment type for the entire series:

  * **Accelerator-optimized A3** : This machine series has multiple commitment types:

    * A3 Edge and A3 High machine type resources are covered by a single commitment type.
    * A3 Mega machine type resources are covered by a separate commitment type.
    * A3 Ultra machine type resources are covered by a separate commitment type.

**Note:** To purchase commitments for A3 Ultra machine types, you must use the _future reservations for capacity blocks_ consumption option. For more information, see [Reserve capacity through your account team](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity) in the AI Hypercomputer documentation.
  * **Memory-optimized M1 and memory-optimized M2** : These machine series have a single, combined commitment type that covers all M1 and M2 machine types.

  * **Memory-optimized M4** : This machine series has two commitment types:

    * One commitment type specifically covers M4 machine types that come with 6 TB of memory.
    * All other M4 machine types are covered by a separate commitment type.
  * **Memory-optimized M4N** : This machine series has two commitment types:

    * One commitment type specifically covers the M4N machine type that comes with 6 TB of memory.
    * All other M4N machine types are covered by a separate commitment type.
  * **Memory-optimized X4** : This machine series has a different commitment type for each machine type:

    * The X4 machine type with 6 TB of memory (`x4-480-6t-metal`)
    * The X4 machine type with 8 TB of memory (`x4-480-8t-metal`)
    * The X4 machine type with 12 TB of memory (`x4-960-12t-metal`)
    * The X4 machine type with 16 TB of memory (`x4-960-16t-metal`)
    * The X4 machine type with 24 TB of memory (`x4-1440-24t-metal`)
    * The X4 machine type with 32 TB of memory (`x4-1920-32t-metal`)



The specific value for each commitment type varies depending on whether you use the gcloud CLI, REST, or the Google Cloud console to purchase a commitment. For the exact values to use when purchasing, see the relevant instructions in the [Purchase resource-based commitments without attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments) or [Purchase resource-based commitments with attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments-with-reservations) sections.

**Caution** : For C3 and C3D commitment types, the machine family that is specified by the commitment type changes depending on the interface: 

  * In the gcloud CLI and REST, the commitment type values use _Compute-optimized_ as the machine family, even though C3 and C3D are part of the general-purpose machine family.
  * In the Google Cloud console, the commitment type values use the correct machine series: _General-Purpose_.

Make sure to select the correct commitment type value that corresponds to the interface that you're using. 

The following table lists all the machine series for which you can purchase resource-based commitments, along with their corresponding commitment types. For each commitment type, the table also lists the eligible machine types and resource types that are eligible for CUDs. For every listed machine type, the applicability includes sole-tenant node types, if sole-tenancy is supported by the machine series.

Commitment type | Eligible resources | Applicable machine types  
---|---|---  
General-purpose E2 | 

  * vCPUs
  * Memory

| All E2 machine types  
General-purpose N2 | 

  * vCPUs
  * Memory
  * Local SSD disks

| All N2 machine types  
General-purpose N2D | 

  * vCPUs
  * Memory
  * Local SSD disks

| All N2D machine types  
General-purpose N4 | 

  * vCPUs
  * Memory

| All N4 machine types  
General-purpose N4D | 

  * vCPUs
  * Memory

| All N4D machine types  
General-purpose N4A | 

  * vCPUs
  * Memory

| All N4A machine types  
General-purpose C3 | 

  * vCPUs
  * Memory
  * Local SSD disks

| All C3 machine types  
General-purpose C3D | 

  * vCPUs
  * Memory
  * Local SSD disks

| All C3D machine types  
General-purpose C4 | 

  * vCPUs
  * Memory

| All C4 machine types  
General-purpose C4A | 

  * vCPUs
  * Memory
  * Local Titanium SSD disks

| All C4A machine types  
General-purpose C4D | 

  * vCPUs
  * Memory
  * Local Titanium SSD disks

| All C4D machine types  
Network-optimized C4N | 

  * vCPUs
  * Memory
  * Local Titanium SSD disks

| All C4N machine types  
General-purpose Tau T2D | 

  * vCPUs
  * Memory

| Standard Tau T2D machine types  
General-purpose N1 | 

  * vCPUs
  * Memory
  * GPUs
  * Local SSD disks

| 

  * All N1 machine types, excluding shared-core.
  * GPUs: 
    * NVIDIA T4. NVIDIA T4 is approaching end of support, review the [NVIDIA T4 end of support documentation](https://docs.cloud.google.com/compute/docs/eol/t4-eos).
    * NVIDIA V100
    * NVIDIA P4. NVIDIA P4 is approaching end of support, review the [NVIDIA P4 end of support documentation](https://docs.cloud.google.com/compute/docs/eol/p4-eos).

  
Storage-optimized Z4D | 

  * vCPUs
  * Memory
  * Local Titanium SSD disks

| All Z4D machine types  
Storage-optimized Z4M | 

  * vCPUs
  * Memory
  * Local Titanium SSD disks

| All Z4M machine types  
Storage-optimized Z3 | 

  * vCPUs
  * Memory
  * Local Titanium SSD disks

| All Z3 machine types  
Compute-optimized H4D | 

  * vCPUs
  * Memory
  * Local Titanium SSD disks

| 

  * All H4D machine types
  * All H4D sole-tenant node types

  
Compute-optimized H3 | 

  * vCPUs
  * Memory

| All H3 machine types  
Compute-optimized C2 | 

  * vCPUs
  * Memory
  * Local SSD disks

| 

  * All C2 machine types
  * All C2 sole-tenant node types

  
Compute-optimized C2D | 

  * vCPUs
  * Memory
  * Local SSD disks

| All C2D machine types  
Memory-optimized M1/M2 | 

  * vCPUs
  * Memory
  * Local SSD disks

| 

  * All M1 and M2 machine types
  * Doesn't apply to Memory Optimized Upgrade Premium SKUs

  
Memory-optimized M3 | 

  * vCPUs
  * Memory
  * Local SSD disks

| All M3 machine types  
Memory-optimized M4 6TB | 

  * vCPUs
  * Memory

| `m4-ultramem-224` (the M4 machine type with 6 TB of memory)  
Memory-optimized M4 | 

  * vCPUs
  * Memory

| All other M4 machine types  
Memory-optimized M4N 6TB | 

  * vCPUs
  * Memory

| `m4n-ultramem-224` (the M4N machine type with 6 TB of memory)  
Memory-optimized M4N | 

  * vCPUs
  * Memory

| All other M4N machine types  
Memory-optimized X4 6TB | 

  * vCPUs
  * Memory

| X4 machine type with 6 TB of memory  
Memory-optimized X4 8TB | 

  * vCPUs
  * Memory

| X4 machine type with 8 TB of memory  
Memory-optimized X4 12TB | 

  * vCPUs
  * Memory

| X4 machine type with 12 TB of memory  
Memory-optimized X4 16TB | 

  * vCPUs
  * Memory

| X4 machine type with 16 TB of memory  
Memory-optimized X4 24TB | 

  * vCPUs
  * Memory

| X4 machine type with 24 TB of memory  
Memory-optimized X4 32TB | 

  * vCPUs
  * Memory

| X4 machine type with 32 TB of memory  
Accelerator-optimized A2 | 

  * vCPUs
  * Memory
  * GPUs
  * Local SSD disks

| 

  * All A2 machine types
  * GPUs: NVIDIA A100

  
Accelerator-optimized A3 | 

  * vCPUs
  * Memory
  * GPUs
  * Local SSD disks

| 

  * A3 Edge and High machine types
  * GPUs: NVIDIA H100

  
Accelerator-optimized A3 Mega | 

  * vCPUs
  * Memory
  * GPUs
  * Local SSD disks

| 

  * A3 Mega machine types
  * GPUs: NVIDIA H100

  
Accelerator-optimized A3 Ultra  
([Available only with AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity))  | 

  * vCPUs
  * Memory
  * GPUs
  * Local SSD disks

| 

  * A3 Ultra machine types
  * GPUs: NVIDIA H200

  
Accelerator-optimized A4  
([Available only with AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity))  | 

  * vCPUs
  * Memory
  * GPUs
  * Local SSD disks

| 

  * All A4 machine types
  * GPUs: NVIDIA B200

  
Accelerator-optimized A4X  
([Available only with AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity))  | 

  * vCPUs
  * Memory
  * GPUs
  * Local SSD disks

| 

  * All A4X machine types
  * GPUs: NVIDIA GB200

  
Accelerator-optimized A4X Max  
([Available only with AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity))  | 

  * vCPUs
  * Memory
  * GPUs
  * Local SSD disks

| 

  * `a4x-maxgpu-4g-metal`
  * GPUs: NVIDIA GB300

  
Graphics-optimized G2 | 

  * vCPUs
  * Memory
  * GPUs
  * Local SSD disks

| 

  * All G2 machine types
  * GPUs: NVIDIA L4

  
Graphics-optimized G4 | 

  * vCPUs
  * Memory
  * GPUs
  * Local Titanium SSD disks

| 

  * All G4 machine types
  * GPUs: NVIDIA RTX PRO 6000

  
  
You can't purchase commitments for `f1-micro`, or `g1-small` machine types or for the sole-tenant premium charge.

### Commitments for Compute Engine machine types

Google Cloud offers resource-based commitments for hardware resources of several Compute Engine machine family series. Purchase the appropriate commitment type for the machine types that you plan to use.

#### General-purpose machine types

CUDs for general-purpose machine types are applied to resources in the following order:

  1. Custom machine types (see supported [machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types))

  2. Sole-tenant nodes

  3. Predefined machine types




When you purchase commitments for general-purpose machine types, you pick which machine series the commitment applies to. For example, if you purchase general-purpose E2 commitments, then they apply to only E2 machine types. Similarly, if you purchase general-purpose N2, N2D, N4, N4D, N4A, C4, C4A, C4D, C3, C3D, Tau T2D, or N1 commitments, then the commitments never overlap.

For example, assume you have a region with the following mix:

  * 10 N2 custom machine type vCPUs
  * 30 GB of custom machine type memory
  * 2 `n2-standard-4` predefined machine types



You purchase N2 commitments for 15 vCPUs and 13.5 GB of memory for committed use. Compute Engine applies the CUDs first to the N2 custom machine types, and applies any remaining discounts to the N2 predefined machine types. In this case, Compute Engine charges all 10 vCPUs of the N2 custom machine types and 13.5 GB of custom machine type memory at committed use prices.

Finally, the remaining 5 vCPUs of committed use apply to 5 random vCPUs across the two `n2-standard-4` machine types. Any resource usage that isn't covered by your commitments might qualify for applicable SUDs.

Also, if you use your commitments to run custom machine types, then Compute Engine charges a 5% premium over the commitment prices. Compute Engine charges this premium for the portion and duration of your commitment that you run these custom machine type VMs.

Commitments are aggregated by machine series. If you are unsure of how many commitments to purchase, then you might want to purchase a smaller number of commitments, and then add more as you need them. For example, you can purchase multiple contracts for 10 vCPUs and zero memory, then purchase separate contracts for additional memory.

To purchase a commitment for general-purpose machine types, see [Purchase resource-based commitments without attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments) and [Purchase resource-based commitments with attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments-with-reservations).

#### Memory-optimized machine types

When you purchase commitments for memory-optimized machine series resources, you must use the correct commitment type that applies to your machine type. The following list outlines how the commitment types change depending on the machine type:

  * **M1 and M2 machine types** : A single, combined commitment type covers all [M1 machine types](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m1_machine_types) and [M2 machine types](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m2_machine_types).
  * **M3 machine types** : A single commitment type covers all [M3 machine types](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_machine_types).
  * **M4 machine types** : There are two commitment types for [M4 machine types](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4_machine_types): 
    * One for the M4 machine type that has 6 TB of memory
    * One for all other M4 machine types
  * **M4N machine types** : There are two commitment types for [M4N machine types](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4n_machine_types): 
    * One for the M4N machine type that has 6 TB of memory
    * One for all other M4N machine types
  * **X4 machine types** : For [X4 machine types](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x4_machine_types), there is a unique commitment type for each of the available memory options:

    * 6 TB of memory (`x4-480-6t-metal`)
    * 8 TB of memory (`x4-480-8t-metal`)
    * 12 TB of memory (`x4-960-12t-metal`)
    * 16 TB of memory (`x4-960-16t-metal`)
    * 24 TB of memory (`x4-1440-24t-metal`)
    * 32 TB of memory (`x4-1920-32t-metal`)



You must purchase the commitment type that matches the machine series and type of your instance.

The Memory Optimized Upgrade Premium Core and RAM SKUs, which are specific to M2 machine types, aren't eligible for CUDs. The prices for these SKUs are incorporated into the price rates that are documented on the [VM instance pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#memory-optimized) and in the [pricing calculator](https://cloud.google.com/products/calculator).

If you intend to use memory-optimized machine types, purchase memory-optimized commitments. To purchase a commitment for memory-optimized machine types, see [Purchase resource-based commitments without attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments).

#### Storage-optimized machine types

To purchase commitments for storage-optimized Z4D, Z4M, or Z3 machine types, see [Purchase resource-based commitments without attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments) and [Purchase resource-based commitments with attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments-with-reservations).

#### Compute-optimized machine types

To purchase commitments for compute-optimized machine types, see one of the following:

  * **For C2 and C2D machine types** : See [Purchase resource-based commitments without attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments).
  * **For H3 and H4D machine types** : See [Purchase resource-based commitments with attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments-with-reservations).



#### Network-optimized machine types

When you purchase commitments for network-optimized machine series resources, you must use the correct commitment type that applies to your machine type. The following list outlines how the commitment types change depending on the machine type:

  * **For C4N machine types** : A single commitment type covers all [C4N machine types](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_machine_types).
  * **For M4N machine types** : See M4N in [Memory-optimized machine types](https://docs.cloud.google.com/compute/docs/instances/:#memory-optimized-machine-types).



To purchase a commitment for network-optimized machine types, see [Purchase resource-based commitments without attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments) and [Purchase resource-based commitments with attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments-with-reservations).

#### Accelerator-optimized machine types

Accelerator-optimized VMs have a specific model and number of NVIDIA GPUs attached. When you purchase commitments for these machine types, you must also reserve your committed GPUs and attach those reservations to your commitments.

To purchase a commitment for these machine types, see the following:

  * **For A3 Mega, A3 High, A3 Edge, A2, G4, or G2 machine types** : See [Purchase resource-based commitments with attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments-with-reservations).
  * **For A4X Max, A4X, A4, or A3 Ultra machine types** : You must use the _future reservations for capacity blocks_ consumption option. For more information, see [Reserve capacity through your account team](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity) in the AI Hypercomputer documentation.



### Commitments for GPUs and Local SSD disk resources

When you purchase commitments for GPUs, you can only specify one GPU type for any given commitment. Consequently, that commitment covers usage only for the specified GPU type. If you want to receive CUDs for using multiple GPU types, then you must purchase separate commitments for each GPU type. For example, suppose that you use both NVIDIA A100 GPUs and NVIDIA V100 GPUs. If you only have a commitment for NVIDIA A100 GPUs, then that commitment can't cover your usage from NVIDIA V100 GPUs. To receive CUDs for both NVIDIA A100 GPU usage and NVIDIA V100 GPU usage, you must purchase separate commitments for each GPU type.

Also, to purchase resource-based commitments for GPUs and most Local SSD disks, you must reserve those resources and attach the reservations to your commitment. If you specify any local Titanium SSD disks in your commitment for use with C4, C4A, C4D, G4, H4D, Z4D, Z4M, or Z3 instances, then you don't need attached reservations for those disks. To learn more about resource-based commitments with attached reservations, see [Attach reservations to resource-based commitments](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments#attach-reservations-to-resource-cuds).

**Note:** This reservation requirement also doesn't apply for any GPU or Local SSD resources that are eligible for [compute flexible commitments](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based).

To learn how to purchase commitments for GPUs or Local SSD disks, see the following:

  * **For GPUs used with A4X Max, A4X, A4, or A3 Ultra machine types** : You must use the _future reservations for capacity blocks_ consumption option. For more information, see [Reserve capacity through your account team](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity) in the AI Hypercomputer documentation.

  * **For all other GPU types and Local SSD disks** : See [Purchase resource-based commitments with attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments-with-reservations).




To learn more about commitments with attached reservations, see [Attach reservations to resource-based commitments](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments#attach-reservations-to-resource-cuds).

## Software license commitments

Similar to hardware resource commitments, you can purchase these commitments for a plan of either one or three years. In return for your commitment to pay for these resources, you receive these resources at discounted prices for the duration of your commitment's term. The percentage of discount that you receive off on-demand prices is also referred to as the committed use discount rate, or CUD rate.

You can purchase commitments for your licenses if you run your workloads on VMs that use the following operating system (OS) images:

  * **SUSE Linux Enterprise Server (SLES) images**
  * **SLES for SAP images**
  * **Red Hat Enterprise Linux (RHEL) images**



The CUD rates that you receive for license commitments of each OS image depend on the number of vCPUs that your VM uses. The following table shows the CUD rates for each type of software license commitment:

SLES imagesSLES for SAP imagesRHEL images

Clear all

**License commitment type** | **Number of vCPUs** | **1-year CUD rate** | **3-year CUD rate**  
---|---|---|---  
**SLES images** | 1-2 | 77% | 79%  
**SLES images** | 3-4 | 54% | 59%  
**SLES images** | 5+ | 45% | 50%  
**SLES for SAP images** | 1-2 | 59% | 63%  
**SLES for SAP images** | 3-4 | 59% | 63%  
**SLES for SAP images** | 5+ | 59% | 63%  
**RHEL images** | 1-8 | 20% | Unavailable  
**RHEL images** | 9-127 | 20% | Unavailable  
**RHEL images** | 128+ | 20% | Unavailable  
  
When you purchase a license commitment, the licenses enter a pool for the specified project and region. The licenses aren't tied to specific VMs. When a VM starts, it consumes a license from the pool. When the VM stops, the license returns to the pool for other VMs to use. You receive the discount as long as a running VM consumes an available license from the pool.

For example, if you need to run 10 VMs in two regions (5 VMs in `us-central1` and 5 VMs in `us-west1`) and under the same project ID, then you must purchase 5 licenses in each region to cover those running VMs. For each commitment, your committed licenses can apply to any 5 concurrently running VMs at any time during the year in the respective region. You are billed monthly for the commitments regardless of your usage.

After you purchase a commitment, your commitment becomes active on the following day at 12 AM US and Canadian Pacific Time (UTC-8, or UTC-7 during daylight saving time). Compute Engine [ maintains a lien on your project](https://docs.cloud.google.com/resource-manager/docs/project-liens) for each region in your project where you purchase a commitment. When you purchase a new commitment for any region in your project, Compute Engine associates the lien for that region with the newly created commitment. 

Between the time of your commitment purchase and its activation time, the status of your commitment remains as `NOT_YET_ACTIVE` (or as `PENDING` on the Google Cloud console). After activation, the status of your commitment changes to `ACTIVE`. For example, suppose that you purchase your commitment on January 20, 2024, at 10:00 PM US and Canadian Pacific Time (UTC-8 or UTC-7). Compute Engine creates your commitment immediately with its status as `NOT_YET_ACTIVE`. Your commitment becomes `ACTIVE` on January 21, 2024, at 12:00 AM US and Canadian Pacific Time (UTC-8 or UTC-7). 

You can't cancel a license commitment after you purchase it. When your license commitments expire, your running VMs continue to run and you are charged for the licenses at on-demand image prices.

**Important:** Always verify that committed use discount contracts or commitments for your licenses are in the correct project ID and regions to avoid being double charged. You must purchase your license commitment in the same project and region as the machine using the license. For example, if you purchase your license commitment in Project A, but the running VMs that require the OS images are in Project B, then you are charged for the license commitment in Project A and the on-demand image price for the VMs running in Project B.

To purchase commitments for OS licenses, see [Purchase software commitments for OS licenses](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-license-commitments).

## Block storage commitments

Block storage commitments provide CUDs for block storage in [Hyperdisk Exapools](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-exapools). Exapools let you purchase storage and performance in 1 GiB increments called _[capacity units](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-exapools#how_capacity_units_work)_. You can consume the purchased capacity units by creating an Exapool or by modifying an existing Exapool to consume the purchased capacity units.

To receive block storage CUDs, you must first purchase a block storage commitment for a specific amount of Exapool capacity units (measured in GiB) for a 1-year or 3-year plan. After your commitment becomes active, Google Cloud applies CUDs to the prices of the matching capacity units in your Exapools. You pay these discounted prices for the entire duration of your commitment's term, regardless of whether or not you create an Exapool with those capacity units.

A block storage commitment covers only the capacity units in an Exapool and doesn't automatically create an Exapool for you. The commitment also doesn't apply to individual disks that aren't created in an Exapool. To use the resources covered by your commitment, create or modify an Exapool with matching capacity units, and then create disks in the Exapool as needed.

### How block storage commitments work

Block storage commitments apply to usage within the specific region for which you purchased the commitment. These commitments aren't tied to specific disks or specific Exapools. When you purchase a block storage commitment, Compute Engine aggregates your committed Exapool capacity units for the specified region. When you create or modify Exapools with capacity units that match the pool type and region specified by your commitment, Compute Engine counts the capacity units in those pools as eligible usage and automatically applies CUDs to their prices.

Compute Engine calculates eligible usage per microsecond and charges you discounted rates on an hourly basis. Compute Engine bills any capacity units in your Exapools that exceed your committed amount as overage usage at on-demand rates. Your commitment continues to cover eligible usage until the expiration date.

Depending on your [CUD sharing scope](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects), Compute Engine combines your committed Exapool capacity units from all commitments either at the project level or at the Cloud Billing account level. If you have CUD sharing enabled, then your commitments are pooled at the Cloud Billing account level and can cover eligible usage across all projects in that account. If you disable CUD sharing, then Compute Engine covers only the usage that comes from the commitment's project.

### Eligible Hyperdisk Exapool types

Each block storage commitment applies to a specific Exapool type and one or more Exapool capacity unit types. Compute Engine offers block storage commitments for the following Exapool types:

  * Hyperdisk Balanced Exapools
  * Hyperdisk Throughput Exapools



For details, see [Exapool types](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-exapools#exapool-types).

A single block storage commitment can apply to only one Exapool type. To receive CUDs for both Hyperdisk Balanced Exapools and Hyperdisk Throughput Exapools, you must purchase separate commitments for each pool type.

When you purchase a block storage commitment, you must also specify the Exapool [capacity unit types](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-exapools#how_capacity_units_work) that you want to commit to purchasing. These unit types are the same capacity unit types that you select when you provision an Exapool to match your workload's read and write requirements. Each unit provides 1 GiB of storage and a fixed amount of performance (IOPS and throughput) per GiB:

  * `CAPACITY_OPTIMIZED` (capacity-optimized units): provides a balanced rate of IOPS and throughput per GiB for both read and write operations.
  * `READ_OPTIMIZED` (read-optimized units): provides the highest rate of read operations and read throughput per GiB for read-intensive workloads.
  * `WRITE_OPTIMIZED` (write-optimized units): provides the highest rate of write operations and write throughput per GiB for write-intensive workloads.



You can commit to purchasing a combination (or _blend_) of these capacity unit types within a single commitment for a given Exapool type. As explained in [How capacity units work](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-exapools#how_capacity_units_work), the blend of capacity units that you choose determines your billing allocation and the maximum provisioned performance of the Exapool, rather than the performance of individual disks inside the pool.

### Applicable CUD rates

To learn more about discount rates for block storage commitments, contact your Google Cloud account team.

To purchase block storage commitments, see [Purchase block storage commitments for Exapools](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-block-storage-commitments).

## Quotas for commitments and committed resources

To purchase resource-based commitments in a specific region, you must have quota available in that region for your commitments and for any applicable committed resources:

  * **Commitments** : every resource-based commitment that you purchase requires regional quota for commitments, regardless of the commitment category.
  * **Committed resources** : depending on the commitment category and the type of resource that you commit to purchasing, you might also need regional quota for those specific committed resources. For example, to purchase commitments for any vCPUs, GPUs, Local SSD disks, or OS licenses, you must have quota available for those specific committed SKUs in the target region. You don't need separate quota for committed memory SKUs or block storage commitments.



For example, to purchase 5 hardware commitments that cover 32 vCPUs of general-purpose N1 machine type, 16 GB memory, 4 NVIDIA P4 GPUs, and 2 Local SSD disks in the `us-central1` region, you must have quota for each of the following:

  * Five commitments in `us-central1`
  * 32 committed N1 vCPUs in `us-central1`
  * Four committed NVIDIA P4 GPUs in `us-central1`
  * 750 GB (or 2 Local SSD disks) of committed Local SSD disk space in `us-central1`

**Note:** If your project is still in the free tier period with free tier credit remaining, or if your project doesn't have payment history, then it doesn't qualify for committed use discounts. As a result, the project isn't granted quota to purchase commitments.

### Quota limits

By default, Compute Engine offers a specific amount of commitment quota for each type of committed resource. These quota limits determine the number of commitments that you can purchase and the amount of resources that you can commit to purchasing. To learn how to view the current quota limits and quota usage values for your commitments and committed resources, see [View quotas in the Google Cloud console](https://docs.cloud.google.com/docs/quotas/view-manage#viewing_your_quota_console).

If you consistently pay for a very high amount of committed vCPUs for your projects across different regions, then you might be eligible for unlimited quota on your committed vCPUs for all machine types (except for memory-optimized machine types) in all regions.

If you use up all your commitment quota, then you won't be able to purchase new commitments. Likewise, if you exhaust your committed resource quota, then you won't be able to purchase a new commitment for that resource even if you have commitment quota available. For example, if you used up all of your commitment quota, then the server returns the following error when you make a commitment purchase request:
    
    
    "Quota 'COMMITMENTS' exceeded. Limit: 0.0"
    

### Increase quota limits

If you don't have enough quota for your commitments or your committed resources, then you can always request a quota increase from the [Quotas page](https://console.cloud.google.com/iam-admin/quotas). You can request quota increases at any time. To learn how to submit a request to increase quota limits for your resources, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

For example, consider a scenario where you purchased two commitments for a total of four `NVIDIA V100` GPUs in the `us-central1` region and met your quota limits. Suppose that you want to purchase two new commitments for two `NVIDIA V100 GPUs` each, in the same region. You must do the following:

  1. Submit a new quota request to increase your `Committed NVIDIA V100 GPUs` quota in `us-central1` to the new maximum number (eight) that you want.

  2. Submit a new quota request to increase your `Commitments` quota in `us-central1` to match the new maximum number (four) that you want.




Wait for your requests to be approved and closed. After your requests are approved, your commitment and committed GPU quotas in `us-central1` increase to match your new needs. You can then purchase your new commitments.

If you place a request for an increase in quota limit for a resource that already has unlimited quota by default, then the quota value for that resource remains unlimited and you are notified that your requested limit is below the approved limit.

### Set a cap for quota limits

You can set a cap on the quota value for your committed resources by [creating a quota override](https://docs.cloud.google.com/docs/quotas/view-manage#create_override). For resources that have unlimited quota by default, the quota override decreases the quota value. To remove the quota override for the resource and return to unlimited quota values by default, you must [reset the quota value](https://docs.cloud.google.com/docs/quotas/view-manage#reset_quota).

To learn more about how to manage quotas for your resources, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).

## CUD recommendations

Google Cloud analyzes your compute instance spending trends with and without a commitment and generates CUDs recommendations. You can use CUD recommendations to optimize your compute costs. You can compare the costs with and without a commitment, and estimate how much you can save each month with a commitment.

The [Recommender](https://docs.cloud.google.com/recommender/docs) generates a card with information about your instance usage over the last 30 days. If your instances show a trend of uncommitted usage over 30 days, then the Recommender classifies this as an opportunity to purchase commitments to reduce your instance costs.

CUD recommendations are refreshed once per day and take the previous 30 days of usage history into consideration. The recommendations are based on two logical model types that analyze your consumption:

  * **Recommendations for stable usage** : Calculates the recommended commitment quantity by analyzing resources that were continuously active over the 30-day period. These commitments cover steady-state workloads.
  * **Recommendations for optimal savings** : Calculates the recommended commitment quantity to maximize overall net savings. This model also considers periods of bursting or intermittent usage. This model recommends commitments for usage periods that exceed a financial break-even threshold, which represents the point where your discount outweighs the commitment cost compared to standard rates. For example, if a commitment offers a 30% discount, then an instance needs to run for more than 70% of the month to break even. Because this model maximizes overall net savings, recommended commitment quantities might sometimes exceed your uncommitted usage on specific days or hours.



Usage is considered uncommitted and eligible if the following is true:

  * The instance's uptime during the 30-day period met or exceeded the financial break-even threshold.
  * The resource belongs to a machine series or resource type that is eligible for resource-based CUDs.
  * The resource belongs to a [machine series or resource type that supports CUD recommendations](https://docs.cloud.google.com/docs/cuds-recommender#supported-resource-types-recommendation).
  * The instance's usage wasn't already covered by an existing commitment.



CUD recommendations are available in the Google Cloud console, through [Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery), and through the [Recommender API](https://docs.cloud.google.com/recommender/docs/overview).

In the **Billing** section of the Google Cloud console, you can view CUD recommendations on the following pages:

  * **[FinOps hub](https://console.cloud.google.com/billing/optimize)** : Displays only the top recommendations that yield the highest estimated savings, which are typically the optimal savings recommendations.
  * **Recommendations page** : Displays all available recommendations, which includes both stable usage and optimal savings recommendations. You can also view commitment recommendations for specific services or projects.



For information about how to view these recommendations, see [View recommendations](https://docs.cloud.google.com/docs/cuds-recommender#viewing-recommendations).

After you select a specific recommendation, you can also [create a scenario](https://docs.cloud.google.com/docs/cuds-recommender#simulate-scenarios) to simulate specific conditions and customize your recommendation. You can do the following as part of your scenario modeling:

  * Toggle between 1-year and 3-year commitment terms.
  * Adjust your coverage threshold.
  * Choose a different usage period to calculate your recommendation.
  * Opt to ignore atypical usage history.



To learn how to purchase your selected commitment recommendation, see [Apply recommendations to purchase additional commitments](https://docs.cloud.google.com/docs/cuds-recommender#purchasing-recommendations).

## View your commitments

To learn how to view the list and details of your commitments, see [View resource-based commitments](https://docs.cloud.google.com/compute/docs/committed-use-discounts/view-resource-based-commitments).

## Modify a commitment

You can modify your active commitments in the following ways:

  * You can change the auto-renew status for your commitment. For more information, see [Renew commitments automatically](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically).
  * You can extend your commitment's term beyond the preset duration of 1 or 3 years by specifying a custom end date for your commitment. For more information, see [Extend commitment terms](https://docs.cloud.google.com/compute/docs/committed-use-discounts/extend-commitment-term).
  * You can modify the amount of resources in your hardware commitments by either merging or splitting your existing commitments. For more information, see [Merge and split commitments](https://docs.cloud.google.com/compute/docs/instances/merge-and-split-commitments).
  * You can upgrade your 1-year hardware commitments and convert them into 3-year commitments. For more information, see [Upgrade commitments](https://docs.cloud.google.com/compute/docs/instances/upgrade-commitment-term).
  * You can change the Cloud Billing account that is linked to, and pays for, the project where you purchased your resource-based commitments. For more information, see [Change the billing account for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project) and [Impact of changing a project's Cloud Billing account](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#moving-project-billing-account).



After you purchase a commitment, you can't modify the commitment's project, commitment type, or region.

**Note:** You can't renew, extend, merge, split, or upgrade commitments that you purchased through [future reservations for capacity blocks in AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity) or [future reservations for capacity blocks for Cloud TPUs](https://docs.cloud.google.com/tpu/docs/long-term-reservation).

## Cancel a commitment

After you purchase a commitment, you can't cancel it. You must pay the agreed upon monthly amount for the duration of the commitment. Commitments aren't affected by future changes to [on-demand prices](https://cloud.google.com/compute/vm-instance-pricing) of your committed Compute Engine resources.

If you accidentally purchased a commitment or made a mistake while configuring your commitment, then you have 14 calendar days from the commitment start date to contact [Cloud Billing support](https://docs.cloud.google.com/support/billing) for help. Approval of any changes is subject to Google's discretion and isn't assured until confirmed by Google.

## Understand your bill with committed use discounts

Read the following documents to gain a better understanding of your billing:

  * [View and download the cost details of your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/cost-table).
  * [Analyze the effectiveness of your committed use discounts](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds).
  * [Understand your savings with cost breakdown reports](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown).



## Get support

If you have any questions regarding committed use discounts on your bill, you can [contact Google Cloud support](https://support.google.com/cloud/answer/6282346?ref_topic=3473162).

## What's next

  * Learn how to [renew resource-based commitments automatically](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically).
  * Learn how to [extend the term of resource-based commitments](https://docs.cloud.google.com/compute/docs/committed-use-discounts/extend-commitment-term).
  * Learn how to [upgrade resource-based commitments](https://docs.cloud.google.com/compute/docs/instances/upgrade-commitment-term).
  * Learn how to [merge and split resource-based commitments](https://docs.cloud.google.com/compute/docs/instances/merge-and-split-commitments).
  * Learn how to [analyze the effectiveness of your CUDs](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds).
  * Review the [prices of your resources with and without CUDs](https://cloud.google.com/compute/vm-instance-pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
