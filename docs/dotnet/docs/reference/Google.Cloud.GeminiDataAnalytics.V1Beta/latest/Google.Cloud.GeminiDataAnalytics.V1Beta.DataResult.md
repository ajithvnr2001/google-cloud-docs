---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.DataResult
title: Data Analytics API with Gemini v1beta API - Class DataResult (1.0.0-beta12) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:18.012576+00:00
---

# Data Analytics API with Gemini v1beta API - Class DataResult (1.0.0-beta12)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.DataResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Data Analytics API with Gemini v1beta API - Class DataResult (1.0.0-beta12) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta12 (latest)  1.0.0-beta11 
    
    
    public sealed class DataResult : IMessage<DataResult>, IEquatable<DataResult>, IDeepCloneable<DataResult>, IBufferMessage, IMessage

Reference documentation and code samples for the Data Analytics API with Gemini v1beta API class DataResult.

Retrieved data.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DataResult

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DataResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.DataResult), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DataResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.DataResult), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DataResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.DataResult), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GeminiDataAnalytics.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta)

## Assembly

Google.Cloud.GeminiDataAnalytics.V1Beta.dll

## Constructors 

### DataResult()
    
    
    public DataResult()

### DataResult(DataResult)
    
    
    public DataResult(DataResult other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DataResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.DataResult)`  
  
  
## Properties 

### Data
    
    
    public RepeatedField<Struct> Data { get; }

Optional. The content of the data. Each row is a struct that matches the schema. Simple values are represented as strings, while nested structures are represented as lists or structs.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` |   
  
### FormattedData
    
    
    public RepeatedField<Struct> FormattedData { get; }

Optional. Formatted representation of the data, when applicable. Each row is a struct that directly corresponds to the row at the same index within the `data` field. Its values are string representations of the original data, formatted according to data source specifications (e.g., "$1,234.56" for currency). Columns without formatting will default to their raw value representation. If no columns have formatting rules, this field will be empty.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` |   
  
### Name
    
    
    public string Name { get; set; }

Optional. A snake-case name for the data result that reflects its contents. The name is used to pass the result around by reference, and serves as a signal about its meaning.

  * Example: "total_sales_by_product"
  * Example: "sales_for_product_12345"



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Schema
    
    
    public Schema Schema { get; set; }

Optional. The schema of the data.

**Property Value**  
---  
**Type** | **Description**  
`[Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest/Google.Cloud.GeminiDataAnalytics.V1Beta.Schema)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
