---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult.Builder
title: Class UploadResult.Builder (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:32.124072+00:00
---

# Class UploadResult.Builder (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class UploadResult.Builder (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 
    
    
    public static final class UploadResult.Builder

Builds an instance of UploadResult See Also: [UploadResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult)

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > UploadResult.Builder

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

## Methods 

### build()
    
    
    public UploadResult build()

Creates an UploadResult object.

**Returns**  
---  
**Type** | **Description**  
`[UploadResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult)` | [UploadResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult)  
  
### setException(@NonNull Exception exception)
    
    
    public UploadResult.Builder setException(@NonNull Exception exception)

Sets the exception produced by a failed upload operation. This field will only be populated if the Transfer was not [success](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferStatus#com_google_cloud_storage_transfermanager_TransferStatus_SUCCESS)ful or [skipped](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferStatus#com_google_cloud_storage_transfermanager_TransferStatus_SKIPPED) See Also: [UploadResult#getException()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult#com_google_cloud_storage_transfermanager_UploadResult_getException__)

**Parameter**  
---  
**Name** | **Description**  
`exception` | `@org.checkerframework.checker.nullness.qual.NonNull java.lang.Exception`  
  
**Returns**  
---  
**Type** | **Description**  
`[UploadResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult.Builder)` | the Builder instance with the value for exception modified.  
  
### setInput(@NonNull BlobInfo input)
    
    
    public UploadResult.Builder setInput(@NonNull BlobInfo input)

Sets the BlobInfo for the object request for upload. This field is required. See Also: [UploadResult#getInput()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult#com_google_cloud_storage_transfermanager_UploadResult_getInput__)

**Parameter**  
---  
**Name** | **Description**  
`input` | `@org.checkerframework.checker.nullness.qual.NonNull com.google.cloud.storage.BlobInfo`  
  
**Returns**  
---  
**Type** | **Description**  
`[UploadResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult.Builder)` | the Builder instance with the value for BlobInfo modified.  
  
### setStatus(@NonNull TransferStatus status)
    
    
    public UploadResult.Builder setStatus(@NonNull TransferStatus status)

Sets the Status of the Upload request. This field is required. See Also: [UploadResult#getStatus()](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult#com_google_cloud_storage_transfermanager_UploadResult_getStatus__), TransferStatus

**Parameter**  
---  
**Name** | **Description**  
`status` | `@org.checkerframework.checker.nullness.qual.NonNull com.google.cloud.storage.transfermanager.TransferStatus`  
  
**Returns**  
---  
**Type** | **Description**  
`[UploadResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult.Builder)` | the Builder instance with the value for status modified.  
  
### setUploadedBlob(@NonNull BlobInfo uploadedBlob)
    
    
    public UploadResult.Builder setUploadedBlob(@NonNull BlobInfo uploadedBlob)

Sets the BlobInfo for the uploaded object. This field will only be populated if the Transfer was a [SUCCESS](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferStatus#com_google_cloud_storage_transfermanager_TransferStatus_SUCCESS).

**Parameter**  
---  
**Name** | **Description**  
`uploadedBlob` | `@org.checkerframework.checker.nullness.qual.NonNull com.google.cloud.storage.BlobInfo`  
  
**Returns**  
---  
**Type** | **Description**  
`[UploadResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult.Builder)` | the Builder instance with the value for uploadedBlob modified.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
