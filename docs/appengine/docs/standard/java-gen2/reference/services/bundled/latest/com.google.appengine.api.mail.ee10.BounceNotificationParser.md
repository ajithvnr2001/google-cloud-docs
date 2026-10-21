---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.ee10.BounceNotificationParser
title: Class BounceNotificationParser (3.0.2) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:03:46.420399+00:00
---

# Class BounceNotificationParser (3.0.2)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.ee10.BounceNotificationParser

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)



Send feedback 

#  Class BounceNotificationParser (3.0.2) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class BounceNotificationParser extends HttpRequestParser

**Deprecated.** _as of version 3.0, use[com.google.appengine.api.mail.jakarta.BounceNotificationParser](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.jakarta.BounceNotificationParser) instead._

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [HttpRequestParser](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.ee10.HttpRequestParser) > BounceNotificationParser

## Inherited Members

[HttpRequestParser.getFieldName(BodyPart)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.ee10.HttpRequestParser#com_google_appengine_api_utils_ee10_HttpRequestParser_getFieldName_javax_mail_BodyPart_)

[HttpRequestParser.getTextContent(BodyPart)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.ee10.HttpRequestParser#com_google_appengine_api_utils_ee10_HttpRequestParser_getTextContent_javax_mail_BodyPart_)

[HttpRequestParser.parseMultipartRequest(HttpServletRequest)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.ee10.HttpRequestParser#com_google_appengine_api_utils_ee10_HttpRequestParser_parseMultipartRequest_jakarta_servlet_http_HttpServletRequest_)

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

### parse(HttpServletRequest request) (deprecated)
    
    
    public static BounceNotification parse(HttpServletRequest request)

Parse the POST data of the given request to get details about the bounce notification.

**Parameter**  
---  
**Name** | **Description**  
`request` | `jakarta.servlet.http.HttpServletRequest`  
The HttpServletRequest whose POST data should be parsed.  
**Returns**  
---  
**Type** | **Description**  
`[BounceNotification](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.BounceNotification)` | a BounceNotification  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
`[MessagingException](https://docs.oracle.com/javase/8/docs/api/javax/mail/MessagingException.html)` |   
  
## Constructors 

### BounceNotificationParser() (deprecated)
    
    
    public BounceNotificationParser()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-06 UTC."],[],[]] 
