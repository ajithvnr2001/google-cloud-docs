---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/transfer-data/
title: Transfer data \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:04.352423+00:00
---

# Transfer data  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/transfer-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Transfer data Stay organized with collections  Save and categorize content based on your preferences. 

Data transfers can occur between the following:

  1. Persistent Volume Claim (PVC) and object storage
  2. Object storage and object storage (within GDC)



Object storage on GDC is S3-compatible and referred to as `s3` type in Kubernetes yamls.

### Types of data sources and destinations

  1. Object storage (referred to as 's3'): Object storage present on GDC
  2. Local storage (referred to as 'local'): Storage on attached PVCs



## Copying from object storage to object storage

Ensure you have the following prerequisites:

  * An S3 Endpoint with read permissions for the source, and an s3 endpoint with write permissions for the destination.
  * If you don't have bucket creation permission with the credentials, the transfer fails if the destination bucket doesn't exist. Ensure the destination bucket exists if that is the case.
  * Privileges to create Jobs and create or read Secrets inside your cluster or namespace. See the following example for permissions.



### Set up the data transfer

To set up the data transfer, complete the following steps:

### Create the transfer namespace

Create the namespace where the transfer job will run:
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      name: NAMESPACE
    

### Configure credentials

Prepare your credentials for the transfer. Follow the option that best matches your transfer scenario.

#### GDC to GDC transfer

