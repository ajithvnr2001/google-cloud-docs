---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/create-volume-replication/
title: Create a volume replication \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:34.537784+00:00
---

# Create a volume replication  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/create-volume-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Create a volume replication Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions on how to create a volume replication.

Replications are managed in the Google Cloud NetApp Volumes **Volume details** page in the Google Cloud console. When you replicate a volume, it creates a destination volume in an existing pool in the destination location.

## Create a volume replication

Use the following instructions to create a volume replication using either the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Click the name of the volume you want to replicate.

The **Details page** for the volume opens.

  4. Select the **Replication tab**. If the volume is part of a replication, details of the replication appear.




**Select an existing storage pool or create a new one** :

To select an existing storage pool for the destination volume:

  1. Click **Select storage pool**.

  2. In the Storage pools dialog, select the destination pool and click **Select**. You return to the **Replication tab** of the source volume details view. Details of the selected pool appear.




To create a new storage pool in a [supported destination region](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication#considerations_for_volume_replication):

  1. Follow the steps in [Create a storage pool](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/create-storage-pool).

  2. After creating the storage pool, go back and select the volume for replication, then select the pool you just created.

  3. Click **Next**.




**Fill out the volume replication dialog box** :

  1. In the **Create a volume replication** dialog, complete the following steps:

     1. Review the source volume details.

     2. Click **Next**.

     3. Configure replication details:

        1. Enter a location-specific unique name for the replication.

        2. Optional: add a description in the **Description** field.

        3. Select a [**replication schedule**](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication#replication_schedule).

        4. Optional: under the **Labels** section, click **Add label** to add labels for the replication resource.

     4. Click **Next**.




**Configure destination volume details** :

  1. Configure destination volume details. Note that the destination volume inherits all settings from the source volume except the ones you must specify:

     1. Review the following details of the destination pools:

        * Location

        * Pool

        * Protocol

        * Active Directory settings

  2. Enter a name for the destination volume.

     1. Optional: add a description in the **Description** field for the destination volume.

     2. Enter a share name. We strongly recommend that you use the same share name as the source volume, since it eases building disaster recovery concepts on top of volume replication.

     3. Optional: under the **Labels** section, click **Add label** to add labels for the destination volume.

  3. Optional: select the **Enable auto-tiering** checkbox to enable auto-tiering for the volume.

**Note:** This option is available only if [auto-tiering is already enabled](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/overview#auto-tiering) on the storage pools of the destination volume.
     1. Specify a cooling threshold between 7 to 183 days in the **Cooling threshold days** field.
  4. Click **Create**.




### gcloud

Create a new volume replication using the following command:
    
    
       gcloud netapp volumes replications create REPLICATION_NAME \
          --project=PROJECT_ID \
          --location=LOCATION \
          --volume=SOURCE_VOLUME_NAME \
          --replication-schedule=REPLICATION_SCHEDULE \
          --destination-volume-parameters=share_name=SHARE_NAME,storage_pool=STORAGE_POOL,volume_id=DESTINATION_VOLUME_NAME,description=DESCRIPTION

Replace the following information:

  * `REPLICATION_NAME`: the name of the replication to create.

  * `PROJECT_ID`: the name of the project you want to create the new volume replication in.

  * `LOCATION`: the location you want to create the new replication in.

  * `SOURCE_VOLUME_NAME`: the name of the source volume.

  * `REPLICATION_SCHEDULE`: the schedule for the replication. The value must be either one of `EVERY_10_MINUTES`, `HOURLY` or `DAILY`.

  * `SHARE_NAME`: the share name.

  * `STORAGE_POOL`: the resource name of the storage pool you want to create the new volume replication in the following format:

`projects/<projectID>/locations/<region>/storagePools/<poolName>`

For allow-listed projects, you can specify a different project using `projectID` for Standard, Premium, and Extreme volumes.

  * `DESTINATION_VOLUME_NAME`: the name of the destination volume to create.

  * `DESCRIPTION`: Optional: the description for the new volume.




For more options, see [Google Cloud SDK documentation on volume replication](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications/create).

An initial transfer begins and can take up to a few days depending on the amount of data in the source volume. Charges incurred for the amount of data that transfers. After the initial transfer completes, the destination volume is in a replicated state and you can mount it safely for read-only operations. Only changed blocks can replicate to the destination volume in subsequent replication actions.

## What's next

[Manage volume replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/manage-replication).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
