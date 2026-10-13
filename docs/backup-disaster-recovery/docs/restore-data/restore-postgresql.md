---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-postgresql/
title: Restore and recover PostgreSQL databases in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:27.325181+00:00
---

# Restore and recover PostgreSQL databases in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-postgresql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Restore and recover PostgreSQL databases in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

## Restore a PostgreSQL database from a volume-level backup image to the source

This procedure uses physical recovery of the source data area. To recover back to the source, follow these instructions:

  1. From the **App Manager Applications** list, right-click the protected database and select **Access**. Use the **Managed Backup Plan** status filter to show only protected databases.
  2. Select a snapshot image and click **Restore**.
  3. On the **Restore** page, select **Restore Back to Source**.
  4. **Target**. This is inaccessible when restoring to the source.
  5. (Optional) Enter a descriptive **Label** to use for this job.
  6. Application Options 
     * If the source application is protected by a snapshot policy that has enabled database log backups, and logs are available with the image, you can use them to roll forward to a specific point in time by changing these options in the **Roll Forward Time** section: 
       * The date field contains all possible dates that the database can be rolled forward to through the application of database transaction logs. Select which date you need the database to be rolled forward to.
       * The time field contains a slider showing all possible times on the selected date that the database can be rolled forward to. If you select the latest possible date and then move the slider to the right most position, the restore job applies to all available logs. If you select the earliest possible date and move the slider to the left most position, the restore job applies no logs.
     * You can specify to roll forward using either **User Time** or **Host Time**. **User Time** is relative to the local time of the current user. **Host time** is relative to the system that hosts the data to be restored.
     * **PostgreSQL Target Server Port**. Enter the target PostgreSQL instance port number for restore.
     * **PostgreSQL Target OS User Name**. Enter the name of the operating system user on the target server where the PostgreSQL instance is to be restored.
     * **PostgreSQL Target Server Home Directory**. Enter the path of the PostgreSQL installed binary home directory on the target server.
     * **PostgreSQL Target Server Data Directory**. Enter the path to the data directory where the data files for the PostgreSQL database on the target server are stored, for example, `/pgdata_lvm/pgdata`.
  7. Advanced Options 
     * **POSTGRESQL TARGET DB USER NAME** and **POSTGRESQL TARGET DB PASSWORD**. (Optional) Enter new credentials for the target PostgreSQL instance that will be created. If you don't specify anything, the default database username (postgres) is used with no password. By default, a password is not required to sign in from the local system.
  8. Click **Pre-flight check**. 
     * If the pre-flight check fails, fix the issue and resubmit the pre-flight check.
     * If the pre-flight check is successful, click **Submit** to submit the restore job.



## Restore a PostgreSQL database from a volume-level backup image to a new target

  1. From the **App Manager Applications** list, right-click the protected database and select **Access**. Use the **Managed Backup Plan** status filter to show only protected databases.
  2. Select a snapshot image and click **Restore**.
  3. On the Restore page, select **Restore to a New Target**.
  4. For all configurations, eligible PostgreSQL nodes will be available to choose under the **Target** drop-down list. Select the node for the new target.
  5. (Optional) Enter a descriptive **Label** to use for this job.
  6. **Replace Original Application Identity**. This option is only available when the restore target is a new host on the same backup/recovery appliance where the backup was originally generated. 
     * **Yes**. This replaces the original application and it has the same application ID, jobhistory, backup images and backup plan as the original application.
     * **No**. This does not replace the original application. It creates a new application that is discovered but not yet protected.
  7. If logs are available, then **Rollforward time** is available. Choose a date and time for the most recent logs to apply to the recovered database.
  8. Included Databases: This is pre-populated with the list of PostgreSQL user databases that will be restored with the PostgreSQL instance restore. It is immutable.
  9. Application Options 
     * **PostgreSQL Target Server Port**. Enter the target PostgreSQL instance port number for restore.
     * **PostgreSQL Target OS User Name**. Enter the name of the operating system user on the target server where the PostgreSQL instance is to be restored.
     * **PostgreSQL Target Server Home Directory**. Enter the path of the PostgreSql installed binary home directory on the target server.
     * **PostgreSQL Target Server Data Directory**. Enter the path of the data directory where the data files for the PostgreSQL database on the target server are stored, for example, `/pgdata_lvm/pgdata`.
  10. Advanced Options 
     * **POSTGRESQL TARGET DB USER NAME** and **POSTGRESQL TARGET DB PASSWORD**. (Optional) Enter new credentials for the target PostgreSQL instance that will be created. If you don't specify anything, the default database username (postgres) is used with no password. By default, a password is not required to sign in from the local system.
  11. Click the **Pre-Flight Check**. 
     * If the pre-flight check fails, fix the issue and resubmit the Pre-Flight Check.
     * If the pre-flight check is successful, click **Submit** to submit the restore job.



