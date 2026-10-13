---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/audit-backup-restore/
title: Create backup and restore audit logs \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:47.748992+00:00
---

# Create backup and restore audit logs  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/audit-backup-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Create backup and restore audit logs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to secure audit logs from your Google Distributed Cloud (GDC) air-gapped appliance environment in remote backup buckets to preserve and restore data when necessary. The process includes steps for installing and configuring necessary components to recover historical audit logs from those backups.

Backups ensure that audit logs are preserved even if the original data is lost or corrupted, helping meet requirements and letting you recover information in case of system failures or accidental deletions. Restored audit logs provide access to historical data, enabling analysis of past events, security incidents, and user activity.

Implementing a backup and restore process for audit logs is beneficial for maintaining data integrity, ensuring compliance, and enabling historical analysis.

## Before you begin

Ensure you have access to the following resources:

  * A remote bucket for backups with an endpoint, secret access key, and access key ID.
  * A certificate authority (CA) certificate for the storage system.
  * A working Kubernetes cluster.



To get the permissions that you need to manage backups, ask your Project IAM Admin to grant you one of the following roles in your project namespace:

  * Audit Logs Platform Restore Bucket Creator
  * Audit Logs Platform Bucket Viewer



Depending on the level of access and permissions you need, you might obtain creator or viewer roles for backup bucket resources in your project namespace. For more information about these roles, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/obs-iam-permissions).

**Set environment variables** : Set the following environment variables to run the commands from this page:
    
    
    * The path of the kubeconfig file:
    
        ```sh
        export KUBECONFIG=KUBECONFIG_PATH
        ```
    
        Replace `KUBECONFIG_PATH` with the path to the
        kubeconfig file for the Management API server.
    
    * Your project namespace:
    
        ```sh
        export PROJECT_NAMESPACE=PROJECT_NAMESPACE
        ```
    

## Secure audit logs in a backup

This section contains the steps to create a backup for audit logs in a remote bucket.

### Set bucket credentials

You must set the access credentials for the following buckets:

  * **Source bucket** : the local GDC bucket that contains the original audit logs you want to secure.
  * **Destination bucket** : the remote bucket where you want to create the backup for audit logs.



Set the credentials for both buckets:

###  Source bucket 

  1. List the buckets in your project namespace from the Management API server:
         
         kubectl --kubeconfig=${KUBECONFIG} get bucket -n ${PROJECT_NAMESPACE}
         

The `DESCRIPTION` field on the output indicates which buckets contain audit logs. Select the bucket that contains the logs you want to secure.

  2. According to the information from the output, set the following environment variables:
         
         SRC_BUCKET= BUCKET_NAME
         SRC_ENDPOINT = ENDPOINT
         SRC_PATH= FULLY_QUALIFIED_BUCKET_NAME
         

Replace the following:

     * `BUCKET_NAME`: the `BUCKET NAME` value of the output.
     * `ENDPOINT`: the `ENDPOINT` value of the output.
     * `FULLY_QUALIFIED_BUCKET_NAME`: the `FULLY-QUALIFIED-BUCKET-NAME` value of the output.
  3. Get the bucket secret name:
         
         kubectl get secret -n PROJECT_NAMESPACE -o json| jq --arg jq_src $SRC_BUCKET '.items[].metadata|select(.annotations."object.gdc.goog/subject"==$jq_src)|.name'
         

  4. Set the credentials variable:
         
         SRC_CREDENTIALS="PROJECT_NAMESPACE/SECRET_NAME"
         

Replace `SECRET_NAME` with the secret name you obtained.

  5. Create the CA certificate secret:
         
         kubectl create secret generic -n PROJECT_NAMESPACE audit-log-loki-ca \
         --from-literal=ca.crt=CERTIFICATE
         

Replace `CERTIFICATE` with the CA certificate of the storage system.

  6. Set the CA certificate variable:
         
         SRC_CA_CERTIFICATE=PROJECT_NAMESPACE/audit-log-loki-ca
         




###  Destination bucket 

  1. Set the following environment variables for the remote destination bucket:
         
         DST_ACCESS_KEY_ID= ACCESS_KEY
         DST_SECRET_ACCESS_KEY= ACCESS_SECRET
         DST_ENDPOINT= REMOTE_ENDPOINT
         DST_PATH= REMOTE_BUCKET_NAME
         

