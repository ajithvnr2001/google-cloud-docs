---
url: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.UnsafeByteOperations
title: Class UnsafeByteOperations (3.19.4) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:31.426557+00:00
---

# Class UnsafeByteOperations (3.19.4)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.UnsafeByteOperations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class UnsafeByteOperations (3.19.4) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class UnsafeByteOperations

Provides a number of unsafe byte operations to be used by advanced applications with high performance requirements. These methods are referred to as "unsafe" due to the fact that they potentially expose the backing buffer of a [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString) to the application.

**DISCLAIMER:** The methods in this class should only be called if it is guaranteed that the buffer backing the [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString) will never change! Mutation of a [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString) can lead to unexpected and undesirable consequences in your application, and will likely be difficult to debug. Proceed with caution!

This can have a number of significant side affects that have spooky-action-at-a-distance-like behavior. In particular, if the bytes value changes out from under a Protocol Buffer:

  * serialization may throw 
  * serialization may succeed but the wrong bytes may be written out 
  * messages are no longer threadsafe 
  * hashCode may be incorrect 
    * can result in a permanent memory leak when used as a key in a long-lived HashMap 
    * the semantics of many programs may be violated if this is the case 



Each of these issues will occur in parts of the code base that are entirely distinct from the parts of the code base modifying the buffer. In fact, both parts of the code base may be correct

  * it is the bridging with the unsafe operations that was in error!



## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > UnsafeByteOperations

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

### unsafeWrap(byte[] buffer)
    
    
    public static ByteString unsafeWrap(byte[] buffer)

An unsafe operation that returns a [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString) that is backed by the provided buffer.

**Parameter**  
---  
**Name** | **Description**  
`buffer` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
the buffer to be wrapped  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString)` | a [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString) backed by the provided buffer  
  
### unsafeWrap(byte[] buffer, int offset, int length)
    
    
    public static ByteString unsafeWrap(byte[] buffer, int offset, int length)

An unsafe operation that returns a [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString) that is backed by a subregion of the provided buffer.

**Parameters**  
---  
**Name** | **Description**  
`buffer` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
the buffer to be wrapped  
`offset` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the offset of the wrapped region  
`length` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the number of bytes of the wrapped region  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString)` | a [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString) backed by the provided buffer  
  
### unsafeWrap(ByteBuffer buffer)
    
    
    public static ByteString unsafeWrap(ByteBuffer buffer)

An unsafe operation that returns a [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString) that is backed by the provided buffer.

**Parameter**  
---  
**Name** | **Description**  
`buffer` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
the Java NIO buffer to be wrapped  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString)` | a [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString) backed by the provided buffer  
  
### unsafeWriteTo(ByteString bytes, ByteOutput output)
    
    
    public static void unsafeWriteTo(ByteString bytes, ByteOutput output)

Writes the given [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString) to the provided [ByteOutput](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput). Calling this method may result in multiple operations on the target [ByteOutput](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput) (i.e. for roped [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString)s).

This method exposes the internal backing buffer(s) of the [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString) to the [ByteOutput](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput) in order to avoid additional copying overhead. It would be possible for a malicious [ByteOutput](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput) to corrupt the [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString). Use with caution!

NOTE: The [ByteOutput](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput) **MUST NOT** modify the provided buffers. Doing so may result in corrupted data, which would be difficult to debug.

**Parameters**  
---  
**Name** | **Description**  
`bytes` | `[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString)`  
the [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString) to be written  
`output` | `[ByteOutput](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteOutput)`  
the output to receive the bytes  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | if an I/O error occurs  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
