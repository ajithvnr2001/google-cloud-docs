---
url: https://docs.cloud.google.com/managed-lustre/docs/transfer-data/
title: Transfer data to or from Cloud Storage \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:57.501636+00:00
---

# Transfer data to or from Cloud Storage  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/transfer-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Transfer data to or from Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Managed Lustre can import data from, and export data to, [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction). Data transfers are incremental; they only copy files that don't already exist in the destination, or that have changed since they were transferred.

Cloud Storage buckets with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled provide faster transfer speeds to and from Managed Lustre compared to standard buckets.

## Performance

Transfers between Managed Lustre and Cloud Storage can reach the following speeds:

  * For files over 32 MB, up to 100 GBps. Transfer speed is limited by an instance's maximum throughput (instance capacity multiplied by [performance tier](https://docs.cloud.google.com/managed-lustre/docs/create-instance#performance-tiers)).



## Cloud Storage egress bandwidth considerations

Cloud Storage provides a default egress bandwidth of up to 200 Gbps per region per project. If you have multiple Managed Lustre instances in the same project and region, you can request an increase to the egress bandwidth limit. For more information, see the [Cloud Storage bandwidth quotas](https://docs.cloud.google.com/storage/quotas#bandwidth).

## Required permissions

### Permissions to initiate the transfer

The user or service account used for initiating the transfer requires the following permissions:

  * `lustre.instances.exportData` in order to transfer from Managed Lustre to Cloud Storage.
  * `lustre.instances.importData` in order to transfer from Cloud Storage.



Both of these permissions are granted with the `roles/lustre.admin` role. You can create a [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) to grant permissions independently.

### Permissions for the Managed Lustre service agent

Managed Lustre uses a [service agent](https://docs.cloud.google.com/managed-lustre/docs/access-control#service-agent) to access Cloud Storage buckets on your behalf. To perform transfers, you must grant the service agent access to the target bucket.

If you don't know your project's service agent identity, see [Create or retrieve the service agent identity](https://docs.cloud.google.com/managed-lustre/docs/access-control#get-service-agent).

#### Grant permissions

The Managed Lustre service agent requires one of the following [Cloud Storage roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles):

  * To transfer data to and from Cloud Storage: `roles/storage.objectUser` on the Cloud Storage bucket.
  * To only transfer from Cloud Storage: `roles/storage.objectViewer` on the Cloud Storage bucket.



To grant one of these roles:

###  Import and export 

Run the following `gcloud` command:
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
      --member=serviceAccount:SERVICE_AGENT_IDENTITY \
      --role=roles/storage.objectUser
    

###  Import only 

Run the following `gcloud` command:
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
      --member=serviceAccount:SERVICE_AGENT_IDENTITY \
      --role=roles/storage.objectViewer
    

Replace the following:

  * BUCKET_NAME: The name of your Cloud Storage bucket.
  * SERVICE_AGENT_IDENTITY: The Managed Lustre service agent identity (`service-<var>PROJECT_NUMBER</var>@gcp-sa-lustre.iam.gserviceaccount.com`).



## Import data to Managed Lustre

You can import data from a Cloud Storage bucket. The bucket can be in the same or a different project. The bucket can be in a different zone or region from your Managed Lustre instance, but inter-region transfers  
might be slower than intra-region transfers.

###  gcloud 
    
    
    gcloud lustre instances import-data INSTANCE_ID \
      --location=LOCATION \
      --gcs-path-uri=gs://BUCKET_NAME/ \
      --lustre-path=PS_PATH
    

Where:

  * INSTANCE_ID is your Managed Lustre instance name.
  * `--location` is the zone of your Managed Lustre instance. For example, `us-central1-a`.
  * `--gcs-path-uri` specifies the URI to a Cloud Storage bucket, or a path within a bucket, using the format `gs://<bucket_name>/<optional_path_inside_bucket>/`. If a path inside the bucket is specified, it must end with a forward slash (`/`).
  * `--lustre-path` specifies the root directory path to the Managed Lustre file system. Must start with `/`. Default is `/`. If specifying a value other than the default, the directory must already exist on the file system.



The following parameters are optional:

  * `--request-id` lets you assign a unique ID to this request. If you retry this request using the same request ID, the server will ignore the request if it has already been completed. Must be a valid [UUID](https://www.google.com/search?q=uuid+format) that is not all zeros.
  * `--async` returns a response immediately, without waiting for the operation to complete.



For more details, see the [Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/lustre/instances/import-data).

###  REST 
    
    
    POST https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID:importData
    Authorization: Bearer [YOUR_ACCESS_TOKEN]
    
    {
      "gcsPath" : {
        "uri" : "gs://BUCKET_NAME/"
      },
      "lustrePath" : {
        "path" : "/PATH"
      }
    }
    

Where:

  * PROJECT_ID is your Google Cloud project name.
  * LOCATION is the zone of your Managed Lustre instance. For example, `us-central1-a`.
  * INSTANCE_ID is your Managed Lustre instance name.
  * `gcsPath` contains a `uri` key whose value specifies the URI to a Cloud Storage bucket, or a path within a bucket, using the format `gs://<bucket_name>/<optional_path_inside_bucket>/`. If a path inside the bucket is specified, it must end with a forward slash (`/`).
  * `lustrePath` contains a `path` key whose value specifies the root directory path to the Managed Lustre file system. Must start with `/`. Default is `/`. If specifying a value other than the default, the directory must already exist on the file system.



To use your own service account instead of the Google-managed service agent, the request supports a `serviceAccount` field in the JSON object:
    
    
    "serviceAccount" : "projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_ID"
    

An example `curl` command looks like:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID:importData \
      -d '{"gcsPath": {"uri":"gs://BUCKET_NAME/"}, "lustrePath": {"path":"/"}}'
    

### File attributes

When you import data from a Cloud Storage bucket to a Managed Lustre instance, the file attributes in the Managed Lustre instance get set in one of two ways:

  * If the Cloud Storage object has custom metadata as described for exporting data, then: 
    * The file's UID, GID, mode, and `mtime` are set based on the object's custom metadata.
    * The file's `atime` is set to the same value as the `mtime`.
  * If the Cloud Storage object does not have the custom metadata, then: 
    * The file's UID and GID are set to 0 (`root`).
    * The file's mode is set to `rwxr-xr-x` (`755`).
    * The file's `atime` and `mtime` are set to the creation time of the Cloud Storage object.



In either case:

  * The `ctime` for a file is set to the time the file was written to the instance.
  * The `atime`, `ctime`, and `mtime` for a directory are set to the time the directory was created on the instance.



## Export data

You can export data from your Managed Lustre instance to a Cloud Storage bucket in the same or a different project. The bucket can be in a different zone or region from your Managed Lustre instance, but inter-region transfers might be slower than intra-region transfers.

###  gcloud 
    
    
    gcloud lustre instances export-data \
      INSTANCE_ID \
      --location=LOCATION \
      --gcs-path-uri="gs://BUCKET_NAME/" \
      --lustre-path="/"
    

Where:

  * INSTANCE_ID is your Managed Lustre instance name.
  * `--location` is the zone of your Managed Lustre instance. For example, `us-central1-a`.
  * `--gcs-path-uri` specifies the URI to a Cloud Storage bucket, or a path within a bucket, using the format `gs://<bucket_name>/<optional_path_inside_bucket>/`. If a path inside the bucket is specified, it must end with a forward slash (`/`).
  * `--lustre-path` specifies the root directory path to the Managed Lustre file system. Must start with `/`. Default is `/`.



The following parameters are optional:

  * `--request-id` lets you assign a unique ID to this request. If you retry this request using the same request ID, the server will ignore the request if it has already been completed. Must be a valid [UUID](https://www.google.com/search?q=uuid+format) that is not all zeros.
  * `--async` returns a response immediately, without waiting for the operation to complete.



###  REST 
    
    
    POST https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID:exportData
    Authorization: Bearer [YOUR_ACCESS_TOKEN]
    
    {
      "lustrePath" : {
        "path" : "/"
      },
      "gcsPath" : {
        "uri" : "gs://BUCKET_NAME/"
      }
    }
    

Where:

  * PROJECT_ID is your Google Cloud project name.
  * INSTANCE_ID is your Managed Lustre instance name.
  * LOCATION is the zone of your Managed Lustre instance. For example, `us-central1-a`.
  * `lustrePath` contains a `path` key whose value specifies the root directory path to the Managed Lustre file system. Must start with `/`. Default is `/`.
  * `gcsPath` contains a `uri` key whose value specifies the URI to a Cloud Storage bucket, or a path within a bucket, using the format `gs://<bucket_name>/<optional_path_inside_bucket>/`. If a path inside the bucket is specified, it must end with a forward slash (`/`).



To use your own service account instead of the Google-managed service agent, the request supports a `serviceAccount` field in the JSON object:
    
    
    "serviceAccount" : "projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_ID"
    

An example `curl` command looks like:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json"
      https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID:exportData \
      -d '{"lustrePath": {"path":"/"}, "gcsPath": {"uri":"gs://BUCKET_NAME/"}}'
    

### File attributes

When you export data from a Managed Lustre instance to a Cloud Storage bucket, the following file attributes are preserved as [custom metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-metadata) in Cloud Storage:

  * The file's UID is stored with the `goog-reserved-posix-uid` key.
  * The file's GID is stored with the `goog-reserved-posix-gid` key.
  * The file's numeric mode is stored with the `goog-reserved-posix-mode` key.
  * The file's `mtime` is stored with the `goog-reserved-file-mtime` key.



These custom metadata key names are the same as those used by [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation#posix_to) for transfers with POSIX file systems.

The following file attributes are not preserved:

  * Symlinks are not preserved.
  * Hard links are exported as separate Cloud Storage objects, resulting in multiple copies.
  * Lustre striping set explicitly using `lfs setstripe` or `lfs setdirstripe` is not preserved.
  * The `atime` and `ctime` of files is not preserved.
  * The `mtime` of directories is not preserved.
  * Empty directories are not preserved.



## Get operation

To see the status of an import or export operation, you'll need the operation ID. This ID is returned by the service when you make an import or export request, and uses the following format:

  * `operation-1234567890123-6127783ad26ea-88913969-02748053`




###  gcloud 
    
    
    gcloud lustre operations describe OPERATION_ID \
      --location=LOCATION
    

###  REST 
    
    
    GET https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID
    Authorization: Bearer [YOUR_ACCESS_TOKEN]
    

An example `curl` command looks like:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID
    

## Cancel operation

To cancel an import or export operation, you'll need the operation ID. This ID is returned by the service when you make an import or export request, and uses the following format:

  * `operation-1234567890123-6127783ad26ea-88913969-02748053`




###  gcloud 
    
    
    gcloud lustre operations cancel OPERATION_ID \
      --location=LOCATION
    

###  REST 
    
    
    POST https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID:cancel
    Authorization: Bearer [YOUR_ACCESS_TOKEN]
    

An example `curl` command looks like:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID:cancel
    

## Limitations

The following limitations apply:

  * Only one transfer operation per instance can be active at a time. Starting a second transfer before the first has completed returns the following error:
        
        ERROR: (gcloud.lustre.instances.export-data) ABORTED: unable to queue the operation
        




## Troubleshooting

When importing data from or exporting data to Cloud Storage, you might encounter transfer stalls, permission issues, or skipped files. Follow these steps to diagnose and resolve common data transfer issues.

### Transfer stalls or slow egress speeds

If an import or export operation stalls or runs significantly slower than expected, check the following:

  * **Cloud Storage egress bandwidth limits:** Cloud Storage enforces a default egress bandwidth quota of up to 200 Gbps per region per project. If multiple instances or high-throughput workloads are transferring data simultaneously, you might be bottlenecked by this quota. See [Cloud Storage bandwidth quotas](https://docs.cloud.google.com/storage/quotas#bandwidth) to request a quota increase.
  * **Instance throughput limits:** Transfer speeds are bounded by your instance's maximum throughput capacity (instance capacity multiplied by its performance tier). Verify your instance's performance tier to ensure it aligns with your performance expectations.



### Permission errors during transfer initiation

If starting a transfer fails with a permission denied or authorization error, verify the following IAM roles:

  * **User and service account permissions:** The identity initiating the transfer command must have `lustre.instances.importData` (for importing) or `lustre.instances.exportData` (for exporting). These are included in the `roles/lustre.admin` role.
  * **Service agent permissions:** The Google-managed Managed Lustre service agent (`service-<PROJECT_NUMBER>@gcp-sa-lustre...`) must have `roles/storage.objectViewer` (for imports) or `roles/storage.objectUser` (for exports) on the target Cloud Storage bucket. See [Grant permissions to the service agent](https://docs.cloud.google.com/managed-lustre/docs/transfer-data#sa-permissions) for detailed setup instructions.



### Skipped files or missing attributes

Managed Lustre data transfers are incremental; they only copy files that don't exist in the destination or have changed since the last transfer.

  * If files appear to be skipped, verify whether they were already successfully transferred previously and have not been modified.
  * When exporting data to Cloud Storage, POSIX metadata (UID, GID, mode, mtime) is preserved using custom metadata keys (e.g., `goog-reserved-posix-uid`). Note that symlinks, empty directories, and explicit PFL striping layouts are not preserved during export. See [Transfer data file attributes](https://docs.cloud.google.com/managed-lustre/docs/transfer-data#export-file-attributes) for full details.



### Inspecting failed transfer operations

If a transfer operation fails, retrieve the detailed error message and failure reason using the operation ID:
    
    
    gcloud lustre operations describe OPERATION_ID \
      --location=LOCATION
    

Review the `error` field in the operation output to determine whether the failure was caused by missing objects, network timeouts, or authentication.

### Unable to queue operation

If you see an error similar to any of the following when attempting to start an operation:
    
    
    ERROR: (gcloud.lustre.instances.import-data) ABORTED: unable to queue the operation
    ERROR: (gcloud.lustre.instances.export-data) ABORTED: unable to queue the operation
    ERROR: (gcloud.lustre.instances.update) ABORTED: unable to queue the operation
    

This error occurs when you attempt to start an operation while another operation of the same type is already in progress on the same instance.

  * **Import/export:** Managed Lustre supports only one active transfer operation per instance at a time. Queuing is not supported for transfer operations.
  * **Instance update:** Managed Lustre allows one active update per instance at a time, and allows an additional update operation to be queued.



To resolve this issue, wait for the current operation to complete before starting a new one.

### `FILESYSTEM_NO_SPACE_ON_DEVICE` errors

If your transfer returns a `FILESYSTEM_NO_SPACE_ON_DEVICE` error, even though monitoring tools indicate that aggregate free space is still available, you may be encountering OST imbalance, client space grants, or inode exhaustion. Refer to [`No space left on device` errors](https://docs.cloud.google.com/managed-lustre/docs/increase-capacity#enospc) for details and mitigation strategies.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
