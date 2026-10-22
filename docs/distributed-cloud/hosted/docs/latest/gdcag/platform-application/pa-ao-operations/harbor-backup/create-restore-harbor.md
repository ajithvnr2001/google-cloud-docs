---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-restore-harbor/
title: Create a restore \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:25.222668+00:00
---

# Create a restore  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-restore-harbor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a restore Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to restore a Harbor instance backup in Google Distributed Cloud (GDC) air-gapped.

Restores require an existing backup to function. The restore uses the specified backup data for the restoration. A restore only supports restoring a Harbor instance that has the same reference as the backup. The original Harbor instance must be deleted before restoration starts.

## Before you begin

You must have an existing backup. You create backups by doing one of the following:

  * **Automatically** : schedule automatic backups using a backup plan. For more information, see [Create a backup plan](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-backup-plan-harbor).
  * **Manually** : create manual backups on demand. For more information, see [Create a manual backup](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-manual-backup-harbor).



### Required IAM roles

Request the necessary permissions from your Project IAM administrator. Enforce least privilege access by requesting only the roles required for your specific tasks.

  * **Secret Admin** (`secret-admin`): get, list, create, update, patch, and delete all Kubernetes secrets within the project namespace. This is a project-level permission that includes the sensitive authentication credentials needed by the backup repository.
  * **Harbor Instance Admin** (`harbor-instance-admin`): get, list, watch, create, update, patch, and delete Harbor instances, backup repositories, backup plans, backups, and restores within a specific project namespace.



## Create a restore

Create a restore in the GDC console or the API.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for harbor instance**.
  3. Click **Backups**.
  4. Click the name of the backup you want to restore.
  5. Click refresh**Restore a backup**.



### API
    
    
    apiVersion: artifactregistry.gdc.goog/v1
    kind: HarborInstanceRestore
    metadata:
      name: RESTORE_NAME
      namespace: INSTANCE_NAMESPACE
    spec:
      backupName: BACKUP_NAME
      description: RESTORE_DESCRIPTION
    

Replace the following:

  * `RESTORE_NAME`: the name of the restore.
  * `INSTANCE_NAMESPACE`: the namespace containing the Harbor instance. The backup plan containing the backup to restore must be in the same namespace as the Harbor instance to restore.
  * `BACKUP_NAME`: the name of the backup that the system restores.
  * `RESTORE_DESCRIPTION`: a text description of the restore being created.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
