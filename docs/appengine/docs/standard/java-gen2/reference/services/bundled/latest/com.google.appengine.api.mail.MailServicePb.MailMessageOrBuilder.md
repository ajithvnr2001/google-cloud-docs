---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailMessageOrBuilder
title: Interface MailServicePb.MailMessageOrBuilder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:14:15.098866+00:00
---

# Interface MailServicePb.MailMessageOrBuilder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailMessageOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface MailServicePb.MailMessageOrBuilder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static interface MailServicePb.MailMessageOrBuilder extends MessageOrBuilder

## Implements

com.google.protobuf.MessageOrBuilder

## Methods 

### getAmpHtmlBody()
    
    
    public abstract String getAmpHtmlBody()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getAmpHtmlBodyBytes()
    
    
    public abstract ByteString getAmpHtmlBodyBytes()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getAttachment(int arg0)
    
    
    public abstract MailServicePb.MailAttachment getAttachment(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MailAttachment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailAttachment)` |   
  
### getAttachmentCount()
    
    
    public abstract int getAttachmentCount()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAttachmentList()
    
    
    public abstract List<MailServicePb.MailAttachment> getAttachmentList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[MailAttachment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailAttachment)>` |   
  
### getAttachmentOrBuilder(int arg0)
    
    
    public abstract MailServicePb.MailAttachmentOrBuilder getAttachmentOrBuilder(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MailAttachmentOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailAttachmentOrBuilder)` |   
  
### getAttachmentOrBuilderList()
    
    
    public abstract List<? extends MailServicePb.MailAttachmentOrBuilder> getAttachmentOrBuilderList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.appengine.api.mail.MailServicePb.MailAttachmentOrBuilder>` |   
  
### getBcc(int arg0)
    
    
    public abstract String getBcc(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getBccBytes(int arg0)
    
    
    public abstract ByteString getBccBytes(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getBccCount()
    
    
    public abstract int getBccCount()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBccList()
    
    
    public abstract List<String> getBccList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getCc(int arg0)
    
    
    public abstract String getCc(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getCcBytes(int arg0)
    
    
    public abstract ByteString getCcBytes(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getCcCount()
    
    
    public abstract int getCcCount()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCcList()
    
    
    public abstract List<String> getCcList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getHeader(int arg0)
    
    
    public abstract MailServicePb.MailHeader getHeader(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MailHeader](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailHeader)` |   
  
### getHeaderCount()
    
    
    public abstract int getHeaderCount()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getHeaderList()
    
    
    public abstract List<MailServicePb.MailHeader> getHeaderList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[MailHeader](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailHeader)>` |   
  
### getHeaderOrBuilder(int arg0)
    
    
    public abstract MailServicePb.MailHeaderOrBuilder getHeaderOrBuilder(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MailHeaderOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.mail.MailServicePb.MailHeaderOrBuilder)` |   
  
### getHeaderOrBuilderList()
    
    
    public abstract List<? extends MailServicePb.MailHeaderOrBuilder> getHeaderOrBuilderList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.appengine.api.mail.MailServicePb.MailHeaderOrBuilder>` |   
  
### getHtmlBody()
    
    
    public abstract String getHtmlBody()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getHtmlBodyBytes()
    
    
    public abstract ByteString getHtmlBodyBytes()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getReplyTo()
    
    
    public abstract String getReplyTo()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getReplyToBytes()
    
    
    public abstract ByteString getReplyToBytes()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getSender()
    
    
    public abstract String getSender()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getSenderBytes()
    
    
    public abstract ByteString getSenderBytes()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getSubject()
    
    
    public abstract String getSubject()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getSubjectBytes()
    
    
    public abstract ByteString getSubjectBytes()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getTextBody()
    
    
    public abstract String getTextBody()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getTextBodyBytes()
    
    
    public abstract ByteString getTextBodyBytes()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getTo(int arg0)
    
    
    public abstract String getTo(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getToBytes(int arg0)
    
    
    public abstract ByteString getToBytes(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getToCount()
    
    
    public abstract int getToCount()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getToList()
    
    
    public abstract List<String> getToList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### hasAmpHtmlBody()
    
    
    public abstract boolean hasAmpHtmlBody()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasHtmlBody()
    
    
    public abstract boolean hasHtmlBody()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasReplyTo()
    
    
    public abstract boolean hasReplyTo()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasSender()
    
    
    public abstract boolean hasSender()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasSubject()
    
    
    public abstract boolean hasSubject()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasTextBody()
    
    
    public abstract boolean hasTextBody()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
