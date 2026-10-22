---
url: https://docs.cloud.google.com/compute/docs/instances/create-instance-with-gcbdr-backup-plan/
title: Apply backup plans to new instances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:17.699022+00:00
---

# Apply backup plans to new instances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/create-instance-with-gcbdr-backup-plan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Apply backup plans to new instances Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to apply a Backup and DR Service backup plan to a Compute Engine instance during the instance's creation. To apply a backup plan to an existing compute instance, see [Apply or change backup plans for existing instances](https://docs.cloud.google.com/compute/docs/instances/change-backup-plan-for-instance).

Use Backup and DR Service backup plans to create rule-based and indelible backups of your compute instances and then store those backups in secure and isolated storage locations.

Backup and DR backup plans let you define advanced backup strategies to store your Compute Engine instances in secure storage locations called backup vaults. Using the backup plan that's applied to your compute instance, you can create scheduled or on-demand backups of your instance in a backup vault.

## Before you begin

  * Enable the Backup and DR Service API where the compute instances are located. 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=backupdr.googleapis.com&_ga=2.145630134.30427899.1640890668-1982243420.1634228058)

  * [ Create a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create)
  * [ Create a backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create)
  * Set up Observability Analytics on your bucket to monitor Backup and DR backup jobs.



### Required roles

  * To get the permissions that you need to create a compute instance and apply a backup plan during its creation, ask your administrator to grant you the following IAM roles: 

    * To create the compute instance: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on the project for the Compute Engine instance 
    * To configure scheduled backups or run on-demand backups: 
      * [Backup and DR Backup User ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`) on the project for the backup vault
      * [Viewer ](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`) on the project for the backup vault

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * If you want to back up a compute instance to a backup vault that is in a different project than the compute instance, then make sure that the [ Backup and DR Vault Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#backup-and-dr-vault-service-agent) for the project that contains the backup vault has permission to access compute instances in the compute instance's project. If the backup vault and compute instance are in the same project, then this permission is granted by default.

  * To ensure that Backup and DR Vault Service Agent has the necessary permissions to back up a Compute Engine instance to a backup vault, ask your administrator to grant the [Backup and DR Compute Engine Operator ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.computeEngineOperator) (`roles/backupdr.computeEngineOperator`) IAM role to Backup and DR Vault Service Agent on the project for the Compute Engine instance. **Important:** You must grant this role to Backup and DR Vault Service Agent, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors. 




## Create a compute instance that has a backup plan applied

You can create a compute instance that has a backup plan applied only by using the Google Cloud console. To perform this task, do the following:

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

If prompted, select your project and click **Continue**.

The **Create an instance** page appears and displays the **Machine configuration** pane.

  2. In the **Name** field, specify a name for your compute instance. For more information, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

  3. In the **Region** field, specify the region where you want your compute instance.

  4. Optional: In the **Zone** field, select a zone for this compute instance.

The default selection is **Any**. If you don't change this default selection, then Google automatically chooses a zone for you based on machine type and availability.

  5. To specify a backup plan for this compute instance, do the following:

     1. In the navigation menu, click **OS and storage**. The **Operating system and storage** pane appears.

**Important:** If you see a **Data protection** pane in the navigation menu, click **Data protection** instead of **OS and storage** and then continue with the remaining steps. For more information, see the [February 14, 2025 release note](https://docs.cloud.google.com/compute/docs/release-notes#February_14_2025).
     2. In the **Backup plan** section, click **Select a plan**.

     3. In the **Select a backup plan** pane that appears, do the following:

        1. Verify that the **Project** field has the same project name where your backup plans exist. If not, select the correct project.

        2. In the **Backup plan name** column, click the name of the backup plan that you want to use.

        3. To confirm your choice of backup plan and return to the **Operating system and storage** pane, click **Apply**.

**Tip:** If the instance has one or more CMEK-encrypted disks, the list of available backup plans is automatically filtered to show only CMEK-compatible backup plans.
  6. Optional. Specify any other configuration parameters for your compute instance. For more information about custom configuration options, see [Create and start an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

  7. To create and start the VM, click **Create**.




## What's next

  * Learn how to use your compute instance's backup plan to [schedule or create backups in a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup).
  * Learn how to [restore a compute instance from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-restore).
  * Learn how to [change the backup plan that's applied to a compute instance](https://docs.cloud.google.com/compute/docs/instances/change-backup-plan-for-instance) ([Preview](https://cloud.google.com/products#product-launch-stages)).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
