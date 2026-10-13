---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationSlot
title: Compute Engine v1 API - Class ReservationSlot (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:24.621542+00:00
---

# Compute Engine v1 API - Class ReservationSlot (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationSlot

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class ReservationSlot (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ReservationSlot : IMessage<ReservationSlot>, IEquatable<ReservationSlot>, IDeepCloneable<ReservationSlot>, IBufferMessage, IMessage

Reference documentation and code samples for the Compute Engine v1 API class ReservationSlot.

Represents a reservation slot resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ReservationSlot

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ReservationSlot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationSlot), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ReservationSlot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationSlot), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ReservationSlot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationSlot), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### ReservationSlot()
    
    
    public ReservationSlot()

### ReservationSlot(ReservationSlot)
    
    
    public ReservationSlot(ReservationSlot other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ReservationSlot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationSlot)`  
  
  
## Properties 

### CreationTimestamp
    
    
    public string CreationTimestamp { get; set; }

Output only. [Output Only] The creation timestamp, formatted asRFC3339 text.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasCreationTimestamp
    
    
    public bool HasCreationTimestamp { get; }

Gets whether the "creation_timestamp" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasId
    
    
    public bool HasId { get; }

Gets whether the "id" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasKind
    
    
    public bool HasKind { get; }

Gets whether the "kind" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasName
    
    
    public bool HasName { get; }

Gets whether the "name" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSelfLink
    
    
    public bool HasSelfLink { get; }

Gets whether the "self_link" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSelfLinkWithId
    
    
    public bool HasSelfLinkWithId { get; }

Gets whether the "self_link_with_id" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasState
    
    
    public bool HasState { get; }

Gets whether the "state" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasZone
    
    
    public bool HasZone { get; }

Gets whether the "zone" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Id
    
    
    public ulong Id { get; set; }

Output only. [Output Only] The unique identifier for this resource. This identifier is defined by the server.

**Property Value**  
---  
**Type** | **Description**  
`[ulong](https://learn.microsoft.com/dotnet/api/system.uint64)` |   
  
### Kind
    
    
    public string Kind { get; set; }

Output only. [Output Only] The type of resource. Alwayscompute#reservationSlot for reservation slots.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. [Output Only] The name of the reservation slot.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PhysicalTopology
    
    
    public ReservationSlotPhysicalTopology PhysicalTopology { get; set; }

Output only. [Output Only] The physical topology of the reservation slot.

**Property Value**  
---  
**Type** | **Description**  
`[ReservationSlotPhysicalTopology](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationSlotPhysicalTopology)` |   
  
### SelfLink
    
    
    public string SelfLink { get; set; }

Output only. [Output Only] A server-defined fully-qualified URL for this resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SelfLinkWithId
    
    
    public string SelfLinkWithId { get; set; }

Output only. [Output Only] A server-defined URL for this resource with the resource ID.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ShareSettings
    
    
    public ShareSettings ShareSettings { get; set; }

Specify share settings to create a shared slot. Set to empty to inherit the share settings from a parent resource.

**Property Value**  
---  
**Type** | **Description**  
`[ShareSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ShareSettings)` |   
  
### State
    
    
    public string State { get; set; }

Output only. [Output Only] The state of the reservation slot. Check the State enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Status
    
    
    public ReservationSlotStatus Status { get; set; }

Output only. [Output Only] The status of the reservation slot.

**Property Value**  
---  
**Type** | **Description**  
`[ReservationSlotStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationSlotStatus)` |   
  
### Zone
    
    
    public string Zone { get; set; }

Output only. [Output Only] The zone in which the reservation slot resides.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
