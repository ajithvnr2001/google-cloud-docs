---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService.Attachment
title: Class MailService.Attachment (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:17:21.735023+00:00
---

# Class MailService.Attachment (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService.Attachment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class MailService.Attachment (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static class MailService.Attachment

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > MailService.Attachment

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

### Attachment(String fileName, byte[] data)
    
    
    public Attachment(String fileName, byte[] data)

Attachments are an optional part of messages, but if present, all information about them must be provided.

**Parameters**  
---  
**Name** | **Description**  
`fileName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The attachment must have a filename associated with it. The extension on that filename must be present and not blocked, or there will be a failure at send time.  
`data` | `byte[]`  
An array with arbitrary byte content. The array must be be present, but may be of zero length.  
  
### Attachment(String fileName, byte[] data, @Nullable String contentID)
    
    
    public Attachment(String fileName, byte[] data, @Nullable String contentID)

Attachments are an optional part of messages, but if present, all information about them must be provided.

**Parameters**  
---  
**Name** | **Description**  
`fileName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The attachment must have a filename associated with it. The extension on that filename must be present and blocked, or there will be a failure at send time.  
`data` | `byte[]`  
An array with arbitrary byte content. The array must be be present, but may be of zero length.  
`contentID` | `[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)`  
The attachment's content ID. May be null.  
  
## Methods 

### getContentID()
    
    
    public @Nullable String getContentID()

**Returns**  
---  
**Type** | **Description**  
`[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)` |   
  
### getData()
    
    
    public byte[] getData()

Gets the content of this attachment.

**Returns**  
---  
**Type** | **Description**  
`byte[]` | The raw data of this attachment.  
  
### getFileName()
    
    
    public String getFileName()

Gets the file name of this attachment.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The file name of this attachment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
