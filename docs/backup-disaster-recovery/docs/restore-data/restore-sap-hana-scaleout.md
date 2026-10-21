---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-sap-hana-scaleout/
title: Restore and recover SAP HANA scale-out databases \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:00.956155+00:00
---

# Restore and recover SAP HANA scale-out databases  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-sap-hana-scaleout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Restore and recover SAP HANA scale-out databases Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page includes information on recovering SAP HANA scale-out instances from Backup and DR backups.

**Note:** This information is for SAP HANA Scale-Out instances. For Scale-Up and HA 1+1 configurations, see [Backup and DR for SAP HANA](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana).

## License requirements and impact on restore

  * The license key for an SAP HANA database is based on the system ID and the hardware ID. After a recovery, an SAP HANA license key becomes invalid if the SID or hardware ID has changed.
  * During recovery, a temporary license key is installed automatically if the backup used for recovery has a permanent license, which is still valid. You can work with the automatically installed temporary license for up to 90 days. During this time, you need to apply to SAP to have the license from the source database transferred to a new license key. You then need to install the new license key in the recovered SAP HANA database.
  * If the backup that was used for recovery only had a temporary license, the database is in lockdown mode immediately after recovery.



**Source database with temporary license** These are backups taken with temporary licenses.

  * **Restore back to source.** : It is 90 days from the time of database creation and the database is in lockdown mode.
  * **Restore to the new target.** It fails as SAP temp license does not allow the restore to new target.



**Source database with permanent license** These are backups taken with permanent licenses.

  * **Restore back to source.** No issue.
  * **Restore to the new target** It has 90 days trial license. Backups succeed but they are not be able to use the backup to restore.



**SAP references**

  * [Points to Note: License Key and Recovery](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.02/en-US/19a0f5a85685453080f00087bb9b9c98.html "hover text")
  * [License Keys for the SAP HANA Database](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.02/en-US/bddd0b28bb571014bd9592d247dcd403.html "hover text")



## Preflight check

During the restore procedure, a preflight checks validate the recovery. These required prerequisites are checked for a successful database restore:

  * **HANA SID** : HANA is configured on the target node with the same HANA SID name.
  * **Config file** : Config file global.ini is configured correctly
  * **Log backup path** : Log backup path is set under global.ini
  * **BACKINT CONFIG** : 
    * **From volume-level image** : Backint is not configured for this database.
    * **From full+incremental image** : If the target server is not already configured with backint, then backint is configured during restore.
  * **HANA VERSION** : Target HANA version is the same as the source HANA version.
  * **USERSTOREKEY** : Provide userstore key exists on target or a valid privileged username and password is specified which exists at the time of backup.
  * **Logical volume**
    * The logical volume name and volume group name should be the same on source and target node.
    * The logical volume size on target should be the same or greater than source logical volume.
  * **Node Status**
    * **Scale-up and standalone config** : Target node is up and available
    * **HANA HA (1+n) config** : Replication needs to disabled before restore can be initiated. Post restore replication needs to be reconfigured. Restore to any node of a HANA HA (1+n) cluster results in creating a standalone application on the selected target host. User has to explicitly configure the cluster back as needed and discover the application appropriately



## Automated recovery of an SAP HANA database

**Note:** This procedure is physical recovery of the entire data set. The recovered data overwrites the original data. This can take a long time depending on the amount of data.

**Before you begin**

  * Be sure to review License requirements and impact on restore
  * Be sure to review Prerequisites required for the successful database restore




### To new from volume-level backup

**Automated recovery of a HANA database to a new target from a volume-level backup**

  1. From the **App Manager Applications** list, right-click the database and select **Access**.
  2. Select the latest snapshot to recover and choose **Restore**.
  3. On the **Restore** page, choose **Restore Back to New Target**.

     * **Target.** For all configurations, eligible HANA nodes will be available to choose under the drop-down. Select the node for restore from the drop-down.
     * **Replace Original Application identity.** This option is only available when restore is performed to a new host on the same appliance where the backup was originally generated.

       * **Yes.** This will replace the original application and will carry the same application ID, jobhistory, backups and backup plan as the original application.
       * **No.** This won't replace the original application. It will be discovered as a new application as part of restore job.
