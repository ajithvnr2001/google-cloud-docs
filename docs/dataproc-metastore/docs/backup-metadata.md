---
url: https://docs.cloud.google.com/dataproc-metastore/docs/backup-metadata/
title: Back up a Dataproc Metastore service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:39:57.544305+00:00
---

# Back up a Dataproc Metastore service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/backup-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Back up a Dataproc Metastore service Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create a backup of a Dataproc Metastore service.

A [backup](https://docs.cloud.google.com/dataproc-metastore/docs/backup-metadata) takes a snapshot of your service, saves its current configuration settings, and all stored metadata.

After you create a backup, you can use the [Restore from a backup](https://docs.cloud.google.com/dataproc-metastore/docs/restore-metadata) feature to populate a new Dataproc Metastore service with the data saved in the snapshot.

## Before you begin

  * [Enable Dataproc Metastore in your project](https://docs.cloud.google.com/dataproc-metastore/docs/enable-service).
  * [Create a Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service).
  * Optional: [Import metadata into Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/import-metadata).



### Required roles

To get the permissions that you need to back up a Dataproc Metastore service, ask your administrator to grant you the following IAM roles: 

  * To grant full control of Dataproc Metastore resources to complete a backup, either the: 
    * [Dataproc Metastore Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`) on the metadata service.
    * [Dataproc Metastore Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`) on the project.
  * To grant read and modify access to specific metadata of databases and tables: [Dataproc Metastore Metadata Operator ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`) on the metadata service 
  * To use the Cloud Storage object that stores scheduled backups: [Cloud Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) on the Dataproc Metastore service agent 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to back up a Dataproc Metastore service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to back up a Dataproc Metastore service:

  * To back up a metadata service: metastore.backups.create 
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

## Backup considerations

Before running a backup operation, note the following considerations:

  * For each Dataproc Metastore service, you can create and store up to seven backups at a time. If you try to exceed seven backups, the backup process fails. If you want to create another backup, you must first manually delete one of your stored backup files.
  * While a backup operation is running, you can't update your Dataproc Metastore service — for example, you can't change configuration settings. However, you can still use your service for normal operations, such as accessing metadata from attached Managed Service for Apache Spark or self-managed clusters.
  * You can create scheduled backups that run at various cron intervals, such as every day.



## Create a backup

To back up a Dataproc Metastore service, complete the steps in one of the following tabs:

### Console

  1. In the Google Cloud console, open the **Dataproc Metastore** page:

[Open Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services)

  2. On the **Dataproc Metastore** page, click the name of the service you want to back up.

The **Service detail** page opens.

![Service detail page](https://docs.cloud.google.com/static/dataproc-metastore/images/service-detail-page.png)**Figure 1.** The Dataproc Metastore service detail page 
  3. At the top of the page, click **Backup**.

The **Backup** page opens.

  4. Enter the **Backup name**.

  5. Optional: Enter a **Description** of the backup.

  6. To start the backup operation, click **Backup**.

Return to the **Dataproc Metastore** page, and verify that your service was successfully backed up.

When the backup completes, Dataproc Metastore automatically returns to the [active state](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services?_gl=1*1qaoqiw*_ga*MTIzMTkxNzU5Ni4xNjYzNzk5NTI1*_ga_WH2QY8WWF5*MTY2MzgwMzk0MC4xOS4xLjE2NjM4MDQxNTAuMC4wLjA.#state) regardless of whether or not the backup succeeded.




### gcloud CLI

  1. To back up a Dataproc Metastore service, run the following [`gcloud metastore services backups create`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/backups/create) command:
         
         gcloud metastore services backups create BACKUP \
             --location=LOCATION \
             --service=SERVICE \
             --description=DESCRIPTION
         

Replace the following:

     * `BACKUP`: the ID or fully qualified identifier for the backup.
     * `LOCATION`: the Google Cloud region in which your Dataproc Metastore service resides.
     * `SERVICE`: the name of your Dataproc Metastore service.
     * `DESCRIPTION`: a description of your backup.
  2. Verify that your service was successfully backed up.

When the backup completes, Dataproc Metastore automatically returns to the [active state](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services?_gl=1*1qaoqiw*_ga*MTIzMTkxNzU5Ni4xNjYzNzk5NTI1*_ga_WH2QY8WWF5*MTY2MzgwMzk0MC4xOS4xLjE2NjM4MDQxNTAuMC4wLjA.#state) regardless of whether or not the backup succeeded.




### REST

Follow the API instructions to [back up metadata from a service](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services.backups/create) by using the APIs Explorer.

When the backup completes, Dataproc Metastore automatically returns to the [active state](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services?_gl=1*1qaoqiw*_ga*MTIzMTkxNzU5Ni4xNjYzNzk5NTI1*_ga_WH2QY8WWF5*MTY2MzgwMzk0MC4xOS4xLjE2NjM4MDQxNTAuMC4wLjA.#state) regardless of whether or not the backup succeeded.

## View backup history

To view the backup history of a Dataproc Metastore service in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console console, open the [Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services) page.
  2. In the navigation bar, click **Backup/Restore**.

Your backup history appears in a table under **Backups**.

The history displays up to the latest 7 backups.

Deleting a Dataproc Metastore service also deletes all associated backup history.




## Delete a backup

To delete a Dataproc Metastore backup in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, open the [Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services) page.
  2. In the navigation bar, click **Backup/Restore**.
  3. Find the backup you want to delete and click the settings button.
  4. Click **Delete**.



## Schedule a backup

Backups can be scheduled to run at user-specified [cron job intervals](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules), including running daily, weekly, or monthly. A cron schedule uses the unix-cron string format (* * * * *) which is a set of five fields in a line, indicating when the job should be executed.

For example, you can set a custom interval to create a backup every week, such as creating a backup every Wednesday at 2:00 PM PST.

### Scheduled backup considerations

  * Scheduled backups need to specify a backup location, which must be a Cloud Storage path.
  * Scheduled backups are always created in the Avro file format.
  * Scheduled backups are configured in the UTC timezone by default. You can change the timezone when creating the backup for the first time.
  * Scheduled backups can be set to run at hourly, daily, weekly, or monthly intervals. The minimum hourly interval you can set is 4 hours.



### Create a scheduled backup

Backups schedules can be set when you create your service for the first time or added later when you update your service.

To create a Dataproc Metastore service 2 with a scheduled backup, complete the steps in one of the following tabs:

### Console

  1. In the Google Cloud console, open the [**Dataproc Metastore**](https://console.cloud.google.com/dataproc/metastore/services) page.

  2. At the top of the **Dataproc Metastore** page, click the **Create** button.

The **Create service** page opens.

  3. Select **Dataproc Metastore 2**.

  4. Under **Scheduled Backups** , set the toggle to **Enable**.

  5. Under **Location** , select the Cloud Storage location where you want to store your scheduled backup.

  6. Optional: under schedule, select the following:

     1. For **Repeats** , select the recurrence, such as **Daily** or **Weekly**.
     2. For **At time** , select the time of recurrence, such as 12:00 AM.
     3. For **Timezone** , select the appropriate time zone, such as **UTC-8**.
  7. For the remaining service configuration options, use the provided defaults.

  8. Click **Submit**.




### gcloud CLI

  1. To schedule a backup of a Dataproc Metastore service, run the following [`gcloud metastore services backups create`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/backups/create) command:
         
         gcloud metastore services create SERVICE \
            --location=LOCATION \
            --enable-scheduled-backup \
            --scheduled-backup-cron=SCHEDULED_BACKUP_CRON \
            --scheduled-backup-location=SCHEDULED_BACKUP_LOCATION
         

Replace the following:

     * `SERVICE`: the ID or fully qualified identifier for the backup.
     * `LOCATION`: the Google Cloud region in which yourDataproc Metastore service resides.
     * `SCHEDULED_BACKUP_CRON`: the frequency of your backup, specified in the [cron time format](https://en.wikipedia.org/wiki/Cron). For example, a cron value of `0 0 * * *` schedules a daily backup.
     * `SCHEDULED_BACKUP_LOCATION`: the Cloud Storage location of your backup. For example: `gs://my-bucket/path/to/location`.

or

You can also schedule a backup by storing the preceding values in a configuration file:
    
    gcloud metastore services create SERVICE \
       --location=LOCATION \
       --scheduled-backup-configs-from-file=SCHEDULED_BACKUP_CONFIGS_FROM_FILE
    

Replace the following:

     * `SCHEDULED_BACKUP_CONFIGS_FROM_FILE`: a path to a JSON file containing the backup configuration values `enabled`, `cron_schedule`, `time_zone`, and `backup_location`.

The following example shows a backup configuration file that enables scheduled backups, sets the backup schedule to every hour, specifies the time zone as PST, and defines the backup location as a Cloud Storage bucket. You can choose time zones from the list of common [tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    
    {
    "enabled": true,
    "cron_schedule": "0 0 * * *",
    "time_zone": "PST",
    "backup_location": "gs://my-bucket/path/to/location"
    }
    




### REST

Follow the API instructions to [create a scheduled backup](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services.backups) by using the APIs Explorer.

### Update a scheduled backup

To update a Dataproc Metastore service 2 configured with a scheduled backup, complete the steps in one of the following tabs:

### Console

  1. In the Google Cloud console, open the [**Dataproc Metastore**](https://console.cloud.google.com/dataproc/metastore/services) page.

  2. On the **Dataproc Metastore** page, click the name of the service you want to schedule a backup for.

  3. Under **Scheduled Backups** , set the toggle to **Enabled**.

  4. Under **Location** , select the Cloud Storage location where you want to store your scheduled backup.

  5. Optional: Under **Schedule** , select values for the following fields:

     1. For **Repeats** , select the recurrence, such as **Daily** or **Weekly**.
     2. For **At time** , select the time of recurrence, such as 12:00 AM.
     3. For **Timezone** , select the appropriate time zone, such as **UTC-8**.



### gcloud CLI

  1. To schedule a backup of a Dataproc Metastore service, run the following [`gcloud metastore services backups update`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/backups/create) command:
         
         gcloud metastore services update SERVICE \
            --location=LOCATION \
            --enable-scheduled-backup \
            --scheduled-backup-cron=SCHEDULED_BACKUP_CRON \
            --scheduled-backup-location=SCHEDULED_BACKUP_LOCATION \
         

Replace the following:

     * `SERVICE`: the ID or fully qualified identifier for the scheduled backup.
     * `LOCATION`: the Google Cloud region in which your Dataproc Metastore service resides.
     * `SCHEDULED_BACKUP_CRON`: the frequency of your backup, specified in the [cron time format](https://en.wikipedia.org/wiki/Cron). For example, a cron value of `0 0 * * *` schedules a daily backup.
     * `SCHEDULED_BACKUP_LOCATION`: the Cloud Storage location of your scheduled backup. For example: `gs://my-bucket/path/to/location`.

You can also update a scheduled backup using the preceding values stored in a configuration file:
    
    gcloud metastore services update SERVICE \
       --location=LOCATION \
       --scheduled-backup-configs-from-file=SCHEDULED_BACKUP_CONFIGS_FROM_FILE
    

Replace the following:

     * `SCHEDULED_BACKUP_CONFIGS_FROM_FILE`: a path to a JSON file containing the backup configuration.

The following example shows a backup config file that disables a scheduled backup.
    
    {
    "enabled": false,
    }
    




### REST

Follow the API instructions to [update a scheduled backup](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services.backups) by using the APIs Explorer.

### View a scheduled backup

To view a Dataproc Metastore service 2 configured with a scheduled backup, complete the steps in one of the following tabs:

### Console

  1. In the Google Cloud console, open the [**Dataproc Metastore**](https://console.cloud.google.com/dataproc/metastore/services) page.

  2. At the top of the page, click **Backup**.

The **Backup** page opens and displays your scheduled backups. Note that the backups are actually stored in the Cloud Storage bucket that you provided in the scheduled backup configuration.




### gcloud CLI

  1. Run the following `gcloud storage ls` command:
         
         gcloud storage ls gs://BUCKET_NAME/SERVICE/LOCATION
         

Replace the following:

     * `BUCKET_NAME`: the path to the Cloud Storage bucket that stores the scheduled backup that you want to view.
     * `SERVICE`: the ID or fully qualified identifier for the scheduled backup.
     * `LOCATION`: the Google Cloud region in which your Dataproc Metastore service resides.



### REST

Follow the API instructions to [view a scheduled backup](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services.backups) by using the APIs Explorer.

## Troubleshoot common issues

  * [The service agent or user account doesn't have necessary permissions](https://docs.cloud.google.com/dataproc-metastore/docs/troubleshooting#backup-restore-user-permissions).
  * For more help solving common troubleshooting issues, see [Backup and restore error scenarios](https://docs.cloud.google.com/dataproc-metastore/docs/troubleshooting#backup-and-restore-error-scenarios).



## What's next

  * [Restore a Dataproc Metastore service from a backup](https://docs.cloud.google.com/dataproc-metastore/docs/restore-metadata)
  * [Update and delete a Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/manage-service)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