For a transfer occurring completely within the **same GDC universe** , the secrets already exist. Note that this method is strictly for transfers within a single universe, not for transfers between different universes.

  1. To obtain the S3 credential Secrets, follow the instructions to [grant bucket access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/grant-obtain-storage-access#grant_bucket_access).

  2. Create a service account (SA) in the destination namespace for your transfer job. Then, add permissions to allow this account to read Secrets in both the source and destination namespaces using cross-namespace RoleBindings.

**Note:** This step is only required if the source and destination buckets are in different namespaces. For transfers within the same GDC project, this step can be skipped.
         
         ---
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: transfer-service-account
           namespace: DESTINATION_NAMESPACE
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: Role
         metadata:
           name: read-secrets-role
           namespace: SOURCE_NAMESPACE
         rules:
         - apiGroups: [""]
           resources: ["secrets"]
           verbs: ["get", "watch", "list"]
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
           name: read-source-secrets-rolebinding
           namespace: SOURCE_NAMESPACE
         subjects:
         - kind: ServiceAccount
           name: transfer-service-account
           namespace: DESTINATION_NAMESPACE
         roleRef:
           kind: Role
           name: read-secrets-role
           apiGroup: rbac.authorization.k8s.io
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: Role
         metadata:
           name: read-secrets-role
           namespace: DESTINATION_NAMESPACE
         rules:
         - apiGroups: [""]
           resources: ["secrets"]
           verbs: ["get", "watch", "list"]
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
           name: read-dest-secrets-rolebinding
           namespace: DESTINATION_NAMESPACE
         subjects:
         - kind: ServiceAccount
           name: transfer-service-account
           namespace: DESTINATION_NAMESPACE
         roleRef:
           kind: Role
           name: read-secrets-role
           apiGroup: rbac.authorization.k8s.io
         ---
         




#### GDC to non-GDC transfer

For a transfer involving an external system, you must specify the access credentials explicitly. 

  1. Create credentials in the destination namespace:
         
         ---
         apiVersion: v1
         kind: Secret
         metadata:
           name: src-secret
           namespace: NAMESPACE
         data:
           access-key-id: NkFDTUg3WDBCVDlQMVpZMU5MWjU= # base 64 encoded version of key
           access-key: VkRkeWJsbFgzb2FZanMvOVpnSi83SU5YUjk3Y0Q2TUdxZ2d4Q3dpdw== # base 64 encoded version of secret key
         ---
         apiVersion: v1
         kind: Secret
         metadata:
           name: dst-secret
           namespace: NAMESPACE
         data:
           access-key-id: NkFDTUg3WDBCVDlQMVpZMU5MWjU= # base 64 encoded version of key
           access-key: VkRkeWJsbFgzb2FZanMvOVpnSi83SU5YUjk3Y0Q2TUdxZ2d4Q3dpdw== # base 64 encoded version of secret key
         ---
         

  2. Create a service account (SA) that is used by your transfer, and then add permissions to the account to read and write secrets using roles and role bindings. You don't need to add permissions if your default namespace SA or custom SA already has these permissions.
         
         ---
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: transfer-service-account
           namespace: NAMESPACE
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: Role
         metadata:
           name: read-secrets-role
           namespace: NAMESPACE
         rules:
         - apiGroups: [""]
           resources: ["secrets"]
           verbs: ["get", "watch", "list"]
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
           name: read-secrets-rolebinding
           namespace: NAMESPACE
         subjects:
         - kind: ServiceAccount
           name: transfer-service-account
           namespace: NAMESPACE
         roleRef:
           kind: Role
           name: read-secrets-role
           apiGroup: rbac.authorization.k8s.io
         ---
         




### Obtain CA certificates

Obtain the CA certificates for your object storage systems. You can obtain the same certificates from your AO or PA by following the instructions to [fetch trust bundles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/fetch-trust-bundles).
    
    
    ---
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: src-cert
      namespace: NAMESPACE
    data:
      ca.crt: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURBekNDQWV1Z0F3SUJBZ0lSQUpHM2psOFZhTU85a1FteGdXUFl3N3d3RFFZSktvWklodmNOQVFFTEJRQXcKR3pFWk1CY0dBMVVFQXhNUVltOXZkSE4wY21Gd0xYZGxZaTFqWVRBZUZ3MHlNekF5TVRVd01USXlNakZhRncweQpNekExTVRZd01USXlNakZhTUJzeEdUQVhCZ05WQkFNVEVHSnZiM1J6ZEhKaGNDMTNaV0l0WTJFd2dnRWlNQTBHCkNTcUdTSWI== # base 64 encoded version of certificate
    
    ---
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: dst-cert
      namespace: NAMESPACE
    data:
      ca.crt: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURBekNDQWV1Z0F3SUJBZ0lSQUtoaEJXWWo3VGZlUUZWUWo0U0RpckV3RFFZSktvWklodmNOQVFFTEJRQXcKR3pFWk1CY0dBMVVFQXhNUVltOXZkSE4wY21Gd0xYZGxZaTFqWVRBZUZ3MHlNekF6TURZeU16TTROVEJhRncweQpNekEyTURReU16TTROVEJhTUJzeEdUQVhCZ05WQkFNVEVHSnZiM1J6ZEhKaGNDMTNaV0l0WTJFd2dnRWlNQTBHCkNTcUdTSWIzRFFF== # base 64 encoded version of certificate. Can be same OR different than source certificate.
    
    ---
    
    

### (Optional) Create a LoggingTarget

Create a LoggingTarget to see transfer-service logs in Loki.
    
    
    apiVersion: logging.gdc.goog/v1
    kind: LoggingTarget
    metadata:
      namespace: NAMESPACE # Same namespace as your transfer job
      name: logtarg1
    spec:
      # Choose matching pattern that identifies pods for this job
      # Optional
      # Relationship between different selectors: AND
      selector:
    
        # Choose pod name prefix(es) to consider for this job
        # Observability platform will scrape all pods
        # where names start with specified prefix(es)
        # Should contain [a-z0-9-] characters only
        # Relationship between different list elements: OR
        matchPodNames:
          - transfer-job # Choose the prefix here that matches your transfer job name
      serviceName: transfer-service
    

### Create the transfer workload

You can run the transfer as a one-time operation using a `Job`, or schedule it to run repeatedly using a `CronJob`.

Choose the method that best fits your use case:

#### Create a one-time Job

Use this configuration for a single, manual data transfer.
    
    
    ---
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: transfer-job
      namespace: NAMESPACE
    spec:
      template:
        spec:
          serviceAccountName: transfer-service-account # The service account created in the previous step
          containers:
            - name: storage-transfer-pod
              image: gcr.io/private-cloud-staging/storage-transfer:latest
              imagePullPolicy: Always
              command:
                - /storage-transfer
              args:
                # The S3 endpoints for your source and destination
                - '--src_endpoint=SRC_ENDPOINT'
                - '--dst_endpoint=DST_ENDPOINT'
                # The Fully Qualified Names (FQN) of the buckets
                - '--src_path=SRC_BUCKET_FQN/'
                - '--dst_path=DST_BUCKET_FQN/'
                # Cross-namespace mapping: point directly to the live credentials using NAMESPACE/SECRET_NAME
                - '--src_credentials=NAMESPACE/SRC_SECRET_NAME'
                - '--dst_credentials=NAMESPACE/DST_SECRET_NAME'
                # Point to the CA certificate Secret created in the destination namespace
                - '--src_ca_certificate_reference=NAMESPACE/CA_CERT_SECRET'
                - '--dst_ca_certificate_reference=NAMESPACE/CA_CERT_SECRET'
                - '--src_type=s3'
                - '--dst_type=s3'
                - '--bandwidth_limit=BANDWIDTH_LIMIT' # Optional. Examples: '10K', '100M', '1G'
          restartPolicy: OnFailure
    ---
    

#### Create a scheduled CronJob

Use this configuration to keep your destination bucket continuously synchronized with your source bucket on a fixed schedule.
    
    
    ---
    apiVersion: batch/v1
    kind: CronJob
    metadata:
      name: transfer-cronjob
      namespace: NAMESPACE
    spec:
      schedule: "0 * * * *"  # Runs at the top of every hour. Adjust the cron schedule as needed.
      concurrencyPolicy: Forbid
      successfulJobsHistoryLimit: 3
      failedJobsHistoryLimit: 5
      jobTemplate:
        spec:
          template:
            spec:
              serviceAccountName: transfer-service-account # The service account created in the previous step
              containers:
                - name: storage-transfer-pod
                  image: gcr.io/private-cloud-staging/storage-transfer:latest
                  imagePullPolicy: Always
                  command:
                    - /storage-transfer
                  args:
                    # The S3 endpoints for your source and destination
                    - '--src_endpoint=SRC_ENDPOINT'
                    - '--dst_endpoint=DST_ENDPOINT'
                    # The Fully Qualified Names (FQN) of the buckets
                    - '--src_path=SRC_BUCKET_FQN/'
                    - '--dst_path=DST_BUCKET_FQN/'
                    # Cross-namespace mapping: point directly to the live credentials using NAMESPACE/SECRET_NAME
                    - '--src_credentials=NAMESPACE/SRC_SECRET_NAME'
                    - '--dst_credentials=NAMESPACE/DST_SECRET_NAME'
                    # Point to the CA certificate Secret created in the destination namespace
                    - '--src_ca_certificate_reference=NAMESPACE/CA_CERT_SECRET'
                    - '--dst_ca_certificate_reference=NAMESPACE/CA_CERT_SECRET'
                    - '--src_type=s3'
                    - '--dst_type=s3'
                    - '--bandwidth_limit=BANDWIDTH_LIMIT' # Optional. Examples: '10K', '100M', '1G'
              restartPolicy: OnFailure
    ---
    

### Monitor your data transfer

After you instantiate the Job, you can monitor its status using `kubectl` commands, such as `kubectl describe`. To verify the transfer, list the objects inside of your destination bucket to validate that your data transferred. The data transfer tool is independent of the location of the endpoints involved in the transfer.

Run the following command to check the status of your workload:
    
    
    # If you created a one-time Job:
    kubectl describe job transfer-job -n NAMESPACE
    
    # If you created a scheduled CronJob:
    kubectl describe cronjob transfer-cronjob -n NAMESPACE
    

The preceding command tells you the status of the job.

The job prompts a pod to transfer the data. You can get the name of the pod and look at logs to see if there are any errors during the transfer.

To view pod logs, run the following:
    
    
    # 1. First, find the exact pod name generated by your Job
    kubectl get pods -n NAMESPACE | grep transfer
    
    # 2. Then, view the logs for that specific pod
    kubectl logs POD_NAME -n NAMESPACE
    

Successful job logs:
    
    
    DEBUG : Starting main for transfer
    I0607 21:34:39.183106       1 transfer.go:103]  "msg"="Starting transfer "  "destination"="sample-bucket" "source"="/data"
    2023/06/07 21:34:39 NOTICE: Bandwidth limit set to {100Mi 100Mi}
    I0607 21:34:49.238901       1 transfer.go:305]  "msg"="Job finished polling "  "Finished"=true "Number of Attempts"=2 "Success"=true
    I0607 21:34:49.239675       1 transfer.go:153]  "msg"="Transfer completed."  "AvgSpeed"="10 KB/s" "Bytes Moved"="10.0 kB" "Errors"=0 "Files Moved"=10 "FilesComparedAtSourceAndDest"=3 "Time since beginning of transfer"="1.0s"
    

