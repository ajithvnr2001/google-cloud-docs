---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Destination
title: Network Connectivity v1beta API - Class Destination (1.0.0-beta02) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:34.866515+00:00
---

# Network Connectivity v1beta API - Class Destination (1.0.0-beta02)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Destination

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Connectivity v1beta API - Class Destination (1.0.0-beta02) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta02 (latest)  1.0.0-beta01 
    
    
    public sealed class Destination : IMessage<Destination>, IEquatable<Destination>, IDeepCloneable<Destination>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Connectivity v1beta API class Destination.

The `Destination` resource. It specifies the IP prefix and the associated autonomous system numbers (ASN) that you want to include in a `MulticloudDataTransferConfig` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Destination

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Destination), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Destination), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Destination), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkConnectivity.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta)

## Assembly

Google.Cloud.NetworkConnectivity.V1Beta.dll

## Constructors 

### Destination()
    
    
    public Destination()

### Destination(Destination)
    
    
    public Destination(Destination other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Destination)`  
  
  
## Properties 

### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Time when the `Destination` resource was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Description
    
    
    public string Description { get; set; }

Optional. A description of this resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DestinationName
    
    
    public DestinationName DestinationName { get; set; }

[DestinationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.DestinationName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Destination#Google_Cloud_NetworkConnectivity_V1Beta_Destination_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[DestinationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.DestinationName)` |   
  
### Endpoints
    
    
    public RepeatedField<Destination.Types.DestinationEndpoint> Endpoints { get; }

Required. Unordered list. The list of `DestinationEndpoint` resources configured for the IP prefix.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Destination)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Destination.Types)[DestinationEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Destination.Types.DestinationEndpoint)` |   
  
### Etag
    
    
    public string Etag { get; set; }

The etag is computed by the server, and might be sent with update and delete requests so that the client has an up-to-date value before proceeding.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### IpPrefix
    
    
    public string IpPrefix { get; set; }

Required. Immutable. The IP prefix that represents your workload on another CSP.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Optional. User-defined labels.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. The name of the `Destination` resource. Format: `projects/{project}/locations/{location}/multicloudDataTransferConfigs/{multicloud_data_transfer_config}/destinations/{destination}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### StateTimeline
    
    
    public StateTimeline StateTimeline { get; set; }

Output only. The timeline of the expected `Destination` states or the current rest state. If a state change is expected, the value is `ADDING`, `DELETING` or `SUSPENDING`, depending on the action specified.

Example: "state_timeline": { "states": [ { // The time when the `Destination` resource will be activated. "effectiveTime": "2024-12-01T08:00:00Z", "state": "ADDING" }, { // The time when the `Destination` resource will be suspended. "effectiveTime": "2024-12-01T20:00:00Z", "state": "SUSPENDING" } ] }

**Property Value**  
---  
**Type** | **Description**  
`[StateTimeline](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.StateTimeline)` |   
  
### Uid
    
    
    public string Uid { get; set; }

Output only. The Google-generated unique ID for the `Destination` resource. This value is unique across all `Destination` resources. If a resource is deleted and another with the same name is created, the new resource is assigned a different and unique ID.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. Time when the `Destination` resource was updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