**Note:** After a HANA HA restore, the node will become standalone and retain the same appid of the cluster. If you enable replication, the next discovery on the restore host will find the cluster and continue to use the same appid as cluster host.
     * **Rollforward time.** Choose a date and time for a database protected with logs to recover to.
     * **TARGET DATABASE SID.** This will be pre-populated with the protected database sid name and is immutable.
     * **SAP DB USER STORE-KEY.** This will be pre-populated with the user store key during the backup. A new userstore key can be specified with a privileged username and password that was available during backup. This new userstore key will be created and will be used for recovery.

     * If the username, password is provided with the existing userstore key, the userstore key will be recreated with this username and password. The validation will only be done after the systemdb recovers. The tenant recovery may fail if the username or password is not valid or does not contain the right privilege and or not available as part of the backup.

     * If a new userstore key with username and password is specified, then the userstore key will be created with the specified userstore key name and username and password. The validation will only be done after the systemdb recovery. The tenant recovery may fail if the username or password is not valid or does not contain the right privilege or is not available as part of the backup.

     * If no userstorekey, username and password are passed, then during the precheck, validation will occur to check if the userstorekey used during backup exists on the target server. The pre check will fail if the userstorekey used during backup is not found. Tenant recovery may fail if the username or password is not valid or does not contain the right privilege or is not available as part of the backup.

     * If no userstorekey is passed, but username and password are provided, then the userstorekey used during backup will recreated with the credentials passed on the target server. The tenant recovery may fail if the username or password is not valid or does not contain the right privilege and or not available as part of the backup.

  4. Click the pre-flight check.



  * If the pre-flight check fails, fix the issue and resubmit the **Pre-Flight Check**.
  * If the pre-flight check is successful, click **Submit** to submit the restore job.



### To source from volume-level backup

**Automated recovery of a HANA database to the source from a volume-level backup**

**Note:** This procedure is physical recovery of the entire dataset. The data is copied over, overwriting the original data. This can take a long time depending on the amount of data.

  1. From the **App Manager** , **Applications** list, right-click the database and select **Access**. From the latest snapshot to recover, choose **Restore**.
  2. On the **Restore** page, choose **Restore Back to Source**.

     * **Target.** complete the following: 
       * For standalone SAP HANA configuration, **Target** is pre-populated.
       * For HANA HA (1+n) configuration, select the HANA HA node to restore to from the drop-down list.
     * **Rollforward time.** Choose a date and time for a database protected with logs to recover to.
     * **TARGET DATABASE SID.** This will be pre-populated with the protected database sid name and is immutable.
     * **SAP DB USER STORE-KEY.** This will be pre-populated with the user store key during the backup. A new userstore key can be specified with a privileged username and password that was available during backup. This new userstore key will be created and will be used for recovery. 
       * If the username and password are provided with the existing userstore key, the userstore key will be recreated with this username and password. The validation will only be done after the systemdb recovers. The tenant recovery may fail if the username or password is not valid or does not contain the right privilege and or not available as part of the backup.
       * If a new userstore key with username and password is specified, the userstore key will be created with the specified userstore key name and username and password. The validation will only be done after the systemdb recovery. The tenant recovery may fail if the username or password is not valid or does not contain the right privilege and or is not available as part of the backup.
       * If no userstorekey, username and password are passed, then during the pre-check, validation will occur to check if the userstorekey used during backup exists on the target server. The pre-check will fail if the userstorekey used during backup is not found. The tenant recovery may fail if the credentials are not valid or don't contain the right privilege and or are not available as part of the backup.
       * If no userstorekey passed, but username and password was provided, then the userstorekey used during the backup will recreated with the credentials passed on the target server. The tenant recovery may fail if the username or password is not valid does not contain the right privilege and or not available as part of the backup.
     1. Click **Pre-Flight Check**.
     * If pre-flight check fails, fix the issue and resubmit the **Pre-Flight Check**.
     * If the pre-flight check is successful, then click **Submit** to submit the restore job.



### To new from full+incremental backup

**Automated recovery of a HANA database to a new target from a full+incremental backup**

  1. From the appliance management console **App Manager** , **Applications** list, right-click the database and select **Access**.
  2. Select the latest snapshot to recover, and choose **Restore**.
  3. On the **Restore** page, choose **Restore to a New Target**.

     * **Target.** For standalone HANA configuration this is pre-populated. HANA HA nodes will be available to choose under the drop-down; select the node for restore from the drop-down.
     * **Replace Original Identity.** This option is only available when restore is performed to a new host on the same backup/recovery appliance where the backup was originally generated.

       * **Yes.** This will replace the original application and will carry the same application ID, job history, backups, and backup plan as the original application.
       * **No.** This won't replace the original application. This will be discovered as a new application as part of the restore job. After a HANA HA restore, the node will become standalone and retain the same appid of the cluster. If you enable replication, the next discovery will find the cluster and continue to use the same appid as cluster host.
     * **INCLUDE LIST.** For recovering SYSTEMDB with or without or one or more tenant databases out of **n** tenant databases, provide a comma separated list of databases under **INCLUDE**.

     * For **EXCLUDE LIST** , for excluding SYSTEMDB or one or more tenant database during recovery out of n tenant database: provide a comma-separated list of databases under **EXCLUDE**. For example, putting SYSTEMDB in the exclude list excludes SYSTEMDB from recovery and recover all tenant databases that are backed up.

