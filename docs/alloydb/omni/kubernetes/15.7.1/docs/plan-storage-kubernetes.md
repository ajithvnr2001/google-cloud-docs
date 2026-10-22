---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/plan-storage-kubernetes/
title: Plan storage and PVC sizes \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.7.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:11:22.288519+00:00
---

# Plan storage and PVC sizes  |  AlloyDB Omni for Kubernetes: 15.7.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/plan-storage-kubernetes/

This page documents AlloyDB Omni version **15.7.1** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/overview)



Send feedback 

#  Plan storage and PVC sizes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.1keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/plan-storage-kubernetes)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/plan-storage-kubernetes)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/plan-storage-kubernetes)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/plan-storage-kubernetes)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/plan-storage-kubernetes)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/plan-storage-kubernetes)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/plan-storage-kubernetes)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/plan-storage-kubernetes)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/plan-storage-kubernetes)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/plan-storage-kubernetes)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/plan-storage-kubernetes)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/plan-storage-kubernetes)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/plan-storage-kubernetes)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/plan-storage-kubernetes)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/plan-storage-kubernetes)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/plan-storage-kubernetes)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/plan-storage-kubernetes)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/plan-storage-kubernetes)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/plan-storage-kubernetes)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/plan-storage-kubernetes)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/plan-storage-kubernetes)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/plan-storage-kubernetes)

To prevent database downtime and data loss caused by storage exhaustion, you must appropriately plan the storage and Persistent Volume Claim (PVC) capacities for your AlloyDB Omni database clusters (`DBCluster`). Use these sizing recommendations to configure your volumes when deploying on Kubernetes by using the AlloyDB Omni Kubernetes operator. 

