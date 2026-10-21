---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/bulkRestore/
title: Objects: bulkRestore \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:23.881562+00:00
---

# Objects: bulkRestore  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/bulkRestore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Objects: bulkRestore Stay organized with collections  Save and categorize content based on your preferences. 

Initiates a long-running operation to bulk restore multiple [soft-deleted objects](https://docs.cloud.google.com/storage/docs/soft-delete) in a bucket. Soft-deleted objects that meet the criteria defined in the request body parameters are restored to the bucket.

When a soft-deleted object is restored, a new copy of that object is created in the same bucket and inherits the same metadata as the soft-deleted object. The inherited metadata is the metadata that existed when the original object became soft deleted, with the following exceptions: 

  * The `createTime` of the new object is set to the time at which the soft-deleted object was restored.
  * The `softDeleteTime` and `hardDeleteTime` values are cleared.
  * A new generation is assigned and the metageneration is reset to 1.
  * If the soft-deleted object was in a bucket that had Autoclass enabled, the new object is restored to Standard storage.
  * The restored object inherits the bucket's default object ACL, unless `copySourceAcl` is `true`.



If a live object using the same name already exists in the bucket and becomes overwritten, the live object becomes a noncurrent object if [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) is enabled on the bucket. If Object Versioning is not enabled, the live object becomes soft deleted.

The specified bucket must have a soft delete policy. Otherwise, the request fails with a `400 Bad Request` error with the reason `SoftDeletePolicyRequired`. 

## Required permissions

The authenticated user must have the following IAM permissions to use this method: 

  * `storage.buckets.restore`
  * `storage.objects.restore`
  * `storage.objects.create`
  * `storage.objects.setIamPolicy` (only required if `copySourceAcl` is `true` and the relevant bucket has [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) disabled)



## Request

### HTTP request
    
    
    POST https://storage.googleapis.com/storage/v1/b/bucket/o/bulkRestore

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of the bucket in which objects will be restored.   
  
### Request body

In the request body, supply a data structure with the following properties:

Property name | Value | Description | Notes  
---|---|---|---  
`allowOverwrite` | `boolean` | If `false` (default), the bulk restore operation will not overwrite live objects that have the same name as the soft-deleted objects to be restored. This means that some soft-deleted objects might not get restored. If `true`, live objects that have the same name as the soft-deleted objects will be overwritten. If [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) is enabled on the bucket, the live objects will become noncurrent when overwritten. If Object Versioning is not enabled, the live object will become soft-deleted when overwritten. Noncurrent objects that have the same name as the soft-deleted objects to be restored do not get overwritten. |  writable   
`matchGlob` | `string` | Restores only the soft-deleted objects that match the specified glob. If this parameter is not specified, all soft-deleted objects that match the specified time range are restored. For more information about glob syntax, see the [match glob documentation](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list#list-object-glob). |  writable   
`softDeletedAfterTime` | `string` | Restores only the soft-deleted objects that were soft deleted after the specified time. |  writable   
`softDeletedBeforeTime` | `string` | Restores only the soft-deleted objects that were soft deleted before the specified time. |  writable   
`createdAfterTime` | `string` | Restores only the soft-deleted objects that were created after the specified time. |  writable   
`createdBeforeTime` | `string` | Restores only the soft-deleted objects that were created before the specified time. |  writable   
`copySourceAcl` | `boolean` |  Applicable only for buckets that don't have [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) enabled. If `true`, copies the soft-deleted object's ACL and applies it to the restored object. If `false` or not specified, the restored object inherits the bucket's default object ACL.  |  writable   
  
## Response

If successful, this method returns an instance of [operation](https://github.com/googleapis/googleapis/blob/master/google/longrunning/operations.proto) in the response body:
    
    
    {
      "name": "string",
      "metadata": { object (BulkRestoreObjectsMetadata)},
      "done": "boolean",
      // Union field result can be only one of the following:
      "error": { object (Status)},
      "response": {}
      // End of list of possible types for union field result
    }

Property name | Value | Description | Notes  
---|---|---|---  
`name` | `string` | The server-assigned name of the operation. |   
`metadata` | `object` | An object of type `BulkRestoreObjectsMetadata`:
    
    
    {
      "allowOverwrite": boolean,
      "matchGlobs": "string",
      "softDeletedAfterTime": "datetime",
      "softDeletedBeforeTime": "datetime",
      "createdAfterTime": "datetime",
      "createdBeforeTime": "datetime",
      "copySourceAcl": boolean,
      "succeededCount": "long",
      "skippedCount": "long",
      "failedCount": "long",
    }

Where: 

  * `succeededCount` is the number of successfully restored objects.
  * `skippedCount` is the number of objects skipped as a result of the specified `softDeletedAfterTime`, `softDeletedBeforeTime`, `createdAfterTime`, `createdBeforeTime`, and `matchGlobs` parameters. If multiple generations of an object match the criteria, only the latest generation is restored and the rest are skipped.
  * `failedCount` is the number of objects that failed to be restored. Objects can fail to be restored if, for example, a live object with the same name cannot be rewritten. 

|   
`done` | `boolean` | If `false`, indicates that the operation is still in progress, and neither `error` nor `response` is set. If `true`, the operation is completed and either `error` or `response` is set. |   
`error` | `object` | Indicates that the operation is considered to be successful, unless it failed to start because of invalid parameters, or because of an access denied error. For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes). |   
`response` | `object` | Empty. Detailed error information can be obtained from [Cloud Audit Logs](https://docs.cloud.google.com/storage/docs/audit-logging). |   
  
## Try it!

Use the APIs Explorer below to call this method on live data and see the response.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
