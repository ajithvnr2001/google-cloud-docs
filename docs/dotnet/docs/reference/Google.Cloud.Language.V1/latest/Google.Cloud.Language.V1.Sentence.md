---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.Sentence
title: Google Cloud Natural Language v1 API - Class Sentence (3.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:52:19.771629+00:00
---

# Google Cloud Natural Language v1 API - Class Sentence (3.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.Sentence

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Natural Language v1 API - Class Sentence (3.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.Sentence)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.7.0/Google.Cloud.Language.V1.Sentence)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.6.0/Google.Cloud.Language.V1.Sentence)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.5.0/Google.Cloud.Language.V1.Sentence)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.4.0/Google.Cloud.Language.V1.Sentence)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.3.0/Google.Cloud.Language.V1.Sentence)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.2.0/Google.Cloud.Language.V1.Sentence)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.1.0/Google.Cloud.Language.V1.Sentence)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.0.0/Google.Cloud.Language.V1.Sentence)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/2.3.0/Google.Cloud.Language.V1.Sentence)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/2.2.0/Google.Cloud.Language.V1.Sentence)


    
    
    public sealed class Sentence : IMessage<Sentence>, IEquatable<Sentence>, IDeepCloneable<Sentence>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Natural Language v1 API class Sentence.

Represents a sentence in the input document.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Sentence

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Sentence](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.Sentence), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Sentence](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.Sentence), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Sentence](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.Sentence), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Language.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1)

## Assembly

Google.Cloud.Language.V1.dll

## Constructors 

### Sentence()
    
    
    public Sentence()

### Sentence(Sentence)
    
    
    public Sentence(Sentence other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Sentence](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.Sentence)`  
  
  
## Properties 

### Sentiment
    
    
    public Sentiment Sentiment { get; set; }

For calls to [AnalyzeSentiment][] or if [AnnotateTextRequest.Features.extract_document_sentiment][google.cloud.language.v1.AnnotateTextRequest.Features.extract_document_sentiment] is set to true, this field will contain the sentiment for the sentence.

**Property Value**  
---  
**Type** | **Description**  
`[Sentiment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.Sentiment)` |   
  
### Text
    
    
    public TextSpan Text { get; set; }

The sentence text.

**Property Value**  
---  
**Type** | **Description**  
`[TextSpan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.TextSpan)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
