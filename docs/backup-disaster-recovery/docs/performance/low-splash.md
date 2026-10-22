---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/performance/low-splash/
title: Causes of low-splash backups on backup/recovery appliances \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:42.154179+00:00
---

# Causes of low-splash backups on backup/recovery appliances  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/performance/low-splash/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Causes of low-splash backups on backup/recovery appliances Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

## What is a low-splash backup?

On a Backup and DR backup/recovery appliance under normal circumstances, Backup and DR takes a time-consuming initial full-ingest backup of a database, and then all subsequent backups are much faster incremental backups. An incremental backup compares bitmaps of the current snapshot and the preceding snapshot and applies only the incremental changes.

A low-splash backup is a special type of backup job that occurs when some system error in the preceding backup job results in an unreliable bitmap image or an inability to read the bitmap. The service that reads the bitmap is cbt_server in a Linux environment and AAMService in a Windows environment.

Low-splash backups are more time-consuming than backups made under normal conditions because they must perform a full ingest again to recreate a reliable bitmap. It can then apply the incremental changes without having to replace the full backup.

## Things that don't cause low-splash backups

  * Connector upgrades
  * Graceful system reboots
  * Graceful restarts of cbt_server or AAMService assuming that the service is still running at the time of backup
  * Failovers that did not experience the errors that cause unreliable bitmaps.

**Note:** Low-splash backups don't occur for Oracle databases on Linux or on Windows.



## Causes of unreliable bitmaps

An unreliable bitmap occurs when something interrupts the backup job, including the following:

  * An unclean shutdown of the host: 
    * A non-graceful shutdown causes low-splash due to unreliability of bitmaps. This includes pulling power on a physical machine or any other method of turning off Windows without going through a graceful shutdown, or a blue screen error. This is true even if one machine in a cluster hits a blue screen error that triggers failover, since the bitmap from the failed machine is unreliable.
    * If all Windows servers in a cluster that have hosted the database since the previous backup are not available and running the Backup and DR agent. We pull bitmaps from each cluster host which hosted the database since the previous backup to find changes, and without all bitmaps, we have to run low-splash to maintain data integrity. Note that if a cluster host that hosted a database hits a BSOD, the bitmap might be available at backup but still be unreliable, so low-splash recovery is needed.
  * A failed kernel module update
  * A crash or a restart in the user mode daemon
  * A fingerprint error while running a backup. (Backup and DR performs a "fingerprint check" on each backup job to check for errors.)
  * Error during vaulting, if during OS shutdown the storage disk is full and the system cannot write all data into the vault.
  * SAP HANA node failover, causing the backup to be redirected to a different node.
  * Backup running in degraded mode due to inability to load the kernel module. This typically occurs when the OS is an unsupported version.
  * If cbt_server or AAMService is stopped during the backup, then bitmaps cannot be fetched and the backup job runs in low-splash mode. If AAMService is not down for very long, then starting AAMService will result in bitmaps being available for a normal backup. 
    * If cbt_server or AAMService is stopped for long enough that some gigabytes of events are queued by the driver, then the bitmaps cannot be recreated and the backup will be in low-splash mode. How long this takes depends on how much disk I/O happens on the database. This typically require days of AAMService downtime.
  * Non-graceful shutdown of the cbt_server or AAMService can cause bitmaps to become unreliable for any currently-loaded bitmaps. Bitmaps are loaded if the tracked file has been written to in the last 15 minutes, so generally for a busy database this would cause low-splash.
  * If a volume containing a tracked file (e.g. a SQL Server .mdf file) is unmounted on the host and then re-mounted, the bitmaps are unreliable since there is no way to know what was written to the file while it was unmounted.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
