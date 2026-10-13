---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob
title: Class Blob (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:41:17.908220+00:00
---

# Class Blob (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Blob (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 
    
    
    public class Blob extends BlobInfo

An object in Google Cloud Storage. A `Blob` object includes the `BlobId` instance, the set of properties inherited from the [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo) class and the `Storage` instance. The class provides methods to perform operations on the object. Reading a property value does not issue any RPC calls. The object content is not stored within the `Blob` instance. Operations that access the content issue one or multiple RPC calls, depending on the content size.

Objects of this class are immutable. Operations that modify the blob like [#update](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob#com_google_cloud_storage_Blob_update_) and [#copyTo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob#com_google_cloud_storage_Blob_copyTo_) return a new object. Any changes to the object in Google Cloud Storage made after creation of the `Blob` are not visible in the `Blob`. To get a `Blob` object with the most recent information use [#reload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob#com_google_cloud_storage_Blob_reload_).

Example of getting the content of the object in Google Cloud Storage:
    
    
     BlobId blobId = BlobId.of(bucketName, blobName);
     Blob blob = storage.get(blobId);
     long size = blob.getSize(); // no RPC call is required
     byte[] content = blob.getContent(); // one or multiple RPC calls will be issued
     

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo) > Blob

## Inherited Members

[BlobInfo.equals(Object)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_equals_java_lang_Object_)

[BlobInfo.getAcl()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getAcl__)

[BlobInfo.getBlobId()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getBlobId__)

[BlobInfo.getBucket()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getBucket__)

[BlobInfo.getCacheControl()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getCacheControl__)

[BlobInfo.getComponentCount()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getComponentCount__)

[BlobInfo.getContentDisposition()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getContentDisposition__)

[BlobInfo.getContentEncoding()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getContentEncoding__)

[BlobInfo.getContentLanguage()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getContentLanguage__)

[BlobInfo.getContentType()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getContentType__)

[BlobInfo.getContexts()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getContexts__)

[BlobInfo.getCrc32c()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getCrc32c__)

[BlobInfo.getCrc32cToHexString()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getCrc32cToHexString__)

[BlobInfo.getCreateTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getCreateTime__)

[BlobInfo.getCreateTimeOffsetDateTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getCreateTimeOffsetDateTime__)

[BlobInfo.getCustomTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getCustomTime__)

[BlobInfo.getCustomTimeOffsetDateTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getCustomTimeOffsetDateTime__)

[BlobInfo.getCustomerEncryption()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getCustomerEncryption__)

[BlobInfo.getDeleteTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getDeleteTime__)

[BlobInfo.getDeleteTimeOffsetDateTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getDeleteTimeOffsetDateTime__)

[BlobInfo.getEtag()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getEtag__)

[BlobInfo.getEventBasedHold()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getEventBasedHold__)

[BlobInfo.getGeneratedId()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getGeneratedId__)

[BlobInfo.getGeneration()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getGeneration__)

[BlobInfo.getHardDeleteTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getHardDeleteTime__)

[BlobInfo.getKmsKeyName()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getKmsKeyName__)

[BlobInfo.getMd5()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getMd5__)

[BlobInfo.getMd5ToHexString()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getMd5ToHexString__)

[BlobInfo.getMediaLink()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getMediaLink__)

[BlobInfo.getMetadata()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getMetadata__)

[BlobInfo.getMetageneration()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getMetageneration__)

[BlobInfo.getName()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getName__)

[BlobInfo.getOwner()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getOwner__)

[BlobInfo.getRetention()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getRetention__)

[BlobInfo.getRetentionExpirationTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getRetentionExpirationTime__)

[BlobInfo.getRetentionExpirationTimeOffsetDateTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getRetentionExpirationTimeOffsetDateTime__)

[BlobInfo.getSelfLink()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getSelfLink__)

[BlobInfo.getSize()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getSize__)

[BlobInfo.getSoftDeleteTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getSoftDeleteTime__)

[BlobInfo.getStorageClass()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getStorageClass__)

[BlobInfo.getTemporaryHold()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getTemporaryHold__)

[BlobInfo.getTimeStorageClassUpdated()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getTimeStorageClassUpdated__)

[BlobInfo.getTimeStorageClassUpdatedOffsetDateTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getTimeStorageClassUpdatedOffsetDateTime__)

[BlobInfo.getUpdateTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getUpdateTime__)

[BlobInfo.getUpdateTimeOffsetDateTime()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_getUpdateTimeOffsetDateTime__)

[BlobInfo.hashCode()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_hashCode__)

[BlobInfo.isDirectory()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_isDirectory__)

[BlobInfo.newBuilder(BlobId)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_newBuilder_com_google_cloud_storage_BlobId_)

[BlobInfo.newBuilder(BucketInfo,String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_newBuilder_com_google_cloud_storage_BucketInfo_java_lang_String_)

[BlobInfo.newBuilder(BucketInfo,String,Long)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_newBuilder_com_google_cloud_storage_BucketInfo_java_lang_String_java_lang_Long_)

[BlobInfo.newBuilder(String,String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_newBuilder_java_lang_String_java_lang_String_)

[BlobInfo.newBuilder(String,String,Long)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_newBuilder_java_lang_String_java_lang_String_java_lang_Long_)

[BlobInfo.toBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_toBuilder__)

[BlobInfo.toString()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_toString__)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### asBlobInfo()
    
    
    public BlobInfo asBlobInfo()

Drop the held [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage) instance.

**Returns**  
---  
**Type** | **Description**  
`[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo)` |   
  
### copyTo(BlobId targetBlob, Blob.BlobSourceOption[] options)
    
    
    public CopyWriter copyTo(BlobId targetBlob, Blob.BlobSourceOption[] options)

Sends a copy request for the current blob to the target blob. Possibly also some of the metadata are copied (e.g. content-type).

Example of copying the blob to a different bucket with a different name.
    
    
     String bucketName = "my_unique_bucket";
     String blobName = "copy_blob_name";
     CopyWriter copyWriter = blob.copyTo(BlobId.of(bucketName, blobName));
     Blob copiedBlob = copyWriter.getResult();
     

**Parameters**  
---  
**Name** | **Description**  
`targetBlob` | `[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId)`  
target blob's id  
`options` | `[BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)[]`  
source blob options  
**Returns**  
---  
**Type** | **Description**  
`[CopyWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.CopyWriter)` | a [CopyWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.CopyWriter) object that can be used to get information on the newly created blob or to complete the copy if more than one RPC request is needed  
  
### copyTo(String targetBucket, Blob.BlobSourceOption[] options)
    
    
    public CopyWriter copyTo(String targetBucket, Blob.BlobSourceOption[] options)

Sends a copy request for the current blob to the target bucket, preserving its name. Possibly copying also some of the metadata (e.g. content-type).

Example of copying the blob to a different bucket, keeping the original name.
    
    
     String bucketName = "my_unique_bucket";
     CopyWriter copyWriter = blob.copyTo(bucketName);
     Blob copiedBlob = copyWriter.getResult();
     

**Parameters**  
---  
**Name** | **Description**  
`targetBucket` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
target bucket's name  
`options` | `[BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)[]`  
source blob options  
**Returns**  
---  
**Type** | **Description**  
`[CopyWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.CopyWriter)` | a [CopyWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.CopyWriter) object that can be used to get information on the newly created blob or to complete the copy if more than one RPC request is needed  
  
### copyTo(String targetBucket, String targetBlob, Blob.BlobSourceOption[] options)
    
    
    public CopyWriter copyTo(String targetBucket, String targetBlob, Blob.BlobSourceOption[] options)

Sends a copy request for the current blob to the target blob. Possibly also some of the metadata are copied (e.g. content-type).

Example of copying the blob to a different bucket with a different name.
    
    
     String bucketName = "my_unique_bucket";
     String blobName = "copy_blob_name";
     CopyWriter copyWriter = blob.copyTo(bucketName, blobName);
     Blob copiedBlob = copyWriter.getResult();
     

Example of moving a blob to a different bucket with a different name.
    
    
     String destBucket = "my_unique_bucket";
     String destBlob = "move_blob_name";
     CopyWriter copyWriter = blob.copyTo(destBucket, destBlob);
     Blob copiedBlob = copyWriter.getResult();
     boolean deleted = blob.delete();
     

**Parameters**  
---  
**Name** | **Description**  
`targetBucket` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
target bucket's name  
`targetBlob` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
target blob's name  
`options` | `[BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)[]`  
source blob options  
**Returns**  
---  
**Type** | **Description**  
`[CopyWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.CopyWriter)` | a [CopyWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.CopyWriter) object that can be used to get information on the newly created blob or to complete the copy if more than one RPC request is needed  
  
### createAcl(Acl acl)
    
    
    public Acl createAcl(Acl acl)

Creates a new ACL entry on this blob.

Example of creating a new ACL entry.
    
    
     Acl acl = blob.createAcl(Acl.of(User.ofAllAuthenticatedUsers(), Acl.Role.READER));
     

**Parameter**  
---  
**Name** | **Description**  
`acl` | `[Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Acl)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Acl)` |   
  
### delete(Blob.BlobSourceOption[] options)
    
    
    public boolean delete(Blob.BlobSourceOption[] options)

Deletes this blob.

Example of deleting the blob, if its generation matches the Blob#getGeneration() value, otherwise a [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException) is thrown.
    
    
     boolean deleted = blob.delete(BlobSourceOption.generationMatch());
     if (deleted) {
       // the blob was deleted
     } else {
       // the blob was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)[]`  
blob delete options  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if blob was deleted, `false` if it was not found  
  
### deleteAcl(Acl.Entity entity)
    
    
    public boolean deleteAcl(Acl.Entity entity)

Deletes the ACL entry for the specified entity on this blob.

Example of deleting the ACL entry for an entity.
    
    
     boolean deleted = blob.deleteAcl(User.ofAllAuthenticatedUsers());
     if (deleted) {
       // the acl entry was deleted
     } else {
       // the acl entry was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`entity` | `[Acl.Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Acl.Entity)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if the ACL was deleted, `false` if it was not found  
  
### downloadTo(OutputStream outputStream, Blob.BlobSourceOption[] options)
    
    
    public void downloadTo(OutputStream outputStream, Blob.BlobSourceOption[] options)

Downloads this blob to the given output stream using specified blob read options. See Also: [Storage#downloadTo(BlobId, OutputStream, Storage.BlobSourceOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_downloadTo_)

**Parameters**  
---  
**Name** | **Description**  
`outputStream` | `[OutputStream](https://docs.oracle.com/javase/8/docs/api/java/io/OutputStream.html)`  
  
`options` | `[BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)[]`  
  
  
### downloadTo(Path path)
    
    
    public void downloadTo(Path path)

Downloads this blob to the given file path.

This method is replaced with [#downloadTo(Path, BlobSourceOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob#com_google_cloud_storage_Blob_downloadTo_), but is kept here for binary compatibility with the older versions of the client library.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[Path](https://docs.oracle.com/javase/8/docs/api/java/nio/file/Path.html)`  
destination  
  
### downloadTo(Path path, Blob.BlobSourceOption[] options)
    
    
    public void downloadTo(Path path, Blob.BlobSourceOption[] options)

Downloads this blob to the given file path using specified blob read options. See Also: [Storage#downloadTo(BlobId, Path, Storage.BlobSourceOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_downloadTo_)

**Parameters**  
---  
**Name** | **Description**  
`path` | `[Path](https://docs.oracle.com/javase/8/docs/api/java/nio/file/Path.html)`  
destination  
`options` | `[BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)[]`  
blob read options  
  
### equals(Object obj)
    
    
    public final boolean equals(Object obj)

Returns true if obj instance `Blob.toPb()` metadata representation and ` Blob.options` instance of StorageOptions are both equal.

**Parameter**  
---  
**Name** | **Description**  
`obj` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[BlobInfo.equals(Object o)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_equals_java_lang_Object_)

### exists(Blob.BlobSourceOption[] options)
    
    
    public boolean exists(Blob.BlobSourceOption[] options)

Checks if this blob exists.

Example of checking if the blob exists.
    
    
     boolean exists = blob.exists();
     if (exists) {
       // the blob exists
     } else {
       // the blob was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)[]`  
blob read options  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | true if this blob exists, false otherwise  
  
### getAcl(Acl.Entity entity)
    
    
    public Acl getAcl(Acl.Entity entity)

Returns the ACL entry for the specified entity on this blob or `null` if not found.

Example of getting the ACL entry for an entity.
    
    
     Acl acl = blob.getAcl(User.ofAllAuthenticatedUsers());
     

**Parameter**  
---  
**Name** | **Description**  
`entity` | `[Acl.Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Acl.Entity)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Acl)` |   
  
### getContent(Blob.BlobSourceOption[] options)
    
    
    public byte[] getContent(Blob.BlobSourceOption[] options)

Returns this blob's content.

Example of reading all bytes of the blob, if its generation matches the Blob#getGeneration() value, otherwise a [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException) is thrown.
    
    
     byte[] content = blob.getContent(BlobSourceOption.generationMatch());
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)[]`  
blob read options  
**Returns**  
---  
**Type** | **Description**  
`byte[]` |   
  
### getStorage()
    
    
    public Storage getStorage()

Returns the blob's `Storage` object used to issue requests.

**Returns**  
---  
**Type** | **Description**  
`[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage)` |   
  
### hashCode()
    
    
    public final int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[BlobInfo.hashCode()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_hashCode__)

### listAcls()
    
    
    public List<Acl> listAcls()

Lists the ACL entries for this blob.

Example of listing the ACL entries.
    
    
     List<Acl> acls = blob.listAcls();
     for (Acl acl : acls) {
       // do something with ACL entry
     }
     

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Acl)>` |   
  
### reader(Blob.BlobSourceOption[] options)
    
    
    public ReadChannel reader(Blob.BlobSourceOption[] options)

Returns a `ReadChannel` object for reading this blob's content.

Example of reading the blob's content through a reader.
    
    
     try (ReadChannel reader = blob.reader()) {
       ByteBuffer bytes = ByteBuffer.allocate(64 * 1024);
       while (reader.read(bytes) > 0) {
         bytes.flip();
         // do something with bytes
         bytes.clear();
       }
     }
     

Example of reading just a portion of the blob's content.
    
    
     int start = 1;
     int end = 8;
     try (ReadChannel reader = blob.reader()) {
       reader.seek(start);
       ByteBuffer bytes = ByteBuffer.allocate(end - start);
       reader.read(bytes);
       return bytes.array();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)[]`  
blob read options  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.ReadChannel` |   
  
### reload(Blob.BlobSourceOption[] options)
    
    
    public Blob reload(Blob.BlobSourceOption[] options)

Fetches the latest blob properties. Returns `null` if the blob no longer exists.

`options` parameter can contain the preconditions. For example, the user might want to get the blob properties only if the content has not been updated externally. ` StorageException` with the code `412` is thrown if preconditions fail.

Example of retrieving the blob's latest information only if the content is not updated externally:
    
    
     Blob blob = storage.get(BlobId.of(bucketName, blobName));
    
     doSomething();
    
     try {
       blob = blob.reload(Blob.BlobSourceOption.generationMatch());
     } catch (StorageException e) {
       if (e.getCode() == 412) {
         // the content was updated externally
       } else {
         throw e;
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)[]`  
preconditions to use on reload, see <https://cloud.google.com/storage/docs/json_api/v1/objects/get> for more information.  
**Returns**  
---  
**Type** | **Description**  
`[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob)` | a `Blob` object with latest information or `null` if no longer exists.  
  
### signUrl(long duration, TimeUnit unit, Storage.SignUrlOption[] options)
    
    
    public URL signUrl(long duration, TimeUnit unit, Storage.SignUrlOption[] options)

Generates a signed URL for this blob. If you want to allow access for a fixed amount of time to this blob, you can use this method to generate a URL that is only valid within a certain time period. This is particularly useful if you don't want publicly accessible blobs, but also don't want to require users to explicitly log in. Signing a URL requires a service account signer. If an instance of com.google.auth.ServiceAccountSigner was passed to [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions)' builder via `setCredentials(Credentials)` or the default credentials are being used and the environment variable `GOOGLE_APPLICATION_CREDENTIALS` is set or your application is running in App Engine, then `signUrl` will use that credentials to sign the URL. If the credentials passed to [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions) do not implement ServiceAccountSigner (this is the case, for instance, for Compute Engine credentials and Google Cloud SDK credentials) then `signUrl` will throw an IllegalStateException unless an implementation of ServiceAccountSigner is passed using the [SignUrlOption#signWith(ServiceAccountSigner)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.SignUrlOption#com_google_cloud_storage_Storage_SignUrlOption_signWith_) option.

A service account signer is looked for in the following order:

  1. The signer passed with the option [SignUrlOption#signWith(ServiceAccountSigner)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.SignUrlOption#com_google_cloud_storage_Storage_SignUrlOption_signWith_)
  2. The credentials passed to [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions)
  3. The default credentials, if no credentials were passed to [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions)



Example of creating a signed URL for the blob that is valid for 2 weeks, using the default credentials for signing the URL:
    
    
     URL signedUrl = blob.signUrl(14, TimeUnit.DAYS);
     

Example of creating a signed URL for the blob passing the [SignUrlOption#signWith(ServiceAccountSigner)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.SignUrlOption#com_google_cloud_storage_Storage_SignUrlOption_signWith_) option, that will be used to sign the URL:
    
    
     String keyPath = "/path/to/key.json";
     URL signedUrl = blob.signUrl(14, TimeUnit.DAYS, SignUrlOption.signWith(
         ServiceAccountCredentials.fromStream(new FileInputStream(keyPath))));
     

Example of creating a signed URL for a blob generation:
    
    
     URL signedUrl = blob.signUrl(1, TimeUnit.HOURS,
         SignUrlOption.withQueryParams(ImmutableMap.of("generation", "1576656755290328")));
     

See Also: [Signed-URLs](https://cloud.google.com/storage/docs/access-control#Signed-URLs)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
time until the signed URL expires, expressed in `unit`. The finer granularity supported is 1 second, finer granularities will be truncated  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
time unit of the `duration` parameter  
`options` | `[SignUrlOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.SignUrlOption)[]`  
optional URL signing options  
**Returns**  
---  
**Type** | **Description**  
`[URL](https://docs.oracle.com/javase/8/docs/api/java/net/URL.html)` | a signed URL for this blob and the specified options  
  
### toBuilder()
    
    
    public Blob.Builder toBuilder()

Returns a builder for the current blob.

**Returns**  
---  
**Type** | **Description**  
`[Blob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.Builder)` |   
**Overrides**

[BlobInfo.toBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo#com_google_cloud_storage_BlobInfo_toBuilder__)

### update(Storage.BlobTargetOption[] options)
    
    
    public Blob update(Storage.BlobTargetOption[] options)

Updates the blob properties. The `options` parameter contains the preconditions for applying the update. To update the properties call [#toBuilder()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob#com_google_cloud_storage_Blob_toBuilder__), set the properties you want to change, build the new `Blob` instance, and then call [#update(BlobTargetOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob#com_google_cloud_storage_Blob_update_).

The property update details are described in [Storage#update(BlobInfo)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_update_com_google_cloud_storage_BlobInfo_). [Storage#update(BlobInfo, BlobTargetOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_update_) describes how to specify preconditions.

Example of updating the content type:
    
    
     BlobId blobId = BlobId.of(bucketName, blobName);
     Blob blob = storage.get(blobId);
     blob.toBuilder().setContentType("text/plain").build().update();
     

See Also: <https://cloud.google.com/storage/docs/json_api/v1/objects/update>

**Parameter**  
---  
**Name** | **Description**  
`options` | `[BlobTargetOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BlobTargetOption)[]`  
preconditions to apply the update  
**Returns**  
---  
**Type** | **Description**  
`[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob)` | the updated `Blob`  
  
### updateAcl(Acl acl)
    
    
    public Acl updateAcl(Acl acl)

Updates an ACL entry on this blob.

Example of updating a new ACL entry.
    
    
     Acl acl = blob.updateAcl(Acl.of(User.ofAllAuthenticatedUsers(), Acl.Role.OWNER));
     

**Parameter**  
---  
**Name** | **Description**  
`acl` | `[Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Acl)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Acl](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Acl)` |   
  
### writer(Storage.BlobWriteOption[] options)
    
    
    public WriteChannel writer(Storage.BlobWriteOption[] options)

Returns a `WriteChannel` object for writing to this blob. By default any md5 and crc32c values in the current blob are ignored unless requested via the ` BlobWriteOption.md5Match` and `BlobWriteOption.crc32cMatch` options.

Example of writing the blob's content through a writer.
    
    
     byte[] content = "Hello, World!".getBytes(UTF_8);
     try (WriteChannel writer = blob.writer()) {
         writer.write(ByteBuffer.wrap(content, 0, content.length));
     } catch (IOException ex) {
       // handle exception
     }
     blob = blob.reload();
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[BlobWriteOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BlobWriteOption)[]`  
target blob options  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.WriteChannel` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
