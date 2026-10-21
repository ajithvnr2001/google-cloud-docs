---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-backup-plan-harbor/
title: Create a backup plan \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:05:54.796984+00:00
---

# Create a backup plan  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-backup-plan-harbor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a backup plan Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to create backup plans for Harbor instances in Google Distributed Cloud (GDC) air-gapped.

The backup plan references the Harbor instance that is backed up. Backup plans define key components for backups such as the backup schedule and the retention policy. GDC creates backups automatically depending on the configuration you provide in the backup plan. You can also create a manual backup on demand, which inherits some values from the backup plan.

## Before you begin

You must have a Harbor backup repository configured. For more information, see [Create a backup repository](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-backup-repository-harbor).

### Required IAM roles

Request the necessary permissions from your Project IAM administrator. Enforce least privilege access by requesting only the roles required for your specific tasks.

  * **Secret Admin** (`secret-admin`): get, list, create, update, patch, and delete all Kubernetes secrets within the project namespace. This is a project-level permission that includes the sensitive authentication credentials needed by the backup repository.
  * **Harbor Instance Admin** (`harbor-instance-admin`): get, list, watch, create, update, patch, and delete Harbor instances, backup repositories, backup plans, backups, and restores within the project namespace.



## Create a backup plan

Create a repository in the GDC console or the API.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for harbor instance**.
  3. Click **Backup plans**.
  4. Click **Create backup plan**.
  5. In the **Zone** menu, select the zone.
  6. In the **Harbor instance source** menu, select the harbor instance this backup plan creates backups for.
  7. In the **Backup plan name** field, enter a name for the backup plan.
  8. Optional: In the **Backup plan description** field, enter a description to distinguish this backup plan from others
  9. In the **Backup repository** menu, select a backup repository from the available options. If there are no options available, you must [Create a backup repository](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-backup-repository-harbor).
  10. Click **Next**.
  11. In the **Cron string** field, define a schedule for this backup plan. Enter an expression using standard cron syntax. For example, the expression `10 3 * * *` creates a backup at `0310` every day. All times are interpreted as UTC. The minimum interval between scheduled backups is 10 minutes.
  12. Optional: In the **Retention policy** section, decide whether to automatically delete backups after a certain number of days:

     1. Select the **Enable automatic backup deletion** checkbox.
     2. In the **Delete backups** **after** field, set the number of days for which to retain the backup. Once the number of days is reached, the backup is automatically deleted.
  13. Click **Next**.

  14. Review the backup plan details. To finalize the creation of this backup plan, click **Create Plan**.




### API
    
    
    apiVersion: artifactregistry.gdc.goog/v1
    kind: HarborInstanceBackupPlan
    metadata:
      name: BACKUP_PLAN_NAME
      namespace: INSTANCE_NAMESPACE
    spec:
      backupSchedule:
        cronSchedule: CRON_STRING
        paused: false
      backupConfig:
        backupRepository: BACKUP_REPO_NAME
        backupScope:
          harborInstance: INSTANCE_NAME
      retentionPolicy:
        backupRetainDays: BACKUP_RETAIN_DAYS
      description: PLAN_DESCRIPTION
    

Replace the following:

  * `BACKUP_PLAN_NAME`: the name of the backup plan.
  * `INSTANCE_NAMESPACE`: the namespace containing the Harbor instance. The backup plan must be in the same namespace as the Harbor instance.
  * `CRON_STRING`: the cron value that defines the backup schedule. For example the value `0 3 * * *` defines a schedule that performs daily backups at 3 AM. Use the `paused` field to pause the schedule. If true, periodic scheduled backups are stopped. A paused backup plan is still able to create a manual backup.
  * `BACKUP_REPO_NAME`: the name of the backup repository. For more information, see [Create a backup repository](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-backup-repository-harbor).
  * `INSTANCE_NAME`: the name of the Harbor instance. For more information, see [Create Harbor registry instances](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances).
  * `BACKUP_RETAIN_DAYS`: the number of days after which the backup is deleted. This value is overridden by manual backups that use this plan.
  * `PLAN_DESCRIPTION`: a text description of the backup plan.



## What's next

  * [Manage a backup plan](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/manage-backup-plan-harbor)
  * [Create a manual backup](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-manual-backup-harbor)
  * [Create a restore](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-restore-harbor)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
