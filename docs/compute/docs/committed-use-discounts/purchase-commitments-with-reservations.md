---
url: https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments-with-reservations/
title: Purchase hardware commitments with attached reservations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T23:39:02.757418+00:00
---

# Purchase hardware commitments with attached reservations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments-with-reservations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Purchase hardware commitments with attached reservations Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine provides resource-based committed use discounts (CUDs) for your predictable workloads. When you purchase commitments for any GPUs or most Local SSD disks, you must reserve those resources and attach the reservations to your commitment. 

This document explains how to purchase resource-based commitments with attached reservations by using the Google Cloud console, the gcloud CLI, or REST.

To learn more about how attached reservations work, see [Attach reservations to resource-based commitments](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments#attach-reservations-to-resource-cuds).

To purchase commitments for vCPUs and memory without attached reservations, see [Purchase resource-based commitments without attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments).

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

To get the permissions that you need to purchase commitments and create reservations, ask your administrator to grant you the [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to purchase commitments and create reservations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to purchase commitments and create reservations:

  * `compute.commitments.create`
  * `compute.reservations.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

By default, project owners have permission to purchase resource-based commitments. However, it's possible for owners to create custom roles that include or exclude certain users. To make sure that you have permission to purchase a resource-based commitment, read about [access control](https://docs.cloud.google.com/compute/docs/access).

## Purchase a hardware resource-based commitment with attached reservations

When you purchase a new commitment, you can attach reservations to your commitment in either of the following ways: 

  * Use existing reservations that match the commitment properties
  * Create new matching reservations while purchasing your commitment



After you purchase a commitment, your commitment becomes active on the following day at 12 AM US and Canadian Pacific Time (UTC-8, or UTC-7 during daylight saving time). Compute Engine [ maintains a lien on your project](https://docs.cloud.google.com/resource-manager/docs/project-liens) for each region in your project where you purchase a commitment. When you purchase a new commitment for any region in your project, Compute Engine associates the lien for that region with the newly created commitment. 

Between the time of your commitment purchase and its activation time, the status of your commitment remains as `NOT_YET_ACTIVE` (or as `PENDING` on the Google Cloud console). After activation, the status of your commitment changes to `ACTIVE`. For example, suppose that you purchase your commitment on January 20, 2024, at 10:00 PM US and Canadian Pacific Time (UTC-8 or UTC-7). Compute Engine creates your commitment immediately with its status as `NOT_YET_ACTIVE`. Your commitment becomes `ACTIVE` on January 21, 2024, at 12:00 AM US and Canadian Pacific Time (UTC-8 or UTC-7). 

**Important:** After you purchase a commitment, you can't cancel it. If you move the project that is associated with the commitment to a different Cloud Billing account, then the project inherits the attribution and CUD sharing settings that apply to the destination account. For more information, see [Impact of changing a project's Cloud Billing account](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#moving-project-billing-account).

### Requirements

Before you purchase a commitment with attached reservations, review these requirements and make sure that your commitment and reservations meet the following criteria:

  * You must purchase the commitment and create the attached reservations in the same project and region.
  * You must purchase the commitment and create the attached reservations for resources from the same machine family series.
  * If your commitment specifies any resource types that require attached reservations, then you must disable the [auto-delete option](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#auto-delete) on the attached reservations. Learn more about the [resource types that require attached reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments#committed_resources_that_require_attached_reservations).
  * If your commitment has GPUs, then the GPU type specified in the reservation and the commitment must match.
  * For GPUs and most Local SSD disks, the number of reserved resources of each resource type must exactly match with the number of committed resources for that resource type. However, this requirement isn't applicable if you specify any local Titanium SSD disks in your commitment for use with C4, C4A, C4D, C4N, G4, H4D, or Z3 machine types.

For example, if you want to purchase a commitment for 4 V100 GPUs and 2 Local SSD disks, then your commitment's attached reservations must specify a total of 4 V100 GPUs and 2 Local SSDs. The amount of vCPU and memory that you reserve can be more or less than what you commit to. However, if you specify 4 C4A vCPUs and 2 local Titanium SSD disks in your commitment, then you don't have to attach any reservations to the commitment.

  * For GPUs, purchase commitments for the specific GPU types that you intend to use. For example, you can purchase commitments for either NVIDIA A100s or NVIDIA V100s, but you can't use a commitment that was purchased for NVIDIA A100 GPUs to cover NVIDIA V100 GPUs.

  * If your attached reservation is a shared reservation and you want to receive the applicable CUDs when you consume that reservation outside your commitment's project, then you must do both the following:

    * Share your reservations only between projects that belong to the same Cloud Billing account as the commitment.
    * Ensure that [CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#turning-on-committed-use-discount-sharing) is enabled for that Cloud Billing account.



### Attach existing reservations

You can attach existing reservations while purchasing your commitment by using the Google Cloud console, the Google Cloud CLI, or REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * To purchase a commitment: `compute.commitments.create` on the project
  * To create reservations: `compute.reservations.create` on the project



###  Console 

Before you purchase a commitment using the Google Cloud console, select the project that you want to use to purchase the commitment. If [CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects) is enabled for a Cloud Billing account, then you can purchase the commitment using any project from that Cloud Billing account. After you select the project, do the following:

  1. In the Google Cloud console, go to the **Committed use discounts** page. [Go to Committed use discounts](https://console.cloud.google.com/compute/commitments)

  2. Click add_box **Purchase commitment**. The **Purchase a commitment** page appears.

  3. In the **Name** field, enter a name for your commitment.

  4. In the **Region** field, select the region where you want to purchase the commitment.

  5. In the **Commitment type** field, select the machine family series for your commitment. The following [commitment types](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#commitment-types-for-hardware-commitments) provide options for GPUs, Local SSD disks, or both:

     * For A2 machine types, select **Accelerator-optimized A2**
     * For A3 Edge and A3 High machine types, select **Accelerator-optimized A3**
     * For A3 Mega machine types, select **Accelerator-optimized A3 Mega** Note: For A4X Max, A4X, A4, or A3 Ultra machine types, you must purchase your commitments by using the _future reservations in AI Hypercomputer_ consumption option. For more information, see [ Reserve capacity through your account team](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity).
     * For G2 machine types, select **Graphics-optimized G2**
     * For G4 machine types, select **Graphics-optimized G4**
     * For C2 machine types, select **Compute-optimized C2**
     * For C2D machine types, select **Compute-optimized C2D**
     * For C3 machine types, select **General-Purpose C3**
     * For C3D machine types, select **General-Purpose C3D** **Caution** : For C3 and C3D commitment types, the machine family that is specified by the commitment type changes depending on the interface: 
       * In the gcloud CLI and REST, the commitment type values use _Compute-optimized_ as the machine family, even though C3 and C3D are part of the general-purpose machine family.
       * In the Google Cloud console, the commitment type values use the correct machine series: _General-Purpose_.
Make sure to select the correct commitment type value that corresponds to the interface that you're using. 
     * For C4 machine types, select **General-Purpose C4**
     * For C4A machine types, select **General-Purpose C4A**
     * For C4D machine types, select **General-Purpose C4D**
     * For C4N machine types, select **Network-optimized C4N**
     * For N1 machine types, select **General-Purpose N1**
     * For N2 machine types, select **General-Purpose N2**
     * For N2D machine types, select **General-Purpose N2D**
     * For M1 machine types, select **Memory-optimized M1/M2**
     * For M3 machine types, select **Memory-optimized M3**
     * For Z3 machine types, select **Storage-optimized Z3**
     * For Z4D machine types, select **Storage-optimized Z4D**
     * For Z4M machine types, select **Storage-optimized Z4M**
  6. To attach one or more existing reservations to the commitment, do the following:

     1. Select the **Attach a new or existing reservation** checkbox.

     2. Click **Attach an existing reservation**. The **Attach existing reservations** pane appears and displays reservations from your project. This list is filtered to match your specified region and commitment type.

     3. In the **Attach existing reservations** pane, select the checkbox for each reservation that you want to attach.

     4. Review the resource summary for your selected reservations and then click **Attach**.

_After you attach your reservations, Compute Engine automatically populates the fields in the**Commitment details** section to match the numbers and types of resources from your attached reservations. If you manually entered values for any resources in the **Commitment details** section before attaching reservations, then your values are overwritten with values from the reservations._

  7. In the **Commitment details** section, do the following:

     1. In the **Cores** field, verify the pre-filled value. Optionally, you can specify a different number of vCPUs.

     2. In the **Memory** field, verify the pre-filled amount of memory in GB. Optionally, you can specify a different amount. You can specify memory only in increments of 0.25 GB. To specify a custom memory value for your commitment, use gcloud CLI or REST instead.

     3. Expand the **GPUs and local SSDs** section and verify that the types and numbers match between the commitment and attached reservations, as follows:

        1. In the **GPU type** field, verify the pre-filled GPU type.

        2. In the **Number of GPUs** field, verify the pre-filled number of GPUs.

        3. In the **Local SSDs** field, verify the pre-filled number of disks.

If you manually specify different values from the attached reservations for any of these fields, then your commitment purchase doesn't go through. For all GPUs and most Local SSD disks, the total numbers and types must match between your commitment and attached reservations.

**Note:** This requirement doesn't apply to local Titanium SSD disks for use with C4, C4A, C4D, C4N, H4D, Z3, or G4 machine series. For these disks only, you don't need to attach any reservations and you can choose to specify different numbers between your commitment and attached reservations.
  8. In the **Term** section, do the following:

     1. To specify the _[plan](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#commitment-plan)_ for your commitment, select either **1 year** or **3 years**. The plan determines the CUD rate and preset term duration of your commitment.

     2. Review the **Start date** field, which shows the date and time when your commitment becomes active. This field is automatically set to 12 AM US and Canadian Pacific Time on the day after your current date.

     3. Optional. To extend your commitment's [term](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#commitment-term) beyond the preset term duration that is defined by your commitment plan, in the **End date** field, specify a custom end date for your commitment. For more information, see [Extend commitment terms](https://docs.cloud.google.com/compute/docs/committed-use-discounts/extend-commitment-term).

     4. Optional. If you want your commitment to [automatically renew](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically) at the end of its term, then select the **Auto-renew commitment** checkbox.

  9. In the **Summary** pane, review your commitment details and any potential quota limitations.

  10. To finish purchasing your commitment, do the following:

     1. Navigate to the bottom of the page.

     2. Review the **Disclosures** section that contains information about fees, discount eligibility, and terms and conditions.

     3. To confirm your acceptance of the [commitment price](https://cloud.google.com/products/compute/pricing) and [service specific terms](https://cloud.google.com/terms/service-terms), select the checkbox.

     4. Click **Purchase**.




###  gcloud 

To purchase a commitment by attaching existing reservations, run the [`gcloud compute commitments create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments/create). In your command, include the `--existing-reservation` flag to specify an existing reservation that you want to attach to your commitment. Include a new instance of this flag for every existing reservation that you want to attach. You can attach any number of existing reservations to your commitment.

For example, to purchase a commitment by attaching two reservations to it, run the following command:
    
    
    gcloud compute commitments create COMMITMENT_NAME \
        --region=REGION \
        --project=PROJECT_ID \
        --resources=vcpu=COMMITTED_VCPUS,memory=COMMITTED_MEMORY,local-ssd=COMMITTED_LOCAL_SSD \
        --resources-accelerator=count=COMMITTED_ACCELERATOR_COUNT,type=COMMITTED_ACCELERATOR_TYPE \
        --plan=PLAN \
        --type=COMMITMENT_TYPE \
        --custom-end-time=CUSTOM_END_DATE \
        --existing-reservation=name='RESERVATION_NAME_1',zone='RESERVATION_ZONE_1' \
        --existing-reservation=name='RESERVATION_NAME_2',zone='RESERVATION_ZONE_2'
    

Replace the following:

  * `COMMITMENT_NAME`: the name of the commitment.
  * `REGION`: the region where the commitment is located.
  * `PROJECT_ID`: the ID of the project where you want to purchase the commitment with the attached reservations.
  * `PLAN`: the commitment plan, which determines your CUD rate and the preset term duration. Specify `12-month` or `36-month`.
  * `CUSTOM_END_DATE`: Optional. A custom end date for your term, which must be formatted as `YYYY-MM-DD`. For example, to specify a custom end date of April 20, 2024, format it as `2024-04-20`.
  * `COMMITMENT_TYPE`: the commitment type. The following commitment types provide options for GPUs, Local SSD disks, or both:

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
    * For N1 machine types, use `general-purpose`
    * For C4 machine types, use `general-purpose-c4`
    * For C4A machine types, use `general-purpose-c4a`
    * For C4D machine types, use `general-purpose-c4d`
    * For C4N machine types, use `network-optimized-c4n`
    * For N2 machine types, use `general-purpose-n2`
    * For N2D machine types, use `general-purpose-n2d`
    * For M1 machine types, use `memory-optimized`
    * For M3 machine types, use `memory-optimized-m3`
    * For Z3 machine types, use `storage-optimized-z3`
    * For Z4D machine types, use `storage-optimized-z4d`
    * For Z4M machine types, use `storage-optimized-z4m`
  * `COMMITTED_VCPUS`: the number of vCPUs that you want in your commitment. The number must be a positive integer.

  * `COMMITTED_MEMORY`: the amount, in MB or GB, of memory that you want in your commitment. For example, `10240MB` or `10GB`. For the gcloud CLI, you can specify memory in MB or GB. If you don't specify a unit, then Compute Engine uses GB as the default unit. However, note that when you use REST, Compute Engine uses MB as the default unit.

  * `COMMITTED_LOCAL_SSD`: the amount, in GB, of Local SSD space that you want in your commitment.

  * `COMMITTED_ACCELERATOR_COUNT`: the number of GPUs that you want in your commitment.

  * `COMMITTED_ACCELERATOR_TYPE`: the GPU type that you want in your commitment.

  * `RESERVATION_NAME_1` and `RESERVATION_NAME_2`: The names of the existing reservations that you want to attach to the commitment.

  * `RESERVATION_ZONE_1` and `RESERVATION_ZONE_2`: The zones of the existing reservations that you want to attach to the commitment.




**Example: Purchase a commitment by attaching existing reservations**

Suppose that you have two reservations `res-01` and `res-02` in the `us-central1-a` and `us-central1-b` zones of the project `myproject`. Suppose that these reservations hold a combined capacity for 4 NVIDIA T4 GPUs and 4 Local SSD disks. To purchase a new commitment in the `us-central1` region of this project for these GPUs and Local SSD disks, and use these existing reservations as attached reservations, run the following command. The commitment specifies 96 vCPUs, 624 GB of memory, 4 NVIDIA T4 GPUs, and 1,500 GB of Local SSD storage (equivalent to 4 Local SSD disks). The Local SSD storage value must be specified in GB (for example, `375GB`). For the gcloud CLI, you can specify memory in MB or GB. If you don't specify a unit, then Compute Engine uses GB as the default unit. However, note that when you use REST, Compute Engine uses MB as the default unit.
    
    
    gcloud compute commitments create commitment-01 \
        --region=us-central1 \
        --project=myproject \
        --resources=vcpu=96,memory=624GB,local-ssd=1500 \
        --resources-accelerator=type=nvidia-tesla-t4,count=4 \
        --plan 12-month \
        _--existing-reservation=name=res-01,zone=us-central1-a \
        --existing-reservation=name=res-02,zone=us-central1-b_
    

###  REST 

To purchase a commitment by attaching existing reservations, make a `POST` request to the [`regionCommitments.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCommitments/insert). In your request, include the `existingReservations` field to specify a comma-separated list of all the existing reservations that you want to attach to your commitment. You can attach any number of existing reservations to your commitment.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/commitments
    
    {
      "name": "COMMITMENT_NAME",
      "plan": "PLAN",
      "type": "COMMITMENT_TYPE",
      "resources":
      [
        {
          "amount": "COMMITTED_VCPUS",
          "type": "VCPU"
        },
        {
          "amount": "COMMITTED_MEMORY",
          "type": "MEMORY"
        },
        {
          "acceleratorType": "COMMITTED_ACCELERATOR_TYPE",
          "amount": "COMMITTED_ACCELERATOR_COUNT",
          "type": "ACCELERATOR"
        },
        {
          "amount": "COMMITTED_LOCAL_SSD",
          "type": "LOCAL_SSD"
        }
      ],
      "customEndTimestamp": "CUSTOM_END_DATETEND_TIMEZ",
      "existingReservations": "RESERVATION_URLS"
    }
    

Replace the following:

  * `COMMITMENT_NAME`: the name of the commitment.
  * `REGION`: the region where the commitment is located.
  * `PROJECT_ID`: the ID of the project where you want to purchase the commitment with the attached reservations.
  * `PLAN`: the commitment plan, which determines your CUD rate and the preset term duration. Specify `TWELVE_MONTH` or `THIRTY_SIX_MONTH`.
  * `COMMITMENT_TYPE`: the commitment type. The following commitment types provide options for GPUs, Local SSD disks, or both: 

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
    * For N1 machine types, use `GENERAL_PURPOSE`
    * For C4 machine types, use `GENERAL_PURPOSE_C4`
    * For C4A machine types, use `GENERAL_PURPOSE_C4A`
    * For C4D machine types, use `GENERAL_PURPOSE_C4D`
    * For C4N machine types, use `NETWORK_OPTIMIZED_C4N`
    * For N2 machine types, use `GENERAL_PURPOSE_N2`
    * For N2D machine types, use `GENERAL_PURPOSE_N2D`
    * For M1 machine types, use `MEMORY_OPTIMIZED`
    * For M3 machine types, use `MEMORY_OPTIMIZED_M3`
    * For Z3 machine types, use `STORAGE_OPTIMIZED_Z3`
    * For Z4D machine types, use `STORAGE_OPTIMIZED_Z4D`
    * For Z4M machine types, use `STORAGE_OPTIMIZED_Z4M`
  * `COMMITTED_VCPUS`: the number of vCPUs that you want in your commitment. The number must be a positive integer.

  * `COMMITTED_MEMORY`: the amount of memory that you want in your commitment. For REST, Compute Engine uses MB as the default unit. However, note that when you use gcloud CLI, Compute Engine uses GB as the default unit.

  * `COMMITTED_LOCAL_SSD`: the amount, in GB, of Local SSD storage that you want in your commitment.

  * `COMMITTED_ACCELERATOR_COUNT`: the number of GPUs that you want in your commitment.

  * `COMMITTED_ACCELERATOR_TYPE`: the GPU type that you want in your commitment.

  * `CUSTOM_END_DATE`: Optional. A custom end date for your term, which must be formatted as `YYYY-MM-DD`. For example, to specify a custom end date of April 20, 2024, format it as `2024-04-20`.

  * `END_TIME`: 12 AM US and Canadian Pacific Time (UTC-8 or UTC-7), as an offset of [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). Specify this value only if you specified a custom end date for your commitment. Specify one of the following values:

    * During daylight saving time: `07:00:00`
    * During other times: `08:00:00`
  * `RESERVATION_URLS`: a comma-separated list of URLs of the existing reservations that you want to attach to the commitment. For example, to attach two reservations, `res-1` and `res-2`, specify the following: 
        
        "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/reservations/example-res-1",
        "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-c/reservations/example-res-2"
        




**Example: Purchase a commitment by attaching existing reservations**

Suppose that you have two reservations `res-01` and `res-02` in the `us-central1-a` and `us-central1-b` zones of the project `myproject`. Suppose that these reservations hold a combined capacity for 4 NVIDIA T4 GPUs and 4 Local SSD disks. To purchase a new commitment in the `us-central1` region of this project for these GPUs and Local SSD disks and to use these existing reservations as attached reservations, make the following `POST` request. The commitment specifies 96 vCPUs, 624 GB of memory, 4 NVIDIA T4 GPUs, and 1,500 GB of Local SSD storage. Note that the Local SSD storage value must be specified in GB. For memory, you must specify the value in MB. However, note that when you use gcloud CLI, Compute Engine uses GB as the default unit for memory.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/my-project/regions/us-central1/commitments
    
    {
      "name": "commitment-01",
      "plan": "TWELVE_MONTH",
      "type": "GENERAL_PURPOSE",
      "resources":
      [
        {
          "amount": "96",
          "type": "VCPU"
        },
        {
          "amount": "638976",
          "type": "MEMORY"
        },
        {
          "acceleratorType": "nvidia-tesla-t4",
          "amount": "4",
          "type": "ACCELERATOR"
        },
        {
          "amount": "1500",
          "type": "LOCAL_SSD"
        }
      ],_"existingReservations":
      [
        "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/reservations/res-01",
        "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-b/reservations/res-02"
      ]_
    }
    

### Create new reservations to attach

You can create your attached reservations while purchasing your commitment by using the Google Cloud console, the gcloud CLI, or REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * To purchase a commitment: `compute.commitments.create` on the project
  * To create reservations: `compute.reservations.create` on the project



###  Console 

Before you purchase a commitment using the Google Cloud console, select the project that you want to use to purchase the commitment. If [CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects) is enabled for a Cloud Billing account, then you can purchase the commitment using any project from that Cloud Billing account. After you select the project, do the following:

  1. In the Google Cloud console, go to the **Committed use discounts** page. [Go to Committed use discounts](https://console.cloud.google.com/compute/commitments)

  2. Click add_box **Purchase commitment**. The **Purchase a commitment** page appears.

  3. In the **Name** field, enter a name for your commitment.

  4. In the **Region** field, select the region where you want to purchase the commitment.

  5. In the **Commitment type** field, select the machine family series for your commitment. The following [commitment types](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#commitment-types-for-hardware-commitments) provide options for GPUs, Local SSD disks, or both:

     * For A2 machine types, select **Accelerator-optimized A2**
     * For A3 Edge and A3 High machine types, select **Accelerator-optimized A3**
     * For A3 Mega machine types, select **Accelerator-optimized A3 Mega** Note: For A4X Max, A4X, A4, or A3 Ultra machine types, you must purchase your commitments by using the _future reservations in AI Hypercomputer_ consumption option. For more information, see [ Reserve capacity through your account team](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity).
     * For G2 machine types, select **Graphics-optimized G2**
     * For G4 machine types, select **Graphics-optimized G4**
     * For C2 machine types, select **Compute-optimized C2**
     * For C2D machine types, select **Compute-optimized C2D**
     * For C3 machine types, select **General-Purpose C3**
     * For C3D machine types, select **General-Purpose C3D** **Caution** : For C3 and C3D commitment types, the machine family that is specified by the commitment type changes depending on the interface: 
       * In the gcloud CLI and REST, the commitment type values use _Compute-optimized_ as the machine family, even though C3 and C3D are part of the general-purpose machine family.
       * In the Google Cloud console, the commitment type values use the correct machine series: _General-Purpose_.
Make sure to select the correct commitment type value that corresponds to the interface that you're using. 
     * For C4 machine types, select **General-Purpose C4**
     * For C4A machine types, select **General-Purpose C4A**
     * For C4D machine types, select **General-Purpose C4D**
     * For C4N machine types, select **Network-optimized C4N**
     * For N1 machine types, select **General-Purpose N1**
     * For N2 machine types, select **General-Purpose N2**
     * For N2D machine types, select **General-Purpose N2D**
     * For M1 machine types, select **Memory-optimized M1/M2**
     * For M3 machine types, select **Memory-optimized M3**
     * For Z3 machine types, select **Storage-optimized Z3**
     * For Z4D machine types, select **Storage-optimized Z4D**
     * For Z4M machine types, select **Storage-optimized Z4M**
  6. To create a new reservation and attach it to the commitment, do the following:

     1. Select the **Attach a new or existing reservation** checkbox.

     2. Click **Create new reservation**. The **Create a new reservation** pane appears.

     3. In the **Name** field, enter a name for the reservation.

     4. Optional: In the **Description** field, enter a description.

     5. In the **Zone** field, select the zone where you want the reserved resources to be available.

     6. In the **Share type** section, specify how you want to share this reservation:

        * To create a single-project reservation, select **Local**.
        * To create a reservation that's shared with multiple projects, select **Shared**. Then, click **Add projects** and select the projects that you want.
     7. In the **Google Cloud Services** section, specify whether to share this reservation with other services like Google Kubernetes Engine or Vertex AI.

     8. In the **Use with VM instance** section, select how you want VMs to consume your reservation:

        * To allow VMs with matching properties to automatically consume this reservation, select **Use reservation automatically**.
        * To consume this reservation's resources only when specifically targeted by name, select **Select specific reservation**.
     9. In the **Resource details** section, do the following:

        1. In the **Number of VM instances** field, enter the number of VMs.

        2. In the **Machine configuration** section, specify properties by selecting **Machine type**. Select a machine type from the list, or select **Custom** to specify the number of **Cores** and amount of **Memory**.

        3. Optional: If you want to reserve GPUs, then click **Add GPU** and specify the **GPU type** and **Number of GPUs** for each VM.

        4. Optional: If you want to reserve Local SSD disks, then specify the **Number of disks** and **Interface type**.

        5. Optional: If you want to specify a group placement policy, then in the **Group placement policy** list, select or create a policy.

     10. To finish specifying the properties for this reservation, click **Create and attach**.

     11. Optional: If you want to create and attach more new reservations, then click **Create new reservation** again and repeat these steps.

_After you attach your reservations, Compute Engine automatically populates the fields in the**Commitment details** section to match the numbers and types of resources from your attached reservations. If you manually entered values for any resources in the **Commitment details** section before attaching reservations, then your values are overwritten with values from the reservations._

  7. In the **Commitment details** section, do the following:

     1. In the **Cores** field, verify the pre-filled value. Optionally, you can specify a different number of vCPUs.

     2. In the **Memory** field, verify the pre-filled amount of memory in GB. Optionally, you can specify a different amount. You can specify memory only in increments of 0.25 GB. To specify a custom memory value for your commitment, use gcloud CLI or REST instead.

     3. Expand the **GPUs and local SSDs** section and verify that the types and numbers match between the commitment and attached reservations, as follows:

        1. In the **GPU type** field, verify the pre-filled GPU type.

        2. In the **Number of GPUs** field, verify the pre-filled number of GPUs.

        3. In the **Local SSDs** field, verify the pre-filled number of disks.

If you manually specify different values from the attached reservations for any of these fields, then your commitment purchase doesn't go through. For all GPUs and most Local SSD disks, the total numbers and types must match between your commitment and attached reservations.

**Note:** This requirement doesn't apply to local Titanium SSD disks for use with C4, C4A, C4D, C4N, H4D, Z3, or G4 machine series. For these disks only, you don't need to attach any reservations and you can choose to specify different numbers between your commitment and attached reservations.
  8. In the **Term** section, do the following:

     1. To specify the _[plan](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#commitment-plan)_ for your commitment, select either **1 year** or **3 years**. The plan determines the CUD rate and preset term duration of your commitment.

     2. Review the **Start date** field, which shows the date and time when your commitment becomes active. This field is automatically set to 12 AM US and Canadian Pacific Time on the day after your current date.

     3. Optional. To extend your commitment's [term](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#commitment-term) beyond the preset term duration that is defined by your commitment plan, in the **End date** field, specify a custom end date for your commitment. For more information, see [Extend commitment terms](https://docs.cloud.google.com/compute/docs/committed-use-discounts/extend-commitment-term).

     4. Optional. If you want your commitment to [automatically renew](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically) at the end of its term, then select the **Auto-renew commitment** checkbox.

  9. In the **Summary** pane, review your commitment details and any potential quota limitations.

  10. To finish purchasing your commitment, do the following:

     1. Navigate to the bottom of the page.

     2. Review the **Disclosures** section that contains information about fees, discount eligibility, and terms and conditions.

     3. To confirm your acceptance of the [commitment price](https://cloud.google.com/products/compute/pricing) and [service specific terms](https://cloud.google.com/terms/service-terms), select the checkbox.

     4. Click **Purchase**.




###  gcloud 

To create your attached reservations while purchasing your commitment, run the [`gcloud compute commitments create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments/create).

**Note:** You can't use the gcloud CLI to create your attached reservations using instance templates. Instead, you must manually specify the VM properties for your reservations.

Depending on whether you want to attach a single reservation or multiple reservations, run the command in one of the following ways:

  * To create and attach a single reservation to your commitment, define the properties of the attached reservation by running the following command:
        
        gcloud compute commitments create COMMITMENT_NAME \
            --region=REGION \
            --project=PROJECT_ID \
            --plan PLAN \
            --type COMMITMENT_TYPE \
            --resources=vcpu=COMMITTED_VCPUS,memory=COMMITTED_MEMORY,local-ssd=COMMITTED_LOCAL_SSD \
            --resources-accelerator=count=COMMITTED_ACCELERATOR_COUNT,type=COMMITTED_ACCELERATOR_TYPE \
            --custom-end-time=CUSTOM_END_DATE \
            --reservation=RESERVATION_NAME \
            --reservation-zone=RESERVATION_ZONE \
            --machine-type=RESERVED_MACHINE_TYPE \
            --require-specific-reservation=REQUIRE_SPECIFIC_RESERVATION_VALUE \
            --vm-count=NUMBER_OF_RESERVED_VMS \
            --accelerator=type=RESERVED_ACCELERATOR_TYPE,count=RESERVED_ACCELERATOR_COUNT \
            --local-ssd=interface=INTERFACE_1,size=375 \
            --local-ssd=interface=INTERFACE_2,size=375 \
            --minimum-cpu-platform=MINIMUM_CPU_PLATFORM \
            --share-setting=SHARE_SETTING \
            --share-with=CONSUMER_PROJECT_ID_1,CONSUMER_PROJECT_ID_2
        

  * To create and attach multiple reservations to your commitment, define the reservation's properties using a YAML file and then specify that YAML file in the command that you use to purchase your commitment. Optionally, you can also use this YAML file approach to create and attach a single reservation to your commitment. To create your attached reservations using this approach, do the following:

    1. Create the YAML file in the current directory and specify the configuration that you want for each attached reservation. For example, to specify the configuration of a shared reservation shared with two projects that specifies GPUs, two Local SSD disks, and a minimum CPU platform, include the following text in your YAML file:
           
           - reservation: RESERVATION_NAME
             reservation_zone: RESERVATION_ZONE
             require_specific_reservation: REQUIRE_SPECIFIC_RESERVATION_VALUE
             vm_count: NUMBER_OF_RESERVED_VMS
             machine_type: RESERVED_MACHINE_TYPE
             accelerator:
             - count: RESERVED_ACCELERATOR_COUNT
               type: RESERVED_ACCELERATOR_TYPE
             local_ssd:
             - interface: INTERFACE_1
               size: 375
             - interface: INTERFACE_2
               size: 375
             project: OWNER_PROJECT_ID
             minimum-cpu-platform: MINIMUM_CPU_PLATFORM
             share-setting: SHARE_SETTING
             share-with:
             - CONSUMER_PROJECT_ID_1
             - CONSUMER_PROJECT_ID_2
           
           

To specify the configuration for multiple reservations, repeat these properties for each reservation that you want to create. You can attach any number of existing reservations that you want to your commitment.

    2. Run the `gcloud compute commitments create` command and include the `--reservations-from-file` flag.
           
           gcloud compute commitments create COMMITMENT_NAME \
               --region REGION \
               --project PROJECT_ID \
               --plan PLAN \
               --type COMMITMENT_TYPE \
               --resources=vcpu=COMMITTED_VCPUS,memory=COMMITTED_MEMORY,local-ssd=COMMITTED_LOCAL_SSD \
               --resources-accelerator=count=COMMITTED_ACCELERATOR_COUNT,type=COMMITTED_ACCELERATOR_TYPE \
               --reservations-from-file=YAML_FILE
           




Replace the following with the corresponding properties of the commitment and the attached reservations:

###  Commitment 

  * `COMMITMENT_NAME`: the name of the commitment.
  * `REGION`: the region where the commitment is located.
  * `PROJECT_ID`: the ID of the project where you want to purchase the commitment with the attached reservations.
  * `PLAN`: the commitment plan, which determines your CUD rate and the preset term duration. Specify `12-month` or `36-month`.
  * `CUSTOM_END_DATE`: Optional. A custom end date for your term, which must be formatted as `YYYY-MM-DD`. For example, to specify a custom end date of April 20, 2024, format it as `2024-04-20`.
  * `COMMITMENT_TYPE`: the commitment type. The following commitment types provide options for GPUs, Local SSD disks, or both:

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
    * For N1 machine types, use `general-purpose`
    * For C4 machine types, use `general-purpose-c4`
    * For C4A machine types, use `general-purpose-c4a`
    * For C4D machine types, use `general-purpose-c4d`
    * For C4N machine types, use `network-optimized-c4n`
    * For N2 machine types, use `general-purpose-n2`
    * For N2D machine types, use `general-purpose-n2d`
    * For M1 machine types, use `memory-optimized`
    * For M3 machine types, use `memory-optimized-m3`
    * For Z3 machine types, use `storage-optimized-z3`
    * For Z4D machine types, use `storage-optimized-z4d`
    * For Z4M machine types, use `storage-optimized-z4m`
  * `COMMITTED_VCPUS`: the number of vCPUs that you want in your commitment. The number must be a positive integer.

  * `COMMITTED_MEMORY`: the amount, in MB or GB, of memory that you want in your commitment. For example, `10GB` or `10240MB`. For the gcloud CLI, you can specify memory in MB or GB. If you don't specify a unit, then Compute Engine uses GB as the default unit. However, note that when you use REST, Compute Engine uses MB as the default unit.

  * `COMMITTED_LOCAL_SSD`: the amount of Local SSD storage, which must be specified in GB; for example, `375GB`.

  * `COMMITTED_ACCELERATOR_COUNT`: the number of GPUs that you want in your commitment.

  * `COMMITTED_ACCELERATOR_TYPE`: the GPU type that you want in your commitment.

  * `YAML_FILE`: The path to the YAML file that contains the configuration of the attached reservations.




###  Attached reservations 

  * `RESERVATION_NAME`: the name of the attached reservation.
  * `RESERVATION_ZONE`: the zone of the attached reservation.
  * `REQUIRE_SPECIFIC_RESERVATION_VALUE`: specifies if the attached reservation is a specifically targeted reservation; either `true` or `false`. For more information about specifically targeted reservations, see [How reservations work](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#how-reservations-work).
  * `NUMBER_OF_RESERVED_VMS`: the number of VMs that you want to reserve in the attached reservation.
  * `RESERVED_MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-types) that you want for the VMs in your attached reservation.

    * For **predefined** machine types, use the format `MACHINE_FAMILY-standard-CPUS`; for example, `n2-standard-4`.
    * For **custom** machine types, use the format `MACHINE_FAMILY-custom-CPUS-MEMORY`; for example `n2-custom-4-5120`. For a full list of restrictions, read the [specifications](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#specifications) for custom machine types.

Replace the following:

      * `MACHINE_FAMILY`: the family of machine types; for example, specify `n2` for N2 VMs.
      * `CPUS`: the number of [vCPUs](https://docs.cloud.google.com/compute/docs/cpu-platforms).
      * `MEMORY`: the total memory for a reserved VM. Memory must be a multiple of 256 MB and must be supplied in MB; for example, to create an N2 VM with 4 vCPUs and 5 GB of memory, which is 5120 MB, use `n2-custom-4-5120`.
  * `RESERVED_ACCELERATOR_COUNT`: the number of GPUs that you want to add, per VM, in the attached reservation.

  * `RESERVED_ACCELERATOR_TYPE`: the [type of accelerator](https://docs.cloud.google.com/compute/docs/gpus) that you want to add in the attached reservation.

  * `INTERFACE_1` and `INTERFACE_2`: the type of interface that you want the [Local SSD disks](https://docs.cloud.google.com/compute/docs/disks#localssds) for each reserved VM to use. Valid options are: `scsi` and `nvme`. Repeat the `local_ssd` parameter for each Local SSD disk that you want to add. You can specify up to 24 Local SSD disks.

  * `OWNER_PROJECT_ID`: the ID of the project where you want to purchase the commitment with the attached reservation. Specify this field if you want to share your attached reservation across multiple consumer projects.

  * `MINIMUM_CPU_PLATFORM`: the minimum CPU platform that you want to specify for the attached reservation.

  * `SHARE_SETTING`: the type of sharing for the attached reservation. Specify this field with the value as `projects` if you want to share your attached reservation across multiple consumer projects. Exclude this field if you want to create a single-project reservation.

  * `CONSUMER_PROJECT_ID_1` and `CONSUMER_PROJECT_ID_2`: the [project IDs](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the projects that can share this reservation, for example `project-1` and `project-2`. You can include up to 100 consumer projects. These projects must be in the same organization as the owner project. Don't include the ID of the project where you create this reservation, as that project is allowed to consume this reservation by default. Exclude these fields if you want to create a single-project reservation.




Compute Engine creates the commitment and the attached reservations only if there are enough resources of the specified machine type in the target zone, and sufficient quota, at the time of your request. If your purchase was successful, then you see a success message similar to the following:
    
    
    Created[https://www.googleapis.com/compute/v1/projects/your-project/regions/your-region/commitments/your-commitment-name]
    

#### Examples

The following example scenarios and commands show how you can purchase a commitment for GPUs, Local SSD disks, or both by creating new reservations to attach to that commitment.

**Example 1: Purchase a commitment for GPUs by attaching a single new reservation**

Suppose that you want to purchase a 1-year commitment for general-purpose resources (or GPU resources) in the `us-central1` region with 96 vCPUs, 624 GB of memory, and 4 NVIDIA V100 GPUs. You want to create a new reservation `reservation-01` in the `us-central1-a` zone that reserves 2 `n1-standard-32` VMs (each VM with 32 vCPUs, 120 GB memory, and 2 NVIDIA V100 GPUs) to consume these committed resources. To purchase this example commitment with its attached reservation, run the following command. For the gcloud CLI, you can specify memory in MB or GB. If you don't specify a unit, then Compute Engine uses GB as the default unit. However, note that when you use REST, Compute Engine uses MB as the default unit.
    
    
    gcloud compute commitments create commitment-01 \
        --region=us-central1 \
        --project=myproject \
        --resources=vcpu=96,memory=624GB \
        --resources-accelerator=type=nvidia-tesla-v100,count=4 \
        --plan 12-month \
        _--reservation=reservation-01 \
        --reservation-zone=us-central1-a \
        --machine-type=n1-standard-32 \
        --accelerator=type=nvidia-tesla-v100,count=2 \
        --vm-count=2_
    

**Example 2: Purchase a commitment for GPUs without specifying vCPUs or memory**

To commit to and reserve GPUs and Local SSD disks without committing to vCPUs or memory, specify `0` as the value for vCPU and memory quantities. For example, suppose that you want to purchase a 1-year commitment for GPU resources in the `us-west2` region with 0 vCPUs, 0 GB memory, and 1 NVIDIA P4 GPU. You also want to create a new reservation `reservation-01` in the `us-west2-b` zone that reserves 1 `n1-standard-2` VM (with 2 vCPUs, 7.5 GB memory, and 1 NVIDIA P4 GPU) to attach to the commitment. To purchase this example commitment with its attached reservation, run the following command. For the gcloud CLI, you can specify memory in MB or GB. If you don't specify a unit, then Compute Engine uses GB as the default unit. However, note that when you use REST, Compute Engine uses MB as the default unit.
    
    
    gcloud compute commitments create commitment-02 \
        --region=us-west2 \
        --project=myproject \
        _--resources=vcpu=0,memory=0_ \
        --resources-accelerator=type=nvidia-tesla-p4,count=1 \
        --plan 12-month \
        --reservation=reservation-01 \
        --reservation-zone=us-west2-b \
        --machine-type=n1-standard-2 \
        --accelerator=type=nvidia-tesla-p4,count=1 \
        --vm-count=1
    

**Example 3: Purchase a commitment for GPUs and Local SSD disks by attaching multiple new reservations**

Suppose that you want to purchase a 1-year commitment for general-purpose resources (or GPU and Local SSD resources) in the `us-central1` region. You want the commitment for 96 vCPUs, 624 GB of memory, 1 NVIDIA V100 GPU, and 750 GB of Local SSD storage (matching 2 Local SSD disks). You also want to create and attach two reservations in the `us-central1-a` zone. In the first reservation, `res-01`, you want to reserve 1 `n1-standard-2` VM (with 2 vCPUs, 7.5 GB memory, and 1 NVIDIA V100 GPU); this is a targeted reservation. In the second reservation, `res-02`, you want to reserve 1 `n1-standard-8` VM (with 8 vCPUs, 30 GB memory) and attach 2 Local SSD disks (one SCSI interface, one NVMe interface).

To purchase this example commitment with the attached reservations, first create the YAML file with the properties of both reservations as follows:
    
    
    - reservation: res-01
      reservation_zone: us-central1-a
      require_specific_reservation: true
      vm_count: 1
      machine_type: n1-standard-2
      accelerator:
      - count: 1
        type: nvidia-tesla-v100
    - reservation: res-02
      reservation_zone: us-central1-a
      vm_count: 1
      machine_type: n1-standard-8
      local_ssd:
      - interface: scsi
        size: 375
      - interface: nvme
        size: 375
    

After you create the YAML file, to finish purchasing the commitment with its attached reservations, run the following command. The Local SSD storage value must be specified in GB (for example, `375GB`). For the gcloud CLI, you can specify memory in MB or GB. If you don't specify a unit, then Compute Engine uses GB as the default unit. However, note that when you use REST, Compute Engine uses MB as the default unit for memory.
    
    
    gcloud compute commitments create commitment-03 \
        --region=us-central1 \
        --project=myproject \
        --resources=vcpu=96,memory=624,local-ssd=750 \
        --resources-accelerator=type=nvidia-tesla-v100,count=1 \
        --plan 12-month \
        _--reservations-from-file= YAML_FILE_
    

###  REST 

To create your attached reservations while purchasing your commitment, make a `POST` request to the [`regionCommitments.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCommitments/insert). In your request, include the `reservations` field to define a list of all the new reservations that you want to create and attach. You can attach any number of existing reservations that you want to your commitment.

  * To create your new reservation by manually specifying all the VM properties, include the `instanceProperties` field and exclude the `sourceInstanceTemplate` field.

For example, to manually specify the configuration of a shared reservation shared with two projects that specifies GPUs, two Local SSD disks, and a minimum CPU platform, make the following request:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/commitments
        
        {
        "name": "COMMITMENT_NAME",
        "plan": "PLAN",
        "type": "COMMITMENT_TYPE",
        "resources":
        [
          {
            "amount": "COMMITTED_VCPUS",
            "type": "VCPU"
          },
          {
            "amount": "COMMITTED_MEMORY",
            "type": "MEMORY"
          },
          {
            "acceleratorType": "COMMITTED_ACCELERATOR_TYPE",
            "amount": "COMMITTED_ACCELERATOR_COUNT",
            "type": "ACCELERATOR"
          },
          {
            "amount": "COMMITTED_LOCAL_SSD",
            "type": "LOCAL_SSD"
          }
        ],
        "customEndTimestamp": "CUSTOM_END_DATETEND_TIMEZ",
        "reservations":
        [
          {
            "name": "RESERVATION_NAME",
            "specificReservation":
            {
              "count": "NUMBER_OF_RESERVED_VMS",
              "instanceProperties":
              {
                "guestAccelerators":
                [
                  {
                    "acceleratorCount": "RESERVED_ACCELERATOR_COUNT",
                    "acceleratorType": "RESERVED_ACCELERATOR_TYPE"
                  }
                ],
                "localSsds":
                [
                  {
                    "diskSizeGb": "375",
                    "interface": "INTERFACE_1"
                  },
                  {
                    "diskSizeGb": "375",
                    "interface": "INTERFACE_2"
                  }
                ],
                "machineType": "RESERVED_MACHINE_TYPE",
                "minCpuPlatform": "MINIMUM_CPU_PLATFORM"
              }
            },
            "specificReservationRequired": "REQUIRE_SPECIFIC_RESERVATION_VALUE",
            "zone": "RESERVATION_ZONE",
            "shareSettings":
            {
              "shareType": "SPECIFIC_PROJECTS",
              "projectMap":
              {
                "CONSUMER_PROJECT_ID_1":
                {
                  "projectId": "CONSUMER_PROJECT_ID_1"
                },
                "CONSUMER_PROJECT_ID_2":
                {
                  "projectId": "CONSUMER_PROJECT_ID_2"
                }
              }
            }
          }
        ]
        }
        
        

  * To create your new reservation by specifying an instance template, include the `sourceInstanceTemplate` field and exclude the `instanceProperties` field.
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/commitments
        
        {
        "name": "COMMITMENT_NAME",
        "plan": "PLAN",
        "type": "COMMITMENT_TYPE",
        "resources":
        [
          {
            "amount": "COMMITTED_VCPUS",
            "type": "VCPU"
          },
          {
            "amount": "COMMITTED_MEMORY",
            "type": "MEMORY"
          },
          {
            "acceleratorType": "COMMITTED_ACCELERATOR_TYPE",
            "amount": "COMMITTED_ACCELERATOR_COUNT",
            "type": "ACCELERATOR"
          },
          {
            "amount": "COMMITTED_LOCAL_SSD",
            "type": "LOCAL_SSD"
          }
        ],
        "customEndTimestamp": "CUSTOM_END_DATETEND_TIMEZ",
        "reservations":
        [
          {
            "name": "RESERVATION_NAME",
            "specificReservation":
            {
              "count": "NUMBER_OF_RESERVED_VMS",
              "sourceInstanceTemplate": "projects/PROJECT_ID/LOCATION/instanceTemplates/INSTANCE_TEMPLATE_NAME"
            },
            "specificReservationRequired": "REQUIRE_SPECIFIC_RESERVATION_VALUE",
            "zone": "RESERVATION_ZONE",
            "shareSettings":
            {
              "shareType": "SPECIFIC_PROJECTS",
              "projectMap":
              {
                "CONSUMER_PROJECT_ID_1":
                {
                  "projectId": "CONSUMER_PROJECT_ID_1"
                },
                "CONSUMER_PROJECT_ID_2":
                {
                  "projectId": "CONSUMER_PROJECT_ID_2"
                }
              }
            }
          }
        ]
        }
        
        




Replace the following with the corresponding properties of the commitment and the attached reservations:

###  Commitment 

  * `COMMITMENT_NAME`: the name of the commitment.
  * `REGION`: the region where the commitment is located.
  * `PROJECT_ID`: the ID of the project where you want to purchase the commitment with the attached reservations.
  * `PLAN`: the commitment plan, which determines your CUD rate and the preset term duration. Specify `TWELVE_MONTH` or `THIRTY_SIX_MONTH`.
  * `COMMITMENT_TYPE`: the commitment type. The following commitment types provide options for GPUs, Local SSD disks, or both:

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
    * For N1 machine types, use `GENERAL_PURPOSE`
    * For C4 machine types, use `GENERAL_PURPOSE_C4`
    * For C4A machine types, use `GENERAL_PURPOSE_C4A`
    * For C4D machine types, use `GENERAL_PURPOSE_C4D`
    * For C4N machine types, use `NETWORK_OPTIMIZED_C4N`
    * For N2 machine types, use `GENERAL_PURPOSE_N2`
    * For N2D machine types, use `GENERAL_PURPOSE_N2D`
    * For M1 machine types, use `MEMORY_OPTIMIZED`
    * For M3 machine types, use `MEMORY_OPTIMIZED_M3`
    * For Z3 machine types, use `STORAGE_OPTIMIZED_Z3`
    * For Z4D machine types, use `STORAGE_OPTIMIZED_Z4D`
    * For Z4M machine types, use `STORAGE_OPTIMIZED_Z4M`
  * `COMMITTED_VCPUS`: the number of vCPUs that you want in your commitment. The number must be a positive integer.

  * `COMMITTED_MEMORY`: the amount of memory that you want in your commitment. For REST, Compute Engine uses MB as the default unit. However, note that when you use gcloud CLI, Compute Engine uses GB as the default unit.

  * `COMMITTED_LOCAL_SSD`: the amount, in GB, of Local SSD storage that you want in your commitment.

  * `COMMITTED_ACCELERATOR_COUNT`: the number of GPUs that you want in your commitment.

  * `COMMITTED_ACCELERATOR_TYPE`: the GPU type that you want in your commitment.

  * `CUSTOM_END_DATE`: Optional. A custom end date for your term, which must be formatted as `YYYY-MM-DD`. For example, to specify a custom end date of April 20, 2024, format it as `2024-04-20`.

  * `END_TIME`: 12 AM US and Canadian Pacific Time (UTC-8 or UTC-7), as an offset of [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). Specify this value only if you specified a custom end date for your commitment. Specify one of the following values:

    * During daylight saving time: `07:00:00`
    * During other times: `08:00:00`



###  Attached reservations 

  * `RESERVATION_NAME`: the name of the attached reservation.
  * `RESERVATION_ZONE`: the zone of the attached reservation.
  * `REQUIRE_SPECIFIC_RESERVATION_VALUE`: specifies if the attached reservation is a specifically targeted reservation; either `true` or `false`. For more information about specifically targeted reservations, see [How reservations work](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#how-reservations-work).
  * `NUMBER_OF_RESERVED_VMS`: the number of VMs that you want to reserve in the attached reservation.
  * `RESERVED_MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-types) that you want for the VMs in your attached reservation.

    * For **predefined** machine types, use the format `MACHINE_FAMILY-standard-CPUS`; for example, `n2-standard-4`.
    * For **custom** machine types, use the format `MACHINE_FAMILY-custom-CPUS-MEMORY`; for example `n2-custom-4-5120`. For a full list of restrictions, read the [specifications](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#specifications) for custom machine types.

Replace the following:

      * `MACHINE_FAMILY`: the family of machine types; for example, specify `n2` for N2 VMs.
      * `CPUS`: the number of [vCPUs](https://docs.cloud.google.com/compute/docs/cpu-platforms).
      * `MEMORY`: the total memory for a reserved VM. Memory must be a multiple of 256 MB and must be supplied in MB; for example, to create an N2 VM with 4 vCPUs and 5 GB of memory, which is 5120 MB, use `n2-custom-4-5120`.
  * `RESERVED_ACCELERATOR_COUNT`: the number of GPUs you want to add, per VM, in the attached reservation.

  * `RESERVED_ACCELERATOR_TYPE`: the [type of accelerator](https://docs.cloud.google.com/compute/docs/gpus) you want to add in the attached reservation.

  * `INTERFACE_1` and `INTERFACE_2`: the type of interface that you want the [Local SSD disks](https://docs.cloud.google.com/compute/docs/disks#localssds) for each reserved VM to use. Valid options are: `scsi` and `nvme`. Repeat the `localSsds` parameter for each Local SSD disk that you want to add. You can specify up to 24 Local SSD disks.

  * `MINIMUM_CPU_PLATFORM`: the minimum CPU platform that you want to specify for the attached reservation.

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template that you want to use to create your attached reservation.

  * `SHARE_SETTING`: the type of sharing for the attached reservation. Specify this field with the value as `SPECIFIC_PROJECTS` if you want to share your attached reservation across multiple consumer projects. Exclude this field if you want to create a single-project reservation.

  * `CONSUMER_PROJECT_ID_1` and `CONSUMER_PROJECT_ID_2`: the [project IDs](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the projects that can share this reservation; for example, `project-1` and `project-2`. You can include up to 100 consumer projects. These projects must be in the same organization as the owner project. Don't include the ID of the project where you create this reservation, as that project is allowed to consume this reservation by default. Exclude these fields if you want to create a single-project reservation.




Compute Engine creates the commitment and the attached reservations only if there are enough resources of the specified machine type in the target zone, and sufficient quota, at the time of your request. If your purchase was successful, then Compute Engine returns a `200` status for your REST API request.

#### Examples

The following example scenarios and commands show how you can purchase a commitment for GPUs, Local SSD disks, or both by creating new reservations to attach to that commitment.

**Example 1: Purchase a commitment for GPUs by attaching a single new reservation**

Suppose that you want to purchase a 1-year commitment for general-purpose resources in the `us-central1` region that includes 96 vCPUs, 624 GB of memory (equivalent to 638976 MB), and 4 NVIDIA V100 GPUs. You want to create a new reservation `reservation-01` in the `us-central1-a` zone that reserves 2 `n1-standard-8` VMs (each VM with 8 vCPUs, 30 GB memory, and 2 NVIDIA V100 GPUs) to attach to that commitment. To purchase this example commitment with its attached reservation, make the following `POST` request. For REST, you must specify memory in MB. However, note that when you use gcloud CLI, Compute Engine uses GB as the default unit.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/my-project/regions/us-central1/commitments
    
    {
      "name": "commitment-01",
      "plan": "TWELVE_MONTH",
      "type": "GENERAL_PURPOSE",
      "resources":
      [
        {
          "amount": "96",
          "type": "VCPU"
        },
        {
          "amount": "638976",
          "type": "MEMORY"
        },
        {
          "acceleratorType": "nvidia-tesla-v100",
          "amount": "4",
          "type": "ACCELERATOR"
        }
      ],
      "reservations":
      [
        {
          "name": "reservation-01",
          "specificReservation":
          {
            "count": "2",
            "instanceProperties":
            {
              "guestAccelerators":
              [
                {
                  "acceleratorCount": 2,
                  "acceleratorType": "nvidia-tesla-v100"
                }
              ],
              "machineType": "n1-standard-8"
            }
          },
          "specificReservationRequired": false,
          "zone": "us-central1-a"
        }
      ]
    }
    

**Example 2: Purchase a commitment for GPUs without specifying vCPUs or memory**

To commit to and reserve GPUs and Local SSD disks without committing to vCPUs or memory, specify `0` as the value for vCPU and memory quantities. For example, suppose that you want to purchase a 1-year commitment only for GPU resources in the `us-west2` region, with 0 vCPUs, 0 MB memory, and 4 NVIDIA P4 GPUs. You also want to create a new reservation `reservation-01` in the `us-west2-b` zone that reserves 1 `n1-standard-2` VM (with 2 vCPUs, 7.5 GB memory, and 4 NVIDIA P4 GPUs) to attach to the commitment. To purchase this example commitment with its attached reservation, make the following `POST` request. For REST, you must specify memory in MB. However, note that when you use gcloud CLI, Compute Engine uses GB as the default unit.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/my-project/regions/us-west2/commitments
    
    {
      "name": "commitment-02",
      "plan": "TWELVE_MONTH",
      "type": "GENERAL_PURPOSE",
      "resources":
      [_{
          "amount": "0",
          "type": "VCPU"
        },
        {
          "amount": "0",
          "type": "MEMORY"
        },_
        {
          "acceleratorType": "nvidia-tesla-p4",
          "amount": "4",
          "type": "ACCELERATOR"
        }
      ],
      "reservations":
      [
        {
          "name": "reservation-01",
          "specificReservation":
          {
            "count": "1",
            "instanceProperties":
            {
              "guestAccelerators":
              [
                {
                  "acceleratorCount": 4,
                  "acceleratorType": "nvidia-tesla-p4"
                }
              ],
              "machineType": "n1-standard-2"
            }
          },
          "specificReservationRequired": false,
          "zone": "us-west2-b"
        }
      ]
    }
    

**Example 3: Purchase a commitment for GPUs and Local SSD disks by attaching multiple new reservations**

Suppose that you want to purchase a 1-year commitment for general-purpose resources in the `us-central1` region, with 96 vCPUs, 624 GB of memory (equivalent to 638976 MB), 1 NVIDIA V100 GPU, and 750 GB of Local SSD storage. You also want to create and attach two reservations in the `us-central1-a` zone. In the first reservation, `res-01`, you want to reserve 1 `n1-standard-2` VM (with 2 vCPUs, 7.5 GB memory, and 1 NVIDIA V100 GPU); this is a targeted reservation. In the second reservation, `res-02`, you want to reserve 1 `n1-standard-8` VM (with 8 vCPUs, 30 GB memory) and attach 2 Local SSD disks (one SCSI interface, one NVMe interface). To purchase this example commitment with the attached reservations, make the following `POST` request. Note that the Local SSD storage value must be specified in GB. For memory, you must specify the value in MB. However, note that when you use gcloud CLI, Compute Engine uses GB as the default unit for memory.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/my-project/regions/us-central1/commitments
    
    {
      "name": "commitment-03",
      "plan": "TWELVE_MONTH",
      "type": "GENERAL_PURPOSE",
      "resources":
      [
        {
          "amount": "96",
          "type": "VCPU"
        },
        {
          "amount": "638976",
          "type": "MEMORY"
        },
        {
          "acceleratorType": "nvidia-tesla-v100",
          "amount": "1",
          "type": "ACCELERATOR"
        },
        {
          "amount": "750",
          "type": "LOCAL_SSD"
        }
      ],
      _"reservations":
      [
        {
          "name": "res-01",
          "specificReservation":
          {
            "count": "1",
            "instanceProperties":
            {
              "guestAccelerators":
              [
                {
                  "acceleratorCount": 1,
                  "acceleratorType": "nvidia-tesla-v100"
                }
              ],
              "machineType": "n1-standard-2"
            }
          },
          "specificReservationRequired": true,
          "zone": "us-central1-a"
        },
        {
          "name": "res-02",
          "specificReservation":
          {
            "count": "1",
            "instanceProperties":
            {
              "localSsds":
              [
                {
                  "diskSizeGb": "375",
                  "interface": "SCSI"
                },
                {
                  "diskSizeGb": "375",
                  "interface": "NVME"
                }
              ],
              "machineType": "n1-standard-8"
            }
          },
          "specificReservationRequired": false,
          "zone": "us-central1-a"
        }
      ]_
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
