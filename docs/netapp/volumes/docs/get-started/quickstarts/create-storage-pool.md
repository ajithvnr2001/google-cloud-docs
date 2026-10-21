---
url: https://docs.cloud.google.com/netapp/volumes/docs/get-started/quickstarts/create-storage-pool/
title: Create a storage pool quickstart \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:27.731507+00:00
---

# Create a storage pool quickstart  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/get-started/quickstarts/create-storage-pool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Create a storage pool quickstart Stay organized with collections  Save and categorize content based on your preferences. 

This quickstart describes how to create a [storage pool](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/overview#about_storage_pools).

## Before you begin

Ensure that you've completed the following steps before you use NetApp Volumes:

  1. Set up a [project in Google Cloud console](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/initiate-console-settings).

  2. [Configure networking](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/networking).

  3. Assign NetApp Volumes [Identity and Access Management permissions](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/iam).




If you plan to explore multiple tutorials and quickstarts, reusing projects can help you avoid exceeding project quota limits.

## Considerations

This quickstart guide assumes you intend to use NFS volumes to create a storage pool. If you want to use SMB volumes, you need to select and define an Active Directory policy before you can proceed, see [Create an Active Directory policy](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/create-ad-policy).

## Create a storage pool

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Storage pools**.

  3. Click **Create**.

  4. In the **Storage pool details** section, complete the following actions:

     1. Enter a name in the **Name** field for your storage pool. The name must be unique for each project.

     2. Optional: add a description for the pool in the **Description** field.

  5. Select a **location** for the pool.

  6. Select a **service level**.

**Important:** Effective September 15, 2026, you can't create new Flex File storage pools, but existing pools remain supported. For more information, see [Migration to Flex Unified service level](https://docs.cloud.google.com/netapp/volumes/docs/get-started/migration-to-flex-unified).
     * **Flex Unified**

Choose either Default-mode or ONTAP-mode when provisioning your pool. For more information, see [Flex Unified: Default-mode versus ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/discover/features#flex_unified_default-mode_versus_ontap-mode).

     * **Flex File**

     * **Standard**

     * **Premium**

     * **Extreme**

For the Flex Unified and Flex File service level, you can choose between zonal or regional availability. For zonal availability, you need to specify the zone to use. For regional availability, you need to specify a primary zone and a replica zone.

  7. Optional: for all Flex Unified pools or regions which support Flex zonal custom performance, complete the following steps in the **Performance** section:

     1. Enter the throughput for the storage pool in the **Throughput** field.

     2. Enter the IOPS for the storage pool in the **IOPS** field.

  8. Enter the capacity for the storage pool in the **Capacity** field.

  9. In the **Set up connections** section, select the **VPC** you want to use. If you haven't peered your VPC, click **Set up connection** and complete the following steps:

     1. Enable the **Service networking API**.

     2. Click **Use an automatically allocated IP range** or click **Select one or more existing IP ranges or create a new one** to manually choose a CIDR. Before you choose a CIDR, review the [network considerations](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/networking#considerations) because you can't change this setting once volumes use it.

     3. Review your selections.

     4. Click **Create connection**.

  10. Disable the **Assign an Active Directory policy to the storage pool** checkbox.

  11. Leave the defaulted encryption to Google-owned and Google-managed encryption key as is.

  12. Optional: in the **Labels** section, click **Add label** to enter relevant labels for reporting and querying purposes.




## Clean up

Use the following instructions to delete a storage pool:

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Storage pools**.

  3. Select the storage pool you want to delete.

  4. Click **Delete**.

  5. To confirm deletion, enter the name of the storage pool.

  6. Click **Delete**.

The storage pool and its contents are deleted.




## What's next

Read the quickstart guide for how to [create a volume](https://docs.cloud.google.com/netapp/volumes/docs/get-started/quickstarts/create-volume).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
