---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.StorageMessageOrBuilder
title: Interface StorageMessageOrBuilder (0.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:16.446333+00:00
---

# Interface StorageMessageOrBuilder (0.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.StorageMessageOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface StorageMessageOrBuilder (0.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.27.0 (latest)  0.23.0  0.22.0  0.21.0  0.19.0  0.16.0  0.15.0  0.13.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface StorageMessageOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getMessage()
    
    
    public abstract Message getMessage()

The message content.

`.google.cloud.geminidataanalytics.v1beta.Message message = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.Message)` | The message.  
  
### getMessageId()
    
    
    public abstract String getMessageId()

The unique resource name of a chat message.

`string message_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The messageId.  
  
### getMessageIdBytes()
    
    
    public abstract ByteString getMessageIdBytes()

The unique resource name of a chat message.

`string message_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for messageId.  
  
### getMessageOrBuilder()
    
    
    public abstract MessageOrBuilder getMessageOrBuilder()

The message content.

`.google.cloud.geminidataanalytics.v1beta.Message message = 2;`

**Returns**  
---  
**Type** | **Description**  
`[MessageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.MessageOrBuilder)` |   
  
### hasMessage()
    
    
    public abstract boolean hasMessage()

The message content.

`.google.cloud.geminidataanalytics.v1beta.Message message = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the message field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
