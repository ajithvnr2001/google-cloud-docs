---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.UploadOptions
title: Class UploadOptions (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:31.778985+00:00
---

# Class UploadOptions (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.UploadOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class UploadOptions (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class UploadOptions

Allows users to customize the behavior of a single upload to the [BlobstoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.jakarta.BlobstoreService).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > UploadOptions

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

### equals(@Nullable Object object)
    
    
    public boolean equals(@Nullable Object object)

**Parameter**  
---  
**Name** | **Description**  
`object` | `[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### getGoogleStorageBucketName()
    
    
    public String getGoogleStorageBucketName()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the storage bucket name.  
  
### getMaxUploadSizeBytes()
    
    
    public long getMaxUploadSizeBytes()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the maximum upload size.  
  
### getMaxUploadSizeBytesPerBlob()
    
    
    public long getMaxUploadSizeBytesPerBlob()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the maximum upload size per blob.  
  
### googleStorageBucketName(String bucketName)
    
    
    public UploadOptions googleStorageBucketName(String bucketName)

**Parameter**  
---  
**Name** | **Description**  
`bucketName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UploadOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.UploadOptions)` |   
  
### hasGoogleStorageBucketName()
    
    
    public boolean hasGoogleStorageBucketName()

Determines if the storage bucket is set.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasMaxUploadSizeBytes()
    
    
    public boolean hasMaxUploadSizeBytes()

Determines if the maximum size is set.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasMaxUploadSizeBytesPerBlob()
    
    
    public boolean hasMaxUploadSizeBytesPerBlob()

Determines if the maximum upload size per blob is set.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### maxUploadSizeBytes(long maxUploadSizeBytes)
    
    
    public UploadOptions maxUploadSizeBytes(long maxUploadSizeBytes)

Sets the maximum size in bytes that for the total upload. If the upload exceeds this value then a 413 error will be returned to the client.

**Parameter**  
---  
**Name** | **Description**  
`maxUploadSizeBytes` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The maximum size in bytes for the upload.  
**Returns**  
---  
**Type** | **Description**  
`[UploadOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.UploadOptions)` | `this` (for chaining)  
  
### maxUploadSizeBytesPerBlob(long maxUploadSizeBytesPerBlob)
    
    
    public UploadOptions maxUploadSizeBytesPerBlob(long maxUploadSizeBytesPerBlob)

Sets the maximum size in bytes for any one blob in the upload. If any blob in the upload exceeds this value then a 413 error will be returned to the client.

**Parameter**  
---  
**Name** | **Description**  
`maxUploadSizeBytesPerBlob` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The maximum size in bytes that any one blob in the upload can be.  
**Returns**  
---  
**Type** | **Description**  
`[UploadOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.UploadOptions)` | `this` (for chaining)  
  
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

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
