---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/delete-snapshot/
title: Delete a snapshot \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:46.560771+00:00
---

# Delete a snapshot  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/delete-snapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Delete a snapshot Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to delete a snapshot.

## Considerations

Consider the following limitations before you delete a snapshot:

  * If you delete a volume, its snapshots delete automatically as well.

  * While snapshots help improve recovery time and point objectives in a backup concept, they don't remove the need to create a second physical copy of the data. For more information, see [Recovery Point Objective (RPO)](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication#recovery_point_objective_rpo).

  * You can delete manual and scheduled snapshots.

  * You can't delete internal snapshots manually.

  * Deletion fails if the last backup was created using the snapshot you want to delete.

  * Deletion fails if an existing snapshot was specified for a manual backup and that instance of the backup is the latest captured backup.

  * For the Flex Unified service level volumes, you can't delete a snapshot until you delete the thin clone that was created from that snapshot.




### Delete a snapshot

Use the following instructions to delete a snapshot using the Google Cloud console or Google Cloud CLI or ONTAP-mode.

### Console

  1. Go to **NetApp Volumes page** in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Select the volume you want to edit.

  4. Click more_vert **Show more**.

  5. Select **Delete**.

  6. To confirm deletion, enter the snapshot name in the **Snapshot name** field.

  7. Click **Delete**.




### gcloud

Run the following command to delete a snapshot:
    
    
     gcloud netapp volumes snapshots delete NAME \
      --project=PROJECT_ID \
      --location=LOCATION \
      --volume=VOLUME_NAME

Replace the following details:

  * `NAME`: the name of the snapshot you want to delete.

  * `PROJECT_ID`: the project ID of the project you created the snapshot in.

  * `LOCATION`: the location of the volume.

  * `VOLUME` the name of the snapshot's volume.




For more options, see [Google Cloud SDK documentation for NetApp Volumes volume snapshots](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots).

### ONTAP-mode

Identify the required ONTAP commands in the [ONTAP documentation](https://docs.netapp.com/us-en/ontap/).

For example, see [Volume snapshot delete](https://docs.netapp.com/us-en/ontap-cli/volume-snapshot-delete.html).

After you identify the required commands, see [ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview) for instructions about how to submit ONTAP commands to the storage pool.

## What's next

Read about [volume reversion](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/revert-volume).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
