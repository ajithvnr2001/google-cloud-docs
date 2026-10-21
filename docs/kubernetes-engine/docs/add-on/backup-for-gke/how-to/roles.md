---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/roles/
title: IAM roles and permissions \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:13:41.883174+00:00
---

# IAM roles and permissions  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  IAM roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes how to grant the Backup for GKE service permissions for a Google Cloud project, backups, or restores.

## Predefined roles

Backup for GKE has the following predefined roles:

**Role** | **Title** | **Description** | **Lowest resource**  
---|---|---|---  
`gkebackup.admin` | Backup for GKE Admin | Full read-write access to all Backup for GKE resources | Project  
`gkebackup.backupAdmin` | Backup for GKE Backup Admin | Creates and manages backup plans and backups. Can delegate manual backup creation to Delegated Backup Admins**.** | Project  
`gkebackup.delegatedBackupAdmin` | Backup for GKE Delegated Backup Admin | Creates and manages backups within a backup plan. | BackupPlan  
`gkebackup.viewer` | Backup for GKE Viewer | Read-only access to all Backup for GKE resources | Project  
`gkebackup.restoreAdmin` | Backup for GKE Restore Admin | Creates and manages restore plans and restores. Can delegate restore creation to Delegated Restore Admins. | Project  
`gkebackup.delegatedRestoreAdmin` | Backup for GKE Delegated Restore Admin | Creates and manages restores within a restore plan. | RestorePlan  
  
## Set project-level permissions

You can grant Identity and Access Management permissions for an entire Google Cloud project to an account in the **IAM** page of the Google Cloud console or by using the Google Cloud CLI. Adding permissions at the project level grants the IAM permissions to an account for the following roles:

  * Backup for GKE Admin
  * Backup for GKE Backup Admin
  * Backup for GKE Viewer
  * Backup for GKE Restore Admin




### gcloud

To set permissions, run the following command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID\
        --role roles/ROLE_ID \
        --member PRINCIPAL
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `ROLE_ID`: the type of role, for example `gkebackup.backupAdmin`.
  * `PRINCIPAL`: An identifier for the principal, which usually has the following form: `member-type:id`. For example, `user:my-user@example.com`.



### Console

Perform the following tasks in the Google Cloud console:

  1. Go to your project's IAM page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click the **Grant access** button below the toolbar.

  3. In the **New principals** box, enter the email for the account that you want to add.

  4. Select a role in the drop-down list, for example **Backup for GKE Admin.**

  5. Click **Save.**




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
