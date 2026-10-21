---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.BounceNotification.DetailsBuilder
title: Class BounceNotification.DetailsBuilder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:33:28.412374+00:00
---

# Class BounceNotification.DetailsBuilder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.BounceNotification.DetailsBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class BounceNotification.DetailsBuilder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static class BounceNotification.DetailsBuilder

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BounceNotification.DetailsBuilder

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

### DetailsBuilder()
    
    
    public DetailsBuilder()

## Methods 

### build()
    
    
    public BounceNotification.Details build()

**Returns**  
---  
**Type** | **Description**  
`[BounceNotification.Details](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.BounceNotification.Details)` |   
  
### withBcc(@Nullable String bcc)
    
    
    public BounceNotification.DetailsBuilder withBcc(@Nullable String bcc)

**Parameter**  
---  
**Name** | **Description**  
`bcc` | `[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BounceNotification.DetailsBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.BounceNotification.DetailsBuilder)` |   
  
### withCc(@Nullable String cc)
    
    
    public BounceNotification.DetailsBuilder withCc(@Nullable String cc)

**Parameter**  
---  
**Name** | **Description**  
`cc` | `[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BounceNotification.DetailsBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.BounceNotification.DetailsBuilder)` |   
  
### withFrom(@Nullable String from)
    
    
    public BounceNotification.DetailsBuilder withFrom(@Nullable String from)

**Parameter**  
---  
**Name** | **Description**  
`from` | `[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BounceNotification.DetailsBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.BounceNotification.DetailsBuilder)` |   
  
### withSubject(@Nullable String subject)
    
    
    public BounceNotification.DetailsBuilder withSubject(@Nullable String subject)

**Parameter**  
---  
**Name** | **Description**  
`subject` | `[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BounceNotification.DetailsBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.BounceNotification.DetailsBuilder)` |   
  
### withText(@Nullable String text)
    
    
    public BounceNotification.DetailsBuilder withText(@Nullable String text)

**Parameter**  
---  
**Name** | **Description**  
`text` | `[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BounceNotification.DetailsBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.BounceNotification.DetailsBuilder)` |   
  
### withTo(@Nullable String to)
    
    
    public BounceNotification.DetailsBuilder withTo(@Nullable String to)

**Parameter**  
---  
**Name** | **Description**  
`to` | `[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BounceNotification.DetailsBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.BounceNotification.DetailsBuilder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
