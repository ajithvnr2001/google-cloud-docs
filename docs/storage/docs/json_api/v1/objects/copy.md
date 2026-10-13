---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/copy/
title: Objects: copy \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:07:41.302241+00:00
---

# Objects: copy  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/copy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Objects: copy Stay organized with collections  Save and categorize content based on your preferences. 

Copies a source object to a destination object. Optionally overrides metadata.

Generally, you should use the [`rewrite`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite) method instead of the `copy` method: the `copy` method uses the `rewrite` method, but calls it exactly once. Larger objects can require multiple `rewrite` calls, so copy attempts of such objects can lead to `Payload too large` errors.

**Note:** The copied object does not retain the ACLs of the original object. Instead, it gains any ACLs you specify in the `copy` method or, if you don't specify any ACLs, the default object ACLs of the bucket it is stored in.

## Required permissions

The authenticated user must have the following IAM permissions to use this method:

  * `storage.objects.create` on the destination bucket
  * `storage.objects.delete` on the destination bucket, if overwriting an existing object
  * `storage.objects.setRetention` on the destination bucket, if the request body includes the `retention` property
  * `storage.objects.get` on the source bucket
  * `storage.objects.createContext` on the destination bucket, if the request body includes a non-empty `contexts.custom` property
  * `storage.objects.dropContexts` on the destination bucket, if the `dropContextGroups` parameter is used.



## Request

