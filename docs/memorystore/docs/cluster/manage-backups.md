---
url: https://docs.cloud.google.com/memorystore/docs/cluster/manage-backups/
title: Manage backups \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:43.887028+00:00
---

# Manage backups  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/manage-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Manage backups Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to perform backup operations in Memorystore for Redis Cluster. You can use backups to restore the data of your cluster to a point in time, as well as to export and analyze the data.

**Note:** Before you read this page, familiarize yourself with [backups](https://docs.cloud.google.com/memorystore/docs/cluster/backups).

## Before you begin

Make sure that either you or the user account that you're using has the [required permissions](https://docs.cloud.google.com/memorystore/docs/cluster/access-control) for the action that you need to perform.

The **Redis Admin** and **Redis Editor** roles can perform all backup operations. The **Redis Viewer** role can view and export backups.

## Initiate an on-demand backup

You can take an on-demand backup for a cluster in Memorystore for Redis Cluster by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click the ID of the cluster for which you want to take a backup.

  3. In the side navigation panel, click **Backups**.

  4. Click **Create backup**.

  5. In the **Create backup** dialog, do the following:

     1. **Optional.** Provide a name for the backup. If you don't name the backup, then the backup has a date-and-time stamp for a name.
     2. Click **Create backup**.



### gcloud
    
    
    gcloud redis clusters create-backup CLUSTER_ID \
    --backup-id=BACKUP_ID \
    --ttl=TTL_PERIOD \
    --project=PROJECT_ID \
    --region=REGION
    

Replace the following:

  * CLUSTER_ID is the ID of the cluster for which you want to take a backup.
  * BACKUP_ID is an ID for the backup such as `december-2024-backup`
  * TTL_PERIOD specifies a time to live (TTL) for the backup. The backup is automatically deleted after reaching the TTL limit. Set to a number of days. For example, `14d`. The minimum value is 1 day. If not specified, the default value is 100 years.
  * PROJECT_ID is your project ID.
  * REGION is the region where your cluster is located (for example, `us-east1`).



The command returns an operation name with the following format:
    
    
    projects/PROJECT_ID/locations/REGION/operations/operation-UID
    

You can use the [`gcloud redis operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/operations/describe) command to check the status of an operation:
    
    
    gcloud redis operations describe projects/PROJECT_ID/locations/REGION/operations/operation-UID
    

You can also use the [`gcloud redis operations list`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/operations/list) command to list all operations in a project and region.

## Configure automated backup schedules

You can either configure a daily backup schedule when you create a cluster or you can enable a daily backup schedule on an existing cluster.

### Create a cluster with an automated backup schedule enabled

You can set a daily backup schedule as you create a cluster in Memorystore for Redis Cluster by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

To learn how to create a cluster and enable a backup schedule for the cluster automatically, see [Create an instance](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances#create_an_instance).

### gcloud
    
    
    gcloud redis clusters create CLUSTER_ID \
    --region=REGION_ID \
    --network=NETWORK \
    --shard-count=SHARD_COUNT \
    --automated-backup-mode=ENABLED \
    --automated-backup-start-time=START_TIME \
    --automated-backup-ttl=RETENTION_POLICY
    

Replace the following:

  * CLUSTER_ID is the ID of the cluster that you're creating.
  * REGION_ID is the region where you want the cluster to be located.

**Note:** You can only create clusters in [regions](https://docs.cloud.google.com/memorystore/docs/cluster/locations) that Memorystore for Redis Cluster supports.

  * NETWORK is the network that you use to create the cluster. It must use this format: `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_ID`. The network ID that you use here must match the network ID that the service connection policy uses. Otherwise, you can't create the cluster.

  * SHARD_COUNT determines the number of shards in the cluster. The shard count also determines the total memory capacity for storing cluster data. For more information about cluster specifications for Memorystore for Redis Cluster, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification).

  * START_TIME specifies when to begin taking backups. Specify the time in the format `HH:00` on a 24-hour cycle in UTC time. For example, `23:00`.

  * RETENTION_POLICY specifies how many days to retain each backup. Set to a number of days, for example, `7d`. The maximum is 365 days and the default is 35 days.

Even after a cluster is deleted, the backup is retained for the retention period with a maximum of 365 days. You must manually delete the backup to remove the backup before the retention period expires.




### Enable scheduled backups on an existing cluster

You can enable a daily backup schedule on an existing cluster by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Note:** You can enable scheduled backups on a cluster only if you didn't set a daily backup schedule when you created the cluster.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click the ID of the cluster for which you want to enable backups.

  3. In the side navigation panel, click **Backups**.

  4. In the **Settings** section, next to the **Automated daily backups** field, click _edit_ **Edit**.

This field has a status of **Disabled**. If this field has an **Enabled** status, then you already enabled scheduled backups for this cluster.

  5. In the **Automated backup settings** dialog, do the following:

     1. Select the **Automated daily backups** checkbox.
     2. In the **Days to retain backups** field, enter the number of days that you want Memorystore for Redis Cluster to keep backups before they're deleted automatically. You can specify from `1` to `365` days. The default value is `35` days.
     3. From the **Time window** menu, select the hour when Memorystore for Redis Cluster takes a daily backup.
     4. Click **Save**.



### gcloud
    
    
    gcloud redis clusters update CLUSTER_ID \
    --automated-backup-mode=enabled \
    --automated-backup-start-time=START_TIME \
    --automated-backup-ttl=RETENTION_POLICY
    

Replace the following:

  * CLUSTER_ID is the ID of the cluster that you're updating.
  * START_TIME A timestamp that specifies when to begin taking backups. The timestamp must be at the hour level and designates a one hour window when backups begin, for example, `2024-01-01T01:00:00Z`.

  * RETENTION_POLICY specifies how many days to retain each backup. Set to a number of days, for example, `7d`.

Even after a cluster is deleted, the backup is retained for the retention period. You must manually delete the backup to remove the backup before the retention period expires.




### Deactivate scheduled backups

You can deactivate scheduled backups on a cluster by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click the ID of the cluster for which you want to deactivate backups.

  3. In the side navigation panel, click **Backups**.

  4. In the **Settings** section, next to the **Automated daily backups** field, click _edit_ **Edit**.

This field has a status of **Enabled**. This field is enabled by default. If this field has a **Disabled** status, then you have already deactivated scheduled backups for this cluster.

  5. In the **Automated backup settings** dialog, do the following:

     1. Clear the **Automated daily backups** checkbox.
     2. Click **Save**.



### gcloud
    
    
    gcloud redis clusters update CLUSTER_ID \
    --automated-backup-mode=disabled
    

Replace CLUSTER_ID with the ID of the cluster that you're updating.

## Concurrency between backup and update cluster operations

Update operations and maintenance operations on a cluster can cancel ongoing backup operations in the following situations:

  * If there's an ongoing operation to update a cluster, then Memorystore for Redis Cluster rejects backup operations.
  * In rare circumstances, maintenance and backup operations might coincide with each other and lead to the backup operations being skipped for that cluster.



## List and describe backups

The following sections demonstrate how to find information about available backups.

### List backup collections

A _backup collection_ includes all backups that you take for a cluster. You can view a list of backup collections by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. In the side navigation panel, click **Backups**.




### gcloud
    
    
    gcloud redis clusters backup-collections list \
    --project=PROJECT_ID \
    --region=REGION
    

Replace the following:

  * REGION is the region where your cluster is located (for example, `us-east1`).
  * PROJECT_ID is your project ID.



The command returns a list of backup collections similar to the following:
    
    
    BACKUP_COLLECTION_NAME                CLUSTER_NAME                                           CLUSTER_UID
    6d9e1ff4-0f89-4c0a-a941-155dd4c3a213  projects/PROJECT_ID/locations/REGION/clusters/cluster1  6e539aed-ee7b-4eea-83ad-b4715b1ef160
    dda2f551-b416-47ff-b1cf-684e00483dc9  projects/PROJECT_ID/locations/REGION/clusters/cluster2  57130520-636c-4ac7-ad7e-86f7cfb32838
    

### List backups for a backup collection

You can view a list of backups for a backup collection by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. In the side navigation panel, click **Backups**.

  3. Click the ID of a cluster that's associated with a backup collection. This backup collection contains a list of backups that you want to view.




### gcloud
    
    
    gcloud redis clusters backups list \
    --backup-collection=BACKUP_COLLECTION
    --project=PROJECT_ID \
    --region=REGION
    

Replace the following:

  * BACKUP_COLLECTION is the name of a backup collection.
  * REGION is the region where your cluster is located such as `us-east1`.
  * PROJECT_ID is your project ID.



The command returns a list of backups similar to the following:
    
    
    BACKUP_NAME  STATE   CREATE_TIME                     EXPIRE_TIME
    backup-1     ACTIVE  2024-11-10T03:52:40.899882388Z  2124-11-10T03:53:02.856981736Z
    backup-2     ACTIVE  2024-11-11T03:48:22.137134936Z  2124-11-11T03:48:44.130735425Z
    

### Describe a backup

You can retrieve information about a backup by using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### gcloud
    
    
    gcloud redis clusters backups describe BACKUP_NAME \
    --backup-collections=BACKUP_COLLECTION
    --project=PROJECT_ID \
    --region=REGION
    

Replace the following:

  * BACKUP_NAME is the name of a backup such as `2024-05-01-10-15-00`.
  * BACKUP_COLLECTION is the name of a backup collection.
  * REGION is the region where your cluster is located such as `us-east1`.
  * PROJECT_ID is your project ID.



The command returns information about the backup similar to the following:
    
    
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
    cluster: projects/PROJECT_ID/locations/us-east1/clusters/cluster1
    clusterUid: 57130520-636c-4ac7-ad7e-86f7cfb32838
    createTime: '2024-11-10T03:52:40.899882388Z'
    expireTime: '2124-11-10T03:53:02.856981736Z'
    name: projects/PROJECT_ID/locations/us-east1/backupCollections/dda2f551-b416-47ff-b1cf-684e00483dc9/backups/december-2024-backup
    nodeType: REDIS_HIGHMEM_MEDIUM
    shardCount: 3
    state: ACTIVE
    totalSizeBytes: '2084589755'
    

### Delete a backup

You can delete a backup by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Note:** If you import data from a backup into a new cluster and then delete the backup, the cluster isn't impacted.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click the ID of the cluster, which contains a backup that you want to delete.

  3. In the side navigation panel, click **Backups**.

  4. Next to the backup that you want to delete, click _more_vert_ **More actions**.

  5. From the menu, select **Delete**.

  6. In the **Delete backup?** dialog, do the following:

     1. In the text field, enter `delete`.
     2. Click **Delete**.



### gcloud
    
    
    gcloud redis clusters backups delete BACKUP_NAME \
    --backup-collection=BACKUP_COLLECTION
    --project=PROJECT_ID \
    --region=REGION
    

Replace the following:

  * BACKUP_NAME is the name of a backup such as `2024-05-01-10-15-00`.
  * BACKUP_COLLECTION is the name of a backup collection.
  * REGION is the region where your cluster is located such as `us-east1`.
  * PROJECT_ID is your project ID.



## Export a backup to a storage bucket

You can export a backup to a Cloud Storage bucket by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Note:** Exporting a backup doesn't delete the backup from the backup collection automatically.

To export a backup, do the following:

  1. Memorystore for Redis Cluster must have permission to access the destination Cloud Storage bucket. Grant the Memorystore for Redis Cluster [service agent](https://docs.cloud.google.com/iam/docs/service-agents) access to the Cloud Storage resources.

The Memorystore for Redis Cluster service agent uses the following naming format:
         
         service-PROJECT_NUMBER@cloud-redis.iam.gserviceaccount.com
         

Replace PROJECT_NUMBER with the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project where the cluster or backup is located.

Grant the service agent a role that gives the `storage.buckets.get`, `storage.objects.create`, `storage.objects.delete`, and `storage.folders.create` permissions. For example, the following command grants the `Storage Admin` role for the specified bucket to the Memorystore for Redis Cluster service agent:

### gcloud
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
         --member=serviceAccount:service-PROJECT_NUMBER@cloud-redis.iam.gserviceaccount.com \
         --role=roles/storage.admin
         

Replace the following:

     * BUCKET_NAME is the name of the destination bucket.
     * PROJECT_NUMBER is the project number used in the service agent name.

  2. Export a backup to a Cloud Storage bucket.

### Console

     1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

     2. Click the ID of the cluster, which contains a backup that you want to export.

     3. In the side navigation panel, click **Backups**.

     4. Next to the backup that you want to export, click _more_vert_ **More actions**.

     5. From the menu, select **Export**.

     6. In the **Choose destination** section of the **Export backup to Cloud Storage** page, click **Browse**.

     7. In the **Select bucket** dialog, click the bucket to which you want to export the backup, and then click **Select**.

**Note:** If a bucket doesn't appear in the dialog, then [create](https://docs.cloud.google.com/storage/docs/creating-buckets) it. Also, the bucket must be a [regional](https://docs.cloud.google.com/storage/docs/locations#key-concepts) bucket and it must be in the same region as the backup. Memorystore for Redis Cluster must have permission to access the bucket, and to create folders and objects inside of the bucket.
     8. In the **Export backup to Cloud Storage** page, click **Export**.

### gcloud
    
    gcloud redis clusters backups export BACKUP_NAME \
    --region=REGION \
    --backup-collection=BACKUP_COLLECTION \
    --gcs-bucket=BUCKET
    

Replace the following:

     * BACKUP_NAME is the name of a Memorystore for Redis Cluster backup.
     * BACKUP_COLLECTION is the name of a backup collection.
     * REGION is the region where the backup collection is located such as `us-east1`.
     * BUCKET_NAME is a Cloud Storage bucket, which doesn't have `gs://` as a prefix.

The bucket must be a [regional](https://docs.cloud.google.com/storage/docs/locations#key-concepts) bucket and it must be in the same region as the backup. Memorystore for Redis Cluster must have permission to access the bucket, and to create folders and objects inside of the bucket.




## Restore data from a backup

To restore data from a backup, you can either seed a new cluster from a managed backup in the same project or you can seed a new cluster from Redis Database (RDB) files in a storage bucket. To seed a cluster from RDB files, Memorystore for Redis Cluster must have permission to access the files.

### Seed a new cluster from a backup

The following example demonstrates how to import data from a backup to a new cluster. The backup must be in the same region as the new cluster. The principal creating the cluster must have `redis.backups.get` permission for the backup.

You can import data from a backup into a new cluster by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click the ID of the cluster, which contains a backup that you want to import.

  3. In the side navigation panel, click **Backups**.

  4. Next to the backup that you want to import, click _more_vert_ **More actions**.

  5. From the menu, select **Import into new cluster**. The **Create a Redis Cluster instance** page appears.

  6. In the **Backup options** section, verify the following:

     1. The **Managed backups** option is selected.
     2. The **Backup ID** field contains the path and name of the backup that you selected.
  7. In the **Name your cluster instance** section, enter an ID for the cluster that you're creating. The Cluster ID must use only lowercase letters, numbers, and hyphens. It must also start with a letter and be unique in its region.

  8. From the **Region** menu, select a region for your cluster.

  9. In the **Zonal availability** section, specify whether you want to create a [single-zone or multi-zone](https://docs.cloud.google.com/memorystore/docs/cluster/single-zone-instances) cluster.

  10. **Optional**. In the **Node Type** section, select a [node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type).

**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type.
  11. **Optional**. In the **Cluster size** section, enter the number of shards for your cluster. The shard count determines the total memory capacity for storing cluster data. For more information about cluster specifications, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification).

  12. **Optional**. If you want to create a cluster with replicas, then in the **Replicas** section, select the number of replicas (per shard). You can select 0-5 replicas. The default value is 1 replica.

**Important:** Memorystore for Redis Cluster populates the **Node Type** , **Cluster size** , and **Replicas** sections automatically with values that are associated with the backup that you're importing. You can keep these values or increase them. For example, if the backup uses a **Medium** node type, then you can change it to **X-Large**. However, we strongly recommend that you don't _decrease_ any values in these sections. If you do, then you might experience issues with importing the backup into your cluster.
  13. In the **Set up connection** section, select the network that your applications can use to connect to this cluster. For more information about private networking for Memorystore for Redis Cluster, see [Networking overview](https://docs.cloud.google.com/memorystore/docs/cluster/networking).

  14. **Optional**. If you want to increase the security of your cluster, then in the **Security** section, enable [IAM authentication](https://docs.cloud.google.com/memorystore/docs/cluster/about-iam-auth) by selecting the **Enable IAM AUTH** checkbox.

**Note:** If you select this checkbox, then Memorystore for Redis Cluster selects the **Enable In-Transit Encryption (TLS)** checkbox automatically. As a result, Memorystore for Redis Cluster [encrypts](https://docs.cloud.google.com/memorystore/docs/cluster/about-in-transit-encryption) your credentials so that they're confidential when they're transmitted from the instance to the application.
  15. In the **Data persistence strategy** section, specify how you want Memorystore for Redis Cluster to persist the data in your cluster. Acceptable values are **No persistence** , [**Append Only File (AOF)** persistence](https://docs.cloud.google.com/memorystore/docs/cluster/about-aof-persistence), and [**Redis Database (RDB)** persistence](https://docs.cloud.google.com/memorystore/docs/cluster/about-rdb-persistence).

  16. **Optional**. If you want to enable [automated backups](https://docs.cloud.google.com/memorystore/docs/cluster/backups#automated_and_on-demand_backups) for your cluster, then do the following:

     1. Select the **Automated daily backups** checkbox.
     2. In the **Days to retain backups** field, enter the number of days that you want Memorystore for Redis Cluster to keep backups before they're deleted automatically. You can specify from `1` to `365` days. The default value is `35` days.
     3. From the **Time window** menu, select a time for the daily backup.
  17. Click **Create cluster**.




### gcloud
    
    
    gcloud redis clusters create CLUSTER_ID \
    --import-managed-backup=BACKUP_NAME \
    --region=REGION
    

Replace the following:

  * CLUSTER_ID is the ID of the cluster that you're creating.
  * BACKUP_NAME is the name of a manage backup. For example, `projects/PROJECT_ID/locations/REGION/backupCollections/BACKUP_COLLECTION_ID/backups/BACKUP_ID`.
  * REGION is the region where your cluster is located such as `us-east1`.



For more options that you can use to create a cluster, see [Create an instance](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances#create_an_instance).

### Seed a new cluster from RDB files in a storage bucket

The following example demonstrates how to import data from RDB files in a Cloud Storage bucket to a new cluster. The bucket must be a regional in the same region as the new cluster or dual-region bucket with one region the same.

To seed a cluster from RDB files in a Cloud Storage bucket, you must grant Memorystore for Redis Cluster access to the bucket and objects, and then import the data from the files.

You can import data from RDB files by using either the Google Cloud console or [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

  1. Memorystore for Redis Cluster must have permission to access the Cloud Storage objects. Grant the Memorystore for Redis Cluster [service agent](https://docs.cloud.google.com/iam/docs/service-agents) access to the Cloud Storage resources.

The Memorystore for Redis Cluster service agent uses the following naming format:
         
         service-PROJECT_NUMBER@cloud-redis.iam.gserviceaccount.com

Replace PROJECT_NUMBER with the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project where you will create the new cluster.

Grant the service agent a role that gives the `storage.buckets.get` and `storage.objects.get` permissions. For example, the following command grants the `Storage Admin` role to a Cloud Storage bucket:

### gcloud
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME --member=serviceAccount:service-PROJECT_NUMBER@cloud-redis.iam.gserviceaccount.com --role=roles/storage.admin
         

Replace the following:

     * BUCKET_NAME is the name of the bucket where the RDB files are located.
     * PROJECT_NUMBER is the project number used in the service agent name.

  2. Import data from RDB files in a Cloud Storage bucket into a new cluster.

### Console

     1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

     2. Next to **Create cluster** , click the _arrow_drop_down_ down arrow, and then select **Create from backup** from the menu that appears. The **Create a Redis Cluster instance** page appears.

     3. In the **Backup options** section, do the following:

        1. Select the **Cloud Storage folder** option.
        2. In the text field, click **Browse**.
        3. In the **Select folder** dialog, select the folder which contains the RDB files that you want to import.
        4. Click **Select**.
     4. In the **Name your cluster instance** section, enter an ID for the cluster. The Cluster ID must use only lowercase letters, numbers, and hyphens. It must also start with a letter and be unique in its region.

     5. From the **Region** menu, select a region for your cluster.

     6. In the **Zonal availability** section, specify whether you want to create a [single-zone or multi-zone](https://docs.cloud.google.com/memorystore/docs/cluster/single-zone-instances) cluster.

     7. **Optional**. In the **Node Type** section, select a [node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type).

**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type.
     8. In the **Cluster size** section, enter the number of shards for your cluster. The shard count determines the total memory capacity for storing cluster data. For more information about cluster specifications, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification).

     9. If you want to create a cluster with replicas, then in the **Replicas** section, select the number of replicas (per shard). You can select 0-5 replicas. The default value is 1 replica.

     10. In the **Set up connection** section, select the network that your applications can use to connect to this cluster. For more information about private networking for Memorystore for Redis Cluster, see [Networking overview](https://docs.cloud.google.com/memorystore/docs/cluster/networking).

     11. **Optional**. If you want to increase the security of your cluster, then in the **Security** section, enable [IAM authentication](https://docs.cloud.google.com/memorystore/docs/cluster/about-iam-auth) by selecting the **Enable IAM AUTH** checkbox.

**Note:** If you select this checkbox, then Memorystore for Redis Cluster selects the **Enable In-Transit Encryption (TLS)** checkbox automatically. As a result, Memorystore for Redis Cluster [encrypts](https://docs.cloud.google.com/memorystore/docs/cluster/about-in-transit-encryption) your credentials so that they're confidential when they're transmitted from the instance to the application.
     12. In the **Data persistence strategy** section, specify how you want Memorystore for Redis Cluster to persist the data in your cluster. Acceptable values are **No persistence** , [**Append Only File (AOF)** persistence](https://docs.cloud.google.com/memorystore/docs/cluster/about-aof-persistence), and [**Redis Database (RDB)** persistence](https://docs.cloud.google.com/memorystore/docs/cluster/about-rdb-persistence).

     13. **Optional**. If you want to enable [automated backups](https://docs.cloud.google.com/memorystore/docs/cluster/backups#automated_and_on-demand_backups) for your cluster, then do the following:

        1. Select the **Automated daily backups** checkbox.
        2. In the **Days to retain backups** field, enter the number of days that you want Memorystore for Redis Cluster to keep backups before they're deleted automatically. You can specify from `1` to `365` days. The default value is `35` days.
        3. From the **Time window** menu, select a time for the daily backup.
     14. Click **Create cluster**.

### gcloud
    
    gcloud redis clusters create CLUSTER_ID \
    --import-gcs-object-uris=URI \
    --region=REGION
    

Replace the following:

     * CLUSTER_ID is the ID of the cluster that you're creating.
     * URI is one or more Cloud Storage URIs separated by commas (`,`). For example, `gs://my-bucket/folder/file1.rdb,gs://my-bucket/folder/file2.rdb`.
     * REGION is the region where your cluster is located such as `us-east1`.

For more options that you can use to create a cluster, see [Create an instance](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances#create_an_instance).




## Cloud Monitoring metrics

You can use Cloud Monitoring metrics to monitor recent backup and import operations. For a list of metrics available for Memorystore for Redis Cluster backups, see [Backup metrics](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#backup_metrics).

## What's next

  * Read more about [backups](https://docs.cloud.google.com/memorystore/docs/cluster/backups).
  * Learn about [Persistence](https://docs.cloud.google.com/memorystore/docs/cluster/persistence-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
