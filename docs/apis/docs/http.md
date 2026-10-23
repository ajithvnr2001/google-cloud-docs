---
url: https://docs.cloud.google.com/apis/docs/http/
title: HTTP guidelines \u00a0|\u00a0 Cloud APIs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:00.273274+00:00
---

# HTTP guidelines  |  Cloud APIs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apis/docs/http/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)



Send feedback 

#  HTTP guidelines Stay organized with collections  Save and categorize content based on your preferences. 

Understanding how Google APIs work with various HTTP versions and implementations is important if you are writing custom code that accesses an API's REST interface using a third-party HTTP client. For most workloads, use Google's recommended [client libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained) instead, which automatically handle the low-level server communication discussed in this document.

## Working with wire protocols (HTTP/*)

This section describes the supported wire protocols (typically a version of HTTP) that Google APIs can use to communicate between clients and servers, and how we recommend that you use them.

### HTTP semantics

When developing API client code, follow standard [HTTP protocol semantics](https://tools.ietf.org/html/rfc7231). Server-side proxies or API stacks might only support a subset of standard HTTP features, and might also support their backward-compatible versions.

HTTP protocol semantics that need to be handled by the server-side implementations of APIs are controlled by the server stack. Only rely on such semantics if these features are explicitly documented as part of the API spec, such as caching support.

### HTTP versions

Clients can use any HTTP/* protocols, as allowed by the client platform or their client-side network, or as negotiated with the server-side proxy. Supported protocols include HTTP/1.1, HTTP/2, and HTTP/3 (QUIC). Legacy support for HTTP/1.0 is highly discouraged.

Some API features might only be supported by newer versions of HTTP protocols; some are only fully specified with HTTP/2 and HTTP/3, such as full-duplex multiplexed streaming. Be aware of the limitations of different HTTP versions if you require any of these features as part of the API spec. Note that older features like HTTP/2 Server Push are deprecated and unsupported by modern web clients.

Generally, we recommend HTTP/3 or HTTP/2 for better performance, reduced head-of-line blocking, and greater resilience to network failures.

### Channels

Channels refer to the Layer 4 network connections, which are typically TCP sockets for HTTP/1.1 and HTTP/2, and UDP sockets for HTTP/3 (QUIC). Client applications shouldn't make assumptions about how channels are managed end-to-end, as connections are almost always terminated by Google Front End (GFE) proxies on behalf of the server process.

HTTP/1.1 clients: If using HTTP/1.1, always reuse TCP connections (Connection: Keep-Alive). HTTP client libraries typically manage a connection pool to facilitate reuse. Avoid HTTP pipelining on HTTP/1.1 connections; it is poorly supported and can lead to issues. For more information, see [HTTP and TCP](https://github.com/httpwg/wiki/wiki/TCP).

HTTP/2 and HTTP/3 clients: Modern clients and browsers predominantly use HTTP/2 or HTTP/3. Both protocols support multiplexing, allowing multiple requests and responses to be in flight concurrently over a single connection.

  * HTTP/2—uses a single TCP connection per origin.
  * HTTP/3—uses a single QUIC connection over UDP per origin. QUIC integrates TLS encryption, congestion control, and connection management, often providing benefits like faster connection setup (0-RTT or 1-RTT) and immunity to TCP head-of-line blocking across streams.



With HTTP/2 and HTTP/3, browser limits on the number of parallel TCP connections to a single host (for example, 2-10) are no longer a primary performance concern. However, be aware that servers (or proxies like GFE) can still enforce limits on the maximum number of concurrent streams within a single HTTP/2 or HTTP/3 connection. This prevents overload and ensures fair resource usage (for example, by limiting concurrent requests or streams per connection to 100).

### HTTPS

Clients can access an API using HTTPS or HTTP, as supported by the API spec. TLS negotiation and TLS versions are transparent to client applications. By default, Google APIs only accept HTTPS traffic.

## Request and response formats

This section describes the structure of API interactions, including the use of URL-encoded data, specific HTTP methods for RESTful actions, and JSON-based payload formats.

### Request URLs

JSON-REST mapping supports URL encoded request data, and the HTTP request and response body use `application/json` as the `Content-Type`.

The HTTP body uses a JSON array to support streamed RPC methods, and the JSON array might contain any number of JSON messages or an error-status JSON message.

### Long request URLs

The URL has a practical length limitation, typically set to 16KB by default, though this might vary depending on the server. If your API uses GET requests with URLs that exceed this length, the requests might not reach the destination API server and will be rejected by the Google Front End (GFE) with the error message `Your client has issued a malformed or illegal request.`

To bypass the limitation, the client code should use a POST request with a Content-Type of `application/x-www-form-urlencoded` along with the HTTP header `X-HTTP-Method-Override: GET`. This approach also works for DELETE requests.

### HTTP methods (verbs)

If the request URLs follow the REST model, their HTTP methods are specified as part of the API specification. In particular, every API method **must** comply with the requirements of the HTTP protocol based on the specific HTTP verb to which the API method maps. For more information, see the [Hypertext Transfer Protocol](http://tools.ietf.org/html/rfc2616#section-9) specification and the [PATCH Method](http://tools.ietf.org/html/rfc5789) RFC.

[Safe Methods](http://tools.ietf.org/html/rfc2616#section-9.1.1), such as HTTP `GET` and `HEAD`, shouldn't represent an action other than retrieval. Specifically, HTTP `GET` ought to be considered _safe_ and should not have any client-visible side-effects.

[Idempotence](http://tools.ietf.org/html/rfc2616#section-9.1.2) in HTTP means that the side-effects of multiple identical requests are the same as for a single request. `GET`, `PUT`, and `DELETE` are the idempotent HTTP methods relevant to the style guide. Note that idempotence is only expressed in terms of server side-effects and does not specify anything about the response. In particular, `DELETE` for non-existing resources **should** return `404 (Not Found)`.

HTTP `POST` and `PATCH` are neither safe nor idempotent. (`PATCH` was introduced in [RFC 5789](http://tools.ietf.org/html/rfc5789))

HTTP Verb | Safe | Idempotent  
---|---|---  
[`GET`](http://tools.ietf.org/html/rfc2616#section-9.3) | Yes | Yes  
[`PUT`](http://tools.ietf.org/html/rfc2616#section-9.6) |  | Yes  
[`DELETE`](http://tools.ietf.org/html/rfc2616#section-9.7) |  | Yes  
[`POST`](http://tools.ietf.org/html/rfc2616#section-9.5) |  |   
[`PATCH`](http://tools.ietf.org/html/rfc5789) |  |   
  
### Payload formats

  * Request and response should share the same Content-Type, except when the request is a `GET` or a `POST` with an "`application/x-www-form-urlencoded`" body.

  * JSON is supported under the `application/json` MIME type. The mapping from proto3 to JSON is formally specified in [JSON Mapping](https://developers.google.com/protocol-buffers/docs/proto3#json).

  * Form parameters (`POST`) can be used in place of URL query parameters (`GET`), following the same REST-style mapping rule for mapping request fields to query parameters. The supported `Content-Type` is `application/x-www-form-urlencoded`.




## Streaming

This section details how Google APIs handle client and server streaming, specifically addressing the constraints of half-duplex versus full-duplex communication and the encoding requirements for streamed JSON messages.

### Half-duplex versus full-duplex

HTTP is a request-response protocol that allows its request or response body to be delivered over different stream-oriented transports such as TCP (HTTP/1.x) or its multiplexed variants (SPDY, HTTP/2, QUIC).

As a client developer, your application can produce the request body in a streaming mode, that is, client-streaming. Likewise, the application can also consume the response body in a streaming mode, that is, server-streaming.

However, the HTTP spec doesn't specify if a server is allowed to stream back the response body (except for error responses) when the request body is still pending. This semantic is known as _full-duplex streaming_. Although many HTTP client/server/proxy software programs do allow full-duplex streaming, even for HTTP/1.1, to avoid any interoperability issue, HTTP-based cloud APIs are restricted to half-duplex streaming only.

By default, bidi streaming methods in Cloud APIs assume the full-duplex semantics. That is, it is not safe to use HTTP to invoke such a method. If a streaming method is half-duplex only (as enforced by the server), the API document should clearly specify the half-duplex behavior.

For browser clients, the standard HTTP semantics are further constrained by the browser Network APIs. Browsers support server-streaming (that generally respects transport-level framing) using XHR or Fetch. The Fetch API makes use of [whatwg streams](https://github.com/whatwg/streams).

Because of browser restrictions, Cloud APIs that require browser support must avoid client-streaming as well as full-duplex streaming, or provide a separate API specifically for browser clients.

Generally speaking, client-streaming over the internet is less useful than server-streaming. This is because using client-streaming often leads to a stateful service, which adversely affects load-balancing and makes the system more vulnerable to failures or attacks. Server-streaming, on the other hand, can be useful as it can significantly reduce latency over networks with long RTT delays.

### Message encoding

JSON messages when streaming are encoded as an array of JSON messages. The request or response body will remain as a valid JSON MIME type.

Example client stream encoding:
    
    
    1 <length> <message-bytes> 1 <length> <message-bytes>  … EOF
    

Example server stream encoding:
    
    
    1 <length> <message-bytes>  … 2 <length> <status-bytes> EOF
    

Wire-level encoding: the definition of StreamBody is only significant in its allocation of tag-ids for the fields "messages" and "status" `<length>` which will be varint encoded with 1-2 bytes for normal messages, so the total encoding overhead is 2-3 bytes per message.

An optional padding field is needed to support base64 encoded streams:
    
    
    message StreamBody {
      repeated bytes message = 1;
      google.rpc.Status status = 2;
      repeated bytes padding = 15;   // max one-byte tag-id: xxx01111
    }
    

Error messages should be appended as the last element of the JSON or protobuf array, under the same format as regular messages.

## State management

Half-close behavior is well defined in any HTTP version for a client or server to signal to the other end that the body is completed.

In particular, client code is free to complete the request when still waiting for the response. Similarly, a client might see a completed response when the request body is still being written to the server. The HTTP standard expects the client to abort or complete the request when a response is completed in an unexpected way, normally with an error status. This is to say, under normal conditions the server shouldn't complete a response when the client is still sending the request.

### Cancellation

Cancellation support allows a client to abort a request when the request or response is still pending.

There is no reliable cancellation support for HTTP/1.* clients, as a client is free to close a TCP connection after the request has been completed without aborting the request or response transaction. A TCP FIN, under HTTP/1.1, shouldn't be interpreted as a cancellation, even when the connection is marked as a keep-alive one (Connection: Keep-Alive).

However, after the client closes the TCP connection, if the server tries to write any data to the client, an RST will be generated, which can trigger a cancellation.

Also note that cancellation is an issue for non-streaming APIs too. This is especially the case when the response involves a long polling and hence the connection might stay idle for an extended period.

Explicit cancellation is supported with SPDY, HTTP/2 and QUIC, notably with the go-away message.

### Keep-alive

Keep-alive support allows a client or server to detect a failed peer, even in the event of packet loss or network failures.

There is no keep-alive support in HTTP/1.1 as TCP keep-alive is not a viable approach.

QUIC or HTTP/2 offers special control messages for the purpose of implementing keep-alive support by applications, including browsers.

However, reliable keep-alive and failure detection will likely require a client library with necessary server-side support: doing long-lived streaming over the internet is often error-prone when relying on basic HTTP as the communication protocol.

## Flow control

Flow-control support requires the client to propagate transport-level flow-control events to the client application. The actual mechanism depends on the style of the HTTP client API that your client application uses. For example, you need blocking writes and reads, or non-blocking reads and writes with explicit flow control support for applications to handle and respect flow-control events, in order to prevent either the client or server from being overloaded.

HTTP/1.1 relies on TCP flow control.

SPDY and HTTP/2 have their own flow control at the stream level, which is further subject to TCP flow control at the connection level as requests are multiplexed over a single TCP connection.

QUIC runs on UDP and therefore manages flow control completely on its own.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
