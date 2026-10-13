---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder
title: Class BlobInfo.Builder (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:41:19.614545+00:00
---

# Class BlobInfo.Builder (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BlobInfo.Builder (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 
    
    
    public abstract static class BlobInfo.Builder

Builder for `BlobInfo`.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BlobInfo.Builder

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

## Constructors 

### Builder()
    
    
    public Builder()

## Methods 

### build()
    
    
    public abstract BlobInfo build()

Creates a `BlobInfo` object.

**Returns**  
---  
**Type** | **Description**  
`[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo)` |   
  
### setAcl(List<Acl> acl)
    
    
    public abstract BlobInfo.Builder setAcl(List<Acl> acl)

Sets the blob's access control configuration. See Also: [ About Access Control Lists](https://cloud.google.com/storage/docs/access-control#About-Access-Control-Lists)

**Parameter**  
---  
**Name** | **Description**  
`acl` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Acl)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setBlobId(BlobId blobId)
    
    
    public abstract BlobInfo.Builder setBlobId(BlobId blobId)

Sets the blob identity.

**Parameter**  
---  
**Name** | **Description**  
`blobId` | `[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setCacheControl(String cacheControl)
    
    
    public abstract BlobInfo.Builder setCacheControl(String cacheControl)

Sets the blob's data cache control. See Also: [Cache-Control](https://tools.ietf.org/html/rfc7234#section-5.2)

**Parameter**  
---  
**Name** | **Description**  
`cacheControl` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setContentDisposition(String contentDisposition)
    
    
    public abstract BlobInfo.Builder setContentDisposition(String contentDisposition)

Sets the blob's data content disposition. See Also: [Content-Disposition](https://tools.ietf.org/html/rfc6266)

**Parameter**  
---  
**Name** | **Description**  
`contentDisposition` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setContentEncoding(String contentEncoding)
    
    
    public abstract BlobInfo.Builder setContentEncoding(String contentEncoding)

Sets the blob's data content encoding. See Also: [Content-Encoding](https://tools.ietf.org/html/rfc7231#section-3.1.2.2)

**Parameter**  
---  
**Name** | **Description**  
`contentEncoding` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setContentLanguage(String contentLanguage)
    
    
    public abstract BlobInfo.Builder setContentLanguage(String contentLanguage)

Sets the blob's data content language. See Also: [Content-Language](http://tools.ietf.org/html/bcp47)

**Parameter**  
---  
**Name** | **Description**  
`contentLanguage` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setContentType(String contentType)
    
    
    public abstract BlobInfo.Builder setContentType(String contentType)

Sets the blob's data content type. See Also: [Content-Type](https://tools.ietf.org/html/rfc2616#section-14.17)

**Parameter**  
---  
**Name** | **Description**  
`contentType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setContexts(BlobInfo.ObjectContexts contexts)
    
    
    public abstract BlobInfo.Builder setContexts(BlobInfo.ObjectContexts contexts)