Replace the following:

     * `ACCESS_KEY`: the access key of the bucket.
     * `ACCESS_SECRET`: the access secret of the bucket.
     * `REMOTE_ENDPOINT`: the endpoint of the bucket.
     * `REMOTE_BUCKET_NAME`: the name of the bucket.
  2. Create a remote bucket secret:
         
         kubectl create secret generic -n PROJECT_NAMESPACE s3-bucket-credentials \
           --from-literal=access-key-id=$DST_ACCESS_KEY_ID \
           --from-literal=secret-access-key=$DST_SECRET_ACCESS_KEY
         

Replace `PROJECT_NAMESPACE` with your project namespace.

  3. Set the credentials variable:
         
         DST_CREDENTIALS=PROJECT_NAMESPACE/s3-bucket-credentials
         

  4. If required, create a secret with the CA certificate of the bucket and set the CA certificate variable:
         
         kubectl create secret generic -n PROJECT_NAMESPACE s3-bucket-ca \
         --from-literal=ca.crt=REMOTE_CERTIFICATE
         

Replace `REMOTE_CERTIFICATE` with the CA certificate of the destination bucket.

Set the CA certificate variable:
         
         DST_CA_CERTIFICATE=PROJECT_NAMESPACE/s3-bucket-ca
         




### Transfer audit logs

Your Infrastructure Operator (IO) must create a transfer job for you to export audit logs from the source bucket to the destination bucket for the backup. The IO uses the preconfigured `audit-log-pa-backup-restore-sa` service account to configure the transfer service for predefined buckets of platform audit logs.

Use the following job to transfer audit logs:
    
    
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: audit-log-transfer-job
      namespace: PROJECT_NAMESPACE
    spec:
      template:
        spec:
          serviceAccountName: audit-log-pa-backup-restore-sa
          containers:
            - name: storage-transfer-pod
              image: gcr.io/private-cloud-staging/storage-transfer:latest
              imagePullPolicy: Always
              command:
                - /storage-transfer
              args:
                - '--src_endpoint=$SRC_ENDPOINT
                - '--dst_endpoint=$DST_ENDPOINT
                - '--src_path=\$SRC_PATH
                - '--dst_path=\$DST_PATH
                - '--src_credentials=$SRC_CREDENTIALS
                - '--dst_credentials=$DST_CREDENTIALS
                - '--dst_ca_certificate_reference=$DST_CA_CERTIFICATE # Optional. Based on destination type.
                - '--src_ca_certificate_reference=$SRC_CA_CERTIFICATE
                - '--src_type=s3'
                - '--dst_type=s3'
                - '--bandwidth_limit=100M' # Optional of the form '10K', '100M', '1G' bytes per second
          restartPolicy: OnFailure # Will restart on failure.
    

[Monitor the data transfer](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/transfer-data) using the job name (`audit-log-transfer-job`) and your project namespace.

The job ends when all the data is transferred to the destination bucket.

## Restore audit logs from a backup

This section contains the steps to restore audit logs from a backup in a remote bucket.

### Create a bucket for restored logs

Create a bucket to store the restored audit logs:

  1. Create the restore bucket:
         
         apiVersion: object.gdc.goog/v1
         kind: Bucket
         metadata:
           annotations:
             object.gdc.goog/audit-logs: PA
           labels:
             logging.private.gdch.goog/loggingpipeline-name: default
           name: audit-logs-loki-restore-pa
           namespace: PROJECT_NAMESPACE
         spec:
           bucketPolicy:
             lockingPolicy:
               defaultObjectRetentionDays: 1
           description: Bucket for storing audit-logs-loki logs restore
           storageClass: Standard
         

Replace `PROJECT_NAMESPACE` with your project namespace.

  2. View the bucket:
         
         kubectl get bucket audit-logs-loki-restore-pa -n PROJECT_NAMESPACE
         

The creation of the bucket might take a few minutes.

  3. According to the information from the output, set the following environment variables:
         
         DST_BUCKET= RESTORE_BUCKET_NAME
         DST_ENDPOINT = RESTORE_ENDPOINT
         DST_PATH= RESTORE_FULLY_QUALIFIED_BUCKET_NAME
         

Replace the following:

     * `RESTORE_BUCKET_NAME`: the `BUCKET NAME` value of the output.
     * `RESTORE_ENDPOINT`: the `ENDPOINT` value of the output.
     * `RESTORE_FULLY_QUALIFIED_BUCKET_NAME`: the `FULLY-QUALIFIED-BUCKET-NAME` value of the output.
  4. Get the bucket secret name:
         
         kubectl get secret -n PROJECT_NAMESPACE -o json| jq --arg jq_src $DST_BUCKET '.items[].metadata|select(.annotations."object.gdc.goog/subject"==$jq_src)|.name'
         

  5. Set the credentials variables:
         
         DST_SECRET_NAME=RESTORE_SECRET_NAME
         DST_CREDENTIALS="PROJECT_NAMESPACE/RESTORE_SECRET_NAME"
         

