---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlock/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ReservationSubBlock (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:51:06.607690+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ReservationSubBlock (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlock/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ReservationSubBlock (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::ReservationSubBlock.

Represents a reservation subBlock resource.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #accelerator_topologies_info
    
    
    def accelerator_topologies_info() -> ::Google::Cloud::Compute::V1::AcceleratorTopologiesInfo

**Returns**

  * ([::Google::Cloud::Compute::V1::AcceleratorTopologiesInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorTopologiesInfo)) — Output only. [Output Only] Slice info for the reservation subBlock. 



### #accelerator_topologies_info=
    
    
    def accelerator_topologies_info=(value) -> ::Google::Cloud::Compute::V1::AcceleratorTopologiesInfo

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::AcceleratorTopologiesInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorTopologiesInfo)) — Output only. [Output Only] Slice info for the reservation subBlock. 



**Returns**

  * ([::Google::Cloud::Compute::V1::AcceleratorTopologiesInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorTopologiesInfo)) — Output only. [Output Only] Slice info for the reservation subBlock. 



### #count
    
    
    def count() -> ::Integer

**Returns**

  * (::Integer) — Output only. [Output Only] The number of hosts that are allocated in this reservation subBlock. 



### #count=
    
    
    def count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. [Output Only] The number of hosts that are allocated in this reservation subBlock. 



**Returns**

  * (::Integer) — Output only. [Output Only] The number of hosts that are allocated in this reservation subBlock. 



### #creation_timestamp
    
    
    def creation_timestamp() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Creation timestamp inRFC3339 text format. 



### #creation_timestamp=
    
    
    def creation_timestamp=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Creation timestamp inRFC3339 text format. 



**Returns**

  * (::String) — Output only. [Output Only] Creation timestamp inRFC3339 text format. 



### #health_info
    
    
    def health_info() -> ::Google::Cloud::Compute::V1::ReservationSubBlockHealthInfo

**Returns**

  * ([::Google::Cloud::Compute::V1::ReservationSubBlockHealthInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlockHealthInfo)) — Output only. [Output Only] Health information for the reservation subBlock. 



### #health_info=
    
    
    def health_info=(value) -> ::Google::Cloud::Compute::V1::ReservationSubBlockHealthInfo

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::ReservationSubBlockHealthInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlockHealthInfo)) — Output only. [Output Only] Health information for the reservation subBlock. 



**Returns**

  * ([::Google::Cloud::Compute::V1::ReservationSubBlockHealthInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlockHealthInfo)) — Output only. [Output Only] Health information for the reservation subBlock. 



### #id
    
    
    def id() -> ::Integer

**Returns**

  * (::Integer) — Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server. 



### #id=
    
    
    def id=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server. 



**Returns**

  * (::Integer) — Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server. 



### #in_use_count
    
    
    def in_use_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. [Output Only] The number of instances that are currently in use on this reservation subBlock. 



### #in_use_count=
    
    
    def in_use_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. [Output Only] The number of instances that are currently in use on this reservation subBlock. 



**Returns**

  * (::Integer) — Output only. [Output Only] The number of instances that are currently in use on this reservation subBlock. 



### #in_use_host_count
    
    
    def in_use_host_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. Number of hosts currently in use. If there is one or more Instances running on the host, it is considered in use. 



### #in_use_host_count=
    
    
    def in_use_host_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. Number of hosts currently in use. If there is one or more Instances running on the host, it is considered in use. 



**Returns**

  * (::Integer) — Output only. Number of hosts currently in use. If there is one or more Instances running on the host, it is considered in use. 



### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Type of the resource. Alwayscompute#reservationSubBlock for reservation subBlocks. 



### #kind=
    
    
    def kind=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Type of the resource. Alwayscompute#reservationSubBlock for reservation subBlocks. 



