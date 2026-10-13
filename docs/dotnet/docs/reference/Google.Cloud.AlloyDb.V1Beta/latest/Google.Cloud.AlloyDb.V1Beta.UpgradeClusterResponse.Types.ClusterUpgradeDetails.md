---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse.Types.ClusterUpgradeDetails
title: AlloyDB v1beta API - Class UpgradeClusterResponse.Types.ClusterUpgradeDetails (1.0.0-beta19) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:09:37.785814+00:00
---

# AlloyDB v1beta API - Class UpgradeClusterResponse.Types.ClusterUpgradeDetails (1.0.0-beta19)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse.Types.ClusterUpgradeDetails

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1beta API - Class UpgradeClusterResponse.Types.ClusterUpgradeDetails (1.0.0-beta19) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta19 (latest)  1.0.0-beta18 
    
    
    public sealed class UpgradeClusterResponse.Types.ClusterUpgradeDetails : IMessage<UpgradeClusterResponse.Types.ClusterUpgradeDetails>, IEquatable<UpgradeClusterResponse.Types.ClusterUpgradeDetails>, IDeepCloneable<UpgradeClusterResponse.Types.ClusterUpgradeDetails>, IBufferMessage, IMessage

Reference documentation and code samples for the AlloyDB v1beta API class UpgradeClusterResponse.Types.ClusterUpgradeDetails.

Upgrade details of a cluster. This cluster can be primary or secondary.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpgradeClusterResponse.Types.ClusterUpgradeDetails

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse.Types)[ClusterUpgradeDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse.Types.ClusterUpgradeDetails), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse.Types)[ClusterUpgradeDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse.Types.ClusterUpgradeDetails), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse.Types)[ClusterUpgradeDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse.Types.ClusterUpgradeDetails), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AlloyDb.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta)

## Assembly

Google.Cloud.AlloyDb.V1Beta.dll

## Constructors 

### ClusterUpgradeDetails()
    
    
    public ClusterUpgradeDetails()

### ClusterUpgradeDetails(ClusterUpgradeDetails)
    
    
    public ClusterUpgradeDetails(UpgradeClusterResponse.Types.ClusterUpgradeDetails other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse.Types)[ClusterUpgradeDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse.Types.ClusterUpgradeDetails)`  
  
  
## Properties 

### ClusterType
    
    
    public Cluster.Types.ClusterType ClusterType { get; set; }

Cluster type which can either be primary or secondary.

**Property Value**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster.Types)[ClusterType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster.Types.ClusterType)` |   
  
### DatabaseVersion
    
    
    public DatabaseVersion DatabaseVersion { get; set; }

Database version of the cluster after the upgrade operation. This will be the target version if the upgrade was successful otherwise it remains the same as that before the upgrade operation.

**Property Value**  
---  
**Type** | **Description**  
`[DatabaseVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DatabaseVersion)` |   
  
### InstanceUpgradeDetails
    
    
    public RepeatedField<UpgradeClusterResponse.Types.InstanceUpgradeDetails> InstanceUpgradeDetails { get; }

Upgrade details of the instances directly associated with this cluster.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse.Types)[InstanceUpgradeDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse.Types.InstanceUpgradeDetails)` |   
  
### Name
    
    
    public string Name { get; set; }

Normalized name of the cluster

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### StageInfo
    
    
    public RepeatedField<UpgradeClusterResponse.Types.StageInfo> StageInfo { get; }

Array containing stage info associated with this cluster.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse.Types)[StageInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse.Types.StageInfo)` |   
  
### UpgradeStatus
    
    
    public UpgradeClusterResponse.Types.Status UpgradeStatus { get; set; }

Upgrade status of the cluster.

**Property Value**  
---  
**Type** | **Description**  
`[UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse.Types)[Status](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UpgradeClusterResponse.Types.Status)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
