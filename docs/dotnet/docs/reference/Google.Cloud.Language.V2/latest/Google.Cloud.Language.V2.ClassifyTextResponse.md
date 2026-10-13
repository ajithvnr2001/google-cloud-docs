---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.ClassifyTextResponse
title: Cloud Natural Language v2 API - Class ClassifyTextResponse (1.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:41.053790+00:00
---

# Cloud Natural Language v2 API - Class ClassifyTextResponse (1.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.ClassifyTextResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Natural Language v2 API - Class ClassifyTextResponse (1.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.ClassifyTextResponse)
  * [ 1.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/1.0.0-beta05/Google.Cloud.Language.V2.ClassifyTextResponse)


    
    
    public sealed class ClassifyTextResponse : IMessage<ClassifyTextResponse>, IEquatable<ClassifyTextResponse>, IDeepCloneable<ClassifyTextResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Natural Language v2 API class ClassifyTextResponse.

The document classification response message.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ClassifyTextResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ClassifyTextResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.ClassifyTextResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ClassifyTextResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.ClassifyTextResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ClassifyTextResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.ClassifyTextResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Language.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2)

## Assembly

Google.Cloud.Language.V2.dll

## Constructors 

### ClassifyTextResponse()
    
    
    public ClassifyTextResponse()

### ClassifyTextResponse(ClassifyTextResponse)
    
    
    public ClassifyTextResponse(ClassifyTextResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ClassifyTextResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.ClassifyTextResponse)`  
  
  
## Properties 

### Categories
    
    
    public RepeatedField<ClassificationCategory> Categories { get; }

Categories representing the input document.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ClassificationCategory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.ClassificationCategory)` |   
  
### LanguageCode
    
    
    public string LanguageCode { get; set; }

The language of the text, which will be the same as the language specified in the request or, if not specified, the automatically-detected language. See [Document.language][] field for more details.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LanguageSupported
    
    
    public bool LanguageSupported { get; set; }

Whether the language is officially supported. The API may still return a response when the language is not supported, but it is on a best effort basis.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
