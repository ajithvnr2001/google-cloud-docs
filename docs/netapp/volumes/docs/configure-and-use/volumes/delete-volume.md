---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/delete-volume/
title: Delete a volume \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:50.022303+00:00
---

# Delete a volume  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/delete-volume/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)



Send feedback 

#  Delete a volume Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to delete a volume.

## Before you begin

When you delete a volume, all of the data and volume snapshots within the volume get deleted and the capacity of the pool returns. Before you delete a volume, you must [delete the replication relationship](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/delete-replication).

## Delete a volume

Use the following instructions to delete a volume using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Identify the volume you want to delete.

  3. Click the more_vert **Show more** icon on the volume and click **Delete**.

  4. A confirmation dialog appears. Read through the warnings.

  5. To proceed, enter the name of the volume and click **Delete**.




### gcloud

Run the following command:
    
    
      gcloud netapp volumes delete VOLUME_NAME \
       --project=PROJECT_ID \
       --location=LOCATION

Replace the following information:

  * `VOLUME_NAME`: the name of the volume to delete

  * `PROJECT_ID`: the name of the project the volume is in

  * `LOCATION`: The location of the volume




For more information on additional optional flags, see [Google Cloud SDK documentation on volumes](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes).

## What's next

[Manage auto-tiering](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-auto-tiering).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
