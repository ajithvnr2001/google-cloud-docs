---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/backup-kubernetes/
title: Back up and restore in Kubernetes \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:27:42.636720+00:00
---

# Back up and restore in Kubernetes  |  AlloyDB Omni using the container orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/backup-kubernetes/

This page documents AlloyDB Omni version **18.1.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)



Send feedback 

#  Back up and restore in Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/backup-kubernetes)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/backup-kubernetes)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/backup-kubernetes)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/backup-kubernetes)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/backup-kubernetes)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/backup-kubernetes)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/backup-kubernetes)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/backup-kubernetes)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/backup-kubernetes)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/backup-kubernetes)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/backup-kubernetes)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/backup-kubernetes)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/backup-kubernetes)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/backup-kubernetes)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/backup-kubernetes)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/backup-kubernetes)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/backup-kubernetes)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/backup-kubernetes)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/backup-kubernetes)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/backup-kubernetes)



This page shows you how to back up and restore your AlloyDB Omni data using the AlloyDB Omni Kubernetes operator. This requires basic knowledge about updating a Kubernetes cluster using manifest files and the `kubectl` command-line tool. For more information about installing and running AlloyDB Omni on a Kubernetes cluster, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/deploy-kubernetes).

To enable AlloyDB Omni _continuous backup and recovery_ , you must create a backup plan for each database cluster. Backups are taken based on the backup schedules defined in the `backupPlan` resource. If no backup schedule is defined in the backup plan, continuous backups are taken daily by default. You can restore or clone backups from any timestamp in the recovery window at seconds granularity. Backups are transparent for TDE-enabled clusters, and you do not need to perform any additional steps to take a backup.

## Enable and schedule backups

Continuous backups are enabled when you create a backup plan resource for your database cluster. You must create a `backupPlan` resource for each database cluster to enable continuous backup for that cluster. This backup plan resource defines the following parameters:

  * The location that the AlloyDB Omni operator stores backups to. This can be local to your Kubernetes cluster, or to a Cloud Storage bucket.

  * An option to set multiple backup schedules that automatically create `full`, `incremental`, and `differential` backups. You can pause this schedule at any time, including when initially defining the backup plan. If a backup plan is paused, scheduled backups aren't created, but you can still use it to create backups manually.

If no backup schedules are specified, then the default is "0 0 * * *", which takes one daily full backup at midnight, local time.

  * A retention period for stored backups. This can be as short as one day, or as long as 90 days. The default value is 14.

  * You can take backups from either primary or standby Kubernetes clusters specifying either the `primary` or `standby` value for the `backupSourceStrategy` field respectively. To boost the performance of the primary cluster, offload backup operations by scheduling them from a standby cluster.


