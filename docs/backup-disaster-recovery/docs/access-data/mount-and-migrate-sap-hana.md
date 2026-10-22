---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate-sap-hana/
title: Mount and migrate an SAP HANA backup for recovery to any target in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:59.688617+00:00
---

# Mount and migrate an SAP HANA backup for recovery to any target in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate-sap-hana/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mount and migrate an SAP HANA backup for recovery to any target in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This information is for SAP HANA scale-out instances. For Scale-Up and HA 1+1 configurations, see [Backup and DR for SAP HANA](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana).

## SAP HANA scale-out instant recovery (mount and migrate)

Automate HANA data migration from backup/recovery appliance staging disks to the production disks using the LVM migration method. Use the LVM migration method after the SAP HANA database is recovered on the backup/recovery appliance staging disk on the scaleup configuration, or non-shared LVM multinode scaleout cluster.

## The recovery script

The recovery script is `/act/custom_apps/saphana/lvm_migrate/hana_lvm_recover_migrate.sh`

See script details.

## Database recovery and migration

**Prerequisites before starting recovery**

  * Stop the SAP HANA database (across all nodes for scale-out configuration) 
    * `sapcontrol -nr <instance number> -function StopSystem`
    * `sapcontrol -nr <instance number> -function GetSystemInstanceList`
  * Ensure that /etc/fstab has the /dev/mapper entries for /hana/data and /hana/log mount. 
    * Use `df -kh` to get the /dev/mapper entries for /hana/data and /hana/log.
  * Verify that /hana/data and /hana/log is not held by any process. 
    * Check using unmount and remount of /hana/data and /hana/log.
  * If HANA fast restart is configured, then comment the entries for HANA fast restart under /etc/fstab, and unmount the fast restart mount point. Enable the fast restart by mounting the fast restart mount, and uncommenting /etc/fstab entry of fast restart mount, after recovery and merge the first step of the two-step mount and migrate is complete.



## Mount the image

  1. Use the appliance management console to mount the backup image to the target server:

     1. Log into the appliance management console as the privileged user.
     2. Select the required application and select **Access**.
     3. Select the image and click **Mount**.
     4. Disable the **CREATE NEW VIRTUAL APPLICATION** option, and select the respective target node or cluster. If mounting to a scaleout cluster, ensure that the **MOUNT TO ALL CLUSTER SERVERS** option is enabled.
     5. Provide the mount point location and click **Submit**.



Upon completion of the mount job, the image is mounted to the specified location on the target HANA server.

**Note:** In case of non-shared multi-node scaleout cluster, database and log backup images are mounted on the main node. On other nodes database backup images are mapped—not mounted—but the log backup image is mounted. During the recovery process, automated scripts mount the database backup image across all the nodes of the cluster.

### Mount and migrate use cases

**Two use cases**

  * **One-step mount and migrate.** Recover the database, then migrate the data from the backup/recovery appliance presented storage to production storage while the database is running.

  * **Two-step mount and migrate.** Recover a copy of the database. The recovered database is operational from the backup/recovery appliance. When your production storage is ready, you can start the migration of data to production storage while the database is running.




#### One step mount and migrate

After you mount the image, you can recover and migrate the data in one run.

  1. Run this script on the target server where the image is mounted.

`/act/custom_apps/saphana/lvm_migrate/hana_lvm_recover_migrate.sh recovermigrate`

For recovery to a specific point in time, use the `-r` option:

`/act/custom_apps/saphana/lvm_migrate/hana_lvm_recover_migrate.sh recovermigrate -r <time>`

With this option, the database is recovered, volume groups of the disks provisioned from backup/recovery appliance are merged with local storage and migration of the database starts.

  2. Once the job is successful, the data is moved to the local production storage from disks provisioned from backup/recovery appliance while the database is running.




**If the HANA source and target sid are different**

If the HANA source and target sid are different, then rename the sid directory to target sid in the data and log mountpoints before running the `hana_lvm_recover_migrate.sh` script.

For example:

source sid: HPR target sid: HSR mountpoint: /mmrestore

  * The directory `/mmrestore/hana/data/HPR` must be renamed to `/mmrestore/hana/data/HSR` in the /mmrestore/hana/data mountpoint before running the `hana_lvm_recover_migrate.sh` script.
  * The directory `/mmrestore/hana/log/HPR` must be renamed to `/mmrestore/hana/log/HSR` in the /mmrestore/hana/log mountpoint before running the `hana_lvm_recover_migrate.sh` script.



