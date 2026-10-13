---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingReactiveCompanionSuggestionsResponse
title: Google Cloud Dialogflow v2beta1 API - Class StreamingReactiveCompanionSuggestionsResponse (1.0.0-beta33) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:39:26.003882+00:00
---

# Google Cloud Dialogflow v2beta1 API - Class StreamingReactiveCompanionSuggestionsResponse (1.0.0-beta33)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingReactiveCompanionSuggestionsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2beta1 API - Class StreamingReactiveCompanionSuggestionsResponse (1.0.0-beta33) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta33 (latest)  1.0.0-beta32 
    
    
    public sealed class StreamingReactiveCompanionSuggestionsResponse : IMessage<StreamingReactiveCompanionSuggestionsResponse>, IEquatable<StreamingReactiveCompanionSuggestionsResponse>, IDeepCloneable<StreamingReactiveCompanionSuggestionsResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2beta1 API class StreamingReactiveCompanionSuggestionsResponse.

The response message for [Participants.StreamingReactiveCompanionSuggestions][google.cloud.dialogflow.v2beta1.Participants.StreamingReactiveCompanionSuggestions].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > StreamingReactiveCompanionSuggestionsResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[StreamingReactiveCompanionSuggestionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingReactiveCompanionSuggestionsResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[StreamingReactiveCompanionSuggestionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingReactiveCompanionSuggestionsResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[StreamingReactiveCompanionSuggestionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingReactiveCompanionSuggestionsResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1)

## Assembly

Google.Cloud.Dialogflow.V2Beta1.dll

## Constructors 

### StreamingReactiveCompanionSuggestionsResponse()
    
    
    public StreamingReactiveCompanionSuggestionsResponse()

### StreamingReactiveCompanionSuggestionsResponse(StreamingReactiveCompanionSuggestionsResponse)
    
    
    public StreamingReactiveCompanionSuggestionsResponse(StreamingReactiveCompanionSuggestionsResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[StreamingReactiveCompanionSuggestionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingReactiveCompanionSuggestionsResponse)`  
  
  
## Properties 

### AnswerRecord
    
    
    public string AnswerRecord { get; set; }

Output only. Only set when `is_final` is `true` and conversational turn processing completes. The final answer record representing the completed suggestion. Only present in the last chunk of the completed response.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AnswerRecordAsAnswerRecordName
    
    
    public AnswerRecordName AnswerRecordAsAnswerRecordName { get; set; }

[AnswerRecordName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecordName)-typed view over the [AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingReactiveCompanionSuggestionsResponse#Google_Cloud_Dialogflow_V2Beta1_StreamingReactiveCompanionSuggestionsResponse_AnswerRecord) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AnswerRecordName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecordName)` |   
  
### HasResponseChunk
    
    
    public bool HasResponseChunk { get; }

Gets whether the "response_chunk" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IntermediateToolCallEvents
    
    
    public ToolCallEvents IntermediateToolCallEvents { get; set; }

Output only. Captures intermediate tool call events that occur during the execution of the reactive query turn. Note that conversational messages within tool calls are displayed within the tool cards and hence are not accumulated within the `reactive_mode_final_response.response` string.

**Property Value**  
---  
**Type** | **Description**  
`[ToolCallEvents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ToolCallEvents)` |   
  
### IsFinal
    
    
    public bool IsFinal { get; set; }

Output only. Indicates whether the client/UI can accept a new query for reactive chat. When `is_final` is `true`, the reactive chat interface is unblocked and ready to receive new human agent queries. For synchronous turns, this is set to `true` on the final response chunk. For asynchronous tool calls running in the background, this is set to `true` on the intermediate trigger chunk to unblock the UI while the background tool execution is in progress.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ReactiveModeFinalResponse
    
    
    public StreamingReactiveCompanionSuggestionsResponse.Types.ReactiveModeResponse ReactiveModeFinalResponse { get; set; }

Output only. The final response from the reactive mode capturing the entire accumulated streaming response, grounding metadata, and tool calls. Only set when `is_final` is `true` and conversational processing for the query turn completes.

**Property Value**  
---  
**Type** | **Description**  
`[StreamingReactiveCompanionSuggestionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingReactiveCompanionSuggestionsResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingReactiveCompanionSuggestionsResponse.Types)[ReactiveModeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingReactiveCompanionSuggestionsResponse.Types.ReactiveModeResponse)` |   
  
### ResponseCase
    
    
    public StreamingReactiveCompanionSuggestionsResponse.ResponseOneofCase ResponseCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[StreamingReactiveCompanionSuggestionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingReactiveCompanionSuggestionsResponse)[ResponseOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingReactiveCompanionSuggestionsResponse.ResponseOneofCase)` |   
  
### ResponseChunk
    
    
    public string ResponseChunk { get; set; }

Streamed response text chunks.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SendTime
    
    
    public Timestamp SendTime { get; set; }

The timestamp when the response chunk was sent by the service.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Status
    
    
    public Status Status { get; set; }

Status of the response for the current query. If set and non-ok, indicates an error occurred during processing of the current query, or confirms that a requested cancellation has successfully completed (status code CANCELLED).

**Property Value**  
---  
**Type** | **Description**  
`[Status](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Status.html)` |   
  
### TextMessageId
    
    
    public string TextMessageId { get; set; }

Required. Output only. The unique message identifier corresponding to the human agent query that generated this response chunk.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
