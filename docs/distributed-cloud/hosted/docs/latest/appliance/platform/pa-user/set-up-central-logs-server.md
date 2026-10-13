---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/set-up-central-logs-server/
title: Set up central logs server \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:47.551947+00:00
---

# Set up central logs server  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/set-up-central-logs-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Set up central logs server Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up a central logs server for Google Distributed Cloud (GDC) air-gapped appliance devices through the Google Distributed Cloud air-gapped data center organization.

To create a central logging location, the GDC appliance must have the following components in the GDC data center organization:

  * unique project
  * bucket for the audit logs 
  * bucket for operational logs



## Create a project

The following steps must be performed in the GDC data center organization to which the logs will be exported.

  1. Set `KUBECONFIG` to the Org Management API:
         
         export KUBECONFIG=ORG_MANAGEMENT_API_KUBECONFIG_PATH
         

**Note:** For legacy GDC data center organization architecture, this is the `kubeconfig` for the Org admin cluster.
  2. To get the permissions that you need to export logs, ask your Organization IAM Admin to grant you the ClusterRole Project Creator (`ClusterRole project-creator`) role. For more information about these roles, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/obs-iam-permissions).

  3. Apply the project custom resource to create a unique project for the GDC appliance from which the logs will be exported:
         
         kubectl apply -f - <<EOF
         apiVersion: resourcemanager.gdc.goog/v1
         kind: Project
         metadata:
           namespace: platform
           name: APPLIANCE_PROJECT_NAME
           labels:                                                                                                                                                                                                                                                                   
             object.gdc.goog/tenant-category: user                                                                                                                                   
         EOF
         

  4. Verify if the new project is available in the GDC appliance:
         
         kubectl get namespace APPLIANCE_PROJECT_NAME
         

  5. Link your new project to a billing account. To track project resource costs, you must have an associated billing account linked to your project.

  6. To get the permissions that you need to export logs, ask your Organization IAM Admin to grant you the Project IAM Admin (`project-iam-admin`) role in the namespace `APPLIANCE_PROJECT_NAME`.




## Create a bucket

The following steps must be performed by the Platform Administrator (PA) in the GDC data center organization to which the logs will be exported.

  1. Set `KUBECONFIG` to the Org Management API:
         
         export KUBECONFIG=ORG_MANAGEMENT_API_KUBECONFIG_PATH
         

**Note:** For legacy GDC data center organization architecture, this is the `kubeconfig` for the Org admin cluster.
  2. To get the permissions that you need to export logs, ask your Organization IAM Admin to grant you the Project Bucket Admin (`project-bucket-admin`) role in the namespace `APPLIANCE_PROJECT_NAME`.

  3. Apply the bucket custom resource to create a bucket:
         
         apiVersion: object.gdc.goog/v1
         kind: Bucket
         metadata:
           name: BUCKET_NAME
           namespace: APPLIANCE_PROJECT_NAME
           labels:                                                                                                                                                                     
             object.gdc.goog/bucket-type: normal                                                                                                                                       
             object.gdc.goog/encryption-version: v2                                                                                                                                    
             object.gdc.goog/tenant-category: user
         spec:                                                                                                                                                                         
           description: Bucket for storing appliance xyz audit logs                                                                                                                     
           location: zone1                                                                                                                                                             
           storageClass: Standard
         

  4. After the bucket is created, run the following to confirm and check the details of the bucket:
         
         kubectl describe buckets BUCKET_NAME -n APPLIANCE_PROJECT_NAME
         

  5. Create a `ProjectServiceAccount` for accessing objects in the bucket.
         
         kubectl apply -f - <<EOF
         ---
         apiVersion: resourcemanager.gdc.goog/v1
         kind: ProjectServiceAccount
         metadata:
           name: BUCKET_NAME-read-write-sa
           namespace: APPLIANCE_PROJECT_NAME
         spec: {}
         EOF
         

  6. Verify that the `ProjectServiceAccount` is propagated:
         
         kubectl get projectserviceaccount BUCKET_NAME-read-write-sa -n APPLIANCE_PROJECT_NAME -o json | jq '.status'
         

  7. Ensure that the `ServiceAccount` has `read` and `write` permissions are added to it for the bucket.
         
         kubectl apply -f - <<EOF
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: Role
         metadata:
           name: BUCKET_NAME-read-write-role
           namespace: APPLIANCE_PROJECT_NAME
         rules:
         - apiGroups:
           - object.gdc.goog
           resourceNames:
           - BUCKET_NAME
           resources:
           - buckets
           verbs:
           - read-object
           - write-object
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
           name: BUCKET_NAME-read-write-rolebinding
           namespace: APPLIANCE_PROJECT_NAME
         roleRef:
           apiGroup: rbac.authorization.k8s.io
           kind: Role
           name: BUCKET_NAME-read-write-role
         subjects:
         - kind: ServiceAccount
           name: BUCKET_NAME-read-write-sa
           namespace: APPLIANCE_PROJECT_NAME
         EOF
         

  8. Obtain the secret that contains access credentials for the bucket:
         
         kubectl get secret -n APPLIANCE_PROJECT_NAME -o json| jq --arg jq_src BUCKET_NAME-read-write-sa '.items[].metadata|select(.annotations."object.gdc.goog/subject"==$jq_src)|.name'
         

