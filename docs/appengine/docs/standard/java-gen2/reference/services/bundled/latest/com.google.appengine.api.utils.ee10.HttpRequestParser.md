---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.ee10.HttpRequestParser
title: Class HttpRequestParser (3.0.2) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:27:35.851850+00:00
---

# Class HttpRequestParser (3.0.2)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.ee10.HttpRequestParser

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)



Send feedback 

#  Class HttpRequestParser (3.0.2) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class HttpRequestParser

`HttpRequestParser` encapsulates helper methods used to parse incoming ` multipart/form-data` HTTP requests. Subclasses should use these methods to parse specific requests into useful data structures.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > HttpRequestParser

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

### getFieldName(BodyPart part)
    
    
    protected static String getFieldName(BodyPart part)

**Parameter**  
---  
**Name** | **Description**  
`part` | `[BodyPart](https://docs.oracle.com/javase/8/docs/api/javax/mail/BodyPart.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[MessagingException](https://docs.oracle.com/javase/8/docs/api/javax/mail/MessagingException.html)` |   
  
### getTextContent(BodyPart part)
    
    
    protected static String getTextContent(BodyPart part)

**Parameter**  
---  
**Name** | **Description**  
`part` | `[BodyPart](https://docs.oracle.com/javase/8/docs/api/javax/mail/BodyPart.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[MessagingException](https://docs.oracle.com/javase/8/docs/api/javax/mail/MessagingException.html)` |   
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseMultipartRequest(HttpServletRequest req)
    
    
    protected static MimeMultipart parseMultipartRequest(HttpServletRequest req)

Parse input stream of the given request into a MimeMultipart object.

**Parameter**  
---  
**Name** | **Description**  
`req` | `jakarta.servlet.http.HttpServletRequest`  
  
**Returns**  
---  
**Type** | **Description**  
`[MimeMultipart](https://docs.oracle.com/javase/8/docs/api/javax/mail/internet/MimeMultipart.html)` | A MimeMultipart object representing the POST data.  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | if the input stream cannot be read.  
`[MessagingException](https://docs.oracle.com/javase/8/docs/api/javax/mail/MessagingException.html)` | if the input stream cannot be read.  
  
## Constructors 

### HttpRequestParser()
    
    
    public HttpRequestParser()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-06 UTC."],[],[]] 
