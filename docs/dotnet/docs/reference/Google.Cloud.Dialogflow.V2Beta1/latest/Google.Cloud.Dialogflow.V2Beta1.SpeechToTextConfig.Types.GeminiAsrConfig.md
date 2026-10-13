---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig.Types.GeminiAsrConfig
title: Google Cloud Dialogflow v2beta1 API - Class SpeechToTextConfig.Types.GeminiAsrConfig (1.0.0-beta33) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:49.746829+00:00
---

# Google Cloud Dialogflow v2beta1 API - Class SpeechToTextConfig.Types.GeminiAsrConfig (1.0.0-beta33)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig.Types.GeminiAsrConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2beta1 API - Class SpeechToTextConfig.Types.GeminiAsrConfig (1.0.0-beta33) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta33 (latest)  1.0.0-beta32 
    
    
    public sealed class SpeechToTextConfig.Types.GeminiAsrConfig : IMessage<SpeechToTextConfig.Types.GeminiAsrConfig>, IEquatable<SpeechToTextConfig.Types.GeminiAsrConfig>, IDeepCloneable<SpeechToTextConfig.Types.GeminiAsrConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2beta1 API class SpeechToTextConfig.Types.GeminiAsrConfig.

Configuration for using Gemini ASR models served via Vertex AI. This message is used to override the default Gemini ASR model or provide additional advanced parameters.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SpeechToTextConfig.Types.GeminiAsrConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SpeechToTextConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig.Types)[GeminiAsrConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig.Types.GeminiAsrConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SpeechToTextConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig.Types)[GeminiAsrConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig.Types.GeminiAsrConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SpeechToTextConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig.Types)[GeminiAsrConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig.Types.GeminiAsrConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1)

## Assembly

Google.Cloud.Dialogflow.V2Beta1.dll

## Constructors 

### GeminiAsrConfig()
    
    
    public GeminiAsrConfig()

### GeminiAsrConfig(GeminiAsrConfig)
    
    
    public GeminiAsrConfig(SpeechToTextConfig.Types.GeminiAsrConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SpeechToTextConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig.Types)[GeminiAsrConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig.Types.GeminiAsrConfig)`  
  
  
## Properties 

### EndOfSpeechSensitivity
    
    
    public SpeechToTextConfig.Types.GeminiAsrConfig.Types.EndSensitivity EndOfSpeechSensitivity { get; set; }

Optional. End of speech sensitivity.

**Property Value**  
---  
**Type** | **Description**  
`[SpeechToTextConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig.Types)[GeminiAsrConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig.Types.GeminiAsrConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig.Types.GeminiAsrConfig.Types)[EndSensitivity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig.Types.GeminiAsrConfig.Types.EndSensitivity)` |   
  
### ModelId
    
    
    public string ModelId { get; set; }

Optional. The Gemini ASR model ID used for transcription. This value overrides the default model ID configured on the server. Example: "gemini-3-flash-lite-asr-preview"

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PrefixPaddingMs
    
    
    public int PrefixPaddingMs { get; set; }

Optional. The required duration of detected speech before start-of-speech is committed.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### SilenceDurationMs
    
    
    public int SilenceDurationMs { get; set; }

Optional. The required duration of detected silence (or non-speech) before end-of-speech is committed.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### StartOfSpeechSensitivity
    
    
    public SpeechToTextConfig.Types.GeminiAsrConfig.Types.StartSensitivity StartOfSpeechSensitivity { get; set; }

Optional. Start of speech sensitivity.

**Property Value**  
---  
**Type** | **Description**  
`[SpeechToTextConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig.Types)[GeminiAsrConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig.Types.GeminiAsrConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig.Types.GeminiAsrConfig.Types)[StartSensitivity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechToTextConfig.Types.GeminiAsrConfig.Types.StartSensitivity)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
