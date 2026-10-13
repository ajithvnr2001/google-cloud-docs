---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-QueryReservationsRequest/
title: Capacity Planner V1BETA API - Class Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest (v0.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:36.195158+00:00
---

# Capacity Planner V1BETA API - Class Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest (v0.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-QueryReservationsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Capacity Planner V1BETA API - Class Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest (v0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Capacity Planner V1BETA API class Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest.

The `QueryReservations` request.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #aggregation_method
    
    
    def aggregation_method() -> ::Google::Cloud::CapacityPlanner::V1beta::UsageHistory::AggregationMethod

**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::UsageHistory::AggregationMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-UsageHistory-AggregationMethod)) — Optional. Aggregation Method of the historical reservation usage 



### #aggregation_method=
    
    
    def aggregation_method=(value) -> ::Google::Cloud::CapacityPlanner::V1beta::UsageHistory::AggregationMethod

**Parameter**

  * **value** ([::Google::Cloud::CapacityPlanner::V1beta::UsageHistory::AggregationMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-UsageHistory-AggregationMethod)) — Optional. Aggregation Method of the historical reservation usage 



**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::UsageHistory::AggregationMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-UsageHistory-AggregationMethod)) — Optional. Aggregation Method of the historical reservation usage 



### #cloud_resource_type
    
    
    def cloud_resource_type() -> ::String

**Returns**

  * (::String) — Required. The resource for the reserved values to return. Possible values include "gce-vcpus", "gce-ram", "gce-local-ssd", "gce-gpu" and "gce-vm". 



### #cloud_resource_type=
    
    
    def cloud_resource_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource for the reserved values to return. Possible values include "gce-vcpus", "gce-ram", "gce-local-ssd", "gce-gpu" and "gce-vm". 



**Returns**

  * (::String) — Required. The resource for the reserved values to return. Possible values include "gce-vcpus", "gce-ram", "gce-local-ssd", "gce-gpu" and "gce-vm". 



### #end_date
    
    
    def end_date() -> ::Google::Type::Date

**Returns**

  * ([::Google::Type::Date](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Type-Date)) — Optional. The end date of reservations usage. 



### #end_date=
    
    
    def end_date=(value) -> ::Google::Type::Date

**Parameter**

  * **value** ([::Google::Type::Date](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Type-Date)) — Optional. The end date of reservations usage. 



**Returns**

  * ([::Google::Type::Date](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Type-Date)) — Optional. The end date of reservations usage. 



### #gpu_type
    
    
    def gpu_type() -> ::String

**Returns**

  * (::String) — Optional. The GPU type for the reserved values to return. Sample values are "nvidia-tesla-t4", and "nvidia-tesla-a100". See https://cloud.google.com/compute/docs/gpus for a list. Empty gpu_type will return results matching all GPUs. 



### #gpu_type=
    
    
    def gpu_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The GPU type for the reserved values to return. Sample values are "nvidia-tesla-t4", and "nvidia-tesla-a100". See https://cloud.google.com/compute/docs/gpus for a list. Empty gpu_type will return results matching all GPUs. 



**Returns**

  * (::String) — Optional. The GPU type for the reserved values to return. Sample values are "nvidia-tesla-t4", and "nvidia-tesla-a100". See https://cloud.google.com/compute/docs/gpus for a list. Empty gpu_type will return results matching all GPUs. 



### #include_unapproved_reservations
    
    
    def include_unapproved_reservations() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether to include pending for approval reservations in the response. This field is only applicable for future reservations. 



### #include_unapproved_reservations=
    
    
    def include_unapproved_reservations=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether to include pending for approval reservations in the response. This field is only applicable for future reservations. 



**Returns**

  * (::Boolean) — Optional. Whether to include pending for approval reservations in the response. This field is only applicable for future reservations. 



### #location_level
    
    
    def location_level() -> ::Google::Cloud::CapacityPlanner::V1beta::TimeSeries::LocationType

**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::TimeSeries::LocationType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-TimeSeries-LocationType)) — Optional. The location level of the reservations usage timeseries. 



### #location_level=
    
    
    def location_level=(value) -> ::Google::Cloud::CapacityPlanner::V1beta::TimeSeries::LocationType

**Parameter**

  * **value** ([::Google::Cloud::CapacityPlanner::V1beta::TimeSeries::LocationType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-TimeSeries-LocationType)) — Optional. The location level of the reservations usage timeseries. 



**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::TimeSeries::LocationType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-TimeSeries-LocationType)) — Optional. The location level of the reservations usage timeseries. 



### #machine_family
    
    
    def machine_family() -> ::String

**Returns**

  * (::String) — Optional. The machine family to use to select the aggregate reserved values to return. Possible values include "n1", and "n2d" etc. Empty machine_family will return results matching all machine families. 



### #machine_family=
    
    
    def machine_family=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The machine family to use to select the aggregate reserved values to return. Possible values include "n1", and "n2d" etc. Empty machine_family will return results matching all machine families. 



