---
url: https://docs.cloud.google.com/storage/docs/metadata/
title: Object metadata \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:56.335577+00:00
---

# Object metadata  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Object metadata Stay organized with collections  Save and categorize content based on your preferences. 

The metadata for a Cloud Storage object identifies the object's properties and lets you control how the object behaves. An object's metadata includes non-editable fields such as the object's generation number, as well as configurable settings like caching behavior, retention configuration, and custom metadata.

## Overview of object metadata

Metadata is stored as _key-value pairs_. For example, the [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) of an object is represented by the metadata entry `storageClass:STANDARD`. `storageClass` is the _key_ for the metadata, and all objects have such a key associated with them. `STANDARD` specifies the _value_ this specific object has, and the value differs from object to object.

The mutability of metadata varies: some metadata you can edit at any time, some metadata you can only set at the time the object is created, and some metadata you can only view. For example, you can edit the value of the `Cache-Control` metadata at any time, but you can only assign the `storageClass` metadata when the object is created or rewritten, and you cannot directly edit the value for the `generation` metadata, though the `generation` value changes when the object is replaced.

## Editable metadata

You can edit the following categories of object metadata:

  * **Fixed-key metadata** : Metadata whose keys are set, but for which you can specify a value.

  * **Custom metadata** : Metadata that you add by specifying both a key and a value associated with the key.




When editing metadata, you should generally avoid non-ascii characters, because they are not permitted in HTTP headers, which the XML API uses.

For steps to edit object metadata, see [View and edit object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata).

### Fixed-key metadata

