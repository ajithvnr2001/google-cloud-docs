---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/revert-volume-instructions/
title: Revert a volume from a snapshot \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:26:06.469502+00:00
---

# Revert a volume from a snapshot  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/revert-volume-instructions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Revert a volume from a snapshot Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions on how to revert a volume from a snapshot.

## Before you begin

You can perform volume reversion when the volume is online and in use by clients. Reversion can change open files without any notification to the application and cause potential data corruption. To avoid this, we recommend that you stop all critical applications before you perform volume reversion. Reverting takes a few minutes.

## Revert a volume from a snapshot

For volumes in an active replication relationship, only the source volume can be reverted.

Use the following instructions to revert a volume from a snapshot using the Google Cloud console or Google Cloud CLI or ONTAP-mode.

### Console

  1. Go to the **NetApp Volumes page** in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Click more_vert **Show more** to revert the volume.

  4. Select **Revert** to display information about the volume.

  5. Select the snapshot to revert.

  6. Verify the creation of the snapshot.

  7. Click **Revert**.

A dialog appears that displays the timestamp of the snapshot to revert and a list of the newer snapshots that disappear if you proceed with volume reversion.

  8. Enter the volume name in the **Volume name** field to confirm the revert operation.

  9. Click **Revert**.




### gcloud

Revert the volume to a snapshot:
    
    
    gcloud netapp volumes revert VOLUME_NAME \
      --project=PROJECT_ID \
      --location=LOCATION \
      --snapshot=SNAPSHOT

Replace the following information:

  * `VOLUME_NAME`: the name of the volume that you want to revert to a specific snapshot point-in-time.

  * `PROJECT_ID`: the name of the project you want to revert the volume in.

  * `LOCATION`: the location of the volume you want to revert.

  * `SNAPSHOT`: the name of the snapshot used in order to revert the volume.




For more options, see [Google Cloud SDK documentation for NetApp Volumes volume snapshots](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots).

### ONTAP-mode

Identify the required ONTAP commands in the [ONTAP documentation](https://docs.netapp.com/us-en/ontap/).

For example, see [Volume snapshot restore](https://docs.netapp.com/us-en/ontap-cli//volume-snapshot-restore.html).

After you identify the required commands, see [ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview) for instructions about how to submit ONTAP commands to the storage pool.

## What's next

[Create a new volume from a snapshot](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/new-volume-from-snapshot).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
