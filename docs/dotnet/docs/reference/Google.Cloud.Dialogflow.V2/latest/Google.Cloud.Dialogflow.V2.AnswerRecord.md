---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnswerRecord
title: Google Cloud Dialogflow v2 API - Class AnswerRecord (4.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:58:06.718937+00:00
---

# Google Cloud Dialogflow v2 API - Class AnswerRecord (4.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnswerRecord

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2 API - Class AnswerRecord (4.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.33.0 (latest)  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public sealed class AnswerRecord : IMessage<AnswerRecord>, IEquatable<AnswerRecord>, IDeepCloneable<AnswerRecord>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2 API class AnswerRecord.

Answer records are records to manage answer history and feedbacks for Dialogflow.

Currently, answer record includes:

  * human agent assistant article suggestion
  * human agent assistant faq article



It doesn't include:

  * `DetectIntent` intent matching
  * `DetectIntent` knowledge



Answer records are not related to the conversation history in the Dialogflow Console. A Record is generated even when the end-user disables conversation history in the console. Records are created when there's a human agent assistant suggestion generated.

A typical workflow for customers provide feedback to an answer is:

  1. For human agent assistant, customers get suggestion via ListSuggestions API. Together with the answers, [AnswerRecord.name][google.cloud.dialogflow.v2.AnswerRecord.name] are returned to the customers.
  2. The customer uses the [AnswerRecord.name][google.cloud.dialogflow.v2.AnswerRecord.name] to call the [AnswerRecords.UpdateAnswerRecord][google.cloud.dialogflow.v2.AnswerRecords.UpdateAnswerRecord] method to send feedback about a specific answer that they believe is wrong.



## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AnswerRecord

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnswerRecord), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnswerRecord), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnswerRecord), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2)

## Assembly

Google.Cloud.Dialogflow.V2.dll

## Constructors 

### AnswerRecord()
    
    
    public AnswerRecord()

### AnswerRecord(AnswerRecord)
    
    
    public AnswerRecord(AnswerRecord other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnswerRecord)`  
  
  
## Properties 

### AgentAssistantRecord
    
    
    public AgentAssistantRecord AgentAssistantRecord { get; set; }

Output only. The record for human agent assistant.

**Property Value**  
---  
**Type** | **Description**  
`[AgentAssistantRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentAssistantRecord)` |   
  
### AnswerFeedback
    
    
    public AnswerFeedback AnswerFeedback { get; set; }

Required. The AnswerFeedback for this record. You can set this with [AnswerRecords.UpdateAnswerRecord][google.cloud.dialogflow.v2.AnswerRecords.UpdateAnswerRecord] in order to give us feedback about this answer.

**Property Value**  
---  
**Type** | **Description**  
`[AnswerFeedback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnswerFeedback)` |   
  
### AnswerRecordName
    
    
    public AnswerRecordName AnswerRecordName { get; set; }

[AnswerRecordName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnswerRecordName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnswerRecord#Google_Cloud_Dialogflow_V2_AnswerRecord_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AnswerRecordName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnswerRecordName)` |   
  
### Name
    
    
    public string Name { get; set; }

The unique identifier of this answer record. Format: `projects/<Project ID>/locations/<Location ID>/answerRecords/<Answer Record ID>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RecordCase
    
    
    public AnswerRecord.RecordOneofCase RecordCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnswerRecord)[RecordOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnswerRecord.RecordOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
