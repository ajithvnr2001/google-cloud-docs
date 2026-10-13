---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MultiColumnDatatypeChange
title: Database Migration v1 API - Class MultiColumnDatatypeChange (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:16.015980+00:00
---

# Database Migration v1 API - Class MultiColumnDatatypeChange (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MultiColumnDatatypeChange

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Migration v1 API - Class MultiColumnDatatypeChange (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MultiColumnDatatypeChange)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.5.0/Google.Cloud.CloudDms.V1.MultiColumnDatatypeChange)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.4.0/Google.Cloud.CloudDms.V1.MultiColumnDatatypeChange)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.3.0/Google.Cloud.CloudDms.V1.MultiColumnDatatypeChange)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.2.0/Google.Cloud.CloudDms.V1.MultiColumnDatatypeChange)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.1.0/Google.Cloud.CloudDms.V1.MultiColumnDatatypeChange)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.0.0/Google.Cloud.CloudDms.V1.MultiColumnDatatypeChange)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.2.0/Google.Cloud.CloudDms.V1.MultiColumnDatatypeChange)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.1.0/Google.Cloud.CloudDms.V1.MultiColumnDatatypeChange)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.0.0/Google.Cloud.CloudDms.V1.MultiColumnDatatypeChange)


    
    
    public sealed class MultiColumnDatatypeChange : IMessage<MultiColumnDatatypeChange>, IEquatable<MultiColumnDatatypeChange>, IDeepCloneable<MultiColumnDatatypeChange>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Migration v1 API class MultiColumnDatatypeChange.

Options to configure rule type MultiColumnDatatypeChange. The rule is used to change the data type and associated properties of multiple columns at once.

The rule filter field can refer to one or more entities.

The rule scope can be one of:Column.

This rule requires additional filters to be specified beyond the basic rule filter field, which is the source data type, but the rule supports additional filtering capabilities such as the minimum and maximum field length. All additional filters which are specified are required to be met in order for the rule to be applied (logical AND between the fields).

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > MultiColumnDatatypeChange

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[MultiColumnDatatypeChange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MultiColumnDatatypeChange), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[MultiColumnDatatypeChange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MultiColumnDatatypeChange), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[MultiColumnDatatypeChange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MultiColumnDatatypeChange), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudDms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1)

## Assembly

Google.Cloud.CloudDms.V1.dll

## Constructors 

### MultiColumnDatatypeChange()
    
    
    public MultiColumnDatatypeChange()

### MultiColumnDatatypeChange(MultiColumnDatatypeChange)
    
    
    public MultiColumnDatatypeChange(MultiColumnDatatypeChange other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[MultiColumnDatatypeChange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MultiColumnDatatypeChange)`  
  
  
## Properties 

### CustomFeatures
    
    
    public Struct CustomFeatures { get; set; }

Optional. Custom engine specific features.

**Property Value**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` |   
  
### NewDataType
    
    
    public string NewDataType { get; set; }

Required. New data type.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OverrideFractionalSecondsPrecision
    
    
    public int OverrideFractionalSecondsPrecision { get; set; }

Optional. Column fractional seconds precision - used only for timestamp based datatypes - if not specified and relevant uses the source column fractional seconds precision.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### OverrideLength
    
    
    public long OverrideLength { get; set; }

Optional. Column length - e.g. varchar (50) - if not specified and relevant uses the source column length.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### OverridePrecision
    
    
    public int OverridePrecision { get; set; }

Optional. Column precision - when relevant - if not specified and relevant uses the source column precision.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### OverrideScale
    
    
    public int OverrideScale { get; set; }

Optional. Column scale - when relevant - if not specified and relevant uses the source column scale.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### SourceDataTypeFilter
    
    
    public string SourceDataTypeFilter { get; set; }

Required. Filter on source data type.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SourceFilterCase
    
    
    public MultiColumnDatatypeChange.SourceFilterOneofCase SourceFilterCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MultiColumnDatatypeChange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MultiColumnDatatypeChange)[SourceFilterOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MultiColumnDatatypeChange.SourceFilterOneofCase)` |   
  
### SourceNumericFilter
    
    
    public SourceNumericFilter SourceNumericFilter { get; set; }

Optional. Filter for fixed point number data types such as NUMERIC/NUMBER.

**Property Value**  
---  
**Type** | **Description**  
`[SourceNumericFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.SourceNumericFilter)` |   
  
### SourceTextFilter
    
    
    public SourceTextFilter SourceTextFilter { get; set; }

Optional. Filter for text-based data types like varchar.

**Property Value**  
---  
**Type** | **Description**  
`[SourceTextFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.SourceTextFilter)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
