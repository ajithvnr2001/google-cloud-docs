---
url: https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments/
title: Combine reservations with committed use discounts \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T23:39:01.908386+00:00
---

# Combine reservations with committed use discounts  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Combine reservations with committed use discounts Stay organized with collections  Save and categorize content based on your preferences. 

[Committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview) provide deeply discounted prices for your Compute Engine resources in exchange for 1-year or 3-year committed-use contracts (also known as commitments). You commit to a minimum amount of resource usage or a minimum amount of spend and receive CUDs on your resource usage costs in return. However, commitments don't reserve zonal capacity for your committed resources. To get zonal resources at discounted prices and also ensure that capacity is reserved for them, you must both purchase commitments and create reservations for those zonal resources.

This document explains how you can receive CUDs for your reserved resources and how to attach reservations to [resource-based commitments](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts).

## Before you begin

  * Review the basics of reservations along with their requirements and restrictions. For more information, see [ About reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview). 
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




## CUDs for your reserved resource usage

You receive CUDs from active commitments for any [eligible resource usage](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#order_of_discount_application) in your projects. If you also have any reservations to hold capacity for resources in that project, then CUDs from active commitments can also apply to those reserved resources. For any reserved resources to become eligible to receive CUDs, the following requirements apply:

  * You aren't receiving any other form of discount for your resource usage.
  * Your VMs must be consuming the reservations while the commitments are active.
  * At a minimum, the following properties must match between your active commitments and the reservations that your VMs consume:

    * The zone specified in your reservation must match the region specified in your commitment.
    * The machine type that is specified by the reservation must be supported by the specific commitment that you purchase.
    * If you're using a resource-based commitment and [CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects) isn't enabled in your Cloud Billing account, then your reservation and commitment must be for the same project.



Depending on the resource type, you can receive either resource-based or spend-based CUDs for your reserved instance usage.

### Resource-based CUDs

Compute Engine offers resource-based CUDs for machine resources like vCPUs, memory, GPUs, and Local SSD disks in the following ways. By default, Compute Engine enables [CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects) to pool your resource-based CUDs at a Cloud Billing account level and apply them to eligible usage across all projects in that account.

  * **vCPUs and memory** : To receive resource-based CUDs for these resource types, purchase resource-based commitments that include the required resource types. When VMs in your Cloud Billing account consume any reservations that match such active commitment properties, Compute Engine automatically applies the discounts to eligible usage. If you reserved more resources than you committed to purchasing, then you don't receive CUDs for those additional resources.

  * **GPUs and Local SSD disks** : To receive resource-based CUDs for GPUs and most Local SSD disks, you must do both the following:

    * Purchase resource-based commitments that include the required resource types.
    * Create reservations that specify the GPUs or Local SSD disks with properties that match your commitment, and attach those reservations to the commitment.

For resource-based CUDs, this reservation requirement applies to all GPUs and Local SSD disks for use with most machine series. Some machine series don't require you to attach reservations for Local SSD disks when you purchase the commitments.


**Caution:** If you have a shared reservation in a project and want usage from the shared projects to be eligible for the current project's CUDs, then you must ensure the following: 

  1. Make sure that [ CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects) is enabled for the current project's Cloud Billing account.
  2. Share your reservation only with projects that are linked to the same Cloud Billing account.



If you don't meet these conditions, then usage from those projects won't be eligible for the shared CUDs and you might be charged the on-demand rates.

### Compute flexible CUDs

Spend-based CUDs for Compute Engine are known as compute flexible CUDs. A single compute flexible commitment covers your eligible Google Cloud spend for a Cloud Billing account across Compute Engine, GKE, and Cloud Run. These commitments are purchased at the Cloud Billing account level and cover eligible spend across regions and machine configurations.

For Compute Engine specifically, the following resources are eligible to receive flexible CUDs:

  * vCPUs, memory of eligible machine series
  * All Local SSD disks
  * GPUs for G2 (L4) and G4 (NVIDIA RTX Pro 6000) machine series



Unlike resource-based commitments, compute flexible commitments don't require or support attached reservations. You can purchase compute flexible commitments for eligible GPUs and Local SSD disks without needing to reserve those resources. Consequently, these commitments don't come with assured capacity for any eligible resources. For GPU instances like G2 or G4 machine types, if capacity for a specific type (for example, G2) isn't available in one zone, then you can use your compute flexible commitment to cover your deployment of those GPU instances in another available zone instead. If capacity for a specific GPU type (for example, G2) isn't available in any zone at all, then you can use your compute flexible commitment to cover your deployment of the other GPU type (for example, G4) instead. If neither GPU type has capacity available in any region, then you can still use your compute flexible commitment to cover your eligible spend on other supported resources or services instead. If you want capacity assurance for GPUs to use with G2 or G4 instances, then create reservations separately for G2 or G4 instances.

When you have compute flexible commitments in a Cloud Billing account, you can receive applicable compute flexible CUDs for consuming reservations in that Cloud Billing account, provided that your spend is on eligible resources and qualifies as [eligible spend](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#how_cuds_apply_to_usage_costs).

## Attach reservations to resource-based commitments

You can attach reservations to any resource-based commitment and ensure that capacity is held in specific zones for the committed resources that you plan to use. You can attach multiple reservations to a single commitment; however, a reservation can only be attached to a single commitment. When you purchase a commitment, you can attach reservations to that commitment in one of the following ways:

  * Use existing reservations that match the commitment properties
  * Create new matching reservations while purchasing your commitment

**Caution:** If you have a shared reservation in a project and want usage from the shared projects to be eligible for the current project's CUDs, then you must ensure the following: 

  1. Enable [ CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects) on the current project's Cloud Billing account.
  2. Share your reservation only with projects that are linked to the same Cloud Billing account.



If you don't meet these conditions, then usage from those projects won't be eligible for the shared CUDs and you might be charged the on-demand rates.

### Resource types that don't require attached reservations

For vCPUs, memory, and local Titanium SSD disks for use with some machine series, you don't need to attach matching reservations to your commitments. Specifically for local Titanium SSD disks, you don't need attached reservations when you purchase commitments for commitment types that are applicable for the following machine series:

  * Accelerator-optimized G4
  * Compute-optimized H4D
  * General-purpose C4
  * General-purpose C4A
  * General-purpose C4D
  * Network-optimized C4N
  * Storage-optimized Z3
  * Storage-optimized Z4D
  * Storage-optimized Z4M



If you want to purchase a resource-based commitment that includes these resource types, then you can purchase that commitment without attaching any reservations for those resources. If you want to attach reservations for any of these vCPUs, memory, or local Titanium SSD disks, then you can optionally choose to attach those reservations.

Your attached reservations for these resources don't have to match the resource types and numbers that are specified by the commitment. Specifically, the following happens when you specify more or less amounts of resources than your commitment:

  * When your commitment specifies more of these resource types than the attached reservations, Compute Engine reserves capacity only for the resources specified by the commitment. However, you can still use the remainder of your committed resources depending on their availability in your region.
  * When your reservation specifies more of these resources than your commitment, you still receive CUDs only for your eligible resource usage. When [CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects) is enabled, resource-based commitments in your Cloud Billing account are pooled and applied to any eligible usage. If your attached reservations specify more resources than what your commitments can cover, then the additional usage might be charged at on-demand rates.



For example, when you purchase a commitment for 4 vCPUs and 30 GB memory, you can choose to do either of the following:

  * Not attach any reservations at all.
  * Attach reservations specifying any combination of these resource types; for example, the following:

    * 4 vCPUs and 30 GB memory
    * 2 vCPUs and 50 GB memory
    * 10 vCPUs and 10 GB memory



However, if your commitment specifies any additional resource types that require attached reservations, then you must still attach reservations for those resources.

To learn how to purchase commitments for resources that don't require reservations, see [Purchase resource-based commitments without attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments).

### Resource types that require attached reservations

For all GPUs and most Local SSD disks, you must reserve those resources and attach the reservations to your resource-based commitments. Without attached reservations for these resources, your resource-based commitment purchase fails. Some local Titanium SSD disks for use with a selection of machine series are exempted from this mandatory reservation attachment. When you purchase a resource-based commitment that includes GPUs, applicable Local SSD disks, or both, you must reserve those resources and attach the reservations to your commitment. You can do this by using a single reservation or a combination of multiple reservations.

**Note:** These reservation requirements don't apply to G2 and G4 GPUs or Local SSD disks when covered by [compute flexible commitments](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based).

When you purchase a commitment for these resources that need attached reservations, you can also optionally include resources that don't need attached reservations in the same commitment. In such scenarios, you can choose to do any of the following:

  * Reserve the optional resources in numbers that match the commitment.
  * Reserve the optional resources in different numbers compared to the commitment.
  * Not reserve the optional resources at all.



To learn how to purchase commitments for GPUs or Local SSD disks, see the following:

  * **For GPUs used with A4X Max, A4X, A4, or A3 Ultra machine types:** See [Reserve capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity) in the AI Hypercomputer documentation.

  * **For all other GPU types and applicable Local SSD disks:** See Purchase resource-based commitments with attached reservations in this document.




When your commitment specifies any resource types that require attached reservation, your attached reservations must specify the exact numbers and types of those resources. Consequently, you also can't have any additional numbers or types of these resources in your attached reservations.

For example, suppose that you purchase a commitment for 30 GB memory and 4 NVIDIA V100 GPUs. The attached reservation (or combination of attached reservations) can specify any amount of vCPUs or memory, but it must have exactly 4 GPUs that are of NVIDIA V100 type. In this example, you can't attach reservations specifying any of the following combination of resources:

  * 6 NVIDIA V100 GPUs
  * 2 NVIDIA V100 GPUs
  * 4 NVIDIA V100 GPUs and 2 NVIDIA A100 GPUs
  * 4 NVIDIA V100 GPUs and 4 Local SSD disks



To view the complete list of machine series that support CUDs for GPUs and Local SSD disks, see the [Hardware commitment types](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#commitment-types-for-hardware-commitments) section in the resource-based CUDs documentation.

### Reservation behavior after commitment purchase

After you purchase a commitment with attached reservations, the reservation behavior depends on whether the commitment specifies any resource types that require attached reservations:

  * **Commitments that require attached reservations** : If the commitment specifies any of these resource types, then you can't do the following throughout the commitment's lifecycle: 
    * Delete the attached reservations or enable the auto-delete setting on those attached reservations. When commitments that specify these resource types expire, any attached reservations are automatically deleted.
    * Resize the reservations or modify any properties of the reservations other than [the share settings](https://docs.cloud.google.com/compute/docs/instances/reservations-modify#modify-share-type). However, you can replace existing attached reservations with new ones.
  * **Commitments where reservations are optional** : If the commitment is for resource types where reservations are optional, then you can delete the reservations, change the number of reserved VMs, or modify properties such as automatic deletion at any time. When these commitments expire, any attached reservations continue to exist unless you configure them to be automatically deleted. Deletion of these reservations has no effect on running VMs that consumed the reserved capacity. The running VMs continue to run and you receive CUD coverage until your commitment expires.



For more information on what can and can't be changed for your attached reservations, see the Allowed changes section of this document.

## Purchase resource-based commitments with attached reservations

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
    

## Replace reservations that are attached to commitments

For commitments that require attached reservations, you can't directly delete, resize, or modify your attached reservations. However, you can modify the machine types and numbers of VMs that are specified in your attached reservation. You can make these modifications by replacing the commitment's existing attached reservation with a new attached reservation.

For commitments where attached reservations are optional, you can delete or resize the attached reservations directly. For more information about the differences in behavior, see Reservation behavior after commitment purchase.

The replacement reservation will always be a newly created reservation. To replace an attached reservation, you must specify the properties of the reservation that you want to use as a replacement. Compute Engine then automatically creates a new reservation with these properties and uses it to replace your attached reservation. You can't use an existing reservation to replace your attached reservation.

### Allowed changes

When you replace a commitment's existing attached reservation with a new reservation, you can request any of the following changes:

  * You can reserve VMs from a different machine type. However, you must still reserve VMs from the same machine series in order to continue receiving CUDs for your reserved resources.
  * You can change the number of VMs that you want to reserve.
  * You can change the quantity of GPUs and Local SSD disks that is attached per VM as long as the total quantity of reserved GPUs and Local SSD disks remains the same.
  * You can specify your replaced reservations to be either single-project (also called _local_ on the Google Cloud console) or shared reservations.



### Requirements

When you replace your commitment's attached reservation with a new one, your request must meet all of the following requirements:

  * You can replace only one attached reservation at a time with exactly one new attached reservation. To replace an attached reservation, simultaneously remove an existing attached reservation by setting its VM count to 0 and define a new attached reservation that you want to replace it.
  * The new reservation must exist in the same project as the commitment.
  * The new reservation must be located in the same zone as the removed reservation.
  * The amount and types of GPUs specified in the new reservation must match the removed reservation.
  * The numbers and types of Local SSD disks specified in the new reservation must match the removed reservation.
  * You can only change up to 100 VMs per request. To make a change that involves more than 100 VMs, divide the change into multiple smaller requests or reach out to Google Cloud Support.



Your request to replace a reservation also depends on the capacity availability at that time. If the capacity for a request is unavailable, then the request fails and returns a resource availability error, which you can try to resolve by modifying or postponing the request. For more information, see the documentation for [troubleshooting resource availability](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-creation#resource-availability). 

If your request to replace an attached reservation fails, then the attached reservation and your existing reserved resources remain unaffected. To preserve your capacity, wait to make any corresponding changes to your VMs until after your request to replace a reservation is successful.

### Steps to replace an attached reservation

You can replace a commitment's reservations using the Google Cloud CLI or REST.

### gcloud

To replace reservations that are attached to commitments, do the following:

  1. Create a YAML file in the current directory with the configurations of the following attached reservations:

     * The current reservation that you want to replace.

To retrieve the details of this reservation, see [View details of a reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-view#describe-reservations).

     * The new replacement reservation.

The contents of the YAML file are similar to the following:
    
    - reservation: CURRENT_RESERVATION_NAME
      reservation_zone: CURRENT_RESERVATION_ZONE
      vm_count: 0
      machine_type: CURRENT_RESERVATION_MACHINE_TYPE
      accelerator:
      - count: CURRENT_RESERVATION_NUMBER_OF_ACCELERATORS
        type: CURRENT_RESERVATION_ACCELERATOR_TYPE
      local_ssd:
      - interface: CURRENT_RESERVATION_INTERFACE_1
        size: 375
      - interface: CURRENT_RESERVATION_INTERFACE_2
        size: 375
      project: CURRENT_RESERVATION_PROJECT_ID
      share_setting: CURRENT_RESERVATION_SHARE_SETTING
      share_with:
      - CURRENT_RESERVATION_CONSUMER_PROJECT_ID_1
      - CURRENT_RESERVATION_CONSUMER_PROJECT_ID_2
    - reservation: REPLACEMENT_RESERVATION_NAME
      reservation_zone: REPLACEMENT_RESERVATION_ZONE
      vm_count: REPLACEMENT_RESERVATION_NUMBER_OF_VMS
      machine_type: REPLACEMENT_RESERVATION_MACHINE_TYPE
      accelerator:
      - count: REPLACEMENT_RESERVATION_NUMBER_OF_ACCELERATORS
        type: REPLACEMENT_RESERVATION_ACCELERATOR_TYPE
      local_ssd:
      - interface: REPLACEMENT_RESERVATION_INTERFACE_1
        size: 375
      - interface: REPLACEMENT_RESERVATION_INTERFACE_2
        size: 375
      project: REPLACEMENT_RESERVATION_PROJECT_ID
      share_setting: REPLACEMENT_RESERVATION_SHARE_SETTING
      share_with:
      - REPLACEMENT_RESERVATION_CONSUMER_PROJECT_ID_1
      - REPLACEMENT_RESERVATION_CONSUMER_PROJECT_ID_2
    
    

Replace the following with the corresponding properties of the current and replacement reservations:

### Current reservation

For the current reservation, all of the following properties must be exactly the same as when you viewed the reservation. Omit the fields for any properties that the current reservation doesn't already have.

     * `CURRENT_RESERVATION_NAME`: the name of the current attached reservation.
     * `CURRENT_RESERVATION_ZONE`: the zone of the current attached reservation.
     * `CURRENT_RESERVATION_MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-types) of the current attached reservation.
     * `CURRENT_RESERVATION_NUMBER_OF_ACCELERATORS`: the number of GPUs reserved in the current attached reservation.
     * `CURRENT_RESERVATION_ACCELERATOR_TYPE`: the [type of accelerator](https://docs.cloud.google.com/compute/docs/gpus) reserved in the current attached reservation.
     * `CURRENT_RESERVATION_INTERFACE_1` and `CURRENT_RESERVATION_INTERFACE_2`: the type of interface that the [Local SSD disk](https://docs.cloud.google.com/compute/docs/disks#localssds) for each reserved VM use in the current attached reservation. Valid options are: `scsi` and `nvme`. Each Local SSD disk is 375 GB. Repeat the `local_ssd` parameter for all the reserved Local SSD disks.
     * `CURRENT_RESERVATION_PROJECT_ID`: the project ID of the current project that has the commitment and the attached reservation. Specify this field if your current attached reservation is shared across multiple consumer projects.
     * `CURRENT_RESERVATION_SHARE_SETTING`: The type of sharing for the current reservation. Specify this field with the value as `projects` if your current attached reservation is shared across multiple consumer projects.
     * `CURRENT_RESERVATION_CONSUMER_PROJECT_ID_1` and `CURRENT_RESERVATION_CONSUMER_PROJECT_ID_2`: the [project IDs](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the projects that you share the current attached reservation with, for example `project-1` and `project-2`.

### Replacement reservation

For the replacement reservation, set the following properties as required. Ensure that you meet all the requirements when you specify these properties. Omit any additional fields that you don't want to use.

     * `REPLACEMENT_RESERVATION_NAME`: the name of the new replacement reservation.
     * `REPLACEMENT_RESERVATION_ZONE`: the zone of the new replacement reservation.
     * `REPLACEMENT_RESERVATION_NUMBER_OF_VMS`: the number of VMs that you want to reserve in the new replacement reservation.
     * `REPLACEMENT_RESERVATION_MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-types) that you want for the VMs in your new replacement reservation.

       * For **predefined** machine types, use the format `MACHINE_FAMILY-standard-CPUS`; for example, `n2-standard-4`.
       * For **custom** machine types, use the format `MACHINE_FAMILY-custom-CPUS-MEMORY`; for example `n2-custom-4-5120`. For a full list of restrictions, read the [specifications](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#specifications) for custom machine types.

Replace the following:

       * `MACHINE_FAMILY`: the family of machine types; for example, specify `n2` for N2 VMs.
       * `CPUS`: the number of [vCPUs](https://docs.cloud.google.com/compute/docs/cpu-platforms).
       * `MEMORY`: the total memory for a reserved VM. Memory must be a multiple of 256 MB and must be supplied in MB; for example, to create an N2 VM with 4 vCPUs and 5 GB of memory, which is 5120 MB, use `n2-custom-4-5120`.
     * `REPLACEMENT_RESERVATION_NUMBER_OF_ACCELERATORS`: the number of GPUs that you want to add, per VM, in the replacement reservation.

     * `REPLACEMENT_RESERVATION_ACCELERATOR_TYPE`: the [type of accelerator](https://docs.cloud.google.com/compute/docs/gpus) that you want to add in the replacement reservation.

     * `REPLACEMENT_RESERVATION_INTERFACE_1` and `REPLACEMENT_RESERVATION_INTERFACE_2`: the type of interface that you want the [Local SSD disks](https://docs.cloud.google.com/compute/docs/disks#localssds) for each reserved VM to use. Valid options are: `scsi` and `nvme`. Each Local SSD disk is 375 GB. Repeat the `local_ssd` parameter for each Local SSD disk that you want to add. You can specify up to 24 Local SSD disks.

     * `REPLACEMENT_RESERVATION_PROJECT_ID`: the project ID of the current project that has the commitment and the attached reservation. Specify this field if you want to share your replacement reservation across multiple consumer projects.

     * `REPLACEMENT_RESERVATION_SHARE_SETTING`: the type of sharing for the replacement reservation. Specify this field with the value as `projects` if you want to share your replacement reservation across multiple consumer projects.

     * `REPLACEMENT_RESERVATION_CONSUMER_PROJECT_ID_1` and `REPLACEMENT_RESERVATION_CONSUMER_PROJECT_ID_2`: the [project IDs](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the projects that can share this reservation, for example `project-1,project-2`. You can include up to 100 consumer projects. These projects must be in the same organization as the owner project. Don't include the `REPLACEMENT_RESERVATION_PROJECT_ID`, which is already allowed to consume this reservation by default.

  2. Run the [`gcloud beta compute commitments update-reservations`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/commitments/update-reservations) command and specify the path to the YAML file using the `--reservations-from-file` flag.
         
         gcloud beta compute commitments update-reservations COMMITMENT_NAME \
             --project=PROJECT_ID \
             --region=REGION \
             --reservations-from-file=YAML_FILE
         

Replace the following:

     * `COMMITMENT_NAME`: the name of the commitment with the attached reservation.
     * `PROJECT_ID`: the project ID of the commitment with the attached reservation.
     * `REGION`: The region where the commitment is located.
     * `YAML_FILE`: The path to the YAML file that contains the configuration of the current and replacement reservations.



### Example for replacing a reservation that is attached to a commitment

To demonstrate this, this section shows an example commitment with an attached reservation and how to replace the example attached reservation.

#### Example commitment with an attached reservation

For example, suppose that you want to update the attached reservations for the `my-commitment-with-reservations` commitment, that was purchased using the following command:
    
    
      gcloud beta compute commitments create my-commitment-with-reservations \
          --region=asia-east1 \
          --resources=vcpu=16,memory=60GB,local-ssd=3000 \
          --resources-accelerator=type=nvidia-tesla-v100,count=4 \
          --plan=12-month \
          --type=general-purpose \
          --reservations-from-file=one-reservation.yaml
    

For this example, suppose that when this command was run, `one-reservation.yaml` was a file in the current directory with the following contents, that define an attached reservation named `res-1`.
    
    
      - reservation: res-1
        reservation_zone: asia-east1-a
        vm_count: 4
        machine_type: n1-standard-4
        accelerator:
        - count: 1
          type: nvidia-tesla-v100
        local_ssd:
        - interface: scsi
          size: 375
        - interface: scsi
          size: 375
    

This `my-commitment-with-reservations` commitment and the attached reservation `res-1` resulted in the following committed and reserved resources:

Resource type | Resources in commitment  
(`my-commitment-with-reservations`) | Resources in current attached reservation  
(`res-1`)  
---|---|---  
vCPUs and memory | 16 vCPUs and 60 GB | 16 vCPUs and 60 GB  
(4 reserved `n1-standard-4` VMs)*  
GPUs | 4 V100 GPUs | 4 V100 GPUs   
(1 V100 GPU per VM, for 4 VMs)*  
Local SSD disks | 3000 GB or 8 Local SSD disks | 3000 GB or 8 Local SSD disks   
(750 GB or 2 Local SSD disks per VM, for 4 VMs)*  
  
*Specifically, the example attached reservation, `res-1`, reserves 4 `n1-standard-4` VMs, each with 1 V100 GPU and 2 Local SSD disks of `scsi` interface type. The `n1-standard-4` [machine type](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines) uses 4 vCPUs and 15 GB for each VM.

#### Replace the example attached reservation

Suppose that you want to replace the attached reservation `res-1` for the commitment with a new attached reservation `res-2` and change the reserved resources to the following:

Resource type | Resources in commitment  
(`my-commitment-with-reservations`) | Resources in current attached reservation  
(`res-1`) | Resources in replacement attached reservation  
(`res-2`)  
---|---|---|---  
vCPUs and memory | 16 vCPUs and 60 GB | 16 vCPUs and 60 GB  
(4 reserved `n1-standard-4` VMs)* | 16 vCPUs and 60 GB  
(2 reserved and shared `n1-standard-8` VMs)†  
GPUs | 4 V100 GPUs | 4 V100 GPUs  
(1 V100 GPU per VM, for 4 VMs)* | 4 V100 GPUs  
(2 V100 GPUs per VM, for 2 VMs)†  
Local SSD disks | 3000 GB or 8 Local SSD disks | 3000 GB or 8 Local SSD disks   
(750 GB or 2 Local SSD disks per VM, for 4 VMs)* | 3000 GB or 8 Local SSD disks   
(1500 GB or 4 Local SSD disks per VM, for 2 VMs)*  
  
*Specifically, the example attached reservation, `res-1`, reserves 4 `n1-standard-4` VMs, each with 1 V100 GPU and 2 Local SSD disks of `scsi` interface type. The `n1-standard-4` [machine type](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines) uses 4 vCPUs and 15 GB for each VM.

†Specifically, the replacement attached reservation defines `res-2`, which reserves 2 `n1-standard-8` VMs, each with 2 V100 GPUs and 4 Local SSD disks of `scsi` interface type. Also, `res-2` is shared with 2 other projects, `project-1` and `project-2` and owned by the current project, `my-project`. The `n1-standard-8` machine type uses 8 vCPUs and 30 GB for each VM.

To replace the attached reservation `res-1` with `res-2` for the `my-commitment-with-reservations` commitment, do the following:

  1. Create a file named `two-reservations.yaml` in the current directory that contains the following contents:
         
         - reservation: res-1
           reservation_zone: asia-east1-a
           vm_count: 0
           machine_type: n1-standard-4
           accelerator:
           - count: 1
             type: nvidia-tesla-v100
           local_ssd:
           - interface: scsi
             size: 375
           - interface: scsi
             size: 375
         - reservation: res-2
           reservation_zone: asia-east1-a
           vm_count: 2
           machine_type: n1-standard-8
           accelerator:
           - count: 2
             type: nvidia-tesla-v100
           project: my-project
           share_setting: projects
           share_with:
           - project-1
           - project-2
           local_ssd:
           - interface: scsi
             size: 375
           - interface: scsi
             size: 375
           - interface: scsi
             size: 375
           - interface: scsi
             size: 375
         

  2. Run the following command:
         
         gcloud beta compute commitments update-reservations my-commitment-with-reservations \
             --region=asia-east1 \
             --reservations-from-file=two-reservations.yaml
         




###  REST 

To replace reservations that are attached to commitments, make a `POST` request using the [`regionCommitments.updateReservations`](https://docs.cloud.google.com/compute/docs/reference/rest/beta/regionCommitments/updateReservations) method.
    
    
    POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/COMMITMENT_REGION/commitments/COMMITMENT_NAME/updateReservations
    
    {
      "reservations":
      [
        {
          "name": "REPLACEMENT_RESERVATION_NAME",
          "specificReservation":
          {
            "count": "REPLACEMENT_RESERVATION_NUMBER_OF_VMS",
            "instanceProperties":
            {
              "guestAccelerators":
              [
                {
                  "acceleratorCount": "REPLACEMENT_RESERVATION_NUMBER_OF_ACCELERATORS",
                  "acceleratorType": "REPLACEMENT_RESERVATION_ACCELERATOR_TYPE"
                }
              ],
              "localSsds":
              [
                {
                  "diskSizeGb": "375",
                  "interface": "REPLACEMENT_RESERVATION_INTERFACE_1"
                },
                {
                  "diskSizeGb": "375",
                  "interface": "REPLACEMENT_RESERVATION_INTERFACE_2"
                }
              ],
              "machineType": "REPLACEMENT_RESERVATION_MACHINE_TYPE"
    
            }
          },
          "zone": "REPLACEMENT_RESERVATION_ZONE",
          "shareSettings":
          {
            "shareType": "SPECIFIC_PROJECTS",
            "projectMap":
            {
              "REPLACEMENT_RESERVATION_CONSUMER_PROJECT_ID_1":
              {
                "projectId": "REPLACEMENT_RESERVATION_CONSUMER_PROJECT_ID_1"
              },
              "REPLACEMENT_RESERVATION_CONSUMER_PROJECT_ID_2":
              {
                "projectId": "REPLACEMENT_RESERVATION_CONSUMER_PROJECT_ID_2"
              }
             }
          }
        },
        {
          "name": "CURRENT_RESERVATION_NAME",
          "specificReservation":
          {
            "count": "0",
            "instanceProperties":
            {
              "guestAccelerators":
              [
                {
                  "acceleratorCount": "CURRENT_RESERVATION_NUMBER_OF_ACCELERATORS",
                  "acceleratorType": "CURRENT_RESERVATION_ACCELERATOR_TYPE"
                }
              ],
              "localSsds":
              [
                {
                  "diskSizeGb": "375",
                  "interface": "CURRENT_RESERVATION_INTERFACE_1"
                },
                {
                  "diskSizeGb": "375",
                  "interface": "CURRENT_RESERVATION_INTERFACE_2"
                }
              ],
              "machineType": "CURRENT_RESERVATION_MACHINE_TYPE"
    
            }
          },
          "zone": "CURRENT_RESERVATION_ZONE",
          "shareSettings":
          {
            "shareType": "SPECIFIC_PROJECTS",
            "projectMap":
            {
              "CURRENT_RESERVATION_CONSUMER_PROJECT_ID_1":
              {
                "projectId": "CURRENT_RESERVATION_CONSUMER_PROJECT_ID_1"
              },
              "CURRENT_RESERVATION_CONSUMER_PROJECT_ID_2":
              {
                "projectId": "CURRENT_RESERVATION_CONSUMER_PROJECT_ID_2"
              }
             }
          }
        }
      ]
    }
    

Replace the following with the corresponding properties of the commitment, the current reservation, and the replacement reservation:

### Commitment

  * `COMMITMENT_NAME`: the name of the commitment with the attached reservation.
  * `PROJECT_ID`: the project ID of the commitment with the attached reservation. This is also the project ID for the current and attached reservations.
  * `COMMITMENT_REGION`: the region of the commitment with the attached reservation.



### Current reservation

For the current reservation, all of the following properties must be exactly the same as when you viewed the reservation. Omit the fields for any properties that the current reservation doesn't already specify.

  * `CURRENT_RESERVATION_NAME`: the name of the current attached reservation.
  * `CURRENT_RESERVATION_ZONE`: the zone of the current attached reservation.
  * `CURRENT_RESERVATION_MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-types) of the current attached reservation.
  * `CURRENT_RESERVATION_NUMBER_OF_ACCELERATORS`: the number of GPUs reserved in the current attached reservation.
  * `CURRENT_RESERVATION_ACCELERATOR_TYPE`: the [type of accelerator](https://docs.cloud.google.com/compute/docs/gpus) reserved in the current attached reservation.
  * `CURRENT_RESERVATION_INTERFACE_1` and `CURRENT_RESERVATION_INTERFACE_2`: the type of interface that the [Local SSD disks](https://docs.cloud.google.com/compute/docs/disks#localssds) for each reserved VM use in the current attached reservation. Valid options are: `scsi` and `nvme`. Each Local SSD disk is 375 GB. Repeat the `localSsds` parameter for all the reserved Local SSD disks.
  * `CURRENT_RESERVATION_SHARE_SETTING`: The type of sharing for the current reservation. Specify this parameter with the value as `projects` if your current attached reservation is shared across multiple consumer projects.
  * `CURRENT_RESERVATION_CONSUMER_PROJECT_ID_1` and `CURRENT_RESERVATION_CONSUMER_PROJECT_ID_2`: the [project IDs](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the projects that you share the current attached reservation with, for example `project-1` and `project-2`.



### Replacement reservation

For the replacement reservation, set the following properties as required. Ensure that you meet all the requirements when you specify these properties. Omit any additional fields that you don't want to use.

  * `REPLACEMENT_RESERVATION_NAME`: the name of the new replacement reservation.
  * `REPLACEMENT_RESERVATION_ZONE`: the zone of the new replacement reservation.
  * `REPLACEMENT_RESERVATION_NUMBER_OF_VMS`: the number of compute instances that you want to reserve in the new replacement reservation.
  * `REPLACEMENT_RESERVATION_MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-types) that you want for the compute instances in your new replacement reservation.

    * For **predefined** machine types, use the format `MACHINE_FAMILY-standard-CPUS`; for example, `n2-standard-4`.
    * For **custom** machine types, use the format `MACHINE_FAMILY-custom-CPUS-MEMORY`; for example `n2-custom-4-5120`. For a full list of restrictions, read the [specifications](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#specifications) for custom machine types.

Replace the following:

    * `MACHINE_FAMILY`: the family of machine types; for example, specify `n2` for N2 compute instances.
    * `CPUS`: the number of [vCPUs](https://docs.cloud.google.com/compute/docs/cpu-platforms).
    * `MEMORY`: the total memory for a reserved VM. Memory must be a multiple of 256 MB and must be supplied in MB; for example, to create an N2 VM with 4 vCPUs and 5 GB of memory, which is 5120 MB, use `n2-custom-4-5120`.
  * `REPLACEMENT_RESERVATION_NUMBER_OF_ACCELERATORS`: the number of GPUs that you want to add, per VM, in the replacement reservation.

  * `REPLACEMENT_RESERVATION_ACCELERATOR_TYPE`: the [type of accelerator](https://docs.cloud.google.com/compute/docs/gpus) that you want to add in the replacement reservation.

  * `REPLACEMENT_RESERVATION_INTERFACE_1` and `REPLACEMENT_RESERVATION_INTERFACE_2`: the type of interface that you want the [Local SSD disks](https://docs.cloud.google.com/compute/docs/disks#localssds) for each reserved VM to use. Valid options are: `scsi` and `nvme`. Each Local SSD disk is 375 GB. Repeat the `localSsds` parameter for each Local SSD disk that you want to add. You can specify up to 24 Local SSD disks.

  * `REPLACEMENT_RESERVATION_SHARE_SETTING`: The type of sharing for the replacement reservation. Specify this parameter with the value as `projects` if you want to share your replacement reservation across multiple consumer projects.

  * `REPLACEMENT_RESERVATION_CONSUMER_PROJECT_ID_1` and `REPLACEMENT_RESERVATION_CONSUMER_PROJECT_ID_2`: the [project IDs](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the projects that can share this reservation, for example `project-1,project-2`. You can include up to 100 consumer projects. These projects must be in the same organization as the owner project. Don't include the `PROJECT_ID`, which is already allowed to consume this reservation by default.




### Example for replacing a reservation that is attached to a commitment

To demonstrate this, this section shows an example commitment with an attached reservation and how to replace the example attached reservation.

#### Example commitment with an attached reservation

For example, suppose that you want to replace the attached reservation `res-1` for the `my-commitment-with-reservations` commitment, that was purchased by making the following `POST` request:
    
    
      POST https://compute.googleapis.com/compute/beta/projects/my-project/regions/asia-east1/commitments
    
      {
        "name": "my-commitment-with-reservations",
        "plan": "TWELVE_MONTH",
        "reservations":
        [
          {
            "name": "res-1",
            "specificReservation":
            {
              "count": "4",
              "instanceProperties":
              {
                "guestAccelerators":
                [
                  {
                    "acceleratorCount": "1",
                    "acceleratorType": "nvidia-tesla-v100"
                  }
                ],
                "localSsds":
                [
                  {
                    "diskSizeGb": "375",
                    "interface": "scsi"
                  },
                  {
                    "diskSizeGb": "375",
                    "interface": "scsi"
                  }
                ],
                "machineType": "n1-standard-4"
              }
            },
            "zone": "asia-east1-a"
          }
        ],
        "resources":
        [
          {
            "amount": "16",
            "type": "VCPU"
          },
          {
            "amount": "61440",
            "type": "MEMORY"
          },
          {
            "acceleratorType": "nvidia-tesla-v100",
            "amount": "4",
            "type": "ACCELERATOR"
          },
          {
            "amount": "3072000",
            "type": "LOCAL_SSD"
          }
        ],
        "type": "GENERAL_PURPOSE"
      }
    

This `my-commitment-with-reservations` commitment and the attached reservation `res-1` resulted in the following committed and reserved resources:

Resource type | Resources in commitment  
(`my-commitment-with-reservations`) | Resources in current attached reservation  
(`res-1`)  
---|---|---  
vCPUs and memory | 16 vCPUs and 60 GB | 16 vCPUs and 60 GB  
(4 reserved `n1-standard-4` VMs)*  
GPUs | 4 V100 GPUs | 4 V100 GPUs   
(1 V100 GPU per VM, for 4 VMs)*  
Local SSD disks | 3000 GB or 8 Local SSD disks | 3000 GB or 8 Local SSD disks   
(750 GB or 2 Local SSD disks per VM, for 4 VMs)*  
  
*Specifically, the example attached reservation, `res-1`, reserves 4 `n1-standard-4` VMs, each with 1 V100 GPU and 2 Local SSD disks of `scsi` interface type. The `n1-standard-4` [machine type](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines) uses 4 vCPUs and 15 GB for each VM.

#### Replace the example attached reservation

Suppose that you want to replace the attached reservation `res-1` for the commitment with a new attached reservation `res-2` and change the reserved resources to the following:

Resource type | Resources in commitment  
(`my-commitment-with-reservations`) | Resources in current attached reservation  
(`res-1`) | Resources in replacement attached reservation  
(`res-2`)  
---|---|---|---  
vCPUs and memory | 16 vCPUs and 60 GB | 16 vCPUs and 60 GB  
(4 reserved `n1-standard-4` VMs)* | 16 vCPUs and 60 GB  
(2 reserved and shared `n1-standard-8` VMs)†  
GPUs | 4 V100 GPUs | 4 V100 GPUs  
(1 V100 GPU per VM, for 4 VMs)* | 4 V100 GPUs  
(2 V100 GPUs per VM, for 2 VMs)†  
Local SSD disks | 3000 GB or 8 Local SSD disks | 3000 GB or 8 Local SSD disks   
(750 GB or 2 Local SSD disks per VM, for 4 VMs)* | 3000 GB or 8 Local SSD disks   
(1500 GB or 4 Local SSD disks per VM, for 2 VMs)*  
  
*Specifically, the example attached reservation, `res-1`, reserves 4 `n1-standard-4` VMs, each with 1 V100 GPU and 2 Local SSD disks of `scsi` interface type. The `n1-standard-4` [machine type](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines) uses 4 vCPUs and 15 GB for each VM.

†Specifically, the replacement attached reservation defines `res-2`, which reserves 2 `n1-standard-8` VMs, each with 2 V100 GPUs and 4 Local SSD disks of `scsi` interface type. Also, `res-2` is shared with 2 other projects, `project-1` and `project-2` and owned by the current project, `my-project`. The `n1-standard-8` machine type uses 8 vCPUs and 30 GB for each VM.

To replace the attached reservation `res-1` with `res-2` for the `my-commitment-with-reservations` commitment, make the following `POST` request by using the [`regionCommitments.updateReservations`](https://docs.cloud.google.com/compute/docs/reference/rest/beta/regionCommitments/updateReservations) method:
    
    
      POST https://compute.googleapis.com/compute/beta/projects/my-project/regions/asia-east1/commitments/my-commitment-with-reservations/updateReservations
    
      {
        "reservations":
        [
          {
            "name": "res-2",
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
                "localSsds":
                [
                  {
                    "diskSizeGb": "375",
                    "interface": "scsi"
                  },
                  {
                    "diskSizeGb": "375",
                    "interface": "scsi"
                  },
                  {
                    "diskSizeGb": "375",
                    "interface": "scsi"
                  },
                  {
                    "diskSizeGb": "375",
                    "interface": "scsi"
                  }
                ],
                "machineType": "n1-standard-8"
              }
            },
            "zone": "asia-east1-a"
          },
          {
            "name": "res-1",
            "specificReservation":
            {
              "count": "0",
              "instanceProperties":
              {
                "guestAccelerators":
                [
                  {
                    "acceleratorCount": 1,
                    "acceleratorType": "nvidia-tesla-v100"
                  }
                ],
                "localSsds":
                [
                  {
                    "diskSizeGb": "375",
                    "interface": "scsi"
                  },
                  {
                    "diskSizeGb": "375",
                    "interface": "scsi"
                  }
                ],
                "machineType": "n1-standard-4"
              }
            },
            "zone": "asia-east1-a"
          }
        ]
      }
    

## What's next

  * Learn more about [resource-based CUDs](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts).
  * Learn how to [consume reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-consume).
  * Learn how to [modify reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-modify).
  * Learn how to [delete reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-delete).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
