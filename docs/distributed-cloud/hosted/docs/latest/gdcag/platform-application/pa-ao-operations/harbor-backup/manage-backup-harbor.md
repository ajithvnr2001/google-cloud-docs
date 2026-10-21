---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/manage-backup-harbor/
title: Manage a backup \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:01:30.059857+00:00
---

# Manage a backup  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/manage-backup-harbor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Manage a backup Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view and delete existing backups of Harbor instances in Google Distributed Cloud (GDC) air-gapped.

Delete unused Harbor backups to free up storage space and reduce costs. This best practice simplifies backup management and can improve the performance of backups.

## Before you begin

You must have an existing backup. You create backups by doing one of the following:

  * **Automatically** : schedule automatic backups using a backup plan. For more information, see [Create a backup plan](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-backup-plan-harbor).
  * **Manually** : create manual backups on demand. For more information, see [Create a manual backup](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-manual-backup-harbor).



### Required IAM roles

Request the necessary permissions from your Project IAM administrator. Enforce least privilege access by requesting only the roles required for your specific tasks.

  * **Secret Admin** (`secret-admin`): get, list, create, update, patch, and delete all Kubernetes secrets within the project namespace. This is a project-level permission that includes the sensitive authentication credentials needed by the backup repository.
  * **Harbor Instance Admin** (`harbor-instance-admin`): get, list, watch, create, update, patch, and delete Harbor instances, backup repositories, backup plans, backups, and restores within a specific project namespace.



## View an existing backup

To view an existing backup, follow these steps:

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for harbor instance**.
  3. Click **Backups**.
  4. View existing backups in the table.
  5. To view the details of a single backup, click the name of the backup in the table.



## Delete a backup

You can delete backups in two ways:

  * **Automatically** : GDC automatically deletes backups after the number of days in their backup plan retention policy is reached.
  * **Manually** : you delete backups manually.



To manually delete an existing backup, follow these steps:

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for harbor instance**.
  3. Click **Backups**.
  4. Click the name of the backup you want to delete.
  5. Click delete**Delete backup**.
  6. In the confirmation dialog, enter the name of the backup you want to delete.
  7. Click **Delete backup**.

**Warning:** This operation can't be undone. Deleting a backup permanently removes it and all its data. You can no longer create restores from this backup.

## What's next

  * [Create a restore](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-restore-harbor)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
