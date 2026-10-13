---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/monitor-cassandra-backups/
title: Monitoring backups \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:01.815034+00:00
---

# Monitoring backups  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/monitor-cassandra-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Monitoring backups Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.15 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.15 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monitor-cassandra-backups.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monitor-cassandra-backups.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/monitor-cassandra-backups.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/monitor-cassandra-backups.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/monitor-cassandra-backups.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/monitor-cassandra-backups.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/monitor-cassandra-backups.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/monitor-cassandra-backups.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/monitor-cassandra-backups.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/monitor-cassandra-backups.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/monitor-cassandra-backups.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/monitor-cassandra-backups.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/monitor-cassandra-backups.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/monitor-cassandra-backups.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/monitor-cassandra-backups.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/monitor-cassandra-backups.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/monitor-cassandra-backups.html)



This page describes how to monitor Cassandra backups. The approach for monitoring backups is the same for backups in Cloud Storage and backups in a remote server.

You can monitor the backups by viewing the details of the `apigee-cassandra-backup` cronjob, which is responsible for creating the backups. Use the `kubectl` command on your Kubernetes cluster to view the status of the cronjob.

The following examples show the usage of the `kubectl` command.

  * Check the status of the cron job: 
        
        kubectl get  cronjobs -n APIGEE_NAMESPACE
        
        NAME                      SCHEDULE     SUSPEND   ACTIVE   LAST SCHEDULE   AGE
        apigee-cassandra-backup   11 * * * *   False     0        9m27s           32m

  * Check the status of the backup job: 
        
        kubectl get jobs -n APIGEE_NAMESPACE |grep apigee-cassandra-backup
        
        apigee-cassandra-backup-1637176260                1/1           79s        9m3s
        
        kubectl get pods -n APIGEE_NAMESPACE | grep backup
        
        apigee-cassandra-backup-1637176260-vj5cg          0/1     Completed   0          7m49s

  * Check the backup logs: 
        
        kubectl logs  -n APIGEE_NAMESPACE $(kubectl get pods -n APIGEE_NAMESPACE |grep apigee-cassandra-backup |awk '{print $1}')
        

If the backup is successful, you will see an output similar to the following: 
        
        starting apigee-cassandra-default-0 in apigee
        snapshot pid 25 started for pod apigee-cassandra-default-0 in namespace apigee
        starting apigee-cassandra-default-1 in apigee
        snapshot pid 36 started for pod apigee-cassandra-default-1 in namespace apigee
        starting apigee-cassandra-default-2 in apigee
        snapshot pid 48 started for pod apigee-cassandra-default-2 in namespace apigee
         25 36 48
        waiting on process 25
        INFO: removing old cassandra snapshots
        INFO: removing old cassandra snapshots
        INFO: removing old cassandra snapshots
        Requested clearing snapshot(s) for [all keyspaces]
        Requested clearing snapshot(s) for [all keyspaces]
        Requested clearing snapshot(s) for [all keyspaces]
        
        .
        .
        .
        Operation completed over 1 objects.
        INFO: backup created tarball and transferred the file to gs://<bucket name>
        INFO: removing cassandra snapshot
        Requested clearing snapshot(s) for [all keyspaces]
        INFO: completed upload for 20211117191141
        finished backup




## Viewing backup logs

The backup job: 

  * Creates a `schema.cql` file.
  * Uploads it to your storage bucket.
  * Echoes the node to backup the data and uploads it at the same time.
  * Waits until all the data is uploaded.



To view the backup logs of a Kubernetes pod, run the `kubectl logs -f <pod_name> -n <namespace>` command: 
    
    
    kubectl logs -f POD_NAME -n APIGEE_NAMESPACE
    

For example: 
    
    
    kubectl logs -f apigee-cassandra-backup-1.6451.680-pff6s -n apigee
    

