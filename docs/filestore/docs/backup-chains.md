---
url: https://docs.cloud.google.com/filestore/docs/backup-chains/
title: Backup chains \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:41.502715+00:00
---

# Backup chains  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/backup-chains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Backup chains Stay organized with collections  Save and categorize content based on your preferences. 

A _backup chain_ is a group of backups for the same instance, region, and [CMEK](https://docs.cloud.google.com/filestore/docs/cmek). Backups are stored in Cloud Storage and are incremental, capturing only changes since the last backup in the chain to save space and reduce costs. Occasionally, a backup might capture a full copy to ensure history reliability.

Every time a backup is created in the same backup chain, to avoid creating a full copy, the previous backup is scanned for both differential and incremental changes:

  * **Differential changes:** includes changes made to files on the share such as file edits, additions, or deletions.

  * **Incremental changes:** includes changes to storage in the bucket where backup data is located. This might include deduplication of data previously referenced in the chain.




Storing instance data to multiple backup chains implies that you are saving and storing backups to alternating locations. Expect higher latency on backup `create` operations when alternating between backup chains.

Unchanged data contained in previous backups are referenced in, but not copied to, newer backups. If an older backup is deleted, its unique data is copied to the next most recent backup and all internal data references are automatically updated.

Internally, a backup chain's history is tracked using snapshots, which consume capacity on the source instance.

Backup creation is instantaneous, but it takes a period that's proportional to the amount of data being copied before the backup is available for use. During this period, the backup transitions through three states:

State | Description  
---|---  
**Creating** | Capturing the file share state; takes a few seconds.  
**Finalizing** | Uploading data; duration depends on data size.  
**Ready** | Ready for use.  
  
After creation, basic tier backups are compressed to reduce costs. Performance might be slightly reduced during creation for zonal, regional, and enterprise service tiers. For more information, see [Compare snapshots and backups](https://docs.cloud.google.com/filestore/docs/compare-snapshots-and-backups#backups).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