**Important:** Kubernetes [CronJobs](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#time-zones) that let you automate making backup schedules, interpret their CronJobs based on the local timezone of the `kube-controller-manager` component. If your `kube-controller-manager` runs in a timezone different from UTC, your backups might not run as expected. To have your backup schedules consistently interpreted in UTC, we strongly recommend adding the `timeZone: "Etc/UTC"` field to your `BackupPlan` spec.

Your database cluster can have up to one backup plan for each backup location type (local or Cloud Storage/S3-compatible), each with their own name cloud storage and configuration. If you create multiple `backupPlan` resources with different backup schedules for a database cluster, then you must define a unique backup location for each backup resource.

### Create a plan to store backups locally

To enable backups that get locally stored, apply the following manifest:
    
    
        apiVersion: alloydbomni.dbadmin.goog/v1
        kind: BackupPlan
        metadata:
          name: BACKUP_PLAN_NAME
          namespace: NAMESPACE
        spec:
          dbclusterRef: DB_CLUSTER_NAME
          backupSchedules:
            full: "FULL_CRON_SCHEDULE"
            differential: "DIFF_CRON_SCHEDULE"
            incremental: "INCR_CRON_SCHEDULE"
          backupRetainDays: RETENTION_DAYS
          backupSourceStrategy: SOURCE_STRATEGY
          paused: PAUSED_BOOLEAN
    

Replace the following:

  * `BACKUP_PLAN_NAME`: a name for this backup plan resource—for example, `backup-plan-1`.

  * `NAMESPACE`: the Kubernetes namespace for this backup plan. It must match the namespace of the database cluster.

  * `DB_CLUSTER_NAME`: the name of your database cluster, which you assigned when you [created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/deploy-kubernetes#create).

  * `FULL_CRON_SCHEDULE`: a backup schedule to create a full backup, containing all data, expressed in [`cron` format](https://en.wikipedia.org/wiki/Cron). For example, set to "0 0 * * 0" to take a full backup at 00:00 on every Sunday.

  * `DIFF_CRON_SCHEDULE`: a backup schedule to create backups that are initially full backups. Subsequent backups are differential, based on intervening changes to the data, expressed in [`cron` format](https://en.wikipedia.org/wiki/Cron). For example, set to "0 22 * * 3" to take a differential backup at 22:00 on every Wednesday.

  * `INCR_CRON_SCHEDULE`: a backup schedule to create backups that include data that has changed from the last full, differential, or incremental backup. It is expressed in [`cron` format](https://en.wikipedia.org/wiki/Cron). For example, set to "0 21 * * *" to take an incremental backup at 21:00 every day.

  * `RETENTION_DAYS`: the number of days for which the AlloyDB Omni operator retains this backup. It must be an integer between `1` and `90`. The default value is `14`.

  * `SOURCE_STRATEGY`: determines whether backups are taken from the primary or standby Kubernetes cluster. The default value is `primary`. You can choose from these values:

    * `primary`: backups are taken from the primary Kubernetes cluster.

    * `standby`: backups are taken from the standby Kubernetes cluster. If no standby instance is available when the `SOURCE_STRATEGY` field is set to `standby`, the backup is taken from the primary Kubernetes cluster instead.

  * `PAUSED_BOOLEAN`: specifies whether or not the backup plan is paused. Provide one of the following values:

    * `true`: backups are paused and no scheduled backups are created.

    * `false`: the AlloyDB Omni operator creates backups according to the schedule specified by `cronSchedule`. This is the default value, if not explicitly set to `true`.

The default value is `false`.




### Create a plan that stores backups in the Cloud Storage

To enable backups that get stored on Cloud Storage, follow these steps:

**Note:** If you choose to store backups locally, plan your disk space carefully. The longer retention period, the more space you need.

  1. [Create a Cloud Storage bucket.](https://docs.cloud.google.com/storage/docs/creating-buckets) Note the name that you assign to this bucket; you need it in a later step.

  2. [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) for adding backups to the bucket.

  3. [Grant the `storage.objectAdmin` Identity and Access Management role to the service account.](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts)

  4. [Create a key for the service account.](https://docs.cloud.google.com/iam/docs/keys-create-delete) This downloads the private key to your local environment.

  5. Rename the downloaded key file to `key.json`.

  6. Create a Kubernetes secret containing the private key:
         
         kubectl create secret generic SECRET_NAME --from-file=KEY_PATH -n NAMESPACE

Replace the following:

     * `SECRET_NAME`: the name of the Kubernetes secret that you are creating—for example, `gcs-key`.

     * `KEY_PATH`: the local file system path to the `key.json` file that you downloaded in the previous steps.

     * `NAMESPACE`: the namespace of the database cluster.

  7. Apply the following manifest:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
           kind: BackupPlan
           metadata:
             name: BACKUP_PLAN_NAME
             namespace: NAMESPACE
           spec:
             dbclusterRef: DB_CLUSTER_NAME
             backupSchedules:
               full: "FULL_CRON_SCHEDULE"
               differential: "DIFF_CRON_SCHEDULE"
               incremental: "INCR_CRON_SCHEDULE"
             backupRetainDays: RETENTION_DAYS
             backupSourceStrategy: SOURCE_STRATEGY
             paused: PAUSED_BOOLEAN
             backupLocation:
               type: GCS
               gcsOptions:
                 bucket: BUCKET_URL
                 key: BACKUP_PATH
                 secretRef:
                   name: SECRET_NAME
                   namespace: NAMESPACE
         

Replace the following:

     * `BACKUP_PLAN_NAME`: a name for this backup plan resource—for example, `backup-plan-1`.

     * `NAMESPACE`: the Kubernetes namespace for this backup plan. It must match the namespace of the database cluster.

     * `DB_CLUSTER_NAME`: the name of your database cluster, which you assigned when you [created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/deploy-kubernetes#create).

     * `FULL_CRON_SCHEDULE`: a backup schedule to create a full backup, containing all data, expressed in [`cron` format](https://en.wikipedia.org/wiki/Cron). For example, set to "0 0 * * 0" to take a full backup at 00:00 on every Sunday.

     * `DIFF_CRON_SCHEDULE`: a backup schedule to create backups that are initially full backups. Subsequent backups are differential, based on intervening changes to the data, expressed in [`cron` format](https://en.wikipedia.org/wiki/Cron). For example, set to "0 22 * * 3" to take a differential backup at 22:00 on every Wednesday.

     * `INCR_CRON_SCHEDULE`: a backup schedule to create backups that include data that has changed from the last full, differential, or incremental backup. It is expressed in [`cron` format](https://en.wikipedia.org/wiki/Cron). For example, set to "0 21 * * *" to take an incremental backup at 21:00 every day.

     * `RETENTION_DAYS`: the number of days for which the AlloyDB Omni operator retains this backup. It must be an integer between `1` and `90`. The default value is `14`.

     * `SOURCE_STRATEGY`: determines whether backups are taken from the primary or standby Kubernetes cluster. The default value is `primary`. You can choose from these values:

       * `primary`: backups are taken from the primary Kubernetes cluster.

       * `standby`: backups are taken from the standby Kubernetes cluster. If no standby instance is available when the `SOURCE_STRATEGY` field is set to `standby`, the backup is taken from the primary Kubernetes cluster instead.

     * `PAUSED_BOOLEAN`: specifies whether or not the backup plan is paused. Provide one of the following values:

       * `true`: backups are paused and no scheduled backups are created.

       * `false`: the AlloyDB Omni operator creates backups according to the schedule specified by `cronSchedule`. This is the default value, if not explicitly set to `true`.

The default value is `false`.

     * `BUCKET_URL`: the name of the Cloud Storage bucket that you created in an earlier step. This is not the full URL to the bucket; don't prefix the bucket name with `gs://`.

     * `BACKUP_PATH`: the path of the directory that the AlloyDB Omni operator writes backups into, within the Cloud Storage bucket. The path must be absolute, beginning with `/`.

     * `SECRET_NAME`: the name you chose for the Kubernetes secret that you created in an earlier step.




### Create backups to S3-compatible storage

You can use the `s30options` field to send backups to S3-compatible endpoints.

The steps in the following procedure are high-level. To get specific instructions for your use case, check the documentation for your S3 provider.

To enable backups on your S3-compatible storage, follow these high-level steps:

  1. Create an S3 storage bucket. Note the name that you assign to this bucket because you use it in a later step.
  2. To access the S3 storage bucket, create a principal, for example, a service account or user. Check with your S3 provider to learn if you need to grant a predefined role or policy to the principal.
  3. Grant read-write access to the principal that you created in the previous step. This step lets you read and write to the S3 storage bucket.
  4. Create an access key for the principal that you created. The access key includes a key ID and a key secret. This operation downloads the key to your local environment.
  5. Create a Kubernetes secret containing the key:
         
         kubectl create secret generic SECRET_NAME --from-literal=access-key-id=KEY_ID --from-literal=access-key=KEY -n NAMESPACE

Replace the following:

     * `SECRET_NAME`: the name of the Kubernetes secret that you're creating, for example, `s3-key`.
     * `KEY_ID`: the key ID of your access key.
     * `KEY`: the key secret of your access key.
     * `NAMESPACE`: the space within which the secret name is kept. This value must be unique.
  6. Apply the following manifest:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: BackupPlan
         metadata:
           name: BACKUP_PLAN_NAME
           namespace: NAMESPACE
         spec:
           dbclusterRef: DB_CLUSTER_NAME
           backupSchedules:
             full: "FULL_CRON_SCHEDULE"
             differential: "DIFF_CRON_SCHEDULE"
             incremental: "INCR_CRON_SCHEDULE"
           backupRetainDays: RETENTION_DAYS
           backupSourceStrategy: SOURCE_STRATEGY
           paused: PAUSED_BOOLEAN
           backupLocation:
             type: S3
             s3Options:
               bucket: BUCKET_NAME
               region: REGION
               endpoint: S3ENDPOINT
               key: BACKUP_PATH
               secretRef:
                 namespace: NAMESPACE
                 name: SECRET_NAME
               certRef:
                 name: CA_BUNDLE_SECRET_NAME
                 namespace: NAMESPACE
         

Replace the following:

     * `BACKUP_PLAN_NAME`: a name for this backup plan resource, for example, `backup-plan-1`.
     * `NAMESPACE`: the Kubernetes namespace for this backup plan. The namespace must match the namespace of the database cluster.
     * `DB_CLUSTER_NAME`: the name of your database cluster, which you assigned when you [created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/deploy-kubernetes#create).
     * `FULL_CRON_SCHEDULE`: a backup schedule to create a full backup, containing all data, expressed in [`cron` format](https://en.wikipedia.org/wiki/Cron). For example, to take a full backup at 00:00 on every Sunday, set `FULL_CRON_SCHEDULE` to   
`0 0 * * 0`.
     * `DIFF_CRON_SCHEDULE`: a backup schedule to create backups that are initially full backups. Subsequent backups are differential, based on intervening changes to the data, expressed in [`cron` format](https://en.wikipedia.org/wiki/Cron). For example, to take a differential backup at 22:00 on every Wednesday, set to `0 22 * * 3` .
     * `INCR_CRON_SCHEDULE`: a backup schedule to create backups that include data that changed from the last full, differential, or incremental backup. This is expressed in [`cron` format](https://en.wikipedia.org/wiki/Cron). For example, to take an incremental backup at 21:00 every day, set this to `0 21 * * *` .
     * `RETENTION_DAYS`: the number of days for which the AlloyDB Omni Kubernetes operator retains this backup. This parameter must be an integer between `1` and `90`. The default value is `14`.
     * `SOURCE_STRATEGY`: determines whether backups are taken from the primary or standby Kubernetes cluster. The default value is `primary`. You can choose from these values: 
       * `primary`: backups are taken from the primary Kubernetes cluster.
       * `standby`: backups are taken from the standby Kubernetes cluster. If no standby instance is available when the `SOURCE_STRATEGY` field is set to `standby`, the backup is taken from the primary Kubernetes cluster instead.
     * `PAUSED_BOOLEAN`: specifies whether or not the backup plan is paused. Provide one of the following values: 
       * `true`: backups are paused and no scheduled backups are created.
       * `false`: the default value. The AlloyDB Omni operator creates backups according to the schedule specified by `cronSchedule`. This is the default value, if not explicitly set to `true`.
     * `BUCKET_NAME`: the name of the S3 storage bucket that you created. The bucket name isn't the full URL to the bucket. Don't prefix the bucket name with `gs://`.
     * `REGION`: the region where the S3 bucket is stored.
     * `S3ENDPOINT`: the endpoint for the S3 storage bucket.
     * `BACKUP_PATH`: the path of the directory that the AlloyDB Omni operator writes backups into, within the S3 storage bucket. The path must be absolute, and it must begin with `/`.
     * `NAMESPACE`: the space within which the secret name must be unique.
     * `SECRET_NAME`: the name you chose for the Kubernetes secret that you created.
     * `CA_BUNDLE_SECRET_NAME`: a pool of PEM-encoded CA certs that the S3 server uses to validate the certificate. Make sure that the bundle is included in the secret under a key named `ca.crt`.

The following example shows you how to create a secret that contains the cert, where `PEM_FILE_PATH` is the path to the `ca` bundle file:
           
           kubectl create secret generic CA_BUNDLE_SECRET_NAME -n NAMESPACE --from-file=ca.crt=PEM_FILE_PATH
           




## Manually create a backup

You can manually create a backup resource at any time, using any backup plan that you have already applied to a database cluster. The AlloyDB Omni operator applies the chosen backup plan's storage location and retention period to the new manual backup.

To manually create a backup from either a primary or standby Kubernetes cluster, you must specify the source database instance for the backup using the `backupSourceRole` field and apply the following manifest:
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Backup
    metadata:
      name: BACKUP_NAME
      namespace: NAMESPACE
    spec:
      dbclusterRef: DB_CLUSTER_NAME
      backupPlanRef: BACKUP_PLAN_NAME
      manual: true
      backupSourceRole: SOURCE_ROLE
      physicalBackupSpec:
        backupType: BACKUP_TYPE
    

Replace the following:

  * `BACKUP_NAME`: a name for this backup—for example, `backup-1`.

  * `NAMESPACE`: the Kubernetes namespace of this restore. It must match the namespace of the database cluster.

  * `BACKUP_PLAN_NAME`: the name of the backup plan resource that this backup belongs to. It must match the name you chose when you created the backup plan.

  * `DB_CLUSTER_NAME`: the name of your database cluster, which you assigned when you [created it](https://docs.cloud.google.com/alloydb/omni/15-next/docs/deploy-kubernetes#create).

  * `SOURCE_ROLE`: specifies the role of the source database instance from which the manual backup is taken. The default value is `primary`. You can choose one of the following values:

    * `primary`: configure the backup from the primary Kubernetes cluster.
    * `standby`: configure the backup from the standby Kubernetes cluster.
  * `BACKUP_TYPE`: specifies the type of manual backup you want to create. Choose from one of the following values:

    * `full`: creates a full backup, containing all data.

    * `diff`: creates a differential backup that depends on the last full backup. Subsequent backups are differential, based on intervening changes to the data.

    * `incr`: creates an incremental backup that depends on the previous full or differential backup to include data that has changed from the last full or differential.




## Monitor and list backups

Your backup plans and backups are all resources on your Kubernetes cluster. To view information about them, use the [`kubectl get`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get) command.

### View a backup plan summary

To view information about your database cluster's backup plans, run the following command:
    
    
    kubectl get backupplan.alloydbomni.dbadmin.goog -n NAMESPACE

Replace `NAMESPACE` with the namespace of the database cluster.

The output resembles the following:
    
    
    NAME               PHASE   LASTBACKUPTIME         NEXTBACKUPTIME
    backup-plan-prod   Ready   2023-10-26T17:26:43Z   2023-10-27T00:00:00Z
    

### View a list of backups

To view a list of backups available to your database cluster, run the following command:
    
    
    kubectl get backup.alloydbomni.dbadmin.goog -n NAMESPACE

Replace `NAMESPACE` with the namespace of the database cluster.

The output resembles the following:
    
    
    NAME                              PHASE       COMPLETETIME
    backup-plan-prod-20231026172643   Succeeded   2023-10-26T17:26:53Z
    manual-backup-1                   Succeeded   2023-10-26T18:15:27Z
    manual-backup-2                   InProgress
    

Each row in the output table represents a backup resource, with the following attributes:

  * The name of the backup.
  * The state of the backup, with `Succeeded` marking a backup ready to restore from.
  * The timestamp of the backup's creation.



## Restore from a backup

**Caution:** Restoring from a backup overwrites all of your database cluster's data.**Note:** When you specify a point in time for restore, make sure that the timestamp you select is before the last transaction commit time. If you attempt to restore to a timestamp after the last transaction commit time, the restore operation might fail with the error `recovery ended before configured recovery target was reached`.

AlloyDB Omni lets you restore from individual backups or clone a cluster using a backup from a specific point in time.

Before you restore from a TDE-enabled cluster backup, make sure that the `tdeConfig` resource is available in the same namespace as the `dbcluster` resource.

### Restore from a named backup

To restore from a backup, replacing the data in your database cluster with the data in the backup, follow these steps.

  1. List all backups whose phase is `Succeeded`.
         
         kubectl get backup.alloydbomni.dbadmin.goog -n NAMESPACE | grep Succeeded

Replace `NAMESPACE` with the namespace of the database cluster.

If at least one good backup candidate exists, then the output resembles the following:
         
         backup-plan-prod-20231026172643   Succeeded   2023-10-26T17:26:53Z
         manual-backup-1                   Succeeded   2023-10-26T18:15:27Z
         

  2. Choose one of the backups listed in the previous step as the backup to restore from. Take note of its name, which you use in the following step.

  3. Apply the following manifest:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
           kind: Restore
           metadata:
             name: RESTORE_NAME
             namespace: NAMESPACE
           spec:
             sourceDBCluster: DB_CLUSTER_NAME
             backup: BACKUP_NAME
         

Replace the following:

     * RESTORE_NAME: a name to use with the data-restore resource that this manifest creates—for example, `restore-1`.

     * DB_CLUSTER_NAME: the name of your database cluster, which you assigned when you [created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/deploy-kubernetes#create).

     * BACKUP_NAME: the name of the backup that you chose in the previous step.




### Clone a cluster from a point in time

AlloyDB Omni operator lets you clone cluster's data from any point in time within a recovery window. The length of the recovery window is directly determined by the retention period.

For example, if your retention period is set to 14 days, then you cannot recover data older than 14 days. You can restore to any point in time within the recovery window. AlloyDB Omni operator retains backups and logs for one day longer than the specified value.

**Note:** AlloyDB Omni operator only supports clone from point in time within the same namespace and same kubernetes cluster. Cross namespace cloning is not supported. For cross cluster restore or clone, see the backup and restore based disaster recovery [manual](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/kubernetes-dr-backup-overview).

  1. Monitor your recovery window to identify the point of restore:
         
         kubectl get backupplan.alloydbomni.dbadmin.goog BACKUP_NAME -n NAMESPACE -o json | jq .status.recoveryWindow
         

The following shows an example response:
         
         recoveryWindow:
         begin: "2024-01-31T02:54:35Z"
         

The timestamp value in the RFC 3339 timestamp format is used in the restore resource.

  2. Create and apply the following restore resource manifest:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: Restore
         metadata:
           name: RESTORE_NAME
           namespace: NAMESPACE
         spec:
           sourceDBCluster: DB_CLUSTER_NAME
           pointInTime: "DATE_AND_TIME_STAMP"
           clonedDBClusterConfig:
             dbclusterName: NEW_DB_CLUSTER_NAME
         

Replace the following:

     * RESTORE_NAME: a name to use with the data-restore resource that this manifest creates—for example, `restore-1`.

     * DB_CLUSTER_NAME: the name of your database cluster, which you assigned when you [created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/deploy-kubernetes#create).

     * DATE_AND_TIME_STAMP: the RFC 3339 timestamp at minute granularity of the continuous backup you want to restore from—for example, `2024-03-05T15:32:10Z`.

     * NEW_DB_CLUSTER_NAME: the name of the new database cluster.




### View restore status

  1. View progress of the restore operation:
         
         kubectl get restore.alloydbomni.dbadmin.goog -n NAMESPACE

Replace `NAMESPACE` with the namespace of the database cluster.

To run the command continuously, add the flag `-Aw`.

The output resembles the following:
         
         NAME        PHASE               COMPLETETIME   RESTOREDPOINTINTIME
         restore-1   RestoreInProgress
         

When the value of the `PHASE` column in the output table reads `ProvisionSucceeded`, then the restore is complete.

  2. View progress of the restored or cloned database cluster coming online:
         
         kubectl get dbclusters -A -n NAMESPACE

Replace `NAMESPACE` with the namespace of the database cluster.

To run the command continuously, add the flag `-Aw`.

The output resembles the following:
         
         NAMESPACE   NAME               PRIMARYENDPOINT   PRIMARYPHASE   DBCLUSTERPHASE
         default     db-cluster-1       10.128.0.55       Ready          DBClusterReady
         

When the value of the `DBCLUSTERPHASE` column in the output table reads `DBClusterReady`, then the restored or cloned database cluster is ready for use.




## Delete a backup

Usually, you don't need to manually delete backups. The AlloyDB Omni operator automatically deletes backups older than the retention period that you specify when creating a backup plan.

If you do want to manually delete a backup, the backup must meet the following requirements:

  * The backup is not the only backup stored for its backup plan. The AlloyDB Omni operator requires that at least one backup exists per backup plan.

  * The backup has no other backups depending on it. For example, a full backup with differential or incremental backups that depend on it; or an incremental backup with differential backups that depend on it.




To delete a backup, run the following command:
    
    
    kubectl delete backup.alloydbomni.dbadmin.goog/BACKUP_NAME -n NAMESPACE

Replace the following:

  * `BACKUP_NAME`: the name of the backup to delete.

  * `NAMESPACE`: the namespace of the database cluster.




## Resize a backup disk

To resize the local disk that stores your backups in the Kubernetes cluster, complete the following steps:

  1. Update the `resources.disks` field of the DBCluster manifest as follows:
         
         spec:
           primarySpec:
             resources:
               disks:
                 - name: BACKUP_DISK
                   size: 10Gi
         

Replace `BACKUP_DISK` with the name of the disk storing your backups.

  2. Apply the manifest to enforce the update.

The AlloyDB Omni operator applies the updated specifications to your DBCluster immediately.




The following restrictions apply to modifying a running database cluster's backup disk:

  * You can increase a disk's size only if the specified `storageClass` supports volume expansion.
  * You can't decrease a disk's size.



## Update a backup plan

Every backup plan is a Kubernetes resource. To update its configuration, do one of the following:

  * Edit and re-apply the manifest file of the backup plan.

  * Use the [`kubectl patch`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#patch) command.




For example, to pause a running backup plan, change the `paused` attribute of its manifest to `true`, and then re-apply the manifest.

## Delete a backup plan

**Caution:** Deleting a backup plan permanently erases all backups associated with that plan.

To delete a backup plan and remove all of its backup resources, run the following command:
    
    
    kubectl delete backupplan.alloydbomni.dbadmin.goog/BACKUP_PLAN_NAME -n NAMESPACE

Replace the following:

  * `BACKUP_PLAN_NAME`: the name of the backup plan to delete.

  * `NAMESPACE`: the namespace of the database cluster.




To pause a backup plan without deleting it, set the `paused` attribute of the backup plan's resource to `true`. A paused backup plan continues to store backups and allow manual backup creation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