### HTTP request
    
    
    POST https://storage.googleapis.com/storage/v1/b/sourceBucket/o/sourceObject/copyTo/b/destinationBucket/o/destinationObject

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`destinationBucket` | `string` |  Name of the bucket in which to store the new object. Overrides the provided object metadata's `bucket` value, if any. For information about how to URL encode object names to be path safe, see [Encoding URI path parts](https://docs.cloud.google.com/storage/docs/request-endpoints#encoding).   
`destinationObject` | `string` |  Name of the new object. Required when the object metadata is not otherwise provided. Overrides the object metadata's `name` value, if any.   
`sourceBucket` | `string` |  Name of the bucket in which to find the source object.   
`sourceObject` | `string` |  Name of the source object. For information about how to URL encode object names to be path safe, see [Encoding URI path parts](https://docs.cloud.google.com/storage/docs/request-endpoints#encoding).   
**Optional query parameters**  
`destinationKmsKeyName` | `string` |  [Resource name of the Cloud KMS key](https://docs.cloud.google.com/kms/docs/resource-hierarchy#retrieve_resource_id) that will be used to encrypt the object. The Cloud KMS key must be located in same location as the object.   
  
If the parameter is not specified, the request uses the destination bucket's default encryption key, if any, or else it uses [standard Cloud Storage encryption](https://docs.cloud.google.com/storage/docs/encryption/default-keys).   
  
If the object is large, re-encryption with the key may take too long and result in a `Deadline exceeded` error. For large objects, consider using the [`rewrite`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite) method instead.   
`destinationPredefinedAcl` | `string` |  Apply a predefined set of access controls to the destination object.   
  
Acceptable values are: 

  * `authenticatedRead`: Object owner gets `OWNER` access, and `allAuthenticatedUsers` get `READER` access.
  * `bucketOwnerFullControl`: Object owner gets `OWNER` access, and project team owners get `OWNER` access.
  * `bucketOwnerRead`: Object owner gets `OWNER` access, and project team owners get `READER` access.
  * `private`: Object owner gets `OWNER` access.
  * `projectPrivate`: Object owner gets `OWNER` access, and project team members get access according to their roles.
  * `publicRead`: Object owner gets `OWNER` access, and `allUsers` get `READER` access.

If `iamConfiguration.uniformBucketLevelAccess.enabled` is set to `true`, requests that include this parameter fail with a `400 Bad Request` response.   
`dropContextGroups` | `string` |  Specifies which groups of object contexts from the source object should be dropped on the destination object during the copy operation. The accepted value is `custom`. The following table summarizes the behavior of object contexts during copy and rewrite operations: | `dropContextGroups` contains `custom`? | `contexts` provided in request body? | Resulting destination contexts  
---|---|---  
**No** | **No** | **Preserved:** All contexts from the source object are kept.  
**No** | **Yes** | **Overridden:** Only contexts provided in the request body are applied.  
**Yes** | **No** | **Dropped:** No contexts are attached to the destination object.  
**Yes** | **Yes** | **Overridden:** Only contexts provided in the request body are applied.  
`ifGenerationMatch` | `long` |  Makes the operation conditional on there being a live destination object with a generation number that matches the given value. Setting `ifGenerationMatch` to 0 makes the operation succeed only if there is no live destination object.   
`ifGenerationNotMatch` | `long` |  Makes the operation conditional on there being a live destination object with a generation number that does not match the given value. If no live destination object exists, the precondition fails. Setting `ifGenerationNotMatch` to 0 makes the operation succeed if there is a live version of the object.   
`ifMetagenerationMatch` | `long` |  Makes the operation conditional on there being a live destination object with a metageneration number that matches the given value.   
`ifMetagenerationNotMatch` | `long` |  Makes the operation conditional on there being a live destination object with a metageneration number that does not match the given value.   
`ifSourceGenerationMatch` | `long` |  Makes the operation conditional on whether the source object's generation matches the given value.   
`ifSourceGenerationNotMatch` | `long` |  Makes the operation conditional on whether the source object's generation does not match the given value.   
`ifSourceMetagenerationMatch` | `long` |  Makes the operation conditional on whether the source object's current metageneration matches the given value.   
`ifSourceMetagenerationNotMatch` | `long` |  Makes the operation conditional on whether the source object's current metageneration does not match the given value.   
`projection` | `string` |  Set of properties to return. Defaults to `noAcl`, unless the object resource specifies the `acl` property, when it defaults to `full`.   
  
Acceptable values are: 

  * `full`: Include all properties.
  * `noAcl`: Omit the `owner`, `acl` property.

  
`sourceGeneration` | `long` |  If present, selects a specific revision of the source object (as opposed to the latest version, the default).   
**Optional extension headers**  
`X-Goog-Copy-Source-Encryption-Algorithm` | `string` |  The encryption algorithm to use, which must be `AES256`. Used if the source object was encrypted with a [customer-supplied encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys).   
`X-Goog-Copy-Source-Encryption-Key` | `string` |  An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-4) Base64-encoded string of the AES-256 encryption key used to encrypt the source object, if it was encrypted with a [customer-supplied encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys).   
`X-Goog-Copy-Source-Encryption-Key-Sha256` | `string` |  An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-4) Base64-encoded string of the SHA256 hash of the encryption key used to encrypt the source object, if it was encrypted with a [customer-supplied encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys).   
`X-Goog-Encryption-Algorithm` | `string` |  The encryption algorithm to use, which must be `AES256`. Used for encrypting the destination object with a [customer-supplied encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys).   
`X-Goog-Encryption-Key` | `string` |  An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-4) Base64-encoded string of your AES-256 encryption key. Used for encrypting the destination object with a [customer-supplied encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys).   
`X-Goog-Encryption-Key-Sha256` | `string` |  An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-4) Base64-encoded string of the SHA256 hash of your encryption key. Used for encrypting the destination object with a [customer-supplied encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys).   
  
### Request body

In the request body, supply metadata to apply to the destination object by using an [object resource](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#resource). If the request body is empty, [editable metadata](https://docs.cloud.google.com/storage/docs/metadata#editable) from the source object is applied to the destination object, with the exception of any ACLs, object holds, or `retention` configuration set on the source object. If you want to retain these from the original object, they must be included in the request body.

By default, [object contexts](https://docs.cloud.google.com/storage/docs/object-contexts) from the source object are preserved on the destination object, even if the request body is not empty. You can update specific contexts by providing them in the request body, or drop all source contexts by using the `dropContextGroups` parameter.

## Response

If successful, this method returns an [object resource](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#resource) in the response body.

For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
