---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.AnalyzeEntitySentimentResponse
title: Google Cloud Natural Language v1 API - Class AnalyzeEntitySentimentResponse (3.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:19.160547+00:00
---

# Google Cloud Natural Language v1 API - Class AnalyzeEntitySentimentResponse (3.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.AnalyzeEntitySentimentResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Natural Language v1 API - Class AnalyzeEntitySentimentResponse (3.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.AnalyzeEntitySentimentResponse)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.7.0/Google.Cloud.Language.V1.AnalyzeEntitySentimentResponse)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.6.0/Google.Cloud.Language.V1.AnalyzeEntitySentimentResponse)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.5.0/Google.Cloud.Language.V1.AnalyzeEntitySentimentResponse)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.4.0/Google.Cloud.Language.V1.AnalyzeEntitySentimentResponse)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.3.0/Google.Cloud.Language.V1.AnalyzeEntitySentimentResponse)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.2.0/Google.Cloud.Language.V1.AnalyzeEntitySentimentResponse)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.1.0/Google.Cloud.Language.V1.AnalyzeEntitySentimentResponse)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.0.0/Google.Cloud.Language.V1.AnalyzeEntitySentimentResponse)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/2.3.0/Google.Cloud.Language.V1.AnalyzeEntitySentimentResponse)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/2.2.0/Google.Cloud.Language.V1.AnalyzeEntitySentimentResponse)


    
    
    public sealed class AnalyzeEntitySentimentResponse : IMessage<AnalyzeEntitySentimentResponse>, IEquatable<AnalyzeEntitySentimentResponse>, IDeepCloneable<AnalyzeEntitySentimentResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Natural Language v1 API class AnalyzeEntitySentimentResponse.

The entity-level sentiment analysis response message.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AnalyzeEntitySentimentResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AnalyzeEntitySentimentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.AnalyzeEntitySentimentResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AnalyzeEntitySentimentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.AnalyzeEntitySentimentResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AnalyzeEntitySentimentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.AnalyzeEntitySentimentResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Language.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1)

## Assembly

Google.Cloud.Language.V1.dll

## Constructors 

### AnalyzeEntitySentimentResponse()
    
    
    public AnalyzeEntitySentimentResponse()

### AnalyzeEntitySentimentResponse(AnalyzeEntitySentimentResponse)
    
    
    public AnalyzeEntitySentimentResponse(AnalyzeEntitySentimentResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AnalyzeEntitySentimentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.AnalyzeEntitySentimentResponse)`  
  
  
## Properties 

### Entities
    
    
    public RepeatedField<Entity> Entities { get; }

The recognized entities in the input document with associated sentiments.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Entity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.Entity)` |   
  
### Language
    
    
    public string Language { get; set; }

The language of the text, which will be the same as the language specified in the request or, if not specified, the automatically-detected language. See [Document.language][google.cloud.language.v1.Document.language] field for more details.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
