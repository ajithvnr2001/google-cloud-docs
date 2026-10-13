---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentL2Forwarding
title: Compute Engine v1 API - Class InterconnectAttachmentL2Forwarding (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:46.626841+00:00
---

# Compute Engine v1 API - Class InterconnectAttachmentL2Forwarding (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentL2Forwarding

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class InterconnectAttachmentL2Forwarding (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class InterconnectAttachmentL2Forwarding : IMessage<InterconnectAttachmentL2Forwarding>, IEquatable<InterconnectAttachmentL2Forwarding>, IDeepCloneable<InterconnectAttachmentL2Forwarding>, IBufferMessage, IMessage

Reference documentation and code samples for the Compute Engine v1 API class InterconnectAttachmentL2Forwarding.

L2 Interconnect Attachment related configuration.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > InterconnectAttachmentL2Forwarding

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[InterconnectAttachmentL2Forwarding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentL2Forwarding), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[InterconnectAttachmentL2Forwarding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentL2Forwarding), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[InterconnectAttachmentL2Forwarding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentL2Forwarding), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### InterconnectAttachmentL2Forwarding()
    
    
    public InterconnectAttachmentL2Forwarding()

### InterconnectAttachmentL2Forwarding(InterconnectAttachmentL2Forwarding)
    
    
    public InterconnectAttachmentL2Forwarding(InterconnectAttachmentL2Forwarding other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[InterconnectAttachmentL2Forwarding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentL2Forwarding)`  
  
  
## Properties 

### ApplianceMappings
    
    
    public MapField<string, InterconnectAttachmentL2ForwardingApplianceMapping> ApplianceMappings { get; }

Optional. A map of VLAN tags to appliances and optional inner mapping rules. If VLANs are not explicitly mapped to any appliance, the defaultApplianceIpAddress is used.

Each VLAN tag can be a single number or a range of numbers in the range of 1 to 4094, e.g., "1" or "4001-4094". Non-empty and non-overlapping VLAN tag ranges are enforced, and violating operations will be rejected.

The VLAN tags in the Ethernet header must use an ethertype value of 0x88A8 or 0x8100.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[InterconnectAttachmentL2ForwardingApplianceMapping](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentL2ForwardingApplianceMapping)` |   
  
### DefaultApplianceIpAddress
    
    
    public string DefaultApplianceIpAddress { get; set; }

Optional. A single IPv4 or IPv6 address used as the default destination IP when there is no VLAN mapping result found.

Unset field (null-value) indicates the unmatched packet should be dropped.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### GeneveHeader
    
    
    public InterconnectAttachmentL2ForwardingGeneveHeader GeneveHeader { get; set; }

Optional. It represents the structure of a Geneve (Generic Network Virtualization Encapsulation) header, as defined in RFC8926. It encapsulates packets from various protocols (e.g., Ethernet, IPv4, IPv6) for use in network virtualization environments.

**Property Value**  
---  
**Type** | **Description**  
`[InterconnectAttachmentL2ForwardingGeneveHeader](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentL2ForwardingGeneveHeader)` |   
  
### HasDefaultApplianceIpAddress
    
    
    public bool HasDefaultApplianceIpAddress { get; }

Gets whether the "default_appliance_ip_address" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasNetwork
    
    
    public bool HasNetwork { get; }

Gets whether the "network" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTunnelEndpointIpAddress
    
    
    public bool HasTunnelEndpointIpAddress { get; }

Gets whether the "tunnel_endpoint_ip_address" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Network
    
    
    public string Network { get; set; }

Required. Resource URL of the network to which this attachment belongs.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TunnelEndpointIpAddress
    
    
    public string TunnelEndpointIpAddress { get; set; }

Required. A single IPv4 or IPv6 address. This address will be used as the source IP address for packets sent to the appliances, and must be used as the destination IP address for packets that should be sent out through this attachment.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