**Note:** Use either **INCLUDE LIST** or **EXCLUDE LIST** for specific database recovery. For example if you have SYSTEMDB and tenant—tn1, tn2, tn3—then complete one of the following:
       * If **INCLUDE LIST** and **EXCLUDE LIST** are both empty, then SYSTEMDB and all tenants (tn1,tn2,tn3) will be recovered.
       * If you want to recover a single tenant tn1, then use the include list with tn1.
       * If you want to recover tn2 and tn3 and exclude SYSTEMDB and tn1, then use the include list with only tn2 and tn3.
       * If you want to recover all tenants (tn1,tn2,tn3) only and exclude SYSTEMDB, then either exclude SYSTEMDB or include tn1, tn2, tn3.
**Note:** SYSTEMDB recovery impact: With SYSTEMDB recovery, any tenant db excluded from the recovery won't start after the restore. The excluded tenant will have to restarted manually.
     * **Rollforward time.** Choose a date and time for a database protected with logs to recover to.

     * **TARGET DATABASE SID.** This will be pre-populated with the protected database sid name and is immutable.

     * **SAP DB USERSTORE KEY.** This will be pre-populated with the user store key during the backup. A new userstore key can be specified with a privileged username and password that was available during backup. This new userstore key will be created and will be used for recovery.

**Important:** Tenant name on the target server should be same as source. Data volume locations for the tenant should be the same as source.
       * If the username, password is provided with the existing userstore key, the userstore key will be recreated with this username and password. The validation will only be done after the SYSTEMDB recovers. The tenant recovery may fail if the username or password is not valid or does not contain the right privilege and or not available as part of the backup.
       * If a new userstore key with username and password is specified, the userstore key will be created with the specified userstore key name and username and password. The validation will only be done after the SYSTEMDB recovery. The tenant recovery may fail if the username or password is not valid or does not contain the right privilege and or not available as part of the backup.
       * If no userstorekey is specified, then the username and password are passed, then during the precheck, validation will occur to check if the userstorekey used during backup exists on the target server. The precheck will fail if the userstorekey used during backup is not found. The tenant recovery may fail if the username or password is not valid or does not contain the right privilege and or not available as part of the backup.
       * If no userstorekey was passed, but username and password was provided, then the userstorekey used during backup will recreated with the credentials passed on the target server. The tenant recovery may fail if the username or password is not valid, if it does not contain the right privileges, or if it is not available as part of the backup.
  4. Click the **Pre-Flight Check**.

     * If the pre-flight check fails, fix the issue and resubmit the **Pre-Flight Check**.
     * If the pre-flight check is successful, then click **Submit** to submit the restore job.



### To source from a full+incremental backup

**Automated recovery of a HANA database back to the source from a full+incremental backup**

**Note:** This procedure uses backint API and is physical recovery of the entire dataset. The data is copied over, overwriting the original data. This can take a long time depending on the amount of data.

  1. From the appliance management console **App Manager** , **Applications** list, right-click the database and select **Access**.
  2. Select the latest snapshot to recover, and choose **Restore**.
  3. On the **Restore** page, choose **Restore Back to Source**.

     * For **Target** , complete the following:

       * For standalone HANA configuration this is pre-populated.
       * For HANA HA (1+n) configuration, HANA HA nodes will be available to choose under drop-down. Select the node for restore from the drop-down.
     * For **INCLUDE LIST** , for recovering SYSTEMDB or one or more tenant database out of n tenant database, provide a comma separated list of database under **INCLUDE**.

     * For **EXCLUDE LIST** , for excluding SYSTEMDB or one or more tenant database during recovery out of n tenant database: provide a comma-separated list of databases under **EXCLUDE**. For example, putting SYSTEMDB in the exclude list excludes SYSTEMDB from recovery and recover all tenant databases that are backed up.

