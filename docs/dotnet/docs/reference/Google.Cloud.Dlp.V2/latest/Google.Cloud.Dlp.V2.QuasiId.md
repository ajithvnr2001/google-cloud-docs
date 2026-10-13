---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.QuasiId
title: Google Cloud Data Loss Prevention v2 API - Class QuasiId (4.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:53.424365+00:00
---

# Google Cloud Data Loss Prevention v2 API - Class QuasiId (4.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.QuasiId

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Data Loss Prevention v2 API - Class QuasiId (4.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.27.0 (latest)  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.5.0  3.4.0  3.3.0  3.2.0  2.16.0  2.15.0 
    
    
    public sealed class QuasiId : IMessage<QuasiId>, IEquatable<QuasiId>, IDeepCloneable<QuasiId>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Data Loss Prevention v2 API class QuasiId.

A column with a semantic tag attached.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > QuasiId

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[QuasiId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.QuasiId), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[QuasiId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.QuasiId), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[QuasiId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.QuasiId), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2)

## Assembly

Google.Cloud.Dlp.V2.dll

## Constructors 

### QuasiId()
    
    
    public QuasiId()

### QuasiId(QuasiId)
    
    
    public QuasiId(QuasiId other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[QuasiId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.QuasiId)`  
  
  
## Properties 

### CustomTag
    
    
    public string CustomTag { get; set; }

A column can be tagged with a custom tag. In this case, the user must indicate an auxiliary table that contains statistical information on the possible values of this column.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Field
    
    
    public FieldId Field { get; set; }

Required. Identifies the column.

**Property Value**  
---  
**Type** | **Description**  
`[FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId)` |   
  
### HasCustomTag
    
    
    public bool HasCustomTag { get; }

Gets whether the "custom_tag" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Inferred
    
    
    public Empty Inferred { get; set; }

If no semantic tag is indicated, we infer the statistical model from the distribution of values in the input data

**Property Value**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` |   
  
### InfoType
    
    
    public InfoType InfoType { get; set; }

A column can be tagged with a InfoType to use the relevant public dataset as a statistical model of population, if available. We currently support US ZIP codes, region codes, ages and genders. To programmatically obtain the list of supported InfoTypes, use ListInfoTypes with the supported_by=RISK_ANALYSIS filter.

**Property Value**  
---  
**Type** | **Description**  
`[InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType)` |   
  
### TagCase
    
    
    public QuasiId.TagOneofCase TagCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[QuasiId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.QuasiId)[TagOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.QuasiId.TagOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