You can edit the following metadata for objects, though you must have sufficient [permission](https://docs.cloud.google.com/storage/docs/access-control/iam) to do so. To update fixed-key metadata for millions or billions of objects in bulk with a single job, use [Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview).

  * Access control metadata
  * Cache-Control
  * Content-Disposition
  * Content-Encoding
  * Content-Language
  * Content-Type
  * Custom-Time
  * Object contexts
  * Object holds
  * Retention configuration



#### Access control metadata

Cloud Storage uses [Identity and Access Management (IAM)](https://docs.cloud.google.com/storage/docs/access-control/iam) and [Access Control Lists (ACLs)](https://docs.cloud.google.com/storage/docs/access-control/lists) to control access to objects. Use these links to learn about these access control methods and associated metadata.

#### Cache-Control

The `Cache-Control` metadata can specify two different aspects of how data is served from Cloud Storage: whether the data can be cached and whether the data can be transformed.

**Note:** `Cache-Control` is also a header you can specify in your HTTP requests for an object; however, Cloud Storage ignores this header and sets response `Cache-Control` headers based on the stored metadata values.

##### Caching data

The `Cache-Control` metadata lets you control whether and for how long caches are allowed to cache your objects, which can then be served to satisfy future requests. Caches can include browser and Internet caches, as well as [Cloud Storage built-in caching](https://docs.cloud.google.com/storage/docs/caching#built-in).

If an applicable object doesn't have a `Cache-Control` metadata entry, Cloud Storage uses the default value of:

  * `public, max-age=3600`, if the object is not encrypted using a [customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) or stored within a [Virtual Private Cloud service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).

  * `no-cache, no-store, max-age=0`, if the object is encrypted using a [customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys).

  * `private, max-age=0`, if the object is stored within a [Virtual Private Cloud service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).

  * `no-cache, no-store, max-age=0, must-revalidate`, if the object is stored within a [Virtual Private Cloud service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) **and** encrypted using a [customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys).




If you allow caching, downloads might continue to receive earlier versions of an object, even after uploading a newer version. This is because such earlier versions remain "fresh" in caches for a period of time determined by `max-age`. Additionally, because objects can be cached at various places on the Internet, there is no way to force a cached object to expire globally. This means that if you revoke public access to an object, the object can still be served from a cache, depending on when it was last accessed and its `Cache-Control` setting. For example, if your object was served with a `Cache-Control` of `public, max-age=3600`, it can persist in a cache for an hour. If you want to prevent serving cached versions of publicly readable objects, set `Cache-Control: no-store` on the object.

If you need greater control over cache behavior, you can configure [Cloud CDN in front of your bucket](https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-bucket).

##### Transforming data

`Cache-Control` metadata also lets you serve objects as they are stored, without applying any [transformations](https://docs.cloud.google.com/storage/docs/transcoding) to the data, such as removing gzip content-encoding for incompatible clients. To serve an object as-is, set `Cache-Control:no-transform`.

#### Content-Disposition

The `Content-Disposition` metadata specifies presentation information about the data being transmitted. Setting `Content-Disposition` allows you to control presentation style of the content, for example determining whether an attachment should be automatically displayed or whether some form of action from the user should be required to open it. See <https://datatracker.ietf.org/doc/html/rfc6266> for the `Content-Disposition` specification.

#### Content-Encoding

The `Content-Encoding` metadata can be used to indicate that an object is compressed, while still maintaining the object's underlying `Content-Type`. For example, a text file that is gzip compressed can have the fact that it's a text file indicated in `Content-Type` and the fact that it's gzip compressed indicated in `Content-Encoding`. You should verify that files are, in fact, compressed using the specified `Content-Encoding` before uploading them, or else unexpected behavior can occur when attempting to download the objects. For more information, see the [Transcoding page](https://docs.cloud.google.com/storage/docs/transcoding).

For compressible content, such as text, using `Content-Encoding: gzip` saves network and storage costs and improves content serving performance. However, for content that is already inherently compressed, such as archives and many media formats, applying another level of compression and marking it in the `Content-Encoding` metadata is typically detrimental to both object size and performance and should be avoided.

#### Content-Language

The `Content-Language` metadata indicates the language(s) that the object is intended for. Refer to [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) language codes for typical values of this metadata.

Cloud Storage supports `Content-Language` values up to 100 characters in length.

#### Content-Type

The most commonly set metadata is `Content-Type` (also known as media type), which lets browsers render the object properly. All objects have a value specified in their `Content-Type` metadata, but this value does not have to match the underlying type of the object. For example, if the `Content-Type` is not specified by the uploader and cannot be determined, it is set to `application/octet-stream` or `application/x-www-form-urlencoded`, depending on how you uploaded the object. For a list of valid content types, see the [IANA Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml) page.

**Note:** Some tools, such as `gcloud storage`, attempt to automatically set `Content-Type` at the time of upload based on the extension of the file being uploaded; however, any explicit value that you set for `Content-Type` overrides this mechanism.

#### Custom-Time

The `Custom-Time` metadata is a user-specified date and time represented in the [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format `YYYY-MM-DD'T'HH:MM:SS.SS'Z'` or `YYYY-MM-DD'T'HH:MM:SS'Z'` when milliseconds are zero. This metadata is typically set in order to use the [`DaysSinceCustomTime`](https://docs.cloud.google.com/storage/docs/lifecycle#dayssincecustomtime) condition in Object Lifecycle Management.

You cannot remove `Custom-Time` after it's been set on an object. Additionally, the value for `Custom-Time` cannot decrease. That is, you cannot set `Custom-Time` to be an earlier date/time than the existing `Custom-Time`. You can, however, effectively remove or reset the `Custom-Time` by rewriting the object.

#### Object contexts

Object contexts are user-defined key-value pairs. You can attach them to your objects to manage and discover data. Modifying object contexts updates the object's metageneration number and ETag. For more information, see [Object contexts](https://docs.cloud.google.com/storage/docs/object-contexts).

#### Object holds

Use metadata flags to place object holds, which prevent objects from being deleted or replaced. For more information, see the [Object holds page](https://docs.cloud.google.com/storage/docs/object-holds).

#### Retention configuration

When present, an object's retention configuration defines a date and time prior to which the object can't be deleted or replaced. To update retention configurations for millions or billions of objects with a single job, use [Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview). For more information, see [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock).

### Custom metadata

Custom metadata is metadata for which you define both the key and the value. To create custom metadata, you specify both a key and a value. After you have created a custom metadata `key:value` pair, you can delete the key or change the value. To update custom metadata for millions or billions of objects with a single job, use [Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview).

Custom metadata is subject to a [size limit](https://docs.cloud.google.com/storage/quotas#objects) and incurs [storage costs](https://docs.cloud.google.com/storage/pricing#storage-notes).

The [Viewing and Editing Metadata page](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata) includes information about setting custom metadata.

#### The `x-goog-meta-` prefix

The [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) sets and retrieves object metadata using request headers, and the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) allows setting custom metadata in the final request of a [resumable upload](https://docs.cloud.google.com/storage/docs/resumable-uploads) by using request headers. In order to clearly distinguish custom metadata headers from standard request headers, both APIs prefix such custom metadata headers with `x-goog-meta-`.

## Non-editable metadata

Some metadata cannot be edited directly. This metadata is set at the time of object creation or rewrite. As part of the object creation or rewrite, you can set some such metadata, such as the [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) of the object or [customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys). Other metadata is automatically added and can only be viewed, such the generation number of the object or the time of creation.

### Generation and metageneration numbers

As part of its metadata, every Cloud Storage object has a numeric `generation` property and a numeric `metageneration` property that uniquely identifies the object:

Property | Description  
---|---  
`generation` or `version ID` | Identifies the version of an object, and exists for every object, regardless of whether a bucket uses [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning). In the context of the Amazon S3-compatible API, such as the [multi-object delete XML API](https://docs.cloud.google.com/storage/docs/xml-api/post-bucket), this identifier is referred to as a `version ID`.

  * An object version's `generation` value is unique. A new object with the same name can replace an existing object, but the new object has a different `generation` value.
  * Generation numbers might not increase for future versions, but each new version has a unique generation number.
  * There is no relationship between the generation numbers of unrelated objects, even if the objects are in the same bucket.

  
`metageneration` | Identifies the metadata version, and increases every time the metadata **of a given`generation`** is updated.

  * `metageneration` begins at `1` for each new `generation` of an object.
  * The `metageneration` property has no meaning without the `generation` property and should be used only in conjunction with it; it's meaningless to compare metadata generations of two object versions.

  
  
The `generation` and `metageneration` properties are used in the following circumstances:

  * When using [preconditions in requests](https://docs.cloud.google.com/storage/docs/request-preconditions): Preconditions cause the request to fail if the precondition isn't satisfied. Failing in this manner prevents the request from applying to an unexpected version of an object, such as retrieving the wrong object data or modifying the wrong state of an object's metadata.

  * When [listing, accessing, restoring, and deleting noncurrent object versions](https://docs.cloud.google.com/storage/docs/using-versioned-objects): Noncurrent object versions are specifically relevant in buckets that use or previously used [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning).




### Checksums

Checksums are metadata calculated from the associated object's data. Checksums are used for [validating that object data isn't corrupted](https://docs.cloud.google.com/storage/docs/data-validation). Cloud Storage objects have several checksum metadata fields.

#### CRC32C

All Cloud Storage objects have a [CRC32C hash](https://datatracker.ietf.org/doc/html/rfc4960#appendix-B). Libraries for computing CRC32C include:

  * [Google's CRC32C](https://github.com/google/crc32c) for C++
  * [hash/crc32](https://pkg.go.dev/hash/crc32) for Go
  * [GoogleAPIs Guava](https://guava.dev/releases/31.0.1-jre/api/docs/com/google/common/hash/Hashing.html#crc32c\(\)) for Java
  * [google-crc32c](https://github.com/googleapis/python-crc32c) for Python
  * [digest-crc](https://github.com/postmodern/digest-crc) in Ruby

**Note:** The CRC popularly known as CRC32 differs from the CRC32C algorithm used by Cloud Storage.

The Base64 encoded CRC32C is in big-endian byte order.

#### MD5

Cloud Storage objects have an MD5 hash if they meet the following criteria:

  * The object is not a [composite object](https://docs.cloud.google.com/storage/docs/composite-objects).
  * The object was not uploaded using an [XML API multipart upload](https://docs.cloud.google.com/storage/docs/multipart-uploads).



When a Content-MD5 header is present in the request, Cloud Storage validates the integrity of the object data by comparing the provided MD5 hash with the calculated hash of the uploaded object. If the hashes don't match, the request is rejected.

#### ETags

All Cloud Storage objects have an ETag. However, the same object can have a different ETag value when it's requested from the XML API compared to the JSON API. In most cases, users should make no assumptions about the value used in an ETag except that it changes whenever the underlying data or metadata changes, per the [specification](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3).

An object's ETag header returns the object's MD5 value if all the following are true:

  * The request is being made through the XML API
  * The object only uses [Google-owned and Google-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/default-keys) for server-side encryption
  * The object is not a [composite object](https://docs.cloud.google.com/storage/docs/composite-objects) and was not uploaded using an [XML API multipart upload](https://docs.cloud.google.com/storage/docs/multipart-uploads)



## Timestamps

The metadata for a Cloud Storage object can include the following timestamps. The field names vary depending on the tool or SDK language that you use to work with the object. For SDKs, see the relevant client library documentation.

### Command line

Field name | Description  
---|---  
`creation_time` | The creation time of the object. This timestamp doesn't change.  
`update_time` | The most recent modification time of the object metadata. This value is initially set to the object's creation time, and then updated whenever any metadata of the object changes. This includes changes made by a requester, such as modifying custom metadata, as well as changes made by Cloud Storage on behalf of a requester, such as changing the storage class based on an [Object Lifecycle Configuration](https://docs.cloud.google.com/storage/docs/lifecycle).  
`noncurrent_time` | The deletion time of the object. Returned if and only if this version of the object is no longer a live version, but remains in the bucket as a [noncurrent version](https://docs.cloud.google.com/storage/docs/object-versioning).  
`soft_delete_time` | The time at which the object was [soft deleted](https://docs.cloud.google.com/storage/docs/soft-delete). Only available for objects in buckets with a soft delete policy.  
`hard_delete_time` | The time at which a soft-deleted object will be permanently deleted and can no longer be restored. This value is the sum of the values of the soft delete time and the retention duration that is set in the bucket's retention policy. Only available for objects in buckets with a soft delete policy. Note that the value for the hard delete time is permanent after it's set and does not change in response to changes in the retention duration.  
`retention_settings.retainUntilTime` | The earliest time that the object can be deleted or replaced. This value is independent of any retention policy that is set for the bucket that contains the object. The maximum value is 3,155,760,000 seconds (100 years) from the current date and time.  
`retention_expiration` | The earliest time that the object can be deleted. This value depends on both the [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock) that is set for the object, and on the [retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock#retention-policy) that is set for the bucket that contains the object.  
`storage_class_update_time` | The time at which the object's storage class was last changed. When the object is initially created, the value is set to the object's creation time.  
`finalize_time` | The finalization time of the object.  
`contexts.KEY.createTime` | The time when this object context key was first added to the object.  
`contexts.KEY.updateTime` | The time when this object context key was last updated.  
`custom_time` | A user-specified timestamp for the object. After you set a custom time on an object, the custom time cannot be removed and cannot be set to an earlier datetime. For more information about how to use the custom time, see [custom time metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-time).  
  
### APIs

### JSON API

Field name | Description  
---|---  
`timeCreated` | The creation time of the object. This timestamp doesn't change.  
`updated` | The most recent modification time of the object metadata. This value is initially set to the object's creation time, and then updated whenever any metadata of the object changes. This includes changes made by a requester, such as modifying custom metadata, as well as changes made by Cloud Storage on behalf of a requester, such as changing the storage class based on an [Object Lifecycle Configuration](https://docs.cloud.google.com/storage/docs/lifecycle).  
`timeDeleted` | The deletion time of the object. Returned if and only if this version of the object is no longer a live version, but remains in the bucket as a [noncurrent version](https://docs.cloud.google.com/storage/docs/object-versioning).  
`softDeleteTime` | The time at which the object was [soft deleted](https://docs.cloud.google.com/storage/docs/soft-delete). Only available for objects in buckets with a soft delete policy.  
`hardDeleteTime` | The time at which a soft-deleted object will be permanently deleted and can no longer be restored. This value is the sum of the values of the soft delete time and the retention duration that is set in the bucket's retention policy. Only available for objects in buckets with a soft delete policy. Note that the value for the hard delete time is permanent after it's set and does not change in response to changes in the retention duration.  
`retention.retainUntilTime` | The earliest time that the object can be deleted or replaced. This value is independent of any retention policy that is set for the bucket that contains the object. The maximum value is 3,155,760,000 seconds (100 years) from the current date and time.  
`retentionExpirationTime` | The earliest time that the object can be deleted. This value depends on both the [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock) that is set for the object, and on the [retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock#retention-policy) that is set for the bucket that contains the object.  
`timeStorageClassUpdated` | The time at which the object's storage class was last changed. When the object is initially created, the value is set to the object's creation time.  
`timeFinalized` | The finalization time of the object.  
`contexts.custom.KEY.createTime` | The time when this object context key was first added to the object.  
`contexts.custom.KEY.updateTime` | The time when this object context key was last updated.  
`customTime` | A user-specified timestamp for the object. After you set a custom time on an object, the custom time cannot be removed and cannot be set to an earlier datetime. For more information about how to use the custom time, see [custom time metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-time).  
  
### XML API

Field name | Description  
---|---  
`Created` | The creation time of the object. This timestamp doesn't change.  
`LastModified` | The most recent modification time of the object metadata. This value is initially set to the object's creation time, and then updated whenever any metadata of the object changes. This includes changes made by a requester, such as modifying custom metadata, as well as changes made by Cloud Storage on behalf of a requester, such as changing the storage class based on an [Object Lifecycle Configuration](https://docs.cloud.google.com/storage/docs/lifecycle).  
`DeletedTime` | The deletion time of the object. Returned if and only if this version of the object is no longer a live version, but remains in the bucket as a [noncurrent version](https://docs.cloud.google.com/storage/docs/object-versioning).  
`x-goog-object-lock-retain-until-date` | The earliest time that the object can be deleted or replaced. This value is independent of any retention policy that is set for the bucket that contains the object. The maximum value is 3,155,760,000 seconds (100 years) from the current date and time.  
`Finalized` | The finalization time of the object.  
`x-goog-custom-time` | A user-specified timestamp for the object. After you set a custom time on an object, the custom time cannot be removed and cannot be set to an earlier datetime. For more information about how to use the custom time, see [custom time metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-time).  
  
### RPC API

Field name | Description  
---|---  
`create_time` | The creation time of the object. This timestamp doesn't change.  
`update_time` | The most recent modification time of the object metadata. This value is initially set to the object's creation time, and then updated whenever any metadata of the object changes. This includes changes made by a requester, such as modifying custom metadata, as well as changes made by Cloud Storage on behalf of a requester, such as changing the storage class based on an [Object Lifecycle Configuration](https://docs.cloud.google.com/storage/docs/lifecycle).  
`delete_time` | The deletion time of the object. Returned if and only if this version of the object is no longer a live version, but remains in the bucket as a [noncurrent version](https://docs.cloud.google.com/storage/docs/object-versioning).  
`soft_delete_time` | The time at which the object was [soft deleted](https://docs.cloud.google.com/storage/docs/soft-delete). Only available for objects in buckets with a soft delete policy.  
`hard_delete_time` | The time at which a soft-deleted object will be permanently deleted and can no longer be restored. This value is the sum of the values of the soft delete time and the retention duration that is set in the bucket's retention policy. Only available for objects in buckets with a soft delete policy. Note that the value for the hard delete time is permanent after it's set and does not change in response to changes in the retention duration.  
`retention.retain_until_time` | The earliest time that the object can be deleted or replaced. This value is independent of any retention policy that is set for the bucket that contains the object. The maximum value is 3,155,760,000 seconds (100 years) from the current date and time.  
`retention_expire_time` | The earliest time that the object can be deleted. This value depends on both the [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock) that is set for the object, and on the [retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock#retention-policy) that is set for the bucket that contains the object.  
`update_storage_class_time` | The time at which the object's storage class was last changed. When the object is initially created, the value is set to the object's creation time.  
`finalize_time` | The finalization time of the object.  
`contexts.custom.KEY.createTime` | The time when this object context key was first added to the object.  
`contexts.custom.KEY.updateTime` | The time when this object context key was last updated.  
`custom_time` | A user-specified timestamp for the object. After you set a custom time on an object, the custom time cannot be removed and cannot be set to an earlier datetime. For more information about how to use the custom time, see [custom time metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-time).  
  
## What's next

  * [View and edit object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata).
  * Learn about available [storage classes](https://docs.cloud.google.com/storage/docs/storage-classes).
  * For a detailed description of all object metadata fields available in the JSON API, see the [Objects reference documentation for JSON](https://docs.cloud.google.com/storage/docs/json_api/v1/objects).
  * Learn about [inventory reports](https://docs.cloud.google.com/storage/docs/insights/inventory-reports), which allow you to get the metadata for all objects in a bucket at once.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
