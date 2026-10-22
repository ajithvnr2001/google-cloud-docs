---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/insert/
title: Buckets: insert \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:39.399683+00:00
---

# Buckets: insert  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/insert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Buckets: insert Stay organized with collections  Save and categorize content based on your preferences. 

Creates a new bucket.

You can't create a bucket with a name that is already in use by another live bucket, because Cloud Storage uses a single, global namespace for bucket names. For more information, see the [bucket naming guidelines](https://docs.cloud.google.com/storage/docs/buckets#naming).

## Required permissions

To use this method,the authenticated user must have the `storage.buckets.create` IAM permission. Additionally, to enable specific bucket features, the authenticated user must have the following permissions:

  * To enable object retention using the `enableObjectRetention` query parameter: `storage.buckets.enableObjectRetention`
  * To set the bucket IP filtering rules: `storage.buckets.setIpFilter`



## Request

### HTTP request
    
    
    POST https://storage.googleapis.com/storage/v1/b

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Required query parameters**  
`project` | `string` |  A valid API project identifier.   
**Optional query parameters**  
`enableObjectRetention` | `boolean` |  When set to `true`, permanently enable object retention for this bucket.   
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
`projection` | `string` |  Set of properties to return. Defaults to `noAcl`, unless the bucket resource specifies `acl` or `defaultObjectAcl` properties, when it defaults to `full`.   
  
Acceptable values are: 

  * `full`: Include all properties.
  * `noAcl`: Omit `owner`, `acl`, and `defaultObjectAcl` properties.

  
  
### Request body

In the request body, supply a [bucket resource](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#resource) with the following properties:

Property name | Value | Description | Notes  
---|---|---|---  
**Required Properties**  
`name` | `string` | The name of the bucket. See the [ bucket naming guidelines](https://docs.cloud.google.com/storage/docs/buckets#naming) for more information. |   
**Optional Properties**  
`acl[]` | `list` | Access controls on the bucket, containing one or more [bucketAccessControls Resources](https://docs.cloud.google.com/storage/docs/json_api/v1/bucketAccessControls). If `iamConfiguration.uniformBucketLevelAccess.enabled` is set to `true`, this field is omitted in responses, and requests that specify this field fail with a `400 Bad Request` response.  |  writable   
`autoclass` | `object` | The [bucket's Autoclass configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#autoclass), which, when enabled, controls the storage class of objects based on how and when the objects are accessed. For more information, see [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass). |  writable   
`billing` | `object` | The [bucket's billing configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#billing), used to control the [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) feature. |  writable   
`cors[]` | `list` | The [bucket's CORS configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#cors). For more information, see [Cross-Origin Resource Sharing](https://docs.cloud.google.com/storage/docs/cross-origin). |  writable   
`customPlacementConfig` | `object` | Applicable only if a bucket is located in a [configurable dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr). The [bucket's custom location configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#customPlacementConfig). |  writable   
`defaultEventBasedHold` | `boolean` | Whether or not to automatically apply [ an `eventBasedHold`](https://docs.cloud.google.com/storage/docs/object-holds#hold-types) to new objects added to the bucket. |  writable   
`defaultObjectAcl[]` | `list` | Default access controls to apply to new objects when no ACL is provided. This list defines an `entity` and `role` for one or more [defaultObjectAccessControls Resources](https://docs.cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls). If `iamConfiguration.uniformBucketLevelAccess.enabled` is set to `true`, this field is omitted in responses, and requests that specify this field fail with a `400 Bad Request` response.  |  writable   
`encryption` | `object` | The [bucket's encryption configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#encryption). |  writable   
`hierarchicalNamespace.enabled` | `boolean` | Whether or not [ hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) is enabled for this bucket. |  writeable   
`iamConfiguration` | `object` | The [bucket's IAM configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#iamConfiguration). |  writable   
`ipFilter` | `object` | The [bucket IP filtering configuration ](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#ipFilter). For more information about bucket IP filtering, see [Bucket IP filtering](https://docs.cloud.google.com/storage/docs/ip-filtering-overview).  |  writable   
`labels` | `object` | User-provided [bucket labels](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels), in key/value pairs. |  writable   
`labels.(key)` | `string` | An individual label entry. |  writable   
`lifecycle` | `object` | The bucket's [lifecycle configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#lifecycle). See [lifecycle management](https://docs.cloud.google.com/storage/docs/lifecycle) for more information.  |  writable   
`location` | `string` | The location of the bucket. Object data for objects in the bucket resides in physical storage within this location. Defaults to `"US"`. See [Cloud Storage bucket locations](https://docs.cloud.google.com/storage/docs/locations) for the authoritative list. |  writable   
`logging` | `object` | The [bucket's logging configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#logging). For more information, see [usage logs and storage logs](https://docs.cloud.google.com/storage/docs/access-logs). |  writable   
`retentionPolicy` | `object` | The [bucket's retention policy configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#retentionPolicy). For more information, see [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock). |  writable   
`rpo` | `string` | The recovery point objective for cross-region replication of the bucket. Applicable only for dual- and multi-region buckets. `"DEFAULT"` uses default replication. `"ASYNC_TURBO"` enables turbo replication, valid for dual-region buckets only. If `rpo` is not specified when the bucket is created, it defaults to `"DEFAULT"`. For more information, see [redundancy across regions](https://docs.cloud.google.com/storage/docs/availability-durability#cross-region-redundancy). |  writable   
`softDeletePolicy` | `object` | The [bucket's soft delete policy configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#softDeletePolicy). For more information, see [Soft Delete](https://docs.cloud.google.com/storage/docs/soft-delete). | writeable  
`storageClass` | `string` | The bucket's default storage class, used whenever no `storageClass` is specified for a newly-created object. If `storageClass` is not specified when the bucket is created, it defaults to `"STANDARD"`. For available storage classes, see [Storage classes](https://docs.cloud.google.com/storage/docs/storage-classes). |  writable   
`versioning` | `object` | The [bucket's versioning configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#versioning). For more information, see [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning). |  writable   
`website` | `object` | The [bucket's website configuration](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#website), controlling how the service behaves when accessing bucket contents as a web site. See the [Static Website Examples](https://docs.cloud.google.com/storage/docs/static-website) for more information. |  writable   
  
## Response

If successful, this method returns a [bucket resource](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#resource) in the response body.

For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