The output must look like the following example, where the secret name of the bucket is displayed:
         
         "object-storage-key-sysstd-sa-olxv4dnwrwul4bshu37ikebgovrnvl773owaw3arx225rfi56swa"
         

  9. Export the value to a variable:
         
         export BUCKET_RW_SECRET_NAME=BUCKET_RW_SECRET_NAME
         

  10. Obtain the key ID for bucket access:
         
         kubectl get secret $BUCKET_RW_SECRET_NAME -n appliance-xyz -o json | jq -r '.data."access-key-id"' | base64 -di
         

The output must look like the following example:
         
         PCEW2HU47Y8ACUWQO4SK
         

  11. Obtain the secret access key for the bucket:
         
         kubectl get secret $BUCKET_RW_SECRET_NAME -n appliance-xyz -o json | jq -r '.data."secret-access-key"' | base64 -di
         

The output must look like the following example:
         
         TzGdAbgp4h2i5UeiYa9k09rNPFQ2tkYADs67+65E
         

  12. Obtain the endpoint of the bucket:
         
         kubectl get bucket BUCKET_NAME -n APPLIANCE_PROJECT_NAME -o json | jq '.status.endpoint'
         

The output must look like the following example:
         
         https://objectstorage.org-1.zone1.google.gdch.test
         

  13. Obtain the fully qualified name of the bucket:
         
         kubectl get bucket BUCKET_NAME -n APPLIANCE_PROJECT_NAME -o json | jq '.status.fullyQualifiedName'
         

The output must look like the following example:
         
         aaaoa9a-logs-bucket
         




## Transfer data from GDC

Follow [Export logs to a remote bucket](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/export-logs) to a remote bucket to transfer logs from the GDC appliance to the bucket created earlier in the GDC air-gapped data center using the endpoint of the bucket, fully qualified name, access key ID, and the secret access key. 

**Note:** The audit and operational logs must be exported separately. The audit and operational logs must have their own destination buckets and transfer jobs.

## Set up Loki and Grafana in Google Distributed Cloud air-gapped data center

The following steps must be performed by the Infrastructure Operator (IO) in the GDC air-gapped data center organization to which the logs have been exported.

### Obtain IAM roles

To get the permissions that you need to export logs, ask your Organization IAM Admin to grant you the Logs Restore Admin (`logs-restore-admin`) role in the namespace `obs-system` in the infra cluster and the Datasource Viewer (`datasource-viewer`) and Datasource Editor (`datasource-editor`) roles in the namespace `obs-system` in the management plane.

