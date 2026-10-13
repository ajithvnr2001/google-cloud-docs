---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobstoreInputStream
title: Class BlobstoreInputStream (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:20.219444+00:00
---

# Class BlobstoreInputStream (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobstoreInputStream

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class BlobstoreInputStream (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class BlobstoreInputStream extends InputStream

BlobstoreInputStream provides an InputStream view of a blob in Blobstore.

It is thread compatible but not thread safe: there is no static state, but any multithreaded use must be externally synchronized.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html) > BlobstoreInputStream

## Inherited Members

[InputStream.available()](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#available--)

[InputStream.close()](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#close--)

[InputStream.mark(int)](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#mark-int-)

[InputStream.markSupported()](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#markSupported--)

[InputStream.nullInputStream()](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#nullInputStream--)

[InputStream.read()](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#read--)

[InputStream.read(byte[])](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#read-byte\[\]-)

[InputStream.read(byte[],int,int)](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#read-byte\[\]-int-int-)

[InputStream.readAllBytes()](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#readAllBytes--)

[InputStream.readNBytes(byte[],int,int)](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#readNBytes-byte\[\]-int-int-)

[InputStream.readNBytes(int)](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#readNBytes-int-)

[InputStream.reset()](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#reset--)

[InputStream.skip(long)](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#skip-long-)

[InputStream.skipNBytes(long)](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#skipNBytes-long-)

[InputStream.transferTo(OutputStream)](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#transferTo-java.io.OutputStream-)

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

### BlobstoreInputStream(BlobKey blobKey)
    
    
    public BlobstoreInputStream(BlobKey blobKey)

Creates a BlobstoreInputStream that reads data from the blob indicated by blobKey, starting at the beginning of the blob.

**Parameter**  
---  
**Name** | **Description**  
`blobKey` | `[BlobKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobKey)`  
A valid BlobKey indicating the blob to read from.  
  
### BlobstoreInputStream(BlobKey blobKey, long offset)
    
    
    public BlobstoreInputStream(BlobKey blobKey, long offset)

Creates a BlobstoreInputStream that reads data from the blob indicated by blobKey, starting at offset.

**Parameters**  
---  
**Name** | **Description**  
`blobKey` | `[BlobKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobKey)`  
A valid BlobKey indicating the blob to read from.  
`offset` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
An offset to start from.  
  
## Methods 

### close()
    
    
    public void close()

**Overrides**

[InputStream.close()](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#close--)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | 

  * does not actually throw but as it's part of our public API and removing it can cause compilation errors, leaving it in (and documenting to quiet Eclipse warning).

  
  
### mark(int readlimit)
    
    
    public void mark(int readlimit)

**Parameter**  
---  
**Name** | **Description**  
`readlimit` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Overrides**

[InputStream.mark(int)](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#mark-int-)

### markSupported()
    
    
    public boolean markSupported()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[InputStream.markSupported()](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#markSupported--)

### read()
    
    
    public int read()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[InputStream.read()](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#read--)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### read(byte[] b, int off, int len)
    
    
    public int read(byte[] b, int off, int len)

**Parameters**  
---  
**Name** | **Description**  
`b` | `byte[]`  
  
`off` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`len` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[InputStream.read(byte[],int,int)](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#read-byte\[\]-int-int-)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### reset()
    
    
    public void reset()

**Overrides**

[InputStream.reset()](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html#reset--)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
