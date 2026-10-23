---
url: https://docs.cloud.google.com/alloydb/docs/backup/create-on-demand/
title: Create an on-demand backup \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:28.709577+00:00
---

# Create an on-demand backup  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/backup/create-on-demand/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Create an on-demand backup Stay organized with collections  Save and categorize content based on your preferences. 

To preserve a snapshot of your AlloyDB for PostgreSQL cluster data outside your automated backup schedule—such as before a schema migration or major application update—you can create an on-demand backup.

When you create an on-demand backup, AlloyDB checks that the cluster you're backing up and its primary instance are in the "Ready" state, and then it starts a long-running operation to perform the backup of the cluster data.

## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.




## Procedure

### Console

  1. In the Google Cloud console, go to the **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.
  3. In the navigation menu, click **Data protection**.
  4. Click **Create backup**.
  5. Enter an ID for the backup.
  6. Optional: Enter a description to help you identify this backup.
  7. If you want to encrypt this backup using [Customer-managed encryption key (CMEK)](https://docs.cloud.google.com/alloydb/docs/cmek) instead of Google-managed encryption, follow these additional steps:

     1. Click **Advanced encryption options**.
     2. Select **Customer-managed encryption key (CMEK)**.
     3. Select a customer-managed key from the menu that appears.

The Google Cloud console limits this list to keys within the same Google Cloud project and region as the new cluster. To use a key that is not on this list, click **Don't see your key? Enter key resource name** , and then type the key's resource name into the resulting dialog.

Note that using CMEK with AlloyDB requires some additional setup. For more information, see [Using CMEK with AlloyDB](https://docs.cloud.google.com/alloydb/docs/use-cmek).

  8. Click **Create**.



AlloyDB checks that the source cluster is in the "Ready" state and then starts a long-running operation to perform the backup. The **Data protection** page shows the backup with a status of "In progress" until the operation completes.

### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the [`gcloud alloydb backups create`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/backups/create) command to create an on-demand backup.
    
    
    gcloud alloydb backups create BACKUP_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --project=PROJECT_ID \
        --async

This command returns an operation, whose status you can query using the [`gcloud alloydb operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/operations/describe) command.
    
    
    gcloud alloydb operations describe OPERATION_ID \
        --region=REGION_ID \
        --project=PROJECT_ID

  * BACKUP_ID: The ID for the backup to create.   
To create a backup in a [cross-region location](https://docs.cloud.google.com/alloydb/docs/backup/overview#cross-region-backup-location) using the gcloud CLI, replace with the full backup path in the following format:  
`projects/PROJECT_ID/locations/REGION_ID/backups/BACKUP_ID`  
Cross-region backups require gcloud CLI version 484.0.0 or higher.
  * CLUSTER_ID: The ID of the cluster you want to back up.
  * REGION_ID: The ID of the region where the cluster is placed.
  * PROJECT_ID: The ID of the project where the cluster is placed.



If you want to encrypt this backup using a [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/alloydb/docs/cmek) instead of the default Google-managed encryption, then you must provide these additional arguments:

  * `--kms-key=KEY_ID`: The ID of the CMEK key to use.
  * `--kms-keyring=KEYRING_ID`: The ID of the key's keyring.
  * `--kms-location=LOCATION_ID`: The ID of that keyring's region. Note that it must match the cluster's region.
  * `--kms-project=PROJECT_ID`: The keyring's project ID.

Using CMEK with AlloyDB requires some additional setup. For more information, see [Using CMEK with AlloyDB](https://docs.cloud.google.com/alloydb/docs/use-cmek).

When you run this command, AlloyDB checks that the source cluster is in the "Ready" state, starts a long-running operation to perform the backup, and displays information about the long-running operation.

You can track completion of the long-running operation using the `operations describe` command:
    
    
    gcloud alloydb operations describe OPERATION_ID \
        --region=REGION_ID \
        --project=PROJECT_ID

OPERATION_ID: The operation ID reported when you ran the `backups create` command.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
