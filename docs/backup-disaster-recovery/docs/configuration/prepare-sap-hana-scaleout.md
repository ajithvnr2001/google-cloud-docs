---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sap-hana-scaleout/
title: Prepare SAP HANA scale-out databases for Backup and DR on a backup/recovery appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:16.827604+00:00
---

# Prepare SAP HANA scale-out databases for Backup and DR on a backup/recovery appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sap-hana-scaleout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Prepare SAP HANA scale-out databases for Backup and DR on a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Before you back up HANA database instances and data, you must add the database server as a host to Backup and DR. Before you begin, be sure to follow these preparation steps.

**Note:** This information is for SAP HANA scale-out instances. For Scale-Up and HA 1+1 configurations, see [Backup and DR for SAP HANA](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana).

## Prerequisites

Before you begin, it's a good idea to review [Backup and DR for SAP HANA scale-out](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-sap-hana-scaleout).

  * All the configured services—see SAP Note 1697613 and SAP Note 1649519— such as `nameserver` and `indexserver`. must be running. You can check this in the Overview of SAP HANA studio > Operational State > Confirm all services are started.

  * To allow the Backup and DR agent to perform host-side operations, use an SAP HANA `hdbuserstore` key instead of a username and password to communicate with HANA database using the SAP HANA secure userstore. See [Configure the HANA userstore key](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-hana#configuring_the_hana_userstore_key).

  * Database `log_mode` must be set to **normal** under the HANA Studio configuration tab. See Set up the log mode and log backup in HANA Studio.

  * All SAP HANA servers that have HANA data to be protected by Backup and DR must have been onboarded to Backup and DR.

  * All SAP HANA servers that have data to be protected by Backup and DR must have the Backup and DR agent installed.

  * If the underlying data volumes for SAP HANA are protected as SAP HANA database backups using LVM snapshot with CBT or file-based backup integrated with `backint`, and if you are also protecting file systems on the same host, in the file system app, you should set `/hana/log` & `/hana/data` in an exclude path. See [Linux file system](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-linux-hosts).

  * HANA Archive log backup recommendation:

    * Make sure to set the HANA Archive log backup path as the `basepath_logbackup` and `basepath_catalogbackup` in global.ini.
    * Don't use HANA Archive log mount to store files other than HANA Archive log backup.
    * By default, archive purge runs with every database backup. To achieve best recovery RTO, keep the default setting.

**Note:** If production log retention is set, then purge runs based on the **Retention of production db logs in hour** setting under Application Details & Settings. Size the HANA archive log backup disk to store archives based on the production log retention setting.

## Configure the HANA userstore key

**Note:** This procedure requires the hostname.

Use the following instructions to configure the HANA userstore key:

  1. Create the database backup user from HANA Studio.

  2. Get the instance and SQL port numbers.

  3. Create the SAP HANA `hdbuserstore` key for system DB backup users.




### Step 1: Create the database backup user from HANA Studio

Choose a database username based on the company's standard. Make sure to create this user account under `SYSTEMDB`.

  1. Create the user under `SYSTEMDB`

     * From SAP HANA Studio SYSTEMDB, go to **System** > **Security** > **Users** > **New User**.

     * Assign a username and a password.

     * Set **Force password change on next logon** to **No**.

     * Click the **System privilege tab** and assign privileges by selecting the following:

### HANA 1.0

     * **Backup admin**
     * **Catalog read**
     * **Database admin**

### HANA 2.0 (SPS01-SPS04)

     * **Backup admin**
     * **Catalog read**
     * **Database admin**
     * **Database start**
     * **Database stop**

### HANA 2.0 (SPS05)

     * **Backup admin**
     * **Catalog read**
     * **Database backup operator**
     * **Database recovery operator**
     * **Database admin**
     * **Database start**
     * **Database stop**

  2. Deploy the newly created system user by clicking the **green arrow**.




### Step 2: Get the instance and SQL port numbers

You need the HANA instance and SQL port numbers for system databases.

### HANA 1.0

The following instructions describe how to get the instance and SQL port numbers from a HANA 1.0 single container system:

  1. Go to **System**.

  2. Click the **Landscape** tab.

  3. Get the value of SQL port for `indexserver`.




### HANA 2.0

The following instructions describe how to get the instance and SQL port numbers from HANA 2.0:

  1. Go to **System**.

  2. Click the **Landscape** tab.

  3. Click the **Services** tab.

  4. Under the **Service** column, navigate to the `nameserver`.

  5. Get the value of SQL port. The instance number are the second and third digits of the SQL port number.




### Step 3: Create the SAP HANA hdbuserstore key for system database backup users

Backup and DR recommends this naming convention for the userstore key name: For SYSTEMDB, set the key name to `Database backup username`. For example: Database backup username (`Actbackup`) Set SYSTEMDB—key_name— (`ACTBACKUP`)

**Procedure for single node HANA system**

  1. Connect to the HANA database system using SSH and login to (sid)adm: `su - (sid)adm`

  2. Change directory: `cd exe`

  3. Create entries in hdbuserstore using command `hdbuserstore`:
         
         ./hdbuserstore SET (key_name) (SAP HANA database hostname):(port) (DB_user_name) (DB_user_password)
         

In this example:
         
         ./hdbuserstore SET ACTBACKUP s4hana:30013 ACTBACKUP (DB_user_password)
         

  4. Check the keystore: `./hdbuserstore list`


**Note:** If the hostname is not included, you will get the error: `ERRORMSG: USERSTORE KEY - Does not have valid hostname configured!`

## Set up the log mode and log backup in HANA Studio

Use the HANA Studio set the HANA log mode and log backup location for Backup and DR to take backups of HANA DB transaction logs:

  1. In SAP HANA HDB studio, make sure log backup is set correctly under **DATABASE (SYSTEMDB FOR HANA 2.0)** > **Backup** > **Configuration** page:

     * Destination type is **File**.

     * Destination is set to a local file system mount path.

     * Backup interval is set to **required RPO**.

     * Automatic log backup is enabled.

     * Database log_mode must be set to **normal**.

  2. Check under Database configuration: DATABASE (SYSTEMDB FOR HANA 2.0) > Configuration page. In the filter, type **basepath**.

  3. Verify that `basepath_logbackup` is set correctly:

     * Set the `basepath_catalogbackup` to the same as `basepath_logbackup`.

     * Open the `basepath_catalogbackup` edit page.

     * Set the **New value** to the same as `basepath_logbackup` and click **Save**. This ensures the backup of the catalog with log backup for point in time recovery.

  4. Run the re-config for the values to take effect.




## Install the Backup and DR agent (connector) on SAP HANA Servers

The Backup and DR agent, a small-footprint, lightweight service on the SAP HANA server, is used to capture an application-consistent copy of SAP HANA databases. It uses changed block tracking to identify changes to database data for Backup and DR's incremental forever capture strategy. All SAP HANA servers that have data to be protected by Backup and DR must have the Backup and DR agent installed.

  1. Download the agent installer file as detailed in [Obtain the right Backup and DR agent for your host](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/about-connector#right-connector)

  2. Log on to the Linux server as root.

  3. Install the agent as detailed in [Install the Backup and DR agent on a Linux host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent)




## What's next

[Add an SAP HANA database host, and discover and protect its databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-sap-hana)

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
