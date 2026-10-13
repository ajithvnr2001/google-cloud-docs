---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route
title: Network Connectivity v1beta API - Class Route (1.0.0-beta02) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:26.146547+00:00
---

# Network Connectivity v1beta API - Class Route (1.0.0-beta02)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Connectivity v1beta API - Class Route (1.0.0-beta02) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta02 (latest)  1.0.0-beta01 
    
    
    public sealed class Route : IMessage<Route>, IEquatable<Route>, IDeepCloneable<Route>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Connectivity v1beta API class Route.

A route defines a path from VM instances within a spoke to a specific destination resource. Only VPC spokes have routes.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Route

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkConnectivity.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta)

## Assembly

Google.Cloud.NetworkConnectivity.V1Beta.dll

## Constructors 

### Route()
    
    
    public Route()

### Route(Route)
    
    
    public Route(Route other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route)`  
  
  
## Properties 

### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The time the route was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Description
    
    
    public string Description { get; set; }

An optional description of the route.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HubRouteName
    
    
    public HubRouteName HubRouteName { get; set; }

[HubRouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubRouteName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route#Google_Cloud_NetworkConnectivity_V1Beta_Route_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[HubRouteName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.HubRouteName)` |   
  
### IpCidrRange
    
    
    public string IpCidrRange { get; set; }

The destination IP address range.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Optional labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements).

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Location
    
    
    public string Location { get; set; }

Output only. The origin location of the route. Uses the following form: "projects/{project}/locations/{location}" Example: projects/1234/locations/us-central1

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Immutable. The name of the route. Route names must be unique. Route names use the following form: `projects/{project_number}/locations/global/hubs/{hub}/routeTables/{route_table_id}/routes/{route_id}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NextHopInterconnectAttachment
    
    
    public NextHopInterconnectAttachment NextHopInterconnectAttachment { get; set; }

Immutable. The next-hop VLAN attachment for packets on this route.

**Property Value**  
---  
**Type** | **Description**  
`[NextHopInterconnectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.NextHopInterconnectAttachment)` |   
  
### NextHopRouterApplianceInstance
    
    
    public NextHopRouterApplianceInstance NextHopRouterApplianceInstance { get; set; }

Immutable. The next-hop Router appliance instance for packets on this route.

**Property Value**  
---  
**Type** | **Description**  
`[NextHopRouterApplianceInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.NextHopRouterApplianceInstance)` |   
  
### NextHopSpoke
    
    
    public NextHopSpoke NextHopSpoke { get; set; }

Immutable. The next-hop spoke for packets on this route.

**Property Value**  
---  
**Type** | **Description**  
`[NextHopSpoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.NextHopSpoke)` |   
  
### NextHopVpcNetwork
    
    
    public NextHopVpcNetwork NextHopVpcNetwork { get; set; }

Immutable. The destination VPC network for packets on this route.

**Property Value**  
---  
**Type** | **Description**  
`[NextHopVpcNetwork](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.NextHopVpcNetwork)` |   
  
### NextHopVpnTunnel
    
    
    public NextHopVPNTunnel NextHopVpnTunnel { get; set; }

Immutable. The next-hop VPN tunnel for packets on this route.

**Property Value**  
---  
**Type** | **Description**  
`[NextHopVPNTunnel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.NextHopVPNTunnel)` |   
  
### Priority
    
    
    public long Priority { get; set; }

Output only. The priority of this route. Priority is used to break ties in cases where a destination matches more than one route. In these cases the route with the lowest-numbered priority value wins.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### Spoke
    
    
    public string Spoke { get; set; }

Immutable. The spoke that this route leads to. Example: projects/12345/locations/global/spokes/SPOKE

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SpokeAsSpokeName
    
    
    public SpokeName SpokeAsSpokeName { get; set; }

[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)-typed view over the [Spoke](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Route#Google_Cloud_NetworkConnectivity_V1Beta_Route_Spoke) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SpokeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SpokeName)` |   
  
### State
    
    
    public State State { get; set; }

Output only. The current lifecycle state of the route.

**Property Value**  
---  
**Type** | **Description**  
`[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.State)` |   
  
### Type
    
    
    public RouteType Type { get; set; }

Output only. The route's type. Its type is determined by the properties of its IP address range.

**Property Value**  
---  
**Type** | **Description**  
`[RouteType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.RouteType)` |   
  
### Uid
    
    
    public string Uid { get; set; }

Output only. The Google-generated UUID for the route. This value is unique across all Network Connectivity Center route resources. If a route is deleted and another with the same name is created, the new route is assigned a different `uid`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. The time the route was last updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
