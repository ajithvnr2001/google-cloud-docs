---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.GetSentMessagesResponseOrBuilder
title: Interface MailStubServicePb.GetSentMessagesResponseOrBuilder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:38:27.589763+00:00
---

# Interface MailStubServicePb.GetSentMessagesResponseOrBuilder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailStubServicePb.GetSentMessagesResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface MailStubServicePb.GetSentMessagesResponseOrBuilder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static interface MailStubServicePb.GetSentMessagesResponseOrBuilder extends MessageOrBuilder

## Implements

com.google.protobuf.MessageOrBuilder

## Methods 

### getSentMessage(int arg0)
    
    
    public abstract MailServicePb.MailMessage getSentMessage(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MailMessage](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailMessage)` |   
  
### getSentMessageCount()
    
    
    public abstract int getSentMessageCount()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSentMessageList()
    
    
    public abstract List<MailServicePb.MailMessage> getSentMessageList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[MailMessage](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailMessage)>` |   
  
### getSentMessageOrBuilder(int arg0)
    
    
    public abstract MailServicePb.MailMessageOrBuilder getSentMessageOrBuilder(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MailMessageOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailMessageOrBuilder)` |   
  
### getSentMessageOrBuilderList()
    
    
    public abstract List<? extends MailServicePb.MailMessageOrBuilder> getSentMessageOrBuilderList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.appengine.api.mail.MailServicePb.MailMessageOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
