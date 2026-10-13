---
url: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractHttpContent
title: Class AbstractHttpContent (2.2.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:41:12.339811+00:00
---

# Class AbstractHttpContent (2.2.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractHttpContent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AbstractHttpContent (2.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.2.0 (latest)  2.1.1  2.0.3  1.47.1  1.46.3  1.45.3  1.44.2  1.43.2  1.42.3  1.41.8 
    
    
    public abstract class AbstractHttpContent implements HttpContent

Abstract implementation of an HTTP content with typical options.

Implementation is not thread-safe.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AbstractHttpContent

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

## Static Methods 

### computeLength(HttpContent content)
    
    
    public static long computeLength(HttpContent content)

Returns the computed content length based using [IOUtils#computeLength(StreamingContent)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.IOUtils#com_google_api_client_util_IOUtils_computeLength_com_google_api_client_util_StreamingContent_) or instead `-1` if [HttpContent#retrySupported()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpContent#com_google_api_client_http_HttpContent_retrySupported__) is `false` because the stream must not be read twice.

**Parameter**  
---  
**Name** | **Description**  
`content` | `[HttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpContent)`  
HTTP content  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | computed content length or `-1` if retry is not supported  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
## Constructors 

### AbstractHttpContent(HttpMediaType mediaType)
    
    
    protected AbstractHttpContent(HttpMediaType mediaType)

**Parameter**  
---  
**Name** | **Description**  
`mediaType` | `[HttpMediaType](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpMediaType)`  
Media type this content represents or `null` to leave out  
  
### AbstractHttpContent(String mediaType)
    
    
    protected AbstractHttpContent(String mediaType)

**Parameter**  
---  
**Name** | **Description**  
`mediaType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Media type string (for example "type/subtype") this content represents or `null` to leave out. Can also contain parameters like `"charset=utf-8"`  
  
## Methods 

### computeLength()
    
    
    protected long computeLength()

Computes and returns the content length or less than zero if not known.

Subclasses may override, but by default this computes the length by calling [#computeLength(HttpContent)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractHttpContent#com_google_api_client_http_AbstractHttpContent_computeLength_com_google_api_client_http_HttpContent_).

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### getCharset()
    
    
    protected final Charset getCharset()

Returns the charset specified in the media type or ISO_8859_1 if not specified.

**Returns**  
---  
**Type** | **Description**  
`[Charset](https://docs.oracle.com/javase/8/docs/api/java/nio/charset/Charset.html)` |   
  
### getLength()
    
    
    public long getLength()

Default implementation calls [#computeLength()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractHttpContent#com_google_api_client_http_AbstractHttpContent_computeLength__) once and caches it for future invocations, but subclasses may override.

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### getMediaType()
    
    
    public final HttpMediaType getMediaType()

Returns the media type to use for the Content-Type header, or `null` if unspecified.

**Returns**  
---  
**Type** | **Description**  
`[HttpMediaType](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpMediaType)` |   
  
### getType()
    
    
    public String getType()

Returns the content type or `null` for none.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### retrySupported()
    
    
    public boolean retrySupported()

Default implementation returns `true`, but subclasses may override.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### setMediaType(HttpMediaType mediaType)
    
    
    public AbstractHttpContent setMediaType(HttpMediaType mediaType)

Sets the media type to use for the Content-Type header, or `null` if unspecified.

This will also overwrite any previously set parameter of the media type (for example ` "charset"`), and therefore might change other properties as well.

**Parameter**  
---  
**Name** | **Description**  
`mediaType` | `[HttpMediaType](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpMediaType)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AbstractHttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractHttpContent)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
