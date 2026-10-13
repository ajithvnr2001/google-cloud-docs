---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectLocationCrossSiteInterconnectInfo
title: Compute Engine v1 API - Class InterconnectLocationCrossSiteInterconnectInfo (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:02.043768+00:00
---

# Compute Engine v1 API - Class InterconnectLocationCrossSiteInterconnectInfo (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectLocationCrossSiteInterconnectInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class InterconnectLocationCrossSiteInterconnectInfo (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class InterconnectLocationCrossSiteInterconnectInfo : IMessage<InterconnectLocationCrossSiteInterconnectInfo>, IEquatable<InterconnectLocationCrossSiteInterconnectInfo>, IDeepCloneable<InterconnectLocationCrossSiteInterconnectInfo>, IBufferMessage, IMessage

Reference documentation and code samples for the Compute Engine v1 API class InterconnectLocationCrossSiteInterconnectInfo.

Information about Cross-Site Interconnect wires which may be created between the containing location and another remote location.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > InterconnectLocationCrossSiteInterconnectInfo

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[InterconnectLocationCrossSiteInterconnectInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectLocationCrossSiteInterconnectInfo), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[InterconnectLocationCrossSiteInterconnectInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectLocationCrossSiteInterconnectInfo), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[InterconnectLocationCrossSiteInterconnectInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectLocationCrossSiteInterconnectInfo), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### InterconnectLocationCrossSiteInterconnectInfo()
    
    
    public InterconnectLocationCrossSiteInterconnectInfo()

### InterconnectLocationCrossSiteInterconnectInfo(InterconnectLocationCrossSiteInterconnectInfo)
    
    
    public InterconnectLocationCrossSiteInterconnectInfo(InterconnectLocationCrossSiteInterconnectInfo other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[InterconnectLocationCrossSiteInterconnectInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectLocationCrossSiteInterconnectInfo)`  
  
  
## Properties 

### City
    
    
    public string City { get; set; }

Output only. The remote location for Cross-Site Interconnect wires. This specifies an InterconnectLocation city (metropolitan area designator), which itself may match multiple InterconnectLocations.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasCity
    
    
    public bool HasCity { get; }

Gets whether the "city" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMaxDynamicPathBandwidthGbps
    
    
    public bool HasMaxDynamicPathBandwidthGbps { get; }

Gets whether the "max_dynamic_path_bandwidth_gbps" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMaxFixedPathBandwidthGbps
    
    
    public bool HasMaxFixedPathBandwidthGbps { get; }

Gets whether the "max_fixed_path_bandwidth_gbps" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### MaxDynamicPathBandwidthGbps
    
    
    public long MaxDynamicPathBandwidthGbps { get; set; }

Output only. The maximum unmetered bandwidth for dynamic paths allowable per WireGroup for this metro.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### MaxFixedPathBandwidthGbps
    
    
    public long MaxFixedPathBandwidthGbps { get; set; }

Output only. The maximum unmetered bandwidth for fixed paths allowable per WireGroup for this metro.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
