---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel
title: Interface BlobAppendableUpload.AppendableUploadWriteableByteChannel (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:41:13.566765+00:00
---

# Interface BlobAppendableUpload.AppendableUploadWriteableByteChannel (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BlobAppendableUpload.AppendableUploadWriteableByteChannel (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public static interface BlobAppendableUpload.AppendableUploadWriteableByteChannel extends WritableByteChannel

The [WritableByteChannel](https://docs.oracle.com/javase/8/docs/api/java/nio/channels/WritableByteChannel.html) returned from [BlobAppendableUpload#open()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload#com_google_cloud_storage_BlobAppendableUpload_open__).

This interface allows writing bytes to an Appendable Upload, and provides methods to close this channel -- optionally finalizing the upload.

The [#write(ByteBuffer)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_write_java_nio_ByteBuffer_) method of this channel is non-blocking.

## Implements

[WritableByteChannel](https://docs.oracle.com/javase/8/docs/api/java/nio/channels/WritableByteChannel.html)

## Methods 

### close()
    
    
    public abstract void close()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

**This method is blocking**

Close this instance to further [#write(ByteBuffer)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_write_java_nio_ByteBuffer_)ing.

Whether the upload is finalized during this depends on the [BlobAppendableUploadConfig#getCloseAction()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig#com_google_cloud_storage_BlobAppendableUploadConfig_getCloseAction__) provided to create the [BlobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload). If [BlobAppendableUploadConfig#getCloseAction()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig#com_google_cloud_storage_BlobAppendableUploadConfig_getCloseAction__)`== `CloseAction#FINALIZE_WHEN_CLOSING, [#finalizeAndClose()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_finalizeAndClose__) will be called. If [BlobAppendableUploadConfig#getCloseAction()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig#com_google_cloud_storage_BlobAppendableUploadConfig_getCloseAction__)`== `CloseAction#CLOSE_WITHOUT_FINALIZING, [#closeWithoutFinalizing()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_closeWithoutFinalizing__) will be called. See Also: [Storage#blobAppendableUpload(BlobInfo, BlobAppendableUploadConfig, BlobWriteOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_blobAppendableUpload_), [BlobAppendableUploadConfig#getCloseAction()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig#com_google_cloud_storage_BlobAppendableUploadConfig_getCloseAction__), [BlobAppendableUploadConfig#withCloseAction(CloseAction)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig#com_google_cloud_storage_BlobAppendableUploadConfig_withCloseAction_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### close(@Nullable String expectedCrc32c)
    
    
    public abstract void close(@Nullable String expectedCrc32c)

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

**This method is blocking**

Close this instance to further [#write(ByteBuffer)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_write_java_nio_ByteBuffer_)ing.

This method behaves like [#close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_close__), but allows passing an optional expected CRC32c checksum. If expectedCrc32c is null, it behaves identically to [#close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_close__). See Also: [Storage#blobAppendableUpload(BlobInfo, BlobAppendableUploadConfig, BlobWriteOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_blobAppendableUpload_), [BlobAppendableUploadConfig#getCloseAction()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig#com_google_cloud_storage_BlobAppendableUploadConfig_getCloseAction__), [BlobAppendableUploadConfig#withCloseAction(CloseAction)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig#com_google_cloud_storage_BlobAppendableUploadConfig_withCloseAction_)

**Parameter**  
---  
**Name** | **Description**  
`expectedCrc32c` | `@org.checkerframework.checker.nullness.qual.Nullable java.lang.String`  
A Base64 encoded string representing the expected CRC32c value for the entire object. If provided, the server will validate the final object's CRC32c against this value. If there's a mismatch, the server will return an error (such as InvalidArgument), and this method will throw a [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException) or equivalent exception, failing the upload. May be null.  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | if the stream was not configured with CloseAction#FINALIZE_WHEN_CLOSING and expectedCrc32c is not null.  
  
### closeWithoutFinalizing()
    
    
    public abstract void closeWithoutFinalizing()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

**This method is blocking**

Close this instance to further [#write(ByteBuffer)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_write_java_nio_ByteBuffer_)ing without finalizing the upload. This will close any underlying stream and release any releasable resources once out of scope.

This method, AppendableUploadWriteableByteChannel#finalizeAndClose() and AppendableUploadWriteableByteChannel#close() are mutually exclusive. If one of the other methods are called before this method, this method will be a no-op. See Also: [BlobAppendableUploadConfig.CloseAction#CLOSE_WITHOUT_FINALIZING](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.CloseAction#com_google_cloud_storage_BlobAppendableUploadConfig_CloseAction_CLOSE_WITHOUT_FINALIZING), [Storage#blobAppendableUpload(BlobInfo, BlobAppendableUploadConfig, BlobWriteOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_blobAppendableUpload_), [BlobAppendableUploadConfig#getCloseAction()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig#com_google_cloud_storage_BlobAppendableUploadConfig_getCloseAction__), [BlobAppendableUploadConfig#withCloseAction(CloseAction)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig#com_google_cloud_storage_BlobAppendableUploadConfig_withCloseAction_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### finalizeAndClose()
    
    
    public abstract void finalizeAndClose()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

**This method is blocking**

Finalize the upload and close this instance to further [#write(ByteBuffer)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_write_java_nio_ByteBuffer_)ing. This will close any underlying stream and release any releasable resources once out of scope.

Once this method is called, and returns no more writes to the object will be allowed by GCS.

This method and [#close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_close__) are mutually exclusive. If one of the other methods are called before this method, this method will be a no-op. See Also: [BlobAppendableUploadConfig.CloseAction#FINALIZE_WHEN_CLOSING](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.CloseAction#com_google_cloud_storage_BlobAppendableUploadConfig_CloseAction_FINALIZE_WHEN_CLOSING), [Storage#blobAppendableUpload(BlobInfo, BlobAppendableUploadConfig, BlobWriteOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_blobAppendableUpload_), [BlobAppendableUploadConfig#getCloseAction()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig#com_google_cloud_storage_BlobAppendableUploadConfig_getCloseAction__), [BlobAppendableUploadConfig#withCloseAction(CloseAction)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig#com_google_cloud_storage_BlobAppendableUploadConfig_withCloseAction_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### finalizeAndClose(@Nullable String expectedCrc32c)
    
    
    public abstract void finalizeAndClose(@Nullable String expectedCrc32c)

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

**This method is blocking**

Finalize the upload and close this instance to further [#write(ByteBuffer)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_write_java_nio_ByteBuffer_)ing. This will close any underlying stream and release any releasable resources once out of scope.

Once this method is called, and returns no more writes to the object will be allowed by GCS.

This method and [#close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_close__) are mutually exclusive. If one of the other methods are called before this method, this method will be a no-op. See Also: [BlobAppendableUploadConfig.CloseAction#FINALIZE_WHEN_CLOSING](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.CloseAction#com_google_cloud_storage_BlobAppendableUploadConfig_CloseAction_FINALIZE_WHEN_CLOSING), [Storage#blobAppendableUpload(BlobInfo, BlobAppendableUploadConfig, BlobWriteOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_blobAppendableUpload_), [BlobAppendableUploadConfig#getCloseAction()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig#com_google_cloud_storage_BlobAppendableUploadConfig_getCloseAction__), [BlobAppendableUploadConfig#withCloseAction(CloseAction)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig#com_google_cloud_storage_BlobAppendableUploadConfig_withCloseAction_)

**Parameter**  
---  
**Name** | **Description**  
`expectedCrc32c` | `@org.checkerframework.checker.nullness.qual.Nullable java.lang.String`  
A Base64 encoded string representing the expected CRC32c value for the entire object. If provided, the server will validate the final object's CRC32c against this value. If there's a mismatch, the server will return an error (such as InvalidArgument), and this method will throw a [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException) or equivalent exception, failing the upload.  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### flush()
    
    
    public abstract void flush()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

**This method is blocking**

Block the invoking thread, waiting until the number of bytes written so far has been acknowledged by Google Cloud Storage.

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | if an error happens while waiting for the flush to complete  
  
### write(ByteBuffer src)
    
    
    public abstract int write(ByteBuffer src)

**This method is non-blocking**

Consume as many bytes as can fit in the underlying outbound queue. The size of the outbound queue is determined from [BlobAppendableUploadConfig#getFlushPolicy()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig#com_google_cloud_storage_BlobAppendableUploadConfig_getFlushPolicy__)` .`getMaxPendingBytes(). If the outbound queue is full, and can not fit more bytes, this method will return 0.

If your application needs to empty its ByteBuffer before progressing, use our helper method [StorageChannelUtils#blockingEmptyTo(ByteBuffer, WritableByteChannel)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageChannelUtils#com_google_cloud_storage_StorageChannelUtils_blockingEmptyTo_java_nio_ByteBuffer_java_nio_channels_WritableByteChannel_) like so:
    
    
     try (AppendableUploadWriteableByteChannel channel = session.open()) {
       int written = StorageChannelUtils.blockingEmptyTo(byteBuffer, channel);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`src` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
The buffer from which bytes are to be retrieved  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The number of bytes written, possibly zero  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | If this channel is closed  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
