---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RouterNat
title: Compute Engine v1 API - Class RouterNat (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:10:22.756981+00:00
---

# Compute Engine v1 API - Class RouterNat (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RouterNat

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class RouterNat (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class RouterNat : IMessage<RouterNat>, IEquatable<RouterNat>, IDeepCloneable<RouterNat>, IBufferMessage, IMessage

Reference documentation and code samples for the Compute Engine v1 API class RouterNat.

Represents a Nat resource. It enables the VMs within the specified subnetworks to access Internet without external IP addresses. It specifies a list of subnetworks (and the ranges within) that want to use NAT. Customers can also provide the external IPs that would be used for NAT. GCP would auto-allocate ephemeral IPs if no external IPs are provided.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RouterNat

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RouterNat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RouterNat), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RouterNat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RouterNat), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RouterNat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RouterNat), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### RouterNat()
    
    
    public RouterNat()

### RouterNat(RouterNat)
    
    
    public RouterNat(RouterNat other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RouterNat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RouterNat)`  
  
  
## Properties 

### AutoNetworkTier
    
    
    public string AutoNetworkTier { get; set; }

The network tier to use when automatically reserving NAT IP addresses. Must be one of: PREMIUM, STANDARD. If not specified, then the current project-level default tier is used. Check the AutoNetworkTier enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DrainNatIps
    
    
    public RepeatedField<string> DrainNatIps { get; }

A list of URLs of the IP resources to be drained. These IPs must be valid static external IPs that have been assigned to the NAT. These IPs should be used for updating/patching a NAT only.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EffectiveTcpTimeWaitTimeoutSec
    
    
    public int EffectiveTcpTimeWaitTimeoutSec { get; set; }

Output only. Effective timeout (in seconds) for TCP connections that are in TIME_WAIT state. This value is equal to tcp_time_wait_timeout_sec. If tcp_time_wait_timeout_sec isn't set, the effective timeout is 30s or 120s. The field is output only.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### EnableDynamicPortAllocation
    
    
    public bool EnableDynamicPortAllocation { get; set; }

Enable Dynamic Port Allocation.

If not specified, it is disabled by default.

If set to true,

  * Dynamic Port Allocation will be enabled on this NAT config.
  * enableEndpointIndependentMapping cannot be set to true.
  * If minPorts is set, minPortsPerVm must be set to a power of two greater than or equal to 32. If minPortsPerVm is not set, a minimum of 32 ports will be allocated to a VM from this NAT config.



**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EnableEndpointIndependentMapping
    
    
    public bool EnableEndpointIndependentMapping { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EndpointTypes
    
    
    public RepeatedField<string> EndpointTypes { get; }

List of NAT-ted endpoint types supported by the Nat Gateway. If the list is empty, then it will be equivalent to include ENDPOINT_TYPE_VM Check the EndpointTypes enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasAutoNetworkTier
    
    
    public bool HasAutoNetworkTier { get; }

Gets whether the "auto_network_tier" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasEffectiveTcpTimeWaitTimeoutSec
    
    
    public bool HasEffectiveTcpTimeWaitTimeoutSec { get; }

Gets whether the "effective_tcp_time_wait_timeout_sec" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasEnableDynamicPortAllocation
    
    
    public bool HasEnableDynamicPortAllocation { get; }

Gets whether the "enable_dynamic_port_allocation" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasEnableEndpointIndependentMapping
    
    
    public bool HasEnableEndpointIndependentMapping { get; }

Gets whether the "enable_endpoint_independent_mapping" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasIcmpIdleTimeoutSec
    
    
    public bool HasIcmpIdleTimeoutSec { get; }

Gets whether the "icmp_idle_timeout_sec" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMaxPortsPerVm
    
    
    public bool HasMaxPortsPerVm { get; }

Gets whether the "max_ports_per_vm" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMinPortsPerVm
    
    
    public bool HasMinPortsPerVm { get; }

Gets whether the "min_ports_per_vm" field is set

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
  
### HasNatIpAllocateOption
    
    
    public bool HasNatIpAllocateOption { get; }

Gets whether the "nat_ip_allocate_option" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSourceSubnetworkIpRangesToNat
    
    
    public bool HasSourceSubnetworkIpRangesToNat { get; }

Gets whether the "source_subnetwork_ip_ranges_to_nat" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSourceSubnetworkIpRangesToNat64
    
    
    public bool HasSourceSubnetworkIpRangesToNat64 { get; }

Gets whether the "source_subnetwork_ip_ranges_to_nat64" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTcpEstablishedIdleTimeoutSec
    
    
    public bool HasTcpEstablishedIdleTimeoutSec { get; }

Gets whether the "tcp_established_idle_timeout_sec" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTcpTimeWaitTimeoutSec
    
    
    public bool HasTcpTimeWaitTimeoutSec { get; }

Gets whether the "tcp_time_wait_timeout_sec" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTcpTransitoryIdleTimeoutSec
    
    
    public bool HasTcpTransitoryIdleTimeoutSec { get; }

Gets whether the "tcp_transitory_idle_timeout_sec" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasType
    
    
    public bool HasType { get; }

Gets whether the "type" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasUdpIdleTimeoutSec
    
    
    public bool HasUdpIdleTimeoutSec { get; }

Gets whether the "udp_idle_timeout_sec" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IcmpIdleTimeoutSec
    
    
    public int IcmpIdleTimeoutSec { get; set; }

Timeout (in seconds) for ICMP connections. Defaults to 30s if not set.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### LogConfig
    
    
    public RouterNatLogConfig LogConfig { get; set; }

Configure logging on this NAT.

**Property Value**  
---  
**Type** | **Description**  
`[RouterNatLogConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RouterNatLogConfig)` |   
  
### MaxPortsPerVm
    
    
    public int MaxPortsPerVm { get; set; }

Maximum number of ports allocated to a VM from this NAT config when Dynamic Port Allocation is enabled.

If Dynamic Port Allocation is not enabled, this field has no effect.

If Dynamic Port Allocation is enabled, and this field is set, it must be set to a power of two greater than minPortsPerVm, or 64 if minPortsPerVm is not set.

If Dynamic Port Allocation is enabled and this field is not set, a maximum of 65536 ports will be allocated to a VM from this NAT config.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MinPortsPerVm
    
    
    public int MinPortsPerVm { get; set; }

Minimum number of ports allocated to a VM from this NAT config. If not set, a default number of ports is allocated to a VM. This is rounded up to the nearest power of 2. For example, if the value of this field is 50, at least 64 ports are allocated to a VM.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Name
    
    
    public string Name { get; set; }

Unique name of this Nat service. The name must be 1-63 characters long and comply withRFC1035.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Nat64Subnetworks
    
    
    public RepeatedField<RouterNatSubnetworkToNat64> Nat64Subnetworks { get; }

List of Subnetwork resources whose traffic should be translated by NAT64 Gateway. It is used only when LIST_OF_IPV6_SUBNETWORKS is selected for the SubnetworkIpRangeToNat64Option above.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[RouterNatSubnetworkToNat64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RouterNatSubnetworkToNat64)` |   
  
