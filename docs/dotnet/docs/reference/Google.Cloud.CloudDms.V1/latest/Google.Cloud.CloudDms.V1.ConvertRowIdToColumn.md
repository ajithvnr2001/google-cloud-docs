---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.ConvertRowIdToColumn
title: Database Migration v1 API - Class ConvertRowIdToColumn (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:12.071284+00:00
---

# Database Migration v1 API - Class ConvertRowIdToColumn (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.ConvertRowIdToColumn

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Migration v1 API - Class ConvertRowIdToColumn (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.ConvertRowIdToColumn)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.5.0/Google.Cloud.CloudDms.V1.ConvertRowIdToColumn)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.4.0/Google.Cloud.CloudDms.V1.ConvertRowIdToColumn)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.3.0/Google.Cloud.CloudDms.V1.ConvertRowIdToColumn)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.2.0/Google.Cloud.CloudDms.V1.ConvertRowIdToColumn)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.1.0/Google.Cloud.CloudDms.V1.ConvertRowIdToColumn)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.0.0/Google.Cloud.CloudDms.V1.ConvertRowIdToColumn)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.2.0/Google.Cloud.CloudDms.V1.ConvertRowIdToColumn)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.1.0/Google.Cloud.CloudDms.V1.ConvertRowIdToColumn)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.0.0/Google.Cloud.CloudDms.V1.ConvertRowIdToColumn)


    
    
    public sealed class ConvertRowIdToColumn : IMessage<ConvertRowIdToColumn>, IEquatable<ConvertRowIdToColumn>, IDeepCloneable<ConvertRowIdToColumn>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Migration v1 API class ConvertRowIdToColumn.

Options to configure rule type ConvertROWIDToColumn. The rule is used to add column rowid to destination tables based on an Oracle rowid function/property.

The rule filter field can refer to one or more entities.

The rule scope can be one of: Table.

This rule requires additional filter to be specified beyond the basic rule filter field, which is whether or not to work on tables which already have a primary key defined.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ConvertRowIdToColumn

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ConvertRowIdToColumn](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.ConvertRowIdToColumn), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ConvertRowIdToColumn](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.ConvertRowIdToColumn), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ConvertRowIdToColumn](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.ConvertRowIdToColumn), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudDms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1)

## Assembly

Google.Cloud.CloudDms.V1.dll

## Constructors 

### ConvertRowIdToColumn()
    
    
    public ConvertRowIdToColumn()

### ConvertRowIdToColumn(ConvertRowIdToColumn)
    
    
    public ConvertRowIdToColumn(ConvertRowIdToColumn other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ConvertRowIdToColumn](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.ConvertRowIdToColumn)`  
  
  
## Properties 

### OnlyIfNoPrimaryKey
    
    
    public bool OnlyIfNoPrimaryKey { get; set; }

Required. Only work on tables without primary key defined

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
