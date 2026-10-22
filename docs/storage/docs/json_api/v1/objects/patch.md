---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/patch/
title: Objects: patch \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:43.442333+00:00
---

# Objects: patch  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Objects: patch Stay organized with collections  Save and categorize content based on your preferences. 

Updates a data blob's associated metadata. This method supports [patch](https://docs.cloud.google.com/storage/docs/json_api#patch) semantics.

## Required permissions

The authenticated user must have the `storage.objects.update` IAM permission to use this method.

Additionally, the following permissions are required for specific request properties or parameters:

  * If the request body includes the `retention` property: `storage.objects.setRetention`
  * To use the `overrideUnlockedRetention` query parameter: `storage.objects.overrideUnlockedRetention`
  * To update object access control lists (ACLs) for buckets with [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) disabled: `storage.objects.setIamPolicy`
  * To return ACLs as part of the response: `storage.objects.getIamPolicy`
  * To attach [object contexts](https://docs.cloud.google.com/storage/docs/object-contexts): `storage.objects.createContext`
  * To update object contexts: `storage.objects.updateContext`
  * To remove object contexts: `storage.objects.deleteContext`



## Request

### HTTP request
    
    
    PATCH https://storage.googleapis.com/storage/v1/b/bucket/o/object

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of the bucket in which the object resides.   
`object` | `string` |  Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI path parts](https://docs.cloud.google.com/storage/docs/request-endpoints#encoding).   
**Optional query parameters**  
`generation` | `long` |  If present, selects a specific revision of this object (as opposed to the latest version, the default).   
`ifGenerationMatch` | `long` |  Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.   
`ifGenerationNotMatch` | `long` |  Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.   
`ifMetagenerationMatch` | `long` |  Makes the operation conditional on whether the object's current metageneration matches the given value.   
`ifMetagenerationNotMatch` | `long` |  Makes the operation conditional on whether the object's current metageneration does not match the given value.   
`overrideUnlockedRetention` | `boolean` |  Applicable for object's that have an unlocked [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock): Required to be set to `true` if the operation includes a `retention` property that changes the `mode` to `Locked`, reduces the `retainUntilTime`, or removes the retention configuration from the object.   
`predefinedAcl` | `string` |  Apply a predefined set of access controls to this object.   
  
Acceptable values are: 

  * `authenticatedRead`: Object owner gets `OWNER` access, and `allAuthenticatedUsers` get `READER` access.
  * `bucketOwnerFullControl`: Object owner gets `OWNER` access, and project team owners get `OWNER` access.
  * `bucketOwnerRead`: Object owner gets `OWNER` access, and project team owners get `READER` access.
  * `private`: Object owner gets `OWNER` access.
  * `projectPrivate`: Object owner gets `OWNER` access, and project team members get access according to their roles.
  * `publicRead`: Object owner gets `OWNER` access, and `allUsers` get `READER` access.

If `iamConfiguration.uniformBucketLevelAccess.enabled` is set to `true`, requests that include this parameter fail with a `400 Bad Request` response.   
`projection` | `string` |  Set of properties to return. Defaults to `noAcl`, unless the object resource specifies the `acl` property, when it defaults to `full`.   
  
Acceptable values are: 

  * `full`: Include all properties.
  * `noAcl`: Omit the `owner`, `acl` property.

  
**Optional extension headers**  
`X-Goog-Encryption-Algorithm` | `string` |  The encryption algorithm to use, which must be `AES256`. Use this header if the object is encrypted with a [customer-supplied encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys) and you want the object's content hashes returned in the response.   
`X-Goog-Encryption-Key` | `string` |  An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-4) Base64-encoded string of your AES-256 encryption key. Use this header if the object is encrypted with a [customer-supplied encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys) and you want the object's content hashes returned in the response.   
`X-Goog-Encryption-Key-Sha256` | `string` |  An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-4) Base64-encoded string of the SHA256 hash of your encryption key. Use this header if the object is encrypted with a [customer-supplied encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys) and you want the object's content hashes returned in the response.   
  
### Request body

In the request body, supply the relevant portions of an [object resource](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#resource), according to the rules of patch semantics.

## Response

If successful, this method returns an [object resource](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#resource) in the response body.

For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