### NatIpAllocateOption
    
    
    public string NatIpAllocateOption { get; set; }

Specify the NatIpAllocateOption, which can take one of the following values:

  * MANUAL_ONLY: Uses only Nat IP addresses provided by customers. When there are not enough specified Nat IPs, the Nat service fails for new VMs.
  * AUTO_ONLY: Nat IPs are allocated by Google Cloud Platform; customers can't specify any Nat IPs. When choosing AUTO_ONLY, then nat_ip should be empty. Check the NatIpAllocateOption enum for the list of possible values.



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NatIps
    
    
    public RepeatedField<string> NatIps { get; }

A list of URLs of the IP resources used for this Nat service. These IP addresses must be valid static external IP addresses assigned to the project.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Rules
    
    
    public RepeatedField<RouterNatRule> Rules { get; }

A list of rules associated with this NAT.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[RouterNatRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RouterNatRule)` |   
  
### SourceSubnetworkIpRangesToNat
    
    
    public string SourceSubnetworkIpRangesToNat { get; set; }

Specify the Nat option, which can take one of the following values:

  * ALL_SUBNETWORKS_ALL_IP_RANGES: All of the IP ranges in every Subnetwork are allowed to Nat.
  * ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES: All of the primary IP ranges in every Subnetwork are allowed to Nat.
  * LIST_OF_SUBNETWORKS: A list of Subnetworks are allowed to Nat (specified in the field subnetwork below)



The default is SUBNETWORK_IP_RANGE_TO_NAT_OPTION_UNSPECIFIED. Note that if this field contains ALL_SUBNETWORKS_ALL_IP_RANGES then there should not be any other Router.Nat section in any Router for this network in this region. Check the SourceSubnetworkIpRangesToNat enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SourceSubnetworkIpRangesToNat64
    
    
    public string SourceSubnetworkIpRangesToNat64 { get; set; }

Specify the Nat option for NAT64, which can take one of the following values:

  * ALL_IPV6_SUBNETWORKS: All of the IP ranges in every Subnetwork are allowed to Nat.
  * LIST_OF_IPV6_SUBNETWORKS: A list of Subnetworks are allowed to Nat (specified in the field nat64_subnetwork below)



The default is NAT64_OPTION_UNSPECIFIED. Note that if this field contains NAT64_ALL_V6_SUBNETWORKS no other Router.Nat section in this region can also enable NAT64 for any Subnetworks in this network. Other Router.Nat sections can still be present to enable NAT44 only. Check the SourceSubnetworkIpRangesToNat64 enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Subnetworks
    
    
    public RepeatedField<RouterNatSubnetworkToNat> Subnetworks { get; }

A list of Subnetwork resources whose traffic should be translated by NAT Gateway. It is used only when LIST_OF_SUBNETWORKS is selected for the SubnetworkIpRangeToNatOption above.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[RouterNatSubnetworkToNat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RouterNatSubnetworkToNat)` |   
  
### TcpEstablishedIdleTimeoutSec
    
    
    public int TcpEstablishedIdleTimeoutSec { get; set; }

Timeout (in seconds) for TCP established connections. Defaults to 1200s if not set.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### TcpTimeWaitTimeoutSec
    
    
    public int TcpTimeWaitTimeoutSec { get; set; }

Timeout (in seconds) for TCP connections that are in TIME_WAIT state. Defaults to 120s if not set.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### TcpTransitoryIdleTimeoutSec
    
    
    public int TcpTransitoryIdleTimeoutSec { get; set; }

Timeout (in seconds) for TCP transitory connections. Defaults to 30s if not set.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Type
    
    
    public string Type { get; set; }

Indicates whether this NAT is used for public or private IP translation. If unspecified, it defaults to PUBLIC. Check the Type enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UdpIdleTimeoutSec
    
    
    public int UdpIdleTimeoutSec { get; set; }

Timeout (in seconds) for UDP connections. Defaults to 30s if not set.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
