---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.TableDefinition
title: BigQuery Audit Data Logging v1 API - Class TableDefinition (1.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:12.167315+00:00
---

# BigQuery Audit Data Logging v1 API - Class TableDefinition (1.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.TableDefinition

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  BigQuery Audit Data Logging v1 API - Class TableDefinition (1.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.TableDefinition)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/1.3.0/Google.Cloud.BigQuery.Logging.V1.TableDefinition)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/1.2.0/Google.Cloud.BigQuery.Logging.V1.TableDefinition)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/1.1.0/Google.Cloud.BigQuery.Logging.V1.TableDefinition)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/1.0.0/Google.Cloud.BigQuery.Logging.V1.TableDefinition)


    
    
    public sealed class TableDefinition : IMessage<TableDefinition>, IEquatable<TableDefinition>, IDeepCloneable<TableDefinition>, IBufferMessage, IMessage

Reference documentation and code samples for the BigQuery Audit Data Logging v1 API class TableDefinition.

Describes an external data source used in a query.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > TableDefinition

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[TableDefinition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.TableDefinition), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[TableDefinition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.TableDefinition), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[TableDefinition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.TableDefinition), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BigQuery.Logging.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1)

## Assembly

Google.Cloud.BigQuery.Logging.V1.dll

## Constructors 

### TableDefinition()
    
    
    public TableDefinition()

### TableDefinition(TableDefinition)
    
    
    public TableDefinition(TableDefinition other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[TableDefinition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.TableDefinition)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Name of the table, used in queries.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SourceUris
    
    
    public RepeatedField<string> SourceUris { get; }

Google Cloud Storage URIs for the data to be imported.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
