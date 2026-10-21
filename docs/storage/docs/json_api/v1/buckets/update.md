---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/update/
title: Buckets: update \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:40.111199+00:00
---

# Buckets: update  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Buckets: update Stay organized with collections  Save and categorize content based on your preferences. 

Updates the metadata of a bucket. Changes to the bucket are readable immediately after writing, but configuration changes may take time to propagate.

**Caution:** You should generally use the [PATCH](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) method, which changes only metadata you define in the request. The UPDATE method might change certain metadata for the bucket even if that metadata is not specified in the request.

## Required permissions

To use this method,the authenticated user must have the `storage.buckets.update` IAM permission. Additionally, to perform specific actions on a bucket, the authenticated user must have the following permissions:

  * To update public access prevention policies or access control lists (ACLs): `storage.buckets.setIamPolicy`
  * To return ACLs on a bucket: `storage.buckets.getIamPolicy`
  * To update bucket IP filtering rules: `storage.buckets.setIpFilter`
  * To return bucket IP filtering rules as part of the response: `storage.buckets.getIpFilter`



## Request

### HTTP request
    
    
    PUT https://storage.googleapis.com/storage/v1/b/bucket

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of a bucket.   
**Optional query parameters**  
`ifMetagenerationMatch` | `long` |  Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.   
`ifMetagenerationNotMatch` | `long` |  Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.   
`predefinedAcl` | `string` |  Apply a predefined set of access controls to this bucket.   
  
Acceptable values are: 

  * `authenticatedRead`: Project team owners get `OWNER` access, and `allAuthenticatedUsers` get `READER` access.
  * `private`: Project team owners get `OWNER` access.
  * `projectPrivate`: Project team members get access according to their roles.
  * `publicRead`: Project team owners get `OWNER` access, and `allUsers` get `READER` access.
  * `publicReadWrite`: Project team owners get `OWNER` access, and `allUsers` get `WRITER` access.

If `iamConfiguration.uniformBucketLevelAccess.enabled` is set to `true`, requests that include this parameter fail with a `400 Bad Request` response.   
`predefinedDefaultObjectAcl` | `string` |  Apply a predefined set of default object access controls to this bucket.   
  
Acceptable values are: 

  * `authenticatedRead`: Object owner gets `OWNER` access, and `allAuthenticatedUsers` get `READER` access.
  * `bucketOwnerFullControl`: Object owner gets `OWNER` access, and project team owners get `OWNER` access.
  * `bucketOwnerRead`: Object owner gets `OWNER` access, and project team owners get `READER` access.
  * `private`: Object owner gets `OWNER` access.
  * `projectPrivate`: Object owner gets `OWNER` access, and project team members get access according to their roles.
  * `publicRead`: Object owner gets `OWNER` access, and `allUsers` get `READER` access.

If `iamConfiguration.uniformBucketLevelAccess.enabled` is set to `true`, requests that include this parameter fail with a `400 Bad Request` response.   
`projection` | `string` |  Set of properties to return. Defaults to `full`.   
  
Acceptable values are: 

  * `full`: Include all properties.
  * `noAcl`: Omit `owner`, `acl`, and `defaultObjectAcl` properties. 

  
  
### Request body

In the request body, supply a [bucket resource](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#resource) with the following properties:

Property name | Value | Description | Notes  
---|---|---|---  
**Required Properties**  
`acl[]` | `list` | Access controls on the bucket. If empty, this parameter is ignored. Can contain one or more [bucketAccessControls Resources](https://docs.cloud.google.com/storage/docs/json_api/v1/bucketAccessControls). **Note:** ACLs do not apply in buckets where `iamConfiguration.uniformBucketLevelAccess.enabled` is set to `true`. Requests to such buckets fail with a `400 Bad Request` response if the request contains a non-empty `acl[]` property. |  writable   
**Optional Properties**  
`autoclass` | `object` | The [bucket's Autoclass configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#autoclass), which, when enabled, controls the storage class of objects based on how and when the objects are accessed. For more information, see [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass). |  writable   
`billing` | `object` | The [bucket's billing configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#billing), used to control the [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) feature. |  writable   
`cors[]` | `list` | The [bucket's CORS configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#cors). For more information, see [Cross-Origin Resource Sharing](https://docs.cloud.google.com/storage/docs/cross-origin). |  writable   
`defaultEventBasedHold` | `boolean` | Whether or not to automatically apply an [`eventBasedHold`](https://docs.cloud.google.com/storage/docs/object-holds#hold-types) to new objects added to the bucket. |  writable   
`defaultObjectAcl[]` | `list` | Default access controls to apply to new objects when no ACL is provided. This list defines an `entity` and `role` for one or more [defaultObjectAccessControls Resources](https://docs.cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls). If `iamConfiguration.uniformBucketLevelAccess.enabled` is set to `true`, this field is omitted in responses, and requests that specify this field fail with a `400 Bad Request` response.  |  writable   
`encryption` | `object` | The [bucket's encryption configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#encryption). |  writable   
`iamConfiguration` | `object` | The [bucket's IAM configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#iamConfiguration). |  writable   
`ipFilter` | `object` | The [bucket IP filtering configuration ](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#ipFilter). For more information about bucket IP filtering, see [Bucket IP filtering](https://docs.cloud.google.com/storage/docs/ip-filtering-overview).  |  writable   
`labels` | `object` | User-provided [bucket labels](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels), in key/value pairs. |  writable   
`labels.(key)` | `string` | An individual label entry. |  writable   
`lifecycle` | `object` | The bucket's [lifecycle configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#lifecycle). See [lifecycle management](https://docs.cloud.google.com/storage/docs/lifecycle) for more information.  |  writable   
`logging` | `object` | The [bucket's logging configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#logging). For more information, see [usage logs and storage logs](https://docs.cloud.google.com/storage/docs/access-logs). |  writable   
`retentionPolicy` | `object` | The [bucket's retention policy configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#retentionPolicy). For more information, see [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock). |  writable   
`rpo` | `string` | The recovery point objective for cross-region replication of the bucket. Applicable only for dual- and multi-region buckets. `"DEFAULT"` uses default replication. `"ASYNC_TURBO"` enables turbo replication, valid for dual-region buckets only. For more information, see [redundancy across regions](https://docs.cloud.google.com/storage/docs/availability-durability#cross-region-redundancy). |  writable   
`softDeletePolicy` | `object` | The [bucket's soft delete policy configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#softDeletePolicy). For more information, see [Soft Delete](https://docs.cloud.google.com/storage/docs/soft-delete). | writeable  
`storageClass` | `string` | The bucket's default storage class, used whenever no `storageClass` is specified for a newly-created object. For available storage classes, see [Storage classes](https://docs.cloud.google.com/storage/docs/storage-classes). |  writable   
`versioning` | `object` | The [bucket's versioning configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#versioning). For more information, see [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning). |  writable   
`website` | `object` | The [bucket's website configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#website), controlling how the service behaves when accessing bucket contents as a web site. See the [Static Website Examples](https://docs.cloud.google.com/storage/docs/static-website) for more information. |  writable   
  
## Response

If successful, this method returns a [bucket resource](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#resource) in the response body.

For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
