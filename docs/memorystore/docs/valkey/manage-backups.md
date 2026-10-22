---
url: https://docs.cloud.google.com/memorystore/docs/valkey/manage-backups/
title: Manage backups \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:15.578734+00:00
---

# Manage backups  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/manage-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Manage backups Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to perform backup operations in Memorystore for Valkey. You can use backups to restore the data of your instance to a point in time, as well as to export and analyze the data.

**Note:** Before you read this page, familiarize yourself with [backups](https://docs.cloud.google.com/memorystore/docs/valkey/backups).

## Before you begin

  1. Make sure that either you or the user account that you're using has the [required permissions](https://docs.cloud.google.com/memorystore/docs/valkey/access-control) for the action that you need to perform.

The **Memorystore Admin** and **Memorystore Editor** roles can perform all backup operations. The **Memorystore Viewer** role can view and export backups.




## Create an on-demand backup

You can take an on-demand backup for a Memorystore for Valkey instance by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the ID of the instance for which you want to take a backup.

  3. In the side navigation panel, click **Backups**.

  4. Click **Create backup**.

  5. In the **Create backup** dialog, do the following:

     1. **Optional.** Provide a name for the backup. If you don't name the backup, then the backup has a date-and-time stamp for a name.
     2. Click **Create backup**.



### gcloud

To create an on-demand backup, use the [`gcloud memorystore instances backup`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/backup) command.
    
    
    gcloud memorystore instances backup INSTANCE_ID \
    --backup-id=BACKUP_ID \
    --ttl=TTL_PERIOD \
    --project=PROJECT_ID \
    --location=REGION_ID
    

Replace the following:

  * INSTANCE_ID: the ID of the Memorystore for Valkey instance.
  * BACKUP_ID: an ID for the backup, such as `march-2025-backup`.
  * TTL_PERIOD: a time to live (TTL) for the backup. After the backup reaches the TTL limit, Memorystore for Valkey deletes the backup automatically.

You set the value for this parameter to a number of days (for example, `14d`). The minimum value is 1 day. If you don't specify a value, then the default value is 100 years.

  * PROJECT_ID: your project ID.

  * REGION_ID: the region where your instance is located (for example, `us-east1`).




The command returns an operation name with the following format:
    
    
    projects/PROJECT_ID/locations/REGION_ID/operations/operation-UID
    

To check the status of an operation, use the [`gcloud memorystore operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/operations/describe) command.
    
    
    gcloud memorystore operations describe projects/PROJECT_ID/locations/REGION_ID/operations/operation-UID
    

To list all operations in a project and region, use the [`gcloud memorystore operations list`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/operations/list) command.
    
    
    gcloud memorystore operations list --projects=PROJECT_ID \
    --location=REGION_ID
    

## Configure automated backup schedules

You can configure a daily backup schedule when you create an instance or you can enable a daily backup schedule on an existing instance.

You can either configure a daily backup schedule when you create an instance or you can enable a daily backup schedule on an existing instance.

### Create an instance with an automated backup schedule enabled

You can set a daily backup schedule as you create an instance in Memorystore for Valkey by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

To create an instance and enable a backup schedule for the instance automatically, see [Create instances](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances).

### gcloud

To create an instance and enable a backup schedule for the instance automatically, use the [`gcloud memorystore instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/create) command.
    
    
    gcloud memorystore instances create INSTANCE_ID \
    --automated-backup-config-mode=enabled \
    --fixed-frequency-schedule-start-time-hours=START_TIME \
    --automated-backup-config-retention=RETENTION_POLICY
    

Replace the following:

  * INSTANCE_ID: the ID of the Memorystore for Valkey instance that you're creating.
  * START_TIME: the time when Memorystore for Valkey begins taking backups. Specify the time in the `HH` format on a 24-hour cycle in UTC time. For example: `23`.
  * RETENTION_POLICY: the number of days for which Memorystore for Valkey retains each backup. Set the value for this parameter to a number of days (for example, `7d`). The maximum value is 365 days and the default value is 35 days.

Even after you [delete the instance](https://docs.cloud.google.com/memorystore/docs/valkey/delete-instances), Memorystore for Valkey retains the backup for the retention period, with a maximum of 365 days. To remove the backup before the retention period expires, you must delete the backup manually.




### Enable scheduled backups on an existing instance

You can enable a daily backup schedule on an existing instance by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Note:** You can enable scheduled backups on an instance only if you didn't set a daily backup schedule when you created the instance.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the ID of the instance for which you want to enable backups.

  3. In the side navigation panel, click **Backups**.

  4. In the **Settings** section, next to the **Automated daily backups** field, click _edit_ **Edit**.

This field has a status of **Disabled**. If this field has an **Enabled** status, then you already enabled scheduled backups for this instance.

  5. In the **Automated backup settings** dialog, do the following:

     1. Select the **Automated daily backups** checkbox.
     2. In the **Days to retain backups** field, enter the number of days that you want Memorystore for Valkey to keep backups before they're deleted automatically. You can specify from `1` to `365` days. The default value is `35` days.
     3. From the **Time window** menu, select the hour when Memorystore for Valkey takes a daily backup.
     4. Click **Save**.



### gcloud

To enable scheduled backups on an instance, use the [`gcloud memorystore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/update) command.
    
    
    gcloud memorystore instances update INSTANCE_ID \
    --automated-backup-config-mode=enabled \
    --fixed-frequency-schedule-start-time-hours=START_TIME \
    --automated-backup-config-retention=RETENTION_POLICY
    

Replace the following:

  * INSTANCE_ID: the ID of the Memorystore for Valkey instance that you're updating.
  * START_TIME: a timestamp that specifies when Memorystore for Valkey begins taking backups. This timestamp must be at the hour level, in the `HH` format, and on a 24-hour cycle in UTC time (for example, `23`). The timestamp also designates a one-hour window of when Memorystore for Valkey begins to take backups.
  * RETENTION_POLICY: the number of days for which Memorystore for Valkey retains each backup. Set the value for this parameter to a number of days (for example, `7d`).

Even after you [delete the instance](https://docs.cloud.google.com/memorystore/docs/valkey/delete-instances), Memorystore for Valkey retains the backup for the retention period. To remove the backup before the retention period expires, you must delete the backup manually.




### Deactivate scheduled backups

You can deactivate scheduled backups on an instance by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the ID of the instance for which you want to deactivate backups.

  3. In the side navigation panel, click **Backups**.

  4. In the **Settings** section, next to the **Automated daily backups** field, click _edit_ **Edit**.

This field has a status of **Enabled**. This field is enabled by default. If this field has a **Disabled** status, then you have already deactivated scheduled backups for this instance.

  5. In the **Automated backup settings** dialog, do the following:

     1. Clear the **Automated daily backups** checkbox.
     2. Click **Save**.



### gcloud

To deactivate scheduled backups on an instance, use the [`gcloud memorystore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/update) command.
    
    
    gcloud memorystore instances update INSTANCE_ID \
    --automated-backup-config-mode=disabled
    

Replace INSTANCE_ID with the ID of the Memorystore for Valkey instance that you're updating.

## Concurrency between backup and update instance operations

Update operations and maintenance operations on an instance can cancel ongoing backup operations in the following situations:

  * If there's an ongoing operation to update an instance, then Memorystore for Valkey rejects backup operations.
  * In rare circumstances, maintenance and backup operations might coincide with each other and lead to the backup operations being skipped for that instance.



## List and describe backups

The following sections demonstrate how to find information about available backups.

### List backup collections

A _backup collection_ includes all backups that you take for an instance. You can view a list of backup collections by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. In the side navigation panel, click **Backups**.




### gcloud

To list backup collections for a project and region, use the [`gcloud memorystore backup-collections list`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/backup-collections/list) command.
    
    
    gcloud memorystore backup-collections list \
    --project=PROJECT_ID \
    --location=REGION_ID
    

Replace the following:

  * PROJECT_ID: your project ID
  * REGION_ID: the region where your instance is located (for example, `us-east1`)



The command returns a list of backup collections.

### List the backups in a backup collection

You can view a list of backups for a backup collection by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. In the side navigation panel, click **Backups**.

  3. Click the ID of an instance that's associated with a backup collection. This backup collection contains a list of backups that you want to view.




### gcloud

To list the backups in a backup collection, use the [`gcloud memorystore backup-collections backups list`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/backup-collections/backups/list) command.
    
    
    gcloud memorystore backup-collections backups list \
    --backup-collection=BACKUP_COLLECTION
    --project=PROJECT_ID \
    --location=REGION_ID
    

Replace the following:

  * BACKUP_COLLECTION: the name of the backup collection
  * PROJECT_ID: your project ID
  * REGION_ID: the region where your instance is located (for example, `us-east1`)



The command returns a list of backups that are in a backup collection.

### Describe a backup

You can retrieve information about a backup by using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### gcloud

To retrieve information about a backup, use the [`gcloud memorystore backup-collections backups describe`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/backup-collections/backups/describe) command.
    
    
    gcloud memorystore backup-collections backups describe BACKUP_NAME \
    --backup-collection=BACKUP_COLLECTION \
    --project=PROJECT_ID \
    --location=REGION_ID
    

Replace the following:

  * BACKUP_NAME: the name of the backup (for example, `2024-05-01-10-15-00`)
  * BACKUP_COLLECTION: the name of the backup collection
  * PROJECT_ID: your project ID
  * REGION_ID: the region where your instance is located (for example, `us-east1`)



The command returns information about the backup that's similar to the following:
    
    
    backupFiles:
    - createTime: '2024-11-10T03:52:55.539Z'
    fileName: 3d2774dab822137c5bac9386f3fa69ee4c73b928.rdb
    sizeBytes: '694879680'
    - createTime: '2024-11-10T03:52:54.742Z'
    fileName: 7f5d99faaefc63ed8292a71da2552db3b06cdcff.rdb
    sizeBytes: '694925906'
    - createTime: '2024-11-10T03:52:54.972Z'
    fileName: 0aac1092a3fb81515aefb6b2421f31eb346c3961.rdb
    sizeBytes: '694784169'
    instance: projects/PROJECT_ID/locations/us-east1/instances/instance1
    instanceUid: 57130520-636c-4ac7-ad7e-86f7cfb32838
    createTime: '2024-11-10T03:52:40.899882388Z'
    expireTime: '2124-11-10T03:53:02.856981736Z'
    name: projects/PROJECT_ID/locations/us-east1/backupCollections/dda2f551-b416-47ff-b1cf-684e00483dc9/backups/march-2025-backup
    nodeType: HIGHMEM_MEDIUM
    shardCount: 3
    state: ACTIVE
    totalSizeBytes: '2084589755'
    

### Delete a backup

You can delete a backup by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Note:** If you import data from a backup into a new instance and then delete the backup, the instance isn't impacted.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the ID of the instance, which contains a backup that you want to delete.

  3. In the side navigation panel, click **Backups**.

  4. Next to the backup that you want to delete, click _more_vert_ **More actions**.

  5. From the menu, select **Delete**.

  6. In the **Delete backup?** dialog, do the following:

     1. In the text field, enter `delete`.
     2. Click **Delete**.



### gcloud

To delete a backup, use the [`gcloud memorystore backup-collections backups delete`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/backup-collections/backups/delete) command.
    
    
    gcloud memorystore backup-collections backups delete BACKUP_NAME \
    --backup-collection=BACKUP_COLLECTION \
    --project=PROJECT_ID \
    --location=REGION_ID
    

Replace the following:

  * BACKUP_NAME: the name of the backup (for example, `2024-05-01-10-15-00`)
  * BACKUP_COLLECTION: the name of the backup collection
  * PROJECT_ID: your project ID
  * REGION_ID: the region where your instance is located (for example, `us-east1`)



## Export a backup to a storage bucket

You can export a backup to a Cloud Storage bucket by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Note:** Exporting a backup doesn't delete the backup from the backup collection automatically.

To export a backup, do the following:

  1. Memorystore for Valkey must have permission to access the destination Cloud Storage bucket. Grant the Memorystore for Valkey [service agent](https://docs.cloud.google.com/iam/docs/service-agents) access to the Cloud Storage resources.

The Memorystore for Valkey service agent uses the following naming format:
         
         service-PROJECT_NUMBER@gcp-sa-memorystore.iam.gserviceaccount.com
         

Replace PROJECT_NUMBER with the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project where the instance or backup is located.

Grant the service agent a role that assigns the `storage.buckets.get`, `storage.objects.create`, `storage.objects.delete`, and `storage.folders.create` permissions to the role.

For example, the following command assigns the `Storage Admin` role to the service agent for a Cloud Storage bucket:

### gcloud
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
         --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-memorystore.iam.gserviceaccount.com \
         --role=roles/storage.admin
         

Replace the following:

     * BUCKET_NAME: the name of the destination Cloud Storage bucket. This bucket must be a [regional](https://docs.cloud.google.com/storage/docs/locations#key-concepts) bucket and it must be in the same region as the backup. Memorystore for Valkey must have permissions to access the bucket and to create folders and objects inside of the bucket.
     * PROJECT_NUMBER: the project number that's used in the service agent name.

  2. Export a backup to a Cloud Storage bucket.

### Console

     1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

     2. Click the ID of the instance, which contains a backup that you want to export.

     3. In the side navigation panel, click **Backups**.

     4. Next to the backup that you want to export, click _more_vert_ **More actions**.

     5. From the menu, select **Export**.

     6. In the **Choose destination** section of the **Export backup to Cloud Storage** page, click **Browse**.

     7. In the **Select bucket** dialog, click the bucket to which you want to export the backup, and then click **Select**.

**Note:** If a bucket doesn't appear in the dialog, then [create](https://docs.cloud.google.com/storage/docs/creating-buckets) it. Also, the bucket must be a [regional](https://docs.cloud.google.com/storage/docs/locations#key-concepts) bucket and it must be in the same region as the backup. Memorystore for Valkey must have permission to access the bucket, and to create folders and objects inside of the bucket.
     8. In the **Export backup to Cloud Storage** page, click **Export**.

### gcloud

To export a backup to a Cloud Storage bucket, use the [`gcloud memorystore backup-collections backups export`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/backup-collections/backups/export) command.
    
    gcloud memorystore backup-collections backups export BACKUP_NAME \
    --backup-collection=BACKUP_COLLECTION \
    --location=REGION_ID \
    --gcs-bucket=BUCKET_NAME
    

Replace the following:

     * BACKUP_NAME: the name of the Memorystore for Valkey backup
     * BACKUP_COLLECTION: the name of the backup collection
     * REGION_ID: the region where the backup collection is located (for example, `us-east1`)
     * BUCKET_NAME: the name of the Cloud Storage bucket, which doesn't have `gs://` as a prefix

The bucket must be a [regional](https://docs.cloud.google.com/storage/docs/locations#key-concepts) bucket and it must be in the same region as the backup. Memorystore for Valkey must have permission to access the bucket, and to create folders and objects inside of the bucket.




## Restore data from a backup

To restore data from a backup, you can either seed a new instance from a managed backup in the same project or you can seed a new instance from [Redis Database (RDB)](https://docs.cloud.google.com/memorystore/docs/valkey/about-rdb-persistence) files in a Cloud Storage bucket. To seed an instance from RDB files, Memorystore for Valkey must have permission to access the files.

**Note:** A Memorystore for Valkey instance with [Cluster Mode Enabled](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled) supports only one database. You can't import a backup that contains multiple databases to an instance that has Cluster Mode Enabled.

### Seed a new instance from a backup

The following example demonstrates how to import data from a backup to a new instance. The backup must be in the same region as the instance. Also, the principal that creates the instance must have the `memorystore.backups.get` permission for the backup.

You can import data from a backup into a new instance by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the ID of the instance, which contains a backup that you want to import.

  3. In the side navigation panel, click **Backups**.

  4. Next to the backup that you want to import, click _more_vert_ **More actions**.

  5. From the menu, select **Import into new instance**. The **Create a Valkey instance** page appears.

  6. In the **Backup options** section, verify the following:

     1. The **Managed backups** option is selected.
     2. The **Backup ID** field contains the path and name of the backup that you selected.
  7. In the **Name your instance** section, enter an ID for the instance that you're creating. The Instance ID must use only lowercase letters, numbers, and hyphens. It must also start with a letter and be unique in its region.

  8. From the **Region** menu, select a region for your instance.

  9. In the **Zonal availability** section, specify whether you want to create a [single-zone or multi-zone](https://docs.cloud.google.com/memorystore/docs/valkey/single-zone-instances) instance.

  10. In the **Cluster Mode** section, specify whether you want a Cluster Mode Enabled or Cluster Mode Disabled instance. For more information about these types of instances, see [Enable and disable cluster mode](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled).

  11. **Optional**. In the **Node Type** section, select a [node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type).

**Caution** : We recommend that you use the `shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Valkey in a production environment, then we recommend using another node type.
  12. **Optional**. In the **Instance size** section, enter the number of shards for your instance. The shard count determines the total memory capacity for storing instance data. For more information about instance specifications, see [Instance and node specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification).

  13. **Optional**. If you want to create an instance with replicas, then in the **Replicas** section, select the number of replicas (per shard). You can select 0-5 replicas. The default value is 1 replica.

**Important:** Memorystore for Valkey populates the **Node Type** , **Instance size** , and **Replicas** sections automatically with values that are associated with the backup that you're importing. You can keep these values or increase them. For example, if the backup uses a **Medium** node type, then you can change it to **X-Large**. However, we strongly recommend that you don't _decrease_ any values in these sections. If you do, then you might experience issues with importing the backup into your instance.
  14. In the **Set up connection** section, select the network that your applications can use to connect to this instance. For more information about private networking for Memorystore for Valkey, see [Networking](https://docs.cloud.google.com/memorystore/docs/valkey/networking).

  15. **Optional**. If you want to increase the security of your instance, then in the **Security** section, enable [IAM authentication](https://docs.cloud.google.com/memorystore/docs/valkey/about-iam-auth) by selecting the **Enable IAM AUTH** checkbox.

**Note:** If you select this checkbox, then Memorystore for Valkey selects the **Enable In-Transit Encryption (TLS)** checkbox automatically. As a result, Memorystore for Valkey [encrypts](https://docs.cloud.google.com/memorystore/docs/valkey/about-in-transit-encryption) your credentials so that they're confidential when they're transmitted from the instance to the application.
  16. In the **Data persistence strategy** section, specify how you want Memorystore for Valkey to persist the data in your instance. Acceptable values are **No persistence** , [**Append Only File (AOF)** persistence](https://docs.cloud.google.com/memorystore/docs/valkey/about-aof-persistence), and [**Memory Snapshot** persistence](https://docs.cloud.google.com/memorystore/docs/valkey/about-rdb-persistence).

  17. **Optional**. If you want to enable [automated backups](https://docs.cloud.google.com/memorystore/docs/valkey/backups#automated-and-on-demand-backups) for your instance, then do the following:

     1. Select the **Automated daily backups** checkbox.
     2. In the **Days to retain backups** field, enter the number of days that you want Memorystore for Valkey to keep backups before they're deleted automatically. You can specify from `1` to `365` days. The default value is `35` days.
     3. From the **Time window** menu, select a time for the daily backup.
  18. In the **Choose version** section, select your [Valkey version](https://docs.cloud.google.com/memorystore/docs/valkey/supported-versions). Available versions are 7.2, 8.0, 9.0, and 9.1. The default version is version 9.1.

**Important:** After you select a version for the instance, you can't downgrade the instance to an earlier version.
  19. Click **Create instance**.




### gcloud

To import data from a backup into a new instance, use the [`gcloud memorystore instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/create) command.
    
    
    gcloud memorystore instances create INSTANCE_ID \
    --managed-backup-source=BACKUP_NAME \
    --location=REGION_ID \
    --shard-count=SHARD_COUNT \
    --engine-version=ENGINE_VERSION \
    --psc-auto-connections=NETWORK
    

Replace the following:

  * INSTANCE_ID: the ID of the Memorystore for Valkey instance that you're creating.
  * BACKUP_NAME: the name of the backup. This name has the following format: `projects/PROJECT_ID/locations/REGION_ID/backupCollections/BACKUP_COLLECTION_ID/backups/BACKUP_ID`.
  * REGION_ID: the region where your instance is located (for example, `us-east1`).
  * SHARD_COUNT: the number of shards for the instance (from 1 to 250).
  * ENGINE_VERSION: the version of your Memorystore for Valkey instance. Accepted values for this parameter are `VALKEY_7_2`, `VALKEY_8_0`, `VALKEY_9_0`, and `VALKEY_9_1`. If you don't specify a value, then `VALKEY_9_1` is the default value.

**Important:** After you specify a version for the instance, you can't downgrade the instance to an earlier version.
  * NETWORK: the network used to create the instance. It must use this format: `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_ID`. The network ID must match the network ID that the [service connection policy](https://docs.cloud.google.com/memorystore/docs/valkey/networking#prerequisites_required_before_creating_an_instance) uses. Otherwise, you can't create the instance.




For more options that you can use to create an instance, see [Create an instance](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances#create_an_instance).

### Seed a new instance from RDB files in a storage bucket

You can import data from [RDB](https://docs.cloud.google.com/memorystore/docs/valkey/about-rdb-persistence) files, which are contained in a Cloud Storage bucket, into a new instance.

To seed an instance from RDB files in a Cloud Storage bucket, you must grant Memorystore for Valkey access to the bucket and objects, and then import the data from the files.

You can import data from RDB files by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

  1. Memorystore for Valkey must have permission to access the destination Cloud Storage bucket. Grant the Memorystore for Valkey [service agent](https://docs.cloud.google.com/iam/docs/service-agents) access to the Cloud Storage resources.

The Memorystore for Valkey service agent uses the following naming format:
         
         service-PROJECT_NUMBER@gcp-sa-memorystore.iam.gserviceaccount.com
         

Replace PROJECT_NUMBER with the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project where the instance or backup is located.

Grant the service agent a role that assigns the `storage.buckets.get` and `storage.objects.get` permissions to the role.

For example, the following command assigns the `Storage Admin` role to the service agent for a Cloud Storage bucket:

### gcloud
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME
         --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-memorystore.iam.gserviceaccount.com
         --role=roles/storage.admin
         

Replace the following:

     * BUCKET_NAME: the name of the bucket where the RDB files are located. This bucket must either be a [regional](https://docs.cloud.google.com/storage/docs/locations#key-concepts) bucket in the same region as the backup, or be a dual-region bucket and have one region the same as that of the backup. Memorystore for Valkey must have permissions to access the bucket.
     * PROJECT_NUMBER: the project number that's used in the service agent name.

  2. Import data from RDB files in a Cloud Storage bucket into a new instance.

### Console

     1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

     2. Next to **Create instance** , click the _arrow_drop_down_ down arrow, and then select **Create from backup** from the menu that appears. The **Create a Valkey instance** page appears.

     3. In the **Backup options** section, do the following:

        1. Select the **Cloud Storage folder** option.
        2. In the text field, click **Browse**.
        3. In the **Select folder** dialog, select the folder which contains the RDB files that you want to import.
        4. Click **Select**.
     4. In the **Name your instance** section, enter an ID for the instance. The Instance ID must use only lowercase letters, numbers, and hyphens. It must also start with a letter and be unique in its region.

     5. From the **Region** menu, select a region for your instance.

     6. In the **Zonal availability** section, specify whether you want to create a [single-zone or multi-zone](https://docs.cloud.google.com/memorystore/docs/valkey/single-zone-instances) instance.

     7. In the **Cluster Mode** section, specify whether you want a Cluster Mode Enabled or Cluster Mode Disabled instance. For more information about these types of instances, see [Enable and disable cluster mode](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled).

     8. In the **Node Type** section, select a [node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type).

**Caution** : We recommend that you use the `shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Valkey in a production environment, then we recommend using another node type.
     9. In the **Instance size** section, enter the number of shards for your instance. The shard count determines the total memory capacity for storing instance data. For more information about instance specifications, see [Instance and node specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification).

     10. If you want to create an instance with replicas, then in the **Replicas** section, select the number of replicas (per shard). You can select 0-5 replicas. The default value is 1 replica.

     11. In the **Set up connection** section, select the network that your applications can use to connect to this instance. For more information about private networking for Memorystore for Valkey, see [Networking](https://docs.cloud.google.com/memorystore/docs/valkey/networking).

     12. **Optional**. If you want to increase the security of your instance, then in the **Security** section, enable [IAM authentication](https://docs.cloud.google.com/memorystore/docs/valkey/about-iam-auth) by selecting the **Enable IAM AUTH** checkbox.

**Note:** If you select this checkbox, then Memorystore for Valkey selects the **Enable In-Transit Encryption (TLS)** checkbox automatically. As a result, Memorystore for Valkey [encrypts](https://docs.cloud.google.com/memorystore/docs/valkey/about-in-transit-encryption) your credentials so that they're confidential when they're transmitted from the instance to the application.
     13. In the **Data persistence strategy** section, specify how you want Memorystore for Valkey to persist the data in your instance. Acceptable values are **No persistence** , [**Append Only File (AOF)** persistence](https://docs.cloud.google.com/memorystore/docs/valkey/about-aof-persistence), and [**Memory Snapshot** persistence](https://docs.cloud.google.com/memorystore/docs/valkey/about-rdb-persistence).

     14. **Optional**. If you want to enable [automated backups](https://docs.cloud.google.com/memorystore/docs/valkey/backups#automated-and-on-demand-backups) for your instance, then do the following:

        1. Select the **Automated daily backups** checkbox.
        2. In the **Days to retain backups** field, enter the number of days that you want Memorystore for Valkey to keep backups before they're deleted automatically. You can specify from `1` to `365` days. The default value is `35` days.
        3. From the **Time window** menu, select a time for the daily backup.
     15. In the **Choose version** section, select your [Valkey version](https://docs.cloud.google.com/memorystore/docs/valkey/supported-versions). Available versions are 7.2, 8.0, 9.0, and 9.1. The default version is version 9.1.

**Important:** After you select a version for the instance, you can't downgrade the instance to an earlier version.
     16. Click **Create instance**.

### gcloud

To import data from RDB files in a Cloud Storage bucket into a new instance, use the [`gcloud memorystore instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/create) command.
    
    gcloud memorystore instances create INSTANCE_ID \
    --gcs-source-uris=URI \
    --location=REGION_ID \
    --node-type=NODE_TYPE \
    --shard-count=SHARD_COUNT
    

Replace the following:

     * INSTANCE_ID: the ID of the Memorystore for Valkey instance that you're creating.
     * URI: one or more Cloud Storage uniform resource identifiers (URIs) that are separated by commas. For example: `gs://my-bucket/folder/file1.rdb,gs://my-bucket/folder/file2.rdb`.
     * REGION_ID: the region where your instance is located (for example, `us-east1`).
     * NODE_TYPE (**Optional**): the [node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type) that you want to use for the instance. If you don't use the parameter, then `highmem-medium` is the default node type.

**Caution** : We recommend that you use the `shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Valkey in a production environment, then we recommend using another node type.
     * SHARD_COUNT: the number of shards for the instance (from 1 to 250).

For more options that you can use to create an instance, see [Create an instance](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances#create_an_instance).




## Cloud Monitoring metrics

To monitor recent backup and import operations, you can use Cloud Monitoring metrics. For a list of metrics that are available for Memorystore for Valkey backups, see [Backup metrics](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#backup_metrics).

## What's next

  * Read more about [backups](https://docs.cloud.google.com/memorystore/docs/valkey/backups).
  * Learn about [persistence](https://docs.cloud.google.com/memorystore/docs/valkey/persistence-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
