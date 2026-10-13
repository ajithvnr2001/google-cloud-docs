---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RouterStatusNatStatus/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::RouterStatusNatStatus (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:21:30.521539+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::RouterStatusNatStatus (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RouterStatusNatStatus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::RouterStatusNatStatus (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::RouterStatusNatStatus.

Status of a NAT contained in this router.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #auto_allocated_nat_ips
    
    
    def auto_allocated_nat_ips() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. A list of IPs auto-allocated for NAT. Example: ["1.1.1.1", "129.2.16.89"] 



### #auto_allocated_nat_ips=
    
    
    def auto_allocated_nat_ips=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Output only. A list of IPs auto-allocated for NAT. Example: ["1.1.1.1", "129.2.16.89"] 



**Returns**

  * (::Array<::String>) — Output only. A list of IPs auto-allocated for NAT. Example: ["1.1.1.1", "129.2.16.89"] 



### #drain_auto_allocated_nat_ips
    
    
    def drain_auto_allocated_nat_ips() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. A list of IPs auto-allocated for NAT that are in drain mode. Example: ["1.1.1.1", "179.12.26.133"]. 



### #drain_auto_allocated_nat_ips=
    
    
    def drain_auto_allocated_nat_ips=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Output only. A list of IPs auto-allocated for NAT that are in drain mode. Example: ["1.1.1.1", "179.12.26.133"]. 



**Returns**

  * (::Array<::String>) — Output only. A list of IPs auto-allocated for NAT that are in drain mode. Example: ["1.1.1.1", "179.12.26.133"]. 



### #drain_user_allocated_nat_ips
    
    
    def drain_user_allocated_nat_ips() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. A list of IPs user-allocated for NAT that are in drain mode. Example: ["1.1.1.1", "179.12.26.133"]. 



### #drain_user_allocated_nat_ips=
    
    
    def drain_user_allocated_nat_ips=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Output only. A list of IPs user-allocated for NAT that are in drain mode. Example: ["1.1.1.1", "179.12.26.133"]. 



**Returns**

  * (::Array<::String>) — Output only. A list of IPs user-allocated for NAT that are in drain mode. Example: ["1.1.1.1", "179.12.26.133"]. 



### #min_extra_nat_ips_needed
    
    
    def min_extra_nat_ips_needed() -> ::Integer

**Returns**

  * (::Integer) — Output only. The number of extra IPs to allocate. This will be greater than 0 only if user-specified IPs are NOT enough to allow all configured VMs to use NAT. This value is meaningful only when auto-allocation of NAT IPs is _not_ used. 



### #min_extra_nat_ips_needed=
    
    
    def min_extra_nat_ips_needed=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. The number of extra IPs to allocate. This will be greater than 0 only if user-specified IPs are NOT enough to allow all configured VMs to use NAT. This value is meaningful only when auto-allocation of NAT IPs is _not_ used. 



**Returns**

  * (::Integer) — Output only. The number of extra IPs to allocate. This will be greater than 0 only if user-specified IPs are NOT enough to allow all configured VMs to use NAT. This value is meaningful only when auto-allocation of NAT IPs is _not_ used. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Unique name of this NAT. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. Unique name of this NAT. 



**Returns**

  * (::String) — Output only. Unique name of this NAT. 



### #num_vm_endpoints_with_nat_mappings
    
    
    def num_vm_endpoints_with_nat_mappings() -> ::Integer

**Returns**

  * (::Integer) — Output only. Number of VM endpoints (i.e., Nics) that can use NAT. 



### #num_vm_endpoints_with_nat_mappings=
    
    
    def num_vm_endpoints_with_nat_mappings=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. Number of VM endpoints (i.e., Nics) that can use NAT. 



**Returns**

  * (::Integer) — Output only. Number of VM endpoints (i.e., Nics) that can use NAT. 



### #rule_status
    
    
    def rule_status() -> ::Array<::Google::Cloud::Compute::V1::RouterStatusNatStatusNatRuleStatus>

**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::RouterStatusNatStatusNatRuleStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RouterStatusNatStatusNatRuleStatus)>) — Status of rules in this NAT. 



### #rule_status=
    
    
    def rule_status=(value) -> ::Array<::Google::Cloud::Compute::V1::RouterStatusNatStatusNatRuleStatus>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Compute::V1::RouterStatusNatStatusNatRuleStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RouterStatusNatStatusNatRuleStatus)>) — Status of rules in this NAT. 



**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::RouterStatusNatStatusNatRuleStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RouterStatusNatStatusNatRuleStatus)>) — Status of rules in this NAT. 



### #user_allocated_nat_ip_resources
    
    
    def user_allocated_nat_ip_resources() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. A list of fully qualified URLs of reserved IP address resources. 



### #user_allocated_nat_ip_resources=
    
    
    def user_allocated_nat_ip_resources=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Output only. A list of fully qualified URLs of reserved IP address resources. 



**Returns**

  * (::Array<::String>) — Output only. A list of fully qualified URLs of reserved IP address resources. 



### #user_allocated_nat_ips
    
    
    def user_allocated_nat_ips() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. A list of IPs user-allocated for NAT. They will be raw IP strings like "179.12.26.133". 



### #user_allocated_nat_ips=
    
    
    def user_allocated_nat_ips=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Output only. A list of IPs user-allocated for NAT. They will be raw IP strings like "179.12.26.133". 



**Returns**

  * (::Array<::String>) — Output only. A list of IPs user-allocated for NAT. They will be raw IP strings like "179.12.26.133". 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
