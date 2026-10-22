---
url: https://docs.cloud.google.com/compute/docs/instances/merge-and-split-commitments/
title: Merge and split commitments \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:12:44.244749+00:00
---

# Merge and split commitments  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/merge-and-split-commitments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Merge and split commitments Stay organized with collections  Save and categorize content based on your preferences. 

To help you manage the resource requirements for your projects, Compute Engine lets you merge or split your existing commitments and redistribute your resources to match the granularity that your projects require.

This document describes the benefits and process of merging and splitting commitments, including their limitations and requirements.

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




## Merge commitments

You can merge multiple compatible commitments to create a new larger commitment. By merging commitments, you can track and manage them as a single entity. Merging commitments helps you avoid staggered commitment end dates by co-terming the individual commitments to expire at the same time. Merging also lets you gradually ramp up your workloads. For example, you can purchase newer, smaller commitments when the need arises and choose to merge them together or with an existing commitment.

**Caution:** When you merge commitments, Google deletes all prioritized attribution rules that are associated with those commitments and you can't recover those rules. If you want to continue using the prioritized attribution rules on merged commitments, then you must recreate the rules after creating the merged commitment.

### How merging works

When you merge individual commitments (source commitments), you create a new commitment (merged commitment) that combines resources from all source commitments. At 12 AM US and Canadian Pacific Time (UTC-8, or UTC-7 during daylight saving time) on the following day, the merged commitment becomes active and the source commitments are canceled. This activation date becomes the merged commitment's start date, and the merge operation concludes.

The merged commitment inherits the following properties, regardless of whether the source commitments have a preset or custom term duration:

  * The end date that is furthest in the future among the source commitments.
  * The term extension eligibility window that ends the earliest among the source commitments.



Because the merged commitment can be created only after your source commitments are active, the merged commitment might have a custom term duration instead of the preset term duration of 1 or 3 years. However, the merged commitment retains the 1- or 3-year commitment plan of the source commitments.

For example, consider two source commitments starting on January 1, 2020, and December 1, 2020. Their end dates are January 1, 2023, and December 1, 2023, respectively. The term extension eligibility window for the first commitment remains open until May 1, 2020, and for the second commitment until April 1, 2021. If you merge these commitments on March 1, 2022, then your merged commitment is a custom term commitment with a start date of March 2, 2022, and an end date of December 1, 2023. The term extension eligibility window for the merged commitment would have already ended by May 1, 2020.

