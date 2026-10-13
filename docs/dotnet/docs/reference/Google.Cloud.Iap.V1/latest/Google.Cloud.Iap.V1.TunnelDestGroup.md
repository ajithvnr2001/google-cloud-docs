---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iap.V1/latest/Google.Cloud.Iap.V1.TunnelDestGroup
title: Cloud Identity-Aware Proxy v1 API - Class TunnelDestGroup (2.10.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:14.940773+00:00
---

# Cloud Identity-Aware Proxy v1 API - Class TunnelDestGroup (2.10.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iap.V1/latest/Google.Cloud.Iap.V1.TunnelDestGroup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Identity-Aware Proxy v1 API - Class TunnelDestGroup (2.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.0 (latest)  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class TunnelDestGroup : IMessage<TunnelDestGroup>, IEquatable<TunnelDestGroup>, IDeepCloneable<TunnelDestGroup>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Identity-Aware Proxy v1 API class TunnelDestGroup.

A TunnelDestGroup.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > TunnelDestGroup

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[TunnelDestGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iap.V1/latest/Google.Cloud.Iap.V1.TunnelDestGroup), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[TunnelDestGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iap.V1/latest/Google.Cloud.Iap.V1.TunnelDestGroup), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[TunnelDestGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iap.V1/latest/Google.Cloud.Iap.V1.TunnelDestGroup), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Iap.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iap.V1/latest/Google.Cloud.Iap.V1)

## Assembly

Google.Cloud.Iap.V1.dll

## Constructors 

### TunnelDestGroup()
    
    
    public TunnelDestGroup()

### TunnelDestGroup(TunnelDestGroup)
    
    
    public TunnelDestGroup(TunnelDestGroup other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[TunnelDestGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iap.V1/latest/Google.Cloud.Iap.V1.TunnelDestGroup)`  
  
  
## Properties 

### Cidrs
    
    
    public RepeatedField<string> Cidrs { get; }

Optional. Unordered list. List of CIDRs that this group applies to.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Fqdns
    
    
    public RepeatedField<string> Fqdns { get; }

Optional. Unordered list. List of FQDNs that this group applies to.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. Identifier for the TunnelDestGroup. Must be unique within the project and contain only lower case letters (a-z) and dashes (-).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TunnelDestGroupName
    
    
    public TunnelDestGroupName TunnelDestGroupName { get; set; }

[TunnelDestGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iap.V1/latest/Google.Cloud.Iap.V1.TunnelDestGroupName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iap.V1/latest/Google.Cloud.Iap.V1.TunnelDestGroup#Google_Cloud_Iap_V1_TunnelDestGroup_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[TunnelDestGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iap.V1/latest/Google.Cloud.Iap.V1.TunnelDestGroupName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-16 UTC."],[],[]] 
