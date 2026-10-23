---
url: https://docs.cloud.google.com/filestore/docs/create-snapshots/
title: Create a snapshot to preserve the state of your data \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:11.760922+00:00
---

# Create a snapshot to preserve the state of your data  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/create-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Create a snapshot to preserve the state of your data Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to create a snapshot to preserve the state of your Filestore data. To learn more about snapshots, see [Snapshots](https://docs.cloud.google.com/filestore/docs/snapshots).

## Create a snapshot

You can create a snapshot of an instance using one of the following methods:

###  Google Cloud console 

  1. In the Google Cloud console, go to the Filestore instances page.

[Go to the Filestore instances page](https://console.cloud.google.com/filestore/instances)

  2. Click the instance that you want to create a snapshot of.

  3. Click the **Snapshots** tab and then click **Create snapshot**.

  4. For **Snapshot ID** , enter a name for the snapshot. The file share name and snapshot ID can have a combined length of up to 77 characters.

  5. **Optional** : Add a description or labels to the snapshot.

  6. Click **Create**.




###  gcloud CLI 

To create a snapshot of an instance, run the [`instances snapshots create`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/create) command. The `--description` and `--labels` flags are added as optional arguments:
    
    
    gcloud filestore instances snapshots create SNAPSHOT_ID \
        --instance=INSTANCE_ID \
        --instance-location=LOCATION \
        --description="DESCRIPTION" \
        --labels=KEY=VALUE
    

Replace the following:

  * SNAPSHOT_ID with the name that you want to give the snapshot. The file share name and snapshot ID can have a combined length of up to 77 characters. For example, `my-snapshot-1`.
  * INSTANCE_ID with the name of the instance from which you want to create a snapshot. For example, `my-instance-1`.
  * LOCATION with the [zone or region](https://docs.cloud.google.com/filestore/docs/regions#supported_regions) of the instance. For example, `us-east1-b` or `us-central1`, respectively. Note that your instance's [service tier](https://docs.cloud.google.com/filestore/docs/service-tiers#overview) determines whether a zone or region is a valid argument.
  * DESCRIPTION with a description of the snapshot.
  * KEY=VALUE,... with one or more `KEY=VALUE` pairs that you want to include.



#### Example

The following command creates a snapshot of the instance `nfs-server`, which is located in `us-central1`. The snapshot is named `nfs-server-snapshot`.
    
    
    gcloud filestore instances snapshots create nfs-server-snapshot \
        --instance=nfs-server \
        --instance-location=us-central1 \
    

## List, view, update, and delete snapshots

You can list, view, update, and delete snapshots.

###  Google Cloud console 

To manage your snapshots in the Google Cloud console:

  1. Go to the Filestore instances page.

[Go to the Filestore instances page](https://console.cloud.google.com/filestore/instances)

  2. Click the instance ID of the instance that you want to view snapshots of.

  3. Click the **Snapshots** tab.




From the **Snapshots** tab:

  * To see details about a snapshot, click its snapshot ID.
  * To edit a snapshot, click **Edit** in the snapshots details page.
  * To delete a snapshot:


  1. Click the snapshot ID of the snapshot that you want to delete.
  2. Click **Delete**.
  3. When prompted, type the snapshot ID.
  4. Click **Delete**.



###  gcloud CLI 

### List all snapshots in your current project

To view a list of snapshots for an instance, run the [`instances snapshots list`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/list) command:
    
    
    gcloud filestore instances snapshots list \
        --instance=INSTANCE_ID \
        --instance-location=LOCATION
    

Replace the following:

  * INSTANCE_ID with the name of the instance from which you want to create a list of snapshots. For example, `my-instance-1`.
  * LOCATION with the [zone or region](https://docs.cloud.google.com/filestore/docs/regions#supported_regions) of the instance. For example, `us-east1-b` or `us-central1`, respectively. Note that your instance's [service tier](https://docs.cloud.google.com/filestore/docs/service-tiers#overview) determines whether a zone or region is a valid argument.



### View information about a snapshot

To view information about a snapshot, run the [`instances snapshots describe`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/describe) command:
    
    
    gcloud filestore instances snapshots describe SNAPSHOT_ID \
        --instance=INSTANCE_ID \
        --instance-location=LOCATION
    

Replace the following:

  * SNAPSHOT_ID with the name that you want to give the snapshot. For example, `my-snapshot-1`.
  * INSTANCE_ID with the name of the instance from which the snapshot was created. For example, `my-instance-1`.
  * LOCATION with the [zone or region](https://docs.cloud.google.com/filestore/docs/regions#supported_regions) of the instance from which the snapshot was created. For example, `us-east1-b` or `us-central1`, respectively. Note that your instance's [service tier](https://docs.cloud.google.com/filestore/docs/service-tiers#overview) determines whether a zone or region is a valid argument.



### Update a snapshot

To update a snapshot, run the [`instances snapshots update`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/update) command. The `--description` and `--update-labels` flags are added as optional arguments:
    
    
    gcloud filestore instances snapshots update SNAPSHOT_ID \
        --instance=INSTANCE_ID \
        --instance-location=LOCATION \
        --description="NEW-DESCRIPTION" \
        --update-labels=KEY1=VALUE1,KEY2=VALUE2...
    

Replace the following:

  * SNAPSHOT_ID with the name that you want to give the snapshot. For example, `my-snapshot-1`.
  * INSTANCE_ID with the name of the instance from which the snapshot was created. For example, `my-instance-1`.
  * LOCATION with the [zone or region](https://docs.cloud.google.com/filestore/docs/regions#supported_regions) of the instance from which the snapshot was created. For example, `us-east1-b` or `us-central1`, respectively. Note that your instance's [service tier](https://docs.cloud.google.com/filestore/docs/service-tiers#overview) determines whether a zone or region is a valid argument.
  * NEW-DESCRIPTION with a new description of the snapshot.
  * KEY1=VALUE1,... with one or more `KEY=VALUE` pairs that you want to update. If a label exists, its value is updated, otherwise a new label is created.



### Delete a snapshot

Snapshot deletion is a long running operation that can take multiple hours to complete, depending the number of files involved.

To delete a snapshot, run the [`instances snapshots delete`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/delete) command:
    
    
    gcloud filestore instances snapshots delete SNAPSHOT_ID \
        --instance=INSTANCE_ID \
        --instance-location=LOCATION \
    

Replace the following:

  * SNAPSHOT_ID with the name that you want to give the snapshot. For example, `my-snapshot-1`.
  * INSTANCE_ID with the name of the instance from which the snapshot was created. For example, `my-instance-1`.
  * LOCATION with the [zone or region](https://docs.cloud.google.com/filestore/docs/regions#supported_regions) of the instance from which the snapshot was created. For example, `us-east1-b` or `us-central1`, respectively. Note that your instance's [service tier](https://docs.cloud.google.com/filestore/docs/service-tiers#overview) determines whether a zone or region is a valid argument.



## Restore data

You can restore individual files from a snapshot or revert the entire file share to a prior snapshot state.

For more information, see [Restore a file from a snapshot](https://docs.cloud.google.com/filestore/docs/restore-file) and [Revert an instance to a prior snapshot state](https://docs.cloud.google.com/filestore/docs/revert-snapshot).

## Monitoring

You can monitor an instance's snapshot capacity using Metrics Explorer. For more information, see [Create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

## What's next

  * [Snapshots overview](https://docs.cloud.google.com/filestore/docs/snapshots)
  * [Restore a file from a snapshot](https://docs.cloud.google.com/filestore/docs/restore-file)
  * [Revert an instance to a prior snapshot state](https://docs.cloud.google.com/filestore/docs/revert-snapshot)
  * [Schedule Filestore enterprise snapshots](https://docs.cloud.google.com/filestore/docs/schedule-filestore-enterprise-snapshots)
  * [Backups overview](https://docs.cloud.google.com/filestore/docs/backups)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