When you [create a `DBCluster` custom resource](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/deploy-kubernetes#create), the AlloyDB Omni operator provisions Kubernetes PVCs based on the disks that you define in the following fields:

  * Primary and high availability (HA) standby instances: configured in the `spec.primarySpec.resources.disks` field on your `DBCluster` custom resource. If you [enable high availability](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/kubernetes-ha#enable) by configuring the `spec.availability.numberOfStandbys` field, each standby replica uses the same disk configuration as the primary instance.
  * Read pool instances: configured in `spec.resources.disks` on each [`DBInstance` custom resource](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/kubernetes-read-pool) where the `instanceType` is set to `ReadPool`. If you omit the `spec.resources` section on a `DBInstance` resource, the read pool instance inherits the disk configuration from the parent `DBCluster` resource's `spec.primarySpec.resources` field.



## Supported PVC volumes

The AlloyDB Omni operator doesn't provision all PVC volumes at the same time:

  * Always provisioned: the operator always provisions `DataDisk`, `ObsDisk`, `BackupDisk`, and `LogDisk` for all primary, HA standby, and read pool database instance Pods. You must explicitly specify `DataDisk` and its size in your manifest. Specifying `ObsDisk`, `BackupDisk`, and `LogDisk` in your manifest is optional. If you omit them, as shown in the basic [installation manifest](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/deploy-kubernetes#create), the operator still provisions these PVCs using their default sizes.
  * Not provisioned by default: the operator doesn't provision the `BackupRepoDisk` volume when you create a standalone `DBCluster` resource or when you [store backups in Cloud Storage](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/backup-kubernetes#remote) or Amazon S3. It provisions the backup repository Pod and its `BackupRepoDisk` PVC only when you [create a `BackupPlan` resource to store backups locally](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/backup-kubernetes#local) on your Kubernetes cluster (that is, a `BackupPlan` resource without a remote `backupLocation` field).



The following table describes the persistent volumes that the AlloyDB Omni operator manages:

Disk name | Mount path | Target Pod | Manifest configuration | Provisioning behavior | Purpose  
---|---|---|---|---|---  
`DataDisk` | `/mnt/disks/pgsql` | Database Pod | Required | Always provisioned for each database Pod. | Stores the PostgreSQL database cluster directory (`PGDATA`), tables, indexes, temporary files, and active write-ahead log (WAL) segments.  
`ObsDisk` | `/obs` | Database Pod | Optional (default: `2Gi`) | Always provisioned for each database Pod. | Stores observability data, including PostgreSQL server logs (`postgresql.log`), pgAudit logs (`postgresql.audit`), internal logs (`postgresql.internal`), and rotated `.gz` log archives.  
`BackupDisk` | `/backup` | Database Pod | Optional (default: `10Gi`) | Always provisioned for each database Pod. | Provides a local staging directory for backup operations on the database Pod.  
`LogDisk` | `/archive` | Database Pod | Optional (default: `2Gi`) | Always provisioned for each database Pod. | Provides a dedicated WAL archive destination for custom or third-party backup sidecars. If you don't use a custom WAL-archiving sidecar, you can omit this disk from your manifest and leave it at its default `2Gi` size.  
`BackupRepoDisk` | `/backup` | Backup repository Pod | Optional (default: `10Gi`) | Not provisioned by default. Provisioned only when a `BackupPlan` resource [stores backups locally](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/backup-kubernetes#local) (not provisioned when no `BackupPlan` is configured or when backups use Cloud Storage or Amazon S3). | Provides a dedicated volume that stores physical database backups, incremental and differential backups, and archived WAL files when you use local storage backups.  
  
## PVC sizing recommendations

Use the following guidelines to size each PVC volume based on your workload, logging configuration, and backup strategy.

### `DataDisk` volume for primary database storage

**Caution:** If the `DataDisk` volume runs out of space and reaches 100% capacity, the PostgreSQL database process shuts down to prevent data corruption.

The AlloyDB Omni operator always provisions the `DataDisk` volume for every database Pod, and you must explicitly specify its size in your manifest. To estimate the minimum capacity for `DataDisk`, use the following formula:
    
    
    DataDisk capacity = (initial_dataset_size + projected_growth + max_wal_size) * 1.30
    

When you size the `DataDisk` volume, consider the following factors:

  * Index overhead: PostgreSQL indexes and system catalog tables typically require an additional 20% to 50% of storage beyond raw table data.
  * Active WAL headroom: high-throughput write transactions accumulate WAL files in the `pg_wal` directory until checkpoints complete. Allocate enough storage to accommodate your configured `max_wal_size` database parameter (typically several gigabytes to tens of gigabytes, depending on your workload). To view or modify database parameters such as `max_wal_size`, see [Configure database parameters](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/configure-database-flags).
  * Temporary files and vacuum operations: query sorting, index creation, reindexing, and autovacuum operations require additional temporary disk space.
  * General sizing rule: allocate 1.5 to 2 times your raw database size, including at least a 30% safety buffer.



### `ObsDisk` volume for diagnostic and audit logs

The AlloyDB Omni operator always provisions the `ObsDisk` volume for every database Pod (with the `2Gi` default size if you omit it from your manifest). If the `ObsDisk` volume fills up, PostgreSQL can't write new log entries, and log rotation can stall. For information about how to configure log rotation and retention settings for the `ObsDisk` volume, see [Configure log rotation](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/configure-log-rotation).

When you size the `ObsDisk` volume, consider the following guidelines:

  * Standard logging: a volume of 4 GiB to 10 GiB is sufficient for standard operational logging under the default log rotation settings (200 MB rotation threshold and 7-day retention).
  * Audit logging (pgAudit): when you [enable audit logging with pgAudit](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/configure-log-rotation#manage-audit-logs-pgaudit), audit logging generates significantly higher log volume. Allocate 20 GiB to 50 GiB or more, depending on your query rate and audit rule verbosity.



### `BackupRepoDisk` volume for local backup repository

Unlike the database Pod disks, `BackupRepoDisk` isn't provisioned by default. The AlloyDB Omni operator provisions the backup repository Pod and its `BackupRepoDisk` PVC only when you create a [BackupPlan resource to store backups locally](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/backup-kubernetes#local) on your Kubernetes cluster without a remote `backupLocation` field. If you omit this disk from your `DBCluster` manifest, it uses the default size of `10Gi`. If you don't configure a `BackupPlan` resource, or if your `BackupPlan` resource uses Cloud Storage with the `GCS` type or Amazon S3 with the `S3` type, the operator doesn't provision `BackupRepoDisk`. For more information about configuring backup plans and resizing backup storage, see [Back up and restore in Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/backup-kubernetes) and [Resize a backup disk](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/backup-kubernetes#resize-backup-disk).

When you store backups locally, the `BackupRepoDisk` volume stores compressed full, differential, and incremental backups along with archived WAL files. The total storage required depends on your database size, daily data change rate, the backup schedule defined in `backupSchedules`, and the retention period set by `backupRetainDays`:

  * Backup compression: compressed backups typically use 37% to 38% of the uncompressed database size, representing a 62% to 63% size reduction. For example, a 50 GiB database compresses to approximately 18.5 GiB.
  * Backup schedule and retention: combining weekly full backups with daily incremental or differential backups requires significantly less storage than taking daily full backups.



The following table shows the benchmarked peak storage usage and recommended `BackupRepoDisk` size (including a 20% buffer) across different backup schedules for a 100 GiB database with a 10% daily data change rate and the default 14-day retention period (`backupRetainDays: 14`):

Backup schedule (`backupSchedules`) | Peak full backups | Differential backups | Incremental backups | Archived WAL files | Peak storage used | Recommended `BackupRepoDisk` size (+20% buffer)  
---|---|---|---|---|---|---  
Weekly full + daily incremental | 148.0 GiB | 0 GiB | 66.6 GiB | 155.4 GiB | 370.0 GiB | 444 GiB (~4.4x database size)  
Weekly full + mid-week differential + daily incremental | 148.0 GiB | 22.2 GiB | 44.4 GiB | 155.4 GiB | 370.0 GiB | 444 GiB (~4.4x database size)  
Weekly full + daily differential | 148.0 GiB | 155.4 GiB | 0 GiB | 155.4 GiB | 458.8 GiB | 551 GiB (~5.5x database size)  
Daily full only (default schedule) | 592.0 GiB | 0 GiB | 0 GiB | 111.0 GiB | 703.0 GiB | 844 GiB (~8.4x database size)  
  
### `BackupDisk` volume for database Pod backup staging

The AlloyDB Omni operator always provisions the `BackupDisk` volume for every database Pod with a default size of 10 GiB (`10Gi`). AlloyDB Omni uses the `BackupDisk` volume as a local staging directory during backup operations. Because the default 10 GiB size is sufficient for standard operations, you can omit `BackupDisk` from your `DBCluster` manifest to use the default size.

### `LogDisk` volume for custom WAL archiving

The AlloyDB Omni operator always provisions the `LogDisk` volume for every database Pod with a default size of 2 GiB (`2Gi`). You only need to specify a custom size for the `LogDisk` volume if you deploy a [custom or third-party sidecar container](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/kubernetes-sidecar-container) that archives WAL files to the `/archive` directory. For standard AlloyDB Omni operator deployments that use built-in backups, you can omit `LogDisk` from your `DBCluster` manifest and leave it at its default `2Gi` size.

## Sizing reference by dataset size

The following table provides recommended PVC sizes for common raw dataset sizes:

Raw data size | Recommended `DataDisk` size | Recommended `ObsDisk` size | Recommended `BackupRepoDisk` size (provisioned for local backups only) | Recommended `BackupDisk` size | Recommended `LogDisk` size  
---|---|---|---|---|---  
50 GiB | 100 GiB | 4 GiB (10 to 20 GiB with pgAudit) | 150 GiB | 10 GiB (default) | 2 GiB (default)  
200 GiB | 400 GiB | 10 GiB (20 to 50 GiB with pgAudit) | 600 GiB | 10 GiB (default) | 2 GiB (default)  
500 GiB | 1,000 GiB (1 TiB) | 15 GiB (30 to 60 GiB with pgAudit) | 1,500 GiB (1.5 TiB) | 10 GiB (default) | 2 GiB (default)  
1 TiB | 2,000 GiB (2 TiB) | 20 GiB (50 to 100 GiB with pgAudit) | 3,000 GiB (3 TiB) | 10 GiB (default) | 2 GiB (default)  
  
## Monitor disk usage and I/O metrics

You can monitor live disk usage directly inside your database and backup repository Pods by using `kubectl` or by collecting Prometheus metrics exported by AlloyDB Omni.

### Check disk usage by using `kubectl`

To check the current disk space usage of the mounted PVC volumes inside your database Pod and backup repository Pod, run the following commands:

  1. Get the name of the database Pod for your `DBCluster` resource:
         
         export DB_POD=$(kubectl get pod -n NAMESPACE -l alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME,alloydbomni.internal.dbadmin.goog/task-type=database -o jsonpath='{.items[0].metadata.name}')

Replace the following:

     * `NAMESPACE`: the Kubernetes namespace where your database cluster is deployed.
     * `DB_CLUSTER_NAME`: the name of your database cluster.
  2. Run `df -h` inside the database container to view the capacity and usage of the `DataDisk` (`/mnt/disks/pgsql`), `ObsDisk` (`/obs`), `BackupDisk` (`/backup`), and `LogDisk` (`/archive`) volumes:
         
         kubectl exec -n NAMESPACE "${DB_POD}" -c database -- df -h /mnt/disks/pgsql /obs /backup /archive

  3. If you [configured a `BackupPlan` resource to store backups locally](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/backup-kubernetes#local), get the name of the backup repository Pod and run `df -h` to view the capacity and usage of the `BackupRepoDisk` volume (`/backup`):
         
         export BACKUP_REPO_POD=$(kubectl get pod -n NAMESPACE -l alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME,alloydbomni.internal.dbadmin.goog/backup-repository -o jsonpath='{.items[0].metadata.name}')
         kubectl exec -n NAMESPACE "${BACKUP_REPO_POD}" -c backuprepo -- df -h /backup




### Monitor storage metrics by using Prometheus

AlloyDB Omni exports storage and disk I/O metrics on the `al-INSTANCE_ID-DB_CLUSTER_NAME-monitoring-system` service (port `9187`). To learn how to scrape and query these metrics, see [Monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/manage#monitor). For a complete list of available metrics, see [AlloyDB Omni metrics](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/reference/omni-metrics).

Monitor the following disk metrics:

  * Storage usage and capacity: Monitor the `alloydb_omni_node_storage_usage_per_disk_byte` and `alloydb_omni_node_storage_limit_per_disk_byte` metrics, which report the used storage and total capacity in bytes for each volume by using the `disk` label (for example, `DataDisk`, `ObsDisk`, or `BackupDisk`). Configure alerts when disk usage reaches 80% and 90% of capacity so that you can expand volumes before they run out of space.
  * Disk throughput and I/O operations: Monitor the `alloydb_omni_node_storage_read_bytes_count_total` and `alloydb_omni_node_storage_write_bytes_count_total` metrics for disk read and write throughput, and the `alloydb_omni_node_storage_read_ops_count_total` and `alloydb_omni_node_storage_write_ops_count_total` metrics for read and write I/O operations.



## Resize PVCs for an existing `DBCluster`

If you already created a `DBCluster` resource following [Create a database cluster](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/deploy-kubernetes#create), your initial manifest likely specified only the `DataDisk` volume (for example, `10Gi`), while the AlloyDB Omni operator provisioned the `ObsDisk` (`2Gi`), `BackupDisk` (`10Gi`), and `LogDisk` (`2Gi`) volumes with their default sizes. You can expand any of these PVCs by updating your `DBCluster` manifest.

Before you resize a PVC, review the following requirements and limitations:

  * StorageClass volume expansion: You can increase a disk's size only if its Kubernetes [`StorageClass` resource](https://kubernetes.io/docs/concepts/storage/storage-classes/) sets `allowVolumeExpansion: true`. For more information, see [Expanding Persistent Volumes Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims).
  * No shrinking or StorageClass changes: You can't decrease a disk's size, and you can't change the `storageClass` field of an existing PVC after it is provisioned.
  * Resizing default-sized disks: To expand a disk that you previously omitted from your manifest (such as the `ObsDisk` volume or `BackupRepoDisk` volume), add an entry for that disk to the `spec.primarySpec.resources.disks` field with a `size` field larger than its current default capacity. Always keep `DataDisk` and any other existing disk entries in the `disks` list when you update the manifest.
  * Pod restart behavior: When you modify the `resources.disks` field, the AlloyDB Omni operator updates the underlying PVC and restarts the database instance Pod to apply the new resource specification. Perform storage expansion during a planned maintenance window or configure [high availability](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/kubernetes-ha) to minimize downtime.



To inspect and resize the PVCs for your `DBCluster`, follow these steps:

  1. List the PVCs in your database cluster's namespace to check their current capacities and `StorageClass` resource:
         
         kubectl get pvc -n NAMESPACE

Replace `NAMESPACE` with the namespace where you deployed your `DBCluster` (for example, `default`).

The output is similar to the following for a cluster named `my-db-cluster`:
         
         NAME                                STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
         backupdisk-al-1060-my-db-cluster-0  Bound    pvc-45a28be2-a111-40ed-9641-61b9d25f313b   10Gi       RWO            standard-rwo   10m
         datadisk-al-1060-my-db-cluster-0    Bound    pvc-c23a1ab8-f97c-4449-9072-502b6d9ba869   10Gi       RWO            standard-rwo   10m
         logdisk-al-1060-my-db-cluster-0     Bound    pvc-f0c41d15-bb13-4d28-b94b-01a28dc67ef6   2Gi        RWO            standard-rwo   10m
         obsdisk-al-1060-my-db-cluster-0     Bound    pvc-69ea1ca7-a868-4dc9-a9f8-503d5e5f2387   2Gi        RWO            standard-rwo   10m
         

  2. Verify that the `StorageClass` resource used by your PVCs supports volume expansion:
         
         kubectl get storageclass STORAGE_CLASS_NAME -o jsonpath='{.allowVolumeExpansion}{"\n"}'

Replace `STORAGE_CLASS_NAME` with the storage class name from the `STORAGECLASS` column of the previous output (for example, `standard-rwo`). Confirm that the command returns `true`.

  3. Update the `spec.primarySpec.resources.disks` field in your `DBCluster` manifest to increase the `size` value of the `DataDisk` volume and add any default-sized disks that you need to expand (such as the `ObsDisk` volume or `BackupRepoDisk` volume).

The following example manifest expands the `DataDisk` volume to `400Gi`, expands the `ObsDisk` volume from its `2Gi` default to `10Gi`, and configures the `BackupRepoDisk` volume at `600Gi` for a 200 GiB workload:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: DBCluster
         metadata:
           name: DB_CLUSTER_NAME
           namespace: NAMESPACE
         spec:
           databaseVersion: "15.7.1"
           primarySpec:
             adminUser:
               passwordRef:
                 name: db-pw-DB_CLUSTER_NAME
             resources:
               cpu: 4
               memory: 32Gi
               disks:
               - name: DataDisk
                 size: 400Gi
                 storageClass: STORAGE_CLASS_NAME
               - name: ObsDisk
                 size: 10Gi
                 storageClass: STORAGE_CLASS_NAME
               - name: BackupRepoDisk
                 size: 600Gi
                 storageClass: STORAGE_CLASS_NAME
         

Replace the following:

     * `DB_CLUSTER_NAME`: the name of your database cluster—for example, `my-db-cluster`.
     * `NAMESPACE`: the namespace of your database cluster.
     * `STORAGE_CLASS_NAME`: the name of the Kubernetes `StorageClass` resource used by your persistent volumes—for example, `standard-rwo`. If you omitted the `storageClass` field when you created the cluster, you can continue to omit it so that the operator uses your cluster's default `StorageClass`.
  4. Apply the updated `DBCluster` manifest:
         
         kubectl apply -f DB_CLUSTER_MANIFEST.yaml

Replace `DB_CLUSTER_MANIFEST` with the path to your `DBCluster` manifest file.

**Note:** If you also deployed [read pool instances](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/kubernetes-read-pool) that define their own `spec.resources.disks` section in a `DBInstance` manifest, update the `spec.resources.disks` section in your `DBInstance` manifest and re-apply it as well.
  5. Verify that the PVCs and `DBCluster` status reflect the expanded sizes:
         
         kubectl get pvc -n NAMESPACE

You can also inspect the `allocatedResources.disks` status field on the `DBCluster` resource:
         
         kubectl get dbcluster DB_CLUSTER_NAME -n NAMESPACE -o jsonpath='{.status.primary.allocatedResources.disks}{"\n"}'

Replace the following:

     * `NAMESPACE`: the namespace of your database cluster.
     * `DB_CLUSTER_NAME`: the name of your database cluster.



For more information about resizing compute and storage resources, see [Resize your Kubernetes-based database cluster](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/manage#resize-kubernetes).

## What's next

  * [Install AlloyDB Omni using the container orchestrator](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/deploy-kubernetes)
  * [Manage and monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/manage)
  * [Configure log rotation](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/configure-log-rotation)
  * [Back up and restore in Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/backup-kubernetes)
  * [Manage high availability in Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/kubernetes-ha)
  * [Create a read pool instance in Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/kubernetes-read-pool)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
