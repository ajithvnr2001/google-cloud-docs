---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/protect-your-data/
title: Protect your data \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:03.083736+00:00
---

# Protect your data  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/protect-your-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Protect your data Stay organized with collections  Save and categorize content based on your preferences. 

This page provides details for how to protect your data. NetApp Volumes supports volume backups to create offline backups with long retention of your volumes and volume replication to create asynchronous mirrors of your volume in different regions.

## Best practices for protecting your data

For the best possible protection, we recommend that you use both volume snapshots and volume backups. NetApp Volumes offers multiple data protection options which can be combined to achieve your selected recovery point and time objectives. A recovery point objective (RPO) describes how recent the latest copy of your data is guaranteed to be, which depends on how frequently the copies are made. A recovery time objective (RTO) defines how long it takes to restore your data.

## Protect your data with snapshots

Snapshots are virtual point-in-time versions of a volume that are taken on a scheduled basis. You can access snapshots using standard file system commands. Snapshots provide a RPO of as little as one hour. RTO depends on the amount of data you have to restore and is primarily limited by the volume throughput limit. Snapshots also allow users to restore specific files and directories, which decreases RTO even further. Snapshots only consume additional volume space for changes made to the volume.

## Protect your data with backups

Volume backups provide independent point-in-time copies of your volume. They can be used to store old backups and provide the necessary second copy of your data. Daily, weekly, and monthly backup schedules allow for RPOs starting at one day. Volume backups can only be restored as a whole. Creating a volume from a backup (RTO) can take hours, depending on the size of the backup.

## Protect your data with volume replication

Volume replication creates a copy of the latest data of a volume in a different region, including all of its snapshots. If your workloads require a low RPO from your disaster recovery plan and a low RTO for business continuity, you can consider performing a [volume replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication). While volume replication makes sure recent data is available in a different region for you to use, you need to adjust your clients to use the volume in the other region.

## Recommendations for protecting your data

  * **Use volume backups in conjunction with snapshots** : using the two features together ensures that you're able to restore your files from snapshots and perform full restores in case of volume loss using backups.

  * **Define a volume backup policy** : make sure that the backup policy satisfies your company requirements for backup age and frequency. We recommend keeping a minimum of two daily backups for each volume.

  * **Define a snapshot schedule** : older snapshots are less likely to be used to restore data. We recommend that you define a snapshot schedule that takes into consideration the diminishing returns of keeping older snapshots against the cost for additional snapshot capacity.




## What's next

[Backup your data](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-backups).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
