---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-repository/manage-backup-repository/
title: View a backup repository \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:52:26.320819+00:00
---

# View a backup repository  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-repository/manage-backup-repository/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  View a backup repository Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to view a backup repository for virtual machines (VMs) in Google Distributed Cloud (GDC) air-gapped.

This document is for developers in platform administrator or application operator groups that manage VM Backup and restore operations. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To view a backup repository, you must have [a storage bucket and S3 credentials](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-storage-buckets) for the bucket.

### Request IAM roles

Ask your Organization IAM Admin to grant you the **Organization Backup Admin** (`organization-backup-admin`) role. This role creates, gets, lists, watches, updates, patches, and deletes VM backup repositories, VM backup plan templates, VM backup requests, and VM restore requests.

## View a repository

View a backup repository GDC console or `kubectl`.

### Console

View a list of repositories using the GDC console.

  1. Sign into the GDC console.
  2. In the navigation menu, click **Backup for Virtual Machines > Repositories**.
  3. Click a repository in the list to view its details.



### kubectl

View a backup repository by listing the backup repositories and viewing their details using `kubectl`.

  1. List the existing backup repositories:
         
         kubectl get backuprepositories.backup.gdc.goog -n PROJECT_NAME
         

  2. In the list, find the backup repository that you want to view.

  3. View the backup repository details:
         
         kubectl describe backuprepositories.backup.gdc.goog BACKUP_REPOSITORY_NAME -n PROJECT_NAME
         

Replace the following:

     * `BACKUP_REPOSITORY_NAME`: the name of the backup repository.
     * `PROJECT_NAME`: the name of the project.



## What's next

  * [Create a backup plan](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/create-scheduled-backup-plan)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
