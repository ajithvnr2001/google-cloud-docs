---
url: https://docs.cloud.google.com/dataproc-metastore/docs/restore-metadata/
title: Restore Dataproc Metastore from a backup \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:39:57.801778+00:00
---

# Restore Dataproc Metastore from a backup  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/restore-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Restore Dataproc Metastore from a backup Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to restore a Dataproc Metastore service from a [backup](https://docs.cloud.google.com/dataproc-metastore/docs/backup-metadata).

A backup is a snapshot of the configuration settings and metadata stored in a Dataproc Metastore service. You can use the restore feature to quickly set up a new Dataproc Metastore service with the data previously saved in a backup.

## Before you begin

  * [Enable Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/enable-service) in your project.
  * [Create a Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service).
  * [Back up a Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/backup-metadata).



### Required roles

To get the permissions that you need to restore a Dataproc Metastore service from a backup, ask your administrator to grant you the following IAM roles: 

  * To grant full control of Dataproc Metastore resources to complete a backup, either the: 
    * [Dataproc Metastore Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`) on the metadata service.
    * [Dataproc Metastore Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`) on the project.
  * To use the Cloud Storage object that stores scheduled backups: [Cloud Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) on the Dataproc Metastore service agent 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to restore a Dataproc Metastore service from a backup. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to restore a Dataproc Metastore service from a backup:

  * To restore a metadata service: metastore.services.restore, metastore.backups.use 
  * To use the Cloud Storage object: 
    * orgpolicy.policy.get
    * resourcemanager.projects.get
    * resourcemanager.projects.list
    * storage.managedFolders.create
    * storage.managedFolders.delete
    * storage.managedFolders.get
    * storage.managedFolders.list
    * `storage.multipartUploads.*`
    * storage.objects.create
    * storage.objects.delete
    * storage.objects.get
    * storage.objects.list
    * storage.objects.restore
    * storage.objects.update



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about specific Dataproc Metastore roles and permissions, see [Dataproc Metastore IAM overview](https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control). 

## About restoring from a backup

When you restore a service from a backup, you can choose one of the following options:

  * Restore all metadata and the configuration settings saved in the backup.
  * Restore all metadata, but don't restore the configuration settings saved in the backup. Instead, your service retains your current configuration settings.

_Configuration settings_ include Dataproc Metastore parameters such as service name, port number, and network settings. _Metadata_ includes all the database and table information stored in a Dataproc Metastore service.




### Considerations

  * While a restore operation is running, you can't update your service — for example, you can't change configuration settings. However, you can still use your service for normal operations, such as using it to access its metadata from attached Managed Service for Apache Spark or self-managed clusters.

  * Dataproc Metastore labels aren't restored.

  * Data stored in the warehouse directory isn't restored.

  * Restoring from a backup doesn't restore or replace fine-grained IAM policies.

  * Restoring from a scheduled backup requires that your backup is located in a Cloud Storage bucket.




## Restore from a backup

To restore a Dataproc Metastore service from a backup, complete the following steps.

  * If you're using the Google Cloud console, you can only restore metadata from a backup that was created in the same project and region as your new service.

  * If you use the Google Cloud CLI or Dataproc Metastore APIs, you can restore metadata from a backup created in a different project and region (cross-service backup).




### Console

  1. In the Google Cloud console, open the **Dataproc Metastore** page:

[Open Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services)

  2. On the **Dataproc Metastore** page, click the name of the service you want to restore from a backup.

The **Service detail** page opens.

