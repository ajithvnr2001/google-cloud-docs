---
url: https://docs.cloud.google.com/filestore/docs/compare-snapshots-and-backups/
title: Compare snapshots and backups \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:39.782542+00:00
---

# Compare snapshots and backups  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/compare-snapshots-and-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Compare snapshots and backups Stay organized with collections  Save and categorize content based on your preferences. 

The following topic briefly describes the intended uses of snapshots and backups.

## Snapshots

_[Snapshots](https://docs.cloud.google.com/filestore/docs/snapshots)_ are resources that consume capacity within the instance and allow you to revert the current state of your instance data to a previous, specific point in time. Users can also elect to revert to a previous version of a specific file.

Snapshots don't replicate any data or consume capacity until the data on the instance is modified. All snapshots of an instance share in-common data, meaning that the instance preserves only the differences between the snapshots. While snapshots do offer cost efficiency when compared to backups, available instance capacity continuously decreases as file modifications are made.

Reverting an instance to a previous state is destructive, as it deletes the latest version of instance data, and should be used carefully.

## Backups

_[Backups](https://docs.cloud.google.com/filestore/docs/backups)_ are external resources that reside outside of the instance, consuming their own separate capacity. The first backup is a complete copy of instance data, with each subsequent backup only consuming the data necessary to track [incremental and differential](https://docs.cloud.google.com/filestore/docs/backups#backup-creation) changes since the previous backup. Internally, a [backup chain's](https://docs.cloud.google.com/filestore/docs/backups#backup-creation) history is tracked using snapshots, which consume capacity on the source instance.

By default, backups are incremental to avoid billing for redundant data and to minimize the use of storage space. To ensure the reliability of the underlying change history, a backup may occasionally capture a full copy of the instance. This happens automatically to maximize storage space and minimize storage costs. You don't need to choose between creating incremental or full backups. When a backup captures a full copy of the instance, previous incremental snapshots of that instance are unchanged.

## What's next

  * [Learn more about backups](https://docs.cloud.google.com/filestore/docs/backups)
  * [Learn more about snapshots](https://docs.cloud.google.com/filestore/docs/snapshots)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
