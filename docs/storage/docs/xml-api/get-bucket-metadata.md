---
url: https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-metadata/
title: Get bucket metadata \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:17:44.474489+00:00
---

# Get bucket metadata  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Get bucket metadata Stay organized with collections  Save and categorize content based on your preferences. 

To get a bucket's metadata, you make a `GET` request that is scoped to a bucket, and you use the appropriate query string parameter. The requested metadata is returned in an XML document in the response body. When using the XML API, each request can only return one part of a bucket's metadata.

You must have `READ` permission to send requests that get bucket metadata. Also, you must be authenticated to use the `GET Bucket` method.

## Query string parameters

Exactly one of the following query parameters should be included as part of the request to get the bucket's metadata.

Parameter | Description | Required  
---|---|---  
`[billing](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#billing)` | Return the status of the [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) feature for a bucket. | No  
`[cors](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#cors)` | Return the [CORS configuration](https://docs.cloud.google.com/storage/docs/cross-origin) for a bucket. | No  
`[customPlacementConfig](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#customplacementconfig)` | Applicable to buckets located in [configurable dual-regions](https://docs.cloud.google.com/storage/docs/locations#location-dr). Return the regions that constitute the configurable dual-region that a bucket is located within. | No  
`[encryptionConfig](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#encryptionconfig)` | Return the encryption settings for a bucket:

  * The [default customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) for a bucket
  * [Which encryption methods are allowed or restricted](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types) for new objects in a bucket

| No  
`[lifecycle](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#lifecycle)` | Return the [lifecycle configuration](https://docs.cloud.google.com/storage/docs/lifecycle) for a bucket. | No  
`[location](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#location_querystring)` | Return the location of the bucket. Returned values can include a region, predefined dual-region, or multi-region name. For a list of possible locations, see [bucket locations](https://docs.cloud.google.com/storage/docs/locations). | No  
`[logging](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#logging)` | Return the [logging configuration](https://docs.cloud.google.com/storage/docs/access-logs) for a bucket. | No  
`[object-lock](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#objectlock)` | Return the [object retention configuration](https://docs.cloud.google.com/storage/docs/object-lock) of a bucket. If object retention is not enabled for the requested bucket, the request fails with a 404 response. | No  
`[storageClass](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#storageClass)` |  Return the default [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) for a bucket.  | No  
`[tagging](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#tagging)` | Return the [labels](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels) for a bucket.  | No  
`[versioning](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#versioning)` | Return the status of [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) for a bucket. | No  
`[websiteConfig](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#websiteConfig)` | Return the [website configuration](https://docs.cloud.google.com/storage/docs/static-website) for a bucket. | No  
  
See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

See [common request headers](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket#request-headers).

## Request body elements

This request does not include an XML document in the request body.

## Request syntax

The following syntax applies to GET Bucket requests that return the metadata for a bucket.
    
    
    GET /?METADATA_QUERY_PARAMETER HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Date: DATE_AND_TIME_OF_REQUEST
    Content-Length: 0
    Authorization: AUTHENTICATION_STRING
    

## Response headers

The request can return a variety of response headers depending on the request headers you use.

## Response body elements

The contents of the response body depends on the query parameter you use in the request.

### `?billing`

The following response body elements are applicable only if you use the `billing` query string parameter to [get the status of Requester Pays](https://docs.cloud.google.com/storage/docs/using-requester-pays) for an existing bucket.

Element | Description  
---|---  
`BillingConfiguration` | The container for `RequesterPays`.  
`RequesterPays` | The status of the Requester Pays feature. The status is given as `Enabled` or `Disabled`.  
  
### `?cors`

The following response body elements are applicable only if you use the `cors` query string parameter to [get the CORS configuration](https://docs.cloud.google.com/storage/docs/using-cors) for an existing bucket.

Element | Description  
---|---  
`CorsConfig` | Container for one or more `Cors` configuration containers. The configurations are evaluated in the order listed within the `CorsConfig` container, with the first `Cors` container that has a configuration matching the Origin and Method of a request used to determine any CORS response headers to add to the response.  
`Cors` | Container for a `CORS` configuration that is applied to the bucket. There might be multiple Origins and multiple Methods in each `Cors` container.  
`Origins` | Container for one or more `Origin` elements, specifying the origins permitted for cross origin resource sharing with this Cloud Storage bucket.  
`Origin` | An Origin permitted for cross origin resource sharing with this Cloud Storage bucket. An origin that consists of only the wildcard (`<Origin>*</Origin>`) gives access to ALL origins.  
`Methods` | Container for one or more `Method` elements, specifying the HTTP methods permitted in cross origin resource sharing with this Cloud Storage bucket.  
`Method` | An HTTP method used in this configuration.  
`ResponseHeaders` | Optional container for one or more `ResponseHeader` elements.  
`ResponseHeader` | Specifies a response header that the user agent is permitted to share across origins.  
`MaxAgeSec` | This value is used to respond to preflight requests, indicating the number of seconds that the client (browser) is allowed to make requests before the client must repeat the preflight request. (Indicates cache expiry time.) Preflight requests are required if the request method contains [non-simple headers](http://www.w3.org/TR/cors/#simple-method) or if the request method is not `POST`, `GET`, or `HEAD`. The value is returned in the `Access-Control-Max-Age` header in responses to preflight requests.  
  
### `?customPlacementConfig`

The following response body elements are applicable only if you use the `customPlacementConfig` query string parameter to return the regions that constitute the [configurable dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) that a bucket is located within.

If the request applies to a bucket located in a region, multi-region, or predefined dual-region, the response contains an empty `DataLocations` element.

Element | Description  
---|---  
`CustomPlacementConfig` | The container for `DataLocations`  
`DataLocations` | The container for a list of regions that constitute the [configurable dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr).  
`DataLocation` | One of the regions that constitute the [configurable dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr).  
  
### `?encryptionConfig`

The following response body elements are applicable only if you use the `encryptionConfig` query string parameter to get the encryption settings for an existing bucket.

Element | Description  
---|---  
`EncryptionConfiguration` |  Container that defines the following encryption settings for the bucket:

  * The [default customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys), represented by the `DefaultKmsKeyName` element.
  * [Which encryption methods are allowed or restricted](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types) for new objects in the bucket, represented by the elements `CustomerManagedEncryptionEnforcement`, `CustomerSuppliedEncryptionEnforcement`, and `GoogleManagedEncryptionEnforcement`.

If this element is empty, then all encryption methods are allowed, and no default Cloud Key Management Service key is set for the bucket.  
`DefaultKmsKeyName` | The name of the Cloud KMS key resource used by default for objects added to the bucket.  
`CustomerManagedEncryptionEnforcement` |  Controls the use of [customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) to encrypt objects in this bucket. If omitted, then creating new objects with CMEKs is allowed. If set, then new objects must comply with the encryption enforcement configuration. This property applies when new objects are created, including when soft-deleted objects are restored. Changing this property has no effect on existing objects. This element is a container for `RestrictionMode` and `EffectiveTime` elements.  
`CustomerSuppliedEncryptionEnforcement` |  Controls the use of [customer-supplied encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys) to encrypt objects in this bucket. If omitted, then creating new objects with customer-supplied encryption keys is allowed. If set, then new objects must comply with the encryption enforcement configuration. This property applies when new objects are created, including when soft-deleted objects are restored. Changing this property has no effect on existing objects. This element is a container for `RestrictionMode` and `EffectiveTime` elements.  
`GoogleManagedEncryptionEnforcement` |  Controls the use of [standard encryption (Google default encryption)](https://docs.cloud.google.com/storage/docs/encryption) to encrypt objects in this bucket. If omitted, then creating new objects with standard encryption is allowed. If set, then new objects must comply with the encryption enforcement configuration. This property applies when new objects are created, including when soft-deleted objects are restored. Changing this property has no effect on existing objects. This element is a container for `RestrictionMode` and `EffectiveTime` elements.  
`RestrictionMode` |  The enforcement configuration for an encryption method. The following values are supported:

  * `NotRestricted`: new objects can use the encryption type.
  * `FullyRestricted`: new objects can't use the encryption type.

  
`EffectiveTime` |  The time when the encryption enforcement configuration for an encryption method was set to `FullyRestricted`. This element is returned only when an encryption type is restricted. If you update a bucket to allow a specific encryption type, then the `EffectiveTime` field for that encryption type is cleared. Specified in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format.  
  
### `?lifecycle`

The following response body elements are applicable only if you use the `lifecycle` query string parameter to [get the lifecycle configuration](https://docs.cloud.google.com/storage/docs/managing-lifecycles) for an existing bucket.

Element | Description  
---|---  
`LifecycleConfiguration` | Container for one or more `Rule` elements, which define the object lifecycle management configuration for the bucket. If this element is empty, the bucket does not have an object lifecycle management configuration set for it.  
`Rule` | Defines a lifecycle management rule, which is made of an action and the conditions that must be met for the action to occur.  
`Action` | Defines the action to occur. Every `Rule` has exactly one and action element.  
`AbortIncompleteMultipartUpload` | Action element to abort incomplete [multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads) and delete the parts associated with them.  
`Delete` | Action element to delete objects in the bucket.  
`SetStorageClass` | Action element to change the [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) of objects in the bucket.  
`Condition` | Conditions that must be met for the action to occur. Every `Rule` contains at least one condition element.  
`Age` | Condition element that matches objects over the specified age (in days).   
`CreatedBefore` | Condition element that matches objects created before midnight of the specified date in UTC. The value is an ISO date string without a timezone, for example `2019-01-15`.  
`CustomTimeBefore` | Condition element that matches objects whose [`Custom-Time` metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-time) contains a date that's older than the date set by this condition. `CustomTimeBefore` is an ISO date string without a time zone, for example `2020-02-25`.  
`DaysSinceCustomTime` | Condition element that matches objects whose [`Custom-Time` metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-time) is more than `DaysSinceCustomTime` days old.  
`DaysSinceNoncurrentTime` | Condition element relevant only for versioned objects. Matches objects that have been noncurrent for more than the specified number of days.  
`IsLive` | Condition element typically only used in conjunction with [object versioning](https://docs.cloud.google.com/storage/docs/object-versioning). When set to `false`, this condition is satisfied for any noncurrent version of an object. When set to `true`, this condition is satisfied for the live version of an object. If you don't use object versioning, all your objects are considered live and match when `IsLive` is `true`.   
`MatchesPrefix` | Condition element that matches objects whose names begin with the specified [prefix](https://docs.cloud.google.com/storage/docs/lifecycle#matchesprefix-suffix).  
`MatchesStorageClass` | Condition element that matches objects of the specified [storage class](https://docs.cloud.google.com/storage/docs/storage-classes).  
`MatchesSuffix` | Condition element that matches objects whose names end with the specified [suffix](https://docs.cloud.google.com/storage/docs/lifecycle#matchesprefix-suffix).  
`NoncurrentTimeBefore` | Condition element relevant only for versioned objects. Matches objects that became [noncurrent](https://docs.cloud.google.com/storage/docs/object-versioning) on a date prior to the date specified in this condition. `NoncurrentTimeBefore` is an ISO date string without a time zone, for example `2020-02-25`.  
`NumberOfNewerVersions` | Condition element relevant only for versioned objects. If the value is N, the condition is satisfied when there are at least N versions (including the live version) newer than this version of the object.  
`SizeAboveBytes` | Condition element that matches objects whose size in bytes, excluding metadata, is larger than the specified value.  
`SizeBelowBytes` | Condition element that matches objects whose size in bytes, excluding metadata, is smaller than the specified value.  
  
### `?location`

The following response body element is applicable only if you use the `location` query string parameter to [get the location](https://docs.cloud.google.com/storage/docs/getting-bucket-metadata) for an existing bucket. Note that for configurable dual-regions, additional location information can be obtained by making a request for the bucket's custom placement configuration, using the `customPlacementConfig` query string.

Element | Description  
---|---  
`LocationConstraint` | The location of the bucket. Can be the name of a single region, predefined dual-region, or multi-region. For a list of locations, see [bucket locations](https://docs.cloud.google.com/storage/docs/locations).  
  
### `?logging`

The following response body elements are applicable only if you use the `logging` query string parameter to [get the logging configuration](https://docs.cloud.google.com/storage/docs/access-logs) for an existing bucket.

Element | Description  
---|---  
`Logging` | Container for a logging configuration. If the element is empty, logging is disabled for the bucket.  
`LogBucket` | The bucket that will receive log objects.  
`LogObjectPrefix` | The object prefix for log objects.  
  
### `?object-lock`

The following response body elements are applicable only if you use the `object-lock` query string parameter to [display bucket's object retention configuration](https://docs.cloud.google.com/storage/docs/using-object-lock).

Element | Description  
---|---  
`ObjectLockConfiguration` | Container for the object retention configuration.  
`ObjectLockEnabled` | Status of object retention for this bucket. `Enabled` is the only valid value for this element. If object retention is not enabled for the bucket, the overall request fails with a 404 response.  
  
### `?storageClass`

The following response body element is applicable only if you use the `storageClass` query string parameter to [get the storage class](https://docs.cloud.google.com/storage/docs/changing-default-storage-class) for an existing bucket.

Element | Description  
---|---  
`StorageClass` | The default storage class for the bucket.  
  
### `?tagging`

The following response body elements are applicable only if you use the `tagging` query string parameter to [get the labels](https://docs.cloud.google.com/storage/docs/using-bucket-labels) for an existing bucket.

Element | Description  
---|---  
`Tagging` | The container for `TagSet`.  
`TagSet` | The container for all labels that are applied to the bucket.  
`Tag` | A container for an individual label. A label is composed of a `key:value` pair.  
`Key` | The key for a label.  
`Value` | The value for a label.  
  
### `?versioning`

The following response body elements are applicable only if you use the `versioning` query string parameter to [get the status of Object Versioning](https://docs.cloud.google.com/storage/docs/using-object-versioning) for an existing bucket.

Element | Description  
---|---  
`VersioningConfiguration` | Container for versioning configuration. This element can be empty if Object Versioning is not enabled for the bucket.  
`Status` | Status of versioning for this bucket. Can be either `Enabled` or `Suspended`.  
  
### `?websiteConfig`

The following response body elements are applicable only if you use the `websiteConfig` query string parameter to get the website configuration for an existing bucket.

Element | Description  
---|---  
`WebsiteConfiguration` | Container for website configuration. If the element is empty, there is no website configuration for the bucket.  
`MainPageSuffix` | The object name suffix used to simulate directory index behavior.  
`NotFoundPage` | Name of the object to return with 404 responses.  
  
## Example

The following example retrieves the labels for a bucket named `my-bucket`. In this example, the bucket has two labels applied to it.

**Request**
    
    
    GET /?tagging HTTP/1.1
    Host: my-bucket.storage.googleapis.com
    Date: Thu, 24 Jan 2016 02:34:56 GMT
    Content-Length: 0
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

**Response**
    
    
    HTTP/1.1 200 OK
    Date: Thu, 16 Nov 2023 02:34:56 GMT
    Expires: Mon, 01 Jan 1990 00:00:00 GMT
    Cache-Control: no-cache, no-store, must-revalidate
    Content-Length: 196
    Content-Type: text/html
    
    <?xml version="1.0" encoding="UTF-8"?>
    <Tagging>
      <TagSet>
         <Tag>
           <Key>environment</Key>
           <Value>production</Value>
         </Tag>
         <Tag>
           <Key>billing</Key>
           <Value>marketing-department</Value>
         </Tag>
      </TagSet>
    </Tagging>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