### Set up Loki

  1. Set `KUBECONFIG` to the Org Infra cluster:
         
         export KUBECONFIG=ORG_INFRA_CLUSTER_KUBECONFIG_PATH
         

  2. Obtain the access key ID and secret access key for the appliance logs bucket from the PA and create a secret that contains the credentials in the `obs-system` namespace:
         
         kubectl create secret generic -n obs-system APPLIANCE_LOGS_BUCKET_SECRET_NAME 
         --from-literal=access-key-id=APPLIANCE_LOGS_BUCKET_ACCESS_KEY_ID 
         --from-literal=secret-access-key=APPLIANCE_LOGS_BUCKET_SECRET_ACCESS_KEY
         

  3. Obtain the endpoint and fully qualified name of the appliance logs bucket from the PA and create a Loki `configmap`:
         
         kubectl apply -f - <<EOF
         ---
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: CONFIGMAP_NAME
           namespace: obs-system
         data:
           loki.yaml: |-
             auth_enabled: true
             common:
               ring:
                 kvstore:
                   store: inmemory
             compactor:
               working_directory: /data/loki/compactor
               compaction_interval: 10m
               retention_enabled: true
               retention_delete_delay: 2h
               retention_delete_worker_count: 150
               delete_request_store: s3
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
               wal:
                 enabled: false
             limits_config:
               discover_service_name: []
               retention_period: 48h
               reject_old_samples: false
               ingestion_rate_mb: 256
               ingestion_burst_size_mb: 256
               max_streams_per_user: 20000
               max_global_streams_per_user: 20000
               max_line_size: 0
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
                 schema: v13
                 store: tsdb
             server:
               http_listen_port: 3100
               grpc_server_max_recv_msg_size: 104857600
               grpc_server_max_send_msg_size: 104857600
               graceful_shutdown_timeout: 60s
             analytics:
               reporting_enabled: false
             storage_config:
               tsdb_shipper:
                 active_index_directory: /tsdb/index
                 cache_location: /tsdb/index-cache
                 cache_ttl: 24h
               aws:
                 endpoint: APPLIANCE_LOGS_BUCKET_ENDPOINT
                 bucketnames: APPLIANCE_LOGS_BUCKET_FULLY_QUALIFIED_NAME
                 access_key_id: ${S3_ACCESS_KEY_ID}
                 secret_access_key: ${S3_SECRET_ACCESS_KEY}
                 s3forcepathstyle: true
         ---
         EOF
         

  4. Create a Loki `statefulset` and service:
         
         kubectl apply -f - <<EOF
         ---
         apiVersion: apps/v1
         kind: StatefulSet
         metadata:
           labels:
             app: STATEFULSET_NAME
           name: STATEFULSET_NAME
           namespace: obs-system
         spec:
           persistentVolumeClaimRetentionPolicy:
             whenDeleted: Retain
             whenScaled: Retain
           podManagementPolicy: OrderedReady
           replicas: 1
           revisionHistoryLimit: 10
           selector:
             matchLabels:
               app: STATEFULSET_NAME
           serviceName: STATEFULSET_NAME
           template:
             metadata:
               labels:
                 app: STATEFULSET_NAME
                 istio.io/rev: default
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
                           - STATEFULSET_NAME
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
                       key: access-key-ID
                       name: APPLIANCE_LOGS_BUCKET_SECRET_NAME
                       optional: false
                 - name: S3_SECRET_ACCESS_KEY
                   valueFrom:
                       secretKeyRef:
                         key: secret-access-key
                         name: APPLIANCE_LOGS_BUCKET_SECRET_NAME
                         optional: false
                 image: gcr.io/private-cloud-staging/loki:v3.0.1-gke.1
                 imagePullPolicy: Always
                 livenessProbe:
                   failureThreshold: 3
                   httpGet:
                     path: /ready
                     port: loki-server
                     scheme: HTTP
                   initialDelaySeconds: 330
                   periodSeconds: 10
                   successThreshold: 1
                   timeoutSeconds: 1
                 name: STATEFULSET_NAME
                 ports:
                 - containerPort: 3100
                   name: loki-server
                   protocol: TCP
                 - containerPort: 7946
                   name: gossip-ring
                   protocol: TCP
                 readinessProbe:
                   failureThreshold: 3
                   httpGet:
                     path: /ready
                     port: loki-server
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
                 - mountPath: /tsdb
                   name: loki-tsdb-storage
                 - mountPath: /tmp
                   name: temp
                 - mountPath: /tmp/loki/rules-temp
                   name: tmprulepath
                 - mountPath: /etc/ssl/certs
                   name: trust-bundle
                   readOnly: true
               dnsPolicy: ClusterFirst
               restartPolicy: Always
               schedulerName: default-scheduler
               securityContext:
                 fsGroup: 10001
                 runAsGroup: 10001
                 runAsUser: 10001
               terminationGracePeriodSeconds: 4800
               volumes:
               - emptyDir: {}
                 name: temp
               - emptyDir: {}
                 name: tmprulepath
               - configMap:
                   defaultMode: 420
                   name: trust-store-root-ext
                   optional: true
                 name: trust-bundle
               - configMap:
                   defaultMode: 420
                   name: CONFIGMAP_NAME
                 name: config
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
                   storage: 5Gi
               storageClassName: standard-rwo
               volumeMode: Filesystem
           - apiVersion: v1
             kind: PersistentVolumeClaim
             metadata:
               creationTimestamp: null
               name: loki-tsdb-storage
             spec:
               accessModes:
               - ReadWriteOnce
               resources:
                 requests:
                   storage: 5Gi
               storageClassName: standard-rwo
               volumeMode: Filesystem
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: STATEFULSET_NAME
           namespace: obs-system
         spec:
           internalTrafficPolicy: Cluster
           ipFamilies:
           - IPv4
           ipFamilyPolicy: SingleStack
           ports:
           - name: loki-server
             port: 3100
             protocol: TCP
             targetPort: loki-server
           selector:
             app: STATEFULSET_NAME
           sessionAffinity: None
           type: ClusterIP
         ---
         EOF
         