**Note:** Use either **INCLUDE LIST** or **EXCLUDE LIST** for specific database recovery. For example if you have SYSTEMDB and tenant—tn1, tn2, tn3—then complete one of the following:
       * If **INCLUDE LIST** and **EXCLUDE LIST** are both empty, then SYSTEMDB and all tenants (tn1,tn2,tn3) will be recovered.
       * If you want to recover a single tenant tn1, then use the include list with tn1.
       * If you want to recover tn2 and tn3 and exclude SYSTEMDB and tn1, then use the include list with only tn2 and tn3.
       * If you want to recover all tenants (tn1,tn2,tn3) only and exclude SYSTEMDB, then either exclude SYSTEMDB or include tn1, tn2, tn3.
**Note:** SYSTEMDB recovery impact: With SYSTEMDB recovery, any tenant db excluded from the recovery won't start after the restore. The excluded tenant will have to restarted manually.
     * For **Rollforward** time, choose a date and time for a database protected with logs to recover to.

     * For **TARGET DATABASE SID** , this will be pre-populated with the protected database sid name and is immutable.

     * For **SAP DB USER STORE-KEY** , this will be pre-populated with the userstore key during the backup. A new userstore key can be specified with a privileged username and password that was available during backup. This new userstore key will be created and will be used for recovery.

       * If the username and password are provided with the existing userstore key, the userstore key will be recreated with this username and password. The validation will only be done after the systemdb recovers. The tenant recovery may fail if the username or password is not valid or does not contain the right privilege or is not available as part of the backup.
       * If a new userstore key with username and password is specified, the userstore key will be created with the specified userstore key name and username and password. The validation will only be done after the systemdb recovery. The tenant recovery may fail if the username or password is not valid or does not contain the right privilege and or not available as part of the backup.
       * If no userstore key, username and password are passed, then during the precheck, validation will occur to check if the userstorekey used during backup exists on the target server. The pre check will fail if the userstorekey used during backup is not found. The tenant recovery may fail if the username or password is not valid or does not contain the right privilege and or not available as part of the backup.
       * If no userstorekey is passed, but username and password are provided, then the userstorekey used during backup will recreated with the credentials passed on the target server. The tenant recovery may fail if the username or password is not valid or does not contain the right privilege and or not available as part of the backup.
       * With SYSTEMDB recovery, the hdbuserstore key is validated at the end of SYSTEMDB recovery and before starting tenant recovery. The tenant recovery may fail if the username or password is not valid or does not contain the right privilege and or not available as part of the backup.
  4. Click **Pre-Flight Check**.

     * If pre-flight check fails then fix the issue and resubmit the **Pre-Flight Check**.
     * If the pre-flight check is successful, then click **Submit** to submit the restore job.



## Manual recovery of an SAP HANA tenant database

You can manually recover a a single tenant database back to the source from a volume-level backup.

**Note:** This procedure is physical recovery of the tenant dataset. The tenant data is copied over, overwriting the original tenant data. This can take a long time depending on the amount of data.

To recover a single-tenant database, complete the following:

  1. From the **App Manager** , **Applications** list, right-click the database and select **Access**.
  2. From the runway, select the latest snapshot to recover, and then select **Mount** on the right.
  3. On the **Mount** page disable **Application Options** , and under **Mount Options** set a mount location such as `/testmnt`.
  4. Log into the server as root and change the directory to /act/custom_apps/saphana/restore: `cd /act/custom_apps/saphana/restore`
  5. Execute the script for recovery:


    
    
          ./CALL_LVM_single_tenant_recover.sh DBSID TENANT SID SYSTEMDB USERSTORE KEY RECOVERY TIME
    

Description of arguments to the script:
    
    
        DBSID = The database SID
        TENANT SID = The name of the tenant database to be restored
        SYSTEM DB USERSTORE KEY = The System DB userstore key
        RECOVERY TIME = The required recovery time in the format YYYY-MM-DD HH24:MI:SS in UTC
    

For example: `./CALL_LVM_single_tenant_recover.sh lv1 lv1 ACTBACKUP '2019-09-24 20:00:00'`

  1. Once the script has completed, the **Tenant DB** is recovered to the point in time and is available for access.
  2. Go to the appliance management console and [unmount and delete the backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount-delete).



## Manual recovery of an SAP HANA database from a Full+Incremental backint dump backup

You can manually recover a database back to the source from a Full+Incremental dump backup.

**Note:** This procedure is physical recovery of the tenant dataset. The tenant data is copied over, overwriting the original tenant data. This can take a long time depending on the amount of data.

To recover a HANA database from a Full+Incremental dump backup, use this script:
    
    
          /act/custom_apps/saphana/dumpbackint/ACT_HANADB_dumprestorebrint.sh HANA SID Port number HANA UserStore Key  Exclude DB list Include DB list HANA version HANA DB backup mount point
          Recovery time in 'yyyy-mm-dd HH:MI:SS' HANA Log backup mount point
    

