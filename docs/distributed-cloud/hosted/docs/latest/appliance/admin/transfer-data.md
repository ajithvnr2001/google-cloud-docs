---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/transfer-data/
title: Transfer data \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:38.552307+00:00
---

# Transfer data  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/transfer-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Transfer data Stay organized with collections  Save and categorize content based on your preferences. 

The Google Distributed Cloud (GDC) air-gapped appliance device transfers arbitrary data to and from a Google Distributed Cloud air-gapped environment. Transfers can be started manually or set to automatically occur on a set interval.

Example transfers:

  * Download software updates or updated customer workloads
  * Upload customer data, device metrics, or device security, audit, and operations logs
  * Backup data snapshots



The storage-transfer tool transfers data and is distributed on an image for use in running containers on the cluster.

## Data sources

The storage-transfer tool allows flexibility with the operating conditions of GDC air-gapped appliance. S3 Compatible APIs can access externally exposed and internal storage targets. The tool also supports local file system and Cloud Storage sources.

The operator is responsible for maintaining control of access keys and any other credentials, secrets, or sensitive data required for authentication to connect GDC air-gapped appliance to external networks. The operator is also responsible for the configuration of the external network.

Refer to [create storage buckets](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-storage-buckets) for creating and accessing external storage.

### Local storage

Local storage is contained in the pod's container environment and includes the temporary file system or mounted volumes. The ServiceAccount bound to the pod must have access to all mount targets when mounting volumes.

### S3 storage

Network available storage is accessible through the S3 Compatible API. The service can be either external or only exposed within the cluster network. You must provide an accessible URL and standardized credentials mounted by using a Kubernetes Secret.

Multi-node and object storage defined data is accessed through the S3 API. See the relevant sections for setting up [multi-node storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/resources/multinode-storage) and [object storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/install-configure-storage-cli) within GDC air-gapped appliance.

### Cloud storage

You must provide an accessible URL and standardized credentials mounted by using a Secret.

If accessing a Cloud Storage bucket with uniform access controls, then you must set the `--bucket-policy-only` flag to `true`.

## Credentials

A Kubernetes Secret is required in order to use the storage-transfer service for either **S3** or **GCS** source or destination definitions. These can be provided with a remote service account or a user account.

When using Secrets in a Job or CronJob definition, the JobSpec must be attached to a Kubernetes ServiceAccount that has access to the Secrets.

Create a ServiceAccount that is used by the transfer, and then add permissions to the ServiceAccount to read and write secrets using roles and role bindings. You can choose not to create a ServiceAccount if your default namespace ServiceAccount or custom ServiceAccount already has permissions.
    
    
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
    

### Remote service accounts

**Important:** To access the URLs on this page, you must connect to the internet. The URLs are provided for use when you have such access.

To get Cloud Storage service account credentials to make a transfer, see <https://developers.google.com/workspace/guides/create-credentials#create_credentials_for_a_service_account>. These credentials must be stored in a secret in the `service-account-key` field.

Here is an example:
    
    
    apiVersion: v1
    data:
      service-account-key: BASE_64_ENCODED_VERSION_OF_CREDENTIAL_FILE_CONTENTS
    kind: Secret
    metadata:
      name: gcs-secret
      namespace: NAMESPACE
    type: Opaque
    

### User accounts

You can use a user account for authentication with S3-compatible buckets, not Cloud Storage buckets. You must specify the `--src_type` or `--dst_type` argument as `s3`.
    
    
    kubectl create secret -n NAMESPACE generic S3_CREDENTIAL_SECRET_NAME \
        --from-literal=access-key-id=ACCESS_KEY_ID
        --from-literal=access-key=ACCESS_KEY
    

Replace the following:

  * `NAMESPACE`: the name of the namespace in which you will create the Job definition.
  * `SECRET_NAME`: the name of the Secret you are creating.
  * `ACCESS_KEY_ID`: the value found in the **Access Key** field in the Google Cloud console. When configuring for Object Storage, this is called **access-key-id**.
  * `ACCESS_KEY`: the value found in the **Secret** field in the Google Cloud console. When configuring for Object Storage, this is the **secret-key** or Secret.



### Certificates

Provide certificates for validation in the job with a Kubernetes Secret containing a `ca.crt` data key.
    
    
      apiVersion: v1
      kind: Secret
      metadata:
        name: SRC_CERTIFICATE_SECRET_NAME
        namespace: NAMESPACE
      data:
        ca.crt : BASE_64_ENCODED_SOURCE_CERTIFICATE
      ---
      apiVersion: v1
      kind: Secret
      metadata:
        name: DST_CERTIFICATE_SECRET_NAME
        namespace: NAMESPACE
      data:
        ca.crt : BASE_64_ENCODED_DESTINATION_CERTIFICATE # Can be same OR different than source certificate.
    

Certificates can be provided by reference to the tool using the arguments `src_ca_certificate_reference` and `dst_ca_certificate_reference` in the format `NAMESPACE/SECRET_NAME`. For example:
    
    
    ...
          containers:
          - name: storage-transfer-pod
            image: gcr.io/private-cloud-staging/storage-transfer:latest
            command:
            - /storage-transfer
            args:
            ...
            - --src_ca_certificate_reference=NAMESPACE/SRC_CERTIFICATE_SECRET_NAME
            - --dst_ca_certificate_reference=NAMESPACE/DST_CERTIFICATE_SECRET_NAME
    

For **S3** storage in the appliance, you can directly use the `trust-store-root-ext` secret as the ca certificate. For example:
    
    
    containers:
          - name: storage-transfer-pod
            image: gcr.io/private-cloud-staging/storage-transfer:latest
            command:
            - /storage-transfer
            args:
            - --src_type=s3
            - --src_ca_certificate_reference=NAMESPACE/trust-store-root-ext
    

