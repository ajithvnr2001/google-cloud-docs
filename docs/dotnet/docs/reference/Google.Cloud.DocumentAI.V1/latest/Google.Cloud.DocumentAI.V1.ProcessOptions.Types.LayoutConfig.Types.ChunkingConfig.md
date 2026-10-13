---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types.LayoutConfig.Types.ChunkingConfig
title: Cloud Document AI v1 API - Class ProcessOptions.Types.LayoutConfig.Types.ChunkingConfig (3.25.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:16.112822+00:00
---

# Cloud Document AI v1 API - Class ProcessOptions.Types.LayoutConfig.Types.ChunkingConfig (3.25.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types.LayoutConfig.Types.ChunkingConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Document AI v1 API - Class ProcessOptions.Types.LayoutConfig.Types.ChunkingConfig (3.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.25.0 (latest)  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.0.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ProcessOptions.Types.LayoutConfig.Types.ChunkingConfig : IMessage<ProcessOptions.Types.LayoutConfig.Types.ChunkingConfig>, IEquatable<ProcessOptions.Types.LayoutConfig.Types.ChunkingConfig>, IDeepCloneable<ProcessOptions.Types.LayoutConfig.Types.ChunkingConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Document AI v1 API class ProcessOptions.Types.LayoutConfig.Types.ChunkingConfig.

Serving config for chunking.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ProcessOptions.Types.LayoutConfig.Types.ChunkingConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ProcessOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types)[LayoutConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types.LayoutConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types.LayoutConfig.Types)[ChunkingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types.LayoutConfig.Types.ChunkingConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ProcessOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types)[LayoutConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types.LayoutConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types.LayoutConfig.Types)[ChunkingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types.LayoutConfig.Types.ChunkingConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ProcessOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types)[LayoutConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types.LayoutConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types.LayoutConfig.Types)[ChunkingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types.LayoutConfig.Types.ChunkingConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DocumentAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1)

## Assembly

Google.Cloud.DocumentAI.V1.dll

## Constructors 

### ChunkingConfig()
    
    
    public ChunkingConfig()

### ChunkingConfig(ChunkingConfig)
    
    
    public ChunkingConfig(ProcessOptions.Types.LayoutConfig.Types.ChunkingConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ProcessOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types)[LayoutConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types.LayoutConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types.LayoutConfig.Types)[ChunkingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1/latest/Google.Cloud.DocumentAI.V1.ProcessOptions.Types.LayoutConfig.Types.ChunkingConfig)`  
  
  
## Properties 

### ChunkSize
    
    
    public int ChunkSize { get; set; }

Optional. The chunk sizes to use when splitting documents, in order of level.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### IncludeAncestorHeadings
    
    
    public bool IncludeAncestorHeadings { get; set; }

Optional. Whether or not to include ancestor headings when splitting.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
