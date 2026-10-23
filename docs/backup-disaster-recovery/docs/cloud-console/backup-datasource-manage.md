---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-datasource-manage/
title: Manage data sources in the Google Cloud console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:46.130397+00:00
---

# Manage data sources in the Google Cloud console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-datasource-manage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Manage data sources in the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to list and view data source details in the Google Cloud console.

Each data source in a backup vault identifies a specific resource. A data source can be a specific virtual machine or a specific database instance that is being backed up or has been backed up to the backup vault. Data sources are automatically created by the Backup and DR based on the backup plan you apply to the resource.

## Before you begin

To get the permissions that you need to list and view data source details, ask your administrator to grant you the [Backup and DR Backup Vault Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultViewer) (`roles/backupdr.backupvaultViewer`) IAM role on your backup vault project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to list and view data source details. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to list and view data source details:

  * `backupdr.bvdataSources.list`
  * `backupdr.bvdataSources.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List data sources

Use the following instructions to list data sources.

###  Console 

  1. In the Google Cloud console, go to the Backup and DR **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-resources)

  2. In the **Resources with vaulted backups** list, you can see a list of all of your vaulted backups with a **Resource type** column that lists their data sources. You can sort the list by the **Resource type** column or filter by **Resource type** to see the data source types that are protected.




###  gcloud 

Use the following instructions to list the protected data source types.

  1. List the data sources.
         
         gcloud backup-dr data-sources list \
           --backup-vault=BACKUPVAULT_NAME \
           --location=LOCATION \
           --project=PROJECT_ID
         

Replace the following:

     * `BACKUPVAULT_NAME`: the name of the backup vault.
     * `LOCATION`: the location of the backup vault.
     * `PROJECT_ID`: the name of the project where the backup vault is created.



Use the following instructions to view the data source details.

  1. View the data source details.
         
         gcloud backup-dr data-sources describe DATA_SOURCE \
           --backup-vault=BACKUPVAULT_NAME \
           --location=LOCATION \
           --project=PROJECT_ID
         

Replace the following:

     * `DATA_SOURCE`: the ID of the data source you want to view details of.
     * `BACKUPVAULT_NAME`: the name of the backup vault.
     * `LOCATION`: the location of the backup vault.
     * `PROJECT_ID`: the name of the project where the backup vault is created.



## What's next

  * [Manage backups in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/bv-backup-manage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
