---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/samples/
title: AlloyDB Omni using the RPM orchestrator samples \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:38:51.887208+00:00
---

# AlloyDB Omni using the RPM orchestrator samples  |  AlloyDB Omni using the RPM orchestrator: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/samples/

This page documents AlloyDB Omni version **18.4.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/overview)
  * [ Samples ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/samples)



Send feedback 

#  AlloyDB Omni using the RPM orchestrator samples Stay organized with collections  Save and categorize content based on your preferences. 

This page provides various YAML configuration examples to deploy and manage AlloyDB Omni using the RPM orchestrator.

### DBCluster configuration

### Minimal DBCluster

A basic configuration to get a standalone DBCluster.

#### View Minimal DBCluster YAML configuration
    
    
    DBCluster:
      metadata:
        name: alloydb-prod
      spec:
        databaseVersion: 18.1.0
        primarySpec:
          adminUser:
            passwordRef:
              name: db-pw-alloydb-prod
          resources:
            disks:
            - name: DataDisk
              path: /mnt/disks/pgsql

### Full DBCluster

A comprehensive DBCluster configuration showing all options.

#### View Full DBCluster YAML configuration
    
    
    DBCluster:
      metadata:
        name: alloydb-prod
      spec:
        databaseVersion: 18.1.0
        loadBalancerPort: 5433
        readOnlyPort: 5434
        mode: ""
        availability:
          numberOfStandbys: 2
          enableAutoFailover: true
          enableAutoHeal: true
          enableStandbyAsReadReplica: true
          autoFailoverTriggerThreshold: 2
          autoHealTriggerThreshold: 2
          healthcheckPeriodSeconds: 10
        primarySpec:
          adminUser:
            passwordRef:
              name: db-pw-alloydb-prod
          port: 5432
          monitorPort: 9187
          parameters:
            max_connections: "100"
            max_wal_size: "2GB"
            max_worker_processes: "32"
            log_connections: "on"
            log_disconnections: "on"
            log_hostname: "on"
            log_statement: "none"
          resources:
            cpu: 16
            memory: 32Gi
            limits:
              memory: 64Gi
            disks:
            - name: DataDisk
              path: /mnt/disks/pgsql
            - name: ObsDisk
              path: /obs
          dbLoadBalancerOptions:
            onprem:
              loadBalancerIP: 10.1.0.95
              loadBalancerType: "internal"
              loadBalancerInterface: "eth0"
          features:
            columnarSpillToDisk:
              cacheSize: "50Gi"
              localVolume:
                path: "/mnt/disks/ssd1"
            ultraFastCache:
              cacheSize: "100Gi"
              localVolume:
                path: "/mnt/disks/ssd2"
            googleMLExtension:
              enabled: true
              config:
                vertexAIKeyRef: "vertex-ai-key"
                vertexAIRegion: "us-central1"

### Secret configuration

Example with password:

#### View Secret (password) YAML configuration
    
    
    Secret:
      metadata:
        name: db-pw-sample-st-1
      spec:
        type: Opaque
        data:
          sample-st-1: cG9zdGdyZXM=

Example with certs:

#### View Secret (certs) YAML configuration
    
    
    Secret:
      metadata:
        name: dbs-alloydbomni-cluster
      spec:
        type: Opaque
        data:
          ca.crt: <base64_ca_certificate>
          tls.crt: <base64_tls_certificate>
          tls.key: <base64_tls_private_key>

Example for Gemini Enterprise Agent Platform Key:

#### View Secret (Vertex AI) YAML configuration
    
    
    Secret:
      metadata:
        name: vertex-ai-key
      spec:
        type: Opaque
        data:
          private-key.json: <base64_encoded_private_key>

### PgBouncer configuration

#### View PgBouncer YAML configuration
    
    
    PgBouncer:
      metadata:
        name: sample-pgbouncer
      spec:
        accessMode: "rw"
        allowSuperUserAccess: true
        dbClusterRef: dbcluster-sample
        port: 6432

### Scheduled Backup Plan

Schedule full and incremental backups.

#### View Scheduled Backup Plan YAML configuration
    
    
    BackupPlan:
      metadata:
        name: sample-backupplan
      spec:
        dbclusterRef: sample-dbc
        backupRetainDays: 14
        paused: false
        backupSchedules:
          # Full backup at 00:00 on every Sunday.
          full: "0 0 * * 0"
          # Incremental backup at 21:00 every day.
          incremental: "0 21 * * *"
        backupLocation:
          type: GCS
          gcsOptions:
            bucket: sample-backup-bucket
            key: /backups
            secretRef:
              name: gcs-access-secret

### Backup to Cloud Storage

Store backups inside a Cloud Storage bucket.

#### View Backup to Cloud Storage YAML configuration
    
    
    BackupPlan:
      metadata:
        name: sample-backupplan-gcs
      spec:
        dbclusterRef: sample-dbc
        backupRetainDays: 14
        paused: false
        backupSchedules:
          # Full backup at 00:00 every Sunday.
          full: "0 0 * * 0"
          # Incremental backup at every day at 21:00.
          incremental: "0 21 * * *"
        backupLocation:
          type: GCS
          gcsOptions:
            bucket: sample-backup-bucket
            key: /backups
            secretRef:
              name: gcs-access-secret

### Backup to Amazon S3

Store backups inside an Amazon S3-compatible bucket.

#### View Backup to Amazon S3 YAML configuration
    
    
    BackupPlan:
      metadata:
        name: sample-backupplan-s3
      spec:
        dbclusterRef: sample-dbc
        backupRetainDays: 14
        paused: false
        backupSchedules:
          # Full backup at 00:00 on every Sunday.
          full: "0 0 * * 0"
          # Incremental backup at 21:00 every day.
          incremental: "0 21 * * *"
        backupLocation:
          type: S3
          s3Options:
            bucket: sample-backup-bucket-s3
            key: /backups
            region: "us-east-1"
            endpoint: "https://s3.storage.com"
            secretRef:
              name: s3-access-secret

### On-Demand Manual Backup

Create a single manual backup.

#### View On-Demand Manual Backup YAML configuration
    
    
    Backup:
      metadata:
        name: sample-backup
      spec:
        dbclusterRef: sample-dbc
        backupPlanRef: sample-backupplan
        manual: true
        physicalBackupSpec:
          backupType: full

### Restore from Backup

Recover or create a cluster from a stored backup.

#### View Restore from Backup YAML configuration
    
    
    Restore:
      metadata:
        name: sample-restore
      spec:
        sourceDBCluster: sample-dbc
        backup: sample-backup

### Restore to a Point-in-Time

Restore a cluster to a specific timestamp in the past.

#### View Restore to a Point-in-Time YAML configuration
    
    
    Restore:
      metadata:
        name: sample-restore-pitr
      spec:
        sourceDBCluster: sample-dbc
        pointInTime: "2026-08-12T00:00:00Z"

### Switchover configuration

Example of a Switchover configuration

#### View Switchover YAML configuration
    
    
    Switchover:
      metadata:
        name: switchover-alloydb-prod-12345
      spec:
        dbclusterRef: "alloydb-prod"

### Failover configuration

Example of a Failover configuration

#### View Failover YAML configuration
    
    
    Failover:
      metadata:
        name: failover-alloydb-prod-abcde
      spec:
        dbclusterRef: "alloydb-prod"

### DBInstance configuration

Example of a DBInstance (ReadPool) configuration

#### View DBInstance (ReadPool) YAML configuration
    
    
    DBInstance:
      metadata:
        name: sample-readpool
      spec:
        instanceType: ReadPool
        dbcParent:
          name: alloydb-prod
        nodeCount: 2

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
