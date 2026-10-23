---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/samples/
title: AlloyDB Omni on Kubernetes Configuration Samples \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:52:19.938303+00:00
---

# AlloyDB Omni on Kubernetes Configuration Samples  |  AlloyDB Omni using the container orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/samples/

This page documents AlloyDB Omni version **18.1.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)
  * [ Samples ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/samples)



Send feedback 

#  AlloyDB Omni on Kubernetes Configuration Samples Stay organized with collections  Save and categorize content based on your preferences. 

This page provides YAML configuration examples for deploying and managing AlloyDB Omni on Kubernetes.

## DBCluster Core & OS Configurations

Explore base cluster configurations and custom operating system settings.

### Minimal DBCluster

A basic configuration to deploy an AlloyDB Omni DBCluster.

#### View Minimal DBCluster YAML configuration
    
    
    # This is a minimal DBCluster spec. See v1_dbcluster_full.yaml for more configurations.
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-pw-dbcluster-sample
    type: Opaque
    data:
      dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: dbcluster-sample
    spec:
      databaseVersion: "18.1.0"
      primarySpec:
        adminUser:
          passwordRef:
            name: db-pw-dbcluster-sample
        resources:
          memory: 5Gi
          cpu: 1
          disks:
          - name: DataDisk
            size: 10Gi

### Full DBCluster

A comprehensive setup that shows the available settings.

