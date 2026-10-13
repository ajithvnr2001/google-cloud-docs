---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType
title: Compute Engine v1 API - Class AcceleratorType (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:24:42.168658+00:00
---

# Compute Engine v1 API - Class AcceleratorType (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class AcceleratorType (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class AcceleratorType : IMessage<AcceleratorType>, IEquatable<AcceleratorType>, IDeepCloneable<AcceleratorType>, IBufferMessage, IMessage

Reference documentation and code samples for the Compute Engine v1 API class AcceleratorType.

Represents an Accelerator Type resource.

Google Cloud Platform provides graphics processing units (accelerators) that you can add to VM instances to improve or accelerate performance when working with intensive workloads. For more information, readGPUs on Compute Engine.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AcceleratorType

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### AcceleratorType()
    
    
    public AcceleratorType()

### AcceleratorType(AcceleratorType)
    
    
    public AcceleratorType(AcceleratorType other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType)`  
  
  
## Properties 

### CreationTimestamp
    
    
    public string CreationTimestamp { get; set; }

[Output Only] Creation timestamp inRFC3339 text format.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Deprecated
    
    
    public DeprecationStatus Deprecated { get; set; }

[Output Only] The deprecation status associated with this accelerator type.

**Property Value**  
---  
**Type** | **Description**  
`[DeprecationStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeprecationStatus)` |   
  
### Description
    
    
    public string Description { get; set; }

[Output Only] An optional textual description of the resource.

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
  
### HasDescription
    
    
    public bool HasDescription { get; }

Gets whether the "description" field is set

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
  
### HasMaximumCardsPerInstance
    
    
    public bool HasMaximumCardsPerInstance { get; }

Gets whether the "maximum_cards_per_instance" field is set

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
  
### HasZone
    
    
    public bool HasZone { get; }

Gets whether the "zone" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Id
    
    
    public ulong Id { get; set; }

[Output Only] The unique identifier for the resource. This identifier is defined by the server.

**Property Value**  
---  
**Type** | **Description**  
`[ulong](https://learn.microsoft.com/dotnet/api/system.uint64)` |   
  
### Kind
    
    
    public string Kind { get; set; }

Output only. [Output Only] The type of the resource. Alwayscompute#acceleratorType for accelerator types.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MaximumCardsPerInstance
    
    
    public int MaximumCardsPerInstance { get; set; }

[Output Only] Maximum number of accelerator cards allowed per instance.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Name
    
    
    public string Name { get; set; }

[Output Only] Name of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ResourceMetadata
    
    
    public ResourceMetadata ResourceMetadata { get; set; }

Output only. Contains standard resource metadata for an AcceleratorType resource. It is populated for each instance of the AcceleratorType resource, and includes the api_version the instance was retrieved through, and its canonical resource_type name.

**Property Value**  
---  
**Type** | **Description**  
`[ResourceMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ResourceMetadata)` |   
  
### SelfLink
    
    
    public string SelfLink { get; set; }

Output only. [Output Only] Server-defined, fully qualified URL for this resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Zone
    
    
    public string Zone { get; set; }

[Output Only] The name of the zone where the accelerator type resides, such as us-central1-a. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
