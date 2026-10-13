---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.MultiLanguageDetectionMetadata
title: Model Armor v1beta API - Class MultiLanguageDetectionMetadata (1.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:44:25.353077+00:00
---

# Model Armor v1beta API - Class MultiLanguageDetectionMetadata (1.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.MultiLanguageDetectionMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Model Armor v1beta API - Class MultiLanguageDetectionMetadata (1.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta06 (latest)  1.0.0-beta05 
    
    
    public sealed class MultiLanguageDetectionMetadata : IMessage<MultiLanguageDetectionMetadata>, IEquatable<MultiLanguageDetectionMetadata>, IDeepCloneable<MultiLanguageDetectionMetadata>, IBufferMessage, IMessage

Reference documentation and code samples for the Model Armor v1beta API class MultiLanguageDetectionMetadata.

Message for Enabling Multi Language Detection.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > MultiLanguageDetectionMetadata

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[MultiLanguageDetectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.MultiLanguageDetectionMetadata), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[MultiLanguageDetectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.MultiLanguageDetectionMetadata), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[MultiLanguageDetectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.MultiLanguageDetectionMetadata), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ModelArmor.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta)

## Assembly

Google.Cloud.ModelArmor.V1Beta.dll

## Constructors 

### MultiLanguageDetectionMetadata()
    
    
    public MultiLanguageDetectionMetadata()

### MultiLanguageDetectionMetadata(MultiLanguageDetectionMetadata)
    
    
    public MultiLanguageDetectionMetadata(MultiLanguageDetectionMetadata other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[MultiLanguageDetectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.MultiLanguageDetectionMetadata)`  
  
  
## Properties 

### EnableMultiLanguageDetection
    
    
    public bool EnableMultiLanguageDetection { get; set; }

Optional. Enable detection of multi-language prompts and responses.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SourceLanguage
    
    
    public string SourceLanguage { get; set; }

Optional. Optional Source language of the user prompt.

If multi-language detection is enabled and this field is not set, the source language will be automatically detected. When a source language is provided, Model Armor uses it to sanitize the input. In that case the system does not perform auto-detection and relies solely on the specified language.

This string field accepts a language code from the ISO-639 standard. For a list of languages supported by Model Armor, see [Model Armor supported languages](https://cloud.google.com/security-command-center/docs/model-armor-overview#languages-supported). For a comprehensive list of language codes, see [ISO-639](https://cloud.google.com/translate/docs/languages#nmt).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
