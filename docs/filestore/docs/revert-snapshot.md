---
url: https://docs.cloud.google.com/filestore/docs/revert-snapshot/
title: Revert a file share to a prior snapshot state \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:35.498101+00:00
---

# Revert a file share to a prior snapshot state  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/revert-snapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Revert a file share to a prior snapshot state Stay organized with collections  Save and categorize content based on your preferences. 

The following guide shows you how to [revert](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/revert) an instance, specifically a single file share within an instance, to a prior snapshot state.

## Should you use the `revert` operation?

The revert snapshot feature is an irreversible operation, both to the live file system and to the newer snapshots in the chain. Use the revert feature carefully. For a more detailed explanation, see [Revert to a snapshot state](https://docs.cloud.google.com/filestore/docs/snapshots#revert-to-snapshot).

All data written after the creation of the target snapshot is deleted at the beginning of the revert process and cannot be recovered. All snapshots that are newer than the target snapshot are also deleted. For example, `snapshot1`, `snapshot2`, and `snapshot3` are created sequentially. Reverting the instance to the state captured in `snapshot2` means that all data written after `snapshot2`, as well as all snapshots taken after the creation of `snapshot2`, are deleted in the revert process.

While a revert operation can take up to two minutes to complete, cleanup of the deleted data can take between six hours to ten days, depending on the number of files involved. You must wait for the revert operation to complete before starting another revert operation.

Only instances with a single share can revert to a snapshot state. The revert snapshot feature can't be combined with [Filestore multishares for GKE](https://docs.cloud.google.com/filestore/docs/multishares). For more information, see [Snapshot feature limitations](https://docs.cloud.google.com/filestore/docs/snapshots#feature_limitations) or the [`gcloud filestore instances revert`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/revert) page.

## Use gcloud CLI to revert a file share to a previous snapshot

###  gcloud CLI 

To revert a file share to the state captured in a snapshot:

  1. Unmount the file share from clients:
         
         sudo umount mount-point-directory
         

  2. Revert the file share to a snapshot state using the [`instances revert`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/revert) command:
         
         gcloud filestore instances revert INSTANCE_ID \
             --target-snapshot=SNAPSHOT_ID \
             --location=LOCATION
         

Replace the following:

     * INSTANCE_ID with the name of the instance where you want to apply the `revert` operation. For example, `my-instance-1`.
     * SNAPSHOT_ID with the name of the snapshot you want to use for the `revert` operation. For example, `my-snapshot-3`.
     * LOCATION with the location of the instance. For example, `us-central1`.



You must wait for the revert operation to complete before you can start another revert operation for the instance. Revert operations can take up to two minutes. However, the data cleanup and space reclamation process can take between six hours to ten days to complete. During this process, the reclaimed space becomes available gradually while the cleanup operation finishes and all reclaimed space is available. For more information, see [Snapshot limitations](https://docs.cloud.google.com/filestore/docs/snapshots#feature-limitations).

## What's next

  * [Snapshots overview](https://docs.cloud.google.com/filestore/docs/snapshots)
  * [Restore a file from a snapshot](https://docs.cloud.google.com/filestore/docs/restore-file)
  * [Schedule Filestore enterprise snapshots](https://docs.cloud.google.com/filestore/docs/schedule-filestore-enterprise-snapshots)
  * [Backups overview](https://docs.cloud.google.com/filestore/docs/backups)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
