---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/restore-backup/
title: Create a restore \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:38.164650+00:00
---

# Create a restore  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/restore-backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a restore Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a manual restore for a backup in Google Distributed Cloud (GDC) air-gapped.

Manual restores enable recovery to a specific point in time by selecting a specific backup version.

## Before you begin

Ensure you have an existing backup. For more information, see [Plan a set of backups](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/plan-backups).

### Request IAM roles

To create a restore for a backup, ask your Organization IAM Admin or Project IAM Admin to grant you one of the following roles:

  * **User Cluster Backup Admin** (`user-cluster-backup-admin`): creates, gets, lists, watches, updates, patches, and deletes backup resources such as backup and restore plans in user clusters. Contact your Organization IAM Admin to request this role.

  * **Backup Creator** (`backup-creator`): creates, gets, lists, watches, updates, patches, and deletes manual backup requests and manual restore requests. Contact your Project IAM Admin to request this role.




## Create a restore

Create a restore using the GDC console or the API.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for Clusters**.
  3. Select a project.
  4. Click the **Backups** tab.
  5. In the list of backups, find the backup to restore and click **Restore**.
  6. Choose a restore plan from the list of plans that apply to this backup.
  7. Enter a name and an optional description for the restore.
  8. Click **Restore**.



### API

Create a `ManualClusterRestoreRequest` custom resource to perform restores from existing `ClusterRestorePlan` resources. Specify the following resources:

  * The `ClusterBackup` resource that you want to restore.
  * The name of the `ClusterRestore` that you want to create
  * The `ClusterRestorePlan` that matches the `ClusterBackupPlan` of the `ClusterBackup`.



Here's an example of a `ManualClusterRestoreRequest` resource:
    
    
    apiVersion: backup.gdc.goog/v1
    kind: ManualClusterRestoreRequest
    metadata:
      name: RESTORE_NAME
      namespace: PROJECT_NAMESPACE
    spec:
      clusterRestoreName: RESTORE_NAME
      clusterRestorePlanName: RESTORE_PLAN
      clusterBackupName: BACKUP_NAME
    

Replace the following:

  * `RESTORE_NAME`: the name of the cluster restore that you want to create.
  * `PROJECT_NAMESPACE`: the name of your GDC project.
  * `RESTORE_PLAN`: the name of the cluster restore plan this cluster restore is derived from.
  * `BACKUP_NAME`: the cluster backup to restore. This `ClusterBackup` resource must be associated with the `ClusterBackupPlan` resource to which the cluster restore plan refers to. For more information, see [Plan a set of restores](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/plan-restores#create-restore-plan).

After initiating a `ManualClusterRestoreRequest`, a `ClusterRestore` custom resource is created.




## What's next

  * [Create a fine-grained restore](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/fine-grained-restore)
  * [View and delete a restore](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/view-and-delete-restore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
