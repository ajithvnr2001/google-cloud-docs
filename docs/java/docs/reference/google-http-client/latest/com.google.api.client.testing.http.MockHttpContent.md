---
url: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.testing.http.MockHttpContent
title: Class MockHttpContent (2.2.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:47.030244+00:00
---

# Class MockHttpContent (2.2.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.testing.http.MockHttpContent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MockHttpContent (2.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.2.0 (latest)  2.1.1  2.0.3  1.47.1  1.46.3  1.45.3  1.44.2  1.43.2  1.42.3  1.41.8 
    
    
    public class MockHttpContent implements HttpContent

[Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta)   
Mock for [HttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpContent).

Implementation is not thread-safe.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > MockHttpContent

## Implements

[HttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpContent)

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

### MockHttpContent()
    
    
    public MockHttpContent()

## Methods 

### getContent()
    
    
    public final byte[] getContent()

Returns the HTTP content.

**Returns**  
---  
**Type** | **Description**  
`[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]` |   
  
### getLength()
    
    
    public long getLength()

Returns the content length or less than zero if not known.

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### getType()
    
    
    public String getType()

Returns the content type or `null` for none.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### retrySupported()
    
    
    public boolean retrySupported()

Returns whether or not retry is supported on this content type.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### setContent(byte[] content)
    
    
    public MockHttpContent setContent(byte[] content)

Sets the HTTP content.

Default value is an empty byte array.

**Parameter**  
---  
**Name** | **Description**  
`content` | `[byte](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[MockHttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.testing.http.MockHttpContent)` |   
  
### setLength(long length)
    
    
    public MockHttpContent setLength(long length)

Returns the HTTP content length or `-1` for unknown.

Default value is `-1`.

**Parameter**  
---  
**Name** | **Description**  
`length` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MockHttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.testing.http.MockHttpContent)` |   
  
### setType(String type)
    
    
    public MockHttpContent setType(String type)

Sets the HTTP content type or `null` for none.

**Parameter**  
---  
**Name** | **Description**  
`type` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MockHttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.testing.http.MockHttpContent)` |   
  
### writeTo(OutputStream out)
    
    
    public void writeTo(OutputStream out)

Writes the byte content to the given output stream.

Implementations must not close the output stream, and instead should flush the output stream. Some callers may assume that the output stream has not been closed, and will fail to work if it has been closed.

**Parameter**  
---  
**Name** | **Description**  
`out` | `[OutputStream](https://docs.oracle.com/javase/8/docs/api/java/io/OutputStream.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