**Returns**

  * (::String) — Output only. [Output Only] Type of the resource. Alwayscompute#reservationSubBlock for reservation subBlocks. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] The name of this reservation subBlock generated by Google Compute Engine. The name must be 1-63 characters long, and comply with RFC1035 `@pattern` [a-z](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlock?:%5B-a-z0-9%5D%5C%7B0,61%7D%5Ba-z0-9%5D)? 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] The name of this reservation subBlock generated by Google Compute Engine. The name must be 1-63 characters long, and comply with RFC1035 `@pattern` [a-z](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlock?:%5B-a-z0-9%5D%5C%7B0,61%7D%5Ba-z0-9%5D)? 



**Returns**

  * (::String) — Output only. [Output Only] The name of this reservation subBlock generated by Google Compute Engine. The name must be 1-63 characters long, and comply with RFC1035 `@pattern` [a-z](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlock?:%5B-a-z0-9%5D%5C%7B0,61%7D%5Ba-z0-9%5D)? 



### #physical_topology
    
    
    def physical_topology() -> ::Google::Cloud::Compute::V1::ReservationSubBlockPhysicalTopology

**Returns**

  * ([::Google::Cloud::Compute::V1::ReservationSubBlockPhysicalTopology](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlockPhysicalTopology)) — Output only. [Output Only] The physical topology of the reservation subBlock. 



### #physical_topology=
    
    
    def physical_topology=(value) -> ::Google::Cloud::Compute::V1::ReservationSubBlockPhysicalTopology

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::ReservationSubBlockPhysicalTopology](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlockPhysicalTopology)) — Output only. [Output Only] The physical topology of the reservation subBlock. 



**Returns**

  * ([::Google::Cloud::Compute::V1::ReservationSubBlockPhysicalTopology](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlockPhysicalTopology)) — Output only. [Output Only] The physical topology of the reservation subBlock. 



### #reservation_sub_block_maintenance
    
    
    def reservation_sub_block_maintenance() -> ::Google::Cloud::Compute::V1::GroupMaintenanceInfo

**Returns**

  * ([::Google::Cloud::Compute::V1::GroupMaintenanceInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GroupMaintenanceInfo)) — Output only. Maintenance information for this reservation subBlock. 



### #reservation_sub_block_maintenance=
    
    
    def reservation_sub_block_maintenance=(value) -> ::Google::Cloud::Compute::V1::GroupMaintenanceInfo

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::GroupMaintenanceInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GroupMaintenanceInfo)) — Output only. Maintenance information for this reservation subBlock. 



**Returns**

  * ([::Google::Cloud::Compute::V1::GroupMaintenanceInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GroupMaintenanceInfo)) — Output only. Maintenance information for this reservation subBlock. 



### #self_link
    
    
    def self_link() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Server-defined fully-qualified URL for this resource. 



### #self_link=
    
    
    def self_link=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Server-defined fully-qualified URL for this resource. 



**Returns**

  * (::String) — Output only. [Output Only] Server-defined fully-qualified URL for this resource. 



### #self_link_with_id
    
    
    def self_link_with_id() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Server-defined URL for this resource with the resource id. 



### #self_link_with_id=
    
    
    def self_link_with_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Server-defined URL for this resource with the resource id. 



**Returns**

  * (::String) — Output only. [Output Only] Server-defined URL for this resource with the resource id. 



### #status
    
    
    def status() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Status of the reservation subBlock. Check the Status enum for the list of possible values. 



### #status=
    
    
    def status=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Status of the reservation subBlock. Check the Status enum for the list of possible values. 



**Returns**

  * (::String) — Output only. [Output Only] Status of the reservation subBlock. Check the Status enum for the list of possible values. 



### #zone
    
    
    def zone() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Zone in which the reservation subBlock resides. 



### #zone=
    
    
    def zone=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Zone in which the reservation subBlock resides. 



**Returns**

  * (::String) — Output only. [Output Only] Zone in which the reservation subBlock resides. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
