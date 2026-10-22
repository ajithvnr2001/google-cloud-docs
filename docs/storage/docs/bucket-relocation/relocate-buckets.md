---
url: https://docs.cloud.google.com/storage/docs/bucket-relocation/relocate-buckets/
title: Relocate buckets \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:18.373087+00:00
---

# Relocate buckets  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/bucket-relocation/relocate-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Relocate buckets Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the process for relocating buckets from one location to another. For information about bucket relocation, see [Bucket relocation](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview).

## Before you begin

Before you can relocate buckets, complete the following steps:

  1. [Configure Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/configure-and-manage-storage-intelligence#configure-storage-intelligence).

  2. [Determine the bucket relocation type](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview#relocation-types) to understand whether write downtime is required.

  3. If your bucket relocation involves write downtime, [enable soft delete](https://docs.cloud.google.com/storage/docs/bucket-relocation/plan-bucket-relocation#enable-soft-delete).

  4. [Check the quotas and limits](https://docs.cloud.google.com/storage/docs/bucket-relocation/plan-bucket-relocation#check-quotas-and-limits) to verify that the new location has sufficient quotas to accommodate the bucket's data.

  5. Review the bucket relocation [limitations](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview#limitations).

  6. [Remove any existing bucket tags](https://docs.cloud.google.com/storage/docs/bucket-relocation/plan-bucket-relocation#unsupported-features).

  7. If you use inventory reports, [save your configurations](https://docs.cloud.google.com/storage/docs/insights/using-inventory-reports).

  8. Get required roles, which are described in the following section.




### Get required roles

To get the permissions that you need to relocate buckets, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to relocate buckets. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to relocate buckets:

  * To relocate a bucket: `storage.buckets.relocate`
  * To view the status of a bucket relocation operation: `storage.bucketOperations.get`
  * To view the list of bucket relocation operations for a project: `storage.bucketOperations.list`
  * To cancel a bucket relocation operation: `storage.bucketOperations.cancel`
  * To view the metadata of a bucket during the dry run and bucket relocation phases: `storage.buckets.get`
  * To get an object in a bucket you want to relocate: `storage.objects.get`
  * To list the objects in a bucket you want to relocate: `storage.objects.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Relocate buckets

This section describes the process of relocating Cloud Storage buckets from one location to another.

To relocate a bucket, complete the following steps:

  1. Test the bucket relocation with a dry run (Optional)

  2. Initiate the bucket relocation process

  3. Initiate the final synchronization step




For more information about these steps, see [Understand the bucket relocation process](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview#bucket-relocation-process).

### Test the bucket relocation with a dry run (Optional)

To minimize potential issues during the bucket relocation process, we recommend you perform a dry run to test the end-to-end process. A dry run simulates the bucket relocation process without moving data, helping you to catch and resolve issues early on. The dry run checks for the following incompatibilities:

  * [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) or [Customer-supplied encryption keys (CSEK)](https://docs.cloud.google.com/docs/security/encryption/customer-supplied-encryption-keys)
  * [Bucket](https://docs.cloud.google.com/storage/docs/bucket-lock#retention-policy) and [object](https://docs.cloud.google.com/storage/docs/object-lock) retention policies
  * Objects with [temporary holds](https://docs.cloud.google.com/storage/docs/object-holds)
  * [Multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads)



While a dry run can't identify every possible issue as some issues might only surface during the live migration due to factors such as real-time resource availability, it reduces the risk of facing time-consuming issues during the actual relocation.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket you want to relocate.
  3. On the **Bucket details** page, click the **Configuration** tab.
  4. In the **Overview** section, click edit **Edit** next to the **Location** field.
  5. On the **Relocate bucket** page, enter your bucket's new location. After each of the following steps, click **Continue** to proceed to the next step: 
     1. In the **Confirm the bucket you plan to relocate** section, review the bucket and its location.
     2. In the **Before you continue** section, review configurations that block the relocation. If a restriction applies to your bucket, consider [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) as an alternative workaround.
     3. In the **Choose where to relocate your bucket** section, do the following:

        1. Select a [location type](https://docs.cloud.google.com/storage/docs/locations). 
        2. Select a [location](https://docs.cloud.google.com/storage/docs/locations#available-locations) where object data within your bucket will be stored.

Based on the source and destination location, you'll be informed if a write downtime is required. For information about the types of relocation and downtime, see [Relocation types](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview#relocation-types).

     4. In the **Choose how you'd like to proceed** section, click **Start with a dry run (recommended)**. A dry run simulates the relocation to identify potential issues without moving data.
     5. Click **Continue**. 
  6. Click **Start**.
  7. On the **Start with a dry run** confirmation dialog, review the message that appears and click **Start dry run**.



After you initiate a dry run, a [long-running operation](https://docs.cloud.google.com/storage/docs/using-long-running-operations) starts. You can monitor the progress in the **Operations** tab of the **bucket details** page.

### Command line

To initiate a dry run, run the [`gcloud storage buckets relocate`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/relocate) command with the `--dry-run` flag:
    
    
    gcloud storage buckets relocate gs://BUCKET_NAME --location=LOCATION --dry-run

Where:

  * `BUCKET_NAME` is the name of the bucket that you want to relocate.

  * `LOCATION` is the destination location of the bucket.




After you initiate a dry run, a [long-running operation](https://google.aip.dev/151) starts. You'll receive an operation ID and a description of the operation. Track the progress and completion of the dry run by [getting the details of the long-running operation](https://docs.cloud.google.com/storage/docs/using-long-running-operations#command-line).

If the dry run reveals any issues, address them before proceeding with the relocation step.

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the settings for the bucket, which must include the `destinationLocation` and `validateOnly` parameters. See the [`Buckets: relocate`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/relocate) documentation for a complete list of settings. The following are common settings to include:
         
         {
           "destinationLocation": "DESTINATION_LOCATION",
           "destinationCustomPlacementConfig": {
             "dataLocations": [
               LOCATIONS,
                 ...
                 ]
             },
           "validateOnly": "true"
           }

Where:

     * `DESTINATION_LOCATION` is the destination location of the bucket.
     * `LOCATIONS` is a list of location codes to be used for the [configurable dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr).
     * `validateOnly` is set to `true` to perform a dry run.
  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api):
         
         curl -X POST --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/relocate"

Where:

     * `JSON_FILE_NAME` is the name of the JSON file you created.
     * `BUCKET_NAME` is the name of the bucket you want to relocate.

After you initiate a dry run, a [long-running operation](https://google.aip.dev/151) starts. The dry run succeeds when the following conditions are met:

     * The dry run reports no errors.
     * The `operations` resource returns a `done` field value of `true`.
           
           {
           "kind": "storage#operation",
           "name": "projects/_/buckets/bucket/operations/operation_id",
           "metadata": {
             "@type": OperationMetadataType*,
             metadata OperationMetadata*
           },
           "done": "true",
           "response": {
                 "@type": ResponseResourceType*,
                 response ResponseResource*
               }
             }

If the dry run reveals any issues, address them before proceeding with the Initiate the relocation step.




### Initiate the bucket relocation

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket you want to relocate.
  3. On the **Bucket details** page, click the **Configuration** tab.
  4. In the **Overview** section, click edit **Edit** next to the **Location** field.
  5. On the **Relocate bucket** page, enter your bucket's new location. After each of the following steps, click **Continue** to proceed to the next step: 
     1. In the **Confirm the bucket you plan to relocate** section, review the bucket and its location.
     2. In the **Before you continue** section, review configurations that block the relocation. If a restriction applies to your bucket, consider [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview) as an alternative workaround.
     3. In the **Choose where to relocate your bucket** section, do the following:

        1. Select a [location type](https://docs.cloud.google.com/storage/docs/locations). 
        2. Select a [location](https://docs.cloud.google.com/storage/docs/locations#available-locations) where object data within your bucket will be stored.

Based on the source and destination location, you'll be informed if a write downtime is required. For information about the types of relocation and downtime, see [Relocation types](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview#relocation-types).

     4. In the **Choose how you'd like to proceed** section, click **Relocate now**.
     5. Click **Continue**.
  6. To start the relocation process, click **Start**.
  7. On the **Relocate now** confirmation dialog, review the message that appears and click **Start relocate**.



After you start the relocation process, a [long-running operation](https://docs.cloud.google.com/storage/docs/using-long-running-operations) starts. You can monitor the progress in the **Operations** tab of the **bucket details** page.

### Command line

To initiate the bucket relocation, run the [`gcloud storage buckets relocate`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/relocate) command:
    
    
    gcloud storage buckets relocate gs://BUCKET_NAME --location=LOCATION

Where:

  * `BUCKET_NAME` is the name of the bucket that you want to relocate.

  * `LOCATION` is the destination location of the bucket.

**Note:** When creating a [configurable dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr), you must set the `--location` flag to be the _location code_ associated with the underlying regions, and you must use the [`--placement` flag](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create#--placement) with a valid pair of regions. For example, `--location=US --placement=US-CENTRAL1,US-EAST1`



### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the settings for the bucket. See the [`Buckets: relocate`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/relocate) documentation for a complete list of settings. The following are common settings to include:
         
         {
           "destinationLocation": "DESTINATION_LOCATION",
           "destinationCustomPlacementConfig": {
           "dataLocations": [
             LOCATIONS,
             ...
             ]
             },
           "validateOnly": "false"
           }

Where:

     * `DESTINATION_LOCATION` is the destination location of the bucket.
     * `LOCATIONS` is a list of location codes to be used for the [configurable dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr).
     * `validateOnly` is set to `false` to initiate the bucket relocation.
  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api):
         
         curl -X POST --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/relocate"

Where:

     * `JSON_FILE_NAME` is the name of the JSON file you created.
     * `BUCKET_NAME` is the name of the bucket you want to relocate.



#### Monitor the relocation process

### Console

To monitor the progress of the dry run or the relocation process, complete the following steps:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that you are relocating.

  3. On the **Bucket details** page, click the **Operations** tab.

  4. In the list of bucket operations that appear, click the dry run or the relocation operation to view its details.




The operation details page displays the relocation summary, key metrics, and an error summary.

### Command line

After you initiate a bucket relocation, a [long-running operation](https://google.aip.dev/151) starts. You'll receive an operation ID and a description of the operation. Track the progress and completion of the relocation process by [getting the details of the long-running operation](https://docs.cloud.google.com/storage/docs/using-long-running-operations#command-line).

### JSON API

Bucket relocation is a [long-running operation](https://google.aip.dev/151) that requires monitoring. To check the process status, regularly review the long-running operation details. For information about how to check the relocation process status, see [Get details of a long-running operation](https://docs.cloud.google.com/storage/docs/using-long-running-operations#rest-apis).

The following example shows the output generated by a relocation operation:
    
    
      done: false
      kind: storage#operation
      metadata:
      '@type': type.googleapis.com/google.storage.control.v2.RelocateBucketMetadata
      commonMetadata:
        createTime: '2024-10-21T04:26:59.666Z
        endTime: '2024-12-29T23:39:53.340Z'
        progressPercent: 99
        requestedCancellation: false
        type: relocate-bucket
        updateTime: '2024-10-21T04:27:03.2892'
      destinationLocation: US-CENTRAL1
      finalizationState: 'READY'
      progress:
        byteProgressPercent: 100
        discoveredBytes: 200
        remainingBytes: 0
        discoveredObjectCount: 10
        remainingObjectCount: 8
        objectProgressPercent: 100
        discoveredSyncCount: 8
        remainingSyncCount: 0
        syncProgressPercent: 100
      relocationState: SYNCING
      sourceLocation: US
      validateOnly: false
      estimatedWriteDowntimeDuration: '7200s'
      writeDowntimeExpireTime: '2024-12-30T10:34:01.786Z'
      name: projects//buckets/my-bucket1/operations/Bar7-1b0khdew@nhenUQRTF_R-Kk4dQ5V1f8fzezkFcPh3XMvlTqJ6xhnqJ1h_QXFIeAirrEqkjgu4zPKSRD6WSSG5UGXil6w
      response:
        '@type': type.googleapis.com/google.storage.control.v2.RelocateBucketResponse
          selfLink: https://storage.googleusercontent.com/storage/v1_ds/b/my-bucket1/operations/Bar7-1b0khdew@nhenUQRTF_R-Kk4dQ5V1f8fzezkFcPh3XMvlTqJ6xhnqJ1h_QXFIeAirrEqkjgu4zPKSRD6WSSG5UGXil6w
    

The following table provides information about the key fields in the output generated by the relocation operation:

Field name | Description | Possible values  
---|---|---  
`done` | Indicates the completion of the bucket relocation operation.  | `true`, `false`  
`kind` | Indicates that this resource represents a storage operation.  |   
`metadata` | Provides information about the operation.  |   
`metadata.@type` | Indicates the type of operation as bucket relocation.  |   
`metadata.commonMetadata` | Metadata common to all operations.  |   
`metadata.commonMetadata.createTime` | The time the long-running operation was created.  |   
`metadata.commonMetadata.endTime` | The time the long-running operation ended.  |   
`metadata.commonMetadata.progressPercent` | The estimated progress of the long-running operation, in percentage. | Between `0` to `100`%. A value of `-1` means that the progress is unknown or not applicable.  
`metadata.commonMetadata.requestedCancellation` | Indicates whether the user has requested cancellation of the long-running operation.  | `true`, `false`  
`metadata.commonMetadata.type` | Indicates the type of the long-running operation.  |   
`metadata.commonMetadata.updateTime` | The time the long-running operation was last updated. |   
`metadata.destinationLocation` | The destination location of the bucket. |   
`metadata.finalizationState` | Indicates the readiness for [initiating the final synchronization step](https://docs.cloud.google.com/storage/docs/bucket-relocation/relocate-buckets#initiate-final-sync). | 

  * `READY`: Indicates that you can initiate the final synchronization step. However, we recommend you wait until the value of the `progressPercent` field reaches `99`.
  * `WAITING_ON_SYNC`: Indicates that you cannot initiate the final synchronization step.
  * `NOT_REQUIRED`: Indicates that the final synchronization step isn't necessary for this bucket and you can skip it.
  * `BLOCKED_ON_ERRORS`: Indicates that the finalization step is temporarily paused due to errors. You'll need to resolve the errors to proceed with the step.
  * `RUNNING`: Indicates that the finalization step is in progress.
  * `FINALIZED`: Indicates that the finalization step has completed successfully.

  
`metadata.progress` | Progress details of the relocation operation. |   
`metadata.progress.byteProgressPercent` | Progress of bytes copied in percentage. | Between `0` to `100`%. A value of `-1` means that the progress is unknown or not applicable.  
`metadata.progress.discoveredBytes` | Number of bytes discovered in the source bucket. |   
`metadata.progress.discoveredObjectCount` | Number of objects discovered in the source bucket. |   
`metadata.progress.discoveredSyncCount` | Number of object metadata updates discovered in the source bucket. |   
`metadata.progress.objectProgressPercent` | Progress of objects copied in percentage. | Between `0` to `100`%. A value of `-1` means that the progress is unknown or not applicable.  
`metadata.progress.remainingBytes` | Number of bytes remaining to be copied from the source bucket to the destination bucket. |   
`metadata.progress.remainingObjectCount` | Number of objects remaining to be copied from the source bucket to the destination bucket. |   
`metadata.progress.remainingSyncCount` | Number of remaining object metadata updates to be synced. |   
`metadata.progress.syncProgressPercent` | Progress of object metadata updates to be synced in percentage. | Between `0` to `100`%. A value of `-1` means that the progress is unknown or not applicable.  
`metadata.relocationState` | Overall state of the bucket relocation operation. | 

  * `SYNCING`: Indicates that the bucket relocation step is actively copying objects from the source bucket to the destination bucket.
  * `FINALIZING`: Indicates that the finalization step has been initiated.
  * `FAILED`: Indicates that the bucket relocation step encountered an error and did not complete successfully.
  * `SUCCEEDED`: Indicates that the bucket relocation step has completed successfully.
  * `CANCELLED`: Indicates that the bucket relocation step was canceled.

  
`metadata.sourceLocation` | The source location of the bucket. |   
`metadata.validateOnly` | Indicates if a [dry run](https://docs.cloud.google.com/storage/docs/bucket-relocation/relocate-buckets#dry-run) of the bucket relocation has been initiated. | `true`, `false`  
`metadata.estimatedWriteDowntimeDuration` | The estimated write downtime duration; populated once the `finalizationState` is `READY`. | Minimum value is `7200s`.  
`metadata.writeDowntimeExpireTime` | The time the write downtime expires. |   
`name` | The unique identifier for this relocation operation.  
Format: `projects/_/buckets/bucket-name/operations/operation-id` |   
`response` | The response of the operation. |   
`response.@type` | The type of the response. |   
`selfLink` | A link to this operation. |   
**Note:** The `metadata.commonMetadata.progressPercent` shows the overall completion of the long-running operation. It reaches `100`% when all steps are finished. This is the only reliable indicator of complete success. Other progress indicators show the movement of bytes, objects, and metadata. These may reach `100`% sooner than `metadata.commonMetadata.progressPercent`. After the bytes, objects, and metadata are moved, bucket relocation finishes the final steps and after that the `metadata.commonMetadata.progressPercent` is updated to `100`%.**Note:** Relocation progress isn't linear or predictable. Don't use the time taken for small relocations to estimate the duration of larger relocations. Relocations without write downtime take at least 7 days to complete, regardless of the bucket's total size or the number of objects.

If you encounter issues when interacting with other Cloud Storage features, see [Limitations](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview#limitations).

### Initiate the final synchronization step

For relocations that require a write downtime, you'll need to initiate the final synchronization. The final synchronization step involves a period where you cannot perform write operations on the bucket. We recommend that you schedule the final synchronization step at a time that minimizes disruption to your applications.

### Console

To initiate the final synchronization step, complete the following steps:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that you are relocating.

  3. On the **Bucket details** page, click the **Operations** tab.

  4. In the list of bucket operations, click the relocation operation to view the operation details page. On the operation details page, when the data copy is at least 99% complete, a message bar appears indicating it's the optimal time to start the final synchronization.

  5. Optional: To set the maximum allowed write downtime, click **Set maximum allowed downtime (TTL)** and specify the maximum downtime duration.

  6. Click **Start final synchronization**.

  7. On the confirmation dialog that appears, click **Start** to begin the final synchronization.




The operation details page shows the relocation summary, key metrics, and an error summary.

### Command line

Before you proceed, confirm that the bucket is fully prepared by checking the `finalizationState` value in the output of the Initiate the bucket relocation step.

When the `finalizationState` value is `READY`, run the [`gcloud storage buckets relocate`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/relocate) command to initiate the final synchronization:
    
    
    gcloud storage buckets relocate --finalize --operation=projects/_/buckets/BUCKET_NAME/operations/OPERATION_ID

Where:

  * `BUCKET_NAME` is the name of the bucket that you want to relocate.
  * `OPERATION_ID` is the ID of the bucket relocation long-running operation, which is returned in the response of methods you call. For example, the following response is returned from calling [`gcloud storage operations list`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/operations/list) and the long-running operation ID is `AbCJYd8jKT1n-Ciw1LCNXIcubwvij_TdqO-ZFjuF2YntK0r74`.


    
    
     `name: projects/_/buckets/my-bucket/operations/AbCJYd8jKT1n-Ciw1LCNXIcubwvij_TdqO-ZFjuF2YntK0r74` 

Set the `ttl` flag to have greater control over the relocation process. For example:
    
    
    gcloud storage buckets relocate --finalize --ttl TTL_DURATION --operation=projects/_/buckets/BUCKET_NAME/operations/OPERATION_ID

Where:

`TTL_DURATION` is the Time to live (TTL) for the write downtime phase during a relocation process. It is expressed as a string, such as `12h` for 12 hours. The `TTL_DURATION` determines the maximum allowed duration for the write downtime phase. If the write downtime exceeds this limit, the relocation process automatically reverts to the bucket relocation step, and write operations to the bucket are re-enabled. The value must be within the range of `6h` (6 hours) to `48h` (48 hours). If not specified, the default value is `12h` (12 hours).

### JSON API

Before you proceed, confirm that the bucket is fully prepared by checking the `finalizationState` value in the output of the bucket relocation step. The `finalizationState` value must be `READY` to proceed.

If you initiate the final synchronization step prematurely, the command returns an error message `The relocate bucket operation isn't ready to advance to finalization running state` but the relocation process continues.

We recommend that you wait until the `progressPercent` value is `99` before initiating the final synchronization step.

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the settings for bucket relocation. See the [`Buckets: advanceRelocateBucket`](https://docs.cloud.google.com/storage/docs/json_api/v1/operations/advanceRelocateBucket) documentation for a complete list of settings. The following are common settings to include:
         
         {
         "expireTime": "EXPIRE_TIME",
         "ttl": "TTL_DURATION"
         }

Where:

     * `EXPIRE_TIME` is the time the write downtime expires.
     * `TTL_DURATION` is the Time to live (TTL) for the write downtime phase during a relocation process. It is expressed as a string, such as `12h` for 12 hours. The `TTL_DURATION` determines the maximum allowed duration for the write downtime phase. If the write downtime exceeds this limit, the relocation process automatically reverts to the bucket relocation step, and write operations to the bucket are re-enabled. The value must be within the range of `6h` (6 hours) to `48h` (48 hours). If not specified, the default value is `12h` (12 hours).
  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api):
         
         curl -X POST --data-binary @JSON_FILE_NAME \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
          "https://storage.googleapis.com/storage/v1/b/bucket/BUCKET_NAME/operations/OPERATION_ID/advanceRelocateBucket"

Where:

     * `JSON_FILE_NAME` is the name of the JSON file you created.
     * `BUCKET_NAME` is the name of the bucket you want to relocate.
     * `OPERATION_ID` is the ID of the long-running operation that initiated the bucket relocation. To get the list of long-running operation IDs for a bucket, see [Operations: list](https://docs.cloud.google.com/storage/docs/json_api/v1/operations/list#response).



## Validate the bucket relocation process

After initiating a relocation, verify its successful completion. This section provides guidance on confirming the successful transfer of data.

Validate the success of the relocation process using the following methods:

  * **Poll long-running operations** : Bucket relocation is a long-running operation. You can poll the long-running operation using the `operation id` to monitor the operation's progress and confirm its successful completion by verifying the `success` state. This involves periodically querying the operation's status until it reaches a terminal state. For information about monitoring long-running operations, see [Use long-running operations in Cloud Storage](https://docs.cloud.google.com/storage/docs/using-long-running-operations).

  * **Analyze Cloud Audit Logs entries** : Cloud Audit Logs provides a detailed record of events and operations in your Google Cloud environment. You can analyze the Cloud Audit Logs entries associated with the relocation to validate its success. Analyze the logs for any errors, warnings, or unexpected behavior that might indicate issues during the transfer. For information about viewing Cloud Audit Logs logs, see [Viewing audit logs](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#viewing_audit_logs).

The following log entries help you to determine if your move is a success or a failure:

    * Successful relocation: `Relocate bucket succeeded. All existing objects are now in the new placement configuration.`

    * Failed relocation: `Relocate bucket has failed. Bucket location remains unchanged.`

Using Pub/Sub notifications, you can also set up alerts that notify when the specific success or failure event appears in the logs. For information about setting up Pub/Sub notifications, see [Configure Pub/Sub notifications for Cloud Storage](https://docs.cloud.google.com/storage/docs/reporting-changes).




## Complete the post bucket relocation tasks

After you have successfully relocated your bucket, complete the following steps:

  1. Optional: Restore any [tag-based](https://docs.cloud.google.com/storage/docs/tags-and-labels#tags) access controls on your bucket.
  2. Existing [inventory report](https://docs.cloud.google.com/storage/docs/insights/inventory-reports) configurations are not preserved during the relocation process and you'll need to manually recreate them. For information about creating an inventory report configuration, see [Create an inventory report configuration](https://docs.cloud.google.com/storage/docs/insights/using-inventory-reports#create-report-config).
  3. Update your infrastructure as code configurations such as Terraform and Google Kubernetes Engine configuration connector to specify the bucket's new location.
  4. [Regional endpoints](https://docs.cloud.google.com/storage/docs/regional-endpoints) are tied to specific locations, and you'll need to modify your application code to reflect the new endpoint.



## How to handle failed bucket relocation operations

Consider the following factors before handling failed bucket relocation operations:

  * A failed bucket relocation might leave obsolete resources, such as temporary files or incomplete data copies, at the destination. You must wait 7 to 14 days before initiating another bucket relocation to the same destination. You can initiate a bucket relocation to a different destination immediately.

  * If the destination location isn't the optimal location for your data, you might want to roll back the relocation. However, you cannot initiate a relocation immediately. A waiting period of 7 to 14 days is required before you can initiate a relocation back to the original source location in order to maintain stability and avoid data conflicts.




## What's next

  * Learn about [bucket relocation](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
