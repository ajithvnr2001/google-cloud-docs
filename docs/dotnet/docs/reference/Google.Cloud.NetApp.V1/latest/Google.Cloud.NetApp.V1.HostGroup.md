---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.HostGroup
title: NetApp v1 API - Class HostGroup (1.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:16.705495+00:00
---

# NetApp v1 API - Class HostGroup (1.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.HostGroup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  NetApp v1 API - Class HostGroup (1.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.0 (latest)  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class HostGroup : IMessage<HostGroup>, IEquatable<HostGroup>, IDeepCloneable<HostGroup>, IBufferMessage, IMessage

Reference documentation and code samples for the NetApp v1 API class HostGroup.

Host group is a collection of hosts that can be used for accessing a Block Volume.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > HostGroup

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[HostGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.HostGroup), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[HostGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.HostGroup), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[HostGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.HostGroup), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetApp.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1)

## Assembly

Google.Cloud.NetApp.V1.dll

## Constructors 

### HostGroup()
    
    
    public HostGroup()

### HostGroup(HostGroup)
    
    
    public HostGroup(HostGroup other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[HostGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.HostGroup)`  
  
  
## Properties 

### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Create time of the host group.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Description
    
    
    public string Description { get; set; }

Optional. Description of the host group.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HostGroupName
    
    
    public HostGroupName HostGroupName { get; set; }

[HostGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.HostGroupName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.HostGroup#Google_Cloud_NetApp_V1_HostGroup_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[HostGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.HostGroupName)` |   
  
### Hosts
    
    
    public RepeatedField<string> Hosts { get; }

Required. The list of hosts associated with the host group.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Optional. Labels of the host group.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. The resource name of the host group. Format: `projects/{project_number}/locations/{location_id}/hostGroups/{host_group_id}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OsType
    
    
    public OsType OsType { get; set; }

Required. The OS type of the host group. It indicates the type of operating system used by all of the hosts in the HostGroup. All hosts in a HostGroup must be of the same OS type. This can be set only when creating a HostGroup.

**Property Value**  
---  
**Type** | **Description**  
`[OsType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.OsType)` |   
  
### State
    
    
    public HostGroup.Types.State State { get; set; }

Output only. State of the host group.

**Property Value**  
---  
**Type** | **Description**  
`[HostGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.HostGroup)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.HostGroup.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.HostGroup.Types.State)` |   
  
### Type
    
    
    public HostGroup.Types.Type Type { get; set; }

Required. Type of the host group.

**Property Value**  
---  
**Type** | **Description**  
`[HostGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.HostGroup)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.HostGroup.Types)[Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.HostGroup.Types.Type)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
