---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/
title: Objects \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:43.112466+00:00
---

# Objects  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Objects Stay organized with collections  Save and categorize content based on your preferences. 

The Objects resource represents an object within Cloud Storage. Objects are pieces of data that you have uploaded to Cloud Storage. For more information, see [Object Name Requirements](https://docs.cloud.google.com/storage/docs/objects#naming).

Every object in Cloud Storage resides in a [bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#resource). The object is owned by its original uploader, who will always retain `OWNER` permission on it.

In addition to the `acl` property, objects contain [objectAccessControls](https://docs.cloud.google.com/storage/docs/json_api/v1/objectAccessControls), for use in fine-grained manipulation of an existing object's access controls.

To try out the methods for this resource, see Methods.

## Resource representations
    
    
    {
      "kind": "storage#object",
      "id": string,
      "selfLink": string,
      "mediaLink": string,
      "name": string,
      "bucket": string,
      "generation": "long",
      "metageneration": "long",
      "contentType": string,
      "storageClass": string,
      "size": "unsigned long",
      "softDeleteTime": "datetime",
      "restoreToken": string,
      "hardDeleteTime": "datetime",
      "md5Hash": string,
      "contentEncoding": string,
      "contentDisposition": string,
      "contentLanguage": string,
      "cacheControl": string,
      "crc32c": string,
      "componentCount": integer,
      "etag": string,
      "kmsKeyName": string,
      "temporaryHold": boolean,
      "eventBasedHold": boolean,
      "retentionExpirationTime": "datetime",
      "retention": {
        "retainUntilTime": "datetime",
        "mode": string
      }
      "timeCreated": "datetime",
      "timeFinalized": "datetime",
      "updated": "datetime",
      "timeDeleted": "datetime",
      "timeStorageClassUpdated": "datetime",
      "customTime": "datetime",
      "metadata": {
        (key): string
      },
      "acl": [
        [objectAccessControls Resource](https://docs.cloud.google.com/storage/docs/json_api/v1/objectAccessControls#resource)
      ],
      "owner": {
        "entity": string,
        "entityId": string
      },
      "customerEncryption": {
        "encryptionAlgorithm": string,
        "keySha256": string
      },
      "contexts": {
        "custom": {
          (key): {
            "value": string,
            "createTime": "datetime",
            "updateTime": "datetime",
            "extendedDataTypeUrl": string
          }
        }
      }
    }

Property name | Value | Description | Notes  
---|---|---|---  
`acl[]` | `list` | Access controls on the object, containing one or more [objectAccessControls Resources](https://docs.cloud.google.com/storage/docs/json_api/v1/objectAccessControls). Only requests that use the `"projection=full"` query parameter return this field in the response.If `iamConfiguration.uniformBucketLevelAccess.enabled` is set to `true`, this field does not apply, and requests that specify it fail. | writable  
`bucket` | `string` | The name of the bucket containing this object. |   
`cacheControl` | `string` | [Cache-Control](https://datatracker.ietf.org/doc/html/rfc7234#section-5.2) directive for the object data. If omitted, and the object is accessible to all anonymous users, the default is `"public, max-age=3600"`. | writable  
`componentCount` | `integer` | Returned for [composite objects](https://docs.cloud.google.com/storage/docs/composite-objects) only. Number of non-composite objects in the composite object. `componentCount` includes non-composite objects that were part of any composite objects used to [compose](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/compose) the current object. |   
`contentDisposition` | `string` | [Content-Disposition](https://datatracker.ietf.org/doc/html/rfc6266) of the object data. | writable  
`contentEncoding` | `string` | [Content-Encoding](https://datatracker.ietf.org/doc/html/rfc7231#section-3.1.2.2) of the object data. | writable  
`contentLanguage` | `string` | [Content-Language](https://docs.cloud.google.com/storage/docs/metadata#content-language) of the object data. | writable  
`contentType` | `string` | [Content-Type](https://datatracker.ietf.org/doc/html/rfc7231#section-3.1.1.5) of the object data. If an object is stored without a Content-Type, it is served as application/octet-stream. | writable  
`contexts` | `object` | Contexts attached to an object, in key-value pairs. For more information about object contexts, see [Object contexts overview](https://docs.cloud.google.com/storage/docs/object-contexts). |  writable   
`contexts.custom` | `object` | Object contexts attached to the object, in key-value pairs. |  writable   
`contexts.custom.(key)` | `object` | An individual object context. Context keys and their corresponding values must start with an alphanumeric character. They can contain any Unicode characters except single quotes (`'`), double quotes (`"`), backslashes (`\`), and forward slashes (`/`). Additionally, duplicate keys are prohibited. Keys with the prefix `google:` are reserved for Google-generated contexts and you can't create or update them. |  writable   
`contexts.custom.(key).value` | `string` | The value associated with this context. This field holds the primary information for the given context key. |  writable   
`contexts.custom.(key).createTime` | `dateTime` | The time when this object context key was first added to the object. Specified in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`contexts.custom.(key).updateTime` | `dateTime` | The time when this object context key was last updated. Specified in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`contexts.custom.(key).extendedDataTypeUrl` | `string` | The type URL of the context's extended metadata (if any) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)). The value is either `type.googleapis.com/google.protobuf.Struct` or not set. |   
`crc32c` | `string` | CRC32c checksum, as described in [RFC 4960, Appendix B](https://datatracker.ietf.org/doc/html/rfc4960#appendix-B); encoded using [base64](https://datatracker.ietf.org/doc/html/rfc4648#section-4) in big-endian byte order. This field is not present for objects encrypted with customer-managed encryption keys (CMEK). For more information about using the CRC32c checksum, see [Data validation](https://docs.cloud.google.com/storage/docs/data-validation). | writable  
`customerEncryption` | `object` | Metadata of customer-supplied encryption key, if the object is encrypted by such a key. |   
`customerEncryption.encryptionAlgorithm` | `string` | The encryption algorithm. |   
`customerEncryption.keySha256` | `string` | SHA256 hash value of the encryption key; encoded using [base64](https://datatracker.ietf.org/doc/html/rfc4648#section-4). |   
`customTime` | `datetime`1 | A user-specified timestamp for the object. After you set a custom time on an object, the custom time cannot be removed and cannot be set to an earlier datetime. For more information about how to use the custom time, see [custom time metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-time). Specified in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. | writable  
`etag` | `string` | HTTP 1.1 [Entity tag](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3) for the object. |   
`eventBasedHold` | `boolean` | Whether or not the object is subject to an [event-based hold](https://docs.cloud.google.com/storage/docs/object-holds#hold-types). | writable  
`generation` | `long`1 | The content generation of this object. Used for [object versioning](https://docs.cloud.google.com/storage/docs/object-versioning) and [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete). |   
`id` | `string` | The ID of the object, including the bucket name, object name, and generation number. |   
`kind` | `string` | The kind of resource being described. For objects, this is always `"storage#object"`. |   
`kmsKeyName` | `string` | [Cloud KMS key](https://docs.cloud.google.com/kms/docs/resource-hierarchy#retrieve_resource_id) used to encrypt this object, if the object is encrypted by such a key. |   
`md5Hash` | `string` | MD5 hash of the data, encoded using [base64](https://datatracker.ietf.org/doc/html/rfc4648#section-4). This field is not present for [composite objects](https://docs.cloud.google.com/storage/docs/composite-objects) and objects encrypted with customer-managed encryption keys (CMEK). For more information about using the MD5 hash, see [Data validation](https://docs.cloud.google.com/storage/docs/data-validation). | writable  
`mediaLink` | `string` | A URL for downloading the object's data. You should generally use one of the other [JSON API endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints#typical) instead. |   
`metadata` | `object` | User-provided metadata, in key-value pairs. | writable  
`metadata.(key)` | `string` | An individual metadata entry. | writable  
`metageneration` | `long`1 | The version of the metadata for this object at this generation. Used for preconditions and for detecting changes in metadata. A metageneration number is only meaningful in the context of a particular generation of a particular object. |   
`name` | `string` | The name of the object. Required if not specified by URL parameter. | writable  
`owner` | `object` | The owner of the object. This is always the uploader of the object. Only requests that use the `"projection=full"` query parameter return this field in the response.If `iamConfiguration.uniformBucketLevelAccess.enabled` is set to `true`, this field does not apply. |   
`owner.entity` | `string` | The entity, in the form `"user-emailAddress"`. |   
`owner.entityId` | `string` | The ID for the entity. |   
`restoreToken` | `string` | Applicable in buckets with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled. The `restoreToken` is a universally unique identifier (UUID) associated with each [soft-deleted object](https://docs.cloud.google.com/storage/docs/soft-delete) and can be used in requests to restore a soft-deleted object or retrieve its metadata. The `restoreToken` is only required when the `name` and `generation` values of an object [do not uniquely identify it](https://docs.cloud.google.com/storage/docs/soft-delete#restore-tokens). Otherwise, including a `restoreToken` is optional. |   
`retention` | `object` | The object's [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock), which defines the earliest datetime that the object can be deleted or replaced. | writable  
`retention.mode` | `string` | The mode of the retention configuration, which can be either `Unlocked` or `Locked`. If set to `Locked`, `retention.mode` cannot be changed, the retention configuration cannot be removed, and `retention.retainUntilTime` cannot be reduced. | writable  
`retention.retainUntilTime` | `datetime`1 |  The earliest time that the object can be deleted or replaced. This value is independent of any retention policy that is set for the bucket that contains the object. The maximum value is 3,155,760,000 seconds (100 years) from the current date and time. Specified in protocol buffer Timestamp format when returned from a Pub/Sub notification, otherwise specified in RFC 3339 format. | writable  
`retentionExpirationTime` | `datetime`1 | The earliest time that the object can be deleted. This value depends on both the [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock) that is set for the object, and on the [retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock#retention-policy) that is set for the bucket that contains the object. Specified in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`selfLink` | `string` | A URL for this object. You should generally use one of the other [JSON API endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints#typical) instead. |   
`size` | `unsigned long`1 | [Content-Length](https://datatracker.ietf.org/doc/html/rfc7230#section-3.3.2) of the data in bytes. |   
`softDeleteTime` | `datetime` | The time at which the object was [soft deleted](https://docs.cloud.google.com/storage/docs/soft-delete). Only available for objects in buckets with a soft delete policy. |   
`hardDeleteTime` | `datetime` | The time at which a soft-deleted object will be permanently deleted and can no longer be restored. This value is the sum of the values of the soft delete time and the retention duration that is set in the bucket's retention policy. Only available for objects in buckets with a soft delete policy. Note that the value for the hard delete time is permanent after it's set and does not change in response to changes in the retention duration. |   
`storageClass` | `string` | [Storage class](https://docs.cloud.google.com/storage/docs/storage-classes) of the object. To change an object's storage class, use [objects rewrite](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite). | writable  
`temporaryHold` | `boolean` | Whether or not the object is subject to a [temporary hold](https://docs.cloud.google.com/storage/docs/object-holds#hold-types). | writable  
`timeCreated` | `datetime`1 | The creation time of the object. This timestamp doesn't change. Specified in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`timeFinalized` | `datetime`1 | The finalization time of the object. Specified in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`timeDeleted` | `datetime`1 | The deletion time of the object. Returned if and only if this version of the object is no longer a live version, but remains in the bucket as a [noncurrent version](https://docs.cloud.google.com/storage/docs/object-versioning). Specified in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`timeStorageClassUpdated` | `datetime`1 | The time at which the object's storage class was last changed. When the object is initially created, the value is set to the object's creation time. |   
`updated` | `datetime`1 | The most recent modification time of the object metadata. This value is initially set to the object's creation time, and then updated whenever any metadata of the object changes. This includes changes made by a requester, such as modifying custom metadata, as well as changes made by Cloud Storage on behalf of a requester, such as changing the storage class based on an [Object Lifecycle Configuration](https://docs.cloud.google.com/storage/docs/lifecycle). Specified in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
1 This property is a string formatted as the specified value type. 

## Methods

Available methods for Objects resources are as follows:

[bulkRestore](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/bulkRestore)
    Asynchronously restores the soft-deleted objects in a bucket.
[compose](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/compose)
    Concatenates a list of existing objects into a new object in the same bucket.
[copy](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/copy)
    Copies a source object to a destination object. Optionally overrides metadata.
[delete](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/delete)
    Deletes an object and its metadata. Deletions are permanent if versioning is not enabled for the bucket, or if the `generation` parameter is used.
[get](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/get)
    Retrieves an object or its metadata.
[insert](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/insert)
    Stores a new object and metadata. For more information about writing data to Cloud Storage, see [Object uploads](https://docs.cloud.google.com/storage/docs/uploads).
[list](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list)
    Retrieves a list of objects matching the criteria.
[move](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/move)
    Moves an object within a bucket with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled.
[patch](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/patch)
    Updates a data blob's associated metadata. This method supports [patch](https://docs.cloud.google.com/storage/docs/json_api#patch) semantics.
[restore](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/restore)
    Restores a soft-deleted object.
[rewrite](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite)
    Rewrites a source object to a destination object. Optionally overrides metadata.
[update](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/update)
    Updates an object's metadata.
[viewFullContext](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/viewFullContext)
    Retrieves a single object context, including its extended data, by key.

For information about status and error codes returned by these APIs, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
