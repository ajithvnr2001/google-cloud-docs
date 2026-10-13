---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types.ParsingConfig
title: Discovery Engine v1beta API - Class DocumentProcessingConfig.Types.ParsingConfig (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:09.334648+00:00
---

# Discovery Engine v1beta API - Class DocumentProcessingConfig.Types.ParsingConfig (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types.ParsingConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class DocumentProcessingConfig.Types.ParsingConfig (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    public sealed class DocumentProcessingConfig.Types.ParsingConfig : IMessage<DocumentProcessingConfig.Types.ParsingConfig>, IEquatable<DocumentProcessingConfig.Types.ParsingConfig>, IDeepCloneable<DocumentProcessingConfig.Types.ParsingConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Discovery Engine v1beta API class DocumentProcessingConfig.Types.ParsingConfig.

Related configurations applied to a specific type of document parser.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DocumentProcessingConfig.Types.ParsingConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DocumentProcessingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types)[ParsingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types.ParsingConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DocumentProcessingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types)[ParsingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types.ParsingConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DocumentProcessingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types)[ParsingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types.ParsingConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Constructors 

### ParsingConfig()
    
    
    public ParsingConfig()

### ParsingConfig(ParsingConfig)
    
    
    public ParsingConfig(DocumentProcessingConfig.Types.ParsingConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DocumentProcessingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types)[ParsingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types.ParsingConfig)`  
  
  
## Properties 

### DigitalParsingConfig
    
    
    public DocumentProcessingConfig.Types.ParsingConfig.Types.DigitalParsingConfig DigitalParsingConfig { get; set; }

Configurations applied to digital parser.

**Property Value**  
---  
**Type** | **Description**  
`[DocumentProcessingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types)[ParsingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types.ParsingConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types.ParsingConfig.Types)[DigitalParsingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types.ParsingConfig.Types.DigitalParsingConfig)` |   
  
### LayoutParsingConfig
    
    
    public DocumentProcessingConfig.Types.ParsingConfig.Types.LayoutParsingConfig LayoutParsingConfig { get; set; }

Configurations applied to layout parser.

**Property Value**  
---  
**Type** | **Description**  
`[DocumentProcessingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types)[ParsingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types.ParsingConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types.ParsingConfig.Types)[LayoutParsingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types.ParsingConfig.Types.LayoutParsingConfig)` |   
  
### OcrParsingConfig
    
    
    public DocumentProcessingConfig.Types.ParsingConfig.Types.OcrParsingConfig OcrParsingConfig { get; set; }

Configurations applied to OCR parser. Currently it only applies to PDFs.

**Property Value**  
---  
**Type** | **Description**  
`[DocumentProcessingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types)[ParsingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types.ParsingConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types.ParsingConfig.Types)[OcrParsingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types.ParsingConfig.Types.OcrParsingConfig)` |   
  
### TypeDedicatedConfigCase
    
    
    public DocumentProcessingConfig.Types.ParsingConfig.TypeDedicatedConfigOneofCase TypeDedicatedConfigCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[DocumentProcessingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types)[ParsingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types.ParsingConfig)[TypeDedicatedConfigOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentProcessingConfig.Types.ParsingConfig.TypeDedicatedConfigOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