#### View Full DBCluster YAML configuration
    
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-pw-dbcluster-sample
    type: Opaque
    data:
      dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: dbcluster-sample
    spec:
      allowExternalIncomingTraffic: true
      availability:
        healthcheckPeriodSeconds: 30 # default is 30secs, new feature in 1.2.0. minimum value is 1 and the maximum value is 86400
        autoFailoverTriggerThreshold: 3 # after which failover is triggered
        autoHealTriggerThreshold: 3
        enableAutoFailover: true
        enableAutoHeal: true
        enableStandbyAsReadReplica: true
        numberOfStandbys: 1
      controlPlaneAgentsVersion: 1.6.0
      databaseVersion: "18.1.0"
      databaseImageOSType: UBI9
      isDeleted: false
      mode: ""
      primarySpec:
        adminUser:
          passwordRef:
            name: db-pw-dbcluster-sample
        allowExternalIncomingTrafficToInstance: false
        auditLogTarget: {}
        dbLoadBalancerOptions:
          annotations:
            networking.gke.io/load-balancer-type: "internal"
            lb.company.com/enabled: "true"
          gcp: {}
        features:
          columnarSpillToDisk:
            cacheSize: 50Gi
          ultraFastCache:
            cacheSize: 100Gi
            # either generic volume or local volume
            genericVolume:
              storageClass: "local-storage"
            # localVolume:
            #   path: "/mnt/disks/raid/0"
            #   nodeAffinity:
            #     required:
            #       nodeSelectorTerms:
            #         - matchExpressions:
            #           - key: "cloud.google.com/gke-local-nvme-ssd"
            #           operator: "In"
            #           values:
            #           - "true"
          googleMLExtension:
            config:
              vertexAIKeyRef: vertex-ai-key-alloydb # secret used to enable AlloyDB Omni to access AlloyDB AI features
              vertexAIRegion: us-central1 # default
        resources:
          cpu: "12"
          disks:
          - name: DataDisk
            size: 1000Gi
            storageClass: px-ceph
          - name: LogDisk
            size: 10Gi
            storageClass: px-ceph
          - name: ObsDisk
            size: 4Gi
            storageClass: px-ceph
          - name: BackupDisk
            size: 10Gi
            storageClass: px-ceph
          memory: 100Gi
        walArchiveSetting:
          location: wal/log  # enable WAL archiving and archive logs to /archive/wal/log
        sidecarRef:
          name: cv-sidecar-config # provide a sidecar config that is referenced here
        parameters:
          google_columnar_engine.enabled: "on"
          google_columnar_engine.memory_size_in_mb: "256"
          google_storage.parallel_log_replay_enabled: 'off'
          google_pg_auth.enable_auth: 'false'
          shared_preload_libraries: "pg_cron,pg_bigm3"
          archive_mode: 'on'
          archive_timeout: '300'
          work_mem: '4MB'
    # operator default values
    # shared_preload_libraries='g_stats,google_columnar_engine,google_db_advisor,google_job_scheduler,pg_stat_statements,pglogical,pgaudit'
          log_rotation_age: "2" # rotate every two minutes. Set to "0" to disable age-based rotation. If unset, no age-based rotation
          log_rotation_size: "400000" # rotate every 400,000kb. set to "0" to disable size-based rotation. If unset, rotate every 200,000kb
        schedulingconfig:
          tolerations:
            - effect: NoSchedule
              key: alloydb-node-type
              operator: Exists
          nodeaffinity:
            # requiredDuringSchedulingIgnoredDuringExecution: strong condition, not being able to meet this would stop pods being scheduled
            preferredDuringSchedulingIgnoredDuringExecution:
              nodeSelectorTerms:
              - matchExpressions:
                - key: alloydb-node-type
                  operator: In
                  values:
                  - database
          podAffinity:
            preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 1
              podAffinityTerm:
                labelSelector:
                  matchExpressions:
                  - key: app
                    operator: In
                    values:
                    - store
                topologyKey: "kubernetes.io/hostname"
          podAntiAffinity:
            preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 1
              podAffinityTerm:
                labelSelector:
                  matchExpressions:
                  - key: security
                    operator: In
                    values:
                    - S1
                topologyKey: "topology.kubernetes.io/zone"
        services:
          Logging: true
          Monitoring: true
    ---
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: "example-local-pv"
    spec:
      capacity:
        storage: 375Gi
      accessModes:
      - "ReadWriteOnce"
      persistentVolumeReclaimPolicy: "Retain"
      storageClassName: "local-storage"
      local:
        path: "/mnt/disks/raid/0"
      nodeAffinity:
        required:
          nodeSelectorTerms:
          - matchExpressions:
          # following example key applies to an operator that is deployed on
          # Google Cloud and uses the local ssd option
            - key: "cloud.google.com/gke-local-nvme-ssd"
              operator: "In"
              values:
              - "true"
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBInstance
    metadata:
      name: dbcluster-sample-rp-1
    spec:
      instanceType: ReadPool
      dbcParent:
        name: dbcluster-sample
      nodeCount: 2
      resources:
        memory: 6Gi
        cpu: 2
        disks:
        - name: DataDisk
          size: 15Gi
      schedulingconfig:
        tolerations:
        - key: "node-role.kubernetes.io/control-plane"
          operator: "Exists"
          effect: "NoSchedule"
        nodeaffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 1
            preference:
              matchExpressions:
              - key: another-node-label-key
                operator: In
                values:
                - another-node-label-value
        podAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 1
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - store
              topologyKey: "kubernetes.io/hostname"
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 1
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: security
                  operator: In
                  values:
                  - S1
              topologyKey: "topology.kubernetes.io/zone"

### Custom Parameters

Configure custom PostgreSQL parameters.

#### View Custom Parameters YAML configuration
    
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-pw-dbcluster-sample
    type: Opaque
    data:
      dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: dbcluster-sample
    spec:
      databaseVersion: "18.1.0"
      primarySpec:
        adminUser:
          passwordRef:
            name: db-pw-dbcluster-sample
        resources:
          memory: 5Gi
          cpu: 1
          disks:
          - name: DataDisk
            size: 10Gi
        parameters:
          google_columnar_engine.enabled: "on"
          google_columnar_engine.memory_size_in_mb: "256"

### Debian-based Deployments

Specify a Debian OS image base.

