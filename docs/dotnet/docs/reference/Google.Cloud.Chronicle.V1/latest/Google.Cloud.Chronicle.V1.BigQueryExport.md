---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport
title: Chronicle v1 API - Class BigQueryExport (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:40.186356+00:00
---

# Chronicle v1 API - Class BigQueryExport (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class BigQueryExport (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class BigQueryExport : IMessage<BigQueryExport>, IEquatable<BigQueryExport>, IDeepCloneable<BigQueryExport>, IBufferMessage, IMessage

Reference documentation and code samples for the Chronicle v1 API class BigQueryExport.

This resource represents the BigQuery export configuration for a Chronicle instance which includes Google Cloud Platform resources like Cloud Storage buckets, BigQuery datasets etc and the export settings for each data source.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BigQueryExport

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Constructors 

### BigQueryExport()
    
    
    public BigQueryExport()

### BigQueryExport(BigQueryExport)
    
    
    public BigQueryExport(BigQueryExport other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)`  
  
  
## Properties 

### BigQueryExportName
    
    
    public BigQueryExportName BigQueryExportName { get; set; }

[BigQueryExportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport#Google_Cloud_Chronicle_V1_BigQueryExport_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[BigQueryExportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportName)` |   
  
### BigQueryExportPackage
    
    
    public BigQueryExportPackage BigQueryExportPackage { get; set; }

Output only. The BigQueryExportPackage entitled for the Chronicle instance.

**Property Value**  
---  
**Type** | **Description**  
`[BigQueryExportPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportPackage)` |   
  
### EntityGraphSettings
    
    
    public DataSourceExportSettings EntityGraphSettings { get; set; }

Optional. The export settings for the Entity Graph data source.

**Property Value**  
---  
**Type** | **Description**  
`[DataSourceExportSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataSourceExportSettings)` |   
  
### IocMatchesSettings
    
    
    public DataSourceExportSettings IocMatchesSettings { get; set; }

Optional. The export settings for the IOC Matches data source.

**Property Value**  
---  
**Type** | **Description**  
`[DataSourceExportSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataSourceExportSettings)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. The resource name of the BigQueryExport. Format: projects/{project}/locations/{location}/instances/{instance}/bigQueryExport

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Provisioned
    
    
    public bool Provisioned { get; set; }

Output only. Whether the BigQueryExport has been provisioned for the Chronicle instance.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### RuleDetectionsSettings
    
    
    public DataSourceExportSettings RuleDetectionsSettings { get; set; }

Optional. The export settings for the Rule Detections data source.

**Property Value**  
---  
**Type** | **Description**  
`[DataSourceExportSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataSourceExportSettings)` |   
  
### UdmEventsAggregatesSettings
    
    
    public DataSourceExportSettings UdmEventsAggregatesSettings { get; set; }

Optional. The export settings for the UDM Events Aggregates data source.

**Property Value**  
---  
**Type** | **Description**  
`[DataSourceExportSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataSourceExportSettings)` |   
  
### UdmEventsSettings
    
    
    public DataSourceExportSettings UdmEventsSettings { get; set; }

Optional. The export settings for the UDM Events data source.

**Property Value**  
---  
**Type** | **Description**  
`[DataSourceExportSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataSourceExportSettings)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
