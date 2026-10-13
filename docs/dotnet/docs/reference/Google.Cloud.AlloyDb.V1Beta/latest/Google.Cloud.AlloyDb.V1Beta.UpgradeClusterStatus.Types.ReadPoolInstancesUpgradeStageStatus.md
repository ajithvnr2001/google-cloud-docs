---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus
title: AlloyDB v1beta API - Class UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus (1.0.0-beta19) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:09:38.760969+00:00
---

# AlloyDB v1beta API - Class UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus (1.0.0-beta19)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1beta API - Class UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus (1.0.0-beta19) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta19 (latest)  1.0.0-beta18 
    
    
    public sealed class UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus : IMessage<UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus>, IEquatable<UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus>, IDeepCloneable<UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus>, IBufferMessage, IMessage

Reference documentation and code samples for the AlloyDB v1beta API class UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus.

Read pool instances upgrade specific status.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpgradeClusterStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterStatus)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterStatus.Types)[ReadPoolInstancesUpgradeStageStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpgradeClusterStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterStatus)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterStatus.Types)[ReadPoolInstancesUpgradeStageStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpgradeClusterStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterStatus)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterStatus.Types)[ReadPoolInstancesUpgradeStageStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AlloyDb.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta)

## Assembly

Google.Cloud.AlloyDb.V1Beta.dll

## Constructors 

### ReadPoolInstancesUpgradeStageStatus()
    
    
    public ReadPoolInstancesUpgradeStageStatus()

### ReadPoolInstancesUpgradeStageStatus(ReadPoolInstancesUpgradeStageStatus)
    
    
    public ReadPoolInstancesUpgradeStageStatus(UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpgradeClusterStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterStatus)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterStatus.Types)[ReadPoolInstancesUpgradeStageStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus)`  
  
  
## Properties 

### UpgradeStats
    
    
    public UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus.Types.Stats UpgradeStats { get; set; }

Read pool instances upgrade statistics.

**Property Value**  
---  
**Type** | **Description**  
`[UpgradeClusterStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterStatus)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterStatus.Types)[ReadPoolInstancesUpgradeStageStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus.Types)[Stats](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterStatus.Types.ReadPoolInstancesUpgradeStageStatus.Types.Stats)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
