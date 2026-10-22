---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/get/
title: Objects: get \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:58.128564+00:00
---

# Objects: get  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Objects: get Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves object metadata. When `alt=media` is included as a query parameter in the request, this method retrieves object data.

This method supports the use of the [`Range`](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#range) header, which can be used to retrieve only part of the object data.

For examples of performing object downloads with different Cloud Storage tools and client libraries, see the [Downloading Objects guide](https://docs.cloud.google.com/storage/docs/downloading-objects).

## Required permissions

The authenticated user must have the `storage.objects.get` IAM permission to use this method. To return object ACLs, the authenticated user must also have the `storage.objects.getIamPolicy` permission.

## Request

### HTTP request
    
    
    GET https://storage.googleapis.com/storage/v1/b/bucket/o/object

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of the bucket in which the object resides.   
`object` | `string` |  Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI path parts](https://docs.cloud.google.com/storage/docs/request-endpoints#encoding).   
**Optional query parameters**  
`alt` | `string` |  Type of data to return. Defaults to `json`. Acceptable values are:

  * `json`: Return object metadata.
  * `media`: Return object data. Not supported for soft-deleted objects.

  
`generation` | `long` |  If present, selects a specific revision of this object (as opposed to the latest version, the default). If `softDeleted` is `true`, this parameter is required.   
`ifGenerationMatch` | `long` |  Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.   
`ifGenerationNotMatch` | `long` |  Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.   
`ifMetagenerationMatch` | `long` |  Makes the operation conditional on whether the object's current metageneration matches the given value.   
`ifMetagenerationNotMatch` | `long` |  Makes the operation conditional on whether the object's current metageneration does not match the given value.   
`projection` | `string` |  Set of properties to return. Defaults to `noAcl`.   
  
Acceptable values are: 

  * `full`: Include all properties.
  * `noAcl`: Omit the `owner`, `acl` property.

  
`restoreToken` | `string` | Applicable in buckets with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled. The `restoreToken` is a universally unique identifier (UUID) associated with each [soft-deleted object](https://docs.cloud.google.com/storage/docs/soft-delete). When getting the metadata for a soft-deleted object, the `restoreToken` is only required when the `name` and `generation` values of the object [do not uniquely identify it](https://docs.cloud.google.com/storage/docs/soft-delete#restore-tokens). Otherwise, including a `restoreToken` in the request is optional.  
`softDeleted` | `boolean` |  If `true`, returns the metadata of the [soft-deleted object](https://docs.cloud.google.com/storage/docs/soft-delete). If `true`, `generation` must also be specified, and `alt=media` cannot be specified.   
**Optional extension headers**  
`X-Goog-Encryption-Algorithm` | `string` |  The encryption algorithm to use, which must be `AES256`. Use this header if the object is encrypted with a [customer-supplied encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys) and you want the object's data or content hashes returned in the response.   
`X-Goog-Encryption-Key` | `string` |  An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-4) Base64-encoded string of your AES-256 encryption key. Use this header if the object is encrypted with a [customer-supplied encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys) and you want the object's data or content hashes returned in the response.   
`X-Goog-Encryption-Key-Sha256` | `string` |  An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-4) Base64-encoded string of the SHA256 hash of your encryption key. Use this header if the object is encrypted with a [customer-supplied encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys) and you want the object's data or content hashes returned in the response.   
  
### Request body

Do not supply a request body with this method.

## Response

By default, this responds with an [object resource](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#resource) in the response body. If you provide the URL parameter `alt=media`, then it will respond with the object data in the response body.

For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
