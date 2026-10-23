---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups/
title: About backups \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:14.298907+00:00
---

# About backups  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  About backups Stay organized with collections  Save and categorize content based on your preferences. 

This page describes backups, backup vaults, region groups, backup policies, prevent backup deletion, and selective file restore.

## Volume backups

NetApp Volumes supports volume backups, which are copies of your volumes stored independently from the volume. Backups are stored in backup vaults, which are containers for backups. If a volume is lost or deleted, you can use backups to restore your data to a new volume.

When you create the first backup of a volume, all of the volume's used data is sent to the backup vault. Subsequent backups of the same volume only include data that has changed from the previous backup. This allows for fast incremental-forever backups and reduces the required capacity inside the backup vault.

You can create manual and scheduled backups. Manual backups can be taken from a volume or from an existing volume snapshot. Scheduled backups require a backup policy.

### Considerations

  * You can restore backups of large capacity volumes only to a new large capacity volume. The regular volume backups can't be restored to large capacity volumes and the other way around.

  * Backups are supported with volume replication. Source volumes allow you to use scheduled backups or to create manual backups. For destination volumes, you must use manual backups. If you try to assign a backup policy to a destination volume, it will fail. When you reverse a volume replication direction, remove the backup policy first from the future destination volume.

  * Before you use VPC Service Controls, see [Limitations of VPC Service Controls for NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/service-perimeter#vpcsc-limitations) for more information.

  * If you have set a **Minimum enforced retention** policy on a backup vault that contains the backup, the backup can't be deleted before the scheduled date in the **Deletable on** field. For more information, see [Prevent backup deletion](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups#prevent_backup_deletion).

  * For Flex Unified iSCSI volumes, when creating a volume from a backup, make sure that the new volume size exactly matches the size of the original iSCSI LUN to avoid restore or access issues.

  * A backup of a Flex Unified volume can only be restored to a Flex Unified storage pool.




## Backup vaults

Backup vaults are logical containers that store volume backups. You can create multiple backup vaults within each region, and each vault can store multiple backups for multiple volumes in that region.

Backup vaults support customer-managed encryption keys (CMEK). When configured, CMEK encrypts all backups within the vault using the keys provided by the user.

There are two types of backup vaults that can exist in a region:

  * **In-region backup vaults** : store backups in the same region as the original volume.

  * **Cross-region backup vaults** : store backups of a volume in a different region. When you create a cross-region vault, a source vault is created in the volume region, and a destination vault is automatically created in the specified destination region. Both vaults store the backup metadata, but only the destination vault stores the actual backup data. This allows volumes and backups to exist in different regions.

The source vault and the volumes you want to backup must be in the same region.

You can restore backups from the source or destination vault by creating a new volume in the vault's location.

You must specify a name for the source vault while destination vaults are automatically named using the following template:

`<source_vault_name>-destination-<4-random-letters>`




### Considerations

  * Volumes can only store backups in one vault.

  * You can only backup a volume to a backup vault in the same region.

  * In-region backup vaults are generally available (GA) for all service levels. You can restore backups located in in-region vaults to any storage pool, for any service level, in the backup's region.

  * Cross-region backup vaults are supported for Flex Unified, Standard, Premium, and Extreme service levels and aren't available for the Flex File service level. You can restore backups located in cross-region vaults to any pool in either the source or destination backup vault location.

  * When you create a backup vault, you can optionally specify a minimum retention period to apply to each new backup stored in the vault. This retention period applies to all existing and future backups of the selected backup types stored in that vault. For more information, see [Prevent backup deletion](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups#prevent_backup_deletion).

  * You can't change the type of an existing backup vault.

  * You can configure CMEK on a backup vault only during vault creation. You can't configure CMEK on an existing vault.

  * You can't directly migrate volumes with existing backups from a standard backup vault to a CMEK vault. To migrate these volumes, complete the following steps:

    1. Disassociate the volume from its current standard backup vault.

    2. Delete all existing backups for that volume in the standard backup vault.

    3. Associate the volume with the required CMEK vault.

  * When using CMEK backup with cross-region backups, the CMEK policy must be created in the destination region.

  * You can create Flex Unified volume backups for Default-mode and ONTAP-mode and restore them to either mode. You can restore backups from other service levels to the Flex Unified service level, but you can't restore Flex Unified backups to other service levels.




## Region groups

You can create cross-region backup vaults between regions that are part of the same region group. However, you can only restore existing backups by creating a new volume in the source or destination backup vault region. For more information about region groups across different locations, see [volume replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication#considerations_for_volume_replication).

## Backup policies

Backup policies define a schedule for automated backup creation. You can specify how many daily, weekly, and monthly backups of the volume you want NetApp Volumes to retain. If a policy is attached to a volume and enabled, then backups are generated automatically.

The number of backups to store as defined in the policy must align with the retention period configured in the backup vault. For more information, see [Prevent backup deletion](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups#prevent_backup_deletion).

### Scheduled backups

Scheduled backups use the following backup name format to help you identify the exact point in time each backup was taken:

`(daily|weekly|monthly)-scheduled-backup-<id>-<timestamp>`

The timestamp is UTC in the following format:

`<YYYY>-<MM>-<DD>-<hhmmss>`

You can't specify the exact time a scheduled backup is created. Scheduled backups that use a backup policy retain the number of specified daily, weekly, and monthly backups. When the maximum amount of backups retained is reached, the oldest backup is deleted.

## Backup encryption with CMEK

**Note:** The CMEK backup feature is generally available (GA) for the Standard, Premium, Extreme, and Flex Unified service levels.

Backups are encrypted by default using Google-managed encryption key. You can also encrypt your backups using a customer-managed encryption key (CMEK).

### Considerations

  * CMEK backup supports both in-region and cross-region backups.

  * You can't convert an existing backup vault that uses Google-managed encryption to use customer-managed encryption.

  * Once you enable CMEK on a backup vault, you can't disable it.

  * All backup vaults and volumes within the same region must be associated with the same CMEK policy because only one policy is supported per region.

  * You must ensure CMEK access and availability. Losing access to keys can cause irrecoverable data loss.




## Prevent backup deletion

**Note:** The prevent backup deletion feature is supported for all service levels in the allow-listed General Availability (GA) and isn't enabled by default. To request access to this feature, contact [sales](https://cloud.google.com/contact).

The contents of a backup can't be modified. However, IAM users with the [appropriate permissions](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/iam) can delete backups. To protect against accidental or malicious deletions by administrators, you have the option to set a retention period for backups that prevents their deletion before that period expires.

### Considerations

  * You can enable this feature on a backup vault by specifying a retention period which must be between 2 to 5475 days, and the type of backups to retain.

  * You can choose to retain daily, weekly, monthly, or manual backups. You must select at least one backup type.

  * Each backup created in the vault is assigned an expiry date, calculated by adding the vault's retention period to the backup's creation time. The backup can't be deleted before this expiry date.

  * The scheduled backups are also protected by deletion prevention.

  * After you set the minimum retention period for a backup vault, the following considerations are applicable:

    * The minimum retention period for a backup vault is permanent and can only be increased, but can't be decreased. If you increase the retention period, it adds the extra time to the current expiry date of each existing backup within the vault.

    * The backup types you choose to retain can't be modified. However, you can add the new backup types.

    * Make sure that backups are scheduled and retained for a duration that meets or exceeds the defined backup retention period.

For example, if your backup policy specifies 14 daily backups, but you have set a retention period of 30 days for daily backups in the vault, the scheduler will cause issues. The system tries to delete the oldest daily backup after 14 days, but will be blocked until the 30-day retention period ends. It is essential to plan your retention period, the type of backups to retain, and your backup policy carefully. Note that a volume can hold a maximum of 1,000 backups, between manual and scheduled. Once this limit is reached, the older backups can't be deleted, and no new backups can be created.

    * You are charged for backups. If you use this feature, you can't delete backups before they reach their expiry date. Therefore, it is recommended to plan this feature usage carefully.

  * The enforced minimum retention period policy applies to all backups created after you set the policy. You can delete backups created before the policy was set without restriction.




## Selective file restore

Selective file restore lets you recover a single file or a set of files from a backup without restoring the entire volume. You can [restore](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/perform-selective-file-restore) the selected files to a new volume or the source volume.

This feature supports both in-region and cross-region backups.

### Considerations

  * Selective file restore is available only with Google Cloud CLI.

  * This feature supports the Flex Unified, Standard, Premium, and Extreme service levels and isn't available for the Flex File service level.

  * A restore job can support a minimum of one file and a maximum of eight files.

  * When restoring multiple files in a single job, all files must be restored to the same destination path.

  * When restoring files to a new volume, the destination volume's protocol must be the same as the source volume's protocol to preserve the file ACL information. If you restore between volumes that use NFSv3 and NFSv4.x, ACLs are preserved and applied according to the destination volume's protocol version.




## What's next

[Set up volume backups](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/set-up-volume-backups).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
