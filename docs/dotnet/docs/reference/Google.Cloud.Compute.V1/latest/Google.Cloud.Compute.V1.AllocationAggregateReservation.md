---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AllocationAggregateReservation
title: Compute Engine v1 API - Class AllocationAggregateReservation (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:26:02.340061+00:00
---

# Compute Engine v1 API - Class AllocationAggregateReservation (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AllocationAggregateReservation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class AllocationAggregateReservation (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class AllocationAggregateReservation : IMessage<AllocationAggregateReservation>, IEquatable<AllocationAggregateReservation>, IDeepCloneable<AllocationAggregateReservation>, IBufferMessage, IMessage

Reference documentation and code samples for the Compute Engine v1 API class AllocationAggregateReservation.

This reservation type is specified by total resource amounts (e.g. total count of CPUs) and can account for multiple instance SKUs. In other words, one can create instances of varying shapes against this reservation.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AllocationAggregateReservation

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AllocationAggregateReservation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AllocationAggregateReservation), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AllocationAggregateReservation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AllocationAggregateReservation), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AllocationAggregateReservation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AllocationAggregateReservation), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### AllocationAggregateReservation()
    
    
    public AllocationAggregateReservation()

### AllocationAggregateReservation(AllocationAggregateReservation)
    
    
    public AllocationAggregateReservation(AllocationAggregateReservation other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AllocationAggregateReservation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AllocationAggregateReservation)`  
  
  
## Properties 

### HasVmFamily
    
    
    public bool HasVmFamily { get; }

Gets whether the "vm_family" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasWorkloadType
    
    
    public bool HasWorkloadType { get; }

Gets whether the "workload_type" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InUseResources
    
    
    public RepeatedField<AllocationAggregateReservationReservedResourceInfo> InUseResources { get; }

Output only. [Output only] List of resources currently in use.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AllocationAggregateReservationReservedResourceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AllocationAggregateReservationReservedResourceInfo)` |   
  
### ReservedResources
    
    
    public RepeatedField<AllocationAggregateReservationReservedResourceInfo> ReservedResources { get; }

List of reserved resources (CPUs, memory, accelerators).

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AllocationAggregateReservationReservedResourceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AllocationAggregateReservationReservedResourceInfo)` |   
  
### VmFamily
    
    
    public string VmFamily { get; set; }

The VM family that all instances scheduled against this reservation must belong to. Check the VmFamily enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### WorkloadType
    
    
    public string WorkloadType { get; set; }

The workload type of the instances that will target this reservation. Check the WorkloadType enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
