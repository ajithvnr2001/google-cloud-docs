---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AllocationSpecificSKUAllocationReservedInstanceProperties
title: Compute Engine v1 API - Class AllocationSpecificSKUAllocationReservedInstanceProperties (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:26:12.092632+00:00
---

# Compute Engine v1 API - Class AllocationSpecificSKUAllocationReservedInstanceProperties (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AllocationSpecificSKUAllocationReservedInstanceProperties

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class AllocationSpecificSKUAllocationReservedInstanceProperties (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class AllocationSpecificSKUAllocationReservedInstanceProperties : IMessage<AllocationSpecificSKUAllocationReservedInstanceProperties>, IEquatable<AllocationSpecificSKUAllocationReservedInstanceProperties>, IDeepCloneable<AllocationSpecificSKUAllocationReservedInstanceProperties>, IBufferMessage, IMessage

Reference documentation and code samples for the Compute Engine v1 API class AllocationSpecificSKUAllocationReservedInstanceProperties.

Properties of the SKU instances being reserved. Next ID: 10

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AllocationSpecificSKUAllocationReservedInstanceProperties

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AllocationSpecificSKUAllocationReservedInstanceProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AllocationSpecificSKUAllocationReservedInstanceProperties), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AllocationSpecificSKUAllocationReservedInstanceProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AllocationSpecificSKUAllocationReservedInstanceProperties), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AllocationSpecificSKUAllocationReservedInstanceProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AllocationSpecificSKUAllocationReservedInstanceProperties), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### AllocationSpecificSKUAllocationReservedInstanceProperties()
    
    
    public AllocationSpecificSKUAllocationReservedInstanceProperties()

### AllocationSpecificSKUAllocationReservedInstanceProperties(AllocationSpecificSKUAllocationReservedInstanceProperties)
    
    
    public AllocationSpecificSKUAllocationReservedInstanceProperties(AllocationSpecificSKUAllocationReservedInstanceProperties other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AllocationSpecificSKUAllocationReservedInstanceProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AllocationSpecificSKUAllocationReservedInstanceProperties)`  
  
  
## Properties 

### GuestAccelerators
    
    
    public RepeatedField<AcceleratorConfig> GuestAccelerators { get; }

Specifies accelerator type and count.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AcceleratorConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorConfig)` |   
  
### HasLocationHint
    
    
    public bool HasLocationHint { get; }

Gets whether the "location_hint" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMachineType
    
    
    public bool HasMachineType { get; }

Gets whether the "machine_type" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMinCpuPlatform
    
    
    public bool HasMinCpuPlatform { get; }

Gets whether the "min_cpu_platform" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### LocalSsds
    
    
    public RepeatedField<AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk> LocalSsds { get; }

Specifies amount of local ssd to reserve with each instance. The type of disk is local-ssd.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk)` |   
  
### LocationHint
    
    
    public string LocationHint { get; set; }

An opaque location hint used to place the allocation close to other resources. This field is for use by internal tools that use the public API.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MachineType
    
    
    public string MachineType { get; set; }

Specifies type of machine (name only) which has fixed number of vCPUs and fixed amount of memory. This also includes specifying custom machine type following custom-NUMBER_OF_CPUS-AMOUNT_OF_MEMORY pattern.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MinCpuPlatform
    
    
    public string MinCpuPlatform { get; set; }

Minimum cpu platform the reservation.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
