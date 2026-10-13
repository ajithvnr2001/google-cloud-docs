---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1beta/latest/Google-Cloud-NetworkConnectivity-V1beta-LinkedVpcNetwork/
title: Network Connectivity V1BETA API - Class Google::Cloud::NetworkConnectivity::V1beta::LinkedVpcNetwork (v0.3.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:43:59.567071+00:00
---

# Network Connectivity V1BETA API - Class Google::Cloud::NetworkConnectivity::V1beta::LinkedVpcNetwork (v0.3.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1beta/latest/Google-Cloud-NetworkConnectivity-V1beta-LinkedVpcNetwork/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Connectivity V1BETA API - Class Google::Cloud::NetworkConnectivity::V1beta::LinkedVpcNetwork (v0.3.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.2 (latest)  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Network Connectivity V1BETA API class Google::Cloud::NetworkConnectivity::V1beta::LinkedVpcNetwork.

An existing VPC network.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #exclude_export_ranges
    
    
    def exclude_export_ranges() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. IP ranges encompassing the subnets to be excluded from peering. 



### #exclude_export_ranges=
    
    
    def exclude_export_ranges=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. IP ranges encompassing the subnets to be excluded from peering. 



**Returns**

  * (::Array<::String>) — Optional. IP ranges encompassing the subnets to be excluded from peering. 



### #include_export_ranges
    
    
    def include_export_ranges() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. IP ranges allowed to be included from peering. 



### #include_export_ranges=
    
    
    def include_export_ranges=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. IP ranges allowed to be included from peering. 



**Returns**

  * (::Array<::String>) — Optional. IP ranges allowed to be included from peering. 



### #producer_vpc_spokes
    
    
    def producer_vpc_spokes() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. The list of Producer VPC spokes that this VPC spoke is a service consumer VPC spoke for. These producer VPCs are connected through VPC peering to this spoke's backing VPC network. Because they are directly connected through VPC peering, NCC export filters do not apply between the service consumer VPC spoke and any of its producer VPC spokes. This VPC spoke cannot be deleted as long as any of these producer VPC spokes are connected to the NCC Hub. 



### #proposed_exclude_export_ranges
    
    
    def proposed_exclude_export_ranges() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. The proposed exclude export IP ranges waiting for hub administrator's approval. 



### #proposed_include_export_ranges
    
    
    def proposed_include_export_ranges() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. The proposed include export IP ranges waiting for hub administrator's approval. 



### #uri
    
    
    def uri() -> ::String

**Returns**

  * (::String) — Required. The URI of the VPC network resource. 



### #uri=
    
    
    def uri=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The URI of the VPC network resource. 



**Returns**

  * (::String) — Required. The URI of the VPC network resource. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
