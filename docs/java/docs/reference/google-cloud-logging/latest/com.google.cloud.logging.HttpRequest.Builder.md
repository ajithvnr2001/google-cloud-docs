---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder
title: Class HttpRequest.Builder (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:20:58.296250+00:00
---

# Class HttpRequest.Builder (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HttpRequest.Builder (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public static final class HttpRequest.Builder

A builder for `HttpRequest` objects.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > HttpRequest.Builder

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

### build()
    
    
    public HttpRequest build()

Creates a `HttpRequest` object for this builder.

**Returns**  
---  
**Type** | **Description**  
`[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest)` |   
  
### setCacheFillBytes(long cacheFillBytes)
    
    
    public HttpRequest.Builder setCacheFillBytes(long cacheFillBytes)

Sets the number of HTTP response bytes inserted into cache. Set only when a cache fill was attempted.

**Parameter**  
---  
**Name** | **Description**  
`cacheFillBytes` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder)` |   
  
### setCacheHit(boolean cacheHit)
    
    
    public HttpRequest.Builder setCacheHit(boolean cacheHit)

Sets whether or not an entity was served from cache (with or without validation). If not set, `false` is used.

**Parameter**  
---  
**Name** | **Description**  
`cacheHit` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder)` |   
  
### setCacheLookup(boolean cacheLookup)
    
    
    public HttpRequest.Builder setCacheLookup(boolean cacheLookup)

Sets whether or not a cache lookup was attempted. If not set, `false` is used.

**Parameter**  
---  
**Name** | **Description**  
`cacheLookup` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder)` |   
  
### setCacheValidatedWithOriginServer(boolean cacheValidatedWithOriginServer)
    
    
    public HttpRequest.Builder setCacheValidatedWithOriginServer(boolean cacheValidatedWithOriginServer)

Sets whether or not the response was validated with the origin server before being served from cache. This field is only meaningful if [#setCacheHit(boolean)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder#com_google_cloud_logging_HttpRequest_Builder_setCacheHit_boolean_) is set to ` true`. If not set, `false` is used.

**Parameter**  
---  
**Name** | **Description**  
`cacheValidatedWithOriginServer` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder)` |   
  
### setLatency(Duration latency)
    
    
    public HttpRequest.Builder setLatency(Duration latency)

**Obsolete**

_Use setLatencyDuration(java.time.Duration) instead_

This feature is stable for usage in this major version, but may be deprecated in a future release.

This method is obsolete. Use [#setLatencyDuration(java.time.Duration)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder#com_google_cloud_logging_HttpRequest_Builder_setLatencyDuration_java_time_Duration_) instead.

**Parameter**  
---  
**Name** | **Description**  
`latency` | `org.threeten.bp.Duration`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder)` |   
  
### setLatencyDuration(Duration latency)
    
    
    public HttpRequest.Builder setLatencyDuration(Duration latency)

Sets the latency on the server, from the time the request was received until the response was sent.

**Parameter**  
---  
**Name** | **Description**  
`latency` | `[Duration](https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder)` |   
  
### setReferer(String referer)
    
    
    public HttpRequest.Builder setReferer(String referer)

Sets the referer URL of the request, as defined in HTTP/1.1 Header Field Definitions. See Also: [HTTP/1.1 Header Field Definitions](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html)

**Parameter**  
---  
**Name** | **Description**  
`referer` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder)` |   
  
### setRemoteIp(String remoteIp)
    
    
    public HttpRequest.Builder setRemoteIp(String remoteIp)

Sets the IP address (IPv4 or IPv6) of the client that issued the HTTP request. Examples: `192.168.1.1`, `FE80::0202:B3FF:FE1E:8329`.

**Parameter**  
---  
**Name** | **Description**  
`remoteIp` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder)` |   
  
### setRequestMethod(HttpRequest.RequestMethod requestMethod)
    
    
    public HttpRequest.Builder setRequestMethod(HttpRequest.RequestMethod requestMethod)

Sets the HTTP request method.

**Parameter**  
---  
**Name** | **Description**  
`requestMethod` | `[HttpRequest.RequestMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.RequestMethod)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder)` |   
  
### setRequestSize(long requestSize)
    
    
    public HttpRequest.Builder setRequestSize(long requestSize)

Sets the size of the HTTP request message in bytes, including the request headers and the request body.

**Parameter**  
---  
**Name** | **Description**  
`requestSize` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder)` |   
  
### setRequestUrl(String requestUrl)
    
    
    public HttpRequest.Builder setRequestUrl(String requestUrl)

Sets the requested URL. Request URL contains the scheme (`http`, `https`), the host name, the path and the query portion of the URL that was requested. Example: ` <http://example.com/some/info?color=red>`.

**Parameter**  
---  
**Name** | **Description**  
`requestUrl` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder)` |   
  
### setResponseSize(long responseSize)
    
    
    public HttpRequest.Builder setResponseSize(long responseSize)

Sets the size of the HTTP response message sent back to the client, in bytes, including the response headers and the response body.

**Parameter**  
---  
**Name** | **Description**  
`responseSize` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder)` |   
  
### setServerIp(String serverIp)
    
    
    public HttpRequest.Builder setServerIp(String serverIp)

Sets the IP address (IPv4 or IPv6) of the origin server that the request was sent to. Examples: `192.168.1.1`, `FE80::0202:B3FF:FE1E:8329`.

**Parameter**  
---  
**Name** | **Description**  
`serverIp` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder)` |   
  
### setStatus(int status)
    
    
    public HttpRequest.Builder setStatus(int status)

Sets the response code indicating the status of response.

**Parameter**  
---  
**Name** | **Description**  
`status` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder)` |   
  
### setUserAgent(String userAgent)
    
    
    public HttpRequest.Builder setUserAgent(String userAgent)

Sets the user agent sent by the client. Example: `Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Q312461; .NET CLR 1.0.3705)`.

**Parameter**  
---  
**Name** | **Description**  
`userAgent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