#### Two-step mount and migrate

After you mount the image, recover a copy of the database. The recovered database is operational from the backup/recovery appliance.

  1. Run the recovermerge option to bring the database copy running out of the mounted image:

`/act/custom_apps/saphana/lvm_migrate/hana_lvm_recover_migrate.sh recovermerge`

For recovery to a specific point in time, use the `-r` option:

`/act/custom_apps/saphana/lvm_migrate/hana_lvm_recover_migrate.sh recovermerge -r <time>`

After a successful recovery, the database is running on backup/recovery appliance mounted devices. The database is up and available to the application.

  2. When the production storage is available, start the migration of data to production storage while the database is running.




`/act/custom_apps/saphana/lvm_migrate/hana_lvm_recover_migrate.sh migrate`

## Unmount and delete the mounted image from a backup/recovery appliance

  1. Log into the appliance management console as the privileged user.
  2. Select the mounted image from step 1.
  3. Click [**Unmount & Delete**](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount-delete).



## Script details (hana_lvm_recover_migrate.sh)

The following details are included in the script.

  * **NAME** : SAP HANA restore helper script
  * **PATH** : /act/custom_apps/saphana/lvm_migrate/hana_lvm_recover_migrate.sh
  * **SYNOPSIS** : `hana_lvm_recover_migrate.sh <OPERATION> [OPTIONS]`
  * **DESCRIPTION** : Restores SAP HANA data from a backup/recovery appliance onto a scaleout or standalone cluster.
  * **OPERATION** : Specifies the operation to execute, this is required.
  * **Merge** : Merges the Actifio and production volume groups.
  * **Migrate** : Migrates volumes from Actifio disks to production disks.
  * **Recover** : Runs the Actifio scaleout recover script.
  * **RecoverMerge** : Runs **Recover** and **Merge**.
  * **RecoverMigrate.** Runs **Recover** and **Migrate**.
  * **Rollback.** Gets the cluster in a state where the restore can be attempted again.
  * **Test.** Can be used to test the job configuration.



**Optional parameters**

The script also provides these optional parameters to override any values.
    
    
        -a \<name\>: mount job name override
    
        -A \<log|params\>: Method to discover job name, log file or params file
    
        -C \<count\>: Expected node count override
    
        -D \<path\>: Path to the HANA data mount point, expected to be the same
        for all nodes
    
        -h: Display help documentation and exit, specify operation for more info
    
        -I \<name\>: HANA database SID override
    
        -K \<user\>: HANA keystore user to use for the restore
    
        -L \<path\>: Path to the HANA log mount point, expected to be the same
        for all nodes
    
        -r \<time\>: Timepoint to which to recover the HANA database
    
        -R: Assert that the recover script has already been run
    
        -S \<path\>: Path to the shared directory, expected to be the same for
        all nodes
    
        -t \<minutes\>: Number of minutes without an update before a job is
        considered timed out
    
        -T \<minutes\>: Number of minutes to allow for starting the HANA DB
        service
    
        -u \<user\>: HANA service account username \<adm user\>
    
        -v: Enable verbose logging
    
        -V \<version\>: HANA version
    
        -w \<seconds\>: Base wait time, job status checks 1x, file system
        operations 4x
    

**Note:** Log files are stored at `<HANA_SHARED_PATH>/<ACT_JOBNAME\>`. Don't edit the .job files.**Note:** If the HANA source and target sid are different, then you must rename the sid directory to the target sid  in the data and log mountpoints before running the `hana_lvm_recover_migrate.sh` script.

### Script options

**Recover**

Run the recovery option if you don't want to migrate the data to production storage.

`/act/custom_apps/saphana/lvm_migrate/hana_lvm_recover_migrate.sh recover`

By default, the script will fetch the latest Job# from the UDSAgent log and collect all the required information needed for the jobs such as target mount points and database SID. If the last job on this target server is not the mount then it will need to provide the **Job #** (using the -a option) of the last mount job to override the default value of mount job:

`/act/custom_apps/saphana/lvm_migrate/hana_lvm_recover_migrate.sh recover -a <Job_#>`

For point in time recovery to a specific point (use -r option)

`/act/custom_apps/saphana/lvm_migrate/hana_lvm_recover_migrate.sh recover -a <Job_#> -r <time>`

