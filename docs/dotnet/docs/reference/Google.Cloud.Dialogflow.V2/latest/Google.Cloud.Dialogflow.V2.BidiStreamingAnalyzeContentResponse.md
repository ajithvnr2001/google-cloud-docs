---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BidiStreamingAnalyzeContentResponse
title: Google Cloud Dialogflow v2 API - Class BidiStreamingAnalyzeContentResponse (4.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:58:14.151025+00:00
---

# Google Cloud Dialogflow v2 API - Class BidiStreamingAnalyzeContentResponse (4.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BidiStreamingAnalyzeContentResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2 API - Class BidiStreamingAnalyzeContentResponse (4.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.33.0 (latest)  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public sealed class BidiStreamingAnalyzeContentResponse : IMessage<BidiStreamingAnalyzeContentResponse>, IEquatable<BidiStreamingAnalyzeContentResponse>, IDeepCloneable<BidiStreamingAnalyzeContentResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2 API class BidiStreamingAnalyzeContentResponse.

The response message for [Participants.BidiStreamingAnalyzeContent][google.cloud.dialogflow.v2.Participants.BidiStreamingAnalyzeContent].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BidiStreamingAnalyzeContentResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BidiStreamingAnalyzeContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BidiStreamingAnalyzeContentResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BidiStreamingAnalyzeContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BidiStreamingAnalyzeContentResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BidiStreamingAnalyzeContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BidiStreamingAnalyzeContentResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2)

## Assembly

Google.Cloud.Dialogflow.V2.dll

## Constructors 

### BidiStreamingAnalyzeContentResponse()
    
    
    public BidiStreamingAnalyzeContentResponse()

### BidiStreamingAnalyzeContentResponse(BidiStreamingAnalyzeContentResponse)
    
    
    public BidiStreamingAnalyzeContentResponse(BidiStreamingAnalyzeContentResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BidiStreamingAnalyzeContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BidiStreamingAnalyzeContentResponse)`  
  
  
## Properties 

### AnalyzeContentResponse
    
    
    public AnalyzeContentResponse AnalyzeContentResponse { get; set; }

The agent response from analyze content.

**Property Value**  
---  
**Type** | **Description**  
`[AnalyzeContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnalyzeContentResponse)` |   
  
### BargeInSignal
    
    
    public BidiStreamingAnalyzeContentResponse.Types.BargeInSignal BargeInSignal { get; set; }

Indicate the user barge-in has been detected, and client should stop playing back the audio.

**Property Value**  
---  
**Type** | **Description**  
`[BidiStreamingAnalyzeContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BidiStreamingAnalyzeContentResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BidiStreamingAnalyzeContentResponse.Types)[BargeInSignal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BidiStreamingAnalyzeContentResponse.Types.BargeInSignal)` |   
  
### RecognitionResult
    
    
    public StreamingRecognitionResult RecognitionResult { get; set; }

The result of speech recognition.

**Property Value**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.StreamingRecognitionResult)` |   
  
### ResponseCase
    
    
    public BidiStreamingAnalyzeContentResponse.ResponseOneofCase ResponseCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[BidiStreamingAnalyzeContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BidiStreamingAnalyzeContentResponse)[ResponseOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BidiStreamingAnalyzeContentResponse.ResponseOneofCase)` |   
  
### TurnComplete
    
    
    public BidiStreamingAnalyzeContentResponse.Types.TurnComplete TurnComplete { get; set; }

Indicate that the turn is complete.

**Property Value**  
---  
**Type** | **Description**  
`[BidiStreamingAnalyzeContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BidiStreamingAnalyzeContentResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BidiStreamingAnalyzeContentResponse.Types)[TurnComplete](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.BidiStreamingAnalyzeContentResponse.Types.TurnComplete)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