#### View Debian-based Deployments YAML configuration
    
    
    # This is a minimal DBCluster spec. See v1_dbcluster_full.yaml for more configurations.
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-pw-dbcluster-sample
    type: Opaque
    data:
      dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: dbcluster-sample
    spec:
      databaseVersion: "18.1.0"
      databaseImageOSType: Debian
      primarySpec:
        adminUser:
          passwordRef:
            name: db-pw-dbcluster-sample
        resources:
          memory: 5Gi
          cpu: 1
          disks:
          - name: DataDisk
            size: 10Gi

### UBI9-based Deployments

Specify a Red Hat Universal Base Image 9 (UBI 9) base.

#### View UBI9-based Deployments YAML configuration
    
    
    # This is a minimal DBCluster spec. See v1_dbcluster_full.yaml for more configurations.
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-pw-dbcluster-sample
    type: Opaque
    data:
      dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: dbcluster-sample
    spec:
      databaseVersion: "18.1.0"
      databaseImageOSType: UBI9
      primarySpec:
        adminUser:
          passwordRef:
            name: db-pw-dbcluster-sample
        resources:
          memory: 5Gi
          cpu: 1
          disks:
          - name: DataDisk
            size: 10Gi

### Pod Scheduling Options

Configure node affinity, tolerations, and scheduling behaviors.

#### View Pod Scheduling Options YAML configuration
    
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-pw-dbcluster-sample
    type: Opaque
    data:
      dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: dbcluster-sample
    spec:
      databaseVersion: "18.1.0"
      availability:
        numberOfStandbys: 1
        enableStandbyAsReadReplica: true
      primarySpec:
        schedulingconfig:
          topologySpreadConstraints:
            - maxSkew: 1
              topologyKey: "topology.kubernetes.io/zone"
              whenUnsatisfiable: DoNotSchedule
        adminUser:
          passwordRef:
            name: db-pw-dbcluster-sample
        resources:
          memory: 5Gi
          cpu: 1
          disks:
          - name: DataDisk
            size: 10Gi

* * *

## High Availability and Scaling

Distribute traffic and ensure zero or minimal downtime.

### HA DBCluster

Set up multiple replicas for high availability.

#### View HA DBCluster YAML configuration
    
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-pw-dbcluster-sample
    type: Opaque
    data:
      dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: dbcluster-sample
    spec:
      databaseVersion: "18.1.0"
      availability:
        numberOfStandbys: 1
        enableStandbyAsReadReplica: true
      primarySpec:
        adminUser:
          passwordRef:
            name: db-pw-dbcluster-sample
        resources:
          memory: 5Gi
          cpu: 1
          disks:
          - name: DataDisk
            size: 10Gi

### DBCluster with Load Balancer

Expose read/write endpoints by using service load balancing.

#### View DBCluster with Load Balancer YAML configuration
    
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-pw-dbcluster-sample
    type: Opaque
    data:
      dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: dbcluster-sample
    spec:
      databaseVersion: "18.1.0"
      primarySpec:
        adminUser:
          passwordRef:
            name: db-pw-dbcluster-sample
        resources:
          memory: 5Gi
          cpu: 1
          disks:
          - name: DataDisk
            size: 10Gi
        dbLoadBalancerOptions:
          annotations:
            # Creates internal LoadBalancer in GKE.
            networking.gke.io/load-balancer-type: "internal"
      allowExternalIncomingTraffic: true

### Read Pool Instance

Add read-only pool instances to scale read operations.

#### View Read Pool Instance YAML configuration
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBInstance
    metadata:
      name: dbcluster-sample-rp-1
    spec:
      instanceType: ReadPool
      dbcParent:
        name: dbcluster-sample
      nodeCount: 2
      resources:
        memory: 6Gi
        cpu: 2
        disks:
        - name: DataDisk
          size: 15Gi
      schedulingconfig:
        tolerations:
        - key: "node-role.kubernetes.io/control-plane"
          operator: "Exists"
          effect: "NoSchedule"
        nodeaffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 1
            preference:
              matchExpressions:
              - key: another-node-label-key
                operator: In
                values:
                - another-node-label-value
        podAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 1
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - store
              topologyKey: "kubernetes.io/hostname"
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 1
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: security
                  operator: In
                  values:
                  - S1
              topologyKey: "topology.kubernetes.io/zone"

