---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute
title: Network Connectivity v1 API - Class PolicyBasedRoute (2.14.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:56.740585+00:00
---

# Network Connectivity v1 API - Class PolicyBasedRoute (2.14.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Connectivity v1 API - Class PolicyBasedRoute (2.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.14.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)
  * [ 2.13.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.13.0/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)
  * [ 2.12.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.12.0/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)
  * [ 2.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.11.0/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.10.0/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.9.0/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.8.0/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.7.0/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.6.0/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.5.0/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.4.0/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.3.0/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.2.0/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.1.0/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.0.0/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/1.2.0/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/1.1.0/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/1.0.0/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)


    
    
    public sealed class PolicyBasedRoute : IMessage<PolicyBasedRoute>, IEquatable<PolicyBasedRoute>, IDeepCloneable<PolicyBasedRoute>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Connectivity v1 API class PolicyBasedRoute.

Policy-based routes route L4 network traffic based on not just destination IP address, but also source IP address, protocol, and more. If a policy-based route conflicts with other types of routes, the policy-based route always takes precedence.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > PolicyBasedRoute

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[PolicyBasedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[PolicyBasedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[PolicyBasedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkConnectivity.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1)

## Assembly

Google.Cloud.NetworkConnectivity.V1.dll

## Constructors 

### PolicyBasedRoute()
    
    
    public PolicyBasedRoute()

### PolicyBasedRoute(PolicyBasedRoute)
    
    
    public PolicyBasedRoute(PolicyBasedRoute other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[PolicyBasedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)`  
  
  
## Properties 

### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Time when the policy-based route was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Description
    
    
    public string Description { get; set; }

Optional. An optional description of this resource. Provide this field when you create the resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Filter
    
    
    public PolicyBasedRoute.Types.Filter Filter { get; set; }

Required. The filter to match L4 traffic.

**Property Value**  
---  
**Type** | **Description**  
`[PolicyBasedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute.Types)[Filter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute.Types.Filter)` |   
  
### HasNextHopIlbIp
    
    
    public bool HasNextHopIlbIp { get; }

Gets whether the "next_hop_ilb_ip" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasNextHopOtherRoutes
    
    
    public bool HasNextHopOtherRoutes { get; }

Gets whether the "next_hop_other_routes" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InterconnectAttachment
    
    
    public PolicyBasedRoute.Types.InterconnectAttachment InterconnectAttachment { get; set; }

Optional. The interconnect attachments that this policy-based route applies to.

**Property Value**  
---  
**Type** | **Description**  
`[PolicyBasedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute.Types)[InterconnectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute.Types.InterconnectAttachment)` |   
  
### Kind
    
    
    public string Kind { get; set; }

Output only. Type of this resource. Always networkconnectivity#policyBasedRoute for policy-based Route resources.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

User-defined labels.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Immutable. A unique name of the resource in the form of `projects/{project_number}/locations/global/PolicyBasedRoutes/{policy_based_route_id}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Network
    
    
    public string Network { get; set; }

Required. Fully-qualified URL of the network that this route applies to, for example: projects/my-project/global/networks/my-network.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NetworkAsNetworkName
    
    
    public NetworkName NetworkAsNetworkName { get; set; }

[NetworkName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.NetworkName)-typed view over the [Network](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute#Google_Cloud_NetworkConnectivity_V1_PolicyBasedRoute_Network) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[NetworkName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.NetworkName)` |   
  
### NextHopCase
    
    
    public PolicyBasedRoute.NextHopOneofCase NextHopCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[PolicyBasedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)[NextHopOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute.NextHopOneofCase)` |   
  
### NextHopIlbIp
    
    
    public string NextHopIlbIp { get; set; }

Optional. The IP address of a global-access-enabled L4 ILB that is the next hop for matching packets. For this version, only nextHopIlbIp is supported.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NextHopOtherRoutes
    
    
    public PolicyBasedRoute.Types.OtherRoutes NextHopOtherRoutes { get; set; }

Optional. Other routes that will be referenced to determine the next hop of the packet.

**Property Value**  
---  
**Type** | **Description**  
`[PolicyBasedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute.Types)[OtherRoutes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute.Types.OtherRoutes)` |   
  
### PolicyBasedRouteName
    
    
    public PolicyBasedRouteName PolicyBasedRouteName { get; set; }

[PolicyBasedRouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRouteName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute#Google_Cloud_NetworkConnectivity_V1_PolicyBasedRoute_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[PolicyBasedRouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRouteName)` |   
  
### Priority
    
    
    public int Priority { get; set; }

Optional. The priority of this policy-based route. Priority is used to break ties in cases where there are more than one matching policy-based routes found. In cases where multiple policy-based routes are matched, the one with the lowest-numbered priority value wins. The default value is

  1. The priority value must be from 1 to 65535, inclusive.



**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### SelfLink
    
    
    public string SelfLink { get; set; }

Output only. Server-defined fully-qualified URL for this resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TargetCase
    
    
    public PolicyBasedRoute.TargetOneofCase TargetCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[PolicyBasedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)[TargetOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute.TargetOneofCase)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. Time when the policy-based route was updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### VirtualMachine
    
    
    public PolicyBasedRoute.Types.VirtualMachine VirtualMachine { get; set; }

Optional. VM instances that this policy-based route applies to.

**Property Value**  
---  
**Type** | **Description**  
`[PolicyBasedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute.Types)[VirtualMachine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute.Types.VirtualMachine)` |   
  
### Warnings
    
    
    public RepeatedField<PolicyBasedRoute.Types.Warnings> Warnings { get; }

Output only. If potential misconfigurations are detected for this route, this field will be populated with warning messages.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[PolicyBasedRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute.Types)[Warnings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoute.Types.Warnings)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