Example:

`/act/custom_apps/saphana/dumpbackint/ACT_HANADB_dumprestorebrint.sh GP1 HDB00 ACTBACKUP "null" "null" 2.0 /act/mnt/Job_23867989_mountpoint_1739957140744 '2025-02-12 09:30:00' /act/mnt/Job_23867989_mountpoint_1739957130467`

## Review the status of your backups in SAP HANA Studio

You can review backup status, metadata, and backups in HANA Studio, but you cannot access the Backup and DR backups from HANA Studio. You must access backups for recovery or other uses from the management console.

  1. In HANA Studio, go to the **Backup** folder.

  2. Go to the **Backup catalog** tab.

The Backup catalog tab displays the status of your backups and details such as start time, duration, size, backup type, and destination.




## HANA and HANA HA 1+n restore behavior

This section includes information about HANA and HANA HA 1+n restore behaviors.

### All HANA configurations

Restoring to a new target with **Manage New Application** option enabled:

  * The restored application are protected, but the **Application Details & Settings** section has only the default values. You must manually set the required values under **Application Details & Settings** after restore for the backup to succeed properly.
  * The restored application protection will be in a disabled state. You must enable protection from **App Manager** > **Applications** > **Manage Backup** plan for backups to start running.



### HANA HA (1+n) configurations

For a HANA 1+1 cluster with **Node A** primary and **Node B** secondary—**Node A** —-> **Node B** —the cluster is discovered as an application under Backup and DR and backup runs from the **Node A** —primary.

**Restore to a new target HANA database: standalone or cluster**

If a new target is discovered as an application or protected then before restore, this application needs to be unprotected and deleted from Backup and DR. The job fails if the new target application exists.

**Restore to Node A primary**

  * **Node B** needs to be unregistered from the cluster before running the restore to **Node A**.
  * **Node A** becomes a standalone application post restore to **Node A**.
  * **Node B** must be registered to **Node A** with **Node B** as the secondary and a force discovery must be run on **Node A** to continue as a cluster backup.



**Restore to Node B secondary**

  * **Node B** must be unregistered or else a take-over must be run on **Node B** before restoring to **Node B**.
  * Shut down **Node A** before restoring to **Node B** , and add **Node A** as secondary to **Node B** post restore.
  * **Node B** is a standalone application after the restore operation. **Node A** must be registered to **Node B** with **Node A** as the secondary.
  * Run a discovery from **Node B** to re-discover it as a cluster application.

**Note:** Attaching **Node B** as secondary to **Node A** will keep the original data of A and wipes the **Node B** restored data. To keep **Node A** and **Node B** as protected standalone applications, run discovery on **Node A** and **Node B** after the restore without enabling the replication.
  * To keep **Node A** and **Node B** as standalone applications and protected, run discovery on **Node A** and **Node B** after the restore without enabling the replication.




### How to disable SAP HANA system replication for restore

  1. Log onto both systems as the operating system user—user adm.
  2. Stop the secondary system: `sapcontrol -nr -function StopSystem HDB`.
  3. On secondary system unregister the secondary system: `hdbnsutil -sr_unregister --id=(secondarySiteID)`.
  4. Disable system replication on the primary system: `hdbnsutil -sr_disable`.
  5. Check system replication, with one of the following scripts:

     * The `systemReplicationStatus.py` script. This script shows replication status and database information
     * The `hdbnsutil -sr_state` script. This script shows the replication nodes role and host mapping details.



## Backup and DR documentation for SAP HANA scale-out

This page is one in a series of pages specific to protecting and recovering SAP HANA scale-out instances with Backup and DR. You can find additional information in the following pages:

  * [Backup and DR for SAP HANA scale-out](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana-scaleout)
  * [Prepare SAP HANA scale-out instances for backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sap-hana)
  * [Add an SAP HANA scale-out host, and discover and protect its databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-sap-hana-scaleout)
  * [Configure staging disk format and backup method for SAP HANA scale-out](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-method-staging-disk-sap-hana-scaleout)
  * [Set application details and settings for SAP HANA scale-out instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-sap-hana-scaleout)
  * [Back up HANA 1+n and HANA scale-out databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-sap-hana-scaleout)
  * [Restore and recover SAP HANA scale-out instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-sap-hana-scaleout)
  * [Mount an SAP HANA scale-out backup as a standard mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sap-hana)
  * [Mount an SAP HANA scale-out backup as a virtual database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sap-hana-virtualdb)
  * [Mount and migrate an SAP HANA scale-out backup for instant recovery to any target](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate-sap-hana)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
