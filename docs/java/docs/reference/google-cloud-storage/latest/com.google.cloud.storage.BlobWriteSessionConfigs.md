---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobWriteSessionConfigs
title: Class BlobWriteSessionConfigs (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:41:22.447533+00:00
---

# Class BlobWriteSessionConfigs (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobWriteSessionConfigs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BlobWriteSessionConfigs (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public final class BlobWriteSessionConfigs

Factory class to select and construct [BlobWriteSessionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobWriteSessionConfig)s.

There are several strategies which can be used to upload a [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob) to Google Cloud Storage. This class provides factories which allow you to select the appropriate strategy for your workload.

Comparison of Strategies Strategy | Factory Method(s) | Description | Transport(s) Supported | Considerations | Retry Support | Cloud Storage API used  
---|---|---|---|---|---|---  
Default (Chunk based upload) | [#getDefault()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobWriteSessionConfigs#com_google_cloud_storage_BlobWriteSessionConfigs_getDefault__) |  Buffer up to a configurable amount of bytes in memory, write to Cloud Storage when full or close. Buffer size is configurable via [DefaultBlobWriteSessionConfig#withChunkSize(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.DefaultBlobWriteSessionConfig#com_google_cloud_storage_DefaultBlobWriteSessionConfig_withChunkSize_int_) | gRPC, HTTP | The network will only be used for the following operations: 

  1. Creating the Resumable Upload Session
  2. Transmitting zero or more incremental chunks
  3. Transmitting the final chunk and finalizing the Resumable Upload Session
  4. If any of the above are interrupted with a retryable error, the Resumable Upload Session will be queried to reconcile client side state with Cloud Storage 

|  Each chunk is retried up to the limitations specified in StorageOptions#getRetrySettings() | [Resumable Upload](https://cloud.google.com/storage/docs/resumable-uploads)  
Buffer to disk then upload | 

  * [#bufferToDiskThenUpload(Path)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobWriteSessionConfigs#com_google_cloud_storage_BlobWriteSessionConfigs_bufferToDiskThenUpload_java_nio_file_Path_)
  * [bufferToDiskThenUpload(Collection < Path>)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobWriteSessionConfigs#com_google_cloud_storage_BlobWriteSessionConfigs_bufferToDiskThenUpload_java_util_Collection_java_nio_file_Path__)
  * [#bufferToTempDirThenUpload()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobWriteSessionConfigs#com_google_cloud_storage_BlobWriteSessionConfigs_bufferToTempDirThenUpload__)

|  Buffer bytes to a temporary file on disk. On close() upload the entire files contents to Cloud Storage. Delete the temporary file.  | gRPC, HTTP | 

  1. A Resumable Upload Session will be used to upload the file on disk.
  2. If the upload is interrupted with a retryable error, the Resumable Upload Session will be queried to restart the upload from Cloud Storage's last received byte 

|  Upload the file in the fewest number of RPC possible retrying within the limitations specified in StorageOptions#getRetrySettings() | [Resumable Upload](https://cloud.google.com/storage/docs/resumable-uploads)  
Journal to disk while uploading | [journaling(Collection < Path>)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobWriteSessionConfigs#com_google_cloud_storage_BlobWriteSessionConfigs_journaling_java_util_Collection_java_nio_file_Path__) |  Create a Resumable Upload Session, before transmitting bytes to Cloud Storage write to a recovery file on disk. If the stream to Cloud Storage is interrupted with a retryable error query the offset of the Resumable Upload Session, then open the recovery file from the offset and transmit the bytes to Cloud Storage.  | gRPC | 

  1. The stream to Cloud Storage will be held open until a) the write is complete b) the stream is interrupted 
  2. Because the bytes are journaled to disk, the upload to Cloud Storage can only be as fast as the disk. 
  3. The use of [Compute Engine Local NVMe SSD](https://cloud.google.com/compute/docs/disks/local-ssd#nvme) is strongly encouraged compared to Compute Engine Persistent Disk. 

|  Opening the stream for upload will be retried up to the limitations specified in StorageOptions#getRetrySettings() All bytes are buffered to disk and allow for recovery from any arbitrary offset.  | [Resumable Upload](https://cloud.google.com/storage/docs/resumable-uploads)  
Parallel Composite Upload | [#parallelCompositeUpload()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobWriteSessionConfigs#com_google_cloud_storage_BlobWriteSessionConfigs_parallelCompositeUpload__) |  Break the stream of bytes into smaller part objects uploading each part in parallel. Then composing the parts together to make the ultimate object.  | gRPC, HTTP | 

  1. Performing parallel composite uploads costs more money. [Class A](https://cloud.google.com/storage/pricing#operations-by-class) operations are performed to create each part and to perform each compose. If a storage tier other than [`STANDARD`](https://cloud.google.com/storage/docs/storage-classes) is used, early deletion fees apply to deletion of the parts. An illustrative example. Upload a 5GiB object using 64MiB as the max size per part. 
     1. 80 Parts will be created (Class A)
     2. 3 compose calls will be performed (Class A)
     3. Delete 80 Parts along with 2 intermediary Compose objects (Free tier as long as `STANDARD` class)
    
    Once the parts and intermediary compose objects are deleted, there will be no storage charges related to those temporary objects.
         </li>
         <li>
           The service account/credentials used to perform the parallel composite upload require
           <a href="https://cloud.google.com/storage/docs/access-control/iam-permissions#object_permissions"><code>storage.objects.delete</code></a>
           in order to cleanup the temporary part and intermediary compose objects.
           <p><i>To handle handle part and intermediary compose object deletion out of band</i>
           passing <xref uid="" data-throw-if-not-resolved="false">PartCleanupStrategy#never()</xref> to <xref uid="com.google.cloud.storage.ParallelCompositeUploadBlobWriteSessionConfig.withPartCleanupStrategy*" data-throw-if-not-resolved="false">ParallelCompositeUploadBlobWriteSessionConfig#withPartCleanupStrategy(PartCleanupStrategy)</xref>
           will prevent automatic cleanup.
         </li>
         <li>
           Please see the <a href="https://cloud.google.com/storage/docs/parallel-composite-uploads">
           Parallel composite uploads</a> documentation for a more in depth explanation of the
           limitations of Parallel composite uploads.
         </li>
         <li>
           A failed upload can leave part and intermediary compose objects behind which will count
           as storage usage, and you will be billed for it.
           <p>By default if an upload fails, an attempt to cleanup the part and intermediary compose
           will be made. However if the program were to crash there is no means for the client to
           perform the cleanup.
           <p>Every part and intermediary compose object will be created with a name which ends in
           <code>.part</code>. An Object Lifecycle Management rule can be setup on your bucket to automatically
           cleanup objects with the suffix after some period of time. See
           <a href="https://cloud.google.com/storage/docs/lifecycle">Object Lifecycle Management</a>
           for full details and a guide on how to setup a <a href="https://cloud.google.com/storage/docs/lifecycle#delete">Delete</a>
           rule with a <a href="https://cloud.google.com/storage/docs/lifecycle#matchesprefix-suffix">suffix match</a> condition.
         </li>
         <li>
           Using parallel composite uploads are not a one size fits all solution. They have very
           real overhead until uploading a large enough object. The inflection point is dependent
           upon many factors, and there is no one size fits all value. You will need to experiment
           with your deployment and workload to determine if parallel composite uploads are useful
           to you.
         </li>
       </ol>
     </td>
     <td>
       Automatic retires will be applied for the following:
       <ol>
         <li>Creation of each individual part</li>
         <li>Performing an intermediary compose</li>
         <li>Performing a delete to cleanup each part and intermediary compose object</li>
       </ol>
    
       Retrying the creation of the final object is contingent upon if an appropriate precondition
       is supplied when calling <xref uid="com.google.cloud.storage.Storage.blobWriteSession*" data-throw-if-not-resolved="false">Storage#blobWriteSession(BlobInfo, BlobWriteOption...)</xref>.
       Either <xref uid="" data-throw-if-not-resolved="false">BlobTargetOption#doesNotExist()</xref> or <xref uid="com.google.cloud.storage.Storage.BlobTargetOption.generationMatch(long)" data-throw-if-not-resolved="false">Storage.BlobTargetOption#generationMatch(long)</xref>
       should be specified in order to make the final request idempotent.
       <p>Each operation will be retried up to the limitations specified in <xref uid="com.google.cloud.storage.StorageOptions.getRetrySettings*" data-throw-if-not-resolved="false">StorageOptions#getRetrySettings()</xref>
     </td>
     <td>
       <ul>
         <li><a href="https://cloud.google.com/storage/docs/parallel-composite-uploads">Parallel composite uploads</a></li>
         <li><a href="https://cloud.google.com/storage/docs/uploading-objects-from-memory">Direct uploads</a></li>
         <li><a href="https://cloud.google.com/storage/docs/composite-objects">Compose</a></li>
         <li><a href="https://cloud.google.com/storage/docs/deleting-objects">Object delete</a></li>
       </ul>
     </td>
    


  
See Also: [Storage#blobWriteSession(BlobInfo, BlobWriteOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_blobWriteSession_), [BlobWriteSessionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobWriteSessionConfig), GrpcStorageOptions.Builder#setBlobWriteSessionConfig(BlobWriteSessionConfig)

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BlobWriteSessionConfigs

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

### bidiWrite()
    
    
    public static BidiBlobWriteSessionConfig bidiWrite()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Factory to produce a resumable upload using a bi-directional stream. This should provide a small performance increase compared to a regular resumable upload.

Configuration of the buffer size can be performed via [BidiBlobWriteSessionConfig#withBufferSize(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BidiBlobWriteSessionConfig#com_google_cloud_storage_BidiBlobWriteSessionConfig_withBufferSize_int_).

**Returns**  
---  
**Type** | **Description**  
`[BidiBlobWriteSessionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BidiBlobWriteSessionConfig)` |   
  
### bufferToDiskThenUpload(Path path)
    
    
    public static BufferToDiskThenUpload bufferToDiskThenUpload(Path path)

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Create a new [BlobWriteSessionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobWriteSessionConfig) which will first buffer the content of the object to a temporary file under the specified `path`.

Once the file on disk is closed, the entire file will then be uploaded to Cloud Storage. See Also: [Storage#blobWriteSession(BlobInfo, BlobWriteOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_blobWriteSession_), GrpcStorageOptions.Builder#setBlobWriteSessionConfig(BlobWriteSessionConfig)

**Parameter**  
---  
**Name** | **Description**  
`path` | `[Path](https://docs.oracle.com/javase/8/docs/api/java/nio/file/Path.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BufferToDiskThenUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BufferToDiskThenUpload)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### bufferToDiskThenUpload(Collection<Path> paths)
    
    
    public static BufferToDiskThenUpload bufferToDiskThenUpload(Collection<Path> paths)

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Create a new [BlobWriteSessionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobWriteSessionConfig) which will first buffer the content of the object to a temporary file under one of the specified `paths`.

Once the file on disk is closed, the entire file will then be uploaded to Cloud Storage.

The specifics of how the work is spread across multiple paths is undefined and subject to change. See Also: [Storage#blobWriteSession(BlobInfo, BlobWriteOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_blobWriteSession_), GrpcStorageOptions.Builder#setBlobWriteSessionConfig(BlobWriteSessionConfig)

**Parameter**  
---  
**Name** | **Description**  
`paths` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[Path](https://docs.oracle.com/javase/8/docs/api/java/nio/file/Path.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[BufferToDiskThenUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BufferToDiskThenUpload)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### bufferToTempDirThenUpload()
    
    
    public static BlobWriteSessionConfig bufferToTempDirThenUpload()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Create a new [BlobWriteSessionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobWriteSessionConfig) which will first buffer the content of the object to a temporary file under `java.io.tmpdir`.

Once the file on disk is closed, the entire file will then be uploaded to Cloud Storage. See Also: [Storage#blobWriteSession(BlobInfo, BlobWriteOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_blobWriteSession_), GrpcStorageOptions.Builder#setBlobWriteSessionConfig(BlobWriteSessionConfig)

**Returns**  
---  
**Type** | **Description**  
`[BlobWriteSessionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobWriteSessionConfig)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### getDefault()
    
    
    public static DefaultBlobWriteSessionConfig getDefault()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Factory to produce the default configuration for uploading an object to Cloud Storage.

Configuration of the chunk size can be performed via [DefaultBlobWriteSessionConfig#withChunkSize(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.DefaultBlobWriteSessionConfig#com_google_cloud_storage_DefaultBlobWriteSessionConfig_withChunkSize_int_). See Also: GrpcStorageDefaults#getDefaultStorageWriterConfig()

**Returns**  
---  
**Type** | **Description**  
`[DefaultBlobWriteSessionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.DefaultBlobWriteSessionConfig)` |   
  
### journaling(Collection<Path> paths)
    
    
    public static JournalingBlobWriteSessionConfig journaling(Collection<Path> paths)

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Create a new [BlobWriteSessionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobWriteSessionConfig) which will journal writes to a temporary file under one of the specified `paths` before transmitting the bytes to Cloud Storage.

The specifics of how the work is spread across multiple paths is undefined and subject to change. See Also: [Storage#blobWriteSession(BlobInfo, BlobWriteOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_blobWriteSession_), GrpcStorageOptions.Builder#setBlobWriteSessionConfig(BlobWriteSessionConfig)

**Parameter**  
---  
**Name** | **Description**  
`paths` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[Path](https://docs.oracle.com/javase/8/docs/api/java/nio/file/Path.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[JournalingBlobWriteSessionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.JournalingBlobWriteSessionConfig)` |   
  
### parallelCompositeUpload()
    
    
    public static ParallelCompositeUploadBlobWriteSessionConfig parallelCompositeUpload()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Create a new [BlobWriteSessionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobWriteSessionConfig) which will perform a [Parallel Composite Upload](https://cloud.google.com/storage/docs/parallel-composite-uploads) by breaking the stream into parts and composing the parts together to make the ultimate object. See Also: [Storage#blobWriteSession(BlobInfo, BlobWriteOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_blobWriteSession_), GrpcStorageOptions.Builder#setBlobWriteSessionConfig(BlobWriteSessionConfig)

**Returns**  
---  
**Type** | **Description**  
`[ParallelCompositeUploadBlobWriteSessionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ParallelCompositeUploadBlobWriteSessionConfig)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
