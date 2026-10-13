---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChartResult
title: Data Analytics API with Gemini v1 API - Class ChartResult (2.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:38.107493+00:00
---

# Data Analytics API with Gemini v1 API - Class ChartResult (2.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChartResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Data Analytics API with Gemini v1 API - Class ChartResult (2.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0 (latest)  1.1.0  1.0.0 
    
    
    public sealed class ChartResult : IMessage<ChartResult>, IEquatable<ChartResult>, IDeepCloneable<ChartResult>, IBufferMessage, IMessage

Reference documentation and code samples for the Data Analytics API with Gemini v1 API class ChartResult.

The result of a chart generation query.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ChartResult

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ChartResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChartResult), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ChartResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChartResult), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ChartResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChartResult), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GeminiDataAnalytics.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1)

## Assembly

Google.Cloud.GeminiDataAnalytics.V1.dll

## Constructors 

### ChartResult()
    
    
    public ChartResult()

### ChartResult(ChartResult)
    
    
    public ChartResult(ChartResult other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ChartResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.ChartResult)`  
  
  
## Properties 

### Image
    
    
    public Blob Image { get; set; }

Optional. A rendering of the chart if this was requested in the context.

**Property Value**  
---  
**Type** | **Description**  
`[Blob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.Blob)` |   
  
### VegaConfig
    
    
    public Struct VegaConfig { get; set; }

Optional. A generated Vega chart config. See <https://vega.github.io/vega/docs/config/>

**Property Value**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