* * *

## Security and Secrets Management

Protect keys, certificates, and cluster credentials.

### Certificate Issuers

Configure custom TLS certificate issuers.

#### View Certificate Issuers YAML configuration
    
    
    # This is a minimal DBCluster spec. See v1_dbcluster_full.yaml for more configurations.
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-pw-dbcluster-sample
    type: Opaque
    data:
      dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: dbcluster-sample
    spec:
      databaseVersion: "18.1.0"
      primarySpec:
        tls:
          dataPlaneCertIssuer:
            name: data-plane-issuer
            kind: ClusterIssuer
          controlPlaneAgentsCertIssuer:
            name: control-plane-issuer
            kind: ClusterIssuer
        adminUser:
          passwordRef:
            name: db-pw-dbcluster-sample
        resources:
          memory: 5Gi
          cpu: 1
          disks:
          - name: DataDisk
            size: 10Gi

### Vault Integration

Retrieve and keep secrets safe by using HashiCorp Vault.

#### View Vault Integration YAML configuration
    
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-pw-dbcluster-sample
    type: Opaque
    data:
    #  dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123
      dbcluster-sample: "ZGhhcm1hbGluZ2FtCg=="
    
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: alloydbadmin-pw-dbcluster-sample
    type: Opaque
    data:
      dbcluster-sample: "Q2hhbmdlTWUxMjM="
    #  dbcluster-sample: "ZGhhcm1hbGluZ2FtCg=="
    #  dbcluster-sample: "YXJhdmluZGFuCg=="
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: dbcluster-sample
    spec:
      databaseVersion: "18.1.0"
    #  availability:
    #    numberOfStandbys: 1
    #    enableStandbyAsReadReplica: true
      primarySpec:
        adminUser:
          passwordRef:
            name: db-pw-dbcluster-sample
        agentPassword:
          passwordRef:
            name: alloydbadmin-pw-dbcluster-sample
        resources:
          memory: 5Gi
          cpu: 1
          disks:
          - name: DataDisk
            size: 10Gi

* * *

## Primary-Standby Replication

Configure replication between upstream (primary) and downstream (standby) databases.

### Upstream (Primary) Configuration

Configure the primary node to publish changes.

#### View Upstream (Primary) Configuration YAML configuration
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Replication
    metadata:
      name: replication-upstream-sample
    spec:
      dbcluster:
        name: dbcluster-sample
      upstream: {}

### Downstream (Standby) Configuration

Configure replication targets to synchronize from a primary node.

#### View Downstream (Standby) Configuration YAML configuration
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Replication
    metadata:
      name: replication-downstream-sample
    spec:
      dbcluster:
        name: dbcluster-sample
      downstream:
        host: "10.10.10.10"
        port: 5432
        username: alloydbreplica
        password:
          name: "ha-rep-pw-dbcluster-sample"
        replicationSlotName: "dbcluster_sample_replication_upstream_sample"
        control: setup
        # to promote downstream, change control to promote

* * *

## Backup, Restore, and Cloning

Manage disaster recovery, on-demand data copies, and schedules.

### Scheduled Backup Plan

Schedule full and incremental backups.

#### View Scheduled Backup Plan YAML configuration
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: BackupPlan
    metadata:
      name: backupplan1
    spec:
      dbclusterRef: dbcluster-sample
      backupRetainDays: 14
      paused: false
      backupSchedules:
        # Full backup at 00:00 on every Sunday.
        full: "0 0 * * 0"
        # Incremental backup at 21:00 every day.
        incremental: "0 21 * * *"

### Backup to Google Cloud Storage (GCS)

