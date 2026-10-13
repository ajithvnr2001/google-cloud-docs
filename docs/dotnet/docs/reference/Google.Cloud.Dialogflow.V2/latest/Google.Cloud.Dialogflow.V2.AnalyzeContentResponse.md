---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnalyzeContentResponse
title: Google Cloud Dialogflow v2 API - Class AnalyzeContentResponse (4.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:58:04.385637+00:00
---

# Google Cloud Dialogflow v2 API - Class AnalyzeContentResponse (4.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnalyzeContentResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2 API - Class AnalyzeContentResponse (4.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.33.0 (latest)  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public sealed class AnalyzeContentResponse : IMessage<AnalyzeContentResponse>, IEquatable<AnalyzeContentResponse>, IDeepCloneable<AnalyzeContentResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2 API class AnalyzeContentResponse.

The response message for [Participants.AnalyzeContent][google.cloud.dialogflow.v2.Participants.AnalyzeContent].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AnalyzeContentResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AnalyzeContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnalyzeContentResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AnalyzeContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnalyzeContentResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AnalyzeContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnalyzeContentResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2)

## Assembly

Google.Cloud.Dialogflow.V2.dll

## Constructors 

### AnalyzeContentResponse()
    
    
    public AnalyzeContentResponse()

### AnalyzeContentResponse(AnalyzeContentResponse)
    
    
    public AnalyzeContentResponse(AnalyzeContentResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AnalyzeContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnalyzeContentResponse)`  
  
  
## Properties 

### AutomatedAgentReply
    
    
    public AutomatedAgentReply AutomatedAgentReply { get; set; }

Only set if a Dialogflow automated agent has responded. Note that in [AutomatedAgentReply.DetectIntentResponse][], [Sessions.DetectIntentResponse.output_audio][] and [Sessions.DetectIntentResponse.output_audio_config][] are always empty, use [reply_audio][google.cloud.dialogflow.v2.AnalyzeContentResponse.reply_audio] instead.

**Property Value**  
---  
**Type** | **Description**  
`[AutomatedAgentReply](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AutomatedAgentReply)` |   
  
### DtmfParameters
    
    
    public DtmfParameters DtmfParameters { get; set; }

Indicates the parameters of DTMF.

**Property Value**  
---  
**Type** | **Description**  
`[DtmfParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.DtmfParameters)` |   
  
### EndUserSuggestionResults
    
    
    public RepeatedField<SuggestionResult> EndUserSuggestionResults { get; }

The suggestions for end user. The order is the same as [HumanAgentAssistantConfig.SuggestionConfig.feature_configs][google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionConfig.feature_configs] of [HumanAgentAssistantConfig.end_user_suggestion_config][google.cloud.dialogflow.v2.HumanAgentAssistantConfig.end_user_suggestion_config].

Same as human_agent_suggestion_results, any failure of Agent Assist features will not lead to the overall failure of an AnalyzeContent API call. Instead, the features will fail silently with the error field set in the corresponding SuggestionResult.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SuggestionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SuggestionResult)` |   
  
### HumanAgentSuggestionResults
    
    
    public RepeatedField<SuggestionResult> HumanAgentSuggestionResults { get; }

The suggestions for most recent human agent. The order is the same as [HumanAgentAssistantConfig.SuggestionConfig.feature_configs][google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionConfig.feature_configs] of [HumanAgentAssistantConfig.human_agent_suggestion_config][google.cloud.dialogflow.v2.HumanAgentAssistantConfig.human_agent_suggestion_config].

Note that any failure of Agent Assist features will not lead to the overall failure of an AnalyzeContent API call. Instead, the features will fail silently with the error field set in the corresponding SuggestionResult.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SuggestionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SuggestionResult)` |   
  
### Message
    
    
    public Message Message { get; set; }

Message analyzed by CCAI.

**Property Value**  
---  
**Type** | **Description**  
`[Message](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Message)` |   
  
### ReplyAudio
    
    
    public OutputAudio ReplyAudio { get; set; }

The audio data bytes encoded as specified in the request. This field is set if:

  * `reply_audio_config` was specified in the request, or
  * The automated agent responded with audio to play to the user. In such case, `reply_audio.config` contains settings used to synthesize the speech.



In some scenarios, multiple output audio fields may be present in the response structure. In these cases, only the top-most-level audio output has content.

**Property Value**  
---  
**Type** | **Description**  
`[OutputAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.OutputAudio)` |   
  
### ReplyText
    
    
    public string ReplyText { get; set; }

The output text content. This field is set if the automated agent responded with text to show to the user.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
