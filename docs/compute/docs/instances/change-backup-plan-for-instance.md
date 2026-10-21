---
url: https://docs.cloud.google.com/compute/docs/instances/change-backup-plan-for-instance/
title: Change your instance's backup plan \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:31:33.226644+00:00
---

# Change your instance's backup plan  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/change-backup-plan-for-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Change your instance's backup plan Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information about how to apply a backup plan, or change the backup plan that is applied, to your Compute Engine instance. You can configure your compute instance's backup plan to align your data protection strategy with your changing operational requirements.

Backup and DR backup plans let you define advanced backup strategies to store your compute instances in secure storage locations called backup vaults. Using the backup plan that's applied to your compute instance, you can create scheduled or on-demand backups of your instance in a backup vault.

## Before you begin

  * Enable the Backup and DR Service API where the Compute Engine instances are located. 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=backupdr.googleapis.com&_ga=2.145630134.30427899.1640890668-1982243420.1634228058)

  * [ Create a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create)
  * [ Create a backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create)
  * Set up Observability Analytics on your bucket to monitor Backup and DR backup jobs.



### Required roles

  * To get the permissions that you need to edit a compute instance's properties and change the associated backup plan, ask your administrator to grant you the following IAM roles: 

    * To edit the compute instance: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on the project for the compute instance 
    * To configure scheduled backups or run on-demand backups: 
      * [Backup and DR Backup User ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`) on the project for the backup vault
      * [Viewer ](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`) on the project for the backup vault

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * If you want to back up a compute instance to a backup vault that is in a different project than the compute instance, then make sure that the [ Backup and DR Vault Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#backup-and-dr-vault-service-agent) for the project that contains the backup vault has permission to access compute instances in the compute instance's project. If the backup vault and compute instance are in the same project, then this permission is granted by default.

  * To ensure that Backup and DR Vault Service Agent has the necessary permissions to back up a Compute Engine instance to a backup vault, ask your administrator to grant the [Backup and DR Compute Engine Operator ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.computeEngineOperator) (`roles/backupdr.computeEngineOperator`) IAM role to Backup and DR Vault Service Agent on the project for the Compute Engine instance. **Important:** You must grant this role to Backup and DR Vault Service Agent, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors. 




## Apply or change backup plans for an existing instance

You can apply or change backup plans for an existing compute instance by modifying the compute instance configuration on the Google Cloud console. If you change the backup plan that's applied to your compute instance, then your new backup plan must be from the same project and store the backup in the same backup vault as your existing plan.

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the compute instance for which you want to apply or change the backup plan. The compute instance details page appears for the selected instance.

  3. Click edit **Edit**. The **Edit** page appears for your compute instance.

  4. Navigate to the **Backup plan** section and click **Change plan**.

  5. In the **Select a backup plan** pane that appears, do the following:

     1. In the **Backup plan name** column, click the name of the backup plan that you want to use.

     2. To confirm your choice of backup plan and return to the **Edit** page, click **Apply**.

**Tip:** If the instance has one or more CMEK-encrypted disks, the list of available backup plans is automatically filtered to show only CMEK-compatible backup plans.
  6. To apply your backup plan and save your new instance configuration, click **Save**.




## What's next

  * Learn how to use your compute instance's backup plan to [schedule or create backups in a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup).
  * Learn how to [restore a compute instance from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-restore).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
