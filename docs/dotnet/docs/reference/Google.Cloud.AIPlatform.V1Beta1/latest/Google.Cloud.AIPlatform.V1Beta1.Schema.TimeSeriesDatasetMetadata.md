---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TimeSeriesDatasetMetadata
title: Vertex AI v1beta1 API - Class TimeSeriesDatasetMetadata (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:29:11.528770+00:00
---

# Vertex AI v1beta1 API - Class TimeSeriesDatasetMetadata (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TimeSeriesDatasetMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class TimeSeriesDatasetMetadata (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class TimeSeriesDatasetMetadata : IMessage<TimeSeriesDatasetMetadata>, IEquatable<TimeSeriesDatasetMetadata>, IDeepCloneable<TimeSeriesDatasetMetadata>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class TimeSeriesDatasetMetadata.

The metadata of Datasets that contain time series data.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > TimeSeriesDatasetMetadata

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[TimeSeriesDatasetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TimeSeriesDatasetMetadata), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[TimeSeriesDatasetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TimeSeriesDatasetMetadata), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[TimeSeriesDatasetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TimeSeriesDatasetMetadata), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1.Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### TimeSeriesDatasetMetadata()
    
    
    public TimeSeriesDatasetMetadata()

### TimeSeriesDatasetMetadata(TimeSeriesDatasetMetadata)
    
    
    public TimeSeriesDatasetMetadata(TimeSeriesDatasetMetadata other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[TimeSeriesDatasetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TimeSeriesDatasetMetadata)`  
  
  
## Properties 

### InputConfig
    
    
    public TimeSeriesDatasetMetadata.Types.InputConfig InputConfig { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[TimeSeriesDatasetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TimeSeriesDatasetMetadata)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TimeSeriesDatasetMetadata.Types)[InputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TimeSeriesDatasetMetadata.Types.InputConfig)` |   
  
### TimeColumn
    
    
    public string TimeColumn { get; set; }

The column name of the time column that identifies time order in the time series.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TimeSeriesIdentifierColumn
    
    
    public string TimeSeriesIdentifierColumn { get; set; }

The column name of the time series identifier column that identifies the time series.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
