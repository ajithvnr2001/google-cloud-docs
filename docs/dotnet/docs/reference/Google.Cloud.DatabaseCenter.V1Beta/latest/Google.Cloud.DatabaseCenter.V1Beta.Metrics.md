---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Metrics
title: Database Center v1beta API - Class Metrics (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:57.379928+00:00
---

# Database Center v1beta API - Class Metrics (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Metrics

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Class Metrics (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    public sealed class Metrics : IMessage<Metrics>, IEquatable<Metrics>, IDeepCloneable<Metrics>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Center v1beta API class Metrics.

Metrics represents the metrics for a database resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Metrics

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Metrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Metrics), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Metrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Metrics), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Metrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Metrics), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Constructors 

### Metrics()
    
    
    public Metrics()

### Metrics(Metrics)
    
    
    public Metrics(Metrics other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Metrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Metrics)`  
  
  
## Properties 

### CurrentMemoryUsedBytes
    
    
    public MetricData CurrentMemoryUsedBytes { get; set; }

Current memory used by the resource in bytes.

**Property Value**  
---  
**Type** | **Description**  
`[MetricData](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.MetricData)` |   
  
### CurrentStorageUsedBytes
    
    
    public MetricData CurrentStorageUsedBytes { get; set; }

Current storage used by the resource in bytes.

**Property Value**  
---  
**Type** | **Description**  
`[MetricData](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.MetricData)` |   
  
### NodeCount
    
    
    public MetricData NodeCount { get; set; }

Number of nodes in instance for spanner or bigtable.

**Property Value**  
---  
**Type** | **Description**  
`[MetricData](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.MetricData)` |   
  
### P95CpuUtilization
    
    
    public MetricData P95CpuUtilization { get; set; }

P95 CPU utilization observed for the resource. The value is a fraction between 0.0 and 1.0 (may momentarily exceed 1.0 in some cases).

**Property Value**  
---  
**Type** | **Description**  
`[MetricData](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.MetricData)` |   
  
### P99CpuUtilization
    
    
    public MetricData P99CpuUtilization { get; set; }

P99 CPU utilization observed for the resource. The value is a fraction between 0.0 and 1.0 (may momentarily exceed 1.0 in some cases).

**Property Value**  
---  
**Type** | **Description**  
`[MetricData](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.MetricData)` |   
  
### PeakMemoryUtilization
    
    
    public MetricData PeakMemoryUtilization { get; set; }

Peak memory utilization observed for the resource. The value is a fraction between 0.0 and 1.0 (may momentarily exceed 1.0 in some cases).

**Property Value**  
---  
**Type** | **Description**  
`[MetricData](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.MetricData)` |   
  
### PeakNumberConnections
    
    
    public MetricData PeakNumberConnections { get; set; }

Peak number of connections observed for the resource. The value is a positive integer.

**Property Value**  
---  
**Type** | **Description**  
`[MetricData](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.MetricData)` |   
  
### PeakStorageUtilization
    
    
    public MetricData PeakStorageUtilization { get; set; }

Peak storage utilization observed for the resource. The value is a fraction between 0.0 and 1.0 (may momentarily exceed 1.0 in some cases).

**Property Value**  
---  
**Type** | **Description**  
`[MetricData](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.MetricData)` |   
  
### ProcessingUnitCount
    
    
    public MetricData ProcessingUnitCount { get; set; }

Number of processing units in spanner.

**Property Value**  
---  
**Type** | **Description**  
`[MetricData](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.MetricData)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
