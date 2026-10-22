---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/alloydb-quickstart/
title: Protect and recover an AlloyDB cluster to a backup vault \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:57.833388+00:00
---

# Protect and recover an AlloyDB cluster to a backup vault  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/alloydb-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Protect and recover an AlloyDB cluster to a backup vault Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to use Backup and DR to protect an AlloyDB cluster with immutable storage and restore it in the event of data loss.

In this quickstart, you complete the following tasks:

  * Configure a scheduled backup for an AlloyDB cluster.
  * Take an on-demand backup of an AlloyDB cluster into a backup vault.
  * Restore an AlloyDB cluster from a vaulted backup.



## Before you begin

  1. Enable the Backup and DR API in your Google Cloud project.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=backupdr.googleapis.com&_ga=2.145630134.30427899.1640890668-1982243420.1634228058)

  2. [Create a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create).

Backup vaults provide protection for backups by storing them in secure, isolated, and specialized storage. For more information about backup vaults, see [Overview of backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault).

  3. [Create a backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create).

  4. Add the **BackupDR AlloyDB Operator** (`roles/backupdr.alloydbOperator`) role in the project that has the AlloyDB cluster to be backed up.




## Grant a role to the backup vault service agent

Every backup vault created has a unique service agent linked to it. For AlloyDB clusters, the service agent performs actions on behalf of the Backup and DR, so it needs appropriate permissions on the projects it needs to access.

Use the following instructions to grant a role to the service agent.

  1. In the Google Cloud console, go to the **Backup vaults** page.

[Go to Backup vaults](https://console.cloud.google.com/backupdr/backup-vaults/list)

  2. Click the backup vault name and copy the service agent's email address.

  3. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  4. In the **New principals** field, enter the service agent's email address.

  5. From the **Select a role** list, select the **BackupDR AlloyDB Operator** (`roles/backupdr.alloydbOperator`) role.

  6. Click **Add another role**. Add the following roles from the **Select a role** list:

     * **Service Account User** (`roles/iam.serviceAccountUser`)

     * **Cloud KMS CryptoKey Encrypter/Decrypter** (`roles/cloudkms.cryptoKeyEncrypterDecrypter`), which is required on the backup vault encryption key.

  7. Click **Save**.




## Back up an AlloyDB cluster into a backup vault

In the Google Cloud console, you can back up AlloyDB clusters to a backup vault by applying backup plans. You can back up in either of these ways: **Scheduled backups** and **On-demand backups**.

### Configure a scheduled backup

Use the following instructions to configure a scheduled backup for AlloyDB clusters.

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

  2. Click **Schedule backup**.

  3. From the **Resource Type** list, select **AlloyDB**.

  4. From the **Project** list, select the project where the AlloyDB cluster is located.

  5. From the **Region** list, select the region where your clusters are located.

  6. From the **Resources** list, click **Browse**. Choose the AlloyDB cluster that you want to back up and click **Done**.

  7. Click **Continue**.

  8. From the **Backup plan** list, click **Select**.

  9. Choose a backup plan that you want to protect the AlloyDB cluster with.

  10. Click **Done**.

  11. Review the backup details and click **Schedule**.

Because the backup window is set to six hours, you can take an on-demand backup of the AlloyDB cluster.

**Note:** The first backup is automatically triggered when the current time is within the backup window.



## Take an on-demand backup

Initiate an on-demand backup for an AlloyDB cluster with a backup plan by triggering the backup rule to run immediately.

Use the following instructions to create an on-demand backup.

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

The **Vaulted backups** page lists only the data resources that have backup plans applied and their backups stored in a backup vault within that project.

  2. Select the resource to back up. Either from the more_vert menu, or from the details page for the resource, select **Create on-demand backup**.

  3. In the **Create an on-demand backup** window, select a backup rule to use and click **Create**.

  4. To view the status of the on-demand backup job, click **Notifications**.

**Note:** The on-demand backup is stored in the backup vault that is configured with the associated backup plan.
  5. Optional: To view the backup operation status, go to the **Jobs** page to view the backup operation status.

[Go to Jobs](https://console.cloud.google.com/backupdr/jobs)




## Restore an AlloyDB cluster from a backup

You can restore an AlloyDB cluster to the same project or to a different project.

To restore an AlloyDB cluster into a backup vault from a backup, use the following instructions.

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

The **Vaulted backups** page lists only the clusters that have backup plans applied and their backups stored in a backup vault within a project.

  2. Select the backup that you want to restore. Either from the backup details page for the backup, or from the more_vert menu, select **Restore**.

The **Restore page** displays where you select the following restore options:

     * The **Resource type** is prefilled with `AlloyDB`.
     * In **Resource name** , select the AlloyDB cluster to restore.
     * When you click **Backup** , a pane opens showing all available backups. Select the specific backup to restore.
     * For **Choose the restore destination** , select the project into which you want to restore the AlloyDB cluster.
     * Click **Continue**.
     * The next page shows the restore details so far, and prompts you to **Configure a new cluster** : This creates a new AlloyDB cluster based on the configuration stored in your backup. You can customize the cluster after the restore is complete. Provide a new **Cluster ID** using lowercase letters, numbers, and hyphens. Start with a letter.
     * Choose a private connection method: There are two methods to connect services in Google Cloud or third party-hosted VPC networks, without assigning external IP addresses: 
       * **Private services access** : Assigns the cluster to a single VPC network using a peering connection. Use this when connecting to specific Google Cloud and third-party services in the same VPC network as the AlloyDB cluster. This requires additional APIs.
       * **Private Service Connect** : Enables cluster access from one or more VPC networks using allowlists and PSC endpoints.
  3. Optional: To view the restore operation status, go to the **Jobs** page to view the restore operation status.

[Go to Jobs](https://console.cloud.google.com/backupdr/jobs)




## Clean up

To avoid incurring charges to your Google Cloud account, remember to delete the resources used on this page if you have no further use for them.

### Remove the backup plan from the AlloyDB cluster

To remove the backup plan from the backed up AlloyDB cluster, use the following instructions.

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-resources)

  2. Select the backed up cluster.

  3. Click **Remove backup plan**.

**Note:** The backup automatically expires and gets deleted after the retention period that you set.



### Delete the backup plan

Use the following instructions to delete the backup plan. Deleting the backup plan is an optional step.

  1. In the Google Cloud console, go to the **Backup plans** page.

[Go to Backup plans](https://console.cloud.google.com/backupdr/backup-plans/list)

  2. Select the backup plan and click **Delete**.

This deletes the backup plan and related contents.




### Delete the backup vault

Use the following instructions to delete the backup vault. Deleting the backup vault is an optional step.

  1. In the Google Cloud console, go to the **Backup vaults** page.

[Go to Backup vaults](https://console.cloud.google.com/backupdr/backup-vaults/list)

     1. Click the backup vault and click **Delete**.

This deletes the backup vault and related contents.


**Note:** The backup vault incurs a cost only when the backup vault stores data. The existence of a backup plan doesn't incur any cost.

## What's next

  * Read the [Backup and DR product overview](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr).
  * Learn about [backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault).
  * Learn about [backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
