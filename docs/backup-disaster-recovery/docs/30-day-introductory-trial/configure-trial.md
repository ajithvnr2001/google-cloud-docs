---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/30-day-introductory-trial/configure-trial/
title: Configure and manage the 30-day introductory trial for Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:57.825153+00:00
---

# Configure and manage the 30-day introductory trial for Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/30-day-introductory-trial/configure-trial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Configure and manage the 30-day introductory trial for Backup and DR Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure, manage, and end the 30-day introductory trial for Backup and DR.

## Required roles

The following table shows the required Identity and Access Management roles and permissions for configuring the 30-day introductory trial for Backup and DR.

Roles required | Permissions required  
---|---  
Ask your administrator to grant you any of the following IAM roles on either a project, a folder, or an organization within the Google Cloud Resource Hierarchy: |   
Backup and DR Admin (`roles/backupdr.admin`) | `backupdr.trial.subscribe`  
Ask your administrator to grant you the following IAM role on your source project: |   
Backup and DR User or User V2 or Viewer (`roles/backupdr.user` or `roles/backupdr.userv2` or `roles/backupdr.viewer`) | `backupdr.trial.get`  
  
You can also get these permissions with custom roles. To see which roles are associated with which permissions, refer to [IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

To grant, change, or revoke access to projects, folders, and organizations, see [Manage access to projects](https://docs.cloud.google.com/resource-manager/docs/access-control-proj).

## Configure the 30-day introductory trial for Backup and DR

### Console

  1. In the Google Cloud console, go to the **Backup and DR** page.

[Go to Backup and DR](https://console.cloud.google.com/backupdr)

  2. Click the **Start 30-day trial** button.

**Note:** If you don't have sufficient permissions to enable the trial, the **Start 30-day trial** button is disabled.
  3. A sidebar opens up. Enable the Backup and DR API and activate the trial.




### REST API

To configure the 30-day introductory trial using the API, see the [API documentation](https://docs.cloud.google.com/backup-disaster-recovery/docs/api).

## Disable the 30-day introductory trial for Backup and DR

You can disable the 30-day introductory trial for Backup and DR at any time during the 30-day period. Before you disable the trial, ensure you do the following to avoid incurring charges after you disable the trial:

  * Manually unprotect the resources.
  * Manually delete the existing backups in the backup vault or self-managed storage.



For product-specific issues, contact the [Google Cloud Support Center](https://cloud.google.com/support). For questions, feedback, or support related to the trial, send an email to [gcbdr-intro-trial@google.com](mailto:gcbdr-intro-trial@google.com).

## End of the 30-day introductory trial

After the 30-day introductory trial period ends, Backup and DR automatically upgrades to paid usage. Following the automatic upgrade, you can continue using all Backup and DR features. For detailed information about pricing for the paid version, see [Backup and DR pricing](https://docs.cloud.google.com/backup-disaster-recovery/pricing).

## What's next

  * Learn about [Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr).
  * For details about Backup and DR pricing after the trial period, see the [Pricing page](https://docs.cloud.google.com/backup-disaster-recovery/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
