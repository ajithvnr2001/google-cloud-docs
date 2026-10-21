---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/oracle-db-protect/
title: Back up an Oracle database to an appliance-managed backup \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:09:00.224304+00:00
---

# Back up an Oracle database to an appliance-managed backup  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/oracle-db-protect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Back up an Oracle database to an appliance-managed backup Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Use the following instructions to apply a backup plan to protect an Oracle database:

  1. In the Backup and DR appliance management console, click **App Manager** > **Applications** and enter the database application name or use the filters to find the database that you need.

  2. Right-click the application and select **Manage Backup Plan**.

  3. On the **Manage Backup Plan** page, select a template and a profile and click **Apply Backup Plan**.

  4. The **Apply Backup Plan** dialog opens. Assign policy overrides and change application settings as needed.

  5. You can wait for the job to run during the period scheduled in the backup plan, or you can run the job at the next opportunity by clicking on the job and selecting **Run Now**.

**Note:** To take Oracle ASM to FS backups over NFS, you must enable **Convert ASM to FS format** in the database **Application Details & Settings**.
  6. The job runs as soon as the scheduler has an opening, often immediately. You can go to the **Jobs Monitor** to view the progress and details of the job.

**Note:** If the template captures logs, and if you have software that purges logs through RMAN, be sure to disable it. If that purge runs during a Backup and DR backup job, the backup may have incomplete log information.

If you back up a workload to a backup/recovery appliance that would exceed its recommended storage capacity or snapshot limit, you will see a notification with a recommendation to back up the data to a different backup/recovery appliance.

**Caution:** Exceeding the capacity of a backup/recovery appliance can lead to failed jobs and unprotected data and failed restore operations.



Oracle database protection is the same for databases running on Bare Metal Solution servers or inside a Compute Engine instance.

## Oracle RMAN logs

This section is for Oracle protection logs on Linux. The following are logs that you might need to consult:

Log | Location | What's in it | What to look for  
---|---|---|---  
Backup and DR agent log | `/var/act/log/UDSAgent.log` | For any mount job. | Any error with ORA-  
Database RMAN backup log | `/var/act/log/<database name>_rman.log` | All the backup command and output for database and archive log backup. | ORA- and RMAN- errors in the log file.  
  
Application aware mounts produce additional logs. Check the following logs on the target database server:

Log | Location | What's in it | What to look for  
---|---|---|---  
Backup and DR agent log | `/var/act/log/UDSAgent.log` | For any mount job. | Any error with ORA-  
Database under file system | `/act/act_scripts/oracleclone/dbrecover_<dbname>.txt` | Progress of the archive log roll-forward. | Errors except those relating to a log looking for an archive during the roll-forward.  
Database under ASM disk group | `/act/act_scripts/asmclone/dbrecover_<dbname>.txt` |  |   
`/act/act_scripts/asmclone/openDBlog_<dbname>.txt` | Steps to configure target database post-roll-forward. | Any error with ORA- |   
  
## The Oracle DBA guide

  * [Backup and DR for Oracle databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-intro)
  * [Prerequisites for protecting an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prerequisites)
  * [Oracle patches and known issues](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-patches-known-issues)
  * [Prepare Oracle databases for protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prepare)
  * [Discover and protect an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-oracle)
  * [Details and settings for Oracle databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/oracle-advanced-settings)
  * [Use dNFS with Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-dnfs)
  * [Protect a discovered Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/oracle-db-protect)
  * [Mount an Oracle database as a standard mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount)
  * [Create an instant virtual copy of an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount-virtualdb)
  * [Restore and recover an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-oracle)
  * [Instant recovery of an Oracle database using Mount and Migrate](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/oracle-mm)
  * [Provision an environment with a Backup and DR workflow](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-workflow-oracle)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
