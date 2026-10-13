---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-UsableSubnetwork/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::UsableSubnetwork (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:02:06.694442+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::UsableSubnetwork (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-UsableSubnetwork/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::UsableSubnetwork (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::UsableSubnetwork.

Subnetwork which the current user has compute.subnetworks.use permission on.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #external_ipv6_prefix
    
    
    def external_ipv6_prefix() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] The external IPv6 address range that is assigned to this subnetwork. 



### #external_ipv6_prefix=
    
    
    def external_ipv6_prefix=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] The external IPv6 address range that is assigned to this subnetwork. 



**Returns**

  * (::String) — Output only. [Output Only] The external IPv6 address range that is assigned to this subnetwork. 



### #internal_ipv6_prefix
    
    
    def internal_ipv6_prefix() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] The internal IPv6 address range that is assigned to this subnetwork. 



### #internal_ipv6_prefix=
    
    
    def internal_ipv6_prefix=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] The internal IPv6 address range that is assigned to this subnetwork. 



**Returns**

  * (::String) — Output only. [Output Only] The internal IPv6 address range that is assigned to this subnetwork. 



### #ip_cidr_range
    
    
    def ip_cidr_range() -> ::String

**Returns**

  * (::String) — The range of internal addresses that are owned by this subnetwork. 



### #ip_cidr_range=
    
    
    def ip_cidr_range=(value) -> ::String

**Parameter**

  * **value** (::String) — The range of internal addresses that are owned by this subnetwork. 



**Returns**

  * (::String) — The range of internal addresses that are owned by this subnetwork. 



### #ipv6_access_type
    
    
    def ipv6_access_type() -> ::String

**Returns**

  * (::String) — The access type of IPv6 address this subnet holds. It's immutable and can only be specified during creation or the first time the subnet is updated into IPV4_IPV6 dual stack. Check the Ipv6AccessType enum for the list of possible values. 



### #ipv6_access_type=
    
    
    def ipv6_access_type=(value) -> ::String

**Parameter**

  * **value** (::String) — The access type of IPv6 address this subnet holds. It's immutable and can only be specified during creation or the first time the subnet is updated into IPV4_IPV6 dual stack. Check the Ipv6AccessType enum for the list of possible values. 



**Returns**

  * (::String) — The access type of IPv6 address this subnet holds. It's immutable and can only be specified during creation or the first time the subnet is updated into IPV4_IPV6 dual stack. Check the Ipv6AccessType enum for the list of possible values. 



### #network
    
    
    def network() -> ::String

**Returns**

  * (::String) — Network URL. 



### #network=
    
    
    def network=(value) -> ::String

**Parameter**

  * **value** (::String) — Network URL. 



**Returns**

  * (::String) — Network URL. 



### #purpose
    
    
    def purpose() -> ::String

**Returns**

  * (::String) — Check the Purpose enum for the list of possible values. 



### #purpose=
    
    
    def purpose=(value) -> ::String

**Parameter**

  * **value** (::String) — Check the Purpose enum for the list of possible values. 



**Returns**

  * (::String) — Check the Purpose enum for the list of possible values. 



### #role
    
    
    def role() -> ::String

**Returns**

  * (::String) — The role of subnetwork. Currently, this field is only used when purpose is set to GLOBAL_MANAGED_PROXY orREGIONAL_MANAGED_PROXY. The value can be set toACTIVE or BACKUP. An ACTIVE subnetwork is one that is currently being used for Envoy-based load balancers in a region. A BACKUP subnetwork is one that is ready to be promoted to ACTIVE or is currently draining. This field can be updated with a patch request. Check the Role enum for the list of possible values. 



### #role=
    
    
    def role=(value) -> ::String

**Parameter**

  * **value** (::String) — The role of subnetwork. Currently, this field is only used when purpose is set to GLOBAL_MANAGED_PROXY orREGIONAL_MANAGED_PROXY. The value can be set toACTIVE or BACKUP. An ACTIVE subnetwork is one that is currently being used for Envoy-based load balancers in a region. A BACKUP subnetwork is one that is ready to be promoted to ACTIVE or is currently draining. This field can be updated with a patch request. Check the Role enum for the list of possible values. 



**Returns**

  * (::String) — The role of subnetwork. Currently, this field is only used when purpose is set to GLOBAL_MANAGED_PROXY orREGIONAL_MANAGED_PROXY. The value can be set toACTIVE or BACKUP. An ACTIVE subnetwork is one that is currently being used for Envoy-based load balancers in a region. A BACKUP subnetwork is one that is ready to be promoted to ACTIVE or is currently draining. This field can be updated with a patch request. Check the Role enum for the list of possible values. 



### #secondary_ip_ranges
    
    
    def secondary_ip_ranges() -> ::Array<::Google::Cloud::Compute::V1::UsableSubnetworkSecondaryRange>

**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::UsableSubnetworkSecondaryRange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-UsableSubnetworkSecondaryRange)>) — Secondary IP ranges. 



### #secondary_ip_ranges=
    
    
    def secondary_ip_ranges=(value) -> ::Array<::Google::Cloud::Compute::V1::UsableSubnetworkSecondaryRange>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Compute::V1::UsableSubnetworkSecondaryRange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-UsableSubnetworkSecondaryRange)>) — Secondary IP ranges. 



**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::UsableSubnetworkSecondaryRange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-UsableSubnetworkSecondaryRange)>) — Secondary IP ranges. 



### #stack_type
    
    
    def stack_type() -> ::String

**Returns**

  * (::String) — The stack type for the subnet. If set to IPV4_ONLY, new VMs in the subnet are assigned IPv4 addresses only. If set toIPV4_IPV6, new VMs in the subnet can be assigned both IPv4 and IPv6 addresses. If not specified, IPV4_ONLY is used.

This field can be both set at resource creation time and updated usingpatch. Check the StackType enum for the list of possible values. 




### #stack_type=
    
    
    def stack_type=(value) -> ::String

**Parameter**

  * **value** (::String) — The stack type for the subnet. If set to IPV4_ONLY, new VMs in the subnet are assigned IPv4 addresses only. If set toIPV4_IPV6, new VMs in the subnet can be assigned both IPv4 and IPv6 addresses. If not specified, IPV4_ONLY is used.

This field can be both set at resource creation time and updated usingpatch. Check the StackType enum for the list of possible values. 




**Returns**

  * (::String) — The stack type for the subnet. If set to IPV4_ONLY, new VMs in the subnet are assigned IPv4 addresses only. If set toIPV4_IPV6, new VMs in the subnet can be assigned both IPv4 and IPv6 addresses. If not specified, IPV4_ONLY is used.

This field can be both set at resource creation time and updated usingpatch. Check the StackType enum for the list of possible values. 




### #subnetwork
    
    
    def subnetwork() -> ::String

**Returns**

  * (::String) — Subnetwork URL. 



### #subnetwork=
    
    
    def subnetwork=(value) -> ::String

**Parameter**

  * **value** (::String) — Subnetwork URL. 



**Returns**

  * (::String) — Subnetwork URL. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