If any source commitments have reservations attached, then the reservations are preserved during the merge and are attached to the merged commitment after its creation. For more information about commitments with attached reservations, see [Attach reservations to resource-based commitments](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments#attach-reservations-to-resource-cuds).

### Example of a merged commitment

The following table shows the properties of source and merged commitments when you merge two commitments (`source-commitment-1` and `source-commitment-2`) into a single commitment (`merged-commitment`) on March 1, 2022:

|  **First source commitment** |  **Second source commitment** |  **Merged commitment**  
---|---|---|---  
**Name** | source-commitment-1 | source-commitment-2 | merged-commitment  
**Type** | N2 | N2 | N2  
**Region** | us-central1 | us-central1 | us-central1  
**Resources** | 

  * vCPUs: 100
  * Memory: 100 GB

| 

  * vCPUs: 200
  * Memory: 300 GB

| 

  * vCPUs: 300
  * Memory: 400 GB

  
**Plan** | 3 years | 3 years | 3 years  
**Term** | 3 years | 3 years | Custom (1 year, 9 months)  
**Start date *** | January 1, 2020 | December 1, 2020 | March 2, 2022  
(the day after the merge)  
**End date †** | January 1, 2023 | December 1, 2023 | December 1, 2023  
**Term extension eligibility window open until** | May 1, 2020 | April 1, 2021 | May 1, 2020  
  
*All commitments start at 12 AM US and Canadian Pacific Time (UTC-8 or UTC-7) on the specified start date.  
†All commitments expire at 12 AM US and Canadian Pacific Time (UTC-8 or UTC-7) on the specified end date. 

### Pricing implications

Your commitment fee is the sum of the discounted prices of all your committed resources. When you merge your commitments, the discounted prices of the merged commitment's resources might change on the day that the merged commitment becomes active. This new discounted price for each resource remains the same until the end of your merged commitment's term, even if on-demand prices change. However, if you merge or split this commitment again, then the discounted prices of the resources might change again.

### Limitations

  * You can't merge software license commitments or block storage commitments.
  * You can't merge commitments that you purchased through [future reservations for capacity blocks for GPU VMs](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity) or [future reservations for capacity blocks for Cloud TPU VMs](https://docs.cloud.google.com/tpu/docs/long-term-reservation).
  * The merged commitment automatically includes any reservations already attached to source commitments. You can't attach any additional reservations (new or existing) to the merged commitment.
  * You can't merge commitments that have expired or are canceled.
  * By default, when you create merged commitments, the auto-renewal setting is disabled on the new commitments, even if all source commitments were set to renew automatically. If you want your merged commitments to renew automatically, then you must manually enable the auto-renewal setting on those commitments. You can do so either [at the time of their creation](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically#create_a_commitment_that_renews_automatically) or [after their creation](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically#enable_auto-renew_on_an_existing_commitment).



### Requirements

When you merge individual source commitments to create a new merged commitment, your source and merged commitments must meet the following requirements:

  * The source commitments must have the same project, region, commitment plan, commitment type, and commitment category.
  * The merged commitment must have the same project, region, commitment plan, commitment type, and commitment category as the source commitments. However, you can choose a new name for your merged commitment.
  * The resource types that you specify for your merged commitment must exactly match the resource types in the source commitments. Also, the quantity for each resource type in your merged commitment must be the sum of the quantities for that resource type in all source commitments. For example, if the first source commitment has 100 vCPUs and 100 GB memory, and the second source commitment has 200 vCPUs and 300 GB memory, then you must create your merged commitment with 300 vCPUs and 400 GB memory.
  * The source and merged commitments must be for hardware resources (vCPUs, memory, GPUs, and Local SSD disks).



### Create merged commitments

Create a merged commitment by using the Google Cloud console, the gcloud CLI, or REST. Before you merge commitments, review the limitations for merging.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.commitments.create` on the project or organization.



### Console

  1. In the Google Cloud console, select the project where you want to merge commitments. Then, go to the **Committed use discounts** page.

[Go to Committed use discounts](https://console.cloud.google.com/compute/commitments)

  2. To initiate the merge operation for a set of commitments, in the **Hardware commitments** tab of the **Commitment list** page, click **Merge**.

Alternatively, you can also select the commitments that you want to merge from the list and then click **Merge**.

  3. On the **Choose commitment** tab of the **Merge** page that opens, do the following:

     1. Under **Choose commitments to merge** , select the commitments that you want to merge from the list. If you already selected these commitments on the **Commitment list** page, then verify your selected commitments on this tab.

Optional: To filter the commitment list, specify the **Plan** , **Region** , and **Commitment type** values for your merged commitment before you select any commitments.

     2. Click **Next**. The **Review** tab opens.

  4. On the **Review** tab of the **Merge** page, do the following:

     1. Review and confirm the details of the merged commitment. To modify the list of individual commitments, select the **Choose commitment** tab on the left side of the window and repeat step 3.

     2. In the **New commitment name** field, enter a name for your merged commitment.

     3. Optional: To enable auto-renewal on your merged commitment, select the **Enable auto renew** checkbox.

     4. Read the **Terms and conditions**.

     5. To finish creating your merged commitment and return to the **Commitment list** page, click **Merge**.




###  gcloud 

To merge existing commitments into a single commitment, use the [gcloud compute commitments create command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments/create) with the `--merge-source-commitments` flag.
    
    
    gcloud compute commitments create COMMITMENT_NAME \
        --region=REGION \
        --project=PROJECT_ID \
        --plan=COMMITMENT_PLAN \
        --type=COMMITMENT_TYPE \
        --resources=vcpu=NUMBER_VCPUS,memory=MEMORY \
        --merge-source-commitments=SOURCE_COMMITMENT_URLS
    

Replace the following:

  * `COMMITMENT_NAME`: the name of your new merged commitment.
  * `NUMBER_VCPUS`: the sum of the numbers of vCPUs in the source commitments.
  * `COMMITMENT_TYPE`: the same commitment type as your source commitments, one of the following: 

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
  * `REGION`: the same region as your source commitments.

  * `PROJECT_ID`: the project ID of the project for which you want to merge commitments.

  * `COMMITMENT_PLAN`: the commitment plan ('12-month' or '36-month'), which must be the same as your source commitments.

  * `MEMORY`: the sum of the amounts of memory, in MB or GB, in the source commitments. For example, 1000 MB. If you don't specify a unit, then the default unit is GB.

  * `SOURCE_COMMITMENT_URLS`: a comma-separated list of at least two distinct source commitment URLs. Don't add spaces between the URLs.




For example, consider two source commitments in the `us-east1` region with resources specified as four N2 vCPUs and 2048 MB, and three N2 vCPUs and 2048 MB, respectively. The commitment plan for each source commitment is `12-month`. The following gcloud CLI command merges the two commitments and creates a new commitment called `merged-commitment`. The merged commitment specifies its resources as seven N2 vCPUs and 4096 MB, and its commitment plan is `12-month`:
    
    
    gcloud compute commitments create merged-commitment \
        --plan=12-month \
        --project=myproject \
        --region=us-east1 \
        --type=general-purpose-n2 \
        --resources=vcpu=7,memory=4096MB \
        --merge-source-commitments=projects/myproject/regions/us-east1/commitments/source-commitment-1,projects/myproject/regions/us-east1/commitments/source-commitment-2
    

###  REST 

To merge existing commitments into a single commitment, use the [`regionCommitments.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCommitments/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/commitments
    {
      "name": "COMMITMENT_NAME",
      "plan": "COMMITMENT_PLAN",
      "type": "COMMITMENT_TYPE",
      "region": "REGION",
      "resources": [
        {
          "type": "VCPU",
          "amount": "NUMBER_VCPUS"
        },
        {
          "type": "MEMORY",
          "amount": "MEMORY"
        }
      ],
      "mergeSourceCommitments": ["SOURCE_COMMITMENT_URL" ...]
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the project for which you want to merge commitments.
  * `REGION`: the same region as your source commitments.
  * `COMMITMENT_TYPE`: the same commitment type as your source commitments, one of the following:

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
  * `COMMITMENT_PLAN`: the commitment plan ('TWELVE_MONTH' or 'THIRTY_SIX_MONTH'), which must be the same as your source commitments.

  * `COMMITMENT_NAME`: the name of your new merged commitment.

  * `NUMBER_VCPUS`: the total number of vCPUs in the source commitments.

  * `MEMORY`: the sum of the amounts of memory, in MB, in the source commitments. For example, 1000 MB. If you don't specify a unit, then the default unit is MB.

  * `SOURCE_COMMITMENT_URL`: the URL of the source commitment that you want to merge. You must specify a comma-separated list of distinct source commitment URLs.




For example, consider two source commitments (`source-commitment-1` and `source-commitment-2`) in the `us-east1` region with their resources specified as (four N2 vCPUs and 2048 MB) and (three N2 vCPUs and 2048 MB) respectively. The commitment plan for each source commitment is `TWELVE_MONTH`. The following `POST` request merges the source commitments and creates a new commitment called `merged-commitment`. The merged commitment specifies its resources as seven N2 vCPUs and 4096 MB, and its commitment plan is `TWELVE_MONTH`.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/myproject/regions/us-east1/commitments
    {
      "name": "merged-commitment",
      "plan": "TWELVE_MONTH",
      "type": "GENERAL_PURPOSE_N2",
      "region": "us-east1",
      "resources": [
        {
          "type": "VCPU",
          "amount": "7"
        },
        {
          "type": "MEMORY",
          "amount": "4096"
        }
      ],
      "mergeSourceCommitments": [
        "projects/myproject/regions/us-east1/commitments/source-commitment-1",
        "projects/myproject/regions/us-east1/commitments/source-commitment-2",
        ...
      ]
    }
    

## Split commitments

You can transfer resources out of an existing commitment and split the commitment into smaller commitments. Splitting lets you closely monitor and manage portions of a large commitment as smaller individual commitments. For example, you can set only a portion of a commitment to [renew automatically](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically) by splitting it and enabling automatic renewal for only one of the child commitments. With splitting, you can also distribute your committed use discounts at a more granular level by using [prioritized attribution](https://docs.cloud.google.com/docs/cuds-attribution#type-prioritized) for the split commitments.

**Caution:** When you split commitments, Google deletes all prioritized attribution rules that are associated with those commitments and you can't recover those rules. If you want to continue using the prioritized attribution rules on split commitments, then you must recreate the rules after creating the split commitment.

### How splitting works

When you split an existing commitment (source commitment), you transfer resources out of your source commitment, create one or more new commitments (split commitments), and redistribute the transferred resources among the new split commitments. Both the activation of split commitments and the resizing of the source commitment take place at 12 AM US and Canadian Pacific Time (UTC-8, or UTC-7 during daylight saving time) on the following day. Compute Engine sets this activation date as the start date for the split commitments. After the split operation concludes, you have the following commitments:

  * The resized source commitment with the resources that remain after the split.
  * The split commitments with the redistributed resources.



The source commitment, although resized, retains all its other attributes, including its start and end dates, and continues to operate normally. The split commitments retain the same end date and [term extension eligibility window](https://docs.cloud.google.com/compute/docs/committed-use-discounts/extend-commitment-term#term-extension-eligibility-window) as the source commitment.

Because split commitments can be created only after your source commitment is already active, the split commitments might have a custom term duration instead of the preset term duration of 1 or 3 years. However, the split commitments retain the 1- or 3-year commitment plan of the source commitment.

You can create only one new split commitment at a time using REST and the gcloud CLI. You can create multiple new split commitments in a single operation by using the Google Cloud console.

You can't split a commitment that has attached reservations. For more information about commitments with attached reservations, see [Combine reservations with committed use discounts](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments#combining_reservations_with_committed_use_discounts).

### Example of a split commitment

The following table shows commitment properties when you split an existing commitment (`source-commitment`) into two distinct commitments (a resized `source-commitment` and a `split-commitment`) on March 1, 2022:

| **Source commitment  
(before split)** | **Split commitment** | **Source commitment  
(after split)**  
---|---|---|---  
**Name** | source-commitment | split-commitment | source-commitment  
**Type** | N2 | N2 | N2  
**Region** | us-central1 | us-central1 | us-central1  
**Resources** | 

  * vCPUs: 200
  * Memory: 200 GB

| 

  * vCPUs: 50
  * Memory: 100 GB

| 

  * vCPUs: 150
  * Memory: 100 GB

  
**Plan** | 3 years | 3 years | 3 years  
**Term** | 3 years | Custom (10 months) | 3 years  
**Start date *** | January 1, 2020 | March 2, 2022  
(the day after the split) | January 1, 2020  
**End date †** | January 1, 2023 | January 1, 2023 | January 1, 2023  
**Term extension eligibility window open until** | January 1, 2021 | January 1, 2021 | January 1, 2021  
  
*All commitments start at 12 AM US and Canadian Pacific Time (UTC-8 or UTC-7) on the specified start date.  
†All commitments expire at 12 AM US and Canadian Pacific Time (UTC-8 or UTC-7) on the specified end date. 

### Pricing implications

Your commitment fee is the sum of the discounted prices of all your committed resources. Splitting a commitment affects your resource costs in the following ways:

  * **Resized source commitment** : The discounted prices of resources from your resized source commitment remain the same.
  * **Split commitment** : The discounted prices of your split commitment's resources might change on the day that the split commitment becomes active. This new discounted price for each resource remains the same until the end of your new split commitment's term, even if on-demand prices change.



However, if you merge or split either of these commitments again, then the discounted prices might change again.

### Limitations

  * You can't split software license commitments or block storage commitments.
  * You can't split commitments that you purchased through [future reservations for capacity blocks](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type#reserve-capacity-aihc).
  * You can't split [commitments that have attached reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments). Consequently, you can't split commitments that have GPUs, Local SSD disks, or both, because commitments with these resources always have attached reservations.
  * You can't attach any reservations (new or existing) to the split commitments.
  * You can't split commitments that have expired or are canceled.
  * By default, when you split your commitments, the auto-renewal setting is disabled on the split commitments, even if all source commitments were set to renew automatically. If you want your split commitments to renew automatically, then you must manually enable the auto-renewal setting on those commitments. You can do so either [at the time of their creation](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically#create_a_commitment_that_renews_automatically) or [after their creation](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically#enable_auto-renew_on_an_existing_commitment).
  * You can create only one new split commitment at a time using REST or the gcloud CLI. As a result, you can split your source commitment into a maximum of two commitments in a single operation when using these interfaces. To split your source commitment into three or more commitments in a single operation, use the Google Cloud console.
  * In the Google Cloud console, you can specify memory only in increments of 0.25 GB. To specify a custom memory value for your commitment, use gcloud CLI or REST instead.



### Requirements

When you split a source commitment and create one or more split commitments, your source and split commitments must meet the following requirements:

  * The split commitments must have the same project, commitment type, region, and commitment plan as the source commitment. However, you must choose new names for your split commitments.
  * The resource types that you specify for split commitments must match some or all resource types in the source commitment. Also, the combined amount of resources that you specify for split commitments must be a portion of the resources in the source commitment. You must retain a portion of the resources in your source commitment. For example, if your source commitment is for 200 vCPUs and 300 GB memory, then the following resize and redistribution scenarios apply:

    * You can redistribute a portion of the 200 vCPUs and a portion of the 300 GB memory among the split commitments.
    * You can redistribute all of the 200 vCPUs, but you must retain a portion of the memory in your source commitment.
    * You can redistribute all of the 300 GB memory, but you must retain a portion of the vCPUs in your source commitment.
    * You can't redistribute all of the 200 vCPUs and all of the 300 GB memory among your split commitments.
  * The source and split commitments must specify only the following hardware resources: vCPUs, memory, or a combination of both.




Also, to split a source commitment by using the gcloud CLI, update the gcloud CLI to version 423.0.0 or later. If you use an earlier version, then the split operation fails and Compute Engine throws an error. 

### Create split commitments

Create one new split commitment at a time by using the gcloud CLI or the Compute Engine API. Create multiple new split commitments at a time by using the Google Cloud console. Before you split a commitment, review the limitations for splitting.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.commitments.create` on the project or organization.



### Console

  1. In the Google Cloud console, select the project where you want to split a commitment. Then, go to the **Committed use discounts** page.

[Go to Committed use discounts](https://console.cloud.google.com/compute/commitments)

  2. To initiate the split operation for a commitment, do one of the following on the **Hardware commitments** tab of the **Commitment list** page:

     * Select the commitment that you want to split from the list and click **Split**.
     * In the **Name** column, click the name of the commitment that you want to split. On the **Hardware commitment details** page that opens, click **Split**.
  3. On the **Resize** tab of the **Split commitment** page that opens, do the following:

     1. In the **vCPUs** and **Memory** fields, specify the number of vCPUs and memory that you want to retain in your original commitment. The remaining resources are available for redistribution to your split commitment. The source commitment can't be empty after you resize it.
     2. Click **Next**. The **Redistribute** tab opens.
  4. On the **Redistribute** tab of the **Split commitment** page, do the following:

     1. In the **Name** field, specify a name for your split commitment.
     2. In the **vCPUs** and **Memory** fields, specify the number of vCPUs and memory for your split commitment. You can specify memory only in increments of 0.25 GB. To specify a custom memory value for your commitment, use gcloud CLI or REST instead.

If you want to create a single split commitment, then specify all of the resources that you want to redistribute from the source commitment. If you want to create multiple split commitments, then specify only the portion of the redistributed resources that you want for this split commitment.

     3. Optional: To enable auto-renewal on your split commitment, select the **Enable auto renew** checkbox.

     4. Click **Done**.

     5. Optional: To create additional split commitments, click **Add an item** and repeat the preceding steps.

     6. Click **Next**. The **Review** tab opens.

  5. On the **Review** tab of the **Split commitment** page, do the following:

     1. Review and confirm the details of the resized commitment and the split commitments. 
        * To modify the resource allocation from your original commitment, select the **Resize** tab on the left side of the window and repeat step 3.
        * To modify your resource redistribution among your split commitments, select the **Redistribute** tab on the left side of the window and repeat step 4.
     2. Read the **Terms and conditions**.
     3. To finish creating your split commitments and return to the **Commitment list** page, click **Submit**.



###  gcloud 

**Important:** To split a source commitment by using the gcloud CLI, update the gcloud CLI to version 423.0.0 or later. If you use an earlier version, then the split operation fails and Compute Engine throws an error. 

To split an existing commitment into two commitments, use the [gcloud compute commitments create command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments/create) with the `--split-source-commitment` flag.
    
    
    gcloud compute commitments create COMMITMENT_NAME \
        --region=REGION \
        --project=PROJECT_ID \
        --plan=COMMITMENT_PLAN \
        --type=COMMITMENT_TYPE \
        --resources=vcpu=NUMBER_VCPUS,memory=MEMORY \
        --split-source-commitment=SOURCE_COMMITMENT_URL
    

Replace the following:

  * `COMMITMENT_NAME`: the name of your new split commitment.
  * `COMMITMENT_TYPE`: the same commitment type as your source commitment, one of the following: 

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
  * `REGION`: the same region as your source commitment.

  * `PROJECT_ID`: the project ID of the project for which you want to split the source commitment.

  * `COMMITMENT_PLAN`: the commitment plan ('12-month' or '36-month'), which must be the same as your source commitment.

  * `NUMBER_VCPUS`: The number of vCPUs that you want to transfer from your source commitment to create your new split commitment. This number must be an integer that is less than the number of vCPUs in the source commitment.

  * `MEMORY`: the amount of memory, in MB or GB, that you want to transfer from your source commitment to create your new split commitment. This amount must be less than the amount of memory in the source commitment. For example, 10000 MB. If you don't specify a unit, then the default unit is GB.

  * `SOURCE_COMMITMENT_URL`: the URL of the source commitment from which you want to carve out resources.




For example, consider a source commitment (`source-commitment`) in the `us-east1` region with resources specified as three N2 vCPUs and 2048 MB memory. The commitment plan for the source commitment is `12-month`. The following gcloud CLI command splits the commitment into two separate commitments:
    
    
    gcloud compute commitments create split-commitment \
        --plan=12-month \
        --type=general-purpose-n2 \
        --region=us-east1 \
        --project=myproject \
        --resources vcpu=1,memory=1024MB \
        --split-source-commitment=projects/myproject/regions/us-east1/commitments/source-commitment
    

When splitting `source-commitment`, Compute Engine does the following:

  * Takes resources from `source-commitment` and creates a new commitment `split-commitment` with one N2 vCPU and 1024 MB memory.
  * Resizes `source-commitment` to the remaining resources.



###  REST 

To split an existing commitment into two commitments, use the [`regionCommitments.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCommitments/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/commitments
    {
      "name": "COMMITMENT_NAME",
      "plan": "COMMITMENT_PLAN",
      "type": "COMMITMENT_TYPE",
      "region": "REGION",
      "resources": [
        {
          "type": "VCPU",
          "amount": "NUMBER_VCPUS"
        },
        {
          "type": "MEMORY",
          "amount": "MEMORY"
        }
      ],
      "splitSourceCommitment": "SOURCE_COMMITMENT_URL"
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the project for which you want to split the source commitment.
  * `REGION`: the same region as your source commitment.
  * `COMMITMENT_NAME`: the name of your new split commitment.
  * `COMMITMENT_TYPE`: the same commitment type as your source commitment, one of the following: 

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
  * `COMMITMENT_PLAN`: the commitment plan ('TWELVE_MONTH' or 'THIRTY_SIX_MONTH'), which must be the same as your source commitment.

  * `NUMBER_VCPUS`: the number of vCPUs that you want to transfer from your source commitment to create your new split commitment. This number must be an integer that is less than the number of vCPUs in the source commitment.

  * `MEMORY`: the amount of memory, in MB, that you want to transfer from your source commitment to create your new split commitment. This amount must be less than the amount of memory in the source commitment. For example, 1000 MB. If you don't specify a unit, then the default unit is MB.

  * `SOURCE_COMMITMENT_URL`: the URL of the source commitment from which you want to transfer resources.




For example, consider a source commitment (`source-commitment`) in the `us-east1` region with resources specified as three N2 vCPUs and 2048 MB memory. The commitment plan for the source commitment is `TWELVE_MONTH`. The following `POST` request splits the commitment into two separate commitments:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/myproject/regions/us-east1/commitments
    {
      "name": "split-commitment",
      "plan": "TWELVE_MONTH",
      "type": "GENERAL_PURPOSE_N2",
      "region": "us-east1",
      "resources": [
        {
          "type": "VCPU",
          "amount": "1"
        },
        {
          "type": "MEMORY",
          "amount": "1024"
        }
      ],
      "splitSourceCommitment": "projects/myproject/regions/us-east1/commitments/source-commitment"
    }
    

When splitting `source-commitment`, Compute Engine does the following:

  * Takes resources from `source-commitment` and creates a new commitment `split-commitment` with one N2 vCPU and 1024 MB memory.
  * Resizes `source-commitment` to the remaining resources.



## What's next

  * Learn how to [renew resource-based commitments automatically](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically).
  * Learn how to [extend the term of resource-based commitments](https://docs.cloud.google.com/compute/docs/committed-use-discounts/extend-commitment-term).
  * Learn how to [upgrade resource-based commitments](https://docs.cloud.google.com/compute/docs/instances/upgrade-commitment-term).
  * Learn how to [analyze the effectiveness of your CUDs](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