![Service detail page](https://docs.cloud.google.com/static/dataproc-metastore/images/service-detail-page.png)**Figure 1.** The Dataproc Metastore service detail page 
  3. To view your backups, click the **Backup/Restore** tab.

  4. Select the backup you want to use. To do this, click the menu icon more_vert and select **Restore**.

The **Restore** page opens.

You can also restore your service on the **Backup detail** page. To do this, click the name of the backup and then click **Restore**.

  5. Select the appropriate restore operation:

     * **Restore metastore data**. Restores all metadata, but doesn't restore the configuration settings saved in the backup
     * **Restore metastore data and service configuration**. Restores all metadata and all configuration settings saved in the backup.
  6. To update the service, click **Restore**.

Return to the **Dataproc Metastore** page, and verify that your service was successfully backed up.

When the restore completes, Dataproc Metastore automatically returns to the [active state](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services?_gl=1*1qaoqiw*_ga*MTIzMTkxNzU5Ni4xNjYzNzk5NTI1*_ga_WH2QY8WWF5*MTY2MzgwMzk0MC4xOS4xLjE2NjM4MDQxNTAuMC4wLjA.#state) regardless of whether or not the restore succeeded.




### gcloud CLI

  1. To restore a Dataproc Metastore service, run the following [`gcloud metastore services restore`](https://cloud.google.com/sdk/gcloud/reference/metastore/services/restore) command:
         
         gcloud metastore services restore SERVICE  \
             --project=PROJECT_ID \
             --location=LOCATION \
             --backup=BACKUP \
             --restore-type=RESTORE_TYPE \
             --backup-location=BACKUP_LOCATION
         

Replace the following:

     * `SERVICE`: the name of your Dataproc Metastore service.
     * `PROJECT_ID`: the project ID of the Google Cloud project your Dataproc Metastore service resides in.
     * `LOCATION`: the Google Cloud region that your Dataproc Metastore service resides.
     * `BACKUP`: Optional: the identifier of the backup file you're restoring from. This value can be the backup ID, a fully qualified URL, or the relative name in the following format: `projects/{project_id}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.
     * `RESTORE_TYPE`: the type of restore operation to perform. Accepted values include `metadata-only` or `full`. The default value is `metadata-only`.
     * `BACKUP_LOCATION`: Optional: The Cloud Storage location of your scheduled backup. For example: `gs://my-bucket/path/to/location`.
  2. Verify that the restore operation was successful.

When the restore completes, Dataproc Metastore automatically returns to the [active state](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services?_gl=1*1qaoqiw*_ga*MTIzMTkxNzU5Ni4xNjYzNzk5NTI1*_ga_WH2QY8WWF5*MTY2MzgwMzk0MC4xOS4xLjE2NjM4MDQxNTAuMC4wLjA.#state) regardless of whether or not the restore succeeded.




### REST

Follow the API instructions to [restore metadata into a service](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/restore) by using the APIs Explorer.

When the restore completes, Dataproc Metastore automatically returns to the [active state](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services?_gl=1*1qaoqiw*_ga*MTIzMTkxNzU5Ni4xNjYzNzk5NTI1*_ga_WH2QY8WWF5*MTY2MzgwMzk0MC4xOS4xLjE2NjM4MDQxNTAuMC4wLjA.#state) regardless of whether or not the restore succeeded.

### View restore history

To view the restore history of a Dataproc Metastore service in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console console, open the [Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services) page.
  2. In the navigation bar, click **Backup/Restore**.

Your restore history appears in a table under **Restore**.

The history displays up to the latest 25 restores you completed.

Deleting a Dataproc Metastore service also deletes all associated restore history.




## Troubleshoot common issues

  * [The service agent or user account doesn't have necessary permissions](https://docs.cloud.google.com/dataproc-metastore/docs/troubleshooting#backup-restore-user-permissions).
  * For more help solving common troubleshooting issues, see [Backup and restore error scenarios](https://docs.cloud.google.com/dataproc-metastore/docs/troubleshooting#backup-and-restore-error-scenarios).



## What's next

  * [Back up metadata from a service](https://docs.cloud.google.com/dataproc-metastore/docs/backup-metadata)
  * [Update and delete a service](https://docs.cloud.google.com/dataproc-metastore/docs/manage-service)
  * [Hive Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/hive-metastore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