Replace `RESTORE_SECRET_NAME` with the secret name you obtained.

  6. Create the CA certificate secret:
         
         kubectl create secret generic -n PROJECT_NAMESPACE audit-log-loki-restore-ca \
         --from-literal=ca.crt=CERTIFICATE
         

Replace `CERTIFICATE` with the CA certificate of the storage system.

  7. Set the CA certificate variable:
         
         DST_CA_CERTIFICATE=PROJECT_NAMESPACE/audit-log-loki-restore-ca
         




### Set source bucket credentials

Set the credentials of the bucket that contains the backup for audit logs:

  1. Set the following environment variables:
         
         SRC_ACCESS_KEY_ID= ACCESS_KEY
         SRC_SECRET_ACCESS_KEY= ACCESS_SECRET
         SRC_ENDPOINT= REMOTE_ENDPOINT
         SRC_PATH= REMOTE_BUCKET_NAME
         

Replace the following:

     * `ACCESS_KEY`: the access key of the backup bucket.
     * `ACCESS_SECRET`: the access secret of the backup bucket.
     * `REMOTE_ENDPOINT`: the endpoint of the backup bucket.
     * `REMOTE_BUCKET_NAME`: the name of the backup bucket.
  2. Create a backup bucket secret:
         
         kubectl create secret generic -n PROJECT_NAMESPACE s3-backup-bucket-credentials \
           --from-literal=access-key-id=$SRC_ACCESS_KEY_ID \
           --from-literal=secret-access-key=$SRC_SECRET_ACCESS_KEY
         

  3. Set the credentials variable:
         
         SRC_CREDENTIALS=PROJECT_NAMESPACE/s3-backup-bucket-credentials
         

  4. Create a secret with the CA certificate of the bucket:
         
         kubectl create secret generic -n PROJECT_NAMESPACE s3-backup-bucket-ca \
         --from-literal=ca.crt=BACKUP_CERTIFICATE
         

Replace `BACKUP_CERTIFICATE` with the CA certificate of the backup bucket.

  5. Set the CA certificate variable:
         
         SRC_CA_CERTIFICATE=PROJECT_NAMESPACE/s3-backup-bucket-ca
         




### Transfer restored audit logs

Your Infrastructure Operator (IO) must create a transfer job for you to restore audit logs from the backup bucket to the restoration bucket. The IO uses the preconfigured `audit-log-pa-backup-restore-sa` service account to configure the transfer service for predefined buckets of platform audit logs.

Use the following job to transfer audit logs:
    
    
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: audit-log-restore-job
      namespace: PROJECT_NAMESPACE
    spec:
      template:
        spec:
          serviceAccountName: audit-log-pa-backup-restore-sa
          containers:
            - name: storage-transfer-pod
              image: gcr.io/private-cloud-staging/storage-transfer:latest
              imagePullPolicy: Always
              command:
                - /storage-transfer
              args:
                - '--src_endpoint=$SRC_ENDPOINT
                - '--dst_endpoint=$DST_ENDPOINT
                - '--src_path=\$SRC_PATH
                - '--dst_path=\$DST_PATH
                - '--src_credentials=$SRC_CREDENTIALS
                - '--dst_credentials=$DST_CREDENTIALS
                - '--dst_ca_certificate_reference=$DST_CA_CERTIFICATE
                - '--src_ca_certificate_reference=$SRC_CA_CERTIFICATE # Optional. Based on destination type
                - '--src_type=s3'
                - '--dst_type=s3'
                - '--bandwidth_limit=100M' # Optional of the form '10K', '100M', '1G' bytes per second
          restartPolicy: OnFailure # Will restart on failure.
    

[Monitor the data transfer](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/transfer-data) using the job name (`audit-log-restore-job`) and your project namespace.

The job ends when all the data is transferred to the restoration bucket.

### Access restored logs

Deploy a Loki instance to access the restored logs using the provided configuration and deployment manifests:

  1. Create a `ConfigMap` object for the configuration of the instance.

