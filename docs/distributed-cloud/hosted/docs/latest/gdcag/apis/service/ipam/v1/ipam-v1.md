---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/v1/ipam-v1/
title: KRM API ipam.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:32:33.392656+00:00
---

# KRM API ipam.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/v1/ipam-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API ipam.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## ipam.gdc.goog/v1

Contains API Schema definitions for the IP Address Management(IPAM) API group.

### CIDREntry

Represents a CIDR entry with IP version identified.

_Appears in:_ \- NetworkStatus

Field | Description  
---|---  
`version` _IPFamily_ | The IP address version of the entry.  
`cidr` _string_ | The CIDR of the entry.  
  
### ConsumerRef

_Appears in:_ \- SubnetStatus

Field | Description  
---|---  
`version` _string_ |   
`group` _string_ |   
`kind` _string_ |   
`name` _string_ |   
`namespace` _string_ |   
  
### NetworkSpec

Contains the information to set up network features for the `Subnet`.

_Appears in:_ \- SubnetSpec

Field | Description  
---|---  
`enableGateway` _boolean_ | Specifies whether a gateway IP address must be assigned for the subnet.  
`enableVLANID` _boolean_ | Specifies whether a VLAN ID must be assigned for the subnet.  
`staticVLANID` _integer_ | The dedicated VLAN ID. If this field is defined, the `VLANID` field must be `true`.  
  
### NetworkStatus

Contains the allocation result for the network configurations.

_Appears in:_ \- SubnetStatus

Field | Description  
---|---  
`vlanID` _integer_ | The VLAN ID acquired for the subnet.  
`gateways` _CIDREntry array_ | The gateway IP addresses acquired for the Subnet. If the Subnet is single-stack, there must be only one IPv4/IPv6 IP address in the list. If the subnet is dual-stack, there must be one IPv4 address and one IPv6 IP addresse in the list.  
  
### ReferenceType

_Underlying type:_ `string` Represents the type of the Subnets a SubnetReference is referencing to.

_Appears in:_ \- SubnetReference

### Subnet

Represents the request and allocation information of a zonal `Subnet`.

_Appears in:_ \- SubnetList

Field | Description  
---|---  
`apiVersion` _string_ | `ipam.gdc.goog/v1`  
`kind` _string_ | `Subnet`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _SubnetSpec_ |   
`status` _SubnetStatus_ |   
  
### SubnetAllocation

Contains a single IP version(IPv4/IPv6)'s CIDR allocation result of a `Subnet`.

_Appears in:_ \- SubnetStatus

Field | Description  
---|---  
`cidr` _string_ | The CIDR allocated to the Subnet.  
`availableCIDRs` _string array_ | The CIDRs left after excluding those consumed by the Subnet's children.  
  
### SubnetList

Represents a collection of `Subnet` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `ipam.gdc.goog/v1`  
`kind` _string_ | `SubnetList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Subnet array_ |   
  
### SubnetReference

Contains the information used to reference a single `Subnet`.

_Appears in:_ \- SubnetSpec \- SubnetStatus

Field | Description  
---|---  
`name` _string_ |   
`namespace` _string_ | The namespace of the referenced Subnet. If it's used in a spec, the namespace can be left empty, which means the referenced Subnet is in the same namespace as the object referencing it.  
`type` _ReferenceType_ | The type of the Subnet(s) this SubnetReference is referencing to, can be SingleSubnet/SubnetGroup.  
  
### SubnetRequest

Contains the IP addresses claiming information for a single IP address version (IPv4/IPv6).

_Appears in:_ \- SubnetSpec

Field | Description  
---|---  
`cidr` _string_ | The CIDR to allocate. This field must be specified when acquiring a dedicated CIDR.  
`prefixLength` _integer_ | The prefix length of the CIDR wanted. This field can be specified when there is no specific requirements on the CIDR to be allocated. If both CIDR and prefix are left empty, the request acquires a /32(IPv4) or /128(IPv6) random CIDR by default.  
  
### SubnetSpec

Defines the specification of a `Subnet`.

_Appears in:_ \- Subnet

Field | Description  
---|---  
`type` _SubnetType_ | The type of the Subnet in the context of the IPAM tree architecture.  
`ipv4Request` _SubnetRequest_ | The request details for acquiring the IPv4 CIDR.  
`ipv6Request` _SubnetRequest_ | The request details for acquiring the IPv6 CIDR.  
`parentReference` _SubnetReference_ | The reference to the parent of this Subnet. This Subnet will get IP allocated from the parent if specified. The parent name must be provided if there is a parent. Namespace of the parent can only be omitted when the parent is in the same namespace as this Subnet.  
`networkSpec` _NetworkSpec_ | The specification needed for setting up network configurations. If the `Subnet` doesn't have network implications, this field should be empty.  
  
### SubnetStatus

Defines the status of the `Subnet`.

_Appears in:_ \- Subnet

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`allocatedParent` _SubnetReference_ | The information of the single parent Subnet from which the CIDRs are allocated from. Empty if the Subnet doesn't have a parent.  
`ipv4Allocation` _SubnetAllocation_ | The allocation information for the IPv4 IP addresses.  
`ipv6Allocation` _SubnetAllocation_ | The allocation information for the IPv6 IP addresses.  
`childrenRefs` _SubnetReference array_ | The references to the children which are allocated from this subnet. This field doesn't apply to `Leaf` type subnets.  
`networkStatus` _NetworkStatus_ | The allocated result of network configurations.  
`consumerRef` _ConsumerRef_ | The active consumer of the subnet.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
