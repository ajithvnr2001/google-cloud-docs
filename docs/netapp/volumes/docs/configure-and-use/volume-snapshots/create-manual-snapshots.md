---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/create-manual-snapshots/
title: Create a manual volume snapshot \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:19.059584+00:00
---

# Create a manual volume snapshot  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/create-manual-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Create a manual volume snapshot Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to create a manual volume snapshot.

## Create a manual snapshot

Use the following instructions to create a manual snapshot using the Google Cloud console or Google Cloud CLI or ONTAP-mode.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Select the volume you want to create a snapshot for.

  4. Click **Create snapshot**.

  5. For the **Create a snapshot** dialog, complete the following steps:

     1. Enter a name in the **Name** field for the snapshot.

     2. Optional: Add a description in the **Description** field.

     3. Optional: under the **Labels** section, click **Add label** to enter relevant labels for reporting and querying purposes.




### gcloud

Run the following command to create a snapshot:
    
    
    gcloud netapp volumes snapshots create NAME \
      --project=PROJECT_ID \
      --location=LOCATION \
      --volume=VOLUME_NAME

Replace the following information:

  * `NAME`: the name of the snapshot you want to create. This name must be unique for each volume.

  * `PROJECT_ID`: the name of the project that you intend to create the snapshot in.

  * `LOCATION`: the location that you want to create the snapshot in.

  * `VOLUME`: the name of the volume you want to snapshot.




For more information about additional optional flags, see [Google Cloud SDK documentation for NetApp Volumes volume snapshots](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots).

### ONTAP-mode

Identify the required ONTAP commands in the [ONTAP documentation](https://docs.netapp.com/us-en/ontap/).

For example, see [Volume snapshot create](https://docs.netapp.com/us-en/ontap-cli//volume-snapshot-create.html#description).

After you identify the required commands, see [ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview) for instructions about how to submit ONTAP commands to the storage pool.

## What's next

[Manage volume snapshots](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/manage-snapshots).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