Viewing logs lets you see the data transfer speed, which is not the same as bandwidth used, bytes moved, number of errored files, and files moved.

## Copy block storage to object storage

Ensure that you meet the following prerequisites:

  * An S3 endpoint with a S3 key ID and secret access key with at least WRITE permissions to the dedicated bucket that you want to transfer data to.
  * A working cluster with connectivity to the S3 endpoint.
  * Privileges to create Jobs and Secrets inside your cluster.
  * For replication of block storage, a Pod with an attached `PersistentVolumeClaim` (PVC) that you want to backup to object storage, and privileges to inspect running Jobs and PVCs.
  * For replication of the block storage, a window during which no writes take place to the `PersistentVolume` (PV).
  * For the restoration of block storage from an object storage endpoint, privileges to allocate a PV with sufficient capacity.



To replicate a PV to object storage, you must attach a volume to an existing Pod. During the window of the transfer, the Pod must not perform any writes. To avoid detaching the mounted PV from the Job, the data transfer process works by running the transfer Job on the same machine as the Pod, and using a hostPath mount to expose the volume on the disk. In preparation for the transfer, you must first find the node on which the Pod is running, and additional metadata such as the Pod UID and PVC type to reference the appropriate path on the Node. You must substitute this metadata into the sample YAML file outlined in the following section.

