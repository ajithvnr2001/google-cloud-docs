---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/kubernetes-dr-backup-k8-gcs/
title: Clone a database cluster in Kubernetes using a Cloud Storage backup \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.13.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:52:55.870386+00:00
---

# Clone a database cluster in Kubernetes using a Cloud Storage backup  |  AlloyDB Omni for Kubernetes: 15.13.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/kubernetes-dr-backup-k8-gcs/

This page documents AlloyDB Omni version **15.13.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/overview)



Send feedback 

#  Clone a database cluster in Kubernetes using a Cloud Storage backup Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.13.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/kubernetes-dr-backup-k8-gcs)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/kubernetes-dr-backup-k8-gcs)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/kubernetes-dr-backup-k8-gcs)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/kubernetes-dr-backup-k8-gcs)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/kubernetes-dr-backup-k8-gcs)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/kubernetes-dr-backup-k8-gcs)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/kubernetes-dr-backup-k8-gcs)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/kubernetes-dr-backup-k8-gcs)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/kubernetes-dr-backup-k8-gcs)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/kubernetes-dr-backup-k8-gcs)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/kubernetes-dr-backup-k8-gcs)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/kubernetes-dr-backup-k8-gcs)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/kubernetes-dr-backup-k8-gcs)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/kubernetes-dr-backup-k8-gcs)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/kubernetes-dr-backup-k8-gcs)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/kubernetes-dr-backup-k8-gcs)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/kubernetes-dr-backup-k8-gcs)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/kubernetes-dr-backup-k8-gcs)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/kubernetes-dr-backup-k8-gcs)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/kubernetes-dr-backup-k8-gcs)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/kubernetes-dr-backup-k8-gcs)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/kubernetes-dr-backup-k8-gcs)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/kubernetes-dr-backup-k8-gcs)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/kubernetes-dr-backup-k8-gcs)

This page shows you how to clone a database cluster in Kubernetes using a Cloud Storage backup of an AlloyDB Omni database cluster. 

The following workflow explains the steps used to clone:

  1. Create and apply the `DBCluster` manifest file on the target database cluster with the `livenessProbe` parameter disabled.
  2. Create and configure the `pgbackrest.conf` file to access the Cloud Storage backup.
  3. Use `pgBackRest` commands to verify you can access source backups.
  4. Use `pgBackRest` commands to restore the backup to the target database cluster.



## Before you begin

  * Make sure you have access to the full path of the Cloud Storage bucket where your source database cluster backup is stored. This is the same path you used when you created the [`BackupPlan`](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/backup-kubernetes#remote) resource for your source database cluster.
  * Create a target AlloyDB Omni database cluster. For more information about installing AlloyDB Omni on Kubernetes, see [Create a database cluster](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/deploy-kubernetes#create).
  * Ensure you are logged in to the database as the `postgres` user.



## Create a database cluster in a target database cluster

Create a database cluster by temporarily disabling the `livenessProbe` parameter. After the restore finishes, reconfigure the `livenessProbe` parameter.

  1. Create the `DBCluster` resource manifest file:
         
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
                 size: DISK_SIZE
                 storageClass: standard
         

Replace the following:

     * `DB_CLUSTER_NAME`: the name of this database cluster—for example, `my-db-cluster`.

     * `ENCODED_PASSWORD`: the database login password for the default `postgres` user role, encoded as a base64 string—for example, `Q2hhbmdlTWUxMjM=` for `ChangeMe123`.

     * `CPU_COUNT`: the number of CPUs available to each database instance in this database cluster.

     * `MEMORY_SIZE`: the amount of memory per database instance of this database cluster. We recommend setting this to 8 gigabytes per CPU. For example, if you set `cpu` to `2` earlier in this manifest, then we recommend setting `memory` to `16Gi`.

     * `DISK_SIZE`: the disk size per database instance—for example, `10Gi`.

  2. Apply the manifest file:
         
         kubectl apply -f DBCLUSTER_FILENAME

Replace the following:

     * DBCLUSTER_FILENAME: the name of the `DBCluster` manifest file created in the previous step.



Use the `kubectl describe` command to verify that the database cluster resource is in the `READY` status.

## Configure the `pgBackRest` file

Configure the `pgBackRest` file to enable the target database cluster to access the Cloud Storage bucket where source backups reside.

  1. In your target database cluster, find the database cluster pod details:
         
         kubectl get pod -l "alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME, alloydbomni.internal.dbadmin.goog/task-type=database"

The response includes the name of the cluster database pod.

  2. Log into the pod:
         
         kubectl exec -ti DATABASE_POD_NAME  -- /bin/bash

Replace the following:

     * DATABASE_POD_NAME: the name of the database cluster pod from the previous step.
  3. Stop the pod before updating the `pgBackRest` configuration file:
         
         supervisorctl.par stop postgres

  4. Create a `pgBackRest` configuration file to access backups stored in Cloud Storage:
         
         cat << EOF > /backup/pgbackrest.conf
           [db]
           pg1-path=/mnt/disks/pgsql/data
           pg1-socket-path=/tmp
           pg1-user=pgbackrest
           [global]
           log-path=/obs/pgbackrest
           log-level-file=info
           repo1-type=gcs
           repo1-gcs-bucket=GCS_SOURCE_BACKUP_BUCKET_NAME
           repo1-path=GCS_SOURCE_BACKUP_BUCKET_PATH
           repo1-storage-ca-file=/scripts/ca-certificates.crt
           repo1-retention-full=9999999
           repo1-gcs-key-type=auto

Replace the following:

     * `GCS_SOURCE_BACKUP_BUCKET_NAME`: the name of the Cloud Storage bucket that you created when creating the [`BackupPlan`](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/backup-kubernetes#remote) resource manifest file for the source database cluster. This is not the full URL to the bucket; don't prefix the bucket name with `gs://`.
     * `GCS_SOURCE_BACKUP_BUCKET_PATH`: the path of the directory that the AlloyDB Omni operator writes backups into, within the Cloud Storage bucket for the source database cluster. The path must be absolute, beginning with `/`.

The `repo1-gcs-key-type` is set to `auto` to use the instance's service account. For more information about other options, see [Cloud Storage Repository Key Type Option](https://pgbackrest.org/configuration.html#section-repository/option-repo-gcs-key-type).




## Verify source backups in the target database cluster

Run `pgBackRest` commands to verify that the source database cluster backups are accessible on the target database cluster.
    
    
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

After the `postgres` process starts, you can connect to the primary instance and run queries to verify that the data is restored from the backup. For more information, see [Connect to AlloyDB Omni running on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/run-connect#kubernetes).

## Configure the database cluster

After you clone a database cluster, configure your database cluster specifications. Most importantly, don't forget to turn on the `livenessProbe` parameter with the following command:
    
    
        kubectl patch dbcluster DBCLUSTER_FILENAME --type merge -p '{"spec":{"primarySpec":{"availabilityOptions":{"livenessProbe":"Enabled"}}}}'

## What's next

  * [Clone a database cluster in Kubernetes using a local backup](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/kubernetes-dr-backup-k8-local)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
