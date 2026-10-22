---
url: https://docs.cloud.google.com/filestore/docs/restore-file/
title: Restore an individual file from a snapshot \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:55.308621+00:00
---

# Restore an individual file from a snapshot  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/restore-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Restore an individual file from a snapshot Stay organized with collections  Save and categorize content based on your preferences. 

The following guide shows how to restore an individual file from a snapshot.

Similar to [reverting an instance](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/revert), using a snapshot to restore a single file is a destructive operation. Use this feature carefully. For a detailed description of snapshot limitations, see [Snapshot feature limitations](https://docs.cloud.google.com/filestore/docs/snapshots#feature_limitations).

###  gcloud CLI 

To restore a file to a previous state that's captured in a snapshot, run the following command from a client VM that has the instance mounted:
    
    
    sudo cp -pa MOUNT-POINT-DIRECTORY/.snapshot/SNAPSHOT_ID/FILE MOUNT-POINT-DIRECTORY
    

#### Example

If you want to restore file `mount-point-directory/genomics-file.txt` to the state preserved in snapshot `snap2`, run:
    
    
    sudo cp -pa mount-point-directory/.snapshot/snap2/genomics-file.txt mount-point-directory/
    

## What's next

  * [Snapshots overview](https://docs.cloud.google.com/filestore/docs/snapshots)
  * [Revert an instance to a prior snapshot state](https://docs.cloud.google.com/filestore/docs/revert-snapshot)
  * [Schedule Filestore enterprise snapshots](https://docs.cloud.google.com/filestore/docs/schedule-filestore-enterprise-snapshots)
  * [Backups overview](https://docs.cloud.google.com/filestore/docs/backups)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
