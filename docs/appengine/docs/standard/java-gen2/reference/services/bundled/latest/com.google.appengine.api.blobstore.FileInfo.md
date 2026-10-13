---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.FileInfo
title: Class FileInfo (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:31.506816+00:00
---

# Class FileInfo (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.FileInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class FileInfo (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class FileInfo

`FileInfo` contains metadata about an uploaded file. This metadata is gathered by parsing the HTTP headers included in the file upload. See Also: [RFC 1867](http://tools.ietf.org/html/rfc1867) for the specification of HTTP file uploads.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FileInfo

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

### FileInfo(String contentType, Date creation, String filename, long size, String md5Hash, @Nullable String gsObjectName)
    
    
    public FileInfo(String contentType, Date creation, String filename, long size, String md5Hash, @Nullable String gsObjectName)

Creates a `FileInfo` by providing the associated metadata. This is done by the API on the developer's behalf.

**Parameters**  
---  
**Name** | **Description**  
`contentType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the MIME Content-Type provided in the HTTP header during upload of this Blob.  
`creation` | `[Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html)`  
the time and date the blob was uploaded.  
`filename` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the file included in the Content-Disposition HTTP header during upload of this Blob.  
`size` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the size in bytes of this Blob.  
`md5Hash` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the md5Hash of this Blob.  
`gsObjectName` | `[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)`  
the name of the file written to Google Cloud Storage or null if the file was not uploaded to Google Cloud Storage.  
  
## Methods 

### equals(@Nullable Object obj)
    
    
    public boolean equals(@Nullable Object obj)

**Parameter**  
---  
**Name** | **Description**  
`obj` | `[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### getContentType()
    
    
    public String getContentType()

Returns the MIME Content-Type provided in the HTTP header during upload of this Blob.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getCreation()
    
    
    public Date getCreation()

Returns the time and date the blob was upload.

**Returns**  
---  
**Type** | **Description**  
`[Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html)` |   
  
### getFilename()
    
    
    public String getFilename()

Returns the file included in the Content-Disposition HTTP header during upload of this Blob.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getGsObjectName()
    
    
    public @Nullable String getGsObjectName()

Returns the name of the file written to Google Cloud Storage or null if the file was not uploaded to Google Cloud Storage. This property is only available for BlobInfos returned by getUploadedBlobInfos(), as its value is not persisted in the Datastore. Any attempt to access this property on other BlobInfos will return null.

**Returns**  
---  
**Type** | **Description**  
`[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)` |   
  
### getMd5Hash()
    
    
    public String getMd5Hash()

Returns the md5Hash of this Blob.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getSize()
    
    
    public long getSize()

Returns the size in bytes of this Blob.

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

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