## Restore a PostgreSQL database from a full+incremental backup image to the source

  1. From the **App Manager Applications** list, right-click the protected database and select **Access**. Use the **Managed Backup Plan** status filter to show only protected databases.
  2. Select a snapshot image and click **Restore**.
  3. On the Restore page, select **Restore Back to Source**.
  4. **Target**. This is inaccessible when restoring to the source.
  5. (Optional) Enter a descriptive **Label** to use for this job.
  6. **Included Databases**. This is the list of PostgreSQL databases that will be restored with PostgreSQL instance restore. Select one or more databases from the list for restore. By default all databases are selected for restore. 
  7. Application Options 
     * **PostgreSQL Target OS User Name**. Enter the name of the operating system user on the target server where the new PostgreSQL instance will get created.
     * **PostgreSQL Target Server Home Directory**. Enter the path to the PostgreSQL installed binary home directory on the target server.
     * **PostgreSQL Target Config File Path**. Enter the config path for PostgreSQL instance on the target server.
  8. Advanced Options 
     * **POSTGRESQL TARGET DB USER NAME** and **POSTGRESQL TARGET DB PASSWORD**. (Optional) Enter new credentials for the target PostgreSQL instance that will be created. If you don't specify anything, the default database username (postgres) is used with no password. By default, a password is not required to sign in from the local system.
  9. Click the **Pre-Flight Check**. 
     * If the pre-flight check fails, fix the issue and resubmit the Pre-Flight Check.
     * If the pre-flight check is successful, click **Submit** to submit the restore job.



## Restore a PostgreSQL database from a full+incremental backup image to a new target

  1. From the **App Manager Applications** list, right-click the protected database and select **Access**. Use the **Managed Backup Plan** status filter to show only protected databases.
  2. Select a snapshot image and click **Restore**.
  3. On the Restore page, select **Restore to a New Target**.
  4. For all configurations, eligible PostgreSQL nodes are available to choose under the **Target** drop-down list. Select the node for the new target.
  5. (Optional) Enter a descriptive **Label** to use for this job.
  6. **Replace Original Application Identity**. This option is only available when the restore target is a new host on the same backup/recovery appliance where the backup was originally generated. 
     * **Yes**. This replaces the original application and has the same application ID, jobhistory, backup images and backup plan as the original application.
     * **No**. This does not replace the original application. It creates a new application that is discovered but not yet protected.
  7. **Included Databases** : This is pre-populated with the list of PostgreSQL databases that will be restored with the PostgreSQL instance restore. It is immutable.
  8. Application Options 
     * **PostgreSQL Target OS User Name**. Enter the name of the operating system user on the target server where the new PostgreSQL instance will get created.
     * **PostgreSQL Target Server Home Directory**. Enter the path to the PostgreSQL installed binary home directory on the target server
     * **PostgreSQL Target Config File Path**. Enter the config path of the PostgreSQL instance on the target server.
  9. Advanced Options 
     * **POSTGRESQL TARGET DB USER NAME** and **POSTGRESQL TARGET DB PASSWORD**. (Optional) Enter new credentials for the target PostgreSQL instance that will be created. If you don't specify anything, the default database username (postgres) is used with no password. By default, a password is not required to sign in from the local system.
  10. Click the **Pre-Flight Check**. 
     * If the pre-flight check fails, fix the issue and resubmit the Pre-Flight Check.
     * If the pre-flight check is successful, click **Submit** to submit the restore job.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
