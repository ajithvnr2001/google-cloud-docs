---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AccessConfig
title: Compute Engine v1 API - Class AccessConfig (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:24:51.946255+00:00
---

# Compute Engine v1 API - Class AccessConfig (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AccessConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class AccessConfig (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class AccessConfig : IMessage<AccessConfig>, IEquatable<AccessConfig>, IDeepCloneable<AccessConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Compute Engine v1 API class AccessConfig.

An access configuration attached to an instance's network interface. Only one access config per instance is supported.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AccessConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AccessConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AccessConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AccessConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AccessConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AccessConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AccessConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### AccessConfig()
    
    
    public AccessConfig()

### AccessConfig(AccessConfig)
    
    
    public AccessConfig(AccessConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AccessConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AccessConfig)`  
  
  
## Properties 

### ExternalIpv6
    
    
    public string ExternalIpv6 { get; set; }

Applies to ipv6AccessConfigs only. The first IPv6 address of the external IPv6 range associated with this instance, prefix length is stored inexternalIpv6PrefixLength in ipv6AccessConfig. To use a static external IP address, it must be unused and in the same region as the instance's zone. If not specified, Google Cloud will automatically assign an external IPv6 address from the instance's subnetwork.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ExternalIpv6PrefixLength
    
    
    public int ExternalIpv6PrefixLength { get; set; }

Applies to ipv6AccessConfigs only. The prefix length of the external IPv6 range.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### HasExternalIpv6
    
    
    public bool HasExternalIpv6 { get; }

Gets whether the "external_ipv6" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasExternalIpv6PrefixLength
    
    
    public bool HasExternalIpv6PrefixLength { get; }

Gets whether the "external_ipv6_prefix_length" field is set

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
  
### HasNatIP
    
    
    public bool HasNatIP { get; }

Gets whether the "nat_i_p" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasNetworkTier
    
    
    public bool HasNetworkTier { get; }

Gets whether the "network_tier" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasPublicPtrDomainName
    
    
    public bool HasPublicPtrDomainName { get; }

Gets whether the "public_ptr_domain_name" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSecurityPolicy
    
    
    public bool HasSecurityPolicy { get; }

Gets whether the "security_policy" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSetPublicPtr
    
    
    public bool HasSetPublicPtr { get; }

Gets whether the "set_public_ptr" field is set

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
  
### Kind
    
    
    public string Kind { get; set; }

Output only. [Output Only] Type of the resource. Alwayscompute#accessConfig for access configs.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

The name of this access configuration. In accessConfigs (IPv4), the default and recommended name is External NAT, but you can use any arbitrary string, such as My external IP orNetwork Access. In ipv6AccessConfigs, the recommend name is External IPv6.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NatIP
    
    
    public string NatIP { get; set; }

Applies to accessConfigs (IPv4) only. Anexternal IP address associated with this instance. Specify an unused static external IP address available to the project or leave this field undefined to use an IP from a shared ephemeral IP address pool. If you specify a static external IP address, it must live in the same region as the zone of the instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NetworkTier
    
    
    public string NetworkTier { get; set; }

This signifies the networking tier used for configuring this access configuration and can only take the following values: PREMIUM,STANDARD.

If an AccessConfig is specified without a valid external IP address, an ephemeral IP will be created with this networkTier.

If an AccessConfig with a valid external IP address is specified, it must match that of the networkTier associated with the Address resource owning that IP. Check the NetworkTier enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PublicPtrDomainName
    
    
    public string PublicPtrDomainName { get; set; }

The DNS domain name for the public PTR record.

You can set this field only if the `setPublicPtr` field is enabled inaccessConfig. If this field is unspecified inipv6AccessConfig, a default PTR record will be created for first IP in associated external IPv6 range.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SecurityPolicy
    
    
    public string SecurityPolicy { get; set; }

The resource URL for the security policy associated with this access config.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SetPublicPtr
    
    
    public bool SetPublicPtr { get; set; }

Specifies whether a public DNS 'PTR' record should be created to map the external IP address of the instance to a DNS domain name.

This field is not used in ipv6AccessConfig. A default PTR record will be created if the VM has external IPv6 range associated.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Type
    
    
    public string Type { get; set; }

The type of configuration. In accessConfigs (IPv4), the default and only option is ONE_TO_ONE_NAT. Inipv6AccessConfigs, the default and only option isDIRECT_IPV6. Check the Type enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
