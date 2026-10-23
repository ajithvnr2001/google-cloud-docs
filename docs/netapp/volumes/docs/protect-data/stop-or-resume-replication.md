---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/stop-or-resume-replication/
title: Stop or resume a replication \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:54.120229+00:00
---

# Stop or resume a replication  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/stop-or-resume-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Stop or resume a replication Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to stop or resume a replication.

## Stop a replication

When you stop a replication, scheduled replication updates from the source volume to the destination volume pause. The destination volume transitions from read-only to read-write. Both volumes continue to share the latest replication snapshot as a new baseline for later resynchronization.

Although the replication relationship between source and destination volume continues to exist, transfers are paused and the volumes become independent. To re-enable the transfer of changes from source volume to destination volume, [resume the replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/stop-or-resume-replication#resume_replication).

Use the following instructions to stop a replication using either the Google Cloud console or Google Cloud CLI:

### Console

  1. Go to the **NetApp Volumes page** in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Click the source volume. The **Details page** for the volume opens.

  4. Select the **Replication tab**.

  5. Click **Stop**. Depending on the replication transfer status, either stop or force stop:

     * **Mirrored transfer state** : Enter the source volume name and click **Stop**.

     * **Transferring** and **Preparing transfer states** : Enter the source volume name and click **Force stop**. A forced stop is required to stop a replication if a transfer is in progress at that time. Therefore, if you resume the replication later, recent changes may need to be transferred again.

The replication status of the volume changes to **Stopped**. The destination volume becomes writable.




### gcloud

Stop a replication:
    
    
    gcloud netapp volumes replications stop REPLICATION_NAME \
     --project=PROJECT_ID \
     --location=LOCATION \
     --volume=VOLUME

Replace the following information:

  * `REPLICATION_NAME`: the name of the replication you want to stop.

  * `PROJECT_ID`: the name of the project your volume is in.

  * `LOCATION`: the location of the source or destination volume.

  * `VOLUME`: the name of the source or destination volume.




For more options, see [Google Cloud SDK documentation on volume replication](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications).

## Resume a replication

You can resume a stopped replication. When you resume a replication, all the changes to the destination volume are undone and NetApp Volumes re-enables the replication. The destination volume transitions from read-write to read-only, and receives updates from the source volume at the scheduled replication interval again. When you resume a replication relationship, the destination volume reverts back to the latest initial replication snapshot, at which point, the volume replication process starts over.

## Resuming a replication relationship

When you resume a replication relationship, any changes to the destination volume while the replication was stopped are deleted.

## Stopping a replication relationship after initialization

When you stop a replication relationship after you initialized it, you can reverse the direction of the replication by swapping the source and destination volume roles. Any data changes on the destination volume are lost when you resume the replication because the destination volume loses all changes and becomes a replica of the source volume.

## Resume a stopped replication

Use the following instructions to resume a stopped replication using either the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes page** in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Click the name of the source volume. The **Details page** for the volume opens.

  4. Select the **Replication tab**.

  5. Click **Resume**.

  6. In the Resume volume replication dialog, review the warning.

  7. To resume, enter the destination volume name and click **Resume**.

The replication status of the volume changes to **Mirrored**.




### gcloud

Resume a volume replication:
    
    
     gcloud netapp volumes create replications resume REPLICATION_NAME \
       --project=PROJECT_ID \
       --location=LOCATION \
       --volume=VOLUME

Replace the following information:

  * `PROJECT_ID`: the name of the project your volume is in.

  * `LOCATION`: the location of the source or destination volume.

  * `VOLUME`: the name of source or destination volume.




For more options, see [Google Cloud SDK documentation on volume replication](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications).

## What's next

[Reverse and resume a replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/reverse-and-resume-replication)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
