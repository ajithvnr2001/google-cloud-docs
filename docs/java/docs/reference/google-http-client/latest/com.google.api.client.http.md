---
url: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http
title: Package com.google.api.client.http (2.2.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:33:42.292496+00:00
---

# Package com.google.api.client.http (2.2.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Package com.google.api.client.http (2.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.2.0 (latest)  2.1.1  2.0.3  1.47.1  1.46.3  1.45.3  1.44.2  1.43.2  1.42.3  1.41.8 

Subset of HTTP 1.1 needed from the specification in [RFC 2616: Hypertext Transfer Protocol -- HTTP/1.1](http://tools.ietf.org/html/rfc2616).

## Classes 

### [AbstractHttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractHttpContent)

Abstract implementation of an HTTP content with typical options.

Implementation is not thread-safe.

### [AbstractInputStreamContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractInputStreamContent)

Serializes HTTP request content from an input stream into an output stream.

The #type field is required. Subclasses should implement the #getLength(), [#getInputStream()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractInputStreamContent#com_google_api_client_http_AbstractInputStreamContent_getInputStream__), and #retrySupported() for their specific type of input stream. By default, all content is read from the input stream. If instead you want to limit the maximum amount of content read from the input stream, you may use ByteStreams#limit(InputStream, long).

Implementations don't need to be thread-safe.

### [BasicAuthentication](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.BasicAuthentication)

Basic authentication HTTP request initializer as specified in [Basic Authentication Scheme](http://tools.ietf.org/html/rfc2617#section-2)

Implementation is immutable and thread-safe. It can be used as either an HTTP request initializer or an HTTP request execute interceptor. [#initialize(HttpRequest)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.BasicAuthentication#com_google_api_client_http_BasicAuthentication_initialize_com_google_api_client_http_HttpRequest_) only sets itself as the interceptor. Authentication is actually done in [#intercept(HttpRequest)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.BasicAuthentication#com_google_api_client_http_BasicAuthentication_intercept_com_google_api_client_http_HttpRequest_), which is implemented using [HttpHeaders#setBasicAuthentication(String, String)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpHeaders#com_google_api_client_http_HttpHeaders_setBasicAuthentication_java_lang_String_java_lang_String_).

### [ByteArrayContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.ByteArrayContent)

Concrete implementation of [AbstractInputStreamContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractInputStreamContent) that generates repeatable input streams based on the contents of byte array.

Sample use:
    
    
     
     static void setJsonContent(HttpRequest request, byte[] json) {
     request.setContent(new ByteArrayContent("application/json", json));
     }
     
     

Implementation is not thread-safe.

### [EmptyContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.EmptyContent)

Empty HTTP content of length zero just to force [HttpRequest#execute()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest#com_google_api_client_http_HttpRequest_execute__) to add the header `Content-Length: 0`.

Note that there is no `Content-Length` header if the HTTP request content is ` null` . However, when making a request like PUT or POST without a `Content-Length` header, some servers may respond with a `411 Length Required` error. Specifying the ` Content-Length: 0` header may work around that problem.

### [ExponentialBackOffPolicy](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.ExponentialBackOffPolicy) (deprecated)

**Deprecated.** _(scheduled to be removed in 1.18). Use[HttpBackOffUnsuccessfulResponseHandler](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpBackOffUnsuccessfulResponseHandler) with [ExponentialBackOff](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.ExponentialBackOff) instead._

[Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta)   
Implementation of [BackOffPolicy](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.BackOffPolicy) that increases the back off period for each retry attempt using a randomization function that grows exponentially.

[#getNextBackOffMillis()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.ExponentialBackOffPolicy#com_google_api_client_http_ExponentialBackOffPolicy_getNextBackOffMillis__) is calculated using the following formula:

randomized_interval = retry_interval * (random value in range [1 - randomization_factor, 1 + randomization_factor])

In other words [#getNextBackOffMillis()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.ExponentialBackOffPolicy#com_google_api_client_http_ExponentialBackOffPolicy_getNextBackOffMillis__) will range between the randomization factor percentage below and above the retry interval. For example, using 2 seconds as the base retry interval and 0.5 as the randomization factor, the actual back off period used in the next retry attempt will be between 1 and 3 seconds.

**Note:** max_interval caps the retry_interval and not the randomized_interval.

If the time elapsed since an [ExponentialBackOffPolicy](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.ExponentialBackOffPolicy) instance is created goes past the max_elapsed_time then the method [#getNextBackOffMillis()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.ExponentialBackOffPolicy#com_google_api_client_http_ExponentialBackOffPolicy_getNextBackOffMillis__) starts returning [BackOffPolicy#STOP](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.BackOffPolicy#com_google_api_client_http_BackOffPolicy_STOP). The elapsed time can be reset by calling [#reset()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.ExponentialBackOffPolicy#com_google_api_client_http_ExponentialBackOffPolicy_reset__).

Example: The default retry_interval is .5 seconds, default randomization_factor is 0.5, default multiplier is 1.5 and the default max_interval is 1 minute. For 10 requests the sequence will be (values in seconds) and assuming we go over the max_elapsed_time on the 10th request:
    
    
     request#     retry_interval     randomized_interval
    
     1             0.5                [0.25,   0.75]
     2             0.75               [0.375,  1.125]
     3             1.125              [0.562,  1.687]
     4             1.687              [0.8435, 2.53]
     5             2.53               [1.265,  3.795]
     6             3.795              [1.897,  5.692]
     7             5.692              [2.846,  8.538]
     8             8.538              [4.269, 12.807]
     9            12.807              [6.403, 19.210]
     10           19.210              [BackOffPolicy#STOP](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.BackOffPolicy#com_google_api_client_http_BackOffPolicy_STOP)
     

Implementation is not thread-safe.

### [ExponentialBackOffPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.ExponentialBackOffPolicy.Builder)

[Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta)   
Builder for [ExponentialBackOffPolicy](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.ExponentialBackOffPolicy).

Implementation is not thread-safe.

### [FileContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.FileContent)

Concrete implementation of [AbstractInputStreamContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractInputStreamContent) that generates repeatable input streams based on the contents of a file.

Sample use:
    
    
     
     private static void setRequestJpegContent(HttpRequest request, File jpegFile) {
     request.setContent(new FileContent("image/jpeg", jpegFile));
     }
     
     

Implementation is not thread-safe.

### [GZipEncoding](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.GZipEncoding)

GZip HTTP content encoding.

### [GenericUrl](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.GenericUrl)

URL builder in which the query parameters are specified as generic data key/value pairs, based on the specification [RFC 3986: Uniform Resource Identifier (URI)](http://tools.ietf.org/html/rfc3986).

The query parameters are specified with the data key name as the parameter name, and the data value as the parameter value. Subclasses can declare fields for known query parameters using the [Key](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Key) annotation. `null` parameter names are not allowed, but `null` query values are allowed.

Query parameter values are parsed using [UrlEncodedParser#parse(String, Object)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.UrlEncodedParser#com_google_api_client_http_UrlEncodedParser_parse_java_lang_String_java_lang_Object_).

Implementation is not thread-safe.

### [HttpBackOffIOExceptionHandler](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpBackOffIOExceptionHandler)

[Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta)   
[HttpIOExceptionHandler](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpIOExceptionHandler) implementation with [BackOff](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.BackOff).

It is designed to work with only one [HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest) at a time. As a result you MUST create a new instance of [HttpBackOffIOExceptionHandler](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpBackOffIOExceptionHandler) with a new instance of [BackOff](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.BackOff) for each instance of [HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest).

Sample usage:

request.setIOExceptionHandler(new HttpBackOffIOExceptionHandler(new ExponentialBackOff());

Note: Implementation doesn't call [BackOff#reset](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.BackOff#com_google_api_client_util_BackOff_reset_) at all, since it expects a new [BackOff](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.BackOff) instance.

Implementation is not thread-safe

### [HttpBackOffUnsuccessfulResponseHandler](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpBackOffUnsuccessfulResponseHandler)

[Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta)   
Back-off handler which handles an abnormal HTTP response with [BackOff](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.BackOff).

It is designed to work with only one [HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest) at a time. As a result you MUST create a new instance of [HttpBackOffUnsuccessfulResponseHandler](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpBackOffUnsuccessfulResponseHandler) with a new instance of [BackOff](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.BackOff) for each instance of [HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest).

Sample usage:

request.setUnsuccessfulResponseHandler( new HttpBackOffUnsuccessfulResponseHandler(new ExponentialBackOff()));

Note: Implementation doesn't call [BackOff#reset](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.BackOff#com_google_api_client_util_BackOff_reset_) at all, since it expects a new [BackOff](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.BackOff) instance.

Implementation is not thread-safe

### [HttpEncodingStreamingContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpEncodingStreamingContent)

Streaming content based on an HTTP encoding.

Implementation is thread-safe only if the streaming content and HTTP encoding are thread-safe.

### [HttpHeaders](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpHeaders)

Stores HTTP headers used in an HTTP request or response, as defined in [Header Field Definitions](http://tools.ietf.org/html/rfc2616#section-14).

`null` is not allowed as a name or value of a header. Names are case-insensitive.

Implementation is not thread-safe.

### [HttpMediaType](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpMediaType)

HTTP Media-type as specified in the [HTTP RFC](https://datatracker.ietf.org/doc/html/rfc2616#section-3.7).

Implementation is not thread-safe.

### [HttpMethods](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpMethods)

HTTP request method constants specified in [RFC 2616 Section 5.1.1](http://tools.ietf.org/html/rfc2616#section-5.1.1).

### [HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest)

HTTP request.

Implementation is not thread-safe.

### [HttpRequestFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestFactory)

Thread-safe light-weight HTTP request factory layer on top of the HTTP transport that has an optional [HTTP request initializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer) for initializing requests.

For example, to use a particular authorization header across all requests, use:

public static HttpRequestFactory createRequestFactory(HttpTransport transport) { return transport.createRequestFactory(new HttpRequestInitializer() { public void initialize(HttpRequest request) throws IOException { request.getHeaders().setAuthorization("..."); } }); }

### [HttpResponse](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse)

HTTP response.

Callers should call [#disconnect](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse#com_google_api_client_http_HttpResponse_disconnect_) when the HTTP response object is no longer needed. However, [#disconnect](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse#com_google_api_client_http_HttpResponse_disconnect_) does not have to be called if the response stream is properly closed. Example usage:

HttpResponse response = request.execute(); try { // process the HTTP response object } finally { response.disconnect(); }

Implementation is not thread-safe.

### [HttpResponseException.Builder](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponseException.Builder)

Builder.

Implementation is not thread safe.

### [HttpStatusCodes](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpStatusCodes)

Constants enumerating the HTTP status codes. Includes status codes specified in [RFC2616](http://tools.ietf.org/html/rfc2616#section-10.3) (HTTP/1.1).

### [HttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport)

Thread-safe abstract HTTP transport.

Implementation is thread-safe, and subclasses must be thread-safe. For maximum efficiency, applications should use a single globally-shared instance of the HTTP transport.

The recommended concrete implementation HTTP transport library to use depends on what environment you are running in:

  * Google App Engine: use ` com.google.api.client.extensions.appengine.http.UrlFetchTransport`. 
    * `com.google.api.client.apache.ApacheHttpTransport` doesn't work on App Engine because the Apache HTTP Client opens its own sockets (though in theory there are ways to hack it to work on App Engine that might work). 
    * `com.google.api.client.javanet.NetHttpTransport` is discouraged due to a bug in the App Engine SDK itself in how it parses HTTP headers in the response. 
  * Android: 
    * For maximum backwards compatibility with older SDK's use ` newCompatibleTransport` from ` com.google.api.client.extensions.android.http.AndroidHttp` (read its JavaDoc for details). 
    * If your application is targeting Gingerbread (SDK 2.3) or higher, simply use ` com.google.api.client.javanet.NetHttpTransport`. 
  * Other Java environments 
    * `com.google.api.client.javanet.NetHttpTransport` is based on the HttpURLConnection built into the Java SDK. It is the preferred choice if not using Apache HTTP Client. 
    * `com.google.api.client.apache.ApacheHttpTransport` is a good choice for users of the Apache HTTP Client, especially if you need some of the configuration options available in that library. 



Some HTTP transports do not support all HTTP methods. Use [#supportsMethod(String)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport#com_google_api_client_http_HttpTransport_supportsMethod_java_lang_String_) to check if a certain HTTP method is supported. Calling [#buildRequest()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport#com_google_api_client_http_HttpTransport_buildRequest_) on a method that is not supported will result in an IllegalArgumentException.

Subclasses should override [#supportsMethod(String)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport#com_google_api_client_http_HttpTransport_supportsMethod_java_lang_String_) and #buildRequest(String, String) to build requests and specify which HTTP methods are supported.

### [InputStreamContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.InputStreamContent)

Concrete implementation of [AbstractInputStreamContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractInputStreamContent) that simply handles the transfer of data from an input stream to an output stream. This should only be used for streams that can not be re-opened and retried. If you have a stream that it is possible to recreate please create a new subclass of [AbstractInputStreamContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.AbstractInputStreamContent).

The input stream is guaranteed to be closed at the end of #writeTo(OutputStream).

Sample use with a URL:
    
    
     
     private static void setRequestJpegContent(HttpRequest request, URL jpegUrl) throws IOException {
     request.setContent(new InputStreamContent("image/jpeg", jpegUrl.openStream()));
     }
     
     

Implementation is not thread-safe.

### [LowLevelHttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.LowLevelHttpRequest)

Low-level HTTP request.

This allows providing a different implementation of the HTTP request that is more compatible with the Java environment used.

Implementation has no fields and therefore thread-safe, but sub-classes are not necessarily thread-safe.

### [LowLevelHttpResponse](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.LowLevelHttpResponse)

Low-level HTTP response.

This allows providing a different implementation of the HTTP response that is more compatible with the Java environment used.

Implementation has no fields and therefore thread-safe, but sub-classes are not necessarily thread-safe.

### [MultipartContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.MultipartContent)

Serializes MIME multipart content as specified by [RFC 2387: The MIME Multipart/Related Content-type](http://tools.ietf.org/html/rfc2387) and [RFC 2046: Multipurpose Internet Mail Extensions: The Multipart/mixed (primary) subtype](http://tools.ietf.org/html/rfc1521#section-7.2.2).

By default the media type is `"multipart/related; boundary=**END_OF_PART**`, but this may be customized by calling [#setMediaType(HttpMediaType)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.MultipartContent#com_google_api_client_http_MultipartContent_setMediaType_com_google_api_client_http_HttpMediaType_), #getMediaType(), or [#setBoundary(String)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.MultipartContent#com_google_api_client_http_MultipartContent_setBoundary_java_lang_String_).

Implementation is not thread-safe.

### [MultipartContent.Part](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.MultipartContent.Part)

Single part of a multi-part request.

Implementation is not thread-safe.

### [OpenCensusUtils](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.OpenCensusUtils)

[Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta)   
Utilities for Census monitoring and tracing.

### [UriTemplate](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.UriTemplate)

Expands URI Templates.

This class supports URI Template Level 1, partial support for Levels 2 and 3, and Level 4 composite templates as described in: [RFC 6570](http://tools.ietf.org/html/rfc6570).

Specifically, for the variables: var := "value" list := ["red", "green", "blue"] keys := [("semi", ";"),("dot", "."),("comma", ",")]

The following templates results in the following expansions: {var} -> value {list} -> red,green,blue {list _} - > red,green,blue {keys} -> semi,%3B,dot,.,comma,%2C {keys_} -> semi=%3B,dot=.,comma=%2C {+list} -> red,green,blue {+list _} - > red,green,blue {+keys} -> semi,;,dot,.,comma,, {+keys_} -> semi=;,dot=.,comma=, {#list} -> #red,green,blue {#list*} ->

# red,green,blue {#keys} -> #semi,;,dot,.,comma,, {#keys*} -> #semi=;,dot=.,comma=, X{.list} ->

X.red,green,blue X{.list _} - > X.red.green.blue X{.keys} -> X.semi,%3B,dot,.,comma,%2C X{.keys_} -> X.semi=%3B.dot=..comma=%2C {/list} -> /red,green,blue {/list _} - > /red/green/blue {/keys} -> /semi,%3B,dot,.,comma,%2C {/keys_} -> /semi=%3B/dot=./comma=%2C {;list} -> ;list=red,green,blue {;list _} - > ;list=red;list=green;list=blue {;keys} -> ;keys=semi,%3B,dot,.,comma,%2C {;keys_} -> ;semi=%3B;dot=.;comma=%2C {?list} -> ?list=red,green,blue {?list _} - > ?list=red&list=green&list=blue {?keys} -> ?keys=semi,%3B,dot,.,comma,%2C {?keys_} -> ?semi=%3B&dot=.&comma=%2C {&list} -> &list=red,green,blue {&list _} - > &list=red&list=green&list=blue {&keys} -> &keys=semi,%3B,dot,.,comma,%2C {&keys_} -> &semi=%3B&dot=.&comma=%2C {?var,list} -> ?var=value&list=red,green,blue

### [UrlEncodedContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.UrlEncodedContent)

Implements support for HTTP form content encoding serialization of type ` application/x-www-form-urlencoded` as specified in the [HTML 4.0 Specification](http://www.w3.org/TR/REC-html40/interact/forms.html#h-17.13.4.1).

Sample usage:

static void setContent(HttpRequest request, Object item) { request.setContent(new UrlEncodedContent(item)); }

Implementation is not thread-safe.

### [UrlEncodedParser](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.UrlEncodedParser)

Implements support for HTTP form content encoding parsing of type ` application/x-www-form-urlencoded` as specified in the [HTML 4.0 Specification](http://www.w3.org/TR/1998/REC-html40-19980424/interact/forms.html#h-17.13.4.1).

Implementation is thread-safe.

The data is parsed using [#parse(String, Object)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.UrlEncodedParser#com_google_api_client_http_UrlEncodedParser_parse_java_lang_String_java_lang_Object_).

Sample usage:

static void setParser(HttpTransport transport) { transport.addParser(new UrlEncodedParser()); }

## Interfaces 

### [BackOffPolicy](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.BackOffPolicy) (deprecated)

**Deprecated.** _(scheduled to be removed in 1.18) Use[HttpBackOffUnsuccessfulResponseHandler](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpBackOffUnsuccessfulResponseHandler) instead._

[Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta)   
Strategy interface to control back off between retry attempts.

### [HttpBackOffUnsuccessfulResponseHandler.BackOffRequired](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpBackOffUnsuccessfulResponseHandler.BackOffRequired)

[Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta)   
Interface which defines if back-off is required based on an abnormal [HttpResponse](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse).

### [HttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpContent)

Serializes HTTP request content into an output stream.

Implementations don't need to be thread-safe.

### [HttpEncoding](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpEncoding)

HTTP content encoding.

Implementations don't need to be thread-safe.

### [HttpExecuteInterceptor](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpExecuteInterceptor)

HTTP request execute interceptor to intercept the start of [HttpRequest#execute()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest#com_google_api_client_http_HttpRequest_execute__) before executing the HTTP request.

For example, this might be used to sign a request for OAuth:

public class OAuthSigner implements HttpExecuteInterceptor { public void intercept(HttpRequest request) throws IOException { // sign request... } }

Sample usage with a request factory:

public static HttpRequestFactory createRequestFactory(HttpTransport transport) { final OAuthSigner signer = new OAuthSigner(...); return transport.createRequestFactory(new HttpRequestInitializer() { public void initialize(HttpRequest request) { request.setInterceptor(signer); } }); }

More complex usage example:

public static HttpRequestFactory createRequestFactory2(HttpTransport transport) { final OAuthSigner signer = new OAuthSigner(...); return transport.createRequestFactory(new HttpRequestInitializer() { public void initialize(HttpRequest request) { request.setInterceptor(new HttpExecuteInterceptor() { public void intercept(HttpRequest request) throws IOException { signer.intercept(request); } }); } }); }

Implementations should normally be thread-safe.

### [HttpIOExceptionHandler](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpIOExceptionHandler)

[Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta)   
Handles an [IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html) in an HTTP request.

For example, this might be used to handle an [IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html) with [BackOff](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.BackOff) policy.

public static class HttpBackOffIOExceptionHandler implements HttpIOExceptionHandler { BackOff backOff; Sleeper sleeper; public boolean handle(HttpRequest request, boolean supportsRetry) throws IOException { if (!supportsRetry) { return false; } try { return BackOffUtils.next(sleeper, backOff); } catch (InterruptedException exception) { Thread.currentThread().interrupt(); return false; } } }

### [HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer)

HTTP request initializer.

For example, this might be used to disable request timeouts:

public class DisableTimeout implements HttpRequestInitializer { public void initialize(HttpRequest request) { request.setConnectTimeout(0); request.setReadTimeout(0); } }

Sample usage with a request factory:

public static HttpRequestFactory createRequestFactory(HttpTransport transport) { return transport.createRequestFactory(new DisableTimeout()); }

More complex usage example:

public static HttpRequestFactory createRequestFactory2(HttpTransport transport) { final DisableTimeout disableTimeout = new DisableTimeout(); return transport.createRequestFactory(new HttpRequestInitializer() { public void initialize(HttpRequest request) { disableTimeout.initialize(request); } }); }

Implementations should normally be thread-safe.

### [HttpResponseInterceptor](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponseInterceptor)

HTTP response interceptor to intercept the end of [HttpRequest#execute()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest#com_google_api_client_http_HttpRequest_execute__) before returning a successful response or throwing an exception for an unsuccessful response.

For example, this might be used to add a simple timer on requests:

public static class TimerResponseInterceptor implements HttpResponseInterceptor {

private final long startTime = System.nanoTime();

public void interceptResponse(HttpResponse response) { long elapsedNanos = System.nanoTime() - startTime; System.out.println("elapsed seconds: " + TimeUnit.NANOSECONDS.toSeconds(elapsedNanos) + "s"); } }

Sample usage with a request factory:

public static HttpRequestFactory createRequestFactory(HttpTransport transport) { return transport.createRequestFactory(new HttpRequestInitializer() {

@Override public void initialize(HttpRequest request) { request.setResponseInterceptor(new TimerResponseInterceptor()); } }); }

More complex usage example:

public static HttpRequestFactory createRequestFactory2(HttpTransport transport) { final HttpResponseInterceptor responseInterceptor = new TimerResponseInterceptor(); return transport.createRequestFactory(new HttpRequestInitializer() {

public void initialize(HttpRequest request) { request.setResponseInterceptor(new HttpResponseInterceptor() {

public void interceptResponse(HttpResponse response) throws IOException { responseInterceptor.interceptResponse(response); } }); } }); }

Implementations should normally be thread-safe.

### [HttpUnsuccessfulResponseHandler](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpUnsuccessfulResponseHandler)

Interface which handles abnormal HTTP responses (in other words not 2XX).

For example, this might be used to refresh an OAuth 2 token:

public static class RefreshTokenHandler implements HttpUnsuccessfulResponseHandler { public boolean handleResponse( HttpRequest request, HttpResponse response, boolean retrySupported) throws IOException { if (response.getStatusCode() == HttpStatusCodes.STATUS_CODE_UNAUTHORIZED) { refreshToken(); } return false; } }

Sample usage with a request factory:

public static HttpRequestFactory createRequestFactory(HttpTransport transport) { final RefreshTokenHandler handler = new RefreshTokenHandler(); return transport.createRequestFactory(new HttpRequestInitializer() { public void initialize(HttpRequest request) { request.setUnsuccessfulResponseHandler(handler); } }); }

More complex usage example:

public static HttpRequestFactory createRequestFactory2(HttpTransport transport) { final RefreshTokenHandler handler = new RefreshTokenHandler(); return transport.createRequestFactory(new HttpRequestInitializer() { public void initialize(HttpRequest request) { request.setUnsuccessfulResponseHandler(new HttpUnsuccessfulResponseHandler() { public boolean handleResponse( HttpRequest request, HttpResponse response, boolean retrySupported) throws IOException { return handler.handleResponse(request, response, retrySupported); } }); } }); }

## Exceptions 

### [HttpResponseException](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponseException)

Exception thrown when an error status code is detected in an HTTP response.

Implementation is not thread safe.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
