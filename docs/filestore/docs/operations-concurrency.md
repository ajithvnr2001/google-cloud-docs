---
url: https://docs.cloud.google.com/filestore/docs/operations-concurrency/
title: Operations concurrency \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:42.784582+00:00
---

# Operations concurrency  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/operations-concurrency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Operations concurrency Stay organized with collections  Save and categorize content based on your preferences. 

The following is a list of known behaviors encountered when attempting to run some concurrent operations.

## Concurrent backup operations

  * [Backup](https://docs.cloud.google.com/filestore/docs/backups) `delete` operations associated with the same source instance must be performed one at a time.

Bulk backup `delete` operations within a backup chain are not supported. While a `delete` operation is pending, any new `delete` operations within the same backup chain return a `RESOURCE_EXHAUSTED` error. This is regardless of whether the source instance has been deleted.

    * If the source instance has been deleted, users receive a similar `FAILED_PRECONDITION` error.

    * This limitation applies to every service tier but basic SSD and basic HDD.

    * Note that Filestore does support concurrent backup `delete` operations when backups reference separate source instances.

For example, an instance labeled `Source1` has backup data referenced in `Backup1` and `Backup2`. `Source2` has backup data referenced in `Backup3` and `Backup4`. `Backup1` and `Backup2` can't be deleted in parallel, however, `Backup2` and `Backup3` can.

  * Backup `create` and backup `delete` operations initiated within the same backup chain _can_ run concurrently. However, users can't complete a backup `create` operation while the most recent backup is being deleted.

    * If the user attempts to create a new backup of the instance while the most recent backup is being deleted, they will receive a `FAILED_PRECONDITION` error. For example, if `Source1` has a backup chain composed of `Backup1` and `Backup2`, and the user begins a `create` operation for `Backup3`, they won't be able to delete `Backup2` until the `create` operation completes. This is because the most recent backup contains the most critical data needed to successfully complete the backup `create` operation.
  * The following backups operations have a rate limit of once per 10 minutes in the steady state:

    * Creating a backup of Filestore instance
    * Restoring a Filestore instance from a backup (in-place restore)
    * Creating a new Filestore instance from a backup

For more information, see [Rate limits for backups](https://docs.cloud.google.com/filestore/docs/limits#rate-limits-backups).




## What's next

  * [Known issues](https://docs.cloud.google.com/filestore/docs/known-issues)
  * [List of Filestore-specific response error codes and messages](https://docs.cloud.google.com/filestore/docs/response-errors)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
