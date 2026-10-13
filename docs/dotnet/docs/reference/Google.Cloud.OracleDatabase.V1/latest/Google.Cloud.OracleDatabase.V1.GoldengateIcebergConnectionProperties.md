---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateIcebergConnectionProperties
title: Oracle Database@Google Cloud v1 API - Class GoldengateIcebergConnectionProperties (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:48.305183+00:00
---

# Oracle Database@Google Cloud v1 API - Class GoldengateIcebergConnectionProperties (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateIcebergConnectionProperties

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud v1 API - Class GoldengateIcebergConnectionProperties (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class GoldengateIcebergConnectionProperties : IMessage<GoldengateIcebergConnectionProperties>, IEquatable<GoldengateIcebergConnectionProperties>, IDeepCloneable<GoldengateIcebergConnectionProperties>, IBufferMessage, IMessage

Reference documentation and code samples for the Oracle Database@Google Cloud v1 API class GoldengateIcebergConnectionProperties.

The properties of GoldengateIcebergConnection.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GoldengateIcebergConnectionProperties

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GoldengateIcebergConnectionProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateIcebergConnectionProperties), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GoldengateIcebergConnectionProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateIcebergConnectionProperties), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GoldengateIcebergConnectionProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateIcebergConnectionProperties), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.OracleDatabase.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1)

## Assembly

Google.Cloud.OracleDatabase.V1.dll

## Constructors 

### GoldengateIcebergConnectionProperties()
    
    
    public GoldengateIcebergConnectionProperties()

### GoldengateIcebergConnectionProperties(GoldengateIcebergConnectionProperties)
    
    
    public GoldengateIcebergConnectionProperties(GoldengateIcebergConnectionProperties other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GoldengateIcebergConnectionProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateIcebergConnectionProperties)`  
  
  
## Properties 

### Catalog
    
    
    public IcebergCatalog Catalog { get; set; }

Required. The Iceberg catalog.

**Property Value**  
---  
**Type** | **Description**  
`[IcebergCatalog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.IcebergCatalog)` |   
  
### Storage
    
    
    public IcebergStorage Storage { get; set; }

Required. The Iceberg storage.

**Property Value**  
---  
**Type** | **Description**  
`[IcebergStorage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.IcebergStorage)` |   
  
### TechnologyType
    
    
    public string TechnologyType { get; set; }

Required. The technology type of Iceberg connection.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
