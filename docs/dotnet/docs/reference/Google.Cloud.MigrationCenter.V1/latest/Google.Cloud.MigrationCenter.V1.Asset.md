---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.Asset
title: Migration Center v1 API - Class Asset (1.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:51.571037+00:00
---

# Migration Center v1 API - Class Asset (1.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.Asset

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Migration Center v1 API - Class Asset (1.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.Asset)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/1.4.0/Google.Cloud.MigrationCenter.V1.Asset)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/1.3.0/Google.Cloud.MigrationCenter.V1.Asset)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/1.2.0/Google.Cloud.MigrationCenter.V1.Asset)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/1.1.0/Google.Cloud.MigrationCenter.V1.Asset)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/1.0.0/Google.Cloud.MigrationCenter.V1.Asset)


    
    
    public sealed class Asset : IMessage<Asset>, IEquatable<Asset>, IDeepCloneable<Asset>, IBufferMessage, IMessage

Reference documentation and code samples for the Migration Center v1 API class Asset.

An asset represents a resource in your environment. Asset types include virtual machines and databases.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Asset

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.Asset), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.Asset), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.Asset), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.MigrationCenter.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1)

## Assembly

Google.Cloud.MigrationCenter.V1.dll

## Constructors 

### Asset()
    
    
    public Asset()

### Asset(Asset)
    
    
    public Asset(Asset other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.Asset)`  
  
  
## Properties 

### AssetDetailsCase
    
    
    public Asset.AssetDetailsOneofCase AssetDetailsCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.Asset)[AssetDetailsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.Asset.AssetDetailsOneofCase)` |   
  
### AssetName
    
    
    public AssetName AssetName { get; set; }

[AssetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.AssetName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.Asset#Google_Cloud_MigrationCenter_V1_Asset_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AssetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.AssetName)` |   
  
### AssignedGroups
    
    
    public RepeatedField<string> AssignedGroups { get; }

Output only. The list of groups that the asset is assigned to.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AssignedGroupsAsGroupNames
    
    
    public ResourceNameList<GroupName> AssignedGroupsAsGroupNames { get; }

[GroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.GroupName)-typed view over the [AssignedGroups](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.Asset#Google_Cloud_MigrationCenter_V1_Asset_AssignedGroups) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ResourceNameList](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNameList-1.html)[GroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.GroupName)` |   
  
### Attributes
    
    
    public MapField<string, string> Attributes { get; }

Generic asset attributes.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The timestamp when the asset was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### InsightList
    
    
    public InsightList InsightList { get; set; }

Output only. The list of insights associated with the asset.

**Property Value**  
---  
**Type** | **Description**  
`[InsightList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.InsightList)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Labels as key value pairs.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MachineDetails
    
    
    public MachineDetails MachineDetails { get; set; }

Output only. Asset information specific for virtual and physical machines.

**Property Value**  
---  
**Type** | **Description**  
`[MachineDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.MachineDetails)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. The full name of the asset.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PerformanceData
    
    
    public AssetPerformanceData PerformanceData { get; set; }

Output only. Performance data for the asset.

**Property Value**  
---  
**Type** | **Description**  
`[AssetPerformanceData](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.AssetPerformanceData)` |   
  
### Sources
    
    
    public RepeatedField<string> Sources { get; }

Output only. The list of sources contributing to the asset.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SourcesAsSourceNames
    
    
    public ResourceNameList<SourceName> SourcesAsSourceNames { get; }

[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.SourceName)-typed view over the [Sources](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.Asset#Google_Cloud_MigrationCenter_V1_Asset_Sources) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ResourceNameList](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNameList-1.html)[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.SourceName)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. The timestamp when the asset was last updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
