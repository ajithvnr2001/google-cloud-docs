---
url: https://docs.cloud.google.com/storage/docs/batch-operations/configure-logs/
title: Cloud Logging for storage batch operations \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:15.325063+00:00
---

# Cloud Logging for storage batch operations  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/batch-operations/configure-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Cloud Logging for storage batch operations Stay organized with collections  Save and categorize content based on your preferences. 

You can configure and view [storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview) logs in Cloud Logging. When you configure Cloud Logging, a batch operations job generates log entries for each transformation job, with each entry corresponding to the attempted transformation of an object.

Storage batch operations support logging to both Cloud Logging and [Cloud Storage Cloud Audit Logs](https://docs.cloud.google.com/storage/docs/audit-logging). While both options capture storage batch operations actions, we recommend using Cloud Logging. Cloud Logging provides a centralized platform for log analysis, real-time monitoring, and advanced filtering, offering a robust solution for managing and understanding your batch operation activity.

## Before you begin

Verify that you have access to Cloud Logging. To use Cloud Logging, we recommend granting the `Logs Viewer (roles/logging.viewer)` Identity and Access Management role. The `Logs Viewer (roles/logging.viewer)` Identity and Access Management role provides the Identity and Access Management permissions required to view your Cloud Logging data. For more information about Logging access permissions, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

To verify and grant the IAM permissions, complete the following steps:

  * [View current access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#view-access) to verify the access that each principal has.
  * [Grant a role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role) to relevant principals in your project.



## Understand logging details

When logging is enabled, storage batch operations capture the following details:

  * **Loggable action** : The loggable action value is always `transform`.

  * **Loggable states** : For each action, you can choose to log one or both of the following states:

    * `SUCCEEDED`: The action was successful.
    * `FAILED`: The action failed.



## Enable logging

To enable logging, specify the actions and the states to log.

### Command line

When creating a storage batch operations job with `gcloud storage batch-operations jobs create`, use the `--log-actions` and `--log-action-states` flags to enable logging.
    
    
    gcloud storage batch-operations jobs create JOB_NAME \
      --manifest-location=MANIFEST_LOCATION \
      --delete-object \
      --log-actions=transform \
      --log-action-states=LOG_ACTION_STATES
    

Where:

  * `JOB_NAME` is the name you want to give your job. For example, `my-job`.
  * `MANIFEST_LOCATION` is the location of your manifest. For example, `gs://my-bucket/manifest.csv`.
  * `LOG_ACTION_STATES` is a comma-separated list of states to log. For example, `succeeded,failed`.



### REST API

[Create a storage batch operations job](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#rest-apis) with a [`LoggingConfig`](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs#LoggingConfig).
    
    
    {
       "loggingConfig": {
          "logActions": ["TRANSFORM"],
          "logActionStates": ["LOG_ACTION_STATES"],
            }
    }

Where:

`LOG_ACTION_STATES` is a comma-separated list of states to log. For example, `"SUCCEEDED","FAILED"`.

## View logs

To view storage batch operations logs, do the following:

### Console

  1. Go to the Google Cloud navigation menu _menu_ and select **Logging > Logs Explorer **:

[Go to the Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Select a Google Cloud project.

  3. From the **Upgrade** menu, switch from **Legacy Logs Viewer** to **Logs Explorer**.

  4. To filter your logs to show only storage batch operations entries, type `storage_batch_operations_job` into the query field and click **Run query**.

  5. In the **Query results** pane, click **Edit time** to change the time period for which to return results.




For more information on using the Logs Explorer, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface).

### Command line

To use the gcloud CLI to search for storage batch operations logs, use the [`gcloud logging read`](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging#reading_log_entries) command.

Specify a filter to limit your results to storage batch operations logs.
    
    
    gcloud logging read "resource.type=storage_batch_operations_job"
    

### REST API

Use the [`entries.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list) Cloud Logging API method.

To filter your results to include only storage batch operations-related entries, use the `filter` field. The following is a sample JSON request object:
    
    
    {
    "resourceNames":
      [
        "projects/my-project-name"
      ],
      "orderBy": "timestamp desc",
      "filter": "resource.type=\"storage_batch_operations_job\""
    }
    

Where:

`my-project-name` is the name of your project.

## Storage batch operations log format

All storage batch operations-specific fields are contained within a `jsonPayload` object. While the exact content of `jsonPayload` varies based on the [job type](https://docs.cloud.google.com/storage/docs/batch-operations/overview#job-type), there is a common structure shared across all `TransformActivityLog` entries. This section outlines the common log fields and then details the operation-specific fields.

  * **Common log fields**

The following fields appear in all logs:
        
        jsonPayload: {
        "@type": "type.googleapis.com/google.cloud.storagebatchoperations.logging.TransformActivityLog",
        "completeTime": "YYYY-MM-DDTHH:MM:SS.SSSSSSSSSZ",
        "status": {
          "errorMessage": "String indicating error",
          "errorType": "ENUM_VALUE",
          "statusCode": "ENUM_VALUE"
        },
        "logName": "projects/PROJECT_ID/logs/storagebatchoperations.googleapis.com%2Ftransform_activity",
        "receiveTimestamp": "YYYY-MM-DDTHH:MM:SS.SSSSSSSSSZ",
        "resource": {
          "labels": {
            "location":"us-central1",
            "job_id": "BATCH_JOB_ID",
            "resource_container": "RESOURCE_CONTAINER",
            // ... other labels
          },
          "type": "storagebatchoperations.googleapis.com/Job"
        },
        // Operation-specific details will be nested here (for example,
        // "DeleteObject", "PutObjectHold", "RewriteObject", "PutMetadata")
        // Each operation-specific object will also contain the following
        // object: "objectMetadataBefore": {
        //   "gcsObject": {
        //     "bucket": "BUCKET_NAME",
        //     "generation": "GENERATION_NUMBER",
        //     "objectKey": "OBJECT_PATH"
        //   }
        // }
        }
        

The following table describes each of the common log fields:

Common log fields | Type | Description  
---|---|---  
`@type` | String | Specifies the type of the log entry's payload and indicates that the log represents a `TransformActivityLog` for storage batch operations.  
`completeTime` | Timestamp | The ISO 8601-compliant timestamp at which the operation completed.  
`status` | Object | Provides information about the result of the batch operation activity.  
`status.errorMessage` | String | An error message if the operation fails. The error message appears only if the `status.statusCode` value is _not_ `OK`.  
`status.errorType` | String | The error type. The error type appears only if the `status.statusCode` value is _not_ `OK`.  
`status.statusCode` | String | The status code of the operation. The operation is successful if the value is `OK`; any other value indicates failure.  
`logName` | String | The full resource name of the log, indicating the project and the log stream.  
`receiveTimestamp` | Timestamp | The timestamp when the log entry was received by the logging system.  
`resource` | Object | Information about the resource that generated the log entry.  
`resource.labels` | Object | Key-value pairs providing additional identifying information about the resource.  
`resource.type` | String | The type of resource that generated the log.  
`objectMetadataBefore` | Object | Contains metadata of the object before the batch operation was attempted.  
`objectMetadataBefore.gcsObject` | Object | Details about the object.  
`objectMetadataBefore.gcsObject.bucket` | String | The name of the bucket where the object resides.  
`objectMetadataBefore.gcsObject.generation` | String | The generation number of the object before the operation.  
`objectMetadataBefore.gcsObject.objectKey` | String | The full path of the object within the bucket.  
  * **Operation-specific`jsonPayload` contents**

The difference between log entries for different batch operations lies in the top-level object nested within the `jsonPayload`. Only one of the following objects is available in a given log entry, corresponding to the specific batch operation performed:

    * Delete object (`DeleteObject`)
          
          jsonPayload:
          {
          "DeleteObject": {
            "objectMetadataBefore": {
              "gcsObject": {
                "bucket": "test-bucket",
                "generation": "1678912345678901",
                "objectKey": "test_object.txt"
              }
            }
            }
          }
          

    * Put object hold (`PutObjectHold`)
          
          jsonPayload:
          {
          "PutObjectHold": {
            "objectMetadataBefore": {
              "gcsObject": {
                "bucket": "test-bucket",
                "generation": "1678912345678901",
                "objectKey": "test_object.txt"
              }
            },
            "temporaryHoldAfter": True,
            "eventBasedHoldAfter": True
          }
          }
          

    * Rewrite object (`RewriteObject`)
          
          jsonPayload:
          {
          "RewriteObject": {
            "objectMetadataBefore": {
              "gcsObject": {
                "bucket": "test-bucket",
                "generation": "1678912345678901",
                "objectKey": "test_object.txt"
              }
            },
            "kmsKeyVersionAfter": "projects/my-gcp-project/locations/us-central1/keyRings/my-keyring-01/cryptoKeys/my-encryption-key/cryptoKeyVersions/1"
          }
          }
          

    * Put metadata (`PutMetadata`)
          
          jsonPayload:
          {
          "PutMetadata": {
            "objectMetadataBefore": {
              "gcsObject": {
                "bucket": "test-bucket",
                "generation": "1678912345678901",
                "objectKey": "test_object.txt"
              }
            },
            "content_disposition_after": "attachment; filename=\"report_final.pdf\"",
            "content_encoding_after": "gzip",
            "content_language_after": "en-US",
            "content_type_after": "application/pdf",
            "cache_control_after": "public, max-age=3600",
            "custom_time_after": "2025-06-27T10:00:00Z",
            "custom_metadata_after": {
              "project": "marketing",
              "version": "2.0",
              "approvedBy": "Admin"
            }
          }
          }
          

The following table describes the operation-specific log fields:

Operation-specific log fields | Type | Description  
---|---|---  
`PutObjectHold` | Object | Indicates a hold operation on an object.  
`PutObjectHold.temporaryHoldAfter` | Boolean | If the value is `True`, it indicates that a temporary hold was applied to the object after the storage batch operations job completed. Valid values are `True` or `False`.  
`PutObjectHold.eventBasedHoldAfter` | Boolean | If the value is `True`, it indicates that an event-based hold was applied to the object after the storage batch operations job completed. Valid values are `True` or `False`.  
`RewriteObject` | Object | Indicates a rewrite operation on an object.  
`RewriteObject.kmsKeyVersionAfter` | String | The Cloud Key Management Service key version used after the rewrite job. The `kmsKeyVersionAfter` field is populated if the object's encryption key changed as a result of the rewrite. It's an optional field, meaning it might not be present if the Cloud KMS key version remained unchanged after the rewrite.  
`PutMetadata` | Object | Indicates a metadata update operation on an object.  
`PutMetadata.content_disposition_after` | String | Specifies the `Content-Disposition` header value after the completion of the `PutMetadata` job. It's an optional field and is only populated if the content disposition was set or modified.  
`PutMetadata.content_encoding_after` | String | Specifies the `Content-Encoding` header value after the completion of the `PutMetadata` job. It's an optional field and is only populated if the content encoding was set or modified.  
`PutMetadata.content_language_after` | String | Specifies the `Content-Language` header value after the completion of the `PutMetadata` job. It's an optional field and is only populated if the content language was set or modified.  
`PutMetadata.content_type_after` | String | Specifies the `Content-Type` header value after the completion of the `PutMetadata` job. It's an optional field and is only populated if the content type was set or modified.  
`PutMetadata.cache_control_after` | String | Specifies the `Cache-Control` header value after the completion of the `PutMetadata` job. It's an optional field and is only populated if the cache control was set or modified.  
`PutMetadata.custom_time_after` | String | Specifies the `Custom-Time` header value after the completion of the `PutMetadata` job. It's an optional field and is only populated if the custom time was set or modified.  
`PutMetadata.custom_metadata_after` | Map (key: string, value: string) | Contains a map of `Custom- Metadata` key-value pairs after the transformation. This field includes any user-defined metadata that was set or modified on the object. It allows for flexible storage of additional metadata.  



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
