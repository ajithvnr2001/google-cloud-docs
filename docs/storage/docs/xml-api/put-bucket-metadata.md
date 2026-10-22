---
url: https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata/
title: Set bucket metadata \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:47.544445+00:00
---

# Set bucket metadata  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Set bucket metadata Stay organized with collections  Save and categorize content based on your preferences. 

Updates the metadata of a bucket. For a list of all bucket metadata, see [Bucket metadata](https://docs.cloud.google.com/storage/docs/bucket-metadata).

To update a bucket's metadata using the XML API, you send a `PUT` request that is scoped to the bucket. In the query, provide the query string parameter that indicates which metadata you want to update. In the request body, provide an XML document that defines the specific metadata changes. Each `PUT` request can modify only one type of bucket metadata.

To use the `PUT Bucket` method, you must authenticate and have `FULL_CONTROL` permission.

## Query string parameters

Exactly one of the following query parameters should be included as part of the request to change the bucket's metadata.

Parameter | Description | Required  
---|---|---  
`[billing](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#billing)` | Enable or disable the [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) feature for a bucket. | No  
`[cors](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#cors)` | Add, change, or remove the [CORS configuration](https://docs.cloud.google.com/storage/docs/cross-origin) for a bucket. | No  
`[encryptionConfig](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#encryptionconfig)` | Configure the encryption settings for a bucket:

  * Add, change, or remove the [default customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) for a bucket.
  * Change [which encryption methods are allowed or restricted](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types) for new objects in a bucket. Changing a bucket's encryption enforcement configuration doesn't affect the encryption type of any objects that already exist in the bucket.

| No  
`[lifecycle](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#lifecycle)` | Add, change, or remove the [lifecycle configuration](https://docs.cloud.google.com/storage/docs/lifecycle) for a bucket. | No  
`[logging](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#logging)` | Add, change, or remove the [logging configuration](https://docs.cloud.google.com/storage/docs/access-logs) for a bucket. | No  
`[storageClass](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#storageClass)` |  Change the default [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) for a bucket. Changing a bucket's default storage class doesn't affect the storage class of objects that already exist in the bucket.  | No  
`[tagging](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#tagging)` | Add, change, or remove the [labels](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels) for a bucket.  | No  
`[versioning](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#versioning)` | Enable or disable [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) for a bucket. | No  
`[websiteConfig](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#websiteConfig)` | Add, change, or remove the [website configuration](https://docs.cloud.google.com/storage/docs/static-website) for a bucket. | No  
  
See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

See [common request headers](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket#request-headers).

## Request body elements

You should structure the request body based on the query parameter you use in the request. The contents included in the request body replace any existing settings or configurations for the specified metadata.

### `?billing`

The following request body elements are applicable only if you use the `billing` query string parameter to [enable or disable Requester Pays](https://docs.cloud.google.com/storage/docs/using-requester-pays) for an existing bucket.

Element | Description  
---|---  
`BillingConfiguration` | The container for `RequesterPays`.  
`RequesterPays` | The status to apply to the Requester Pays feature. Accepted values are `Enabled` and `Disabled`.  
  
### `?cors`

The following request body elements are applicable only if you use the `cors` query string parameter to [specify CORS for an existing bucket](https://docs.cloud.google.com/storage/docs/using-cors).

Element | Description  
---|---  
`CorsConfig` | Container for one or more `Cors` configuration containers. If you specify multiple `Cors` containers, the configurations are evaluated in the order listed within the `CorsConfig` container, with the first `Cors` container that has a configuration matching the Origin and Method of a request used to determine any CORS response headers to add to the response.  
`Cors` | Container for a `CORS` configuration to be applied to the bucket. You can specify multiple Origins and multiple Methods in each `Cors` container. There will be a match if the request Origin matches any of the `Origins` in the `Cors` container and the request Method matches any of the `Methods` in the `Cors` container.  
`Origins` | Container for one or more `Origin` elements, specifying the origins permitted for cross origin resource sharing with this Cloud Storage bucket.  
`Origin` | An Origin permitted for cross origin resource sharing with this Cloud Storage bucket. For example, `https://origin1.example.com`. If you supply a value that consists of only the wildcard (`<Origin>*</Origin>`), this gives access to ALL origins.  
`Methods` | Container for one or more `Method` elements, specifying the HTTP methods permitted in cross origin resource sharing with this Cloud Storage bucket.  
`Method` | An HTTP method used in this configuration. Valid values are `DELETE`, `GET`, `HEAD`, `POST`, and `PUT`. `OPTIONS` is interpreted as a preflight request, so you don't need to specify this method in your CORS configuration.  
`ResponseHeaders` | Optional container for one or more `ResponseHeader` elements.  
`ResponseHeader` | Specifies a response header that the user agent is permitted to share across origins.  
`MaxAgeSec` | This value is used to respond to preflight requests, indicating the number of seconds that the client (browser) is allowed to make requests before the client must repeat the preflight request. (Indicates cache expiry time.) Preflight requests are required if the request method contains [non-simple headers](http://www.w3.org/TR/cors/#simple-method) or if the request method is not `POST`, `GET`, or `HEAD`. The value is returned in the `Access-Control-Max-Age` header in responses to preflight requests.  
  
### `?encryptionConfig`

The following request body elements are applicable only if you use the `encryptionConfig` query string parameter to configure the encryption settings for an existing bucket.

Element | Description  
---|---  
`EncryptionConfiguration` |  Container that defines the following encryption settings for the bucket:

  * The [default customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys), represented by the `DefaultKmsKeyName` element.
  * [Which encryption methods are allowed or restricted](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types) for new objects in the bucket, represented by the elements `CustomerManagedEncryptionEnforcement`, `CustomerSuppliedEncryptionEnforcement`, and `GoogleManagedEncryptionEnforcement`.

If this element is empty, then all encryption methods are allowed, and the existing default Cloud Key Management Service key (if any) is removed.  
`DefaultKmsKeyName` | The name of the Cloud KMS key resource to use by default for new objects added to the bucket. If this element is omitted, then the existing default Cloud KMS key (if any) is removed.  
`CustomerManagedEncryptionEnforcement` |  Controls the use of [customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) to encrypt objects in this bucket. If omitted, then creating new objects with CMEKs is allowed. If set, then new objects must comply with the encryption enforcement configuration. This property applies when new objects are created, including when soft-deleted objects are restored. Changing this property has no effect on existing objects. This element is a container for a `RestrictionMode` element.  
`CustomerSuppliedEncryptionEnforcement` |  Controls the use of [customer-supplied encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys) to encrypt objects in this bucket. If omitted, then creating new objects with customer-supplied encryption keys is allowed. If set, then new objects must comply with the encryption enforcement configuration. This property applies when new objects are created, including when soft-deleted objects are restored. Changing this property has no effect on existing objects. This element is a container for a `RestrictionMode` element.  
`GoogleManagedEncryptionEnforcement` |  Controls the use of [standard encryption (Google default encryption)](https://docs.cloud.google.com/storage/docs/encryption) to encrypt objects in this bucket. If omitted, then creating new objects with standard encryption is allowed. If set, then new objects must comply with the encryption enforcement configuration. This property applies when new objects are created, including when soft-deleted objects are restored. Changing this property has no effect on existing objects. This element is a container for a `RestrictionMode` element.  
`RestrictionMode` |  The enforcement configuration for an encryption method. The following values are supported:

  * `NotRestricted`: new objects can use the encryption type.
  * `FullyRestricted`: new objects can't use the encryption type.

  
  
### `?lifecycle`

The following request body elements are applicable only if you use the `lifecycle` query string parameter to [set or remove the lifecycle configuration](https://docs.cloud.google.com/storage/docs/managing-lifecycles) for an existing bucket.

Element | Description  
---|---  
`LifecycleConfiguration` | Defines the lifecycle management policies for the bucket, which contains 0 or more (up to 100) rules. Use an empty element (for example, `<LifecycleConfiguration/>`) to disable lifecycle management for the bucket.  
`Rule` | Defines a lifecycle management rule, which is made of an action and the conditions that must be met for the action to occur.  
`Action` | Defines the action to occur. Must contain one and only one action element.  
`AbortIncompleteMultipartUpload` | Action element to abort incomplete [multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads) and delete the parts associated with them. Only supports the following conditions: `Age`, `MatchesPrefix`, and `MatchesSuffix`.  
`Delete` | Action element to delete objects in the bucket.  
`SetStorageClass` | Action element to change the [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) of objects in the bucket.  
`Condition` | Conditions that must be met for the action to occur. A rule must contain at least one condition element.  
`Age` | Condition element that matches objects over the specified age (in days).   
`CreatedBefore` | Condition element that matches objects created before midnight of the specified date in UTC. The value is an ISO date string without a timezone, for example `2019-01-15`.  
`CustomTimeBefore` | Condition element that matches objects whose [`Custom-Time` metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-time) contains a date that's older than the date set by this condition. `CustomTimeBefore` is an ISO date string without a time zone, for example `2020-02-25`.  
`DaysSinceCustomTime` | Condition element that matches objects whose [`Custom-Time` metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-time) is more than `DaysSinceCustomTime` days old.  
`DaysSinceNoncurrentTime` | Condition element relevant only for versioned objects. Matches objects that have been noncurrent for more than the specified number of days.  
`IsLive` | Condition element typically only used in conjunction with [object versioning](https://docs.cloud.google.com/storage/docs/object-versioning). When set to `false`, this condition is satisfied for any noncurrent version of an object. When set to `true`, this condition is satisfied for the live version of an object. If you don't use object versioning, all your objects are considered live and match when `IsLive` is `true`.   
`MatchesPrefix` | Condition element that matches objects that have names beginning with the specified prefix. The prefix must meet [object naming requirements](https://docs.cloud.google.com/storage/docs/objects#naming). This condition can be added multiple times to the same rule in order to match more than one prefix.  
`MatchesStorageClass` | Condition element that matches objects of the specified [storage class](https://docs.cloud.google.com/storage/docs/storage-classes). This condition can be added multiple times to the same rule in order to cover more than one storage class.  
`MatchesSuffix` | Condition element that matches objects that have names ending with the specified suffix. The suffix must meet [object naming requirements](https://docs.cloud.google.com/storage/docs/objects#naming). This condition can be added multiple times to the same rule in order to match more than one suffix.  
`NoncurrentTimeBefore` | Condition element relevant only for versioned objects. Matches objects that became [noncurrent](https://docs.cloud.google.com/storage/docs/object-versioning) on a date prior to the date specified in this condition. `NoncurrentTimeBefore` is an ISO date string without a time zone, for example `2020-02-25`.  
`NumberOfNewerVersions` | Condition element relevant only for versioned objects. If the value is N, the condition is satisfied when there are at least N versions (including the live version) newer than this version of the object.  
`SizeAboveBytes` | Condition element that matches objects whose size in bytes, excluding metadata, is larger than the specified value.  
`SizeBelowBytes` | Condition element that matches objects whose size in bytes, excluding metadata, is smaller than the specified value.  
  
### `?logging`

The following request body elements are applicable only if you use the `logging` query string parameter to [specify the logging configuration](https://docs.cloud.google.com/storage/docs/access-logs) for an existing bucket.

Element | Description  
---|---  
`Logging` | Container for a logging configuration. Use an empty element (for example, `<Logging/>`) to disable logging for the bucket.  
`LogBucket` | The bucket that will receive log objects. Must be a [valid bucket name](https://docs.cloud.google.com/storage/docs/buckets#naming). Required.  
`LogObjectPrefix` | The object prefix for log objects. It can be at most 900 characters and must be a [valid object name](https://docs.cloud.google.com/storage/docs/objects#naming). Optional.  
  
### `?storageClass`

The following request body element is applicable only if you use the `storageClass` query string parameter to [specify the storage class](https://docs.cloud.google.com/storage/docs/changing-default-storage-class) for an existing bucket.

Element | Description  
---|---  
`StorageClass` | Defines the default storage class for the bucket.  
  
### `?tagging`

The following request body elements are applicable only if you use the `tagging` query string parameter to [set the labels](https://docs.cloud.google.com/storage/docs/using-bucket-labels) for an existing bucket.

Element | Description  
---|---  
`Tagging` | The container for `TagSet`.  
`TagSet` | The container for all labels that are applied to the bucket.  
`Tag` | A container for an individual label. A label is composed of a `key:value` pair.  
`Key` | The key for a label.  
`Value` | The value for a label.  
  
### `?versioning`

The following request body elements are applicable only if you use the `versioning` query string parameter to [enable or disable Object Versioning](https://docs.cloud.google.com/storage/docs/using-object-versioning) for an existing bucket.

Element | Description  
---|---  
`VersioningConfiguration` | Container for versioning configuration.  
`Status` | Status of versioning for this bucket. Can be either `Enabled` or `Suspended`.  
  
### `?websiteConfig`

The following request body elements are applicable only if you use the `websiteConfig` query string parameter to specify a website configuration for an existing bucket.

A bucket's website configuration only applies to requests that use a [`CNAME` or `A` redirect](https://docs.cloud.google.com/storage/docs/request-endpoints#custom-domains). For more information on using a bucket to host a static website, including other options for setting your website configuration, see [Hosting a Static Website](https://docs.cloud.google.com/storage/docs/hosting-static-website).

Element | Description  
---|---  
`WebsiteConfiguration` | Container for website configuration.  
`MainPageSuffix` |  An object name suffix to simulate directory index behavior. Must be a [valid object name](https://docs.cloud.google.com/storage/docs/objects#naming). Optional.   
`NotFoundPage` |  Name of the object to return with 404 responses. Must be a [valid object name](https://docs.cloud.google.com/storage/docs/objects#naming). Optional.   
  
## Request syntax

The following syntax applies to PUT Bucket requests that change the metadata for a bucket.
    
    
    PUT /?METADATA_QUERY_PARAMETER HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Date: DATE_AND_TIME_OF_REQUEST
    Content-Length: REQUEST_BODY_LENGTH
    Content-Type: MIME_TYPE_OF_REQUEST_BODY
    Authorization: AUTHENTICATION_STRING
    
    XML_DOCUMENT_DEFINING_BUCKET_METADATA
    

## Response headers

The request can return a variety of response headers depending on the request headers you use.

## Response body elements

The response does not include an XML document in the response body.

## Example

The following sample sets a CORS configuration on a bucket named `acme-pets`. This CORS configuration sets two origins and the HTTP methods allowed for those origins. In this example, all of the available HTTP methods are allowed.

**Request**
    
    
    PUT /?cors HTTP/1.1
    Host: acme-pets.storage.googleapis.com
    Date: Thu, 12 Mar 2022 03:38:42 GMT
    Content-Length: 1320
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    
    <?xml version="1.0" encoding="UTF-8"?>
    <CorsConfig>
      <Cors>
        <Origins>
          <Origin>http://origin1.example.com</Origin>
          <Origin>http://origin2.example.com</Origin>
        </Origins>
        <Methods>
          <Method>GET</Method>
          <Method>HEAD</Method>
          <Method>PUT</Method>
          <Method>POST</Method>
          <Method>DELETE</Method>
        </Methods>
        <ResponseHeaders>
          <ResponseHeader>x-goog-meta-foo1</ResponseHeader>
          <ResponseHeader>x-goog-meta-foo2</ResponseHeader>
        </ResponseHeaders>
        <MaxAgeSec>1800</MaxAgeSec>
      </Cors>
    </CorsConfig>
    
    

**Response**
    
    
    HTTP/1.1 200 OK
    Date: Thu, 12 Mar 2012 03:38:42 GMT
    Expires: Mon, 01 Jan 1990 00:00:00 GMT
    Cache-Control: no-cache, no-store, must-revalidate
    Content-Length: 0
    Content-Type: text/html
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
