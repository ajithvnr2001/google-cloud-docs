---
url: https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.context.AttributeContext.RequestOrBuilder
title: Interface AttributeContext.RequestOrBuilder (2.78.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:40.068405+00:00
---

# Interface AttributeContext.RequestOrBuilder (2.78.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.context.AttributeContext.RequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AttributeContext.RequestOrBuilder (2.78.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.78.0 (latest)  2.74.0  2.73.0  2.72.0  2.70.0  2.67.0  2.66.0  2.65.1  2.64.1  2.63.2  2.62.0  2.61.3  2.60.0  2.59.2  2.58.0  2.57.0  2.56.0  2.54.1  2.53.0  2.52.0  2.51.0  2.50.1  2.49.0  2.48.0  2.46.0  2.45.1  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.1  2.38.0  2.37.1  2.36.0  2.34.0  2.33.0  2.32.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.1  2.22.1  2.21.1  2.15.0  2.14.3  2.13.0  2.12.0  2.11.0  2.10.0  2.9.6  2.8.4  2.7.4 
    
    
    public static interface AttributeContext.RequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsHeaders(String key)
    
    
    public abstract boolean containsHeaders(String key)

The HTTP request headers. If multiple headers share the same key, they must be merged according to the HTTP spec. All header keys must be lowercased, because HTTP header keys are case-insensitive.

`map<string, string> headers = 3;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAuth()
    
    
    public abstract AttributeContext.Auth getAuth()

The request authentication. May be absent for unauthenticated requests. Derived from the HTTP request `Authorization` header or equivalent.

`.google.rpc.context.AttributeContext.Auth auth = 13;`

**Returns**  
---  
**Type** | **Description**  
`[AttributeContext.Auth](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.context.AttributeContext.Auth)` | The auth.  
  
### getAuthOrBuilder()
    
    
    public abstract AttributeContext.AuthOrBuilder getAuthOrBuilder()

The request authentication. May be absent for unauthenticated requests. Derived from the HTTP request `Authorization` header or equivalent.

`.google.rpc.context.AttributeContext.Auth auth = 13;`

**Returns**  
---  
**Type** | **Description**  
`[AttributeContext.AuthOrBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.context.AttributeContext.AuthOrBuilder)` |   
  
### getHeaders() (deprecated)
    
    
    public abstract Map<String,String> getHeaders()

Use [#getHeadersMap()](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.context.AttributeContext.RequestOrBuilder#com_google_rpc_context_AttributeContext_RequestOrBuilder_getHeadersMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getHeadersCount()
    
    
    public abstract int getHeadersCount()

The HTTP request headers. If multiple headers share the same key, they must be merged according to the HTTP spec. All header keys must be lowercased, because HTTP header keys are case-insensitive.

`map<string, string> headers = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getHeadersMap()
    
    
    public abstract Map<String,String> getHeadersMap()

The HTTP request headers. If multiple headers share the same key, they must be merged according to the HTTP spec. All header keys must be lowercased, because HTTP header keys are case-insensitive.

`map<string, string> headers = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getHeadersOrDefault(String key, String defaultValue)
    
    
    public abstract String getHeadersOrDefault(String key, String defaultValue)

The HTTP request headers. If multiple headers share the same key, they must be merged according to the HTTP spec. All header keys must be lowercased, because HTTP header keys are case-insensitive.

`map<string, string> headers = 3;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getHeadersOrThrow(String key)
    
    
    public abstract String getHeadersOrThrow(String key)

The HTTP request headers. If multiple headers share the same key, they must be merged according to the HTTP spec. All header keys must be lowercased, because HTTP header keys are case-insensitive.

`map<string, string> headers = 3;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getHost()
    
    
    public abstract String getHost()

The HTTP request `Host` header value.

`string host = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The host.  
  
### getHostBytes()
    
    
    public abstract ByteString getHostBytes()

The HTTP request `Host` header value.

`string host = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for host.  
  
### getId()
    
    
    public abstract String getId()

The unique ID for a request, which can be propagated to downstream systems. The ID should have low probability of collision within a single day for a specific service.

`string id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The id.  
  
### getIdBytes()
    
    
    public abstract ByteString getIdBytes()

The unique ID for a request, which can be propagated to downstream systems. The ID should have low probability of collision within a single day for a specific service.

`string id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for id.  
  
### getMethod()
    
    
    public abstract String getMethod()

The HTTP request method, such as `GET`, `POST`.

`string method = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The method.  
  
### getMethodBytes()
    
    
    public abstract ByteString getMethodBytes()

The HTTP request method, such as `GET`, `POST`.

`string method = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for method.  
  
### getOrigin()
    
    
    public abstract String getOrigin()

The values from Origin header from the HTTP request, such as "<https://console.cloud.google.com>". Modern browsers can only have one origin. Special browsers and/or HTTP clients may require multiple origins.

`string origin = 14;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The origin.  
  
### getOriginBytes()
    
    
    public abstract ByteString getOriginBytes()

The values from Origin header from the HTTP request, such as "<https://console.cloud.google.com>". Modern browsers can only have one origin. Special browsers and/or HTTP clients may require multiple origins.

`string origin = 14;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for origin.  
  
### getPath()
    
    
    public abstract String getPath()

The HTTP URL path, excluding the query parameters.

`string path = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The path.  
  
### getPathBytes()
    
    
    public abstract ByteString getPathBytes()

The HTTP URL path, excluding the query parameters.

`string path = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for path.  
  
### getProtocol()
    
    
    public abstract String getProtocol()

The network protocol used with the request, such as "http/1.1", "spdy/3", "h2", "h2c", "webrtc", "tcp", "udp", "quic". See <https://www.iana.org/assignments/tls-extensiontype-values/tls-extensiontype-values.xhtml#alpn-protocol-ids> for details.

`string protocol = 11;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The protocol.  
  
### getProtocolBytes()
    
    
    public abstract ByteString getProtocolBytes()

The network protocol used with the request, such as "http/1.1", "spdy/3", "h2", "h2c", "webrtc", "tcp", "udp", "quic". See <https://www.iana.org/assignments/tls-extensiontype-values/tls-extensiontype-values.xhtml#alpn-protocol-ids> for details.

`string protocol = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for protocol.  
  
### getQuery()
    
    
    public abstract String getQuery()

The HTTP URL query in the format of `name1=value1&name2=value2`, as it appears in the first line of the HTTP request. No decoding is performed.

`string query = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The query.  
  
### getQueryBytes()
    
    
    public abstract ByteString getQueryBytes()

The HTTP URL query in the format of `name1=value1&name2=value2`, as it appears in the first line of the HTTP request. No decoding is performed.

`string query = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for query.  
  
### getReason()
    
    
    public abstract String getReason()

A special parameter for request reason. It is used by security systems to associate auditing information with a request.

`string reason = 12;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The reason.  
  
### getReasonBytes()
    
    
    public abstract ByteString getReasonBytes()

A special parameter for request reason. It is used by security systems to associate auditing information with a request.

`string reason = 12;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for reason.  
  
### getScheme()
    
    
    public abstract String getScheme()

The HTTP URL scheme, such as `http` and `https`.

`string scheme = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The scheme.  
  
### getSchemeBytes()
    
    
    public abstract ByteString getSchemeBytes()

The HTTP URL scheme, such as `http` and `https`.

`string scheme = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for scheme.  
  
### getSize()
    
    
    public abstract long getSize()

The HTTP request size in bytes. If unknown, it must be -1.

`int64 size = 10;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The size.  
  
### getTime()
    
    
    public abstract Timestamp getTime()

The timestamp when the `destination` service receives the last byte of the request.

`.google.protobuf.Timestamp time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The time.  
  
### getTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getTimeOrBuilder()

The timestamp when the `destination` service receives the last byte of the request.

`.google.protobuf.Timestamp time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasAuth()
    
    
    public abstract boolean hasAuth()

The request authentication. May be absent for unauthenticated requests. Derived from the HTTP request `Authorization` header or equivalent.

`.google.rpc.context.AttributeContext.Auth auth = 13;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the auth field is set.  
  
### hasTime()
    
    
    public abstract boolean hasTime()

The timestamp when the `destination` service receives the last byte of the request.

`.google.protobuf.Timestamp time = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the time field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
