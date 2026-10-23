---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/move/
title: Objects: move \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:30.976033+00:00
---

# Objects: move  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/move/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Objects: move Stay organized with collections  Save and categorize content based on your preferences. 

Moves an object within a bucket.

This operation moves a source object to a destination object in the same bucket by renaming the object. The move itself is an atomic transaction, ensuring all steps either complete successfully or no changes are made.

The move operation performs the following actions:

  1. The source object is deleted as follows: 
     * No early deletion fee is incurred.
     * [Soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) retention period is not applied.
     * [Audit logs](https://docs.cloud.google.com/storage/docs/audit-logging) and [notification messages](https://docs.cloud.google.com/storage/docs/pubsub-notifications) are generated for the object.
  2. The destination object is created with the same data and metadata as the source object except for the following changes: 
     * A new object `name`
     * A new `generation number`
     * A new `metageneration number`, set to `1`
     * New `create` and `update` timestamps
     * The destination object is moved to Standard storage if the bucket has Autoclass enabled
  3. If a destination folder doesn't exist, the move operation creates the folder along with the destination object. The move operation also automatically creates any necessary parent folders.



Consider the following points when using the `move` method:

  * The source and destination must have different object names.
  * The source object must exist. You can only move existing objects.
  * If an object already exists at the destination, the move operation replaces the existing object. The replaced object will become noncurrent or soft-deleted depending on whether Object Versioning or soft delete is enabled. You can disable the replacement behavior using preconditions on the request.



## Required permissions

The authenticated user must have the following IAM permissions to use this method:

  * Permissions required on the source object:
    * `storage.objects.delete` and `storage.objects.get`
_or_
    * `storage.objects.move` (required only to move an object without allowing read or delete access)
  * Permissions required on the destination object:
    * `storage.objects.create`
    * `storage.objects.delete` (required only for replacing an object)
    * `storage.folders.create` (required only for automatically creating any missing parent folders)
    * `storage.objects.getIamPolicy` (only required if `projection` is `full` and the relevant bucket has [uniform bucket-level access disabled](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access))



## Request

### HTTP request
    
    
    POST https://storage.googleapis.com/storage/v1/b/bucket/o/sourceObject/moveTo/o/destinationObject

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of the bucket containing the object you want to move.   
`sourceObject` | `string` |  Name of the source object. For information about how to URL encode object names to be path safe, see [Encoding URI path parts](https://docs.cloud.google.com/storage/docs/request-endpoints#encoding).   
`destinationObject` | `string` |  Name of the new object. Required when the object metadata is not otherwise provided. Overrides the object metadata's `name` value, if any. For information about how to URL encode object names to be path safe, see [Encoding URI path parts](https://docs.cloud.google.com/storage/docs/request-endpoints#encoding).   
**Optional query parameters**  
`ifGenerationMatch` | `long` |  Makes the operation conditional on there being a live destination object with a generation number that matches the given value. Setting `ifGenerationMatch` to `0` makes the operation succeed only if there is no live destination object.   
`ifGenerationNotMatch` | `long` |  Makes the operation conditional on there being a live destination object with a generation number that does not match the given value. If no live destination object exists, the precondition fails. Setting `ifGenerationNotMatch` to `0` makes the operation succeed if there is a live version of the object. The `ifGenerationMatch` and `ifGenerationNotMatch` parameters are mutually exclusive. Specifying both parameters in a single request results in an error.   
`ifMetagenerationMatch` | `long` |  Makes the operation conditional on there being a live destination object with a metageneration number that matches the given value.   
`ifMetagenerationNotMatch` | `long` |  Makes the operation conditional on there being a live destination object with a metageneration number that does not match the given value. The `ifMetagenerationMatch` and `ifMetagenerationNotMatch` parameters are mutually exclusive. Specifying both parameters in a single request result in an error.   
`ifSourceGenerationMatch` | `long` |  Makes the operation conditional on whether the source object's generation matches the given value.   
`ifSourceGenerationNotMatch` | `long` |  Makes the operation conditional on whether the source object's generation does not match the given value. The `ifSourceGenerationMatch` and `ifSourceGenerationNotMatch` parameters are mutually exclusive. Specifying both parameters in a single request result in an error.   
`ifSourceMetagenerationMatch` | `long` |  Makes the operation conditional on whether the source object's current metageneration matches the given value.   
`ifSourceMetagenerationNotMatch` | `long` |  Makes the operation conditional on whether the source object's current metageneration does not match the given value. The `ifSourceMetagenerationMatch` and `ifSourceMetagenerationNotMatch` parameters are mutually exclusive. Specifying both parameters in a single request result in an error.   
`projection` | `string` |  Set of properties to return. Defaults to `noAcl`.   
  
Acceptable values are: 

  * `full`: Include all properties. 
  * `noAcl`: Omit the `owner`, `acl` property. 

  
  
### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns the destination object's [resource](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#resource) in the response body.

The following errors could occur:

  * If the source object is subject to either an [object retention policy](https://docs.cloud.google.com/storage/docs/object-lock) or [bucket retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock), the request fails with a `403 Forbidden error` with the reason `retentionPolicyNotMet`.
  * Likewise, if a live object already exists at the destination and it is subject to either an [object retention policy](https://docs.cloud.google.com/storage/docs/object-lock) or [bucket retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock), the request fails with a `403 Forbidden` error with the reason `retentionPolicyNotMet`.



For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
