---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.CustomPronunciations
title: Google Cloud Text-to-Speech v1 API - Class CustomPronunciations (3.18.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:53:07.227834+00:00
---

# Google Cloud Text-to-Speech v1 API - Class CustomPronunciations (3.18.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.CustomPronunciations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Text-to-Speech v1 API - Class CustomPronunciations (3.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.18.0 (latest)  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class CustomPronunciations : IMessage<CustomPronunciations>, IEquatable<CustomPronunciations>, IDeepCloneable<CustomPronunciations>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Text-to-Speech v1 API class CustomPronunciations.

A collection of pronunciation customizations.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CustomPronunciations

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CustomPronunciations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.CustomPronunciations), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CustomPronunciations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.CustomPronunciations), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CustomPronunciations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.CustomPronunciations), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.TextToSpeech.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1)

## Assembly

Google.Cloud.TextToSpeech.V1.dll

## Constructors 

### CustomPronunciations()
    
    
    public CustomPronunciations()

### CustomPronunciations(CustomPronunciations)
    
    
    public CustomPronunciations(CustomPronunciations other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CustomPronunciations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.CustomPronunciations)`  
  
  
## Properties 

### Pronunciations
    
    
    public RepeatedField<CustomPronunciationParams> Pronunciations { get; }

The pronunciation customizations are applied.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[CustomPronunciationParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1/latest/Google.Cloud.TextToSpeech.V1.CustomPronunciationParams)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
