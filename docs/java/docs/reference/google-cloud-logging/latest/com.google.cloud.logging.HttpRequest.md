---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest
title: Class HttpRequest (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:20:57.839917+00:00
---

# Class HttpRequest (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HttpRequest (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public final class HttpRequest implements Serializable

Objects of this class represent information about the (optional) HTTP request associated with a log entry. See Also: [ Http Request](https://cloud.google.com/logging/docs/api/ref_v2beta1/rest/v2beta1/LogEntry#httprequest)

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > HttpRequest

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

## Static Fields 

### EMPTY
    
    
    public static final HttpRequest EMPTY

**Field Value**  
---  
**Type** | **Description**  
`[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest)` |   
  
## Static Methods 

### newBuilder()
    
    
    public static HttpRequest.Builder newBuilder()

Returns a builder for `HttpRequest` objects.

**Returns**  
---  
**Type** | **Description**  
`[HttpRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder)` |   
  
## Methods 

### cacheHit()
    
    
    public boolean cacheHit()

Returns whether or not an entity was served from cache (with or without validation). If not set, this method returns `false`.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### cacheLookup()
    
    
    public boolean cacheLookup()

Returns whether or not a cache lookup was attempted. If not set, this method returns ` false`.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### cacheValidatedWithOriginServer()
    
    
    public boolean cacheValidatedWithOriginServer()

Returns whether or not the response was validated with the origin server before being served from cache. If not set, this method returns `false`. This field is only meaningful if [#cacheHit()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest#com_google_cloud_logging_HttpRequest_cacheHit__) is set to `true`.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### equals(Object obj)
    
    
    public boolean equals(Object obj)

**Parameter**  
---  
**Name** | **Description**  
`obj` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### getCacheFillBytes()
    
    
    public Long getCacheFillBytes()

Returns the number of HTTP response bytes inserted into cache. Set only when a cache fill was attempted.

**Returns**  
---  
**Type** | **Description**  
`[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)` |   
  
### getLatency()
    
    
    public Duration getLatency()

**Obsolete**

_Use getLatencyDuration() instead_

This feature is stable for usage in this major version, but may be deprecated in a future release.

This method is obsolete. Use [#getLatencyDuration()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest#com_google_cloud_logging_HttpRequest_getLatencyDuration__) instead.

**Returns**  
---  
**Type** | **Description**  
`org.threeten.bp.Duration` |   
  
### getLatencyDuration()
    
    
    public Duration getLatencyDuration()

Returns the processing latency on the server, from the time the request was received until the response was sent.

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html)` | the latency, for null if not populated.  
  
### getReferer()
    
    
    public String getReferer()

Returns the referer URL of the request, as defined in HTTP/1.1 Header Field Definitions. See Also: [HTTP/1.1 Header Field Definitions](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html)

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getRemoteIp()
    
    
    public String getRemoteIp()

Returns the IP address (IPv4 or IPv6) of the client that issued the HTTP request. Examples: `192.168.1.1`, `FE80::0202:B3FF:FE1E:8329`.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getRequestMethod()
    
    
    public HttpRequest.RequestMethod getRequestMethod()

Returns the HTTP request method.

**Returns**  
---  
**Type** | **Description**  
`[HttpRequest.RequestMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.RequestMethod)` |   
  
### getRequestSize()
    
    
    public Long getRequestSize()

Returns the size of the HTTP request message in bytes, including the request headers and the request body.

**Returns**  
---  
**Type** | **Description**  
`[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)` |   
  
### getRequestUrl()
    
    
    public String getRequestUrl()

Returns the requested URL. Request URL contains the scheme (`http`, `https`), the host name, the path and the query portion of the URL that was requested. Example: ` <http://example.com/some/info?color=red>`.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getResponseSize()
    
    
    public Long getResponseSize()

Returns the size of the HTTP response message sent back to the client, in bytes, including the response headers and the response body.

**Returns**  
---  
**Type** | **Description**  
`[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)` |   
  
### getServerIp()
    
    
    public String getServerIp()

Returns the IP address (IPv4 or IPv6) of the origin server that the request was sent to. Examples: `192.168.1.1`, `FE80::0202:B3FF:FE1E:8329`.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getStatus()
    
    
    public Integer getStatus()

Returns the response code indicating the status of response.

**Returns**  
---  
**Type** | **Description**  
`[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)` |   
  
### getUserAgent()
    
    
    public String getUserAgent()

Returns the user agent sent by the client. Example: `Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Q312461; .NET CLR 1.0.3705)`.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### toBuilder()
    
    
    public HttpRequest.Builder toBuilder()

Returns a builder for this object.

**Returns**  
---  
**Type** | **Description**  
`[HttpRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder)` |   
  
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

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
