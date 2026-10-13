---
url: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.LoggingOutputStream
title: Class LoggingOutputStream (2.2.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:19.108856+00:00
---

# Class LoggingOutputStream (2.2.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.LoggingOutputStream

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LoggingOutputStream (2.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.2.0 (latest)  2.1.1  2.0.3  1.47.1  1.46.3  1.45.3  1.44.2  1.43.2  1.42.3  1.41.8 
    
    
    public class LoggingOutputStream extends FilterOutputStream

Thread-safe output stream wrapper that forwards all writes to a given output stream, while logging all writes to a [LoggingByteArrayOutputStream](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.LoggingByteArrayOutputStream).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [OutputStream](https://docs.oracle.com/javase/8/docs/api/java/io/OutputStream.html) > [FilterOutputStream](https://docs.oracle.com/javase/8/docs/api/java/io/FilterOutputStream.html) > LoggingOutputStream

## Inherited Members

[FilterOutputStream.close()](https://docs.oracle.com/javase/8/docs/api/java/io/FilterOutputStream.html#close--)

[FilterOutputStream.flush()](https://docs.oracle.com/javase/8/docs/api/java/io/FilterOutputStream.html#flush--)

[FilterOutputStream.write(byte[])](https://docs.oracle.com/javase/8/docs/api/java/io/FilterOutputStream.html#write-byte\[\]-)

[FilterOutputStream.write(byte[],int,int)](https://docs.oracle.com/javase/8/docs/api/java/io/FilterOutputStream.html#write-byte\[\]-int-int-)

[FilterOutputStream.write(int)](https://docs.oracle.com/javase/8/docs/api/java/io/FilterOutputStream.html#write-int-)

[OutputStream.nullOutputStream()](https://docs.oracle.com/javase/8/docs/api/java/io/OutputStream.html#nullOutputStream--)

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

### LoggingOutputStream(OutputStream outputStream, Logger logger, Level loggingLevel, int contentLoggingLimit)
    
    
    public LoggingOutputStream(OutputStream outputStream, Logger logger, Level loggingLevel, int contentLoggingLimit)

**Parameters**  
---  
**Name** | **Description**  
`outputStream` | `[OutputStream](https://docs.oracle.com/javase/8/docs/api/java/io/OutputStream.html)`  
output stream to forward all writes to  
`logger` | `[Logger](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html)`  
logger  
`loggingLevel` | `[Level](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Level.html)`  
logging level  
`contentLoggingLimit` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
maximum number of bytes to log (may be `0` to avoid logging content)  
  
## Methods 

### close()
    
    
    public void close()

**Overrides**

[FilterOutputStream.close()](https://docs.oracle.com/javase/8/docs/api/java/io/FilterOutputStream.html#close--)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### getLogStream()
    
    
    public final LoggingByteArrayOutputStream getLogStream()

Returns the log stream.

**Returns**  
---  
**Type** | **Description**  
`[LoggingByteArrayOutputStream](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.LoggingByteArrayOutputStream)` |   
  
### write(byte[] b, int off, int len)
    
    
    public void write(byte[] b, int off, int len)

**Parameters**  
---  
**Name** | **Description**  
`b` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
  
`off` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`len` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Overrides**

[FilterOutputStream.write(byte[],int,int)](https://docs.oracle.com/javase/8/docs/api/java/io/FilterOutputStream.html#write-byte\[\]-int-int-)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### write(int b)
    
    
    public void write(int b)

**Parameter**  
---  
**Name** | **Description**  
`b` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Overrides**

[FilterOutputStream.write(int)](https://docs.oracle.com/javase/8/docs/api/java/io/FilterOutputStream.html#write-int-)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
