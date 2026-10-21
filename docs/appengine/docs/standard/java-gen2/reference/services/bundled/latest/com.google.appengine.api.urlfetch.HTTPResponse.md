---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPResponse
title: Class HTTPResponse (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:34:44.866725+00:00
---

# Class HTTPResponse (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class HTTPResponse (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class HTTPResponse implements Serializable

`HTTPResponse` encapsulates the results of a ` HTTPRequest` made via the `URLFetchService`.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > HTTPResponse

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

### HTTPResponse(int responseCode, byte @Nullable [] content, @Nullable URL finalUrl, List<HTTPHeader> headers)
    
    
    public HTTPResponse(int responseCode, byte @Nullable [] content, @Nullable URL finalUrl, List<HTTPHeader> headers)

Construct an HTTPResponse object.

**Parameters**  
---  
**Name** | **Description**  
`responseCode` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the HTTP response code  
`content` | `byte @org.jspecify.annotations.Nullable []`  
the HTTP response content (can be null)  
`finalUrl` | `[Nullable URL](https://docs.oracle.com/javase/8/docs/api/java/net/@org/jspecify/annotations/Nullable%20URL.html)`  
the URL that served the request if redirection was followed (can be null)  
`headers` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[HTTPHeader](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPHeader)>`  
the HTTP response headers  
  
## Methods 

### getContent()
    
    
    public byte @Nullable [] getContent()

Returns the content of the request, or null if there is no content present (e.g. in a HEAD request).

**Returns**  
---  
**Type** | **Description**  
`byte @org.jspecify.annotations.Nullable []` |   
  
### getFinalUrl()
    
    
    public @Nullable URL getFinalUrl()

Returns the final URL the content came from if redirects were followed automatically in the request, if different than the input URL; otherwise this will be null.

**Returns**  
---  
**Type** | **Description**  
`[Nullable URL](https://docs.oracle.com/javase/8/docs/api/java/net/@org/jspecify/annotations/Nullable%20URL.html)` |   
  
### getHeaders()
    
    
    public List<HTTPHeader> getHeaders()

Returns a `List` of HTTP response headers that were returned by the remote server. Multi-valued headers are represented as a single `HTTPHeader` with comma-separated values.

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[HTTPHeader](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPHeader)>` |   
  
### getHeadersUncombined()
    
    
    public List<HTTPHeader> getHeadersUncombined()

Returns a `List` of HTTP response headers that were returned by the remote server. These are not combined for repeated values.

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[HTTPHeader](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPHeader)>` |   
  
### getResponseCode()
    
    
    public int getResponseCode()

Returns the HTTP response code from the request (e.g. 200, 500, etc.).

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
