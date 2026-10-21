---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-sql-server-into-backup-vault/
title: Back up a Microsoft SQL Server database into a backup vault using the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:12.034819+00:00
---

# Back up a Microsoft SQL Server database into a backup vault using the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/backup-sql-server-into-backup-vault/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Back up a Microsoft SQL Server database into a backup vault using the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page describes how to back up Microsoft SQL Server database into a backup vault.

Microsoft SQL Server database backups can be stored in regional backup vaults. Sending backups to a backup vault provides protection against modification (immutability) and deletion (indelibility). For more information about backup vault, see [Overview of backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault).

With a backup vault, you can store backups in a single region. If you need backups in multiple regions, consider the following options:

  * You can define a backup plan and resource profile that sends backups to two or more OnVault pools with two or more backup vaults. Create these backup vaults in different regions, which provides dual-region protection for your backups. Note that you will be charged for the storage in each backup vault separately.
  * Define an OnVault pool that uses a multi-regional Cloud Storage bucket. Note that this option doesn't provide the protection against modification and deletion that a backup vault provides.



## Before you begin

Before you protect SQL server databases into a backup vault, you must add the hosts and discover their databases using the appliance management console SQL Server wizard as detailed in [Add a SQL Server database host and discover databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-sql-server).

## Back up Microsoft SQL Server into a backup vault

Backing up Microsoft SQL Server into a backup vault involves the following steps.

  1. Create a backup vault

  2. Register a backup/recovery appliance as an authorized accessor for a backup vault

  3. Create an OnVault pool associated with backup vault

  4. Create a profile associated with the backup vault

  5. Create a template

  6. Apply a backup plan to protect a Microsoft SQL Server database




## Create a backup vault

A Backup vault is a container to store backups. To back up a Microsoft SQL server database to a backup vault, you need to create a [backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault). For instructions, see [Create and manage a backup vault in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create). 

## Register a backup/recovery appliance as an authorized accessor for a backup vault

You can access a backup vault from the backup/recovery appliance project only after the appliance service account is granted with the Backup and DR Backup Vault Accessor (`roles/backupdr.backupvaultAccessor`) IAM role in the backup vault project. Without this role, you cannot access the backup vault to complete the setup to enable backup creation. For instructions, see [Grant roles to the backup/recovery appliance service account](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create#service-account).

**Note:** The backup/recovery appliance and the backup vault don't need to be in the same project.

## Create an OnVault pool associated with a backup vault

OnVault pools created with the backup vault type store data in the backup vault. A backup vault with a minimum enforced retention period prevents the deletion of backups before the enforced retention period is met.

Backup/recovery appliances that are registered with the backup vault pool type are displayed for selection.

Use the following instructions to create an OnVault pool that points to a backup vault.

  1. In the Backup and DR appliance management console, click **Manage** and select **Storage pools** from the menu.
  2. Click **Add OnVault pool**.
  3. Enter a name for the pool. Valid characters are letters, numbers, spaces, hyphens (-), and underscores (_).
  4. Check that the **Pool type** is set to **Backup vault**.
  5. From the **Appliance** list, select the appliance you want to add the OnVault pool to. If your appliance is not available to select, you will need to [updated the appliance](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance) to the latest version.
  6. In the **Project ID** field, enter the Google Cloud project that contains your backup vault.
  7. From the **Region** list, select the region that contains your backup vault.
  8. From the **Choose a backup vault** section, select a backup vault.
  9. Click **Save**.



## Create a profile associated with a backup vault based OnVault pool

A resource profile specifies the storage medium for Microsoft SQL server backups. You can use a backup vault, a specialized storage for Backup and DR backups, designed with features that support resilience against malicious or accidental deletion of backups. After the profile is created and designated for use with backup vaults, the profile cannot be edited to use a different storage pool type and a backup vault must always be specified. Also, if the resource profile is in use to protect an application, the specified backup vaults cannot be changed. 

Use the following instructions to create a resource profile which points to a backup vault.

  1. In the Backup and DR appliance management console, click **Backup plans** and select **Profiles** from the menu.
  2. Click **Create profile**.
  3. Enter a name and optional description for the resource profile.
  4. Select **Use OnVault pools that point to backup vaults (Recommended)**.
  5. In the **Primary appliance** section, from the **Appliance** list, select the appliance type that the backup pool type is associated with.
  6. From the **Snapshot pool** list, select a snapshot pool type.
  7. From the **OnVault pool 1** list, select the OnVault pool associated with your backup vault.
  8. Optional. From the **OnVault pool 2** list, select the OnVault pool associated with your backup vault that is created in a different region.
  9. Click **Save profile**.



## Create a template with the backup policies

A backup plan template defines backup creation and management details, such as the backup schedule and the timeline for backup deletion. Backup plan templates are created within the appliance management console. Create a backup template using the instructions in [Manage backup templates](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template).

## Apply a backup plan to protect a Microsoft SQL server

Use the following instructions to apply a backup plan to protect a Microsoft SQL server database.

  1. From the Backup and DR appliance management console, go to **App Manager** > **Applications**. The **Applications** page opens.

  2. Select the Microsoft SQL server database, instance, AG, or consistency group that you want to back up and in the lower right corner of the page select **Manage Backup Plan**.

  3. From the **Manage Backup Plan** window, choose a **Template** and **Profile** from the drop-down lists:

     * **Template.** An existing backup template that includes policies to define the snapshot and replication of the application data.

     * **Profile.** An existing resource profile that defines the resources used to store the data of the application as snapshot and replicated images.

  4. From the **Manage Backup Plan Template** window make the following changes prior to applying a backup plan:

     * **Application Settings.** Settings specific to Microsoft SQL such as application type, hostname, host IP address, path, operating system, backup/recovery appliance, and appliance IP address.

     * **Policy Overrides.** Override specific policy settings previously configured in the selected backup template. Policy overrides can be useful or required in certain circumstances. You can only override policy settings if the policy's template has been configured to allow policy settings overrides.

  5. To select databases, under **Database Inclusion Rule** , click **Edit**. The **Manage Membership** dialog opens.

     * From the **Manage Membership** dialog, select the databases to back up by assigning an inclusion rule (**All** , **System Databases** , **User Databases**), and then select whether the rule should **Include Selected** or **Exclude Selected**.

     * Click **Save** and the **Manage Membership** dialog closes.

  6. Click **Apply** to apply the backup template and resource profile and the success message box appears.

The first time the selected database is discovered, an on-demand job runs as soon as possible to protect the data. Afterward, new data is backed up when the scheduled job runs according to the hours of operations defined in the backup template. For example, if at 10:00 (UTC) you assign a template that has hours of operation from 02:00 to 05:00 (UTC), then the first job won't start until the appliance has an available job slot after 02:00 (UTC).

If you back up a workload to a backup/recovery appliance that would exceed its recommended storage capacity or snapshot limit, you will see a notification with a recommendation to back up the data to a different backup/recovery appliance.

**Caution:** Exceeding the capacity of a backup/recovery appliance can lead to failed jobs and unprotected data and failed restore operations.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
