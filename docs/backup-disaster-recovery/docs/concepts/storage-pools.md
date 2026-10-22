---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/storage-pools/
title: Manage storage pools in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:05.833442+00:00
---

# Manage storage pools in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/storage-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Manage storage pools in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Backup/recovery appliances store data in these types of pools:

  * **Cloud** : Cloud type pools represent Cloud credentials used to back up Compute Engine instances, These pools are automatically created when a Cloud credential is created. They don't represent a pool of disk managed by the backup/recovery appliance. Only specify this type of pool in a [resource profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles) that is being used to back up Compute Engine instances.

  * OnVault: OnVault pools provide long-term storage using Cloud Storage buckets.

  * [Snapshot](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/snapshot-pool): Snapshot pools contain your most recent backups and restored backups. They enable instant access to your data. For more on the snapshot pool, see [Snapshot pools](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/snapshot-pool).


**Note:** The **Primary Pool** —act_pri_pool000—is for the backup/recovery appliance's system data. Don't change the primary pool unless instructed by Support.

You can view the storage pools by navigating to **Manage** > **Storage Pools**. From there, you can do the following:

  * View information related to the storage pools, such as pool name, appliance, warning and safe mode levels. See [Configure the alert levels for storage pools and resource profiles](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/storage-pools-about#alerts).



## OnVault pools

OnVault pool storage is typically used for long-term retention of data. When sending data to Cloud Storage buckets defined by an OnVault pool, the OnVault pool's compression option is on by default to minimize network traffic and storage consumption.

OnVault pools can use Google nearline, coldline and archive class storage. To create an OnVault pool, see [Use OnVault pools](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/using-onvault-pools). You can also adjust the pool warning and safe percentages. See [Configure the alert levels for storage pools and resource profiles](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/storage-pools-about#alerts).

After the initial ingest of the full backup, only the changes to data are sent to the OnVault Pool. This is the same incremental forever model used by other Backup and DR policies.

When accessing data in an OnVault pool's storage:

  * Backup/recovery appliances can create clones.

  * Backup/recovery appliances can mount data.

  * Backup/recovery appliances can perform restores.

  * LiveClones cannot be created.




## Mirror pool, snapshot pool for replicated data

Use these instructions to select the destination snapshot pool that is to be used to store the incoming StreamSnap replication data:

  1. Click **Manage** and select **Appliances** from the drop-down menu.
  2. Select an appliance.
  3. Click **Configure Appliance** to open the **Appliance Configuration** page.
  4. Go to **System** > **Configuration** > **Storage Pools**.
  5. Click the **Storage** tab. A drop-down menu appears where you can select the destination snapshot pool for replicated data that comes to this backup/recovery appliance.
  6. Click the gray **Save Settings** button.



## View storage pool information

Use the instructions to view information for the storage pools associated with each backup/recovery appliance managed by the appliance management console.

  1. Click **Manage** and select **Storage Pools** from the drop-down menu.

The **Storage Pools** page opens.

  2. To modify the display, you can do the following:

     * **Adjust Fields** : To modify the fields that appear in the table, right-click within the table header row and click the checkboxes for the fields you want displayed—or those fields you don't want to view.
     * **Sort Content** : To sort the content listed in a table column by alphanumeric order, select a column header and then click the up or down arrow to change the order.
     * **Adjust Column Width** : To adjust the width of a table column to show more content in the table, drag the column divider in a column header to the left or right to resize the column width. Column dividers are marked by a pair of thin gray lines.
     * **Filter By** : To filter the list, enter one or more filter criteria as appropriate. If you don't see the **Filter By** area, click **show filter**. To clear a filter, click the **x** to the right of the applied filter.

**Note:** Filters that are of type text, list, and date, persist across different appliance management console sessions for the same user.
  3. Click the export icon to export the storage pools list. You can export in PDF format.

  4. Select from the drop-down list at the bottom of the table to modify the number of rows displayed in a table page, you can. Choices include 10, 25, 50, 100, or 500 rows per table page.




## Configure the alert levels for storage pools and resource profiles

You can configure two usage alert levels, warning and safe mode, for the snapshot pools.

**Note:** Do not change these settings unless advised by support. If a snapshot pool fills to 100%, snapshots can be brought offline and become unrecoverable.

When the snapshot pool reaches its safe limit, the backup/recovery appliance:

  * Issues an alert that the stored data exceeds the configured warning limit.
  * Stops running new jobs that writes to the snapshot pool.



Use these instructions to configure the usage level:

**Note:** Don't change the default settings unless advised by support.

  1. Click **Manage** and select **Appliances** from the drop-down menu.

The **Appliances** page opens.

  2. Select an appliance.

  3. Click **Configure Appliance** to open the **Appliance Configuration** page.

  4. Go to **System** > **Configuration** > **Storage Pools**.

  5. Select the **Snapshot** or **Primary** tab.

The default warning level is 80% for the snapshot and primary pools. When this level is exceeded, warnings are displayed.

  6. Set **Safe Mode** to an appropriate level of usage. The default value is 90% for the snapshot and primary pools. When this value is exceeded, the backup/recovery appliance stops writing to storage.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
