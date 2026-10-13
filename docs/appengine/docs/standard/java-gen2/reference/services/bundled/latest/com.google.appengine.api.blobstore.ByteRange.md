---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.ByteRange
title: Class ByteRange (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:31.167559+00:00
---

# Class ByteRange (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.ByteRange

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class ByteRange (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class ByteRange

A byte range as parsed from a request Range header. Format produced by this class is also compatible with the X-AppEngine-BlobRange header, used for serving sub-ranges of blobs.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ByteRange

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

### parse(String byteRange)
    
    
    public static ByteRange parse(String byteRange)

Parse byte range from header.

**Parameter**  
---  
**Name** | **Description**  
`byteRange` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Byte range string as received from header.  
**Returns**  
---  
**Type** | **Description**  
`[ByteRange](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.ByteRange)` | ByteRange object set to byte range as parsed from string.  
  
### parseContentRange(String contentRange)
    
    
    public static ByteRange parseContentRange(String contentRange)

Parse content range from header for byte-range only.

**Parameter**  
---  
**Name** | **Description**  
`contentRange` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Content range string as received from header.  
**Returns**  
---  
**Type** | **Description**  
`[ByteRange](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.ByteRange)` | ByteRange object set to byte range as parsed from string, but does not include the size information.  
  
## Constructors 

### ByteRange(long start)
    
    
    public ByteRange(long start)

Constructor.

**Parameter**  
---  
**Name** | **Description**  
`start` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Start index of blob range to serve. If negative, serve the last abs(start) bytes of the blob.  
  
### ByteRange(long start, @Nullable Long end)
    
    
    protected ByteRange(long start, @Nullable Long end)

**Parameters**  
---  
**Name** | **Description**  
`start` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`end` | `[Nullable Long](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Long.html)`  
  
  
### ByteRange(long start, long end)
    
    
    public ByteRange(long start, long end)

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`start` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Start index of blob range to serve. May not be negative.  
`end` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
End index of blob range to serve. Index is inclusive, meaning the byte indicated by end is included in the response.  
  
## Methods 

### equals(@Nullable Object object)
    
    
    public boolean equals(@Nullable Object object)

Two `ByteRange` objects are considered equal if they have the same start and end.

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

### getEnd()
    
    
    public long getEnd()

Get end index of byte range.

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | End index of byte range.  
  
### getStart()
    
    
    public long getStart()

Get start index of byte range.

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Start index of byte range.  
  
### hasEnd()
    
    
    public boolean hasEnd()

Indicates whether or not this byte range indicates an end.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | true if byte range has an end.  
  
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

Format byte range for use in header.

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
