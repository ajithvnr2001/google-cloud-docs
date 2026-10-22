---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/manage-image-expiration/
title: Manage expiration of backups \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:45.366811+00:00
---

# Manage expiration of backups  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/manage-image-expiration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Manage expiration of backups Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

You can force the expiration of a backup earlier than its scheduled date and time in order to gain storage space and potentially reduce storage costs.

You can manage backup expiration in the following ways:

  * From the **Application** page to expire all backups in an application.

  * From the **Table** view to expire one or more backups in an application.

  * From the **Timeline** view to expire only the selected backup.




## Backup expiration limitations

When you are configuring for backup expiration, consider the following limitations:

  * Certain backup types cannot be expired. If you select a backup that belongs to any of the types listed, you may not see the **Manage Expiration** option. You cannot expire backups that are of type:

    * failover
    * prep-mount
    * streamsnap
    * syncback
    * liveclone
  * The last backup of an unprotected application won't expire automatically; it must be expired manually.

  * Backups that use the **Enforced Retention** advanced policy setting to set an immutability date to a later date cannot be configured for expiration before the specified immutability period is over.

**Note:** The enforced retention advanced policy setting is not compatible with application protection that points to a backup vault. When a backup vault is the storage target, the backup vault determines the enforced retention period.



For more information on immutability and enforced retention, see [Configuring Advanced Settings: Policy Settings Override](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings).

## Managing backup expiration in the applications page

Use the following instructions to manage backup expiration for all backups in an application:

  1. Click the **App Manager** tab and select **Applications** from the drop-down menu.
  2. Right-click the application that has the backups you want to expire and select **Manage Expiration**.
  3. Optional. Disable the **Enable Scheduled Expiration** option. When you disable this option, backups that would have expired based on the configured schedule can no longer expire.
  4. Optional: Disable the **Enable Log Expiration** option. When you disable this option, a database log data that would have expired based on the configured retention can no longer expire.
  5. Select from the following expiration options:

     * **Expire all backups now** : When the scheduler runs next, expiration jobs start for these backups.
     * **Set new expiration date** : lets you select a new expiration date and time.
     * **Extend retention by** : lets you extend the expiration by the number of days or weeks or months or years you specify.
     * **Shorten retention by** : lets you shorten the expiration by the number of days or weeks or months or years you specify.
     * **Set all existing backups to never expire** : configure the backups to never expire. By default, backups that are set to never expire, will have an expiration date set to 2100-01-01. The **Copy Data List** view has an **Expiration** filter option **Never** that shows backups configured to never expire. For information on the **Copy Data List** view, see [Access backups in the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-list-and-yaml).
  6. Click **Apply**.




## Manage backup expiration from table view

Use the following instructions to manage backup expiration of one or more backups from the table view:

  1. Click the **App Manager** tab and select **Applications** from the drop-down menu. The **Applications** page opens.
  2. Right-click the application that has the backup(s) you want to expire and select **Access**. The **Timeline** view opens.
  3. Select the **Table** option. The **Backups** page opens listing captured backups in the table view.

  4. Click one or more backups, and then select **Manage Expiration** from the lower right corner of the page. Alternately, right-click the application and select **Manage Expiration**. The **Manage Expirations** dialog opens.

  5. Select from the following expiration options:

     * **Expire Now** : when the scheduler runs next, expiration jobs start for these backups.
     * **Set new expiration date** : lets you select a new expiration date and time.
     * **Extend retention by** : (default option) lets you extend the expiration by the number of days, weeks, months, or years you specify.
     * **Shorten retention by** : lets you shorten the expiration by the number of days, weeks, months, or years you specify.

When specifying a shortened retention period, the new expiration date for some backups may actually be a date in the past. In this situation, the dialog will list all backups that will have an expiration date set in the past along with a warning that these backups will expire immediately.

     * **Set to never expire** : configures the backups to never expire. By default, backups that are set to never expire will have an expiration date set to 2100-01-01. The **Copy Data List** view has an **Expiration** filter option **Never** that shows backups configured to never expire. For information on the **Copy Data List** view, see [Access backups in the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-list-and-yaml).
  6. Select one of the following **Log retention** options. This option displays only when the selected backup has associated logs.

     * **Do not change log retention** : select this option if you don't want to change log retention period. By default, this option is selected.
     * **Linked to database backup** : select this option to retain database logs until the database backup expires and the logs are past the configured log retention period.
     * **Independent from database backup** : select this option to retain all database logs for the selected database backups, regardless of when they expire.
  7. Click **Apply**.




## Manage backup expiration in the timeline view of the access page

Use the following instructions to manage expiration of a specific backup from the timeline ramp view:

  1. Click the **App Manager** tab and select **Applications** from the drop-down menu. The **Applications** page opens.
  2. Right-click the application that has the backup(s) you want to expire and select **Access**. The **Access** page opens listing captured backups in the **Timeline** view.
  3. Select the backup you want to manage expiration for, then select **Manage Expiration** from the menu options. The **Manage Expiration** page opens.

  4. Select from the following expiration options:

     * **Expire backups now** : forces the expiration job to run at that time and expire the backup.
     * **Set new expiration date** : lets you select a new expiration date and time.
     * **Extend retention by** : (default option) lets you extend the expiration by the number of days or weeks or months or years you specify.
     * **Shorten retention by** : lets you shorten the expiration by the number of days or weeks or months or years you specify.
     * **Set existing backups to never expire** : configure the backups to never expire. By default, backups that are set to never expire will have an expiration date set to 2100-01-01. The Copy Data List view has an **Expiration filter** option "Never" that shows backups configured to never expire. For information on the **Copy Data List** view, see [Access backups in the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-list-and-yaml).
     * **Do not change expiration date** : Select this option if you don't want to change the expiration date for a backup of a database. This option is displayed only when the selected backup has associated database logs.
  5. Select one of the following **Log retention** options. This option displays only when the selected backup has associated logs.

     * **Independent from database backup** (default): select this option to retain all database logs for the selected database backups, regardless of when they expire.
     * **Linked to database backup** : select this option to retain database logs until the database backup expires and the logs are past the configured log retention period. If a dependency between the backup and its log backups has been established, this option is selected by default.
  6. Click **Apply**.




## Force expiration of an active backup

To force the expiration of an active backup:

  1. Click the **App Manager** tab and select **Applications** from the drop-down menu. The Applications page opens.
  2. Select the application or VM that contains the captured backup that you want to expire, then choose **Access** from the drop-down list at the bottom right corner of the Applications page. The Access page opens listing captured backups in the Timeline ramp view. Backup types that support expiration include Snapshot, Remote Snapshot (StreamSnap backups), and OnVault. For more information about the Timeline view, see [Select an image from the timeline ramp view](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-list-and-yaml#access-time) for details.
  3. Select the backup that you want to expire, then select **Expire** from the drop-down list. The Expire page opens.
  4. Click **Submit** to expire the backup.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
