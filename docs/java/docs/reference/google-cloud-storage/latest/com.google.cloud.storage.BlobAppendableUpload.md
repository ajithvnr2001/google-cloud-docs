---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload
title: Interface BlobAppendableUpload (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:41:13.413105+00:00
---

# Interface BlobAppendableUpload (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BlobAppendableUpload (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public interface BlobAppendableUpload extends BlobWriteSession

Interface representing those methods which can be used to write to and interact with an appendable upload. See Also: [Storage#blobAppendableUpload(BlobInfo, BlobAppendableUploadConfig, BlobWriteOption...)](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_blobAppendableUpload_)

## Implements

[BlobWriteSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobWriteSession)

## Methods 

### getResult()
    
    
    public abstract ApiFuture<BlobInfo> getResult()

Return an [ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)`<BlobInfo>` which will represent the state of the object in Google Cloud Storage.

This future will not resolve until:

  1. The object is successfully finalized in Google Cloud Storage by calling AppendableUploadWriteableByteChannel#finalizeAndClose()
  2. This session is detached from the upload without finalizing by calling AppendableUploadWriteableByteChannel#closeWithoutFinalizing()
  3. The session is closed by calling AppendableUploadWriteableByteChannel#close()
  4. A terminal failure occurs, the terminal failure will become the exception result 



_NOTICE:_ Some fields may not be populated unless finalization has completed.

If a terminal failure is encountered, calling either ApiFuture#get() or ApiFuture#get(long, TimeUnit) will result in an [java.util.concurrent.ExecutionException](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ExecutionException.html) with the cause.

**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo)>` |   
  
### open()
    
    
    public abstract BlobAppendableUpload.AppendableUploadWriteableByteChannel open()

Open the AppendableUploadWriteableByteChannel for this session.

A session may only be `open`ed once. If multiple calls to open are made, an illegal state exception will be thrown

The returned `AppendableUploadWriteableByteChannel` can throw IOExceptions from any of its usual methods. Any [IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html) thrown can have a cause of a [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException). However, not all `IOExceptions` will have `StorageException`s.

**Returns**  
---  
**Type** | **Description**  
`[BlobAppendableUpload.AppendableUploadWriteableByteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | When creating the AppendableUploadWriteableByteChannel if an unrecoverable underlying IOException occurs it can be rethrown  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
