---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/backup-restore/
title: Back up and restore a domain \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:38:26.128223+00:00
---

# Back up and restore a domain  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/backup-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Back up and restore a domain Stay organized with collections  Save and categorize content based on your preferences. 

This topic shows you how to do the following tasks in Managed Service for Microsoft Active Directory:

  * Take a backup of your existing domain which saves the current state of your domain.
  * List the backups available for your domain.
  * Restore domain to a previous state using backup.
  * Get metadata information about a specific backup.
  * Update labels for your backup.
  * Delete backups which you no longer need.

**Note:** You can't use a third-party software to back up and restore a Managed Microsoft AD domain.

## Overview

Managed Microsoft AD supports backing up and restoring your domains. There are three types of backups available:

  * **On-demand backup:** You can take a backup of your domain on demand in Managed Microsoft AD at any time. You can create up to five on-demand backups. If a domain already contains five on-demand backups, you must delete an existing backup before you create a new one.
  * **Scheduled backup:** Scheduled backup is created every 12 hours automatically.
  * **Schema extension backup:** Managed Microsoft AD creates a backup automatically when you initiate [schema extension](https://docs.cloud.google.com/managed-microsoft-ad/docs/schema-extension). A domain can have a maximum of 10 schema extension backups at any point in time. If a domain already has 10 schema extension backups, when you initiate schema extension, Managed Microsoft AD deletes an existing schema extension backup in chronological order before it creates a new one.



You can use any of these backup types to [perform an authoritative restore](https://docs.cloud.google.com/managed-microsoft-ad/docs/backup-restore#restore-backup), which returns the domain to a previous point in time.

**Note:** Managed Microsoft AD retains scheduled and schema extension backups for 21 days. It retains on-demand backups forever unless you delete them.

The backup operation takes backup from the primary region domain controller. When restored, it replicates automatically to all regions.

Note that during a restore, you cannot use your domain.

## Before you begin

  1. Make sure that you have [created a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain).
  2. Make sure that you have any one of the following IAM user roles:

     * Google Cloud Managed Identities Backup Admin (`roles/managedidentities.backupAdmin`)
     * Google Cloud Managed Identities Domain Admin (`roles/managedidentities.domainAdmin`)

For more information, see [Cloud Managed Identities roles](https://docs.cloud.google.com/iam/docs/roles-permissions/managedidentities).

For more information about assigning an IAM role to user, see [Granting access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).




## Gather information

You need the following information to work with backups:

  * **Domain name:** The name of your Managed Microsoft AD domain. For example, `my-domain.example.com`.
  * **Backup name:** The name for your backup must follow these rules:

    * Must start with a letter.
    * Must contain between 1-63 characters.
    * Must end with a number or a letter.
    * Must be unique within the domain.
**Note:** Scheduled and schema extension backups automatically generate the backup name with a timestamp. The timestamp refers to the backup creation date. For example, `scheduled-backup-2021-12-19-215800`.



## Work with on-demand backups

You can create an on-demand backup of your domain and update its labels. You can run the following gcloud CLI commands from the project where you created your Managed Microsoft AD domain.

### Create an on-demand backup

To create an on-demand backup of your domain, run the following gcloud CLI command:
    
    
    gcloud active-directory domains backups create BACKUP_NAME \
      --domain=DOMAIN_NAME \
      --project=DOMAIN_RESOURCE_PROJECT_ID
    

Replace the following:

  * `BACKUP_NAME`: A name for your on-demand domain backup. For example, `my-domain-backup`.
  * `DOMAIN_NAME`: The name of your Managed Microsoft AD domain. For example, `my-domain.example.com`.
  * `DOMAIN_RESOURCE_PROJECT_ID`: The project ID of the domain resource project. For example, `my-project`.



You receive the following response that indicates that backup creation has started:
    
    
    Create request issued for: [BACKUP_NAME]
    Waiting for operation [OPERATION_ID] to complete...
    

It can take up to 90 minutes to create a backup. Alternatively, you can add the `--async` flag to execute the command in the background. Note that you can repeat this process to create up to five independent on-demand backups for a domain.

### Update labels for an on-demand backup

To update labels for an on-demand backup, run the following gcloud CLI command:
    
    
    gcloud active-directory domains backups update BACKUP_NAME \
      --domain=DOMAIN_NAME \
      --project=DOMAIN_RESOURCE_PROJECT_ID \
      --update-labels=KEY=VALUE
    

Replace the following:

  * `BACKUP_NAME`: The name of your on-demand domain backup. For example, `my-domain-backup`.
  * `DOMAIN_NAME`: The name of your Managed Microsoft AD domain. For example, `my-domain.example.com`.
  * `DOMAIN_RESOURCE_PROJECT_ID`: The project ID of the domain resource project. For example, `my-project`.
  * `KEY` and `VALUE`: A key-value pair that you want to add to your domain backup. For example, `backupcount=1`.



## Manage backups

To manage all types of backups, you can run the following gcloud CLI commands from the project where you created your Managed Microsoft AD domain.

### List backups

You can list the backups created for a specific domain. Run the following gcloud CLI command:
    
    
    gcloud active-directory domains backups list \
      --domain=DOMAIN_NAME \
      --project=DOMAIN_RESOURCE_PROJECT_ID
    

Replace the following:

  * `DOMAIN_NAME`: The name of your Managed Microsoft AD domain. For example, `my-domain.example.com`.
  * `DOMAIN_RESOURCE_PROJECT_ID`: The project ID of the domain resource project. For example, `my-project`.



### Get backup information

You can retrieve all the information specific to a domain backup. Run the following gcloud CLI command:
    
    
    gcloud active-directory domains backups describe BACKUP_NAME \
      --domain=DOMAIN_NAME \
      --project=DOMAIN_RESOURCE_PROJECT_ID
    

Replace the following:

  * `BACKUP_NAME`: The name of your domain backup. For example, `my-domain-backup`.
  * `DOMAIN_NAME`: The name of your Managed Microsoft AD domain. For example, `my-domain.example.com`.
  * `DOMAIN_RESOURCE_PROJECT_ID`: The project ID of the domain resource project. For example, `my-project`.



### Delete a backup

To delete a backup, run the following gcloud CLI command:
    
    
    gcloud active-directory domains backups delete BACKUP_NAME \
      --domain=DOMAIN_NAME \
      --project=DOMAIN_RESOURCE_PROJECT_ID
    

Replace the following:

  * `BACKUP_NAME`: The name of your domain backup. For example, `my-domain-backup`.
  * `DOMAIN_NAME`: The name of your Managed Microsoft AD domain. For example, `my-domain.example.com`.
  * `DOMAIN_RESOURCE_PROJECT_ID`: The project ID of the domain resource project. For example, `my-project`.



## Restore a domain from a backup

You can restore a domain to a previous state using any of its backups.

Before you restore a domain, make sure you refer to these [considerations](https://docs.cloud.google.com/managed-microsoft-ad/docs/restore-considerations).

To restore a domain, run the following gcloud CLI command from the project where you created your Managed Microsoft AD domain.
    
    
    gcloud active-directory domains restore DOMAIN_NAME \
      --backup=BACKUP_NAME \
      --project=DOMAIN_RESOURCE_PROJECT_ID
    

Replace the following:

  * `DOMAIN_NAME`: The name of your Managed Microsoft AD domain. For example, `my-domain.example.com`.
  * `BACKUP_NAME`: The name of your domain backup. For example, `my-domain-backup`.
  * `DOMAIN_RESOURCE_PROJECT_ID`: The project ID of the domain resource project. For example, `my-project`.



You receive the following response that indicates that the restore process has started:
    
    
    Request issued for: [DOMAIN_NAME]
    Waiting for operation [OPERATION_ID] to complete...
    

It can take up to 90 minutes to restore a domain. Alternatively, you can add the `--async` flag to execute the command in the background.

**Note:** You cannot use your domain during the restore process. When you restore a domain, the domain controllers are down for up to 90 minutes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
