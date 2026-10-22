---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/v1/global-ipam-v1/
title: KRM API ipam.global.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:08.491846+00:00
---

# KRM API ipam.global.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/v1/global-ipam-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API ipam.global.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## ipam.global.gdc.goog/v1

Contains API Schema definitions for the IP Address Management (IPAM) global API group.

### PropagationStatus

_Appears in:_ \- SubnetStatus

Field | Description  
---|---  
`zone` _string_ | The name of the zone in which the Subnet is propagated to.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
  
### Subnet

Represents the request and allocation information of a global IP address range in CIDR format.

_Appears in:_ \- SubnetList

Field | Description  
---|---  
`apiVersion` _string_ | `ipam.global.gdc.goog/v1`  
`kind` _string_ | `Subnet`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _SubnetSpec_ |   
`status` _SubnetStatus_ |   
  
### SubnetList

Represents a collection of `Subnet` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `ipam.global.gdc.goog/v1`  
`kind` _string_ | `SubnetList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Subnet array_ |   
  
### SubnetSpec

Defines the specification of a `Subnet`.

_Appears in:_ \- Subnet

Field | Description  
---|---  
`type` _SubnetType_ | The type of the Subnet in the context of the IPAM tree architecture.  
`ipv4Request` _SubnetRequest_ | The request details for acquiring the IPv4 CIDR.  
`ipv6Request` _SubnetRequest_ | The request details for acquiring the IPv6 CIDR.  
`zone` _string_ | The name of the zone which this Subnet belongs to. If left empty, it is treated as a global only resource.  
`parentReference` _SubnetReference_ | The reference to the parent of this Subnet. This Subnet will get IP allocated from the parent if specified. The parent name must be provided if there is a parent. Namespace of the parent can only be omitted when the parent is in the same namespace as this Subnet.  
`propagationStrategy` _ZonePropagationStrategy_ | The strategy used to propagate the Subnet to zonal API server.  
  
### SubnetStatus

Represents the status of the `Subnet`.

_Appears in:_ \- Subnet

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`allocatedParent` _SubnetReference_ | The information of the single parent Subnet from which the CIDRs are allocated from. Empty if the Subnet doesn't have a parent.  
`ipv4Allocation` _SubnetAllocation_ | The allocation information for the IPv4 IP addresses.  
`ipv6Allocation` _SubnetAllocation_ | The allocation information for the IPv6 IP addresses.  
`childrenRefs` _SubnetReference array_ | The references to the children which are allocated from this Subnet. This field doesn't apply to Leaf type Subnets.  
`zonePropagations` _PropagationStatus array_ | The propagation status of each zone that the Subnet propagated to. This field doesn't apply to Subnet without PropagationStrategy.  
`consumerRef` _ConsumerRef_ | The active consumer of the subnet.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