### Collect metadata

To collect the metadata required to create the data transfer Job, work through these steps:

  1. Find the Node that has the scheduled Pod:
         
         kubectl get pod POD_NAME -o jsonpath='{.spec.nodeName}'
         

Record the output of this command as the NODE_NAME to use in the data transfer Job YAML file.

  2. Find the Pod UID:
         
         kubectl get pod POD_NAME -o 'jsonpath={.metadata.uid}'
         

Record the output of this command as the POD_UID to use in the data transfer Job YAML file.

  3. Find the PVC name:
         
         kubectl get pvc www-web-0 -o 'jsonpath={.spec.volumeName}'
         

Record the output of this command as the PVC_NAME to use in the data transfer Job YAML file.

  4. Find the PVC storage provisioner:
         
         kubectl get pvc www-web-0 -o jsonpath='{.metadata.annotations.volume\.v1\.kubernetes\.io\/storage-provisioner}'
         

Record the output of this command as the PROVISIONER_TYPE to use in the data transfer Job YAML file.




### Create secrets

To replicate file to object storage across clusters, you must first instantiate the secrets inside your Kubernetes cluster. You must use matching keys for the Secret data for the tool to pull the credentials.

To perform the transfer in an existing namespace, see the following example of creating Secrets in a `transfer` namespace:
    
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: src-secret
      namespace: transfer
    data:
      access-key-id: c3JjLWtleQ== # echo -n src-key| base64 -w0
      access-key: c3JjLXNlY3JldA== # echo -n src-secret| base64 -w0
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: dst-secret
      namespace: transfer
    data:
      access-key-id: ZHN0LWtleQ== # echo -n dst-key| base64 -w0
      access-key: ZHN0LXNlY3JldA== # echo -n dst-secret| base64 -w0
    

