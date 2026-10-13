---
url: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestFactory
title: Class HttpRequestFactory (2.2.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:11:02.502639+00:00
---

# Class HttpRequestFactory (2.2.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestFactory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HttpRequestFactory (2.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.2.0 (latest)  2.1.1  2.0.3  1.47.1  1.46.3  1.45.3  1.44.2  1.43.2  1.42.3  1.41.8 
    
    
    public final class HttpRequestFactory

Thread-safe light-weight HTTP request factory layer on top of the HTTP transport that has an optional [HTTP request initializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer) for initializing requests.

For example, to use a particular authorization header across all requests, use:

public static HttpRequestFactory createRequestFactory(HttpTransport transport) { return transport.createRequestFactory(new HttpRequestInitializer() { public void initialize(HttpRequest request) throws IOException { request.getHeaders().setAuthorization("..."); } }); }

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > HttpRequestFactory

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

### buildDeleteRequest(GenericUrl url)
    
    
    public HttpRequest buildDeleteRequest(GenericUrl url)

Builds a `DELETE` request for the given URL.

**Parameter**  
---  
**Name** | **Description**  
`url` | `[GenericUrl](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.GenericUrl)`  
HTTP request URL or `null` for none  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest)` | new HTTP request  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### buildGetRequest(GenericUrl url)
    
    
    public HttpRequest buildGetRequest(GenericUrl url)

Builds a `GET` request for the given URL.

**Parameter**  
---  
**Name** | **Description**  
`url` | `[GenericUrl](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.GenericUrl)`  
HTTP request URL or `null` for none  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest)` | new HTTP request  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### buildHeadRequest(GenericUrl url)
    
    
    public HttpRequest buildHeadRequest(GenericUrl url)

Builds a `HEAD` request for the given URL.

**Parameter**  
---  
**Name** | **Description**  
`url` | `[GenericUrl](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.GenericUrl)`  
HTTP request URL or `null` for none  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest)` | new HTTP request  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### buildPatchRequest(GenericUrl url, HttpContent content)
    
    
    public HttpRequest buildPatchRequest(GenericUrl url, HttpContent content)

Builds a `PATCH` request for the given URL and content.

**Parameters**  
---  
**Name** | **Description**  
`url` | `[GenericUrl](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.GenericUrl)`  
HTTP request URL or `null` for none  
`content` | `[HttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpContent)`  
HTTP request content or `null` for none  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest)` | new HTTP request  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### buildPostRequest(GenericUrl url, HttpContent content)
    
    
    public HttpRequest buildPostRequest(GenericUrl url, HttpContent content)

Builds a `POST` request for the given URL and content.

**Parameters**  
---  
**Name** | **Description**  
`url` | `[GenericUrl](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.GenericUrl)`  
HTTP request URL or `null` for none  
`content` | `[HttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpContent)`  
HTTP request content or `null` for none  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest)` | new HTTP request  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### buildPutRequest(GenericUrl url, HttpContent content)
    
    
    public HttpRequest buildPutRequest(GenericUrl url, HttpContent content)

Builds a `PUT` request for the given URL and content.

**Parameters**  
---  
**Name** | **Description**  
`url` | `[GenericUrl](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.GenericUrl)`  
HTTP request URL or `null` for none  
`content` | `[HttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpContent)`  
HTTP request content or `null` for none  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest)` | new HTTP request  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### buildRequest(String requestMethod, GenericUrl url, HttpContent content)
    
    
    public HttpRequest buildRequest(String requestMethod, GenericUrl url, HttpContent content)

Builds a request for the given HTTP method, URL, and content.

**Parameters**  
---  
**Name** | **Description**  
`requestMethod` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
HTTP request method  
`url` | `[GenericUrl](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.GenericUrl)`  
HTTP request URL or `null` for none  
`content` | `[HttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpContent)`  
HTTP request content or `null` for none  
**Returns**  
---  
**Type** | **Description**  
`[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest)` | new HTTP request  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### getInitializer()
    
    
    public HttpRequestInitializer getInitializer()

Returns the HTTP request initializer or `null` for none.

This initializer is invoked before setting its method, URL, or content.

**Returns**  
---  
**Type** | **Description**  
`[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer)` |   
  
### getTransport()
    
    
    public HttpTransport getTransport()

Returns the HTTP transport.

**Returns**  
---  
**Type** | **Description**  
`[HttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
