---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/samples/
title: AlloyDB Omni using the RPM orchestrator samples \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:14:29.427996+00:00
---

# AlloyDB Omni using the RPM orchestrator samples  |  AlloyDB Omni using the RPM orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/samples/

This page documents AlloyDB Omni version **18.1.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/overview)
  * [ Samples ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/samples)



Send feedback 

#  AlloyDB Omni using the RPM orchestrator samples Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

This page provides various YAML configuration examples to deploy and manage AlloyDB Omni using the RPM orchestrator.

### DBCluster configuration

### Minimal DBCluster

A basic configuration to get a standalone DBCluster. 
    
    
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
    
    
    DBCluster:
      metadata:
        name: alloydb-prod
      spec:
        databaseVersion: 18.1.0
        mode: ""
        availability:
          numberOfStandbys: 2
          enableAutoFailover: true
          enableAutoHeal: true
          autoFailoverTriggerThreshold: 2
          autoHealTriggerThreshold: 2
          healthcheckPeriodSeconds: 10
        primarySpec:
          adminUser:
            passwordRef:
              name: db-pw-alloydb-prod
          parameters:
            max_connections: "100"
            max_wal_size: "2GB"
            max_worker_processes: "32"
            log_connections: "on"
            log_disconnections: "on"
            log_hostname: "on"
            log_statement: "none"
            huge_pages: "off"
            tcp_keepalives_idle: "10"
            tcp_keepalives_interval: "10"
            tcp_keepalives_count: "10"
          resources:
            cpu: 16
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

### Secret configuration

Example with password: 
    
    
    Secret:
      metadata:
        name: db-pw-sample-st-1
      spec:
        type: Opaque
        data:
          sample-st-1: cG9zdGdyZXM=

Example with certs: 
    
    
    Secret:
      metadata:
        name: dbs-alloydbomni-cluster
      spec:
        type: Opaque
        data:
          ca.crt: <base64_ca_certificate>
          tls.crt: <base64_tls_certificate>
          tls.key: <base64_tls_private_key>

### PgBouncer configuration
    
    
    PgBouncer:
      metadata:
        name: pgbouncer-sample
      spec:
        accessMode: "rw"
        allowSuperUserAccess: true
        dbClusterRef: dbcluster-sample
        port: 6432

### BackupPlan configuration

The following sample shows how to configure a BackupPlan that stores backups in a Cloud Storage bucket. 
    
    
    BackupPlan:
      metadata:
        name: backupplan-sample-dbc
      spec:
        dbclusterRef: sample-dbc
        backupLocation:
          type: GCS
          gcsOptions:
            bucket: sample-backup-bucket
            key: /backups

### Backup configuration

Example of a Backup
    
    
    Backup:
      metadata:
        name: backup-sample
      spec:
        backupPlanRef: backupplan-sample-dbc
        dbclusterRef: sample-dbc

### Switchover configuration

Example of a Switchover configuration
    
    
    Switchover:
      metadata:
        name: switchover-alloydb-prod-12345
      spec:
        dbclusterRef: "alloydb-prod"

### Switchover configuration

Example of a Failover configuration
    
    
    Failover:
      metadata:
        name: failover-alloydb-prod-abcde
      spec:
        dbclusterRef: "alloydb-prod"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