**Returns**

  * (::String) — Optional. The machine family to use to select the aggregate reserved values to return. Possible values include "n1", and "n2d" etc. Empty machine_family will return results matching all machine families. 



### #machine_shape
    
    
    def machine_shape() -> ::Google::Cloud::CapacityPlanner::V1beta::MachineShape

**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::MachineShape](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-MachineShape)) — Optional. The machine_shape as a filter to select matching reservations. 



### #machine_shape=
    
    
    def machine_shape=(value) -> ::Google::Cloud::CapacityPlanner::V1beta::MachineShape

**Parameter**

  * **value** ([::Google::Cloud::CapacityPlanner::V1beta::MachineShape](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-MachineShape)) — Optional. The machine_shape as a filter to select matching reservations. 



**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::MachineShape](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-MachineShape)) — Optional. The machine_shape as a filter to select matching reservations. 



### #ownership_type
    
    
    def ownership_type() -> ::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::OwnershipType

**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::OwnershipType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-QueryReservationsRequest-OwnershipType)) — Optional. Types of ownerships to filter reservations based on. In case of OWNED, it filters reservations which are owned by selected parent project/folder/organization. If unspecified, all types are included. 



### #ownership_type=
    
    
    def ownership_type=(value) -> ::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::OwnershipType

**Parameter**

  * **value** ([::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::OwnershipType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-QueryReservationsRequest-OwnershipType)) — Optional. Types of ownerships to filter reservations based on. In case of OWNED, it filters reservations which are owned by selected parent project/folder/organization. If unspecified, all types are included. 



**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::OwnershipType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-QueryReservationsRequest-OwnershipType)) — Optional. Types of ownerships to filter reservations based on. In case of OWNED, it filters reservations which are owned by selected parent project/folder/organization. If unspecified, all types are included. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The compute engine resource and location for the time series values to return. The format is:

projects/{project}/locations/{location} or organizations/{organization}/locations/{location} or folders/{folder}/locations/{location} 




### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The compute engine resource and location for the time series values to return. The format is:

projects/{project}/locations/{location} or organizations/{organization}/locations/{location} or folders/{folder}/locations/{location} 




**Returns**

  * (::String) — Required. The compute engine resource and location for the time series values to return. The format is:

projects/{project}/locations/{location} or organizations/{organization}/locations/{location} or folders/{folder}/locations/{location} 




### #reservation_data_level
    
    
    def reservation_data_level() -> ::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::ReservationDataLevel

**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::ReservationDataLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-QueryReservationsRequest-ReservationDataLevel)) — Required. Reservations output data format. 



### #reservation_data_level=
    
    
    def reservation_data_level=(value) -> ::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::ReservationDataLevel

**Parameter**

  * **value** ([::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::ReservationDataLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-QueryReservationsRequest-ReservationDataLevel)) — Required. Reservations output data format. 



**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::ReservationDataLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-QueryReservationsRequest-ReservationDataLevel)) — Required. Reservations output data format. 



### #reservation_type
    
    
    def reservation_type() -> ::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::ReservationType

**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::ReservationType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-QueryReservationsRequest-ReservationType)) — Required. The Reservation type for example, future reservation request and allocation. If unspecified, all types are included. 



### #reservation_type=
    
    
    def reservation_type=(value) -> ::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::ReservationType

**Parameter**

  * **value** ([::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::ReservationType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-QueryReservationsRequest-ReservationType)) — Required. The Reservation type for example, future reservation request and allocation. If unspecified, all types are included. 



**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::ReservationType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-QueryReservationsRequest-ReservationType)) — Required. The Reservation type for example, future reservation request and allocation. If unspecified, all types are included. 



### #share_type
    
    
    def share_type() -> ::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::ShareType

**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::ShareType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-QueryReservationsRequest-ShareType)) — Optional. Types of share settings to filter reservations in response. If unspecified, all types are included. 



### #share_type=
    
    
    def share_type=(value) -> ::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::ShareType

**Parameter**

  * **value** ([::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::ShareType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-QueryReservationsRequest-ShareType)) — Optional. Types of share settings to filter reservations in response. If unspecified, all types are included. 



**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::QueryReservationsRequest::ShareType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-QueryReservationsRequest-ShareType)) — Optional. Types of share settings to filter reservations in response. If unspecified, all types are included. 



### #start_date
    
    
    def start_date() -> ::Google::Type::Date

**Returns**

  * ([::Google::Type::Date](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Type-Date)) — Optional. The start date of reservations usage. 



### #start_date=
    
    
    def start_date=(value) -> ::Google::Type::Date

**Parameter**

  * **value** ([::Google::Type::Date](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Type-Date)) — Optional. The start date of reservations usage. 



**Returns**

  * ([::Google::Type::Date](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Type-Date)) — Optional. The start date of reservations usage. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
