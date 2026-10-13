---
url: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.extensions.appengine.http.UrlFetchTransport
title: Class UrlFetchTransport (2.2.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:47:29.766550+00:00
---

# Class UrlFetchTransport (2.2.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.extensions.appengine.http.UrlFetchTransport

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class UrlFetchTransport (2.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.2.0 (latest)  2.1.1  2.0.3  1.47.1  1.46.3  1.45.3  1.44.2  1.43.2  1.42.3  1.41.8 
    
    
    public final class UrlFetchTransport extends HttpTransport

Thread-safe HTTP transport for Google App Engine based on [URL Fetch](https://cloud.google.com/appengine/docs/standard/java/issue-requests).

Implementation is thread-safe. For maximum efficiency, applications should use a single globally-shared instance of the HTTP transport.

URL Fetch is only available on Google App Engine (not on any other Java environment), and is the underlying HTTP transport used for App Engine. Their implementation of [HttpURLConnection](https://docs.oracle.com/javase/8/docs/api/java/net/HttpURLConnection.html) is simply an abstraction layer on top of URL Fetch. By implementing a transport that directly uses URL Fetch, we can optimize the behavior slightly, and can potentially take advantage of features in URL Fetch that are not available in [HttpURLConnection](https://docs.oracle.com/javase/8/docs/api/java/net/HttpURLConnection.html). Furthermore, there is currently a serious bug in how HTTP headers are processed in the App Engine implementation of [HttpURLConnection](https://docs.oracle.com/javase/8/docs/api/java/net/HttpURLConnection.html), which we are able to avoid using this implementation. Therefore, this is the recommended transport to use on App Engine.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [HttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport) > UrlFetchTransport

## Inherited Members

[HttpTransport.buildRequest(String,String)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport#com_google_api_client_http_HttpTransport_buildRequest_java_lang_String_java_lang_String_)

[HttpTransport.createRequestFactory()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport#com_google_api_client_http_HttpTransport_createRequestFactory__)

[HttpTransport.createRequestFactory(HttpRequestInitializer)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport#com_google_api_client_http_HttpTransport_createRequestFactory_com_google_api_client_http_HttpRequestInitializer_)

[HttpTransport.isMtls()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport#com_google_api_client_http_HttpTransport_isMtls__)

[HttpTransport.isShutdown()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport#com_google_api_client_http_HttpTransport_isShutdown__)

[HttpTransport.shutdown()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport#com_google_api_client_http_HttpTransport_shutdown__)

[HttpTransport.supportsMethod(String)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport#com_google_api_client_http_HttpTransport_supportsMethod_java_lang_String_)

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

### getDefaultInstance()
    
    
    public static UrlFetchTransport getDefaultInstance()

Returns a global thread-safe instance.

**Returns**  
---  
**Type** | **Description**  
`[UrlFetchTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.extensions.appengine.http.UrlFetchTransport)` |   
  
## Constructors 

### UrlFetchTransport()
    
    
    public UrlFetchTransport()

Constructor with the default fetch options.

Use Builder to modify fetch options.

## Methods 

### buildRequest(String method, String url)
    
    
    protected UrlFetchRequest buildRequest(String method, String url)

Builds a low level HTTP request for the given HTTP method.

**Parameters**  
---  
**Name** | **Description**  
`method` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`url` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.api.client.extensions.appengine.http.UrlFetchRequest` |   
**Overrides**

[HttpTransport.buildRequest(String method, String url)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport#com_google_api_client_http_HttpTransport_buildRequest_java_lang_String_java_lang_String_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### supportsMethod(String method)
    
    
    public boolean supportsMethod(String method)

Returns whether a specified HTTP method is supported by this transport.

Default implementation returns true if and only if the request method is `"DELETE"`, `"GET"`, `"POST"`, or `"PUT"`. Subclasses should override.

**Parameter**  
---  
**Name** | **Description**  
`method` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[HttpTransport.supportsMethod(String method)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport#com_google_api_client_http_HttpTransport_supportsMethod_java_lang_String_)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
