---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary.Types.Stats
title: Maintenance v1 API - Class MaintenanceSummary.Types.Stats (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:14.574107+00:00
---

# Maintenance v1 API - Class MaintenanceSummary.Types.Stats (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary.Types.Stats

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Maintenance v1 API - Class MaintenanceSummary.Types.Stats (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class MaintenanceSummary.Types.Stats : IMessage<MaintenanceSummary.Types.Stats>, IEquatable<MaintenanceSummary.Types.Stats>, IDeepCloneable<MaintenanceSummary.Types.Stats>, IBufferMessage, IMessage

Reference documentation and code samples for the Maintenance v1 API class MaintenanceSummary.Types.Stats.

Stats indicates the type of aggregate and the corresponding aggregates.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > MaintenanceSummary.Types.Stats

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[MaintenanceSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary.Types)[Stats](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary.Types.Stats), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[MaintenanceSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary.Types)[Stats](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary.Types.Stats), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[MaintenanceSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary.Types)[Stats](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary.Types.Stats), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Maintenance.Api.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1)

## Assembly

Google.Cloud.Maintenance.Api.V1.dll

## Constructors 

### Stats()
    
    
    public Stats()

### Stats(Stats)
    
    
    public Stats(MaintenanceSummary.Types.Stats other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[MaintenanceSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary.Types)[Stats](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary.Types.Stats)`  
  
  
## Properties 

### Aggregates
    
    
    public RepeatedField<MaintenanceSummary.Types.Aggregate> Aggregates { get; }

Aggregates is a list <group, count> pairs. For example, if the group_by is `"state"` a possible tuple in the aggregates list could be "SCHEDULED" : `11`,

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[MaintenanceSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary.Types)[Aggregate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary.Types.Aggregate)` |   
  
### GroupBy
    
    
    public string GroupBy { get; set; }

groupBy specifies the type of aggregate. For example a group_by might be `"state"`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
