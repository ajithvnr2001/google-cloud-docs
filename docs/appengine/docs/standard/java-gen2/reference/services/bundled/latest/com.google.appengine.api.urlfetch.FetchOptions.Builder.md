---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions.Builder
title: Class FetchOptions.Builder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:58:26.365450+00:00
---

# Class FetchOptions.Builder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class FetchOptions.Builder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static final class FetchOptions.Builder

Contains static creation methods for [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FetchOptions.Builder

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

## Static Methods 

### allowTruncate()
    
    
    public static FetchOptions allowTruncate()

Create a [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions) that allows truncation of the response. Shorthand for `FetchOptions.withDefaults().allowTruncate();`. Please read the [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions) class javadoc for an explanation of how response truncating works.

**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions)` | The newly created FetchOptions instance.  
  
### disallowTruncate()
    
    
    public static FetchOptions disallowTruncate()

Create a [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions) that disallows truncation of the response. Shorthand for `FetchOptions.withDefaults().disallowTruncate();`. Please read the [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions) class javadoc for an explanation of how esponse truncating works.

**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions)` | The newly created FetchOptions instance.  
  
### doNotFollowRedirects()
    
    
    public static FetchOptions doNotFollowRedirects()

Create a [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions) that does not follow redirects. Shorthand for `FetchOptions.withDefaults().doNotFollowRedirects();`. Please read the [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions) class javadoc for an explanation of how redirection following works.

**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions)` | The newly created FetchOptions instance.  
  
### doNotValidateCertificate()
    
    
    public static FetchOptions doNotValidateCertificate()

Create a [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions) that does not perform SSL certificate validation.

Shorthand for `FetchOptions.withDefaults().doNotValidateCertificate();`. Please read the [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions) class javadoc for an explanation of how certificate validation works.

**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions)` | The newly created FetchOptions instance.  
  
### followRedirects()
    
    
    public static FetchOptions followRedirects()

Create a [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions) that follows redirects. Shorthand for `FetchOptions.withDefaults().followRedirects();`. Please read the [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions) class javadoc for an explanation of how redirection following works.

**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions)` | The newly created FetchOptions instance.  
  
### validateCertificate()
    
    
    public static FetchOptions validateCertificate()

Create a [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions) that performs SSL certificate validation.

Shorthand for `FetchOptions.withDefaults().validateCertificate();`. Please read the [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions) class javadoc for an explanation of how certificate validation works.

**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions)` | The newly created FetchOptions instance.  
  
### withDeadline(double deadline)
    
    
    public static FetchOptions withDeadline(double deadline)

Create a [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions) with the specified deadline. Shorthand for `FetchOptions.withDefaults().setDeadline(deadline);`.

**Parameter**  
---  
**Name** | **Description**  
`deadline` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions)` | The newly created FetchOptions instance.  
  
### withDefaults()
    
    
    public static FetchOptions withDefaults()

Helper method for creating a [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions) instance with default values. See Also: [FetchOptions#DEFAULT_ALLOW_TRUNCATE](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions#com_google_appengine_api_urlfetch_FetchOptions_DEFAULT_ALLOW_TRUNCATE), [FetchOptions#DEFAULT_DEADLINE](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions#com_google_appengine_api_urlfetch_FetchOptions_DEFAULT_DEADLINE), [FetchOptions#DEFAULT_FOLLOW_REDIRECTS](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions#com_google_appengine_api_urlfetch_FetchOptions_DEFAULT_FOLLOW_REDIRECTS)

**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
