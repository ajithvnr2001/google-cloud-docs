---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.VoiceCloneParams
title: Google Cloud Text-to-Speech v1 API - Class VoiceCloneParams (3.18.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:14.728119+00:00
---

# Google Cloud Text-to-Speech v1 API - Class VoiceCloneParams (3.18.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.VoiceCloneParams

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Text-to-Speech v1 API - Class VoiceCloneParams (3.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.18.0 (latest)  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class VoiceCloneParams : IMessage<VoiceCloneParams>, IEquatable<VoiceCloneParams>, IDeepCloneable<VoiceCloneParams>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Text-to-Speech v1 API class VoiceCloneParams.

The configuration of Voice Clone feature.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > VoiceCloneParams

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[VoiceCloneParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.VoiceCloneParams), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[VoiceCloneParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.VoiceCloneParams), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[VoiceCloneParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.VoiceCloneParams), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.TextToSpeech.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1)

## Assembly

Google.Cloud.TextToSpeech.V1.dll

## Constructors 

### VoiceCloneParams()
    
    
    public VoiceCloneParams()

### VoiceCloneParams(VoiceCloneParams)
    
    
    public VoiceCloneParams(VoiceCloneParams other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[VoiceCloneParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.VoiceCloneParams)`  
  
  
## Properties 

### VoiceCloningKey
    
    
    public string VoiceCloningKey { get; set; }

Required. Created by GenerateVoiceCloningKey.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