## Optional: Define a LoggingTarget to see logs in Loki

By default, logs from Jobs are only viewable in the Kubernetes resources and are not available in the observability stack and must be configured with a LoggingTarget to be viewable.
    
    
      apiVersion: logging.gdc.goog/v1alpha1
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
            - data-transfer-job # Choose the prefix here that matches your transfer job name
        serviceName: transfer-service
    

## Define a built-in Job

Users manage their own Job resources. For single-use data transfers, define a Job. The Job creates a Pod to run the storage-transfer container.

An example Job:
    
    
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: data-transfer-job
      namespace: NAMESPACE
    spec:
      template:
        spec:
          restartPolicy: Never
          serviceAccountName: transfer-service-account,
          containers:
          - name: storage-transfer-pod
            image: gcr.io/private-cloud-staging/storage-transfer:latest
            command:
            - /storage-transfer
            args:
            - --src_path=/src
            - --src_type=local
            - --dst_endpoint=https://your-dst-endpoint.com
            - --dst_credentials=NAMESPACE/CREDENTIAL_SECRET_NAME
            - --dst_path=/FULLY_QUALIFIED_BUCKET_NAME/BUCKET_PATH
            - --dst_type=gcs
            - --bucket_policy_only=true
            - --bandwidth_limit=10M #Optional of the form '10K', '100M', '1G' bytes per second
            volumeMounts:
            - mountPath: /src
              name: data
          volumes:
          - name: data
            persistentVolumeClaim:
              claimName: data-transfer-source
    

## Define a built-in CronJob

Users manage their own defined CronJob resources. Using a built-in CronJob allows for regularly scheduled data transfers.

An example CronJob that achieves an automated data transfer:
    
    
    apiVersion: batch/v1
    kind: CronJob
    metadata:
      name: data-transfer-cronjob
      namespace: NAMESPACE
    spec:
      schedule: "* * * * *"
      concurrencyPolicy: Forbid
      jobTemplate:
        spec:
          template:
            spec:
              serviceAccountName: transfer-service-account
              containers:
              - name: storage-transfer-pod
                image: gcr.io/private-cloud-staging/storage-transfer:latest
                command:
                - /storage-transfer
                args:
                - --src_path=LOCAL_PATH
                - --src_type=local
                - --dst_endpoint=https://your-dst-endpoint.com
                - --dst_credentials=NAMESPACE/CREDENTIAL_SECRET_NAME
                - --dst_path=/FULLY_QUALIFIED_BUCKET_NAME/BUCKET_PATH
                - --dst_type=gcs
                - --bucket_policy_only=true
                volumeMounts:
                - mountPath: LOCAL_PATH
                  name: source
              restartPolicy: Never
              volumes:
              - name: source
                persistentVolumeClaim:
                  claimName: data-transfer-source
    

Google recommends setting `concurrencyPolicy` to `Forbid` to prevent data contention. The CronJob, Secret, and PersistentVolumeClaim must be in the same namespace.

## Prioritize data jobs

Setting priority on data jobs can be achieved in a number of ways that are not mutually exclusive. You can set less frequent job schedules in the CronJob definition.

Jobs can also be ordered by using InitContainers (<https://kubernetes.io/docs/concepts/workloads/pods/init-containers/>) which always run in order of definition. However, all containers must run successfully. Use InitContainers to give higher priority to one job, or manage data contention by defining two or more InitContainers with mirrored source and destination definitions.

An example `jobTemplate` that achieves ordered data transfer:
    
    
    apiVersion: batch/v1
    kind: CronJob
    metadata:
      name: ordered-data-transfer-cronjob
      namespace: NAMESPACE
    spec:
      schedule: "* * * * *"
      concurrencyPolicy: Forbid
      jobTemplate:
        spec:
          template:
            spec:
              containers:
              - name: job-complete
                image: whalesay
                command: ["sh", "-c", "echo Job Completed."]
              initContainers:
              - name: A-to-B
                image: gcr.io/private-cloud-staging/storage-transfer:latest
                command: [/storage-transfer]
                args:
                - --src_type=s3
                - --src_endpoint=ENDPOINT_A
                - --src_path=/example-bucket
                - --src_credentials=NAMESPACE/CREDENTIAL_SECRET_NAME
                - --src_ca_certificate_reference=NAMESPACE/SRC_CERTIFICATE_SECRET_NAME
                - --dst_type=s3
                - --dst_endpoint=ENDPOINT_B
                - --dst_credentials=NAMESPACE/CREDENTIAL_SECRET_NAME
                - --dst_ca_certificate_reference=NAMESPACE/DST_CERTIFICATE_SECRET_NAME
                - --dst_path=/example-bucket
              - name: B-to-A
                image: gcr.io/private-cloud-staging/storage-transfer:latest
                command: [/storage-transfer]
                args:
                - --src_type=s3
                - --src_endpoint=ENDPOINT_B
                - --src_credentials=NAMESPACE/CREDENTIAL_SECRET_NAME
                - --src_ca_certificate_reference=NAMESPACE/SRC_CERTIFICATE_SECRET_NAME
                - --src_path=/example-bucket
                - --dst_type=s3
                - --dst_endpoint=ENDPOINT_A
                - --dst_credentials=NAMESPACE/CREDENTIAL_SECRET_NAME
                - --dst_ca_certificate_reference=NAMESPACE/DST_CERTIFICATE_SECRET_NAME
                - --dst_path=/example-bucket
    

Container `A-to-B` runs before `B-to-A`. This example achieves both a bisync and job ordering.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
