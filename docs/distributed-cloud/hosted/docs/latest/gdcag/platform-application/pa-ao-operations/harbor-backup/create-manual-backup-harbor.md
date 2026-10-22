---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-manual-backup-harbor/
title: Create a manual backup \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:25:11.106053+00:00
---

# Create a manual backup  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-manual-backup-harbor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a manual backup Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions on how to create an on-demand manual backup of a Harbor instance in Google Distributed Cloud (GDC) air-gapped.

Manual backups create a backup of a Harbor instance at a specific point in time. You can create manual backups outside of the schedule defined by a backup plan. However, you must create a backup plan to create a manual backup, as manual backups inherit attributes from backup plans.

## Before you begin

You must have an existing backup plan configured. The manual backup inherits the attributes of this backup plan. For more information, see [Create a backup plan](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-backup-plan-harbor).

### Required IAM roles

Request the necessary permissions from your IAM Project Admin. Enforce least privilege access by requesting only the roles required for your specific tasks.

  * **Secret Admin** (`secret-admin`): get, list, create, update, patch, and delete all Kubernetes secrets within the project namespace. This is a project-level permission that includes the sensitive authentication credentials needed by the backup repository.
  * **Harbor Instance Admin** (`harbor-instance-admin`): get, list, watch, create, update, patch, and delete Harbor instances, backup repositories, backup plans, backups, and restores within a specific project namespace.



## Create a manual backup

Create a manual backup in the GDC console or the API.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for harbor instance**.
  3. Click **Backup plans**.
  4. Click the name of the backup plan in the table for which to create the manual backup for.
  5. Click save**Start a backup**.

**Note:** During the backup process, the Harbor instance is temporarily switched to read-only mode. In read-only mode, the instance can't push new artifacts to the repository.
  6. In the **Backup name** field, enter a name for the backup.

  7. Optional: In the **Backup description** field, enter a description to distinguish this backup from others.

  8. Optional: To automatically delete backups after a certain number of days, follow these steps:

     1. Select the **Enable automatic backup deletion** checkbox.
     2. In the **Delete backups** **after** field, set the number of days for which to retain the backup. Once the number of days is reached, the backup is automatically deleted.
  9. Click **Create**. The backup appears in the backup table.




### API
    
    
    apiVersion: artifactregistry.gdc.goog/v1
    kind: HarborInstanceBackup
    metadata:
      name: BACKUP_NAME
      namespace: INSTANCE_NAMESPACE
    spec:
      backupPlanName: BACKUP_PLAN_NAME
      manual: true
      retainDays: RETAIN_DAYS
      description: BACKUP_DESCRIPTION
    

Replace the following:

  * `BACKUP_NAME`: the name of the backup being created.
  * `INSTANCE_NAMESPACE`: the namespace containing the Harbor instance. The backup must be in the same namespace as the Harbor instance.
  * `BACKUP_PLAN_NAME`: the reference for the backup plan. The backup configuration is inherited from the backup plan, including the backup repository to store and which Harbor Instance to backup.
  * `RETAIN_DAYS`: the number of days the backups persist in the backup repository for. The retention policy in the backup plan is overridden. For more information, [Create a backup plan](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-backup-plan-harbor).
  * `BACKUP_DESCRIPTION`: a text description of the backup.



## What's next

  * [Manage a backup](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/manage-backup-harbor)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
