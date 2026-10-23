---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/csql-quickstart/
title: Protect and recover a Cloud SQL instance to a backup vault \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:31.738290+00:00
---

# Protect and recover a Cloud SQL instance to a backup vault  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/csql-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Protect and recover a Cloud SQL instance to a backup vault

Learn how to protect and restore a Cloud SQL instance to a backup vault. In this quickstart, you'll learn how to configure a scheduled backup for a Cloud SQL instance, back up a Cloud SQL instance into a backup vault, and restore a Cloud SQL instance from a vaulted backup.

## Before you begin

  1. Enable the Backup and DR API in your Google Cloud project.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=backupdr.googleapis.com&_ga=2.145630134.30427899.1640890668-1982243420.1634228058)

  2. [Create a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create). Backup vaults provide protection for backups by storing them in secure, isolated, and specialized storage. For more information about backup vaults, see [Overview of backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault).

  3. [Create a backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create).

  4. **For CMEK-enabled instances** : if the source Cloud SQL instance is protected with a Customer-Managed Encryption Key (CMEK), you must grant the `roles/cloudkms.cryptoKeyEncrypterDecrypter` Identity and Access Management role to the Backup and DR service agent. This permission is required on the Cloud Key Management Service key used by the source Cloud SQL instance.

The Backup and DR service agent is in the project where the backup vault is located. Grant this role to the service agent before attempting to protect CMEK-enabled Cloud SQL instances.




## Grant a role to the backup vault service agent

Every backup vault created has a unique service agent linked to it. For Cloud SQL instances, the service agent performs actions on behalf of the Backup and DR, so it needs appropriate permissions on the projects it needs to access.

Use the following instructions to grant a role to the service agent.

  1. In the Google Cloud console, go to the **Backup vaults** page.

[Go to Backup vaults](https://console.cloud.google.com/backupdr/backup-vaults/list)

  2. Click the backup vault name and copy the service agent's email address.

  3. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  4. In the **New principals** field, enter the service agent's email address.

  5. From the **Select a role** list, select the **BackupDR Cloud SQL Operator** (`roles/backupdr.cloudSqlOperator`) role.

  6. Click **Add another role**.

  7. From the **Select a role** list, select the **Service Account User** (`roles/iam.serviceAccountUser`) role.

  8. Click **Save**.




## Back up a Cloud SQL instance into a backup vault

In the Google Cloud console, you can back up Cloud SQL instances to a backup vault by applying backup plans. You can back up in either of these two ways: Scheduled backups and On-demand backups.

### Configure a scheduled backup

Use the following instructions to configure a scheduled backup for Cloud SQL instances.

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

  2. Click **Schedule backup**.

  3. From the **Resource Type** list, select **Cloud SQL**.

  4. From the **Project** list, select the project where the Cloud SQL instance is located.

  5. From the **Region** list, select the region where your instances are located.

  6. From the **Resources** list, click **Browse**. Choose the Cloud SQL instance that you want to back up and click **Done**.

  7. Click **Continue**.

  8. From the **Backup plan** list, click **Select**.

  9. Choose a backup plan that you want to protect the Cloud SQL instance with.

  10. Click **Done**.

  11. Review the backup details and click **Schedule**.

As the backup window is set to six hours, you can take an on-demand backup of the Cloud SQL instance.

**Note:** The first backup is automatically triggered when the current time is within the backup window.



### Take an on-demand backup

Initiate an on-demand backup for a Cloud SQL instance with a backup plan by triggering an existing backup rule to run immediately, or by specifying a user-defined custom retention period.

Use the following instructions to create an on-demand backup.

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

The **Vaulted backups** page lists only the data resources that have backup plans applied and their backups stored in a backup vault within that project.

  2. Select the resource to back up. Either from the more_vert menu, or from the details page for the resource, select **Create on-demand backup**.

  3. In the **Create an on-demand backup** window, select a backup rule to use and click **Create**.

  4. To view the status of the on-demand backup job, click **Notifications**.

**Note:** The on-demand backup is stored in the backup vault that is configured with the associated backup plan.
  5. In the Google Cloud console, go to the **Jobs** page to view the backup operation status.

[Go to Jobs](https://console.cloud.google.com/backupdr/jobs)




## Restore a Cloud SQL instance from a backup

You can restore a Cloud SQL instance to the same project or to a different project.

Use the following instructions to restore a Cloud SQL instance into a backup vault from a backup.

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

The **Vaulted backups** page lists only the instances that have backup plans applied and their backups stored in a backup vault within a project.

  2. Select the backup that you want to restore. Either from the backup details page for the backup, or from the **More actions** (more_vert) menu, select **Restore**.

The **Restore page** displays where you select the following restore options:

     * The **Resource type** is prefilled with `Cloud SQL`.

     * In **Resource name** , select the Cloud SQL instance to restore.

     * When you click **Backup** , a pane opens showing all available backups. Select the specific backup to restore.

     * For **Choose the restore destination** , select the project into which you want to restore the Cloud SQL instance.

     1. Click **Continue**.

     2. The next page shows the restore details so far, and prompts you to **Choose restore destination** , with these options:

        * **Restore to a new instance** : This creates a new instance based on the configuration stored in your backup. You can customise the instance after the restore is complete. Provide a new **Instance ID** using lowercase letters, numbers, and hyphens. Start with a letter.
**Note:** When restoring a Cloud SQL instance from a CMEK-encrypted backup, the restored instance will, by default, be encrypted using the same Cloud Key Management Service key that protected the source instance's disk at the time of backup. You have the option to specify a different Cloud KMS key for the target instance during the restore process.**Note:** During cross-region restores to a new instance, it's required to re-encrypt the restored Cloud SQL instance with a different Cloud Key Management Service key that resides in the restored target's region (not applicable when overwriting an existing instance).
        * **Overwrite an existing instance** : Select an existing instance to overwrite from the list of available instances.

        * **Overwrite the source instance** : This will overwrite your current instance. All the current data on the selected instance will be overwritten, including previous point-in-time recovery logs. The overwritten data cannot be recovered later. This is not recommended for production use.

  3. In the Google Cloud console, go to the **Jobs** page to view the restore operation status.

[Go to Jobs](https://console.cloud.google.com/backupdr/jobs)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

Use the following instructions to remove the backup plan from the backed up Cloud SQL instance.

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-resources)

  2. Select the backed up instance.

  3. Click **Remove backup plan**.

**Note:** The backup automatically expires and is deleted after the retention period that you set expires.



### Delete the backup plan

Optionally, if you want to delete the backup plan, do the following:

  1. In the Google Cloud console, go to the **Backup plans** page.

[Go to Backup plans](https://console.cloud.google.com/backupdr/backup-plans/list)

  2. Select the backup plan and click **Delete**.

This deletes the backup plan and related contents.




### Delete the backup vault

Optionally, if you want to delete the backup vault, do the following:

  1. In the Google Cloud console, go to the **Backup vaults** page.

[Go to Backup vaults](https://console.cloud.google.com/backupdr/backup-vaults/list)

  2. Click the backup vault and click **Delete**.

This deletes the backup vault and related contents.

**Note:** The backup vault incurs a cost only when the backup vault stores data. The existence of a backup plan doesn't incur any cost.



## What's next

  * Read the [Backup and DR product overview](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr).
  * Learn about [backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault).
  * Learn about [backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
