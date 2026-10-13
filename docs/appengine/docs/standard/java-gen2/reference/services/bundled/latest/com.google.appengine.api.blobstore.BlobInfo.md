---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobInfo
title: Class BlobInfo (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:19.476403+00:00
---

# Class BlobInfo (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class BlobInfo (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class BlobInfo implements Serializable

`BlobInfo` contains metadata about a blob. This metadata is gathered by parsing the HTTP headers included in the blob upload. See Also: [RFC 1867](http://tools.ietf.org/html/rfc1867) for the specification of HTTP file uploads.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BlobInfo

## Implements

[Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)

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

### BlobInfo(BlobKey blobKey, String contentType, Date creation, String filename, long size)
    
    
    public BlobInfo(BlobKey blobKey, String contentType, Date creation, String filename, long size)

**Parameters**  
---  
**Name** | **Description**  
`blobKey` | `[BlobKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobKey)`  
  
`contentType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`creation` | `[Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html)`  
  
`filename` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`size` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### BlobInfo(BlobKey blobKey, String contentType, Date creation, String filename, long size, String md5Hash)
    
    
    public BlobInfo(BlobKey blobKey, String contentType, Date creation, String filename, long size, String md5Hash)

**Parameters**  
---  
**Name** | **Description**  
`blobKey` | `[BlobKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobKey)`  
  
`contentType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`creation` | `[Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html)`  
  
`filename` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`size` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`md5Hash` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### BlobInfo(BlobKey blobKey, String contentType, Date creation, String filename, long size, String md5Hash, @Nullable String gsObjectName)
    
    
    public BlobInfo(BlobKey blobKey, String contentType, Date creation, String filename, long size, String md5Hash, @Nullable String gsObjectName)

Creates a `BlobInfo` by providing the [BlobKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobKey) and all associated metadata. This is typically done by the API on the developer's behalf.

**Parameters**  
---  
**Name** | **Description**  
`blobKey` | `[BlobKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobKey)`  
the [BlobKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobKey) of the Blob.  
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
the object name of this Blob, if it is stored on Google Cloud Storage, null otherwise.  
  
## Fields 

### blobKey
    
    
    protected final BlobKey blobKey

**Field Value**  
---  
**Type** | **Description**  
`[BlobKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobKey)` |   
  
### contentType
    
    
    protected final String contentType

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### creation
    
    
    protected final Date creation

**Field Value**  
---  
**Type** | **Description**  
`[Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html)` |   
  
### filename
    
    
    protected final String filename

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### gsObjectName
    
    
    protected final @Nullable String gsObjectName

**Field Value**  
---  
**Type** | **Description**  
`[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)` |   
  
### md5Hash
    
    
    protected String md5Hash

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### size
    
    
    protected final long size

**Field Value**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
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

### getBlobKey()
    
    
    public BlobKey getBlobKey()

Returns the [BlobKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobKey) of the Blob this `BlobInfo` describes.

**Returns**  
---  
**Type** | **Description**  
`[BlobKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobKey)` |   
  
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

Returns the object name of this Blob, if it is stored in Google Cloud Storage, in the form `/[bucket-name]/[object-name]`. Returns `null` if the Blob is stored in Blobstorage.

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
