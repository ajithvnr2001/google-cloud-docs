---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.StreamingSynthesisInput
title: Google Cloud Text-to-Speech v1 API - Class StreamingSynthesisInput (3.18.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:27.773120+00:00
---

# Google Cloud Text-to-Speech v1 API - Class StreamingSynthesisInput (3.18.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.StreamingSynthesisInput

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Text-to-Speech v1 API - Class StreamingSynthesisInput (3.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.18.0 (latest)  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class StreamingSynthesisInput : IMessage<StreamingSynthesisInput>, IEquatable<StreamingSynthesisInput>, IDeepCloneable<StreamingSynthesisInput>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Text-to-Speech v1 API class StreamingSynthesisInput.

Input to be synthesized.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > StreamingSynthesisInput

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[StreamingSynthesisInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.StreamingSynthesisInput), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[StreamingSynthesisInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.StreamingSynthesisInput), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[StreamingSynthesisInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.StreamingSynthesisInput), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.TextToSpeech.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1)

## Assembly

Google.Cloud.TextToSpeech.V1.dll

## Constructors 

### StreamingSynthesisInput()
    
    
    public StreamingSynthesisInput()

### StreamingSynthesisInput(StreamingSynthesisInput)
    
    
    public StreamingSynthesisInput(StreamingSynthesisInput other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[StreamingSynthesisInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.StreamingSynthesisInput)`  
  
  
## Properties 

### HasMarkup
    
    
    public bool HasMarkup { get; }

Gets whether the "markup" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasPrompt
    
    
    public bool HasPrompt { get; }

Gets whether the "prompt" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasText
    
    
    public bool HasText { get; }

Gets whether the "text" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InputSourceCase
    
    
    public StreamingSynthesisInput.InputSourceOneofCase InputSourceCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[StreamingSynthesisInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.StreamingSynthesisInput)[InputSourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.StreamingSynthesisInput.InputSourceOneofCase)` |   
  
### Markup
    
    
    public string Markup { get; set; }

Markup for Chirp 3: HD voices specifically. This field may not be used with any other voices.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MultiSpeakerMarkup
    
    
    public MultiSpeakerMarkup MultiSpeakerMarkup { get; set; }

Multi-speaker markup for Gemini TTS. This field may not be used with any other voices.

**Property Value**  
---  
**Type** | **Description**  
`[MultiSpeakerMarkup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.MultiSpeakerMarkup)` |   
  
### Prompt
    
    
    public string Prompt { get; set; }

This is system instruction supported only for controllable voice models.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Text
    
    
    public string Text { get; set; }

The raw text to be synthesized. It is recommended that each input contains complete, terminating sentences, which results in better prosody in the output audio.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