Store backups securely in a Google Cloud Storage bucket.

#### View Backup to Google Cloud Storage (GCS) YAML configuration
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: BackupPlan
    metadata:
      name: backupplan1
      namespace: db
    spec:
      dbclusterRef: dbcluster-sample
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
          bucket: dbcluster-sample-backups
          key: /backup
          # You can optionally provide a key for accessing your GCS bucket.
          # The key.json needs to be base64 encoded and stored in the given secret under data[key.json].
          # Or comment out below, which will then use the GKE cluster service account
          # to access the GCS bucket (you need to make sure the service account has
          # the right permission to R/W the GCS bucket).
          secretRef:
            name: gcs-key
            namespace: db
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: gcs-key
      namespace: db
    data:
      key.json: |
        <paste your base64 encoded GCS key json here with 4 spaces for indentation>

### Backup to Amazon S3

Store backups inside an Amazon S3-compatible bucket.

#### View Backup to Amazon S3 YAML configuration
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: BackupPlan
    metadata:
      name: backupplan1
      namespace: db
    spec:
      dbclusterRef: dbcluster-sample
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
          bucket: dbcluster-sample-backups-s3
          key: /backup
          region: "us-east-1"
          endpoint: "https://s3.storage.com"
          secretRef:
            name: s3-access-secret
            namespace: db
          # You can optionally provide the cert to be used to connect to the S3 with TLS.
          # If not provided, TLS verification will be skipped.
          certRef:
            name: server-tls
            namespace: server-ns
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      namespace: db
      name: "s3-access-secret"
    type: Opaque
    data:
      # Update the following with your S3 access keys.
      access-key-id: "Q2hhbmdlTWUxMjM=" # access-key-id is ChangeMe123
      access-key:  "Q2hhbmdlTWUxMjM=" # access-key is ChangeMe123

### On-Demand Manual Backup

Create a single manual backup.

#### View On-Demand Manual Backup YAML configuration
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Backup
    metadata:
      name: backup1
    spec:
      dbclusterRef: dbcluster-sample
      backupPlanRef: backupplan1
      manual: true
      physicalBackupSpec:
        backupType: full

### Restore from Backup

Recover or create a cluster from a stored backup.

#### View Restore from Backup YAML configuration
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Restore
    metadata:
      name: restore1
    spec:
      sourceDBCluster: dbcluster-sample
      backup: backup1

### Database Clone

Clone standard DBClusters.

#### View Database Clone YAML configuration
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Restore
    metadata:
      name: clone1
    spec:
      sourceDBCluster: dbcluster-sample
      pointInTime: "2024-02-23T19:59:43Z"
      clonedDBClusterConfig:
        dbclusterName: new-dbcluster-sample

* * *

## Operations and Failover

Execute safe topology transitions.

### Controlled Switchover

Promote a secondary replica through a planned switchover with zero data loss.

#### View Controlled Switchover YAML configuration
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Switchover
    metadata:
      name: switchover-sample
    spec:
      dbclusterRef: dbcluster-sample

### Disaster Recovery Failover

Handle unplanned disaster recovery or failover scenarios.

#### View Disaster Recovery Failover YAML configuration
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Failover
    metadata:
      name: failover-sample
    spec:
      dbclusterRef: dbcluster-sample

* * *

## Connection Pooling (PgBouncer)

Set up database proxy layers by using PgBouncer.

### Basic PgBouncer

Deploy a standard PgBouncer companion.

#### View Basic PgBouncer YAML configuration
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: PgBouncer
    metadata:
      name: mypgbouncer
    spec:
      allowSuperUserAccess: true
      dbclusterRef: dbcluster-sample
      replicaCount: 1
      parameters:
        pool_mode: transaction
        ignore_startup_parameters: extra_float_digits
        default_pool_size: "15"
        max_client_conn: "800"
        max_db_connections: "160"
      podSpec:
        resources:
          memory: 1Gi
          cpu: 1
        image: "gcr.io/alloydb-omni-staging/g-pgbouncer:1.4.0"
      serviceOptions:
        type: "ClusterIP"

