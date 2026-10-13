---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig
title: Class TransferManagerConfig (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:47.681668+00:00
---

# Class TransferManagerConfig (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TransferManagerConfig (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 
    
    
    public final class TransferManagerConfig

Configuration for an instance of [TransferManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager) See Also: Builder

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TransferManagerConfig

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

### newBuilder()
    
    
    public static TransferManagerConfig.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[TransferManagerConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.Builder)` |   
  
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

### getMaxWorkers()
    
    
    public int getMaxWorkers()

Maximum amount of workers to be allocated to perform work in Transfer Manager See Also: Builder#setMaxWorkers(int)

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getParallelCompositeUploadPartNamingStrategy()
    
    
    public ParallelCompositeUploadBlobWriteSessionConfig.PartNamingStrategy getParallelCompositeUploadPartNamingStrategy()

Part Naming Strategy to be used during Parallel Composite Uploads See Also: Builder#setParallelCompositeUploadPartNamingStrategy(PartNamingStrategy)

**Returns**  
---  
**Type** | **Description**  
`[ParallelCompositeUploadBlobWriteSessionConfig.PartNamingStrategy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ParallelCompositeUploadBlobWriteSessionConfig.PartNamingStrategy)` |   
  
### getPerWorkerBufferSize()
    
    
    public int getPerWorkerBufferSize()

Buffer size allowed to each worker See Also: Builder#setPerWorkerBufferSize(int)

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getService()
    
    
    public TransferManager getService()

The service object for [TransferManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager)

**Returns**  
---  
**Type** | **Description**  
`[TransferManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager)` |   
  
### getStorageOptions()
    
    
    public StorageOptions getStorageOptions()

Storage options that Transfer Manager will use to interact with Google Cloud Storage See Also: Builder#setStorageOptions(StorageOptions)

**Returns**  
---  
**Type** | **Description**  
`[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions)` |   
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### isAllowDivideAndConquerDownload()
    
    
    public boolean isAllowDivideAndConquerDownload()

Whether to allow Transfer Manager to perform chunked Uploads/Downloads if it determines chunking will be beneficial See Also: Builder#setAllowDivideAndConquerDownload(boolean)

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isAllowParallelCompositeUpload()
    
    
    public boolean isAllowParallelCompositeUpload()

Whether to allow Transfer Manager to perform Parallel Composite Uploads if it determines chunking will be beneficial See Also: <xref uid="Builder#setAllowParallelCompositeUpload(boolean)

Note: Performing parallel composite uploads costs more money. [Class A](https://cloud.google.com/storage/pricing#operations-by-class) operations are performed to create each part and to perform each compose. If a storage tier other than [`STANDARD`](https://cloud.google.com/storage/docs/storage-classes) is used, early deletion fees apply to deletion of the parts. 

Please see the [Parallel composite uploads](https://cloud.google.com/storage/docs/parallel-composite-uploads) documentation for a more in depth explanation of the limitations of Parallel composite uploads." data-throw-if-not-resolved="false">Builder#setAllowParallelCompositeUpload(boolean)

Note: Performing parallel composite uploads costs more money. [Class A](https://cloud.google.com/storage/pricing#operations-by-class) operations are performed to create each part and to perform each compose. If a storage tier other than [`STANDARD`](https://cloud.google.com/storage/docs/storage-classes) is used, early deletion fees apply to deletion of the parts. 

Please see the [Parallel composite uploads](https://cloud.google.com/storage/docs/parallel-composite-uploads) documentation for a more in depth explanation of the limitations of Parallel composite uploads.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### toBuilder()
    
    
    public TransferManagerConfig.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[TransferManagerConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.Builder)` |   
  
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
