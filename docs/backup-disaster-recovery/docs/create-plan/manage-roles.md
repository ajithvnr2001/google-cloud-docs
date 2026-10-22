---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/manage-roles/
title: Manage IAM roles \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:57.685326+00:00
---

# Manage IAM roles  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/manage-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Manage IAM roles Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to assign and modify a Backup and DR role to a user.

To access Backup and DR, each user needs a Google Account that has been added to a Google Cloud project, folder, or organization as a principal with an Identity and Access Management role that allows access to the Google Cloud console.

For a complete list of permissions associated with each role, see [IAM roles and permissions for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-control#roles). You can also [create custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) that contain subsets of permissions that map directly to your needs.

## Assign IAM roles to a user

Use the following instructions to assign a role to a user.

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Click a **Select a project** drop-down menu at the top of the page.

  3. Click **Grant Access**.

  4. In the **Add Principals** section, enter the principal's email address, domain, or other identifier.

  5. Select the project you want to view users in.

  6. Find the principal's email address, domain, or other identifier in **Principals** and select **Edit principal**.

  7. The **Assign roles** drop-down menu displays all the roles–including any custom roles–that you can grant to the principal on this resource. Search for [predefined roles](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-control#roles).

  8. Click **Save**.




## Modify a user's assigned roles

Use the following instructions to modify an existing role to a user.

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Click a **Select a project** drop-down menu at the top of the page.

  3. Select the user you want to modify the role of and click **Edit principal.**

  4. The **Select a role** drop-down menu displays all the roles–including any custom roles–that you can grant to the principal on this resource. Search for [predefined roles](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-control#roles).

  5. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
