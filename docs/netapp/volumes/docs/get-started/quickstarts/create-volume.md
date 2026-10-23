---
url: https://docs.cloud.google.com/netapp/volumes/docs/get-started/quickstarts/create-volume/
title: Create a volume quickstart \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:29.311485+00:00
---

# Create a volume quickstart  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/get-started/quickstarts/create-volume/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Create a volume quickstart Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to create a volume. These volume instructions aren't applicable to the Flex Unified ONTAP-mode.

## Before you begin

For this quickstart, we recommend that you create your first volume with the NFSv3 protocol type. If you only want to use SMB volumes, you can delete the NFSv3 volume after you complete this quickstart.

## Create a volume

Use the following instructions to create a volume:

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Enter a **volume name**.

  4. Optional: Add a description in the **Description** field.

  5. Enter a **share name**. The share name corresponds to the export path for an NFS volume.

  6. Select the **Volume type**.

  7. Enter the **capacity** of the volume.

  8. Select the **protocol**.

  9. Add an **export rule**.

  10. Click **Create**.




The first volume creation takes a few minutes. The creation of each subsequent volume takes a few seconds.

## Clean up

Use the following instructions to delete a volume:

  1. Go to the **NetApp Volumes page** in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Select the volume you want to delete and select **Delete**.

  4. To confirm deletion, type the name of the volume.

  5. Click **Delete**.

The volume and its contents are deleted.




## What's next

Use the quickstart guide for how to [mount the volume on a client](https://docs.cloud.google.com/netapp/volumes/docs/get-started/quickstarts/mount-volume).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
