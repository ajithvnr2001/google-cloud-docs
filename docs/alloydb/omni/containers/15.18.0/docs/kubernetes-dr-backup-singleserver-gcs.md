---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/kubernetes-dr-backup-singleserver-gcs/
title: Clone a database cluster in a single server using a Cloud Storage backup \u00a0|\u00a0 AlloyDB Omni using containers: 15.18.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:16:37.888789+00:00
---

# Clone a database cluster in a single server using a Cloud Storage backup  |  AlloyDB Omni using containers: 15.18.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/kubernetes-dr-backup-singleserver-gcs/

This page documents AlloyDB Omni version **15.18.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/overview)



Send feedback 

#  Clone a database cluster in a single server using a Cloud Storage backup Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.18.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/kubernetes-dr-backup-singleserver-gcs)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/kubernetes-dr-backup-singleserver-gcs)

This page show you how to manually clone a database cluster in a single server using a Cloud Storage backup. 

The following workflow explains the cloning steps:

  1. Configure the `pgbackrest.conf` file to access the Cloud Storage backup.
  2. Use `pgBackRest` commands to verify source backups can be accessed.
  3. Use `pgBackRest` commands to restore the backup to the target server.



## Before you begin

  * Access to the full path of the Cloud Storage bucket where your source database cluster backup resides. This is the same path you used when you created the `BackupPlan` resource for your source database cluster.
  * A single server target AlloyDB Omni database cluster is created. For more information about installing AlloyDB Omni on Kubernetes, see [Install AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/quickstart).
  * Ensure you are logged in to the database as the `postgres` user.



## Configure the `pgBackRest` file on the target server

Configure the `pgBackRest` file to enable the target database cluster to access the Cloud Storage bucket where source backups reside.

  1. In the target server, navigate to the `alloydb-data` directory.

  2. Create a `pgBackRest` configuration file to access backups stored in Cloud Storage:
         
         $ cat << EOF > /backup/pgbackrest.conf
           [db]
           pg1-path=/mnt/disks/pgsql/data-restored
           pg1-socket-path=/tmp
           pg1-user=pgbackrest
           [global]
           log-path=/obs/pgbackrest
           log-level-file=info
           repo1-type=gcs
           repo1-gcs-bucket=GCS_SOURCE_BACKUP_BUCKET_NAME
           repo1-path=GCS_SOURCE_BACKUP_BUCKET_PATH
           repo1-storage-ca-file=/etc/ssl/certs/ca-certificates.crt
           repo1-retention-full=9999999
           repo1-gcs-key-type=auto

Replace the following:

     * GCS_SOURCE_BACKUP_BUCKET_NAME: the name of the Cloud Storage `pgBackRest` bucket you created in the source database cluster. This is not the full URL to the bucket; don't prefix the bucket name with `gs://`.
     * GCS_SOURCE_BACKUP_BUCKET_PATH: the path of the directory that the AlloyDB Omni operator writes backups into, within the Cloud Storage bucket for the source database cluster. The path must be absolute, beginning with `/`.

The `repo1-gcs-key-type` is set to `auto` to use the instance's service account. For more information about other options, see [GCS Repository Key Type Option](https://pgbackrest.org/configuration.html#section-repository/option-repo-gcs-key-type).




## Verify source backups in target server

Sign in to the target server and run `pgBackRest` commands to verify that the source database cluster backups are accessible on the target server:

###  Docker 
    
    
    sudo docker exec CONTAINER_NAME pgbackrest --config-path=/mnt/disks/pgsql --stanza=db --repo=1 info

###  Podman 
    
    
    sudo podman exec CONTAINER_NAME pgbackrest --config-path=/mnt/disks/pgsql --stanza=db --repo=1 info

Replace `CONTAINER_NAME` with the name of a new AlloyDB Omni container—for example, `my-omni-1`.

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

## Restore the backup in the target server

After you identify the backup or a point in time you want to restore to, run `pgBackRest` commands in your target server. For more information about these commands, see [Restore Command](https://pgbackrest.org/command.html#command-restore).

The following are some sample `pgBackRest` restore commands:

  * Restore from a backup
        
        pgbackrest --config-path=/mnt/disks/pgsql --stanza=db --repo=1 restore --set=20240213-231400F --type=immediate --target-action=promote --delta --link-all --log-level-console=info

  * Restore from a point in time
        
        pgbackrest --config-path=/mnt/disks/pgsql --stanza=db --repo=1 restore --target="2024-01-22 11:27:22" --type=time --target-action=promote --delta --link-all --log-level-console=info




## Copy data to the target server

After the restore command completes successfully, you can copy the data from the `/mnt/disks/pgsql/data-restored` temporary directory to the current `/alloydb-data/data` directory.

  1. In the target server, stop the database service:



###  Docker 
    
    
    docker stop CONTAINER_NAME

###  Podman 
    
    
    podman stop CONTAINER_NAME

  1. Rename the current data directory to another name as a best practice:
         
         mv ~/alloydb-data/data  ~/alloydb-data/data-old

  2. Rename the `data-restored` temporary directory to the current data directory:
         
         mv ~/alloydb-data/data-restored ~/alloydb-data/data

  3. Update `pg1-path` value in the `postgresql.auto.conf` file to load the restored data:



    
    
        vim ~/alloydb-data/data/postgresql.auto.conf
        # Verify postgresql.auto.conf.
        # Do not edit this file manually!
        # It will be overwritten by the ALTER SYSTEM command.
        # Recovery settings generated by pgBackRest restore on 2024-03-13 20:47:11
        restore_command = 'pgbackrest --config-path=/mnt/disks/pgsql --pg1-path=/mnt/disks/pgsql/data --repo=1 --stanza=db archive-get %f "%p"'
        recovery_target = 'immediate'
        recovery_target_action = 'promote'
        recovery_target_timeline = 'current'

  1. In the target server, start the database service:

###  Docker 
         
         docker start CONTAINER_NAME

###  Podman 
         
         podman start CONTAINER_NAME




After the database service starts, you can connect to the primary instance and run queries to verify that the data is restored from the backup. For more information, see [Connect to AlloyDB Omni on a single server](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/run-connect#connect).

## What's next

  * [Clone a database cluster in a single server using a local backup](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/kubernetes-dr-backup-singleserver-local)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
