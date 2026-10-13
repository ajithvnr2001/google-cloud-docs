---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.Types.ExecutionSpec
title: Cloud Dataplex v1 API - Class DataScan.Types.ExecutionSpec (3.15.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:11.902514+00:00
---

# Cloud Dataplex v1 API - Class DataScan.Types.ExecutionSpec (3.15.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.Types.ExecutionSpec

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Dataplex v1 API - Class DataScan.Types.ExecutionSpec (3.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.15.0 (latest)  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0 
    
    
    public sealed class DataScan.Types.ExecutionSpec : IMessage<DataScan.Types.ExecutionSpec>, IEquatable<DataScan.Types.ExecutionSpec>, IDeepCloneable<DataScan.Types.ExecutionSpec>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Dataplex v1 API class DataScan.Types.ExecutionSpec.

DataScan execution settings.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DataScan.Types.ExecutionSpec

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.Types)[ExecutionSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.Types.ExecutionSpec), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.Types)[ExecutionSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.Types.ExecutionSpec), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.Types)[ExecutionSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.Types.ExecutionSpec), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1)

## Assembly

Google.Cloud.Dataplex.V1.dll

## Constructors 

### ExecutionSpec()
    
    
    public ExecutionSpec()

### ExecutionSpec(ExecutionSpec)
    
    
    public ExecutionSpec(DataScan.Types.ExecutionSpec other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.Types)[ExecutionSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.Types.ExecutionSpec)`  
  
  
## Properties 

### Field
    
    
    public string Field { get; set; }

Immutable. The unnested field (of type _Date_ or _Timestamp_) that contains values which monotonically increase over time.

If not specified, a data scan will run for all data in the table.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasField
    
    
    public bool HasField { get; }

Gets whether the "field" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IncrementalCase
    
    
    public DataScan.Types.ExecutionSpec.IncrementalOneofCase IncrementalCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[DataScan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.Types)[ExecutionSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.Types.ExecutionSpec)[IncrementalOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataScan.Types.ExecutionSpec.IncrementalOneofCase)` |   
  
### Trigger
    
    
    public Trigger Trigger { get; set; }

Optional. Spec related to how often and when a scan should be triggered.

If not specified, the default is `OnDemand`, which means the scan will not run until the user calls `RunDataScan` API.

**Property Value**  
---  
**Type** | **Description**  
`[Trigger](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.Trigger)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
