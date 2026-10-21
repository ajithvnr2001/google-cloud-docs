---
url: https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments/
title: Purchase hardware commitments without attached reservations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T23:39:00.897868+00:00
---

# Purchase hardware commitments without attached reservations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Purchase hardware commitments without attached reservations Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine provides resource-based committed use discounts (CUDs) for your predictable workloads. You can purchase commitments for hardware resources like vCPUs, memory, and specific types of Local SSD disks without attaching any reservations for those resources. 

This document explains how to purchase resource-based commitments without attached reservations by using the Google Cloud console, the gcloud CLI, or REST.

To learn more about commitments with attached reservations, see [Attach reservations to resource-based commitments](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments#attach-reservations-to-resource-cuds).

To purchase commitments for GPUs, Local SSD disks, or both, see [Purchase resource-based commitments with attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments-with-reservations).

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




### Required roles

To get the permission that you need to purchase resource-based commitments, ask your administrator to grant you the [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.commitments.create` permission, which is required to purchase resource-based commitments. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

By default, project owners have permission to purchase resource-based commitments. However, it's possible for owners to create custom roles that include or exclude certain users. To make sure that you have permission to purchase a resource-based commitment, read about [access control](https://docs.cloud.google.com/compute/docs/access).

## Purchase a hardware commitment without attached reservations

Purchase hardware resource-based commitments without attached reservations using the Google Cloud console, the gcloud CLI, or REST.

After you purchase a commitment, your commitment becomes active on the following day at 12 AM US and Canadian Pacific Time (UTC-8, or UTC-7 during daylight saving time). Compute Engine [ maintains a lien on your project](https://docs.cloud.google.com/resource-manager/docs/project-liens) for each region in your project where you purchase a commitment. When you purchase a new commitment for any region in your project, Compute Engine associates the lien for that region with the newly created commitment. 

Between the time of your commitment purchase and its activation time, the status of your commitment remains as `NOT_YET_ACTIVE` (or as `PENDING` on the Google Cloud console). After activation, the status of your commitment changes to `ACTIVE`. For example, suppose that you purchase your commitment on January 20, 2024, at 10:00 PM US and Canadian Pacific Time (UTC-8 or UTC-7). Compute Engine creates your commitment immediately with its status as `NOT_YET_ACTIVE`. Your commitment becomes `ACTIVE` on January 21, 2024, at 12:00 AM US and Canadian Pacific Time (UTC-8 or UTC-7). 

**Important:** After you purchase a commitment, you can't cancel it. If you move the project that is associated with the commitment to a different Cloud Billing account, then the project inherits the attribution and CUD sharing settings that apply to the destination account. For more information, see [Impact of changing a project's Cloud Billing account](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#moving-project-billing-account).

###  Console 

Before you purchase a commitment using the Google Cloud console, select the project that you want to use to purchase the commitment. If [CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects) is enabled for a Cloud Billing account, then you can purchase the commitment using any project from that Cloud Billing account. After you select the project, do the following:

  1. In the Google Cloud console, go to the **Committed use discounts** page. [Go to Committed use discounts](https://console.cloud.google.com/compute/commitments)

  2. Click add_box **Purchase commitment**. The **Purchase a commitment** page appears.

  3. In the **Name** field, enter a name for your commitment.

  4. In the **Region** field, select the region where you want to purchase the commitment.

  5. In the **Commitment type** field, select the machine family series for your commitment. For vCPUs, memory, or both, you can choose from the following commitment types:

     * For A2 machine types, select **Accelerator-optimized A2**
     * For A3 Edge and A3 High machine types, select **Accelerator-optimized A3**
     * For A3 Mega machine types, select **Accelerator-optimized A3 Mega** Note: For A4X Max, A4X, A4, or A3 Ultra machine types, you must purchase your commitments by using the _future reservations in AI Hypercomputer_ consumption option. For more information, see [ Reserve capacity through your account team](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity).
     * For G2 machine types, select **Graphics-optimized G2**
     * For G4 machine types, select **Graphics-optimized G4**
     * For C2 machine types, select **Compute-optimized C2**
     * For C2D machine types, select **Compute-optimized C2D**
     * For H3 machine types, select **Compute-optimized H3**
     * For H4D machine types, select **Compute-optimized H4D**
     * For C3 machine types, select **General-Purpose C3**
     * For C3D machine types, select **General-Purpose C3D** **Caution** : For C3 and C3D commitment types, the machine family that is specified by the commitment type changes depending on the interface: 
       * In the gcloud CLI and REST, the commitment type values use _Compute-optimized_ as the machine family, even though C3 and C3D are part of the general-purpose machine family.
       * In the Google Cloud console, the commitment type values use the correct machine series: _General-Purpose_.
Make sure to select the correct commitment type value that corresponds to the interface that you're using. 
     * For C4 machine types, select **General-Purpose C4**
     * For C4A machine types, select **General-Purpose C4A**
     * For C4D machine types, select **General-Purpose C4D**
     * For C4N machine types, select **Network-optimized C4N**
     * For E2 machine types, select **General-Purpose E2**
     * For N1 machine types, select **General-Purpose N1**
     * For N2 machine types, select **General-Purpose N2**
     * For N2D machine types, select **General-Purpose N2D**
     * For N4 machine types, select **General-Purpose N4**
     * For N4D machine types, select **General-Purpose N4D**
     * For N4A machine types, select **General-Purpose N4A**
     * For Tau T2D machine types, select **General-Purpose T2D**
     * For M1 or M2 machine types, select **Memory-optimized M1/M2**
     * For M3 machine types, select **Memory-optimized M3**
     * For the M4 machine type with 6 TB of memory, select **Memory-optimized M4 6TB**
     * For other M4 machine types, select **Memory-optimized M4**
     * For the M4N machine type with 6 TB of memory, select **Memory-optimized M4N 6TB**
     * For other M4N machine types, select **Memory-optimized M4N**
     * For the X4 machine type with 6 TB of memory, select **Memory-optimized X4 480 6T**
     * For the X4 machine type with 8 TB of memory, select **Memory-optimized X4 480 8T**
     * For the X4 machine type with 12 TB of memory, select **Memory-optimized X4 960 12T**
     * For the X4 machine type with 16 TB of memory, select **Memory-optimized X4 960 16T**
     * For the X4 machine type with 24 TB of memory, select **Memory-optimized X4 1440 24T**
     * For the X4 machine type with 32 TB of memory, select **Memory-optimized X4 1920 32T**
     * For Z3 machine types, select **Storage-optimized Z3**
     * For Z4D machine types, select **Storage-optimized Z4D**
     * For Z4M machine types, select **Storage-optimized Z4M**
  6. In the **Commitment details** section, do the following:

     1. To specify vCPUs for your commitment, in the **Cores** field, enter the number of vCPUs.

     2. To specify memory for your commitment, in the **Memory** field, enter the amount of memory in GB.

You can specify memory only in increments of 0.25 GB. To specify a custom memory value for your commitment, use gcloud CLI or REST instead.

  7. To specify Local SSD disks for your commitment, expand the **GPUs and local SSDs** section. Then, in the **Local SSDs** field, specify the number of disks. Without attached reservations, you can specify Local SSD disks only for these commitment types:

     * **General-purpose C4, C4A, or C4D**
     * **Accelerator-optimized G4**
     * **Storage-optimized Z3**
     * **Compute-optimized H4D**
  8. In the **Term** section, do the following:

     1. To specify the _[plan](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#commitment-plan)_ for your commitment, select either **1 year** or **3 years**. The plan determines the CUD rate and preset term duration of your commitment.

     2. Review the **Start date** field, which shows the date and time when your commitment becomes active. This field is automatically set to 12 AM US and Canadian Pacific Time on the day after your current date.

     3. Optional. To extend your commitment's [term](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#commitment-term) beyond the preset term duration that is defined by your commitment plan, in the **End date** field, specify a custom end date for your commitment. For more information, see [Extend commitment terms](https://docs.cloud.google.com/compute/docs/committed-use-discounts/extend-commitment-term).

     4. Optional. If you want your commitment to [automatically renew](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically) at the end of its term, then select the **Auto-renew commitment** checkbox.

  9. In the **Summary** pane, review your commitment details and any potential quota limitations.

  10. To finish purchasing your commitment, do the following:

     1. Navigate to the bottom of the page.

     2. Review the **Disclosures** section, which contains information about fees, discount eligibility, and terms and conditions.

     3. To confirm your acceptance of the [commitment price](https://cloud.google.com/products/compute/pricing) and [service specific terms](https://cloud.google.com/terms/service-terms), select the checkbox.

     4. Click **Purchase**.




###  gcloud 

Using the gcloud CLI, run the [`gcloud compute commitments create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments/create):
    
    
    gcloud compute commitments create COMMITMENT_NAME \
        --region REGION \
        --project PROJECT_ID \
        --resources vcpu=NUMBER_VCPUS,memory=MEMORY,local-ssd=LOCAL_SSD \
        --plan PLAN \
        --type COMMITMENT_TYPE \
        --custom-end-time=CUSTOM_END_DATE \
        --auto-renew
    

Replace the following:

  * `COMMITMENT_NAME`: the name that you want to identify this commitment with.
  * `REGION`: the region that this commitment applies to. Each region has different commitment prices. For current prices, see the [price sheet](https://cloud.google.com/compute/vm-instance-pricing).
  * `PROJECT_ID`: the project ID of the project for which you want to create the commitment.
  * `NUMBER_VCPUS`: the number of vCPUs that you want to purchase commitments for. The number of vCPUs must be an integer of 0 or more and can be even or odd.
  * `MEMORY`: the amount, in MB or GB, of memory that you want to purchase commitments for. For example, `1000MB`. For the gcloud CLI, you can specify memory in MB or GB. If you don't specify a unit, then Compute Engine uses GB as the default unit. However, note that when you use REST, Compute Engine uses MB as the default unit.
  * `LOCAL_SSD`: Optional. The amount of Local SSD storage, which must be specified in GB; for example, `375GB`. Purchase of commitments for Local SSD disks without attached reservations is supported only for C4, C4A, C4D, G4, H4D, or Z3 commitment types.
  * `PLAN`: the commitment plan, which determines your CUD rate and preset term. Specify `12-month` or `36-month`.
  * `COMMITMENT_TYPE`: one of:

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
  * `CUSTOM_END_DATE`: Optional. A custom end date for your term, which must be formatted as `YYYY-MM-DD`.

  * `--auto-renew`: Optional. Automatically renews your commitment at the end of its term.




#### Examples

The following examples purchase commitments in the `myproject` project and the `us-central1` region.

**Example 1: Purchase a commitment for general-purpose N1 resources**

To purchase a 1-year commitment for general-purpose N1 resources with 5 vCPUs and 32.5 GB of memory (equivalent to 33280 MB), run the following command. For the gcloud CLI, you can specify memory in MB or GB. If you don't specify a unit, then Compute Engine uses GB as the default unit. However, note that when you use REST, Compute Engine uses MB as the default unit:
    
    
        gcloud compute commitments create example-commitment --region us-central1 \
            --resources vcpu=5,memory=33280MB --plan 12-month \
            --type general-purpose --project=myproject
    

**Example 2: Purchase a commitment for compute-optimized C2 resources**

To purchase a 1-year commitment for compute-optimized C2 resources with 16 vCPUs and 64 GB of memory, run the following command. For the gcloud CLI, you can specify memory in MB or GB. If you don't specify a unit, then Compute Engine uses GB as the default unit. However, note that when you use REST, Compute Engine uses MB as the default unit:
    
    
        gcloud compute commitments create example-compute-optimized-commitment \
            --region us-central1 --resources vcpu=16,memory=64GB --plan 12-month \
            --type compute-optimized --project=myproject
    

**Example 3: Purchase a commitment for memory-optimized M1 or M2 resources**

To purchase a 1-year commitment for memory-optimized M1 or M2 resources with 96 vCPUs and 1,433.6 GB of memory, run the following command. For the gcloud CLI, you can specify memory in MB or GB. If you don't specify a unit, then Compute Engine uses GB as the default unit. However, note that when you use REST, Compute Engine uses MB as the default unit:
    
    
        gcloud compute commitments create example-memory-optimized-commitment \
            --region us-central1 --resources vcpu=96,memory=1433.6GB \
            --plan 12-month --type memory-optimized \
            --project=myproject
    

**Example 4: Purchase a commitment for general-purpose C4 resources with a Local SSD disk**

To purchase a 1-year commitment for Local SSD disks that don't require attached reservations (supported only for C4, C4A, C4D, G4, H4D, or Z3 commitment types), include `local-ssd` in the `--resources` flag. Each Local SSD disk is 375 GB. For example, to purchase a 1-year commitment for general-purpose C4 resources with 8 vCPUs, 32 GB of memory, and 1 Local SSD disk (375 GB), run the following command. The Local SSD storage value must be specified in GB (for example, `375GB`). For the gcloud CLI, you can specify memory in MB or GB. If you don't specify a unit, then Compute Engine uses GB as the default unit. However, note that when you use REST, Compute Engine uses MB as the default unit for memory.
    
    
        gcloud compute commitments create example-local-ssd-commitment \
            --region us-central1 --resources vcpu=8,memory=32GB,local-ssd=375GB \
            --plan 12-month --type general-purpose-c4 --project=myproject
    

###  REST 

In the API, make a `POST` request to the [`regionCommitments.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCommitments/insert), with a request body that contains information about the commitment.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/commitments?requestId=OPTIONAL_UNIQUE_ID
    
    {
        "name": "COMMITMENT_NAME",
        "plan": "PLAN",
        "type": "COMMITMENT_TYPE",
        "resources": [
            {
                "type": "VCPU",
                "amount": "COMMITTED_VCPUS"
            },
            {
                "type": "MEMORY",
                "amount": "COMMITTED_MEMORY"
            },
            {
                "type": "LOCAL_SSD",
                "amount": "COMMITTED_LOCAL_SSD"
            }
        ],
        "customEndTimestamp": "CUSTOM_END_DATETEND_TIMEZ",
        "autoRenew": AUTO_RENEW_BOOLEAN
    }

**Note:** [`requestId`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCommitments/insert) is an optional query parameter, but we recommend providing it to help prevent unintended duplicate requests.

Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to purchase the commitment.
  * `REGION`: the region where you want to purchase the commitment.
  * `OPTIONAL_UNIQUE_ID`: Optional. A unique request ID to help prevent unintended duplicate requests.
  * `COMMITMENT_NAME`: the name for your commitment.
  * `PLAN`: the commitment plan, either `TWELVE_MONTH` or `THIRTY_SIX_MONTH`.
  * `COMMITMENT_TYPE`: the commitment type, one of the following:

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
  * `COMMITTED_VCPUS`: the number of vCPUs that you want in your commitment.

  * `COMMITTED_MEMORY`: the amount of memory, in MB, that you want in your commitment. For REST, Compute Engine uses MB as the default unit. However, note that when you use gcloud CLI, Compute Engine uses GB as the default unit.

  * `COMMITTED_LOCAL_SSD`: Optional. The amount of Local SSD storage, which must be specified in GB; for example, `375GB`. Purchase of commitments for Local SSD disks without attached reservations is supported only for C4, C4A, C4D, G4, H4D, or Z3 commitment types.

  * `CUSTOM_END_DATE`: Optional. A custom end date for your commitment, formatted as `YYYY-MM-DD`.

  * `END_TIME`: 12 AM US and Canadian Pacific Time (UTC-8 or UTC-7). Specify `07:00:00` during daylight saving time, or `08:00:00` during other times.

  * `AUTO_RENEW_BOOLEAN`: Optional. Set to `true` to automatically renew your commitment at the end of its term.




#### Examples

The following examples purchase commitments in the `myproject` project and the `us-central1` region.

**Example 1: Purchase a commitment for general-purpose N1 resources**

To purchase a 1-year commitment for general-purpose N1 resources with 5 vCPUs and 18.75 GB of memory (equivalent to 19200 MB), make the following POST request. For REST, you must specify memory in MB. However, note that when you use gcloud CLI, Compute Engine uses GB as the default unit.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/myproject/regions/us-central1/commitments
    
    {
        "name": "example-commitment",
        "plan": "TWELVE_MONTH",
        "type": "GENERAL_PURPOSE",
        "resources": [
            {
                "amount": "5",
                "type": "VCPU"
            },
            {
                "amount": "19200",
                "type": "MEMORY"
            }
        ]
    }

**Example 2: Purchase a commitment for memory-optimized M1 or M2 resources**

To purchase a 1-year commitment for memory-optimized M1 or M2 resources with 96 vCPUs and 1,433.6 GB of memory (equivalent to 1468006 MB), make the following POST request. For REST, you must specify memory in MB. However, note that when you use gcloud CLI, Compute Engine uses GB as the default unit.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/myproject/regions/us-central1/commitments
    
    {
        "name": "example-memory-optimized-commitment",
        "plan": "TWELVE_MONTH",
        "type": "MEMORY_OPTIMIZED",
        "resources": [
            {
                "amount": "96",
                "type": "VCPU"
            },
            {
                "amount": "1468006",
                "type": "MEMORY"
            }
        ]
    }

**Example 3: Purchase a commitment for compute-optimized C2 resources**

To purchase a 1-year commitment for compute-optimized C2 resources with 16 vCPUs and 64 GB of memory (equivalent to 65536 MB), make the following POST request. For REST, you must specify memory in MB. However, note that when you use gcloud CLI, Compute Engine uses GB as the default unit.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/myproject/regions/us-central1/commitments
    
    {
        "name": "example-compute-optimized-commitment",
        "plan": "TWELVE_MONTH",
        "type": "COMPUTE_OPTIMIZED",
        "resources": [
            {
                "amount": "16",
                "type": "VCPU"
            },
            {
                "amount": "65536",
                "type": "MEMORY"
            }
        ]
    }

**Example 4: Purchase a commitment for general-purpose C4 resources with a Local SSD disk**

To purchase a 1-year commitment for general-purpose C4 resources and a Local SSD disk without any attached reservations (supported only for C4, C4A, C4D, G4, H4D, or Z3 commitment types) with 8 vCPUs, 32 GB of memory, and 1 Local SSD disk (375 GB), make the following POST request. Note that the Local SSD storage value must be specified in GB. For memory, you must specify the value in MB. However, note that when you use gcloud CLI, Compute Engine uses GB as the default unit for memory.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/myproject/regions/us-central1/commitments
    
    {
        "name": "example-local-ssd-commitment",
        "plan": "TWELVE_MONTH",
        "type": "GENERAL_PURPOSE_C4",
        "resources": [
            {
                "amount": "8",
                "type": "VCPU"
            },
            {
                "amount": "32768",
                "type": "MEMORY"
            },
            {
                "amount": "375",
                "type": "LOCAL_SSD"
            }
        ]
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
