---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-ExportReservationsUsageRequest/
title: Capacity Planner V1BETA API - Class Google::Cloud::CapacityPlanner::V1beta::ExportReservationsUsageRequest (v0.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:09.447842+00:00
---

# Capacity Planner V1BETA API - Class Google::Cloud::CapacityPlanner::V1beta::ExportReservationsUsageRequest (v0.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-ExportReservationsUsageRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Capacity Planner V1BETA API - Class Google::Cloud::CapacityPlanner::V1beta::ExportReservationsUsageRequest (v0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Capacity Planner V1BETA API class Google::Cloud::CapacityPlanner::V1beta::ExportReservationsUsageRequest.

The `ExportReservationsUsage` request

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #cloud_resource_type
    
    
    def cloud_resource_type() -> ::String

**Returns**

  * (::String) — Required. The resource for the `ReservationsUsage` values to return. Possible values include "gce-vcpus", "gce-ram", "gce-local-ssd", and "gce-gpu". 



### #cloud_resource_type=
    
    
    def cloud_resource_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource for the `ReservationsUsage` values to return. Possible values include "gce-vcpus", "gce-ram", "gce-local-ssd", and "gce-gpu". 



**Returns**

  * (::String) — Required. The resource for the `ReservationsUsage` values to return. Possible values include "gce-vcpus", "gce-ram", "gce-local-ssd", and "gce-gpu". 



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

  * (::String) — Optional. The GPU type to query reservations and usage by. For example: NVIDIA T4.

Note: The following fields are mutually exclusive: `gpu_type`, `machine_family`, `machine_shape`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gpu_type=
    
    
    def gpu_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The GPU type to query reservations and usage by. For example: NVIDIA T4.

Note: The following fields are mutually exclusive: `gpu_type`, `machine_family`, `machine_shape`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Optional. The GPU type to query reservations and usage by. For example: NVIDIA T4.

Note: The following fields are mutually exclusive: `gpu_type`, `machine_family`, `machine_shape`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




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

  * (::String) — Optional. The machine family to query reservations and usage by. For example: n1, n2d.

Note: The following fields are mutually exclusive: `machine_family`, `machine_shape`, `gpu_type`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #machine_family=
    
    
    def machine_family=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The machine family to query reservations and usage by. For example: n1, n2d.

Note: The following fields are mutually exclusive: `machine_family`, `machine_shape`, `gpu_type`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Optional. The machine family to query reservations and usage by. For example: n1, n2d.

Note: The following fields are mutually exclusive: `machine_family`, `machine_shape`, `gpu_type`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #machine_shape
    
    
    def machine_shape() -> ::Google::Cloud::CapacityPlanner::V1beta::MachineShape

**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::MachineShape](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-MachineShape)) — Optional. The machine_shape as a filter to select matching reservations and its usage.

Note: The following fields are mutually exclusive: `machine_shape`, `machine_family`, `gpu_type`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #machine_shape=
    
    
    def machine_shape=(value) -> ::Google::Cloud::CapacityPlanner::V1beta::MachineShape

**Parameter**

  * **value** ([::Google::Cloud::CapacityPlanner::V1beta::MachineShape](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-MachineShape)) — Optional. The machine_shape as a filter to select matching reservations and its usage.

Note: The following fields are mutually exclusive: `machine_shape`, `machine_family`, `gpu_type`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::MachineShape](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-MachineShape)) — Optional. The machine_shape as a filter to select matching reservations and its usage.

Note: The following fields are mutually exclusive: `machine_shape`, `machine_family`, `gpu_type`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #output_config
    
    
    def output_config() -> ::Google::Cloud::CapacityPlanner::V1beta::OutputConfig

**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::OutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-OutputConfig)) — Required. Output configuration indicating where the results will be output to. 



### #output_config=
    
    
    def output_config=(value) -> ::Google::Cloud::CapacityPlanner::V1beta::OutputConfig

**Parameter**

  * **value** ([::Google::Cloud::CapacityPlanner::V1beta::OutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-OutputConfig)) — Required. Output configuration indicating where the results will be output to. 



**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::OutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-OutputConfig)) — Required. Output configuration indicating where the results will be output to. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The compute engine resource and location of the reservationsusage. The format is: projects/{project}/locations/{location} or organizations/{organization}/locations/{location} or folders/{folder}/locations/{location} 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The compute engine resource and location of the reservationsusage. The format is: projects/{project}/locations/{location} or organizations/{organization}/locations/{location} or folders/{folder}/locations/{location} 



**Returns**

  * (::String) — Required. The compute engine resource and location of the reservationsusage. The format is: projects/{project}/locations/{location} or organizations/{organization}/locations/{location} or folders/{folder}/locations/{location} 



### #share_type
    
    
    def share_type() -> ::Google::Cloud::CapacityPlanner::V1beta::ExportReservationsUsageRequest::ShareType

**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::ExportReservationsUsageRequest::ShareType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-ExportReservationsUsageRequest-ShareType)) — Optional. Type of share settings to filter reservations in response. If unspecified, all types are included. 



### #share_type=
    
    
    def share_type=(value) -> ::Google::Cloud::CapacityPlanner::V1beta::ExportReservationsUsageRequest::ShareType

**Parameter**

  * **value** ([::Google::Cloud::CapacityPlanner::V1beta::ExportReservationsUsageRequest::ShareType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-ExportReservationsUsageRequest-ShareType)) — Optional. Type of share settings to filter reservations in response. If unspecified, all types are included. 



**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::ExportReservationsUsageRequest::ShareType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-ExportReservationsUsageRequest-ShareType)) — Optional. Type of share settings to filter reservations in response. If unspecified, all types are included. 



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



### #usage_aggregation_method
    
    
    def usage_aggregation_method() -> ::Google::Cloud::CapacityPlanner::V1beta::UsageHistory::AggregationMethod

**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::UsageHistory::AggregationMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-UsageHistory-AggregationMethod)) — Required. The method that should be used to convert sampled reservations data to daily usage values. 



### #usage_aggregation_method=
    
    
    def usage_aggregation_method=(value) -> ::Google::Cloud::CapacityPlanner::V1beta::UsageHistory::AggregationMethod

**Parameter**

  * **value** ([::Google::Cloud::CapacityPlanner::V1beta::UsageHistory::AggregationMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-UsageHistory-AggregationMethod)) — Required. The method that should be used to convert sampled reservations data to daily usage values. 



**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::UsageHistory::AggregationMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-UsageHistory-AggregationMethod)) — Required. The method that should be used to convert sampled reservations data to daily usage values. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