At the end of successful recovery the database is running out of backup/recovery appliance mounted devices.

**merge**

This option can be run post recovery operation from step A—for migration of data to production storage—when the database is running from the devices mounted from the appliance. During this process, the database is brought down and volume groups of production storage are merged with backup/recovery appliance volume groups. After successful merge operation, the database is brought online.

When the merge option is passed, the expectation is to have the recovery process for the database completed. If the recovery was done manually without using this script, then the user can specify -R option to confirm that recovery was run. If the recovery is not done, the script does not continue with the merge process.

`/act/custom_apps/saphana/lvm_migrate/hana_lvm_recover_migrate.sh merge`

**recovermerge**

Run the recovermerge option if you plan to migrate the data to production storage. The recovermerge option is the superset of recover and merge processes where the merge operation is done as part of the recovery. This avoids the restart of the database at the start of the migration process.

`/act/custom_apps/saphana/lvm_migrate/hana_lvm_recover_migrate.sh recovermerge`

If the last job on this target server is not the mount then it needs to provide the **Job #** , using the -a option, of the last mount job to override the default value of mount job:

`/act/custom_apps/saphana/lvm_migrate/hana_lvm_recover_migrate.sh recovermerge -a <Job_#>`

For point in time recovery to a specific point, use -r option:

`/act/custom_apps/saphana/lvm_migrate/hana_lvm_recover_migrate.sh recovermerge -a <Job_#> -r <time>`

After successful recovery, scripts continue to run the merge operation where volume groups of production storage is merged with backup/recovery appliance volume groups. During this process, the database is brought down and after successful merge operation, the database is brought online.

**Note:** In the scaleout configuration if the volume group names are the same across all the nodes, then the volume groups are renamed based on the node sequence.

**migrate**

Run the migrate option post recover or recovermerge run of the script and the system is ready to start the migration of data from backup/recovery appliance presented storage to production storage while the database is running.

`/act/custom_apps/saphana/lvm_migrate/hana_lvm_recover_migrate.sh migrate`

If the recovery is not done, the script does not continue with the migrate process. During the migrate process the script checks if the merge operation is done then it proceeds with migrating without restarting the database, otherwise it merges the volume groups of production storage with backup/recovery appliance volume groups. During this process, the database is brought down and after successful merge operation, the database is brought online.

**recovermigrate**

recovermigrate is a superset of recover, recovermerge and migrate operations. With this process, the database is recovered, volume groups of the disks provisioned from a backup/recovery appliance are merged with local storage, and a database migration is started.

The script is `/act/custom_apps/saphana/lvm_migrate/hana_lvm_recover_migrate.sh recovermigrate`.

If the last **Job** on this target server is not the mount then it needs to provide the **Job #** , using the -a option, of the last mount job to override the default value of mount job:

`/act/custom_apps/saphana/lvm_migrate/hana_lvm_recover_migrate.sh recovermigrate -a <Job_#>`

For point in time recovery to a specific point, use the -r option:

`/act/custom_apps/saphana/lvm_migrate/hana_lvm_recover_migrate.sh recovermigrate -a <Job_#> -r <time>`

For scale-out configuration, the migration is initiated in parallel across all the nodes of the cluster.

**Note:** In the scaleout configuration if the volume group names are the same across all the nodes, then the volume groups are renamed based on the node sequence.

Once the job is successful, the data is moved to the local production storage from disks provisioned from a backup/recovery appliance while the database is running.

**rollback**

The rollback option goes through job logs to identify the stage of the recover, merge, migrate, recovermerge, or recovermigrate job and revert any changes made to the database server. If the volume groups are merged between local production and backup/recovery appliance staging disks, then staging disk physical volumes are removed from production volume groups to perform the rollback operation.

`/act/custom_apps/saphana/lvm_migrate/hana_lvm_recover_migrate.sh rollback`

**test**

The **Test** operation can be used to ensure the environment is configured correctly to run before initiating any actual recovery operations. Since the **Test** operation does not make any changes, it can be run as many times as needed, or skipped entirely.

Ensure that the following are items checked during the test run:

  * Node check; this task runs in all operations.
  * Check if the expected node count matches the actual node count.
  * Check if SSH access is available to non-master nodes, if applicable.
  * Check if the nodes have access to the shared directory.



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

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
