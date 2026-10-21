---
url: https://docs.cloud.google.com/alloydb/docs/backup/delete/
title: Delete a backup \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:53.890555+00:00
---

# Delete a backup  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/backup/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Delete a backup Stay organized with collections  Save and categorize content based on your preferences. 

To reduce backup storage costs and remove backups that you no longer need, you can delete an AlloyDB for PostgreSQL backup.

## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.




## Procedure

### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the `backups delete` command to delete an AlloyDB backup.
    
    
    gcloud alloydb backups delete BACKUP_ID \
        --region=REGION_ID \
        --project=PROJECT_ID

  * BACKUP_ID: The ID of the backup. You can find a backup's ID by [viewing a list of backups](https://docs.cloud.google.com/alloydb/docs/backup/list).
  * REGION_ID: The ID of the region where the backup is placed.
  * PROJECT_ID: The ID of the project where the backup is placed.



## Restrictions on deleting backups

You can delete on-demand or automated backups at any time, but AlloyDB limits the circumstances under which you can delete continuous backups. AlloyDB requires the presence of these backups for [continuous backup and recovery](https://docs.cloud.google.com/alloydb/docs/backup/overview#continuous-backup) to work.

AlloyDB lets you delete a continuous backup only if at least one of these circumstances is true:

  * You have [disabled continuous backup and recovery](https://docs.cloud.google.com/alloydb/docs/backup/configure#disable-continuous) on this cluster.

  * The backup that you want to delete is older than the cluster's configured recovery window for continuous backup and recovery.




In addition, AlloyDB doesn't let you delete any backup that has continuous or automated backups based on it. These backups are incremental backups, and they rely on the existence of specific previous backups in order to keep your data safe and restorable.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
