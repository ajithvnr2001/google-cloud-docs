---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService
title: Interface MailService (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:13:38.371773+00:00
---

# Interface MailService (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface MailService (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface MailService

The `MailService` provides a way for user code to send emails to arbitrary destinations.

## Methods 

### send(MailService.Message message)
    
    
    public abstract void send(MailService.Message message)

Sends a mail that has been prepared in a MailService.Message. 

The message will be delivered asynchronously, and delivery problems will result in a bounce to the specified sender. 

`Sender` and at least one of the collections for `to, cc, bcc` must not be `null`.

**Parameter**  
---  
**Name** | **Description**  
`message` | `[MailService.Message](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService.Message)`  
The message to be sent.  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | when incorrect arguments are passed.  
  
### sendToAdmins(MailService.Message message)
    
    
    public abstract void sendToAdmins(MailService.Message message)

Send an email alert to all admins of an application. 

The message will be delivered asynchronously, and delivery problems will result in a bounce to the admins. 

The content of the `to, cc, bcc` fields should be ` null`.

**Parameter**  
---  
**Name** | **Description**  
`message` | `[MailService.Message](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailService.Message)`  
The message to be sent.  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | when incorrect arguments are passed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
