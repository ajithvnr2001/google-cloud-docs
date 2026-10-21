---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions
title: Class FetchOptions (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:40:34.187113+00:00
---

# Class FetchOptions (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class FetchOptions (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class FetchOptions implements Serializable

Allows users to customize the behavior of [URLFetchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService) operations. 

If [#allowTruncate()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions#com_google_appengine_api_urlfetch_FetchOptions_allowTruncate__) is called, [URLFetchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService) will truncate large responses and return them without error. 

If [#disallowTruncate](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions#com_google_appengine_api_urlfetch_FetchOptions_disallowTruncate_) is called, [ResponseTooLargeException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.ResponseTooLargeException) will be thrown if the response is too large. 

If [#followRedirects()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions#com_google_appengine_api_urlfetch_FetchOptions_followRedirects__) is called the [URLFetchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService) operation will follow redirects. 

If [#doNotFollowRedirects()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions#com_google_appengine_api_urlfetch_FetchOptions_doNotFollowRedirects__) is called the [URLFetchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService) operation will not follow redirects. 

If [#validateCertificate()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions#com_google_appengine_api_urlfetch_FetchOptions_validateCertificate__) is called the [URLFetchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService) operation will, if using an HTTPS connection, instruct the application to send a request to the server only if the certificate is valid and signed by a trusted certificate authority (CA), and also includes a hostname that matches the certificate. If the certificate validation fails, a javax.net.ssl.SSLHandshakeException exception is thrown. HTTP connections are unaffected by this option. 

If [#doNotValidateCertificate()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions#com_google_appengine_api_urlfetch_FetchOptions_doNotValidateCertificate__) is called the [URLFetchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService) will not validate the server's SSL certificate in any fashion. This is the default behavior. Note, however, that validation will be turned on by default in the near future. If you rely upon making requests to a site with an invalid or untrusted certificate, you should explicitly call [#doNotValidateCertificate()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions#com_google_appengine_api_urlfetch_FetchOptions_doNotValidateCertificate__) to avoid errors in future versions. 

Notes on usage:  
The recommended way to instantiate a `FetchOptions` object is to statically import Builder.* and invoke a static creation method followed by an instance mutator (if needed):
    
    
     import static com.google.appengine.api.urlfetch.FetchOptions.Builder.*;
    
     ...
     URL url = getURLToFetch();
     urlFetchService.fetch(new HTTPRequest(url, HTTPMethod.GET,
         allowTruncate()));
    
     urlFetchService.fetch(new HTTPRequest(url, HTTPMethod.GET,
         allowTruncate().doNotFollowRedirects()));
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FetchOptions

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

## Static Fields 

### DEFAULT_ALLOW_TRUNCATE
    
    
    public static final boolean DEFAULT_ALLOW_TRUNCATE

**Field Value**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DEFAULT_DEADLINE
    
    
    public static final @Nullable Double DEFAULT_DEADLINE

The default deadline is 5 seconds.

**Field Value**  
---  
**Type** | **Description**  
`[Nullable Double](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Double.html)` |   
  
### DEFAULT_FOLLOW_REDIRECTS
    
    
    public static final boolean DEFAULT_FOLLOW_REDIRECTS

**Field Value**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Methods 

### allowTruncate()
    
    
    public FetchOptions allowTruncate()

Enables response truncation. Please read the class javadoc for an explanation of how allowTruncate is used.

**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions)` | `this` (for chaining)  
  
### disallowTruncate()
    
    
    public FetchOptions disallowTruncate()

Disables response truncation. Please read the class javadoc for an explanation of how allowTruncate is used.

**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions)` | `this` (for chaining)  
  
### doNotFollowRedirects()
    
    
    public FetchOptions doNotFollowRedirects()

Disables following of redirects. Please read the class javadoc for an explanation of how doNotFollowRedirects is used.

**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions)` | `this` (for chaining)  
  
### doNotValidateCertificate()
    
    
    public FetchOptions doNotValidateCertificate()

Disables certificate validation on HTTPS connections. Please read the class javadoc for an explanation of how this option affects certificate validation behavior.

**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions)` | `this` (for chaining)  
  
### followRedirects()
    
    
    public FetchOptions followRedirects()

Enables following of redirects. Please read the class javadoc for an explanation of how followRedirects is used.

**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions)` | `this` (for chaining)  
  
### getAllowTruncate()
    
    
    public boolean getAllowTruncate()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDeadline()
    
    
    public @Nullable Double getDeadline()

**Returns**  
---  
**Type** | **Description**  
`[Nullable Double](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Double.html)` |   
  
### getFollowRedirects()
    
    
    public boolean getFollowRedirects()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getValidateCertificate()
    
    
    public boolean getValidateCertificate()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### setDeadline(Double deadline)
    
    
    public FetchOptions setDeadline(Double deadline)

Sets the deadline, in seconds, for the fetch request.

**Parameter**  
---  
**Name** | **Description**  
`deadline` | `[Double](https://docs.oracle.com/javase/8/docs/api/java/lang/Double.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions)` | `this` (for chaining)  
  
### validateCertificate()
    
    
    public FetchOptions validateCertificate()

Enables certificate validation on HTTPS connections via the normal CA-based mechanism. Please read the class javadoc for an explanation of how this option affects certificate validation behavior.

**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions)` | `this` (for chaining)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
