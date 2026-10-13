---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SubnetworkSecondaryRange
title: Compute Engine v1 API - Class SubnetworkSecondaryRange (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:10.324558+00:00
---

# Compute Engine v1 API - Class SubnetworkSecondaryRange (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SubnetworkSecondaryRange

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class SubnetworkSecondaryRange (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class SubnetworkSecondaryRange : IMessage<SubnetworkSecondaryRange>, IEquatable<SubnetworkSecondaryRange>, IDeepCloneable<SubnetworkSecondaryRange>, IBufferMessage, IMessage

Reference documentation and code samples for the Compute Engine v1 API class SubnetworkSecondaryRange.

Represents a secondary IP range of a subnetwork.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SubnetworkSecondaryRange

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SubnetworkSecondaryRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SubnetworkSecondaryRange), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SubnetworkSecondaryRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SubnetworkSecondaryRange), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SubnetworkSecondaryRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SubnetworkSecondaryRange), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### SubnetworkSecondaryRange()
    
    
    public SubnetworkSecondaryRange()

### SubnetworkSecondaryRange(SubnetworkSecondaryRange)
    
    
    public SubnetworkSecondaryRange(SubnetworkSecondaryRange other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SubnetworkSecondaryRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SubnetworkSecondaryRange)`  
  
  
## Properties 

### HasIpCidrRange
    
    
    public bool HasIpCidrRange { get; }

Gets whether the "ip_cidr_range" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasIpCollection
    
    
    public bool HasIpCollection { get; }

Gets whether the "ip_collection" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasIpVersion
    
    
    public bool HasIpVersion { get; }

Gets whether the "ip_version" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasRangeName
    
    
    public bool HasRangeName { get; }

Gets whether the "range_name" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasReservedInternalRange
    
    
    public bool HasReservedInternalRange { get; }

Gets whether the "reserved_internal_range" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IpCidrRange
    
    
    public string IpCidrRange { get; set; }

The range of IP addresses belonging to this subnetwork secondary range. Provide this property when you create the subnetwork. Ranges must be unique and non-overlapping with all primary and secondary IP ranges within a network. Both IPv4 and IPv6 ranges are supported. For IPv4, the range can be any range listed in theValid ranges list.

For IPv6: The range must have a /64 prefix length. The range must be omitted, for auto-allocation from Google-defined ULA IPv6 range. For BYOGUA internal IPv6 secondary range, the range may be specified along with the `ipCollection` field. If an `ipCollection` is specified, the requested ip_cidr_range must lie within the range of the PDP referenced by the `ipCollection` field for allocation. If `ipCollection` field is specified, but ip_cidr_range is not, the range is auto-allocated from the PDP referenced by the `ipCollection` field.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### IpCollection
    
    
    public string IpCollection { get; set; }

Reference to a Public Delegated Prefix (PDP) for BYOIP. This field should be specified for configuring BYOGUA internal IPv6 secondary range. When specified along with the ip_cidr_range, the ip_cidr_range must lie within the PDP referenced by the `ipCollection` field. When specified without the ip_cidr_range, the range is auto-allocated from the PDP referenced by the `ipCollection` field.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### IpVersion
    
    
    public string IpVersion { get; set; }

Check the IpVersion enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RangeName
    
    
    public string RangeName { get; set; }

The name associated with this subnetwork secondary range, used when adding an alias IP/IPv6 range to a VM instance. The name must be 1-63 characters long, and comply withRFC1035. The name must be unique within the subnetwork.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ReservedInternalRange
    
    
    public string ReservedInternalRange { get; set; }

The URL of the reserved internal range. Only IPv4 is supported.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
