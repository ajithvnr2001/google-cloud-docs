---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SuggestSmartRepliesResponse
title: Google Cloud Dialogflow v2 API - Class SuggestSmartRepliesResponse (4.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:18.266658+00:00
---

# Google Cloud Dialogflow v2 API - Class SuggestSmartRepliesResponse (4.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SuggestSmartRepliesResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2 API - Class SuggestSmartRepliesResponse (4.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.33.0 (latest)  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public sealed class SuggestSmartRepliesResponse : IMessage<SuggestSmartRepliesResponse>, IEquatable<SuggestSmartRepliesResponse>, IDeepCloneable<SuggestSmartRepliesResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2 API class SuggestSmartRepliesResponse.

The response message for [Participants.SuggestSmartReplies][google.cloud.dialogflow.v2.Participants.SuggestSmartReplies].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SuggestSmartRepliesResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SuggestSmartRepliesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SuggestSmartRepliesResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SuggestSmartRepliesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SuggestSmartRepliesResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SuggestSmartRepliesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SuggestSmartRepliesResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2)

## Assembly

Google.Cloud.Dialogflow.V2.dll

## Constructors 

### SuggestSmartRepliesResponse()
    
    
    public SuggestSmartRepliesResponse()

### SuggestSmartRepliesResponse(SuggestSmartRepliesResponse)
    
    
    public SuggestSmartRepliesResponse(SuggestSmartRepliesResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SuggestSmartRepliesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SuggestSmartRepliesResponse)`  
  
  
## Properties 

### ContextSize
    
    
    public int ContextSize { get; set; }

Number of messages prior to and including [latest_message][google.cloud.dialogflow.v2.SuggestSmartRepliesResponse.latest_message] to compile the suggestion. It may be smaller than the [SuggestSmartRepliesRequest.context_size][google.cloud.dialogflow.v2.SuggestSmartRepliesRequest.context_size] field in the request if there aren't that many messages in the conversation.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### LatestMessage
    
    
    public string LatestMessage { get; set; }

The name of the latest conversation message used to compile suggestion for.

Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LatestMessageAsMessageName
    
    
    public MessageName LatestMessageAsMessageName { get; set; }

[MessageName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.MessageName)-typed view over the [LatestMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SuggestSmartRepliesResponse#Google_Cloud_Dialogflow_V2_SuggestSmartRepliesResponse_LatestMessage) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[MessageName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.MessageName)` |   
  
### SmartReplyAnswers
    
    
    public RepeatedField<SmartReplyAnswer> SmartReplyAnswers { get; }

Output only. Multiple reply options provided by smart reply service. The order is based on the rank of the model prediction. The maximum number of the returned replies is set in SmartReplyConfig.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SmartReplyAnswer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SmartReplyAnswer)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
