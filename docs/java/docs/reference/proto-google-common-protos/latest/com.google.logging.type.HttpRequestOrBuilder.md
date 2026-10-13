---
url: https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.logging.type.HttpRequestOrBuilder
title: Interface HttpRequestOrBuilder (2.78.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:56.171168+00:00
---

# Interface HttpRequestOrBuilder (2.78.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.logging.type.HttpRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface HttpRequestOrBuilder (2.78.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.78.0 (latest)  2.74.0  2.73.0  2.72.0  2.70.0  2.67.0  2.66.0  2.65.1  2.64.1  2.63.2  2.62.0  2.61.3  2.60.0  2.59.2  2.58.0  2.57.0  2.56.0  2.54.1  2.53.0  2.52.0  2.51.0  2.50.1  2.49.0  2.48.0  2.46.0  2.45.1  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.1  2.38.0  2.37.1  2.36.0  2.34.0  2.33.0  2.32.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.1  2.22.1  2.21.1  2.15.0  2.14.3  2.13.0  2.12.0  2.11.0  2.10.0  2.9.6  2.8.4  2.7.4 
    
    
    public interface HttpRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCacheFillBytes()
    
    
    public abstract long getCacheFillBytes()

The number of HTTP response bytes inserted into cache. Set only when a cache fill was attempted.

`int64 cache_fill_bytes = 12;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The cacheFillBytes.  
  
### getCacheHit()
    
    
    public abstract boolean getCacheHit()

Whether or not an entity was served from cache (with or without validation).

`bool cache_hit = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The cacheHit.  
  
### getCacheLookup()
    
    
    public abstract boolean getCacheLookup()

Whether or not a cache lookup was attempted.

`bool cache_lookup = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The cacheLookup.  
  
### getCacheValidatedWithOriginServer()
    
    
    public abstract boolean getCacheValidatedWithOriginServer()

Whether or not the response was validated with the origin server before being served from cache. This field is only meaningful if `cache_hit` is True.

`bool cache_validated_with_origin_server = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The cacheValidatedWithOriginServer.  
  
### getLatency()
    
    
    public abstract Duration getLatency()

The request processing latency on the server, from the time the request was received until the response was sent.

`.google.protobuf.Duration latency = 14;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The latency.  
  
### getLatencyOrBuilder()
    
    
    public abstract DurationOrBuilder getLatencyOrBuilder()

The request processing latency on the server, from the time the request was received until the response was sent.

`.google.protobuf.Duration latency = 14;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getProtocol()
    
    
    public abstract String getProtocol()

Protocol used for the request. Examples: "HTTP/1.1", "HTTP/2", "websocket"

`string protocol = 15;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The protocol.  
  
### getProtocolBytes()
    
    
    public abstract ByteString getProtocolBytes()

Protocol used for the request. Examples: "HTTP/1.1", "HTTP/2", "websocket"

`string protocol = 15;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for protocol.  
  
### getReferer()
    
    
    public abstract String getReferer()

The referer URL of the request, as defined in [HTTP/1.1 Header Field Definitions](https://datatracker.ietf.org/doc/html/rfc2616#section-14.36).

`string referer = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The referer.  
  
### getRefererBytes()
    
    
    public abstract ByteString getRefererBytes()

The referer URL of the request, as defined in [HTTP/1.1 Header Field Definitions](https://datatracker.ietf.org/doc/html/rfc2616#section-14.36).

`string referer = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for referer.  
  
### getRemoteIp()
    
    
    public abstract String getRemoteIp()

The IP address (IPv4 or IPv6) of the client that issued the HTTP request. This field can include port information. Examples: `"192.168.1.1"`, `"10.0.0.1:80"`, `"FE80::0202:B3FF:FE1E:8329"`.

`string remote_ip = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The remoteIp.  
  
### getRemoteIpBytes()
    
    
    public abstract ByteString getRemoteIpBytes()

The IP address (IPv4 or IPv6) of the client that issued the HTTP request. This field can include port information. Examples: `"192.168.1.1"`, `"10.0.0.1:80"`, `"FE80::0202:B3FF:FE1E:8329"`.

`string remote_ip = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for remoteIp.  
  
### getRequestMethod()
    
    
    public abstract String getRequestMethod()

The request method. Examples: `"GET"`, `"HEAD"`, `"PUT"`, `"POST"`.

`string request_method = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The requestMethod.  
  
### getRequestMethodBytes()
    
    
    public abstract ByteString getRequestMethodBytes()

The request method. Examples: `"GET"`, `"HEAD"`, `"PUT"`, `"POST"`.

`string request_method = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for requestMethod.  
  
### getRequestSize()
    
    
    public abstract long getRequestSize()

The size of the HTTP request message in bytes, including the request headers and the request body.

`int64 request_size = 3;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The requestSize.  
  
### getRequestUrl()
    
    
    public abstract String getRequestUrl()

The scheme (http, https), the host name, the path and the query portion of the URL that was requested. Example: `"<http://example.com/some/info?color=red>"`.

`string request_url = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The requestUrl.  
  
### getRequestUrlBytes()
    
    
    public abstract ByteString getRequestUrlBytes()

The scheme (http, https), the host name, the path and the query portion of the URL that was requested. Example: `"<http://example.com/some/info?color=red>"`.

`string request_url = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for requestUrl.  
  
### getResponseSize()
    
    
    public abstract long getResponseSize()

The size of the HTTP response message sent back to the client, in bytes, including the response headers and the response body.

`int64 response_size = 5;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The responseSize.  
  
### getServerIp()
    
    
    public abstract String getServerIp()

The IP address (IPv4 or IPv6) of the origin server that the request was sent to. This field can include port information. Examples: `"192.168.1.1"`, `"10.0.0.1:80"`, `"FE80::0202:B3FF:FE1E:8329"`.

`string server_ip = 13;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serverIp.  
  
### getServerIpBytes()
    
    
    public abstract ByteString getServerIpBytes()

The IP address (IPv4 or IPv6) of the origin server that the request was sent to. This field can include port information. Examples: `"192.168.1.1"`, `"10.0.0.1:80"`, `"FE80::0202:B3FF:FE1E:8329"`.

`string server_ip = 13;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serverIp.  
  
### getStatus()
    
    
    public abstract int getStatus()

The response code indicating the status of response. Examples: 200, 404.

`int32 status = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The status.  
  
### getUserAgent()
    
    
    public abstract String getUserAgent()

The user agent sent by the client. Example: `"Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Q312461; .NET CLR 1.0.3705)"`.

`string user_agent = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The userAgent.  
  
### getUserAgentBytes()
    
    
    public abstract ByteString getUserAgentBytes()

The user agent sent by the client. Example: `"Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Q312461; .NET CLR 1.0.3705)"`.

`string user_agent = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for userAgent.  
  
### hasLatency()
    
    
    public abstract boolean hasLatency()

The request processing latency on the server, from the time the request was received until the response was sent.

`.google.protobuf.Duration latency = 14;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the latency field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
