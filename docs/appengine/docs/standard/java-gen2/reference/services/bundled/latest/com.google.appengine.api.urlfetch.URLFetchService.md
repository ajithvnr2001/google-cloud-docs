---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService
title: Interface URLFetchService (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:31:58.441292+00:00
---

# Interface URLFetchService (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface URLFetchService (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface URLFetchService

The `URLFetchService` provides a way for user code to execute HTTP requests to external URLs.

Chunked and hanging requests are not supported, and all content will be returned in a single block.

## Static Fields 

### DEFAULT_DEADLINE_PROPERTY
    
    
    public static final String DEFAULT_DEADLINE_PROPERTY

System property for defining a global default URLFetch deadline.

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### DEFAULT_TLS_VALIDATION_PROPERTY
    
    
    public static final String DEFAULT_TLS_VALIDATION_PROPERTY

System property to turn on server certificate validation by default. The value of the property should be the string `"true"` in order to enable validation.

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Methods 

### fetch(HTTPRequest request)
    
    
    public abstract HTTPResponse fetch(HTTPRequest request)

Execute the specified request and return its response.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[HTTPRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPRequest)`  
The http request.  
**Returns**  
---  
**Type** | **Description**  
`[HTTPResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPResponse)` | The result of the fetch.  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | If `request.getMethod` is not supported by the `URLFetchService`.  
  
### fetch(URL url)
    
    
    public abstract HTTPResponse fetch(URL url)

Convenience method for retrieving a specific URL via a HTTP GET request with no custom headers and default values for all [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions) attributes. For more complex requests, use [#fetch(HTTPRequest)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService#com_google_appengine_api_urlfetch_URLFetchService_fetch_com_google_appengine_api_urlfetch_HTTPRequest_).

**Parameter**  
---  
**Name** | **Description**  
`url` | `[URL](https://docs.oracle.com/javase/8/docs/api/java/net/URL.html)`  
The url to fetch.  
**Returns**  
---  
**Type** | **Description**  
`[HTTPResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPResponse)` | The result of the fetch.  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | If the provided URL is malformed.  
  
### fetchAsync(HTTPRequest request)
    
    
    public abstract Future<HTTPResponse> fetchAsync(HTTPRequest request)

Asynchronously execute the specified request and return its response.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[HTTPRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPRequest)`  
The http request.  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[HTTPResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPResponse)>` | A future containing the result of the fetch, or one of the exceptions documented for [#fetch(HTTPRequest)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService#com_google_appengine_api_urlfetch_URLFetchService_fetch_com_google_appengine_api_urlfetch_HTTPRequest_).  
  
### fetchAsync(URL url)
    
    
    public abstract Future<HTTPResponse> fetchAsync(URL url)

Convenience method for asynchronously retrieving a specific URL via a HTTP GET request with no custom headers and default values for all [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions) attributes. For more complex requests, use [#fetchAsync(HTTPRequest)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService#com_google_appengine_api_urlfetch_URLFetchService_fetchAsync_com_google_appengine_api_urlfetch_HTTPRequest_).

**Parameter**  
---  
**Name** | **Description**  
`url` | `[URL](https://docs.oracle.com/javase/8/docs/api/java/net/URL.html)`  
The url to fetch.  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[HTTPResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPResponse)>` | A future containing the result of the fetch, or one of the exceptions documented for [#fetch(URL)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService#com_google_appengine_api_urlfetch_URLFetchService_fetch_java_net_URL_).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