## Set up Grafana `DataSource`

  1. Set `KUBECONFIG` to the Org Management API:
         
         export KUBECONFIG=ORG_MANAGEMENT_API_KUBECONFIG_PATH
         

**Note:** For legacy GDC air-gapped data center architecture, this is the `kubeconfig` for the Org admin cluster.
  2. Create `DataSources` for the Infra and Platform logs:
         
         kubectl apply -f - <<EOF
         ---
         apiVersion: monitoring.private.gdc.goog/v1alpha1
         kind: Datasource
         metadata:
           name: INFRA_DATASOURCE_NAME
           namespace: APPLIANCE_PROJECT_NAME-obs-system
         spec:
           datasource:
             access: proxy
             isDefault: false
             jsonData:
               httpHeaderName1: X-Scope-OrgID
             name: UI_FRIENDLY_NAME
             orgId: 1
             readOnly: true
             secureJsonData:
               httpHeaderValue1: infra-obs
             type: loki
             uid: INFRA_DATASOURCE_NAME
             url: http://STATEFULSET_NAME.obs-system.svc:3100
             version: 1
             withCredentials: false
         ---
         apiVersion: monitoring.private.gdc.goog/v1alpha1
         kind: Datasource
         metadata:
           name: PLATFORM_DATASOURCE_NAME
           namespace: APPLIANCE_PROJECT_NAME-obs-system
         spec:
           datasource:
             access: proxy
             isDefault: false
             jsonData:
               httpHeaderName1: X-Scope-OrgID
             name: UI_FRIENDLY_NAME
             orgId: 1
             readOnly: true
             secureJsonData:
               httpHeaderValue1: platform-obs
             type: loki
             uid: PLATFORM_DATASOURCE_NAME
             url: http://STATEFULSET_NAME.obs-system.svc:3100
             version: 1
             withCredentials: false
         ---
         EOF
         




## View logs in Google Distributed Cloud air-gapped data center Grafana

The logs exported to the Google Distributed Cloud air-gapped data center bucket can be viewed in the Grafana instance of the GDC appliance project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