**Parameter**  
---  
**Name** | **Description**  
`contexts` | `[BlobInfo.ObjectContexts](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.ObjectContexts)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setCrc32c(String crc32c)
    
    
    public abstract BlobInfo.Builder setCrc32c(String crc32c)

Sets the CRC32C checksum of blob's data as described in [RFC 4960, Appendix B;](http://tools.ietf.org/html/rfc4960#appendix-B) encoded in base64 in big-endian order. See Also: [Hashes and ETags: Best Practices](https://cloud.google.com/storage/docs/hashes-etags#_JSONAPI)

**Parameter**  
---  
**Name** | **Description**  
`crc32c` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setCrc32cFromHexString(String crc32cHexString)
    
    
    public abstract BlobInfo.Builder setCrc32cFromHexString(String crc32cHexString)

Sets the CRC32C checksum of blob's data as described in [RFC 4960, Appendix B;](http://tools.ietf.org/html/rfc4960#appendix-B) from hex string. See Also: [Hashes and ETags: Best Practices](https://cloud.google.com/storage/docs/hashes-etags#_JSONAPI)

**Parameter**  
---  
**Name** | **Description**  
`crc32cHexString` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setCustomTime(Long customTime) (deprecated)
    
    
    public BlobInfo.Builder setCustomTime(Long customTime)

**Deprecated.** _Use[#setCustomTimeOffsetDateTime(OffsetDateTime)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder#com_google_cloud_storage_BlobInfo_Builder_setCustomTimeOffsetDateTime_java_time_OffsetDateTime_)_

Sets the custom time for an object. Once set it can't be unset and only changed to a custom datetime in the future. To unset the custom time, you must either perform a rewrite operation or upload the data again.

Example of setting the custom time.
    
    
     String bucketName = "my-unique-bucket";
     String blobName = "my-blob-name";
     long customTime = 1598423868301L;
     BlobInfo blob = BlobInfo.newBuilder(bucketName, blobName).setCustomTime(customTime).build();
     

**Parameter**  
---  
**Name** | **Description**  
`customTime` | `[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setCustomTimeOffsetDateTime(OffsetDateTime customTime)
    
    
    public BlobInfo.Builder setCustomTimeOffsetDateTime(OffsetDateTime customTime)

Sets the custom time for an object. Once set it can't be unset and only changed to a custom datetime in the future. To unset the custom time, you must either perform a rewrite operation or upload the data again.

Example of setting the custom time.
    
    
     String bucketName = "my-unique-bucket";
     String blobName = "my-blob-name";
     OffsetDateTime customTime = Instant.ofEpochMilli(1598423868301L).atOffset(0); // UTC
     BlobInfo blob = BlobInfo.newBuilder(bucketName, blobName).setCustomTime(customTime).build();
     

**Parameter**  
---  
**Name** | **Description**  
`customTime` | `[OffsetDateTime](https://docs.oracle.com/javase/8/docs/api/java/time/OffsetDateTime.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setEventBasedHold(Boolean eventBasedHold)
    
    
    public abstract BlobInfo.Builder setEventBasedHold(Boolean eventBasedHold)

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Sets the blob's event-based hold.

**Parameter**  
---  
**Name** | **Description**  
`eventBasedHold` | `[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setMd5(String md5)
    
    
    public abstract BlobInfo.Builder setMd5(String md5)

Sets the MD5 hash of blob's data. MD5 value must be encoded in base64. See Also: [Hashes and ETags: Best Practices](https://cloud.google.com/storage/docs/hashes-etags#_JSONAPI)

**Parameter**  
---  
**Name** | **Description**  
`md5` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setMd5FromHexString(String md5HexString)
    
    
    public abstract BlobInfo.Builder setMd5FromHexString(String md5HexString)

Sets the MD5 hash of blob's data from hex string. See Also: [Hashes and ETags: Best Practices](https://cloud.google.com/storage/docs/hashes-etags#_JSONAPI)

**Parameter**  
---  
**Name** | **Description**  
`md5HexString` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setMetadata(@Nullable Map<@NonNull String,@Nullable String> metadata)
    
    
    public abstract BlobInfo.Builder setMetadata(@Nullable Map<@NonNull String,@Nullable String> metadata)

Sets the blob's user provided metadata.

**Parameter**  
---  
**Name** | **Description**  
`metadata` | `@org.checkerframework.checker.nullness.qual.Nullable java.util.Map<@org.checkerframework.checker.nullness.qual.NonNull java.lang.String,@org.checkerframework.checker.nullness.qual.Nullable java.lang.String>`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setRetention(BlobInfo.Retention retention)
    
    
    public abstract BlobInfo.Builder setRetention(BlobInfo.Retention retention)

**Parameter**  
---  
**Name** | **Description**  
`retention` | `[BlobInfo.Retention](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Retention)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setStorageClass(StorageClass storageClass)
    
    
    public abstract BlobInfo.Builder setStorageClass(StorageClass storageClass)

Sets the blob's storage class.

**Parameter**  
---  
**Name** | **Description**  
`storageClass` | `[StorageClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageClass)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setTemporaryHold(Boolean temporaryHold)
    
    
    public abstract BlobInfo.Builder setTemporaryHold(Boolean temporaryHold)

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Sets the blob's temporary hold.

**Parameter**  
---  
**Name** | **Description**  
`temporaryHold` | `[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setTimeStorageClassUpdated(Long timeStorageClassUpdated) (deprecated)
    
    
    public BlobInfo.Builder setTimeStorageClassUpdated(Long timeStorageClassUpdated)

**Deprecated.** _Use[#setTimeStorageClassUpdatedOffsetDateTime(OffsetDateTime)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder#com_google_cloud_storage_BlobInfo_Builder_setTimeStorageClassUpdatedOffsetDateTime_java_time_OffsetDateTime_)_

Sets the modification time of an object's storage class. Once set it can't be unset directly, the only way is to rewrite the object with the desired storage class.

**Parameter**  
---  
**Name** | **Description**  
`timeStorageClassUpdated` | `[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
### setTimeStorageClassUpdatedOffsetDateTime(OffsetDateTime timeStorageClassUpdated)
    
    
    public BlobInfo.Builder setTimeStorageClassUpdatedOffsetDateTime(OffsetDateTime timeStorageClassUpdated)

**Parameter**  
---  
**Name** | **Description**  
`timeStorageClassUpdated` | `[OffsetDateTime](https://docs.oracle.com/javase/8/docs/api/java/time/OffsetDateTime.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
