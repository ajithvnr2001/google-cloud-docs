---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.GenerateStatelessSummaryResponseOrBuilder
title: Interface GenerateStatelessSummaryResponseOrBuilder (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:39.809121+00:00
---

# Interface GenerateStatelessSummaryResponseOrBuilder (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.GenerateStatelessSummaryResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GenerateStatelessSummaryResponseOrBuilder (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 
    
    
    public interface GenerateStatelessSummaryResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getContextSize()
    
    
    public abstract int getContextSize()

Number of messages prior to and including [last_conversation_message][] used to compile the suggestion. It may be smaller than the [GenerateStatelessSummaryRequest.context_size][] field in the request if there weren't that many messages in the conversation.

`int32 context_size = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The contextSize.  
  
### getLatestMessage()
    
    
    public abstract String getLatestMessage()

The name of the latest conversation message used as context for compiling suggestion. The format is specific to the user and the names of the messages provided.

`string latest_message = 2 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The latestMessage.  
  
### getLatestMessageBytes()
    
    
    public abstract ByteString getLatestMessageBytes()

The name of the latest conversation message used as context for compiling suggestion. The format is specific to the user and the names of the messages provided.

`string latest_message = 2 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for latestMessage.  
  
### getSummary()
    
    
    public abstract GenerateStatelessSummaryResponse.Summary getSummary()

Generated summary.

`.google.cloud.dialogflow.v2beta1.GenerateStatelessSummaryResponse.Summary summary = 1; `

**Returns**  
---  
**Type** | **Description**  
`[GenerateStatelessSummaryResponse.Summary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.GenerateStatelessSummaryResponse.Summary)` | The summary.  
  
### getSummaryOrBuilder()
    
    
    public abstract GenerateStatelessSummaryResponse.SummaryOrBuilder getSummaryOrBuilder()

Generated summary.

`.google.cloud.dialogflow.v2beta1.GenerateStatelessSummaryResponse.Summary summary = 1; `

**Returns**  
---  
**Type** | **Description**  
`[GenerateStatelessSummaryResponse.SummaryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.GenerateStatelessSummaryResponse.SummaryOrBuilder)` |   
  
### hasSummary()
    
    
    public abstract boolean hasSummary()

Generated summary.

`.google.cloud.dialogflow.v2beta1.GenerateStatelessSummaryResponse.Summary summary = 1; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the summary field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
