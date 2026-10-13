---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-QueryForecastsRequest/
title: Capacity Planner V1BETA API - Class Google::Cloud::CapacityPlanner::V1beta::QueryForecastsRequest (v0.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:03.858472+00:00
---

# Capacity Planner V1BETA API - Class Google::Cloud::CapacityPlanner::V1beta::QueryForecastsRequest (v0.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-QueryForecastsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Capacity Planner V1BETA API - Class Google::Cloud::CapacityPlanner::V1beta::QueryForecastsRequest (v0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Capacity Planner V1BETA API class Google::Cloud::CapacityPlanner::V1beta::QueryForecastsRequest.

The `QueryForecasts` request. Next : 14

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

  * ([::Google::Cloud::CapacityPlanner::V1beta::UsageHistory::AggregationMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-UsageHistory-AggregationMethod)) — Aggregation Method of the historical usage for which the forecast is generated 



### #aggregation_method=
    
    
    def aggregation_method=(value) -> ::Google::Cloud::CapacityPlanner::V1beta::UsageHistory::AggregationMethod

**Parameter**

  * **value** ([::Google::Cloud::CapacityPlanner::V1beta::UsageHistory::AggregationMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-UsageHistory-AggregationMethod)) — Aggregation Method of the historical usage for which the forecast is generated 



**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::UsageHistory::AggregationMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-UsageHistory-AggregationMethod)) — Aggregation Method of the historical usage for which the forecast is generated 



### #cloud_resource_type
    
    
    def cloud_resource_type() -> ::String

**Returns**

  * (::String) — Required. The resource for the `Forecast` values to return. Possible values include "gce-vcpus", "gce-ram", "gce-local-ssd", "gce-persistent-disk", "gce-gpu" and "gce-tpu". Empty cloud_resource_type will return results matching all resources. 



### #cloud_resource_type=
    
    
    def cloud_resource_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource for the `Forecast` values to return. Possible values include "gce-vcpus", "gce-ram", "gce-local-ssd", "gce-persistent-disk", "gce-gpu" and "gce-tpu". Empty cloud_resource_type will return results matching all resources. 



**Returns**

  * (::String) — Required. The resource for the `Forecast` values to return. Possible values include "gce-vcpus", "gce-ram", "gce-local-ssd", "gce-persistent-disk", "gce-gpu" and "gce-tpu". Empty cloud_resource_type will return results matching all resources. 



### #confidential_mode
    
    
    def confidential_mode() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether the persistent disk is in confidential mode. 



### #confidential_mode=
    
    
    def confidential_mode=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether the persistent disk is in confidential mode. 



**Returns**

  * (::Boolean) — Optional. Whether the persistent disk is in confidential mode. 



### #disk_type
    
    
    def disk_type() -> ::String

**Returns**

  * (::String) — Optional. The disk_type for the `Forecast` values to return with request persistent-disk cloud_resource_type. Empty disk_type will return results matching all disk types. 



### #disk_type=
    
    
    def disk_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The disk_type for the `Forecast` values to return with request persistent-disk cloud_resource_type. Empty disk_type will return results matching all disk types. 



**Returns**

  * (::String) — Optional. The disk_type for the `Forecast` values to return with request persistent-disk cloud_resource_type. Empty disk_type will return results matching all disk types. 



### #forecast_type
    
    
    def forecast_type() -> ::Google::Cloud::CapacityPlanner::V1beta::Forecast::ForecastType

**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::Forecast::ForecastType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-Forecast-ForecastType)) — The type of forecast to use to select the `Forecast` values to return. FORECAST_TYPE_UNSPECIFIED will return results matching all the forecast types. 



### #forecast_type=
    
    
    def forecast_type=(value) -> ::Google::Cloud::CapacityPlanner::V1beta::Forecast::ForecastType

**Parameter**

  * **value** ([::Google::Cloud::CapacityPlanner::V1beta::Forecast::ForecastType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-Forecast-ForecastType)) — The type of forecast to use to select the `Forecast` values to return. FORECAST_TYPE_UNSPECIFIED will return results matching all the forecast types. 



