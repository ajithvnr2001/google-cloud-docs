---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo
title: Class BlobInfo (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:41:19.106439+00:00
---

# Class BlobInfo (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BlobInfo (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 
    
    
    public class BlobInfo implements Serializable

Information about an object in Google Cloud Storage. A `BlobInfo` object includes the `BlobId` instance and the set of properties, such as the blob's access control configuration, user provided metadata, the CRC32C checksum, etc. Instances of this class are used to create a new object in Google Cloud Storage or update the properties of an existing object. To deal with existing Storage objects the API includes the [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob) class which extends ` BlobInfo` and declares methods to perform operations on the object. Neither `BlobInfo` nor `Blob` instances keep the object content, just the object properties.

Example of usage `BlobInfo` to create an object in Google Cloud Storage:
    
    
     BlobId blobId = BlobId.of(bucketName, blobName);
     BlobInfo blobInfo = BlobInfo.newBuilder(blobId).setContentType("text/plain").build();
     Blob blob = storage.create(blobInfo, "Hello, world".getBytes(StandardCharsets.UTF_8));
     

See Also: [Concepts and Terminology](https://cloud.google.com/storage/docs/concepts-techniques#concepts)

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BlobInfo

## Implements

[Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### newBuilder(BlobId blobId)
    
    
    public static BlobInfo.Builder newBuilder(BlobId blobId)

Returns a `BlobInfo` builder where blob identity is set using the provided value.

**Parameter**  
---  
**Name** | **Description**  
`blobId` | `[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### newBuilder(BucketInfo bucketInfo, String name)
    
    
    public static BlobInfo.Builder newBuilder(BucketInfo bucketInfo, String name)

Returns a `BlobInfo` builder where blob identity is set using the provided values.

**Parameters**  
---  
**Name** | **Description**  
`bucketInfo` | `[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo)`  
  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### newBuilder(BucketInfo bucketInfo, String name, Long generation)
    
    
    public static BlobInfo.Builder newBuilder(BucketInfo bucketInfo, String name, Long generation)

Returns a `BlobInfo` builder where blob identity is set using the provided values.

**Parameters**  
---  
**Name** | **Description**  
`bucketInfo` | `[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo)`  
  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`generation` | `[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### newBuilder(String bucket, String name)
    
    
    public static BlobInfo.Builder newBuilder(String bucket, String name)

Returns a `BlobInfo` builder where blob identity is set using the provided values.

**Parameters**  
---  
**Name** | **Description**  
`bucket` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### newBuilder(String bucket, String name, Long generation)
    
    
    public static BlobInfo.Builder newBuilder(String bucket, String name, Long generation)

Returns a `BlobInfo` builder where blob identity is set using the provided values.

**Parameters**  
---  
**Name** | **Description**  
`bucket` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`generation` | `[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
## Methods 

### equals(Object o)
    
    
    public boolean equals(Object o)

**Parameter**  
---  
**Name** | **Description**  
`o` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### getAcl()
    
    
    public List<Acl> getAcl()

Returns the blob's access control configuration. See Also: [ About Access Control Lists](https://cloud.google.com/storage/docs/access-control#About-Access-Control-Lists)

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Acl)>` |   
  
### getBlobId()
    
    
    public BlobId getBlobId()

Returns the blob's identity.

**Returns**  
---  
**Type** | **Description**  
`[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId)` |   
  
### getBucket()
    
    
    public String getBucket()

Returns the name of the containing bucket.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getCacheControl()
    
    
    public String getCacheControl()

Returns the blob's data cache control. See Also: [Cache-Control](https://tools.ietf.org/html/rfc7234#section-5.2)

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getComponentCount()
    
    
    public Integer getComponentCount()

Returns the number of components that make up this blob. Components are accumulated through the [Storage#compose(Storage.ComposeRequest)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_compose_com_google_cloud_storage_Storage_ComposeRequest_) operation and are limited to a count of 1024, counting 1 for each non-composite component blob and componentCount for each composite component blob. This value is set only for composite blobs. See Also: [Component Count Property](https://cloud.google.com/storage/docs/composite-objects#_Count)

**Returns**  
---  
**Type** | **Description**  
`[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)` |   
  
### getContentDisposition()
    
    
    public String getContentDisposition()

Returns the blob's data content disposition. See Also: [Content-Disposition](https://tools.ietf.org/html/rfc6266)

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getContentEncoding()
    
    
    public String getContentEncoding()

Returns the blob's data content encoding. See Also: [Content-Encoding](https://tools.ietf.org/html/rfc7231#section-3.1.2.2)

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getContentLanguage()
    
    
    public String getContentLanguage()

Returns the blob's data content language. See Also: [Content-Language](http://tools.ietf.org/html/bcp47)

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getContentType()
    
    
    public String getContentType()

Returns the blob's data content type. See Also: [Content-Type](https://tools.ietf.org/html/rfc2616#section-14.17)

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getContexts()
    
    
    public BlobInfo.ObjectContexts getContexts()

**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.ObjectContexts](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.ObjectContexts)` |   
  
### getCrc32c()
    
    
    public String getCrc32c()

Returns the CRC32C checksum of blob's data as described in [RFC 4960, Appendix B;](http://tools.ietf.org/html/rfc4960#appendix-B) encoded in base64 in big-endian order. See Also: [Hashes and ETags: Best Practices](https://cloud.google.com/storage/docs/hashes-etags#_JSONAPI)

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getCrc32cToHexString()
    
    
    public String getCrc32cToHexString()

Returns the CRC32C checksum of blob's data as described in [RFC 4960, Appendix B;](http://tools.ietf.org/html/rfc4960#appendix-B) decoded to string. See Also: [Hashes and ETags: Best Practices](https://cloud.google.com/storage/docs/hashes-etags#_JSONAPI)

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getCreateTime() (deprecated)
    
    
    public Long getCreateTime()

**Deprecated.** _Use[#getCreateTimeOffsetDateTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getCreateTimeOffsetDateTime__)_

Returns the creation time of the blob expressed as the number of milliseconds since the Unix epoch.

**Returns**  
---  
**Type** | **Description**  
`[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)` |   
  
### getCreateTimeOffsetDateTime()
    
    
    public OffsetDateTime getCreateTimeOffsetDateTime()

Returns the creation time of the blob.

**Returns**  
---  
**Type** | **Description**  
`[OffsetDateTime](https://docs.oracle.com/javase/8/docs/api/java/time/OffsetDateTime.html)` |   
  
### getCustomTime() (deprecated)
    
    
    public Long getCustomTime()

**Deprecated.** _Use[#getCustomTimeOffsetDateTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getCustomTimeOffsetDateTime__)_

Returns the custom time specified by the user for an object.

**Returns**  
---  
**Type** | **Description**  
`[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)` |   
  
### getCustomTimeOffsetDateTime()
    
    
    public OffsetDateTime getCustomTimeOffsetDateTime()

Returns the custom time specified by the user for an object.

**Returns**  
---  
**Type** | **Description**  
`[OffsetDateTime](https://docs.oracle.com/javase/8/docs/api/java/time/OffsetDateTime.html)` |   
  
### getCustomerEncryption()
    
    
    public BlobInfo.CustomerEncryption getCustomerEncryption()

Returns information on the customer-supplied encryption key, if the blob is encrypted using such a key.

**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.CustomerEncryption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.CustomerEncryption)` |   
  
### getDeleteTime() (deprecated)
    
    
    public Long getDeleteTime()

**Deprecated.** _Use[#getDeleteTimeOffsetDateTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getDeleteTimeOffsetDateTime__)_

Returns the deletion time of the blob expressed as the number of milliseconds since the Unix epoch.

**Returns**  
---  
**Type** | **Description**  
`[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)` |   
  
### getDeleteTimeOffsetDateTime()
    
    
    public OffsetDateTime getDeleteTimeOffsetDateTime()

Returns the deletion time of the blob.

**Returns**  
---  
**Type** | **Description**  
`[OffsetDateTime](https://docs.oracle.com/javase/8/docs/api/java/time/OffsetDateTime.html)` |   
  
### getEtag()
    
    
    public String getEtag()

Returns HTTP 1.1 Entity tag for the blob. See Also: [Entity Tags](http://tools.ietf.org/html/rfc2616#section-3.11)

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getEventBasedHold()
    
    
    public Boolean getEventBasedHold()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns a `Boolean` with either `true`, `null` and in certain cases ` false`.

Case 1: `true` the field [com.google.cloud.storage.Storage.BlobField#EVENT_BASED_HOLD](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BlobField#com_google_cloud_storage_Storage_BlobField_EVENT_BASED_HOLD) is selected in a [Storage#get(BlobId, Storage.BlobGetOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_get_) and event-based hold for the blob is enabled.

Case 2.1: `null` the field [com.google.cloud.storage.Storage.BlobField#EVENT_BASED_HOLD](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BlobField#com_google_cloud_storage_Storage_BlobField_EVENT_BASED_HOLD) is selected in a [Storage#get(BlobId, Storage.BlobGetOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_get_), but event-based hold for the blob is not enabled. This case can be considered implicitly `false`.

Case 2.2: `null` the field [com.google.cloud.storage.Storage.BlobField#EVENT_BASED_HOLD](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BlobField#com_google_cloud_storage_Storage_BlobField_EVENT_BASED_HOLD) is not selected in a [Storage#get(BlobId, Storage.BlobGetOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_get_), and the state for this field is unknown.

Case 3: `false` event-based hold is explicitly set to false using in a Builder#setEventBasedHold(Boolean) client side for a follow-up request e.g. [Storage#update(BlobInfo, Storage.BlobTargetOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_update_) in which case the value of event-based hold will remain `false` for the given instance.

**Returns**  
---  
**Type** | **Description**  
`[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)` |   
  
### getGeneratedId()
    
    
    public String getGeneratedId()

Returns the service-generated for the blob.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getGeneration()
    
    
    public Long getGeneration()

Returns blob's data generation. Used for blob versioning.

**Returns**  
---  
**Type** | **Description**  
`[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)` |   
  
### getHardDeleteTime()
    
    
    public OffsetDateTime getHardDeleteTime()

If this object has been soft-deleted, returns the time at which it will be permanently deleted.

**Returns**  
---  
**Type** | **Description**  
`[OffsetDateTime](https://docs.oracle.com/javase/8/docs/api/java/time/OffsetDateTime.html)` |   
  
### getKmsKeyName()
    
    
    public String getKmsKeyName()

Returns the Cloud KMS key used to encrypt the blob, if any.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMd5()
    
    
    public String getMd5()

Returns the MD5 hash of blob's data encoded in base64. See Also: [Hashes and ETags: Best Practices](https://cloud.google.com/storage/docs/hashes-etags#_JSONAPI)

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMd5ToHexString()
    
    
    public String getMd5ToHexString()

Returns the MD5 hash of blob's data decoded to string. See Also: [Hashes and ETags: Best Practices](https://cloud.google.com/storage/docs/hashes-etags#_JSONAPI)

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMediaLink()
    
    
    public String getMediaLink()

Returns the blob's media download link.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMetadata()
    
    
    public @Nullable Map<@NonNull String,@Nullable String> getMetadata()

Returns blob's user provided metadata.

**Returns**  
---  
**Type** | **Description**  
`@org.checkerframework.checker.nullness.qual.Nullable java.util.Map<@org.checkerframework.checker.nullness.qual.NonNull java.lang.String,@org.checkerframework.checker.nullness.qual.Nullable java.lang.String>` |   
  
### getMetageneration()
    
    
    public Long getMetageneration()

Returns blob's metageneration. Used for preconditions and for detecting changes in metadata. A metageneration number is only meaningful in the context of a particular generation of a particular blob.

**Returns**  
---  
**Type** | **Description**  
`[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)` |   
  
### getName()
    
    
    public String getName()

Returns the blob's name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getOwner()
    
    
    public Acl.Entity getOwner()

Returns the blob's owner. This will always be the uploader of the blob.

**Returns**  
---  
**Type** | **Description**  
`[Acl.Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Acl.Entity)` |   
  
### getRetention()
    
    
    public BlobInfo.Retention getRetention()

Returns the object's Retention policy.

**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Retention](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Retention)` |   
  
### getRetentionExpirationTime() (deprecated)
    
    
    public Long getRetentionExpirationTime()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

**Deprecated.** _Use[#getRetentionExpirationTimeOffsetDateTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getRetentionExpirationTimeOffsetDateTime__)_

Returns the retention expiration time of the blob as `Long`, if a retention period is defined. If retention period is not defined this value returns `null`

**Returns**  
---  
**Type** | **Description**  
`[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)` |   
  
### getRetentionExpirationTimeOffsetDateTime()
    
    
    public OffsetDateTime getRetentionExpirationTimeOffsetDateTime()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the retention expiration time of the blob, if a retention period is defined. If retention period is not defined this value returns `null`

**Returns**  
---  
**Type** | **Description**  
`[OffsetDateTime](https://docs.oracle.com/javase/8/docs/api/java/time/OffsetDateTime.html)` |   
  
### getSelfLink()
    
    
    public String getSelfLink()

Returns the URI of this blob as a string.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getSize()
    
    
    public Long getSize()

Returns the content length of the data in bytes. See Also: [Content-Length](https://tools.ietf.org/html/rfc2616#section-14.13)

**Returns**  
---  
**Type** | **Description**  
`[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)` |   
  
### getSoftDeleteTime()
    
    
    public OffsetDateTime getSoftDeleteTime()

If this object has been soft-deleted, returns the time it was soft-deleted.

**Returns**  
---  
**Type** | **Description**  
`[OffsetDateTime](https://docs.oracle.com/javase/8/docs/api/java/time/OffsetDateTime.html)` |   
  
### getStorageClass()
    
    
    public StorageClass getStorageClass()

Returns the storage class of the blob.

**Returns**  
---  
**Type** | **Description**  
`[StorageClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageClass)` |   
  
### getTemporaryHold()
    
    
    public Boolean getTemporaryHold()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns a `Boolean` with either `true`, `null` and in certain cases ` false`.

Case 1: `true` the field [com.google.cloud.storage.Storage.BlobField#TEMPORARY_HOLD](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BlobField#com_google_cloud_storage_Storage_BlobField_TEMPORARY_HOLD) is selected in a [Storage#get(BlobId, Storage.BlobGetOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_get_) and temporary hold for the blob is enabled.

Case 2.1: `null` the field [com.google.cloud.storage.Storage.BlobField#TEMPORARY_HOLD](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BlobField#com_google_cloud_storage_Storage_BlobField_TEMPORARY_HOLD) is selected in a [Storage#get(BlobId, Storage.BlobGetOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_get_), but temporary hold for the blob is not enabled. This case can be considered implicitly `false`.

Case 2.2: `null` the field [com.google.cloud.storage.Storage.BlobField#TEMPORARY_HOLD](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BlobField#com_google_cloud_storage_Storage_BlobField_TEMPORARY_HOLD) is not selected in a [Storage#get(BlobId, Storage.BlobGetOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_get_), and the state for this field is unknown.

Case 3: `false` event-based hold is explicitly set to false using in a Builder#setEventBasedHold(Boolean) client side for a follow-up request e.g. [Storage#update(BlobInfo, Storage.BlobTargetOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_update_) in which case the value of temporary hold will remain `false` for the given instance.

**Returns**  
---  
**Type** | **Description**  
`[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)` |   
  
### getTimeStorageClassUpdated() (deprecated)
    
    
    public Long getTimeStorageClassUpdated()

**Deprecated.** _Use[#getTimeStorageClassUpdatedOffsetDateTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getTimeStorageClassUpdatedOffsetDateTime__)_

Returns the time that the object's storage class was last changed or the time of the object creation.

**Returns**  
---  
**Type** | **Description**  
`[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)` |   
  
### getTimeStorageClassUpdatedOffsetDateTime()
    
    
    public OffsetDateTime getTimeStorageClassUpdatedOffsetDateTime()

Returns the time that the object's storage class was last changed or the time of the object creation.

**Returns**  
---  
**Type** | **Description**  
`[OffsetDateTime](https://docs.oracle.com/javase/8/docs/api/java/time/OffsetDateTime.html)` |   
  
### getUpdateTime() (deprecated)
    
    
    public Long getUpdateTime()

**Deprecated.** _Use[#getUpdateTimeOffsetDateTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getUpdateTimeOffsetDateTime__)_

Returns the last modification time of the blob's metadata expressed as the number of milliseconds since the Unix epoch.

**Returns**  
---  
**Type** | **Description**  
`[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)` |   
  
### getUpdateTimeOffsetDateTime()
    
    
    public OffsetDateTime getUpdateTimeOffsetDateTime()

Returns the last modification time of the blob's metadata.

**Returns**  
---  
**Type** | **Description**  
`[OffsetDateTime](https://docs.oracle.com/javase/8/docs/api/java/time/OffsetDateTime.html)` |   
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### isDirectory()
    
    
    public boolean isDirectory()

Returns `true` if the current blob represents a directory. This can only happen if the blob is returned by [Storage#list(String, Storage.BlobListOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_list_) when the [Storage.BlobListOption#currentDirectory()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BlobListOption#com_google_cloud_storage_Storage_BlobListOption_currentDirectory__) option is used. When this is the case only [#getBlobId()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getBlobId__) and [#getSize()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getSize__) are set for the current blob: [BlobId#getName()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId#com_google_cloud_storage_BlobId_getName__) ends with the '/' character, [BlobId#getGeneration()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId#com_google_cloud_storage_BlobId_getGeneration__) returns `null` and [#getSize()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getSize__) is `0`.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### toBuilder()
    
    
    public BlobInfo.Builder toBuilder()

Returns a builder for the current blob.

**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### toString()
    
    
    public String toString()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
