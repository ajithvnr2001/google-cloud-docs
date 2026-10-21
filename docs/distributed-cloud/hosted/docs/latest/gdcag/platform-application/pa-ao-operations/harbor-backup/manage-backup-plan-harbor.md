---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/manage-backup-plan-harbor/
title: Manage a backup plan \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:05:52.367437+00:00
---

# Manage a backup plan  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/manage-backup-plan-harbor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Manage a backup plan Stay organized with collections  Save and categorize content based on your preferences. 

This document provides instructions on how to manage existing backup plans for Harbor instances, including how to view backup plans and pause backup plan schedules.

## Before you begin

You must have an existing backup plan configured. For more information, see [Create a backup plan](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-backup-plan-harbor).

### Required IAM roles

Request the necessary permissions from your Project IAM administrator. Enforce least privilege access by requesting only the roles required for your specific tasks.

  * **Secret Admin** (`secret-admin`): get, list, create, update, patch, and delete all Kubernetes secrets within the project namespace. This is a project-level permission that includes the sensitive authentication credentials needed by the backup repository.
  * **Harbor Instance Admin** (`harbor-instance-admin`): get, list, watch, create, update, patch, and delete Harbor instances, backup repositories, backup plans, backups, and restores within a specific project namespace.



## View a backup plan

To view an existing backup plan, follow these steps:

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for harbor instance**.
  3. Click **Backup plans**.
  4. View all existing backup plans in the table.
  5. To view the details of a single backup plan, click the name of that backup plan in the table.
  6. To view the backups in a backup plan, click the **Backups** tab.
  7. To view more details about the backup plan, click the **Plan configuration** tab.



## Manage the backup plan schedule

Backup plans create automatic backups as defined in the backup plan schedule. Pause this schedule to stop creating automatic backups. You can create backups manually when the backup plan schedule is paused. After you pause the schedule, you can resume it to continue creating automatic backups.

### Pause a backup plan schedule

To pause a backup plan schedule, follow these steps:

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for harbor instance**.
  3. Click **Backup plans**.
  4. Click the name of the backup plan in the table.
  5. Click pause**Pause schedule**.
  6. In the confirmation dialog, click **Pause**.



### Resume a paused backup plan schedule

To resume a paused backup plan schedule, follow these steps:

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for harbor instance**.
  3. Click **Backup plans**.
  4. Click the name of the backup plan in the table.
  5. Click play_circle**Resume schedule**.
  6. In the confirmation dialog, click **Resume schedule**.



## What's next

  * [Create a manual backup](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-manual-backup-harbor)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
