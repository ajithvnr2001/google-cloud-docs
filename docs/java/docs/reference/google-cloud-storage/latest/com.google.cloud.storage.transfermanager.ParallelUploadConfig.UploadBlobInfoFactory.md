---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.UploadBlobInfoFactory
title: Interface ParallelUploadConfig.UploadBlobInfoFactory (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:42.998524+00:00
---

# Interface ParallelUploadConfig.UploadBlobInfoFactory (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.UploadBlobInfoFactory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ParallelUploadConfig.UploadBlobInfoFactory (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 
    
    
    public static interface ParallelUploadConfig.UploadBlobInfoFactory

## Static Methods 

### defaultInstance()
    
    
    public static ParallelUploadConfig.UploadBlobInfoFactory defaultInstance()

The default instance which applies not modification to the provided `fileName`

**Returns**  
---  
**Type** | **Description**  
`[ParallelUploadConfig.UploadBlobInfoFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.UploadBlobInfoFactory)` |   
  
### prefixObjectNames(String prefix)
    
    
    public static ParallelUploadConfig.UploadBlobInfoFactory prefixObjectNames(String prefix)

Adapter factory to provide the same semantics as if using Builder#setPrefix(String)

**Parameter**  
---  
**Name** | **Description**  
`prefix` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ParallelUploadConfig.UploadBlobInfoFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.UploadBlobInfoFactory)` |   
  
### transformFileName(Function<String,String> fileNameTransformer)
    
    
    public static ParallelUploadConfig.UploadBlobInfoFactory transformFileName(Function<String,String> fileNameTransformer)

Convenience method to "lift" a [Function](https://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html) that transforms the file name to an UploadBlobInfoFactory

**Parameter**  
---  
**Name** | **Description**  
`fileNameTransformer` | `[Function](https://docs.oracle.com/javase/8/docs/api/java/util/function/Function.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[ParallelUploadConfig.UploadBlobInfoFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.UploadBlobInfoFactory)` |   
  
## Methods 

### apply(String bucketName, String fileName)
    
    
    public abstract BlobInfo apply(String bucketName, String fileName)

Method to produce a [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo) to be used for the upload to Cloud Storage.

The bucket name in the returned BlobInfo MUST be equal to the value provided to the ParallelUploadConfig.Builder#setBucketName(String), if not that upload will fail with a [TransferStatus#FAILED_TO_START](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferStatus#com_google_cloud_storage_transfermanager_TransferStatus_FAILED_TO_START) and a [BucketNameMismatchException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.BucketNameMismatchException).

**Parameters**  
---  
**Name** | **Description**  
`bucketName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the bucket to be uploaded to. The value provided here will be the value from [ParallelUploadConfig#getBucketName()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig#com_google_cloud_storage_transfermanager_ParallelUploadConfig_getBucketName__).  
`fileName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The String representation of the absolute path of the file to be uploaded  
**Returns**  
---  
**Type** | **Description**  
`[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo)` | The instance of [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo) that should be used to upload the file to Cloud Storage.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
