---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.TranscriptNormalization
title: Cloud Speech-to-Text v2 API - Class TranscriptNormalization (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:16.525201+00:00
---

# Cloud Speech-to-Text v2 API - Class TranscriptNormalization (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.TranscriptNormalization

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Speech-to-Text v2 API - Class TranscriptNormalization (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.TranscriptNormalization)
  * [ 1.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.7.0/Google.Cloud.Speech.V2.TranscriptNormalization)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.6.0/Google.Cloud.Speech.V2.TranscriptNormalization)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.5.0/Google.Cloud.Speech.V2.TranscriptNormalization)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.4.0/Google.Cloud.Speech.V2.TranscriptNormalization)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.3.0/Google.Cloud.Speech.V2.TranscriptNormalization)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.2.0/Google.Cloud.Speech.V2.TranscriptNormalization)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.1.0/Google.Cloud.Speech.V2.TranscriptNormalization)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.0.0/Google.Cloud.Speech.V2.TranscriptNormalization)


    
    
    public sealed class TranscriptNormalization : IMessage<TranscriptNormalization>, IEquatable<TranscriptNormalization>, IDeepCloneable<TranscriptNormalization>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Speech-to-Text v2 API class TranscriptNormalization.

Transcription normalization configuration. Use transcription normalization to automatically replace parts of the transcript with phrases of your choosing. For StreamingRecognize, this normalization only applies to stable partial transcripts (stability > 0.8) and final transcripts.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > TranscriptNormalization

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[TranscriptNormalization](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.TranscriptNormalization), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[TranscriptNormalization](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.TranscriptNormalization), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[TranscriptNormalization](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.TranscriptNormalization), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Speech.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2)

## Assembly

Google.Cloud.Speech.V2.dll

## Constructors 

### TranscriptNormalization()
    
    
    public TranscriptNormalization()

### TranscriptNormalization(TranscriptNormalization)
    
    
    public TranscriptNormalization(TranscriptNormalization other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[TranscriptNormalization](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.TranscriptNormalization)`  
  
  
## Properties 

### Entries
    
    
    public RepeatedField<TranscriptNormalization.Types.Entry> Entries { get; }

A list of replacement entries. We will perform replacement with one entry at a time. For example, the second entry in ["cat" => "dog", "mountain cat" => "mountain dog"] will never be applied because we will always process the first entry before it. At most 100 entries.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[TranscriptNormalization](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.TranscriptNormalization)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.TranscriptNormalization.Types)[Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.TranscriptNormalization.Types.Entry)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