The following is an example of a `ConfigMap` object:
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: audit-logs-loki-restore-pa
           namespace: PROJECT_NAMESPACE
         data:
           loki.yaml: |-
             auth_enabled: true
             common:
               ring:
                 kvstore:
                   store: inmemory
             chunk_store_config:
               max_look_back_period: 0s
             compactor:
               shared_store: s3
               working_directory: /data/loki/boltdb-shipper-compactor
               compaction_interval: 10m
               retention_enabled: true
               retention_delete_delay: 2h
               retention_delete_worker_count: 150
             ingester:
               chunk_target_size: 1572864
               chunk_encoding: snappy
               max_chunk_age: 2h
               chunk_idle_period: 90m
               chunk_retain_period: 30s
               autoforget_unhealthy: true
               lifecycler:
                 ring:
                   kvstore:
                     store: inmemory
                   replication_factor: 1
                   heartbeat_timeout: 10m
               max_transfer_retries: 0
               wal:
                 enabled: true
                 flush_on_shutdown: true
                 dir: /wal
                 checkpoint_duration: 1m
                 replay_memory_ceiling: 20GB
             limits_config:
               retention_period: 48h
               enforce_metric_name: false
               reject_old_samples: false
               ingestion_rate_mb: 256
               ingestion_burst_size_mb: 256
               max_streams_per_user: 20000
               max_global_streams_per_user: 20000
               per_stream_rate_limit: 256MB
               per_stream_rate_limit_burst: 256MB
               shard_streams:
                 enabled: false
                 desired_rate: 3MB
             schema_config:
               configs:
               - from: "2020-10-24"
                 index:
                   period: 24h
                   prefix: index_
                 object_store: s3
                 schema: v11
                 store: boltdb-shipper
             server:
               http_listen_port: 3100
               grpc_server_max_recv_msg_size: 104857600
               grpc_server_max_send_msg_size: 104857600
             analytics:
               reporting_enabled: false
             storage_config:
               boltdb_shipper:
                 active_index_directory: /data/loki/boltdb-shipper-active
                 cache_location: /data/loki/boltdb-shipper-cache
                 cache_ttl: 24h
                 shared_store: s3
               aws:
                 endpoint: $DST_ENDPOINT
                 bucketnames: $DST_PATH
                 access_key_id: ${S3_ACCESS_KEY_ID}
                 secret_access_key: ${S3_SECRET_ACCESS_KEY}
                 s3forcepathstyle: true
         

  2. Deploy the instance as a `StatefulSet` object with a `Service` for accessing logs.