The output is similar to the following: 
    
    
    myusername-macbookpro:cassandra-backup-utility myusername$ kubectl logs -f apigee-cassandra-backup-1.64577680-f9sc4
    starting apigee-cassandra-default-0 in default
    starting apigee-cassandra-default-1 in default
    starting apigee-cassandra-default-2 in default
    35 46 57
    waiting on process  35
    Activated service account credentials for: [apigee-cassandra-backup-svc@gce-myusername.iam.gserviceaccount.com]
    Activated service account credentials for: [apigee-cassandra-backup-svc@gce-myusername.iam.gserviceaccount.com]
    Activated service account credentials for: [apigee-cassandra-backup-svc@gce-myusername.iam.gserviceaccount.com]
    Requested creating snapshot(s) for [all keyspaces] with snapshot name [20190406190808] and options {skipFlush=false}
    Snapshot directory: 20190406190808
    INFO: backup created cassandra snapshot 20190406190808
    tar: Removing leading `/' from member names
    /apigee/data/cassandra/data/ks1/mytest3-37bc2df0587811e98e8d875b0ed64754/snapshots/
    /apigee/data/cassandra/data/ks1/mytest3-37bc2df0587811e98e8d875b0ed64754/snapshots/20190406190808/
    /apigee/data/cassandra/data/ks1/mytest3-37bc2df0587811e98e8d875b0ed64754/snapshots/20190406190808/mc-1-big-Data.db
    Requested creating snapshot(s) for [all keyspaces] with snapshot name [20190406190808] and options {skipFlush=false}
    Requested creating snapshot(s) for [all keyspaces] with snapshot name [20190406190808] and options {skipFlush=false}
    Snapshot directory: 20190406190808
    INFO: backup created cassandra snapshot 20190406190808
    tar: Removing leading `/' from member names
    /apigee/data/cassandra/data/system/hints-2666e20573ef38b390fefecf96e8f0c7/snapshots/
    /apigee/data/cassandra/data/system/hints-2666e20573ef38b390fefecf96e8f0c7/snapshots/20190406190808/
    /apigee/data/cassandra/data/system/hints-2666e20573ef38b390fefecf96e8f0c7/snapshots/20190406190808/manifest.json
    /apigee/data/cassandra/data/system/prepared_statements-18a9c2576a0c3841ba718cd529849fef/snapshots/
    /apigee/data/cassandra/data/system/prepared_statements-18a9c2576a0c3841ba718cd529849fef/snapshots/20190406190808/
    /apigee/data/cassandra/data/system/prepared_statements-18a9c2576a0c3841ba718cd529849fef/snapshots/20190406190808/manifest.json
    /apigee/data/cassandra/data/system/range_xfers-55d764384e553f8b9f6e676d4af3976d/snapshots/
    /apigee/data/cassandra/data/system/range_xfers-55d764384e553f8b9f6e676d4af3976d/snapshots/20190406190808/
    /apigee/data/cassandra/data/system/range_xfers-55d764384e553f8b9f6e676d4af3976d/snapshots/20190406190808/manifest.json
    /apigee/data/cassandra/data/system/peer_events-59dfeaea8db2334191ef109974d81484/snapshots/
    /apigee/data/cassandra/data/system/peer_events-59dfeaea8db2334191ef109974d81484/snapshots/20190406190808/
    /apigee/data/cassandra/data/system/peer_events-59dfeaea8db2334191ef109974d81484/snapshots/20190406190808/manifest.json
    /apigee/data/cassandra/data/system/built_views-4b3c50a9ea873d7691016dbc9c38494a/snapshots/
    /apigee/data/cassandra/data/system/built_views-4b3c50a9ea873d7691016dbc9c38494a/snapshots/20190406190808/
    /apigee/data/cassandra/data/system/built_views-4b3c50a9ea873d7691016dbc9c38494a/snapshots/20190406190808/manifest.json
    ……
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-3-big-Filter.db
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-2-big-CompressionInfo.db
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-2-big-Index.db
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-3-big-Statistics.db
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-2-big-Data.db
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-1-big-Index.db
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-1-big-Statistics.db
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-2-big-TOC.txt
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-2-big-Statistics.db
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-1-big-Summary.db
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-1-big-Filter.db
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-2-big-Summary.db
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-3-big-Index.db
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/manifest.json
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-2-big-Filter.db
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-2-big-Digest.crc32
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-3-big-Summary.db
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-3-big-Data.db
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-1-big-TOC.txt
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/schema.cql
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-3-big-CompressionInfo.db
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-1-big-Digest.crc32
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-3-big-TOC.txt
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-1-big-Data.db
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-3-big-Digest.crc32
    /apigee/data/cassandra/data/ks2/user-d6d39d70586311e98e8d875b0ed64754/snapshots/20190406190808/mc-1-big-CompressionInfo.db
    ……
    /tmp/tokens.txt
    / [1 files][    0.0 B/    0.0 B]
    Operation completed over 1 objects.
    / [1 files][    0.0 B/    0.0 B]
    Operation completed over 1 objects.
    INFO: backup created tarball and transferred the file to gs://gce-myusername-apigee-cassandra-backup/apigeecluster/dc-1
    INFO: removing cassandra snapshot
    INFO: backup created tarball and transferred the file to gs://gce-myusername-apigee-cassandra-backup/apigeecluster/dc-1
    INFO: removing cassandra snapshot
    Requested clearing snapshot(s) for [all keyspaces]
    INFO: Backup 20190406190808 completed
    waiting on process  46
    Requested clearing snapshot(s) for [all keyspaces]
    INFO: Backup 20190406190808 completed
    Requested clearing snapshot(s) for [all keyspaces]
    waiting on process  57
    INFO: Backup 20190406190808 completed
    waiting result
    to get schema from 10.32.0.28
    INFO: /tmp/schema.cql has been generated
    Activated service account credentials for: [apigee-cassandra-backup-svc@gce-myusername.iam.gserviceaccount.com]
    tar: removing leading '/' from member names
    tmp/schema.cql
    Copying from <TDIN>...
    / [1 files][    0.0 B/    0.0 B]
    Operation completed over 1 objects.
    INFO: backup created tarball and transferred the file to gs://gce-myusername-apigee-cassandra-backup/apigeecluster/dc-1
    finished uploading schema.cql

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
