---
url: https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/kubernetes-dr-backup-k8-local/
title: Clone a database cluster in Kubernetes using a local backup \u00a0|\u00a0 AlloyDB Omni for containers: 16.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:26:57.257828+00:00
---

# Clone a database cluster in Kubernetes using a local backup  |  AlloyDB Omni for containers: 16.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/kubernetes-dr-backup-k8-local/

This page documents AlloyDB Omni version **16.3.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/overview)



Send feedback 

#  Clone a database cluster in Kubernetes using a local backup Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.3.0keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/kubernetes-dr-backup-k8-local)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/kubernetes-dr-backup-k8-local)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/kubernetes-dr-backup-k8-local)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/kubernetes-dr-backup-k8-local)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/kubernetes-dr-backup-k8-local)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/kubernetes-dr-backup-k8-local)

This document describes how to clone a database cluster in Kubernetes using local backup of an AlloyDB Omni database cluster. 

This document makes the following assumptions:

  * Your source and target database clusters are created on Google Kubernetes Engine, and the backup disks are Compute Engine persistent disks. 
  * The Compute Engine persistent disks that are used as a backup disk in the database aren't used by other database clusters.

**Note:** If you use other environments, then follow the instructions in the relevant documentation to replicate these steps in your environment.

When you clone a database cluster, you follow these steps:

  1. Identify the backup disk information, such as the persistent volume name and Compute Engine persistent disk handler for the source database cluster backup disk. Make sure that you enabled the backup feature for the source database cluster, and that you have at least one successful backup. If these conditions aren't met, follow the instructions in [Enable and schedule backups](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/backup-kubernetes#enable).
  2. Create a `PersistentVolume` resource to use an existing backup disk on the target database cluster to access the backup disk of the source database cluster.
  3. Create and apply the [`DBCluster`](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/deploy-kubernetes#create) resource manifest file on the target database cluster with the `livenessProbe` parameter disabled and backup disk information added.
  4. Use `pgBackRest` commands to verify source backups can be accessed.
  5. Use `pgBackRest` commands to restore the backup to the target database cluster.



## Before you begin

  * Make sure you have access to the backup disk where your source database cluster backup is stored.
  * The source database cluster backup disk must be able to mount to the target database cluster. For more information, see [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/). If the underlying storage backend doesn't support ReadOnlyMany (ROX) access, make sure that the backup disk isn't being used by any pods in the source cluster.
  * Since the source backup disk is mounted to the target database cluster, the `pgBackRest.conf` file is reused as-is.
  * Ensure you are logged in to the database as the `postgres` user.



## Get source backup disk information

As part of the restore process, determine the backup disk Persistent Volume Claim (PVC) name for your source database cluster. PVCs are used within Kubernetes to manage persistent storage for applications.

The following sample commands help locate the underlying PV name and the Compute Engine persistent disk handler. In the example, all the backup disks are Compute Engine persistent disks, which can be accessed across Compute Engine VMs using the disk handler identifier.

  1. Connect to your target database cluster to find the PVC name:
         
         kubectl get pvc -n DB_CLUSTER_NAMESPACE | grep DB_CLUSTER_NAME | grep backuprepodisk

Replace the following:

     * `DB_CLUSTER_NAMESPACE`: the Kubernetes namespace for this backup plan. It must match the namespace of the database cluster.

     * `DB_CLUSTER_NAME`: the name of this database cluster—for example, `my-db-cluster`.

The following is the sample response.
    
    backuprepodisk-my-db-cluster-br-0   Bound
        pvc-36d8f05d-ef1a-4750-ac01-9bb330c15b3a   10Gi       RWO            standard-rwo   5d21h

  2. Use the backup disk PVC name from the previous step-—for example, `backuprepodisk-my-db-cluster-br-0`, to find the underlying PV name and Compute Engine persistent disk handler:
         
         kubectl get pvc/PVC_NAME -n DB_CLUSTER_NAMESPACE -o jsonpath={.spec.volumeName}

Replace the following:

     * `PVC_NAME`: the PVC name of the backup disk from response in the previous step—for example `backuprepodisk-my-db-cluster-br-0`.
  3. Export the configurations based on the PV name as variables to be used in the subsequent sections:
         
         export BACKUP_DISK_SIZE=$(kubectl get pv/PV_NAME -o jsonpath="{.spec.capacity.storage}")
           export FS_TYPE=$(kubectl get pv/PV_NAME -o jsonpath="{.spec.csi.fsType}")
           export VOLUME_HANDLER=$(kubectl get pv/PV_NAME -o jsonpath="{.spec.csi.volumeHandle}")
           export STORAGE_CLASS=$(kubectl get pv/PV_NAME -o jsonpath="{.spec.storageClassName}")

Replace the following:

     * `PV_NAME`: the PV name of the backup disk from response in the previous step. For example, "backupDiskVolume".



## Create a persistent volume resource

Using the disk handler name, create a `PersistentVolume` resource.

  1. In the target Kubernetes cluster, create the `PersistentVolume` manifest file:
         
         apiVersion: v1
             kind: PersistentVolume
             metadata:
               name: PV_NAME
             spec:
               storageClassName: "${STORAGE_CLASS}"
               capacity:
                 storage: "${BACKUP_DISK_SIZE}"
               accessModes:
                 - ReadWriteOnce
               csi:
                 driver: pd.csi.storage.gke.io
                 volumeHandle: "${VOLUME_HANDLER}"
                 fsType: "${FS_TYPE}"
         

Replace the following:

     * PV_NAME: the name of the `PersistentVolume` resource that will be created.
  2. Apply the manifest file:
         
         kubectl apply -f PV_FILENAME

Replace the following:

     * PV_FILENAME: the name of the `PersistentVolume` manifest file created in the previous step.



## Create a target database cluster

Create a database cluster by temporarily disabling the `livenessProbe` parameter. After the restore finishes, reconfigure the `livenessProbe` parameter.

  1. Create the `DBCluster` manifest file:
         
         apiVersion: v1
           kind: Secret
           metadata:
             name: db-pw-DB_CLUSTER_NAME
           type: Opaque
           data:
             DB_CLUSTER_NAME: "ENCODED_PASSWORD"
           ---
           apiVersion: alloydbomni.dbadmin.goog/v1
           kind: DBCluster
           metadata:
             name: DB_CLUSTER_NAME
           spec:
             databaseVersion: "16.3.0"
             primarySpec:
               availabilityOptions:
                 livenessProbe: "Disabled"
               adminUser:
                 passwordRef:
                   name: db-pw-DB_CLUSTER_NAME
               resources:
                 cpu: CPU_COUNT
                 memory: MEMORY_SIZE
                 disks:
                 - name: DataDisk
                   size: DATA_DISK_SIZE
                 - name: BackupDisk
                   size: ${BACKUP_DISK_SIZE}
                   storageClass: ${STORAGE_CLASS}
                   volumeName: PV_NAME
         

Replace the following:

     * `DB_CLUSTER_NAME`: the name of this database cluster—for example, `my-db-cluster`.

     * `ENCODED_PASSWORD`: the database login password for the default `postgres` user role, encoded as a base64 string—for example, `Q2hhbmdlTWUxMjM=` for `ChangeMe123`.

     * `CPU_COUNT`: the number of CPUs available to each database instance in this database cluster.

     * `MEMORY_SIZE`: the amount of memory per database instance of this database cluster. We recommend that you set this to 8 gigabytes per CPU. For example, if you set CPU_COUNT to `2`, then we recommend that you set `memory` to `16Gi`.

     * `DATA_DISK_SIZE`: the disk size per database instance, for example, `10Gi`.

  2. Apply the manifest file:
         
         kubectl apply -f DBCLUSTER_FILENAME

Replace the following:

     * DBCLUSTER_FILENAME: the name of the `DBCluster` manifest file created in the previous step.



Use the `kubectl describe` command to verify that the database cluster resource is in the `READY` status.

## Verify source backups in target database cluster

Run `pgBackRest` commands to verify that the source database cluster backups are accessible on the target database cluster.

  1. In your target database cluster, find the database cluster pod details:
         
         kubectl get pod -l "alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME, alloydbomni.internal.dbadmin.goog/task-type=database"

The response includes the name of the cluster database pod.

  2. Log into the database pod:
         
         kubectl exec -ti DATABASE_POD_NAME  -- /bin/bash

Replace the following:

     * DATABASE_POD_NAME : the name of the database cluster pod from the previous step.
  3. Stop the pod before updating the `pgBackRest` configuration file:
         
         supervisorctl.par stop postgres

  4. Update the `pgBackRest` configuration file:
         
         cp /backup/pgbackrest.conf /backup/pgbackrest.conf.bak
           rm /backup/pgbackrest.conf
           cat << EOF > /backup/pgbackrest.conf
           [db]
           pg1-path=/mnt/disks/pgsql/data
           pg1-socket-path=/tmp
           pg1-user=pgbackrest
           [global]
           log-path=/backup/logs
           log-level-file=info
           EOF

  5. Verify the source backups in the database cluster pod:
         
         pgbackrest --config-path=/backup --stanza=db --repo=1 info

The following is a sample response:
         
         stanza: db
               status: ok
               cipher: none
               db (current)
                   wal archive min/max (15): 000000010000000000000002/00000001000000000000000D
                   full backup: 20240213-231400F
                       timestamp start/stop: 2024-02-13 23:14:00+00 / 2024-02-13 23:17:14+00
                       wal start/stop: 000000010000000000000003 / 000000010000000000000003
                       database size: 38.7MB, database backup size: 38.7MB
                       repo1: backup set size: 4.6MB, backup size: 4.6MB
                   incr backup: 20240213-231400F_20240214-000001I
                       timestamp start/stop: 2024-02-14 00:00:01+00 / 2024-02-14 00:00:05+00
                       wal start/stop: 00000001000000000000000D / 00000001000000000000000D
                       database size: 38.7MB, database backup size: 488.3KB
                       repo1: backup set size: 4.6MB, backup size: 84.2KB
                       backup reference list: 20240213-231400F
         




The timestamps in the response are used either to restore the full backup or to restore from a point in time from the recovery window.

## Restore the backup in the target database cluster

After you identify the backup or a point in time you want to restore to, run `pgBackRest` commands in your target database cluster. For more information about these commands, see [Restore Command](https://pgbackrest.org/command.html#command-restore).

The following are some sample `pgBackRest` restore commands:

  * Restore from a backup
        
        pgbackrest --config-path=/backup --stanza=db --repo=1 restore --set=20240213-231400F --type=immediate --target-action=promote --delta --link-all --log-level-console=info

  * Restore from a point in time
        
        pgbackrest --config-path=/backup --stanza=db --repo=1 restore --target="2024-01-22 11:27:22" --type=time --target-action=promote --delta --link-all --log-level-console=info




## Restart the pod

After the restore command completes successfully, you can start the `postgres` process.
    
    
    supervisorctl.par start postgres

After the `postgres` process starts, you can connect to the primary instance and run queries to verify that the data is restored from the backup. For more information, see [Connect to AlloyDB Omni running on Kubernetes](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/run-connect#kubernetes).

## Configure the database cluster

After you clone a database cluster, configure your database cluster specifications. Make sure to turn on the `livenessProbe` parameter using the following command:
    
    
        kubectl patch dbcluster DBCLUSTER_FILENAME --type merge -p '{"spec":{"primarySpec":{"availabilityOptions":{"livenessProbe":"Enabled"}}}}'

## What's next

  * [Clone a database cluster in Kubernetes using a Cloud Storage backup](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/kubernetes-dr-backup-k8-gcs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
