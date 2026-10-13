---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnalyzeContentRequest
title: Google Cloud Dialogflow v2 API - Class AnalyzeContentRequest (4.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:58:04.535125+00:00
---

# Google Cloud Dialogflow v2 API - Class AnalyzeContentRequest (4.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnalyzeContentRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2 API - Class AnalyzeContentRequest (4.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.33.0 (latest)  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public sealed class AnalyzeContentRequest : IMessage<AnalyzeContentRequest>, IEquatable<AnalyzeContentRequest>, IDeepCloneable<AnalyzeContentRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2 API class AnalyzeContentRequest.

The request message for [Participants.AnalyzeContent][google.cloud.dialogflow.v2.Participants.AnalyzeContent].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AnalyzeContentRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AnalyzeContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnalyzeContentRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AnalyzeContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnalyzeContentRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AnalyzeContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnalyzeContentRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2)

## Assembly

Google.Cloud.Dialogflow.V2.dll

## Constructors 

### AnalyzeContentRequest()
    
    
    public AnalyzeContentRequest()

### AnalyzeContentRequest(AnalyzeContentRequest)
    
    
    public AnalyzeContentRequest(AnalyzeContentRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AnalyzeContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnalyzeContentRequest)`  
  
  
## Properties 

### AssistQueryParams
    
    
    public AssistQueryParameters AssistQueryParams { get; set; }

Parameters for a human assist query.

**Property Value**  
---  
**Type** | **Description**  
`[AssistQueryParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AssistQueryParameters)` |   
  
### AudioInput
    
    
    public AudioInput AudioInput { get; set; }

The natural language speech audio to be processed.

**Property Value**  
---  
**Type** | **Description**  
`[AudioInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AudioInput)` |   
  
### CxParameters
    
    
    public Struct CxParameters { get; set; }

Additional parameters to be put into Dialogflow CX session parameters. To remove a parameter from the session, clients should explicitly set the parameter value to null.

Note: this field should only be used if you are connecting to a Dialogflow CX agent.

**Property Value**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` |   
  
### EventInput
    
    
    public EventInput EventInput { get; set; }

An input event to send to Dialogflow.

**Property Value**  
---  
**Type** | **Description**  
`[EventInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.EventInput)` |   
  
### InputCase
    
    
    public AnalyzeContentRequest.InputOneofCase InputCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[AnalyzeContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnalyzeContentRequest)[InputOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnalyzeContentRequest.InputOneofCase)` |   
  
### Participant
    
    
    public string Participant { get; set; }

Required. The name of the participant this text comes from. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParticipantAsParticipantName
    
    
    public ParticipantName ParticipantAsParticipantName { get; set; }

[ParticipantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ParticipantName)-typed view over the [Participant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnalyzeContentRequest#Google_Cloud_Dialogflow_V2_AnalyzeContentRequest_Participant) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ParticipantName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ParticipantName)` |   
  
### QueryParams
    
    
    public QueryParameters QueryParams { get; set; }

Parameters for a Dialogflow virtual-agent query.

**Property Value**  
---  
**Type** | **Description**  
`[QueryParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.QueryParameters)` |   
  
### ReplyAudioConfig
    
    
    public OutputAudioConfig ReplyAudioConfig { get; set; }

Speech synthesis configuration. The speech synthesis settings for a virtual agent that may be configured for the associated conversation profile are not used when calling AnalyzeContent. If this configuration is not supplied, speech synthesis is disabled.

**Property Value**  
---  
**Type** | **Description**  
`[OutputAudioConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.OutputAudioConfig)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if a `request_id` is provided.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SuggestionInput
    
    
    public SuggestionInput SuggestionInput { get; set; }

An input representing the selection of a suggestion.

**Property Value**  
---  
**Type** | **Description**  
`[SuggestionInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SuggestionInput)` |   
  
### TextInput
    
    
    public TextInput TextInput { get; set; }

The natural language text to be processed.

**Property Value**  
---  
**Type** | **Description**  
`[TextInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.TextInput)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
