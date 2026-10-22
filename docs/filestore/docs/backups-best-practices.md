---
url: https://docs.cloud.google.com/filestore/docs/backups-best-practices/
title: Best practices for creating backups \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:41.233667+00:00
---

# Best practices for creating backups  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/backups-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Best practices for creating backups Stay organized with collections  Save and categorize content based on your preferences. 

The following sections cover recommended best practices.

## Preparing your file share for the best backup consistency

The quality of a backup depends on the ability of your application to recover from backups that are created during heavy write workloads. In most situations, you can create backups that have good consistency even while your applications write data to the file share. However, if your applications require strict consistency, we recommend doing one or more of the following:

  * Use **sync** mount. For more information, see "The sync mount option" section in [nfs(5)](https://linux.die.net/man/5/nfs). Alternatively, you can open files with the `O_DIRECT|O_SYNC` flags. For more information, see [open(2)](https://linux.die.net/man/2/open).
  * Pause applications or operating system processes that write data to the file share and cause them to flush their changes to the file share before initiating the backup. For more information, see [fsync(2)](https://linux.die.net/man/2/fsync).
  * If your applications require consistency between multiple shares, pause all applications on all instances that are writing to all file shares and create backups of all file shares before resuming your applications.
  * If you require application level consistency, stop your applications and unmount the file share before creating a backup.



## Using existing backups as a baseline for new backups to reduce backup creation time

Existing backups of a file share within a region are used as baselines for creating new backups of the file share, reducing backup creation time. Therefore, we recommend that you do the following:

  * Take a new backup of a file share before you delete the previous backup of that file share.

  * Wait for new backups to be in the `Ready` state before creating subsequent backups of the same file share.




## Scheduling backups during off-peak hours to reduce backup creation time

Creating backups during off-peak hours reduces the time that it takes to create a backup. If you schedule regular backups of your file shares, we recommend scheduling them during off-peak hours when possible.

Peak hours for backups creation are the end of each business day and midnight in the region where the Filestore instance is located. We recommend creating your backups either in the early morning or during the business day.

## Organizing your data on separate Filestore instances to maximize efficiency

The more data on the file share, the larger the backup and the more it costs. To back up only the data that you need to back up, we recommend organizing your data on separate file shares, namely:

  * Storing critical data with different write patterns or with different backup requirements on different file shares.
  * Reducing the number of backups that you need to create by keeping similar data in one file share.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