### Full PgBouncer

Configure advanced tuning, custom authorization, and connection-pool overrides.

#### View Full PgBouncer YAML configuration
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: PgBouncer
    metadata:
      name: mypgbouncer
    spec:
      allowSuperUserAccess: true
      dbclusterRef: dbcluster-sample
      replicaCount: 2
      parameters:
        pool_mode: transaction
        ignore_startup_parameters: extra_float_digits
        default_pool_size: "15"
        max_client_conn: "800"
        max_db_connections: "160"
      podSpec:
        resources:
          memory: 1Gi
          cpu: 1
        image: "gcr.io/alloydb-omni-staging/g-pgbouncer:1.4.0"
        schedulingconfig:
          nodeaffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
              nodeSelectorTerms:
              - matchExpressions:
                - key: nodetype
                  operator: In
                  values:
                  - pgbouncer
      serviceOptions:
        type: "LoadBalancer"
        loadBalancerSourceRanges:
        - "11.0.0.0/8"
        annotations:
          networking.gke.io/load-balancer-type: "internal"

* * *

## Integrated Services and Sidecars

Enhance database capabilities with machine learning, observability, and custom agent sidecars.

### DBCluster with ML Agent

Integrate the local ML or Vertex AI proxy sidecar.

#### View DBCluster with ML Agent YAML configuration
    
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-pw-dbcluster-sample
    type: Opaque
    data:
      dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: vertex-ai-key-alloydb
    type: Opaque
    data:
      private-key.json: ""
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: dbcluster-sample
    spec:
      databaseVersion: "18.1.0"
      primarySpec:
        features:
          googleMLExtension:
            enabled: true
            config:
              vertexAIKeyRef: vertex-ai-key-alloydb
              vertexAIRegion: us-central1
        adminUser:
          passwordRef:
            name: db-pw-dbcluster-sample
        resources:
          memory: 5Gi
          cpu: 1
          disks:
          - name: DataDisk
            size: 10Gi

### Observability Configuration

Configure cluster metrics, including custom SQL queries to collect user-defined database and application-specific metrics.

#### View Observability Configuration YAML configuration
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: ObservabilityConfig
    metadata:
      name: my-custom-metrics
    spec:
      dbClusterRefs:
        - dbcluster-sample
      customMetrics:
        resourceLimits:
          workMemory: "4MB"
          maxParallelWorkers: 0 #limits to 1 CPU core
        definitions:
          - metricGroup: querygroup_postgres
            database: "postgres"
            query: |
              SELECT
                datname,
                pg_database_size(datname) as db_size_bytes,
                (SELECT count(*) FROM pg_stat_activity WHERE datname = d.datname) as active_connections
              FROM pg_database d
              WHERE datname = 'postgres'
            metrics:
              - name: datname
                desc: "Database name"
                usage: label
              - name: db_size_bytes
                desc: "Size of the current database in bytes"
                usage: gauge
              - name: active_connections
                desc: "Number of active connections to the database"
                usage: gauge
          - metricGroup: querygroup_alloydbadmin
            database: "alloydbadmin"
            query: |
              SELECT count(*) as healthcheck_count
              FROM healthcheck
            metrics:
              - name: healthcheck_count
                desc: "Number of rows in healthcheck table"
                usage: gauge

### Custom Sidecar

Inject standard support sidecars into your cluster pods.

#### View Custom Sidecar YAML configuration
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Sidecar
    metadata:
      name: sidecar-sample
    spec:
      sidecars:
      - image: busybox
        name: sidecar-sample
        volumeMounts:
          - name: obsdisk
            mountPath: /logs
        command: ["/bin/sh"]
        args:
        - -c
        - |
          while [ true ]
          do
          date
          set -x
          ls -lh /logs/diagnostic
          set +x
          done

