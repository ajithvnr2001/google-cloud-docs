---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPRequest
title: Class HTTPRequest (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:05:25.693047+00:00
---

# Class HTTPRequest (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class HTTPRequest (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class HTTPRequest implements Serializable

`HTTPRequest` encapsulates a single HTTP request that is made via the `URLFetchService`.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > HTTPRequest

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

## Constructors 

### HTTPRequest(URL url)
    
    
    public HTTPRequest(URL url)

Creates a `HTTPRequest` that represents a GET request to the specified URL.

**Parameter**  
---  
**Name** | **Description**  
`url` | `[URL](https://docs.oracle.com/javase/8/docs/api/java/net/URL.html)`  
  
  
### HTTPRequest(URL url, HTTPMethod method)
    
    
    public HTTPRequest(URL url, HTTPMethod method)

Creates a `HTTPRequest` that represents an HTTP request to the specified URL with the specified HTTP method (GET, POST, etc).

**Parameters**  
---  
**Name** | **Description**  
`url` | `[URL](https://docs.oracle.com/javase/8/docs/api/java/net/URL.html)`  
  
`method` | `[HTTPMethod](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPMethod)`  
  
  
### HTTPRequest(URL url, HTTPMethod method, FetchOptions fetchOptions)
    
    
    public HTTPRequest(URL url, HTTPMethod method, FetchOptions fetchOptions)

Creates a `HTTPRequest` that represents an HTTP request to the specified URL with the specified HTTP method (GET, POST, etc) and the specified [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions).

**Parameters**  
---  
**Name** | **Description**  
`url` | `[URL](https://docs.oracle.com/javase/8/docs/api/java/net/URL.html)`  
  
`method` | `[HTTPMethod](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPMethod)`  
  
`fetchOptions` | `[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions)`  
  
  
## Methods 

### addHeader(HTTPHeader header)
    
    
    public void addHeader(HTTPHeader header)

Adds `header` to this request. If an `HTTPHeader` with the same `name` already exists for this request, it's values are merged with `header`.

**Parameter**  
---  
**Name** | **Description**  
`header` | `[HTTPHeader](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPHeader)`  
a not `null` `HTTPHeader`  
  
### getFetchOptions()
    
    
    public FetchOptions getFetchOptions()

Get the fetch options for this request.

**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions)` |   
  
### getHeaders()
    
    
    public List<HTTPHeader> getHeaders()

Returns an immutable `List` of `HTTPHeader` objects that have been added to this request.

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[HTTPHeader](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPHeader)>` |   
  
### getMethod()
    
    
    public HTTPMethod getMethod()

Gets the HTTP method for this request (GET, POST, etc).

**Returns**  
---  
**Type** | **Description**  
`[HTTPMethod](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPMethod)` |   
  
### getPayload()
    
    
    public byte @Nullable [] getPayload()

Gets the payload (such as POST body) for this request. Certain HTTP methods (e.g. GET) will not have any payload, and this method will return null.

**Returns**  
---  
**Type** | **Description**  
`byte @org.jspecify.annotations.Nullable []` |   
  
### getURL()
    
    
    public URL getURL()

Gets the URL for this request.

**Returns**  
---  
**Type** | **Description**  
`[URL](https://docs.oracle.com/javase/8/docs/api/java/net/URL.html)` |   
  
### setHeader(HTTPHeader header)
    
    
    public void setHeader(HTTPHeader header)

Sets an `HTTPHeader` for this request. If an [HTTPHeader](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPHeader) with the same `name` already exists, its value is replaced.

**Parameter**  
---  
**Name** | **Description**  
`header` | `[HTTPHeader](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPHeader)`  
  
  
### setPayload(byte[] payload)
    
    
    public void setPayload(byte[] payload)

Sets the payload for this request. This method should not be called for certain HTTP methods (e.g. GET).

**Parameter**  
---  
**Name** | **Description**  
`payload` | `byte[]`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