**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::Forecast::ForecastType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-Forecast-ForecastType)) — The type of forecast to use to select the `Forecast` values to return. FORECAST_TYPE_UNSPECIFIED will return results matching all the forecast types. 



### #gpu_type
    
    
    def gpu_type() -> ::String

**Returns**

  * (::String) — Optional. The GPU type for the `Forecast` values to return. Sample values are "nvidia-tesla-t4", and "nvidia-tesla-a100". See https://cloud.google.com/compute/docs/gpus for a list. Empty gpu_type will return results matching all GPUs. 



### #gpu_type=
    
    
    def gpu_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The GPU type for the `Forecast` values to return. Sample values are "nvidia-tesla-t4", and "nvidia-tesla-a100". See https://cloud.google.com/compute/docs/gpus for a list. Empty gpu_type will return results matching all GPUs. 



**Returns**

  * (::String) — Optional. The GPU type for the `Forecast` values to return. Sample values are "nvidia-tesla-t4", and "nvidia-tesla-a100". See https://cloud.google.com/compute/docs/gpus for a list. Empty gpu_type will return results matching all GPUs. 



### #machine_family
    
    
    def machine_family() -> ::String

**Returns**

  * (::String) — The machine family to use to select the `Forecast` values to return. Possible values include "n1", and "n2d". Empty machine_family will return results matching all machine families. 



### #machine_family=
    
    
    def machine_family=(value) -> ::String

**Parameter**

  * **value** (::String) — The machine family to use to select the `Forecast` values to return. Possible values include "n1", and "n2d". Empty machine_family will return results matching all machine families. 



**Returns**

  * (::String) — The machine family to use to select the `Forecast` values to return. Possible values include "n1", and "n2d". Empty machine_family will return results matching all machine families. 



### #machine_shape
    
    
    def machine_shape() -> ::Google::Cloud::CapacityPlanner::V1beta::MachineShape

**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::MachineShape](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-MachineShape)) — Optional. The machine shape for the time series values to return. 



### #machine_shape=
    
    
    def machine_shape=(value) -> ::Google::Cloud::CapacityPlanner::V1beta::MachineShape

**Parameter**

  * **value** ([::Google::Cloud::CapacityPlanner::V1beta::MachineShape](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-MachineShape)) — Optional. The machine shape for the time series values to return. 



**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::MachineShape](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-MachineShape)) — Optional. The machine shape for the time series values to return. 



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




### #prediction_interval
    
    
    def prediction_interval() -> ::Google::Cloud::CapacityPlanner::V1beta::Forecast::PredictionInterval

**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::Forecast::PredictionInterval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-Forecast-PredictionInterval)) — The prediction interval to use to select the `Forecast` values to return. PREDICTION_INTERVAL_UNSPECIFIED will return results matching all prediction intervals. 



### #prediction_interval=
    
    
    def prediction_interval=(value) -> ::Google::Cloud::CapacityPlanner::V1beta::Forecast::PredictionInterval

**Parameter**

  * **value** ([::Google::Cloud::CapacityPlanner::V1beta::Forecast::PredictionInterval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-Forecast-PredictionInterval)) — The prediction interval to use to select the `Forecast` values to return. PREDICTION_INTERVAL_UNSPECIFIED will return results matching all prediction intervals. 



**Returns**

  * ([::Google::Cloud::CapacityPlanner::V1beta::Forecast::PredictionInterval](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-Forecast-PredictionInterval)) — The prediction interval to use to select the `Forecast` values to return. PREDICTION_INTERVAL_UNSPECIFIED will return results matching all prediction intervals. 



### #tpu_type
    
    
    def tpu_type() -> ::String

**Returns**

  * (::String) — Optional. The TPU type for the `Forecast` values to return. Empty tpu_type will return results matching all TPUs. 



### #tpu_type=
    
    
    def tpu_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The TPU type for the `Forecast` values to return. Empty tpu_type will return results matching all TPUs. 



**Returns**

  * (::String) — Optional. The TPU type for the `Forecast` values to return. Empty tpu_type will return results matching all TPUs. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