### DBCluster with Custom Sidecar

Configure a base DBCluster that includes standard support sidecars.

#### View DBCluster with Custom Sidecar YAML configuration
    
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-pw-dbcluster-sample
    type: Opaque
    data:
      dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: dbcluster-sample
    spec:
      databaseVersion: "18.1.0"
      primarySpec:
        adminUser:
          passwordRef:
            name: db-pw-dbcluster-sample
        resources:
          memory: 5Gi
          cpu: 1
          disks:
          - name: DataDisk
            size: 10Gi
        sidecarRef:
            name: sidecar-sample

### Commvault Backup Sidecar

Specify Commvault agent configuration as a helper sidecar.

#### View Commvault Backup Sidecar YAML configuration
    
    
    # Source: commvault/templates/configmap.yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: cvconfigmap
    data:
      CV_MASVCNAME: commvault-prod
      CV_CSHOSTNAME: "tipcs.idcprodcert.loc"
      CV_CSIPADDR: "123.123.123.123"
      CV_CSCLIENTNAME: "tipcs"
      CV_CLIENT_ROLE: "postgres"
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: commcell-secret
    data:
      CV_COMMCELL_USER: Y3ZhZG1pbgo= # commcell username is cvadmin
      CV_COMMCELL_PWD: Y3ZwYXNzd29yZAo= # commcell password is cvpassword
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Sidecar
    metadata:
      name: cv-sidecar-config
      annotations:
        alloydbomni.dbadmin.goog/sidecar: commvault
    spec:
      sidecars:
      - name: "commvault-pgsqlagent"
        image: "commvault/accessnode:11.32.42"
        lifecycle:
          preStop:
            exec:
              command: [ "/bin/sh", "-c" , "cp /opt/commvault/Base/FwConfig* /etc/CommVaultRegistry/Galaxy/FwConfig/" ]
        envFrom:
        - configMapRef:
            name: cvconfigmap
        volumeMounts:
        - name: logdisk
          mountPath: /archive/
        - name: tmp-socket
          mountPath: /tmp
        - name: commvault-env-store2
          mountPath: /opt/cvdocker_env
          readOnly: true
        - name: backupdisk
          mountPath: /etc/CommVaultRegistry
          subPath: Registry
        - name: backupdisk
          mountPath: /var/log/commvault/Log_Files
          subPath: Log_Files
        - name: backupdisk
          mountPath: /opt/commvault/MediaAgent/IndexCache
          subPath: IndexCache
        - name: backupdisk
          mountPath: /opt/commvault/iDataAgent/jobResults
          subPath: jobResults
        - name: backupdisk
          mountPath: /opt/commvault/Base/certificates
          subPath: certificates
        - name: datadisk
          mountPath: /mnt/disks/pgsql
        - name: commcell-secret
          mountPath: /opt/commcell_secret
        ports:
        - name: cvdport
          containerPort: 8400
        securityContext:
          runAsUser: 0
      additionalVolumes:
      - name: commcell-secret
        secret:
          secretName: commcell-secret
      - name: commvault-env-store2
        configMap:
          name: cvconfigmap

### DBCluster with Commvault Sidecar

Configure a DBCluster that specifies a Commvault agent helper sidecar container.

#### View DBCluster with Commvault Sidecar YAML configuration
    
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-pw-dbcluster-sample
    type: Opaque
    data:
      dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: dbcluster-sample
    spec:
      databaseVersion: "18.1.0"
      primarySpec:
        adminUser:
          passwordRef:
            name: db-pw-dbcluster-sample
        resources:
          memory: 5Gi
          cpu: 1
          disks:
          - name: DataDisk
            size: 10Gi
          - name: LogDisk
            size: 10Gi
        walArchiveSetting:
          location: wal/log  # enable WAL archiving and archive logs to /archive/wal/log
        sidecarRef:
            name: cv-sidecar-config

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