### Create the Job

With the data that you collected in the previous section, create a Job with the data transfer tool. The data transfer Job has a `hostPath` mount referencing the path for the PV of interest, and a `nodeSelector` for the relevant node.

The following is an example of a data transfer Job:
    
    
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: transfer-job
      namespace: transfer
    spec:
      template:
        spec:
          nodeSelector: NODE_NAME
          serviceAccountName: data-transfer-sa
          containers:
          - name: storage-transfer-pod
            image: storage-transfer
            command:
            - /storage-transfer
            args:
            - --dst_endpoint=https://your-dst-endpoint.com
            - --src_path=/pvc-data
            - --dst_path=transfer-dst-bucket
            - --dst_credentials=transfer/dst-secret
            - --src_type=local
            - --dst_type=s3
          volumeMounts:
          - mountPath: /pvc-data
            name: pvc-volume
          volumes:
          - name: pvc-volume
          hostPath:
            path: /var/lib/kubelet/pods/POD_UID/volumes/PROVISIONER_TYPE/PVC_NAME
          restartPolicy: Never
    

As with the S3 data transfer, you must create a Secret containing the access keys for the destination endpoint in the Kubernetes cluster, and the data transfer Job must run with a service account with adequate privileges to read the Secret from the API server. Monitor the status of the transfer with standard `kubectl` commands operating on the Job.

Consider the following details when transferring block storage to object storage:

  * By default, symbolic links follow and replicate to the object storage, but a deep rather than shallow copy performs. Upon restoration, it destroys symlinks.
  * As with object storage replication, cloning into a subdirectory of the bucket is destructive. Ensure that the bucket is available exclusively for your volume.



### Restore from object storage to block storage

#### Allocate a PV

To restore block storage from an object storage endpoint, follow these steps:

  1. Allocate a persistent volume to target in the restore. Use a PVC to allocate the volume, as shown in the following example:
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: restore-pvc
           namespace: restore-ns
         spec:
           storageClassName: "default"
           accessModes:
         ReadWriteOnce
           resources:
             requests:
               storage: 1Gi # Need sufficient capacity for full restoration.
         

  2. Check the status of the PVC:
         
         kubectl get pvc restore-pvc -n restore-ns
         

After the PVC is in a `Bound` state, it is ready to consume inside the Pod that rehydrates it.

  3. If a Stateful set eventually consumes the PV, you must match the rendered StatefulSet PVCs. The Pods that StatefulSet produces consumes the hydrated volumes. The following example shows volume claim templates in a StatefulSet named `ss`.
         
         volumeClaimTemplates:
           - metadata:
               name: pvc-name
             spec:
               accessModes: [ "ReadWriteOnce" ]
               storageClassName: "default"
               resources:
                 requests:
                   storage: 1Gi
         

  4. Pre-allocate PVCs with names such as `ss-pvc-name-0` and `ss-pvc-name-1` to ensure that the resultant Pods consume the pre-allocated volumes.




#### Hydrate the PV

After the PVC is bound to a PV, start the Job to populate the PV:
    
    
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: transfer-job
      namespace: transfer
    spec:
      template:
        spec:
          serviceAccountName: data-transfer-sa
          volumes:
          - name: data-transfer-restore-volume
            persistentVolumeClaim:
              claimName: restore-pvc
          containers:
          - name: storage-transfer-pod
            image: storage-transfer
            command:
            - /storage-transfer
            args:
            - --src_endpoint=https://your-src-endpoint.com
            - --src_path=/your-src-bucket
            - --src_credentials=transfer/src-secret
            - --dst_path=/restore-pv-mnt-path
            - --src_type=s3
            - --dst_type=local
          volumeMounts:
          - mountPath: /restore-pv-mnt-path
            name: data-transfer-restore-volume
    

After the Job has finished running, the data from the object storage bucket populates the volume. A separate Pod can consume the data by using the same standard mechanisms for mounting a volume. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
