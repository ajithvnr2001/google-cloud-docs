---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/restore/
title: Objects: restore \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:15.757364+00:00
---

# Objects: restore  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Objects: restore Stay organized with collections  Save and categorize content based on your preferences. 

Restores a [soft-deleted object](https://docs.cloud.google.com/storage/docs/soft-delete).

When a soft-deleted object is restored, a new copy of that object is created in the same bucket. The new object inherits the same metadata as the soft-deleted object. The inherited metadata is the metadata that existed when the original object became soft deleted, with the following exceptions: 

  * The `createTime` of the new object is set to the time at which the soft-deleted object was restored.
  * The `softDeleteTime` and `hardDeleteTime` values are cleared.
  * A new generation is assigned and the metageneration is reset to 1.
  * If the soft-deleted object was in a bucket that had Autoclass enabled, the new object is restored to Standard storage.
  * The restored object inherits the bucket's default object ACL, unless `copySourceAcl` is `true`.



If a live object using the same name already exists in the bucket and becomes overwritten, the live object becomes a noncurrent object if [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) is enabled on the bucket. If Object Versioning is not enabled, the live object becomes soft deleted.

## Required permissions

The authenticated user must have the following IAM permissions to use this method: 

  * `storage.objects.restore`
  * `storage.objects.create`
  * `storage.objects.delete` (only required if overwriting an existing object)
  * `storage.objects.getIamPolicy` (only required if `projection` is `full` and the relevant bucket has [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) disabled)
  * `storage.objects.setIamPolicy` (only required if `copySourceAcl` is `true` and the relevant bucket has [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) disabled)



## Request

### HTTP request
    
    
    POST https://storage.googleapis.com/storage/v1/b/bucket/o/object/restore

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of the bucket in which the new object will be created. Must be the same bucket that contained the soft-deleted object being restored.   
`object` | `string` |  Name of the soft-deleted object to restore. For information about how to URL encode object names to be path safe, see [Encoding URI path parts](https://docs.cloud.google.com/storage/docs/request-endpoints#encoding).   
**Required query parameters**  
`generation` | `long` |  Specifies the version of the soft-deleted object to restore.   
**Optional query parameters**  
`copySourceAcl` | `boolean` |  Applicable only for buckets that don't have [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) enabled. If `true`, copies the soft-deleted object's ACL and applies it to the restored object. If `false` or not specified, the restored object inherits the bucket's default object ACL.   
`ifGenerationMatch` | `long` |  Makes the operation conditional on there being a live version of the object with a generation number that matches the given value. Setting `ifGenerationMatch` to 0 makes the operation succeed only if there is no such live object.   
`ifGenerationNotMatch` | `long` |  Makes the operation conditional on there being a live version of the object with a generation number that does not match the given value. If no live object exists, the precondition fails. Setting `ifGenerationNotMatch` to 0 makes the operation succeed if there is a live version of the object.   
`ifMetagenerationMatch` | `long` |  Makes the operation conditional on there being a live version of the object with a metageneration number that matches the given value.   
`ifMetagenerationNotMatch` | `long` |  Makes the operation conditional on there being a live version of the object with a metageneration number that does not match the given value.   
`projection` | `string` |  Set of properties to return. Defaults to `noAcl`.   
  
Acceptable values are: 

  * `full`: Include all properties. 
  * `noAcl`: Omit the `owner`, `acl` property. 

  
`restoreToken` | `string` | Applicable in buckets with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled. The `restoreToken` is a universally unique identifier (UUID) associated with each [soft-deleted object](https://docs.cloud.google.com/storage/docs/soft-delete). When restoring a soft-deleted object, the `restoreToken` is only required when the `name` and `generation` values of the object [do not uniquely identify it](https://docs.cloud.google.com/storage/docs/soft-delete#restore-tokens). Otherwise, including a `restoreToken` in the request is optional.  
  
### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns an [object resource](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#resource) in the response body.

The following errors could occur: 

  * If the specified bucket in the request does not have a soft delete policy, the request fails with a `400 Bad Request` error with the reason `SoftDeletePolicyRequired`.
  * If the soft-deleted object's retention duration has passed, or the soft-deleted object no longer exists, the request fails with a `404 Not Found` error with the reason `notFound`.
  * If the specified object in the request is not a soft-deleted object but is either live or noncurrent, the request fails with a `412 Failed Precondition` error with the reason `objectNotSoftDeleted`.
  * If the specified object in the request belongs to a bucket that has a [Bucket Lock retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock), where the object's age is less than the retention duration, the request fails with a `403 Forbidden` error with the reason `retentionPolicyNotMet`.



For more information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