The following is an example of `StatefulSet` and `Service` objects:
         
         apiVersion: apps/v1
         kind: StatefulSet
         metadata:
           labels:
             app: audit-logs-loki-restore-pa
             logging.private.gdch.goog/loggingpipeline-name: default
           name: audit-logs-loki-restore-pa
           namespace: PROJECT_NAMESPACE
         spec:
           persistentVolumeClaimRetentionPolicy:
             whenDeleted: Retain
             whenScaled: Retain
           podManagementPolicy: OrderedReady
           replicas: 1
           revisionHistoryLimit: 10
           selector:
             matchLabels:
               app: audit-logs-loki-restore-pa
           serviceName: audit-logs-loki-restore-pa
           template:
             metadata:
               labels:
                 app: audit-logs-loki-restore-pa
                 app.kubernetes.io/part-of: audit-logs-loki-restore-pa
                 egress.networking.gke.io/enabled: "true"
                 istio.io/rev: default
                 logging.private.gdch.goog/log-type: audit
             spec:
               affinity:
                 nodeAffinity:
                   preferredDuringSchedulingIgnoredDuringExecution:
                   - preference:
                       matchExpressions:
                       - key: node-role.kubernetes.io/control-plane
                         operator: DoesNotExist
                       - key: node-role.kubernetes.io/master
                         operator: DoesNotExist
                     weight: 1
                 podAntiAffinity:
                   preferredDuringSchedulingIgnoredDuringExecution:
                   - podAffinityTerm:
                       labelSelector:
                         matchExpressions:
                         - key: app
                           operator: In
                           values:
                           - audit-logs-loki-restore-pa
                       topologyKey: kubernetes.io/hostname
                     weight: 100
               containers:
               - args:
                 - -config.file=/etc/loki/loki.yaml
                 - -config.expand-env=true
                 - -target=all
                 env:
                 - name: S3_ACCESS_KEY_ID
                   valueFrom:
                     secretKeyRef:
                       key: access-key-id
                       name: $DST_SECRET_NAME
                       optional: false
                 - name: S3_SECRET_ACCESS_KEY
                   valueFrom:
                       secretKeyRef:
                         key: secret-access-key
                         name: $DST_SECRET_NAME
                         optional: false
                 image: gcr.io/private-cloud-staging/loki:v2.8.4-gke.2
                 imagePullPolicy: Always
                 livenessProbe:
                   failureThreshold: 3
                   httpGet:
                     path: /ready
                     port: http-metrics
                     scheme: HTTP
                   initialDelaySeconds: 330
                   periodSeconds: 10
                   successThreshold: 1
                   timeoutSeconds: 1
                 name: audit-logs-loki-restore-pa
                 ports:
                 - containerPort: 3100
                   name: http-metrics
                   protocol: TCP
                 - containerPort: 7946
                   name: gossip-ring
                   protocol: TCP
                 readinessProbe:
                   failureThreshold: 3
                   httpGet:
                     path: /ready
                     port: http-metrics
                     scheme: HTTP
                   initialDelaySeconds: 45
                   periodSeconds: 10
                   successThreshold: 1
                   timeoutSeconds: 1
                 resources:
                   limits:
                     ephemeral-storage: 2000Mi
                     memory: 8000Mi
                   requests:
                     cpu: 300m
                     ephemeral-storage: 2000Mi
                     memory: 1000Mi
                 securityContext:
                   readOnlyRootFilesystem: true
                 terminationMessagePath: /dev/termination-log
                 terminationMessagePolicy: File
                 volumeMounts:
                 - mountPath: /etc/loki
                   name: config
                 - mountPath: /data
                   name: loki-storage
                 - mountPath: /tmp
                   name: temp
                 - mountPath: /tmp/loki/rules-temp
                   name: tmprulepath
                 - mountPath: /etc/ssl/certs/storage-cert.crt
                   name: storage-cert
                   subPath: ca.crt
                 - mountPath: /wal
                   name: loki-storage
               dnsPolicy: ClusterFirst
               priorityClassName: audit-logs-loki-priority
               restartPolicy: Always
               schedulerName: default-scheduler
               securityContext:
                 fsGroup: 10001
                 runAsGroup: 10001
                 runAsUser: 10001
               serviceAccount: audit-log-pa-backup-restore-sa
               serviceAccountName: audit-log-pa-backup-restore-sa
               terminationGracePeriodSeconds: 4800
               volumes:
               - emptyDir: {}
                 name: temp
               - configMap:
                   defaultMode: 420
                   name: audit-logs-loki-restore-pa
                 name: config
               - emptyDir: {}
                 name: tmprulepath
               - name: storage-cert
                 secret:
                   defaultMode: 420
                   secretName: web-tls
           updateStrategy:
             type: RollingUpdate
           volumeClaimTemplates:
           - apiVersion: v1
             kind: PersistentVolumeClaim
             metadata:
               creationTimestamp: null
               name: loki-storage
             spec:
               accessModes:
               - ReadWriteOnce
               resources:
                 requests:
                   storage: 50Gi
               storageClassName: standard-rwo
               volumeMode: Filesystem
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: audit-logs-loki-restore-pa
           namespace: PROJECT_NAMESPACE
         spec:
           internalTrafficPolicy: Cluster
           ipFamilies:
           - IPv4
           ipFamilyPolicy: SingleStack
           ports:
           - name: http-metrics
             port: 3100
             protocol: TCP
             targetPort: http-metrics
           selector:
             app: audit-logs-loki-restore-pa
           sessionAffinity: None
           type: ClusterIP
         




### View restored logs

**Note:** The system can revert the configuration of the Loki instance as the data source.

Configure Grafana to view the restored audit logs from the Loki instance:

  1. Open the Grafana endpoint of your project. For more information, see [Query and view logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/query-and-view-logs).
  2. From the navigation menu of the user interface, click **Administration** > **Data sources**.
  3. Click add **Add new data source**.
  4. On the **Add data source** page, select **Loki**.
  5. On the **Settings** page, enter `Audit Logs - Restore` in the **Name** field.
  6. On the **HTTP** section, enter the following value in the **URL** field:
         
         http://audit-logs-loki-restore-pa.PROJECT_NAMESPACE.svc:3100
         

  7. On the **Custom HTTP Headers** section, enter the following values in the corresponding fields:

     * **Header:** `X-Scope-OrgID`
     * **Value:** `infra-obs`



In figure 1, **Loki** is displayed as an option on the **Add data source** page.

![The Loki option is displayed as a data source on the Add data source page of the UI.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/admin/images/audit-log-ui.png)

**Figure 1.** The **Add data source** page on the UI of the monitoring instance.

![The relevant fields to configure Loki as the data source are displayed on the Settings page](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/admin/images/datasource-setup-ui.png)

**Figure 2.** The **Settings** page on the UI of the monitoring instance.

The `Audit Logs - Restore` option is now available as a data source in the log explorer.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
