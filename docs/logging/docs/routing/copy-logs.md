---
url: https://docs.cloud.google.com/logging/docs/routing/copy-logs/
title: Batch and route log entries retroactively \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:03.536089+00:00
---

# Batch and route log entries retroactively  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/routing/copy-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Batch and route log entries retroactively Stay organized with collections  Save and categorize content based on your preferences. 

You can copy stored log entries from Cloud Logging log buckets to Cloud Storage buckets to support security audits, perform custom data analysis, or archive historical log entries. The copy operation is non-destructive; log entries remain in the source log bucket, and you can copy across different Google Cloud projects.

Copy operations route existing log entries retroactively by using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). In contrast, [sinks](https://docs.cloud.google.com/logging/docs/routing/overview#sinks) route matching log entries automatically in real time as they arrive, but cannot route log entries that were stored before the sink was created.

## Limitations

The following limitations apply when copying log entries:

  * You can copy log entries only to Cloud Storage buckets; other destinations aren't available.

  * You can't copy log entries from log buckets that have [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/logging/docs/routing/managed-encryption) configured.




## Before you begin

Before you get started with copying log entries, do the following:

  * Verify that you're using the latest version of the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). For instructions about how to install or update the gcloud CLI, see [Managing Google Cloud CLI components](https://docs.cloud.google.com/sdk/docs/components).


  * To get the permissions that you need to copy log entries, ask your administrator to grant you the following IAM roles on the project that contains the log bucket you are copying from: 

    * To run a copy operation: [Logging Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.admin) (`roles/logging.admin`) 
    * To view and manage the status of a copy operation: [Logs Configuration Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.configWriter) (`roles/logging.configWriter`) 



  * To get the permissions that you need to write log entries to Cloud Storage, ask your administrator to grant you the [Storage Object Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectCreator) (`roles/storage.objectCreator`) IAM role on the project that contains the Cloud Storage bucket. 




## Copy log entries

Logging only copies log entries that are stored in the log bucket when the copy operation starts. Log entries that are stored in log buckets after the copy operation starts don't get copied to Cloud Storage.

To copy log entries to Cloud Storage, you need to know the following information:

  * The ID and location of the log bucket you're copying from. To retrieve the log bucket ID and its location, use the gcloud CLI command [`gcloud logging buckets list`](https://docs.cloud.google.com/logging/docs/buckets#listing-log-buckets).
  * The name of the Cloud Storage bucket you're copying to. For information about how to retrieve the Cloud Storage bucket name, see [Getting Cloud Storage bucket information](https://docs.cloud.google.com/storage/docs/getting-bucket-metadata).
  * A [filter](https://docs.cloud.google.com/logging/docs/view/logging-query-language) for the log entries you want to copy.



To copy log entries, run the [`gcloud logging copy`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/copy) command:
    
    
    gcloud logging copy LOG_BUCKET_ID storage.googleapis.com/CLOUD_STORAGE_BUCKET_NAME \
    --location=LOCATION --log-filter='FILTER' --project=PROJECT_ID
    

Before you run the previous command, do the following:

  * Replace LOG_BUCKET_ID with the name of your log bucket.
  * Replace CLOUD_STORAGE_BUCKET_NAME with the name of your Cloud Storage bucket.
  * Replace LOCATION with the location of the log bucket.
  * (Optional): Replace FILTER with the filter that defines which log entries are copied.

If you omit the `--log-filter` flag, then all log entries in the log bucket are copied to the Cloud Storage bucket.

**Note:** The copy command cannot copy log entries whose retention has expired.
  * Replace PROJECT_ID with your Google Cloud project ID. You can omit this flag when the active gcloud CLI configuration is set to the correct Google Cloud project.




Example command:
    
    
    gcloud logging copy my-log-bucket storage.googleapis.com/my-gcs-bucket \
    --location=global --log-filter='timestamp > "2024-07-18T10:00:00.0Z"' \
    --project=my-project
    

This command creates a [long-running operation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning) to run in the background and returns the name of the copy operation and the location of the log bucket:
    
    
    name: projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID
    

The location of the copy operation is the same as the location of the log bucket that you are copying from.

## View and manage copy operations

You can view and manage your copy operations by using the [`gcloud logging operations`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/operations) commands, which let you list, view, and cancel operations.

The following commands require that you specify the location of the operation. Use the location of your log bucket. For information about how to find the location of your log bucket, see [View a bucket's details](https://docs.cloud.google.com/logging/docs/buckets#viewing-logs-buckets).

### List copy operations

You can list recent copy operations, including scheduled, running, completed, failed, and canceled operations. Recent copy operations appear in the results for up to 30 days after the end time.

To list copy operations, run the following command:
    
    
    gcloud logging operations list --location=LOCATION \
    --operation-filter=request_type=CopyLogEntries \
    --project=PROJECT_ID
    

Before you run the previous command, do the following:

  * Replace LOCATION with the location of the log bucket that you are copying from.
  * Replace PROJECT_ID with your Google Cloud project ID.



The command returns information about the long-running operation, including the operation ID:
    
    
    projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID
    

### View the status of a copy operation

You can retrieve the status and other metadata about copy operations, including the following:

  * `startTime`: The timestamp indicating the creation of the operation.
  * `endTime`: The timestamp indicating the completion of the operation.
  * `state`: The status of the operation (scheduled, running, canceled, failed, or succeeded).
  * `cancellation`: Whether the user has requested to cancel the operation.
  * `progress`: Estimated progress of the operation (0-100%).
  * `destination`: The name of the Cloud Storage bucket to which the operation is copying log entries.
  * `filter`: The filter specifying which log entries to copy.
  * `name`: The name of the log bucket from which the operation is copying log entries.
  * `logEntriesCopiedCount`: The number of log entries successfully copied to the Cloud Storage bucket by the operation.



Note that not all of the listed metadata fields apply to every copy operation. For example, if a copy operation is still running, the `endTime` metadata doesn't apply to the operation. As another example, if the `--log-filter=FILTER` flag wasn't used when running the `gcloud logging copy` command, then the `filter` metadata doesn't apply to the operation.

To retrieve information about a copy operation, run the following command:
    
    
    gcloud logging operations describe OPERATION_ID \
    --location=LOCATION --project=PROJECT_ID
    

Before you run the previous command, do the following:

  * Replace OPERATION_ID with the ID of the operation.
  * Replace LOCATION with the location of the log bucket that you are copying from.
  * Replace PROJECT_ID with your Google Cloud project ID.



The command returns metadata about the copy operation. For example, here is an output for an operation that is in progress:
    
    
    done: false
    metadata:
      `@type`: type.googleapis.com/google.logging.v2.CopyLogEntriesMetadata
      progress: 75
      destination: storage.googleapis.com/CLOUD_STORAGE_BUCKET_NAME
      source: projects/PROJECT_ID/locations/LOCATION/buckets/LOG_BUCKET_ID
      verb: copy
      startTime: `2024-05-23T10:52:40.039751Z`
      state: OPERATION_STATE_RUNNING
    name: projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID
    

**Note:** If the copy operation is in a `PENDING` state, then the operation is waiting for quota. For information about quotas, see [Cloud Logging API quotas](https://docs.cloud.google.com/logging/quotas#api-limits).

### Cancel a copy operation

You can cancel an in-progress copy operation. If you cancel a copy operation, all log entries that were copied before the operation was canceled remain in the Cloud Storage bucket.

After canceling a copy operation, Logging completes all ongoing processes before it completes the cancellation. This might result in some log entries still being copied to Cloud Storage after you cancel the operation.

To cancel a copy operation, run the following command:
    
    
    gcloud logging operations cancel OPERATION_ID \
    --location=LOCATION --project=PROJECT_ID
    

Before you run the previous command, do the following:

  * Replace OPERATION_ID with the ID of the operation.
  * Replace LOCATION with the location of the log bucket that you are copying from.
  * Replace PROJECT_ID with your Google Cloud project ID.



## View log entries in Cloud Storage

For information about how to view and understand the log entries that you copied to Cloud Storage, see [View log entries routed to Cloud Storage](https://docs.cloud.google.com/logging/docs/export/storage).

## Quotas and limits

All copy operations take at least an hour to complete, no matter the amount of data that is being copied.

To copy a large volume—for example, petabytes—split the copying across multiple copy operations by using the `timestamp` field in the `--log-filter` flag.

The copy command cannot copy log entries whose retention has expired.

## Troubleshooting

This section describes how to troubleshoot errors when copying log entries.

### Failed to write export data

When you view the status of a copy operation by using `gcloud logging operations describe`, the operation might display the following error:
    
    
    done: true
    error:
      code: 7
      message: Failed to write export data to the destination Cloud Storage bucket.
    

This error occurs when Logging is unable to write or finalize log files in the destination Cloud Storage bucket. Writing exported files during the operation can fail for several reasons:

  * A VPC Service Controls service perimeter blocks requests to the destination Cloud Storage bucket.
  * The IAM permissions of the account that initiated the copy operation were modified or revoked while the operation was running.
  * The copy operation ran long enough for the authorization credentials to expire.
  * The destination Cloud Storage bucket uses CMEK, and the Cloud Key Management Service key is disabled or the Cloud Storage service agent lacks encryption permissions.
  * A write retry attempts to overwrite an existing file that cannot be replaced. For example, if an export batch is retried after a transient delay, or if a copy operation is restarted, then the retry might attempt to overwrite a file that was already created. If that file is protected by an active object hold or a locked retention policy, then Cloud Storage rejects the overwrite.
  * The destination bucket was deleted, entered a locked state, or the project exceeded its resource quota.



To resolve this issue, do the following:

  1. **Review VPC Service Controls:** If your organization uses VPC Service Controls, then review Cloud Audit Logs for perimeter denials (`cloudaudit.googleapis.com/data_access`). The perimeter for the destination Cloud Storage bucket must permit access from the project running the copy operation, or configure an ingress and egress rule.

  2. **Verify destination bucket IAM roles:** The account that initiated the copy operation must have the [Storage Object Creator](https://docs.cloud.google.com/storage/docs/access-control/iam) (`roles/storage.objectCreator`) role on the destination bucket.

  3. **Verify Customer-Managed Encryption Keys (CMEK):** If the destination bucket uses CMEK for default encryption, then verify that the Cloud KMS key is enabled and that the Cloud Storage service agent has the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#cryptoKey) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) role on the key.

  4. **Divide large copy operations into shorter time intervals:** To prevent timeouts or credential expiration when copying large volumes of log entries, divide the operation into smaller batches. To split the log entries into batches, use the `timestamp` field in the `--log-filter` flag.

  5. **Verify that no object holds or retention conflicts exist:** Verify that the destination bucket does not contain objects at the target destination path that are protected by an active [object hold](https://docs.cloud.google.com/storage/docs/object-holds) or a locked [retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock).




## Pricing

For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page. If you route log data to other Google Cloud services, then see the following documents:

  * [Cloud Storage pricing](https://cloud.google.com/storage/pricing)
  * [BigQuery pricing](https://cloud.google.com/bigquery/pricing#data_ingestion_pricing)
  * [Pub/Sub pricing](https://cloud.google.com/pubsub/pricing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
