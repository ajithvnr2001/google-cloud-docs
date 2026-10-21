---
url: https://docs.cloud.google.com/compute/docs/committed-use-discounts/extend-commitment-term/
title: Extend commitment terms \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T07:09:32.157854+00:00
---

# Extend commitment terms  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/committed-use-discounts/extend-commitment-term/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Extend commitment terms Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information about extending the term of your [Compute Engine hardware resource-based commitments](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) beyond the preset 1- and 3-year options. 

Term extensions give you the flexibility to extend a commitment's term beyond the preset 1 or 3 years and specify a custom term duration of your choice—for example, 2, 3.5, or 5.5 years. By extending your commitment's term, you can tailor your commitment's term to match your resource usage needs and keep receiving the resulting committed use discounts (CUDs) for that longer and custom duration. You can extend the terms of both 1-year and 3-year commitments as follows:

  * **1-year commitments** : You can specify custom term durations that are greater than 1 year and less than 3 years.
  * **3-year commitments** : You can specify custom term durations that are greater than 3 years and less than 6 years.



For other ways to keep your commitments active for a longer duration, see the following alternatives:

  * If you have a 1-year commitment and you want a higher discount rate in addition to a longer term, then [upgrade your commitment](https://docs.cloud.google.com/compute/docs/instances/upgrade-commitment-term).
  * If you want your commitment to automatically renew for one or more full terms, then [enable auto-renewal on your commitment](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically).



## How term extension works

A commitment is active for a specific period, defined by its start and end dates, known as its _term_. If a commitment has auto-renewal enabled, then it begins a new term each time that it renews. When you perform a term extension, you are modifying the end date of only the commitment's **ongoing term** —the term that is active when you request the extension.

You can extend a commitment's ongoing term and set a custom term duration by specifying a future end date of your choice. Your commitment then becomes a custom term commitment. For 1-year commitments, the custom end date can be anywhere between 1 and 3 years (but can't be exactly 3 years) after the start date of the ongoing term. For 3-year commitments, the custom end date can be anywhere between 3 and 6 years (but can't be exactly 6 years) after the start date of the ongoing term.

You can perform a term extension for both new and existing commitments as follows:

  * **New commitments** : You can specify a custom end date when you purchase the commitment.
  * **Existing commitments** : After your commitment becomes active, you can specify or update the custom end date by updating the commitment's properties.



After you place a term extension request for your commitment, the changes take effect at 12 AM US and Canadian Pacific Time (UTC-8, or UTC-7 during daylight saving time) on the following day. Your commitment remains active until the new custom end date and its term gets adjusted accordingly. Extending your commitment's term doesn't affect the other properties of the commitment:

  * Name
  * Start date
  * Region
  * Project
  * Commitment type
  * Commitment plan
  * Auto-renewal setting
  * Committed resources



Extending your commitment's term doesn't change the CUD rate that you receive in return for that commitment.

Any [reservations that are attached to your commitment](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments#attach-reservations-to-resource-cuds) continue to exist throughout the lifetime of your extended term, unless you manually replace them.

### Term extension eligibility window

After a commitment's term begins, you have a limited time period during which you can request a term extension. This time period is called the _term extension eligibility window_.

Regardless of whether the commitment has a preset or custom term duration, the term extension eligibility window depends on the most recent operation that you performed on the commitment. Depending on the operation, the term extension eligibility window applies in the following ways:

  * **Newly purchased commitments** : For 1-year commitments, the eligibility window remains open up to four months after the commitment activation. For 3-year commitments, the eligibility window remains open up to one year after the commitment activation.

  * **Auto-renewed commitments** : If your commitment automatically renews for a new term, then the eligibility window refreshes at the start of the renewed term. For 1-year commitments, the eligibility window remains open up to four months from the start of the renewed term. For 3-year commitments, the eligibility window remains open up to one year from the start of the renewed term.

  * **Merged commitments** : If you merge commitments that have different eligibility windows, then, for the merged commitment, Compute Engine uses the eligibility window that ends the earliest.

  * **Split commitments** : When you split a commitment, the eligibility window remains the same for both the resized source commitment and the new split commitment.

  * **Upgraded commitments** : When you upgrade a 1-year commitment into a 3-year commitment, Compute Engine also updates the eligibility window for the commitment. The updated window remains open up to 1 year from the start of the ongoing term.

For example, suppose that your 1-year commitment's start date is January 1, 2024. The eligibility window for your original 1-year term remains open until May 1, 2024. Suppose that you then upgraded this commitment to a 3-year commitment on April 1, 2024. After the upgrade, your commitment's updated eligibility window remains open until January 1, 2025.




### Multiple term extensions

You can extend the term of your commitment any number of times within the term extension eligibility window. On any given day, for any given active commitment, you can place multiple term extension requests until 12 AM US and Canadian Pacific Time (UTC-8 or UTC-7) of the next day, as long as you specify a later end date each time. However, Google recommends that you minimize the number of term extension requests that you place for a single commitment on a given day.

After your term extension for a specific end date takes effect and your commitment has a new custom end date, you can't undo the term extension or reduce the duration of your commitment's term. You can perform subsequent extension operations only for end dates that are later than the most recently specified end date.

### Impact of pending commitment update requests

For existing, active commitments that already have a pending update request, you can place a new term extension request only if the pending request is also for a term extension. If the commitments have any pending update requests—such as merge, split, upgrade, or auto-renewal setting update—then, to request term extensions, you must wait for the pending operations to complete and the updates to take effect. After 12 AM US and Canadian Pacific Time (UTC-8 or UTC-7) on the following day, when the updates take effect, you can request a term extension for that commitment.

### Pricing implications

Your commitment fee is the sum of the discounted prices of all your committed resources. When you extend your commitment's term, the discounted prices of your resources stay the same for the entirety of your custom term, even if the on-demand prices change. For more information about resource prices, see [Compute Engine pricing](https://cloud.google.com/compute/all-pricing).

**Note:** If you merge or split your commitments, then the discounted prices for your committed resources might change on the day that your merged or split commitments become active.

### Quota considerations

To specify a custom end date while purchasing a commitment, you must have sufficient [quota available both for the commitment and the committed resources](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#quota). To specify a custom end date for an existing commitment, you don't typically need to request any additional quota.

## How term extension affects future commitment operations

If your commitment has a custom term duration, then performing any subsequent commitment management operations on your custom term commitment might affect its custom end date and eligibility window. The following sections explain how a custom term commitment behaves during other commitment operations:

### Auto-renewal for custom term commitments

The renewed term length of an automatically renewing commitment always matches the preset term length defined by the commitment's plan, which is either 1 year or 3 years. You also receive the same discount percentage. Even if your commitment has a [ custom term length](https://docs.cloud.google.com/compute/docs/committed-use-discounts/extend-commitment-term), Compute Engine renews your commitment only for its preset term length of either 1 or 3 years. Auto-renewal of a custom term commitment won't be for another term of that custom length. For examples, see the following:

  * A commitment with a custom term of 1.5 years will renew only for 1 additional year.
  * A commitment with a custom term of 5.5 years will renew only for 3 additional years.



If you want a custom term commitment to stay active for a longer time period than the renewed term, then you can request another term extension after its renewal. Your term extension eligibility window also gets refreshed at the start of your renewed term. For a 1-year commitment, the eligibility window during the renewed term remains open for up to 4 months after the renewal. For 3-year commitments, this window remains open for up to 1 year after the renewal.

For example, suppose that your 1-year commitment's start date was January 1, 2024\. You extend the term of this commitment and specify a custom end date of June 30, 2025. If you also enabled auto-renewal on your commitment, then, on July 1, 2025, your commitment gets renewed for another term of 1 year. The end date of the renewed term will be June 30, 2026. The term extension eligibility window during that renewed term remains open until November 1, 2025.

For more information about auto-renewal of commitments, see [Renew commitments automatically](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically).

### Merge operations for custom term commitments

Merge operations behave the same way for both commitments with custom term durations and preset term durations. The merged commitment inherits the following properties:

  * The end date that is furthest in the future among the source commitments, regardless of whether it's a custom end date.
  * The eligibility window that ends the earliest among the source commitments.



For example, suppose that you want to merge two custom term 1-year commitments. The first commitment has a start date of January 1, 2024, and has a custom end date of June 30, 2025. The eligibility window for the first commitment remains open until May 1, 2024. The second commitment has a start date of February 1, 2024, and a custom end date of July 30, 2025. The eligibility window for the second commitment remains open until June 1, 2024. If you merge these commitments on April 1, 2024, then the merged commitment inherits July 30, 2025 as its end date. The eligibility window for the merged commitment remains open until May 1, 2024.

For more information about merging commitments, see [Merge commitments](https://docs.cloud.google.com/compute/docs/instances/merge-and-split-commitments#merging).

### Split operations for custom term commitments

Split operations behave the same way for both commitments with custom term durations and preset term durations. The resized source commitment and the new split commitments retain the same custom end date and term extension eligibility window.

For example, suppose that your 1-year commitment's start date is January 1, 2024, and has a custom end date of June 30, 2025. The eligibility window for your commitment remains open until May 1, 2024. Suppose that on March 1, 2024, you split this commitment into two separate commitments. The newly split commitments inherit the custom end date of June 30, 2025, and their eligibility windows remain open until May 1, 2024.

For more information about splitting commitments, see [Split commitments](https://docs.cloud.google.com/compute/docs/instances/merge-and-split-commitments#splitting).

### Upgrade operations for custom term commitments

You can upgrade 1-year commitments that have custom term durations. Upgrading a custom term commitment works the same way as upgrading commitments that have preset term durations. When you upgrade a 1-year commitment with a custom term duration, Compute Engine does the following:

  * Changes the commitment's plan to 3 years
  * Moves the end date of the commitment's ongoing term by two years into the future.



For example, suppose that your 1-year commitment has a start date of January 1, 2024, and has a custom end date of June 30, 2025. The eligibility window for your original 1-year term remains open until May 1, 2024. If you upgrade this commitment on April 1, 2024, then the commitment changes to a 3-year commitment with an end date of June 30, 2027. The commitment's updated eligibility window remains open until January 1, 2025. You also start receiving the CUD rate that is applicable for a 3-year commitment.

For more information about upgrading commitments, see [Upgrade commitments](https://docs.cloud.google.com/compute/docs/instances/upgrade-commitment-term).

## Limitations

The following limitations apply to term extensions of resource-based commitments:

  * You can extend the terms of only hardware resource commitments.
  * You can't extend the terms of inactive or expired commitments.
  * You can't extend the terms of commitments that you purchased through [future reservations for capacity blocks](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type#reserve-capacity-aihc).
  * For 1-year commitments, you can't specify a custom end date that results in a total commitment term of 3 years or longer. Instead, consider changing your commitment's plan from a 1-year to 3-year by [upgrading your commitment](https://docs.cloud.google.com/compute/docs/instances/upgrade-commitment-term).
  * For 3-year commitments, you can't specify a custom end date that results in a total commitment term of 6 years or longer. Instead, consider [enabling auto-renewal on your commitment](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically#enable_auto-renewal_on_an_existing_commitment). Auto-renewal enables your commitment to renew for another term of 3 full years.
  * When a custom term commitment renews, the new term has the 1-year or 3-year duration that is defined by the commitment's plan, rather than the custom duration.
  * For existing active commitments that already have a pending commitment update request, you can place a new term extension request only if the pending request is also for a term extension. If the commitments have any other pending update requests—such as merge, split, upgrade, or auto-renewal setting update—then, to request term extensions, you must wait until after 12 AM US and Canadian Pacific Time (UTC-8 or UTC-7) on the following day for the pending operations to complete and the updates to take effect.



## Requirements

You must meet the following requirements to successfully extend the term of a commitment:

  * The term extension request must be placed during the term extension eligibility window for the commitment.
  * For 1-year commitments, the custom end date must be between 1 and 3 years (but can't be exactly 3 years) into the future from the start date of the ongoing term.
  * For 3-year commitments, the custom end date must be between 3 and 6 years (but can't be exactly 6 years) into the future from the start date of the ongoing term.
  * You mustn't have any other ongoing or pending merge, split, upgrade, or renewal operations for that commitment.



## Best practices

Google recommends that you follow these best practices when you extend a commitment's term:

  * Before you place a term extension request, wait for all other pending commitment operations to complete and the updates to take effect.
  * Minimize the number of term extension requests that you place for a single commitment on the same day.



## Extend the term when you purchase the commitment

When you purchase a commitment, you can specify a custom end date to extend the preset 1- or 3-year term.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.commitments.create` on the project or organization.



To purchase a commitment that has an extended term duration, follow these steps:

###  Console 

Before you purchase your commitment, in the Google Cloud console, select the project that you want to use to purchase the commitment. If [CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects) is enabled for a Cloud Billing account, then you can purchase the commitment using any project from that Cloud Billing account.

  1. In the Google Cloud console, go to the **Committed use discounts** page.

[Go to Committed use discounts](https://console.cloud.google.com/compute/commitments)

  2. Click add_box **Purchase commitment**. The **Purchase a commitment** page appears.

  3. On the **Purchase a commitment** page, specify the properties for your commitment, as follows:

     1. To configure a term extension for your commitment, in the **Term** section, do the following:

        1. Specify the _[plan](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#commitment-plan)_ for your commitment by selecting either **1 year** or **3 years**. The plan determines the CUD rate and preset term duration of your commitment.

        2. Review the **Start date** field, which shows the date and time when your commitment becomes active. This field is automatically set to 12 AM US and Canadian Pacific Time on the day after your current date.

        3. To specify a custom end date for your commitment, in the **End date** field, specify the date that you want.

     2. For instructions on how to configure other properties for your commitment, see one of the following pages depending on your use case:

        * [Purchase hardware resource-based commitments without attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments)
        * [Purchase hardware resource-based commitments with attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments-with-reservations)

At a minimum, you must specify the name, region, resources, [commitment type](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#commitment-types-for-hardware-commitments), and [commitment plan](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#commitment-plan).

  4. In the **Summary** pane on the right, review your commitment details and any potential quota limitations.

  5. To finish purchasing your commitment, do the following:

     1. Navigate to the bottom of the page.

     2. Review the **Disclosures** section that contains information about fees, discount eligibility, and terms and conditions.

     3. To confirm your acceptance of the [commitment price](https://cloud.google.com/products/compute/pricing) and [service specific terms](https://cloud.google.com/terms/service-terms), select the checkbox.

     4. Click **Purchase**.




###  gcloud 

To purchase a commitment with a custom and extended term, run the [`gcloud compute commitments create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments/create) and include the `--custom-end-time` flag.

For example, to purchase a commitment for vCPUs, memory, or both, use the following command:
    
    
    gcloud compute commitments create COMMITMENT_NAME \
        --region=REGION \
        --project=PROJECT_ID \
        --plan=COMMITMENT_PLAN \
        --type=COMMITMENT_TYPE \
        --resources=vcpu=NUMBER_VCPUS,memory=MEMORY \
        **--custom-end-time= CUSTOM_END_DATE**
    

Replace the following:

  * `COMMITMENT_NAME`: the name of the commitment
  * `REGION`: the region of the commitment and where you want to commit to purchasing Compute Engine resources.
  * `PROJECT_ID`: the ID of the project
  * `COMMITMENT_PLAN`: the commitment plan. This property also determines the minimum duration for which you must commit to purchasing resources. Specify one of the following values:

    * For a 1-year commitment: `12-month`
    * For a 3-year commitment: `36-month`.
  * `COMMITMENT_TYPE`: the machine series for which you want to commit to purchasing resources. The following options are available:

    * For A2 machine types, use `accelerator-optimized`
    * For A3 Edge and A3 High machine types, use `accelerator-optimized-a3`
    * For A3 Mega machine types, use `accelerator-optimized-a3-mega` Note: For A4X Max, A4X, A4, or A3 Ultra machine types, you must purchase your commitments by using the _future reservations in AI Hypercomputer_ consumption option. For more information, see [ Reserve capacity through your account team](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity).
    * For G2 machine types, use `graphics-optimized`
    * For G4 machine types, use `graphics-optimized-g4`
    * For C2 machine types, use `compute-optimized`
    * For C2D machine types, use `compute-optimized-c2d`
    * For C3 machine types, use `compute-optimized-c3`
    * For C3D machine types, use `compute-optimized-c3d` **Caution** : For C3 and C3D commitment types, the machine family that is specified by the commitment type changes depending on the interface: 
      * In the gcloud CLI and REST, the commitment type values use _Compute-optimized_ as the machine family, even though C3 and C3D are part of the general-purpose machine family.
      * In the Google Cloud console, the commitment type values use the correct machine series: _General-Purpose_.
Make sure to select the correct commitment type value that corresponds to the interface that you're using. 
    * For H3 machine types, use `compute-optimized-h3`
    * For H4D machine types, use `compute-optimized-h4d`
    * For N1 machine types, use `general-purpose`
    * For C4 machine types, use `general-purpose-c4`
    * For C4A machine types, use `general-purpose-c4a`
    * For C4D machine types, use `general-purpose-c4d`
    * For C4N machine types, use `network-optimized-c4n`
    * For E2 machine types, use `general-purpose-e2`
    * For N2 machine types, use `general-purpose-n2`
    * For N2D machine types, use `general-purpose-n2d`
    * For N4 machine types, use `general-purpose-n4`
    * For N4D machine types, use `general-purpose-n4d`
    * For N4A machine types, use `general-purpose-n4a`
    * For Tau T2D machine types, use `general-purpose-t2d`
    * For M1 or M2 machine types, use `memory-optimized`
    * For M3 machine types, use `memory-optimized-m3`
    * For M4 machine types with 6 TB of memory, use `memory-optimized-m4-6tb`
    * For other M4 machine types, use `memory-optimized-m4`
    * For the M4N machine type with 6 TB of memory, use `memory-optimized-m4n-6tb`
    * For other M4N machine types, use `memory-optimized-m4n`
    * For X4 machine types with 6 TB of memory, use `memory-optimized-x4-6t`
    * For X4 machine types with 8 TB of memory, use `memory-optimized-x4-8t`
    * For X4 machine types with 12 TB of memory, use `memory-optimized-x4-12t`
    * For X4 machine types with 16 TB of memory, use `memory-optimized-x4-960-16t`
    * For X4 machine types with 24 TB of memory, use `memory-optimized-x4-1440-24t`
    * For X4 machine types with 32 TB of memory, use `memory-optimized-x4-1920-32t`
    * For Z3 machine types, use `storage-optimized-z3`
    * For Z4D machine types, use `storage-optimized-z4d`
    * For Z4M machine types, use `storage-optimized-z4m`

If you don't specify the `--type` flag, then Compute Engine uses `general-purpose` as the default value.

  * `NUMBER_VCPUS`: the number of vCPUs that you want to commit to purchasing.

  * `MEMORY`: the amount, in MB or GB, of memory that you want to commit to purchasing—for example, `1000MB` or `100GB`. If you don't specify the units, then Compute Engine uses `GB` as the default unit.

  * `CUSTOM_END_DATE`: the custom end date for your term, which must be formatted as `YYYY-MM-DD`. For example, to specify a custom end date of April 20, 2024, format it as `2024-04-20`.




For detailed syntax of how to extend the term when you purchase a commitment for GPUs, local SSD disks, or both, see [Purchase hardware resource-based commitments with attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments-with-reservations).

For example, consider a commitment (`example-commitment`) in the `us-central1` region with resources specified as four N1 vCPUs and nine GB memory. The commitment plan for the commitment is `12-month`. Suppose that you want to purchase this commitment on January 1, 2024, and want a custom term that ends at the end of June 30, 2025. To purchase this commitment, run the following command:
    
    
    gcloud compute commitments create example-commitment \
        --region=us-central1 \
        --project=my-project \
        --plan=12-month \
        --type=general-purpose \
        --resources=memory=9GB,vcpu=4 \
        **--custom-end-time=2025-07-01**
    

###  REST 

To purchase a commitment with a custom and extended term, make a `POST` request to the [`regionCommitments.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCommitments/insert). In the request body, include the `customEndTimestamp` field.

For example, to purchase a commitment for vCPUs, memory, or both, use the following `POST` request body:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/commitments
    {
        "name": "COMMITMENT_NAME",
        "plan": "COMMITMENT_PLAN",
        "type": "COMMITMENT_TYPE",
        "resources":
        [
            {
                "amount": "NUMBER_VCPUS",
                "type": "VCPU"
            },
            {
                "amount": "MEMORY",
                "type": "MEMORY"
            }
        ],
        **"customEndTimestamp": " CUSTOM_END_DATETEND_TIMEZ"**
    }
    

Replace the following:

  * `COMMITMENT_NAME`: the name of the commitment
  * `REGION`: the region of the commitment and where you want to commit to purchasing Compute Engine resources.
  * `PROJECT_ID`: the ID of the project
  * `COMMITMENT_PLAN`: the commitment plan. This property also determines the minimum duration for which you must commit to purchasing resources. Specify one of the following values:

    * For a 1-year commitment: `TWELVE_MONTH`
    * For a 3-year commitment: `THIRTY_SIX_MONTH`.
  * `COMMITMENT_TYPE`: the machine series for which you want to commit to purchasing resources. The following options are available:

    * For A2 machine types, use `ACCELERATOR_OPTIMIZED`
    * For A3 Edge and A3 High machine types, use `ACCELERATOR_OPTIMIZED_A3`
    * For A3 Mega machine types, use `ACCELERATOR_OPTIMIZED_A3_MEGA` Note: For A4X Max, A4X, A4, or A3 Ultra machine types, you must purchase your commitments by using the _future reservations in AI Hypercomputer_ consumption option. For more information, see [ Reserve capacity through your account team](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity).
    * For G2 machine types, use `GRAPHICS_OPTIMIZED`
    * For G4 machine types, use `GRAPHICS_OPTIMIZED_G4`
    * For C2 machine types, use `COMPUTE_OPTIMIZED`
    * For C2D machine types, use `COMPUTE_OPTIMIZED_C2D`
    * For C3 machine types, use `COMPUTE_OPTIMIZED_C3`
    * For C3D machine types, use `COMPUTE_OPTIMIZED_C3D` **Caution** : For C3 and C3D commitment types, the machine family that is specified by the commitment type changes depending on the interface: 
      * In the gcloud CLI and REST, the commitment type values use _Compute-optimized_ as the machine family, even though C3 and C3D are part of the general-purpose machine family.
      * In the Google Cloud console, the commitment type values use the correct machine series: _General-Purpose_.
Make sure to select the correct commitment type value that corresponds to the interface that you're using. 
    * For H3 machine types, use `COMPUTE_OPTIMIZED_H3`
    * For H4D machine types, use `COMPUTE_OPTIMIZED_H4D`
    * For N1 machine types, use `GENERAL_PURPOSE`
    * For C4 machine types, use `GENERAL_PURPOSE_C4`
    * For C4A machine types, use `GENERAL_PURPOSE_C4A`
    * For C4D machine types, use `GENERAL_PURPOSE_C4D`
    * For C4N machine types, use `NETWORK_OPTIMIZED_C4N`
    * For E2 machine types, use `GENERAL_PURPOSE_E2`
    * For N2 machine types, use `GENERAL_PURPOSE_N2`
    * For N2D machine types, use `GENERAL_PURPOSE_N2D`
    * For N4 machine types, use `GENERAL_PURPOSE_N4`
    * For N4D machine types, use `GENERAL_PURPOSE_N4D`
    * For N4A machine types, use `GENERAL_PURPOSE_N4A`
    * For Tau T2D machine types, use `GENERAL_PURPOSE_T2D`
    * For M1 or M2 machine types, use `MEMORY_OPTIMIZED`
    * For M3 machine types, use `MEMORY_OPTIMIZED_M3`
    * For M4 machine types with 6 TB of memory, use `MEMORY_OPTIMIZED_M4_6TB`
    * For other M4 machine types, use `MEMORY_OPTIMIZED_M4`
    * For the M4N machine type with 6 TB of memory, use `MEMORY_OPTIMIZED_M4N_6TB`
    * For other M4N machine types, use `MEMORY_OPTIMIZED_M4N`
    * For X4 machine types with 6 TB of memory, use `MEMORY_OPTIMIZED_X4_480_6T`
    * For X4 machine types with 8 TB of memory, use `MEMORY_OPTIMIZED_X4_480_8T`
    * For X4 machine types with 12 TB of memory, use `MEMORY_OPTIMIZED_X4_960_12T`
    * For X4 machine types with 16 TB of memory, use `MEMORY_OPTIMIZED_X4_960_16T`
    * For X4 machine types with 24 TB of memory, use `MEMORY_OPTIMIZED_X4_1440_24T`
    * For X4 machine types with 32 TB of memory, use `MEMORY_OPTIMIZED_X4_1920_32T`
    * For Z3 machine types, use `STORAGE_OPTIMIZED_Z3`
    * For Z4D machine types, use `STORAGE_OPTIMIZED_Z4D`
    * For Z4M machine types, use `STORAGE_OPTIMIZED_Z4M`
  * `NUMBER_VCPUS`: the number of vCPUs that you want to commit to purchasing.

  * `MEMORY`: the amount, in MB, of memory that you want to commit to purchasing—for example, `10240MB`.

  * `CUSTOM_END_DATE`: the custom end date for your term, which must be formatted as `YYYY-MM-DD`. For example, to specify a custom end date of April 20, 2024, format it as `2024-04-20`.

  * `END_TIME`: 12 AM US and Canadian Pacific Time (UTC-8 or UTC-7), as an offset of [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). Specify one of the following values:

    * During daylight saving time: `07:00:00`
    * During other times: `08:00:00`



For detailed syntax of how to extend the term when you purchase a commitment for GPUs, local SSD disks, or both, see [Purchase hardware resource-based commitments with attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments-with-reservations).

For example, consider a commitment (`example-commitment`) in the `us-central1` region with resources specified as four N1 vCPUs and nine GB memory. The commitment plan for the commitment is `TWELVE_MONTH`. Suppose that you want to purchase this commitment on January 1, 2024, and want a custom term that ends at the end of June 30, 2025\. To purchase this commitment, make the following request:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/my-project/regions/us-central1/commitments
    {
        "name": "example-commitment",
        "plan": "TWELVE_MONTH",
        "type": "GENERAL_PURPOSE",
        "resources":
        [
            {
                "amount": "4",
                "type": "VCPU"
            },
            {
                "amount": "9216",
                "type": "MEMORY"
            }
        ],
        **"customEndTimestamp": "2025-07-01T07:00:00Z"**
    }
    

## Extend the term of an existing commitment

You can extend the term of an existing, active commitment by updating the commitment's properties to specify or update the custom end date.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.commitments.update` on the project or organization.



To extend the term of an existing commitment, use one of the following options:

###  Console 

Before you initiate the term extension operation, on the Google Cloud console, select the project where you want to extend your commitment's term.

  1. In the Google Cloud console, go to the **Committed use discounts** page.

[Go to Committed use discounts](https://console.cloud.google.com/compute/commitments)

The **Commitment list** page opens and displays the **Hardware commitments** tab.

  2. To initiate the term extension operation for a commitment, on the **Hardware commitments** tab, select an active commitment, and then click **Extend**.

Alternatively, you can do the following:

     1. On the **Hardware commitments** tab of the **Commitment list** page, click the name of the active commitment that you want to extend.

     2. On the **Hardware commitment details** page for the selected commitment, click **Extend**.

The **Extend** pane appears for the selected commitment.

  3. To complete the term extension operation, in the **Extend** pane for the commitment, do the following:

     1. Review your **Commitment details**.

     2. In the **Select an end date** field, specify a custom end date for your commitment.

     3. In the **Commitment timeline** section, review the **New end date** field.

     4. To confirm the term extension request, click **Extend**.




###  gcloud 

To extend the term of an existing active commitment, run the [`gcloud compute commitments update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments/update) and include the `--custom-end-time` flag.
    
    
    gcloud compute commitments update COMMITMENT_NAME \
        --region=REGION \
        --project=PROJECT_ID \
        **--custom-end-time= CUSTOM_END_DATE**
    

Replace the following:

  * `COMMITMENT_NAME`: the name of the commitment
  * `PROJECT_ID`: the ID of the project
  * `REGION`: the region of the commitment and where you want to commit to purchasing Compute Engine resources.
  * `CUSTOM_END_DATE`: the custom end date that you want for your term, in the `YYYY-MM-DD` format, where `YYYY` is the year, `MM` is the month, and `DD` is the day. For example, to specify a custom end date of April 20, 2024, format it as `2024-04-20`.



For example, consider a custom term commitment (`example-commitment`) in the `us-central1` region with resources specified as four N1 vCPUs and nine GB memory. The commitment plan for the commitment is `12-month`. This commitment was purchased on January 1, 2024, and expires on June 30, 2025\. To extend its term further until the end of June 30, 2026, run the following command:
    
    
    gcloud compute commitments update example-commitment \
        --region=us-central1 \
        --project=my-project \
        **--custom-end-time=2026-07-01**
    

###  REST 

To extend the term of an existing active commitment, make a `PATCH` request to the [`regionCommitments.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCommitments/update). In the request body, include the `customEndTimestamp` field.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/commitments/COMMITMENT_NAME
    {
        "name": "COMMITMENT_NAME",
        **"customEndTimestamp": " CUSTOM_END_DATETEND_TIMEZ"**
    }
    

Replace the following:

  * `COMMITMENT_NAME`: the name of the commitment
  * `REGION`: the region of the commitment and where you want to commit to purchasing Compute Engine resources.
  * `PROJECT_ID`: the ID of the project
  * `CUSTOM_END_DATE`: the custom end date that you want for your term, in the `YYYY-MM-DD` format, where `YYYY` is the year, `MM` is the month, and `DD` is the day. For example, to specify a custom end date of April 20, 2024, format it as `2024-04-20`.
  * `END_TIME`: 12 AM US and Canadian Pacific Time (UTC-8 or UTC-7), as an offset of [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). Specify one of the following values:

    * During daylight saving time: `07:00:00`
    * During other times: `08:00:00`



For example, consider a custom term commitment (`example-commitment`) in the `us-central1` region with resources specified as four N1 vCPUs and nine GB memory. The commitment plan for the commitment is `12-month`. This commitment was purchased on January 1, 2024, and expires on June 30, 2025\. To extend its term further until the end of June 30, 2026, make the following request:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/my-project/regions/us-central1/commitments/example-commitment
    {
        "name": "example-commitment",
        **"customEndTimestamp": "2026-07-01T07:00:00Z"**
    }
    

## What's next

  * Learn how to [renew resource-based commitments automatically](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically).
  * Learn how to [upgrade resource-based commitments](https://docs.cloud.google.com/compute/docs/instances/upgrade-commitment-term).
  * Learn how to [analyze the effectiveness of your CUDs](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
