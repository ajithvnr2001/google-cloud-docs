---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-AutomaticScaling/
title: App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::AutomaticScaling (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:16.236873+00:00
---

# App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::AutomaticScaling (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-AutomaticScaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::AutomaticScaling (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API class Google::Cloud::AppEngine::V1::AutomaticScaling.

Automatic scaling is based on request rate, response latencies, and other application metrics.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #cool_down_period
    
    
    def cool_down_period() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — The time period that the [Autoscaler](https://cloud.google.com/compute/docs/autoscaler/) should wait before it starts collecting information from a new instance. This prevents the autoscaler from collecting information when the instance is initializing, during which the collected usage would not be reliable. Only applicable in the App Engine flexible environment. 



### #cool_down_period=
    
    
    def cool_down_period=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — The time period that the [Autoscaler](https://cloud.google.com/compute/docs/autoscaler/) should wait before it starts collecting information from a new instance. This prevents the autoscaler from collecting information when the instance is initializing, during which the collected usage would not be reliable. Only applicable in the App Engine flexible environment. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — The time period that the [Autoscaler](https://cloud.google.com/compute/docs/autoscaler/) should wait before it starts collecting information from a new instance. This prevents the autoscaler from collecting information when the instance is initializing, during which the collected usage would not be reliable. Only applicable in the App Engine flexible environment. 



### #cpu_utilization
    
    
    def cpu_utilization() -> ::Google::Cloud::AppEngine::V1::CpuUtilization

**Returns**

  * ([::Google::Cloud::AppEngine::V1::CpuUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-CpuUtilization)) — Target scaling by CPU usage. 



### #cpu_utilization=
    
    
    def cpu_utilization=(value) -> ::Google::Cloud::AppEngine::V1::CpuUtilization

**Parameter**

  * **value** ([::Google::Cloud::AppEngine::V1::CpuUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-CpuUtilization)) — Target scaling by CPU usage. 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::CpuUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-CpuUtilization)) — Target scaling by CPU usage. 



### #disk_utilization
    
    
    def disk_utilization() -> ::Google::Cloud::AppEngine::V1::DiskUtilization

**Returns**

  * ([::Google::Cloud::AppEngine::V1::DiskUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DiskUtilization)) — Target scaling by disk usage. 



### #disk_utilization=
    
    
    def disk_utilization=(value) -> ::Google::Cloud::AppEngine::V1::DiskUtilization

**Parameter**

  * **value** ([::Google::Cloud::AppEngine::V1::DiskUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DiskUtilization)) — Target scaling by disk usage. 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::DiskUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DiskUtilization)) — Target scaling by disk usage. 



### #max_concurrent_requests
    
    
    def max_concurrent_requests() -> ::Integer

**Returns**

  * (::Integer) — Number of concurrent requests an automatic scaling instance can accept before the scheduler spawns a new instance.

Defaults to a runtime-specific value. 




### #max_concurrent_requests=
    
    
    def max_concurrent_requests=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Number of concurrent requests an automatic scaling instance can accept before the scheduler spawns a new instance.

Defaults to a runtime-specific value. 




**Returns**

  * (::Integer) — Number of concurrent requests an automatic scaling instance can accept before the scheduler spawns a new instance.

Defaults to a runtime-specific value. 




### #max_idle_instances
    
    
    def max_idle_instances() -> ::Integer

**Returns**

  * (::Integer) — Maximum number of idle instances that should be maintained for this version. 



### #max_idle_instances=
    
    
    def max_idle_instances=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Maximum number of idle instances that should be maintained for this version. 



**Returns**

  * (::Integer) — Maximum number of idle instances that should be maintained for this version. 



### #max_pending_latency
    
    
    def max_pending_latency() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Maximum amount of time that a request should wait in the pending queue before starting a new instance to handle it. 



### #max_pending_latency=
    
    
    def max_pending_latency=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Maximum amount of time that a request should wait in the pending queue before starting a new instance to handle it. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Maximum amount of time that a request should wait in the pending queue before starting a new instance to handle it. 



### #max_total_instances
    
    
    def max_total_instances() -> ::Integer

**Returns**

  * (::Integer) — Maximum number of instances that should be started to handle requests for this version. 



### #max_total_instances=
    
    
    def max_total_instances=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Maximum number of instances that should be started to handle requests for this version. 



**Returns**

  * (::Integer) — Maximum number of instances that should be started to handle requests for this version. 



### #min_idle_instances
    
    
    def min_idle_instances() -> ::Integer

**Returns**

  * (::Integer) — Minimum number of idle instances that should be maintained for this version. Only applicable for the default version of a service. 



### #min_idle_instances=
    
    
    def min_idle_instances=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Minimum number of idle instances that should be maintained for this version. Only applicable for the default version of a service. 



**Returns**

  * (::Integer) — Minimum number of idle instances that should be maintained for this version. Only applicable for the default version of a service. 



### #min_pending_latency
    
    
    def min_pending_latency() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Minimum amount of time a request should wait in the pending queue before starting a new instance to handle it. 



### #min_pending_latency=
    
    
    def min_pending_latency=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Minimum amount of time a request should wait in the pending queue before starting a new instance to handle it. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Minimum amount of time a request should wait in the pending queue before starting a new instance to handle it. 



### #min_total_instances
    
    
    def min_total_instances() -> ::Integer

**Returns**

  * (::Integer) — Minimum number of running instances that should be maintained for this version. 



### #min_total_instances=
    
    
    def min_total_instances=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Minimum number of running instances that should be maintained for this version. 



**Returns**

  * (::Integer) — Minimum number of running instances that should be maintained for this version. 



### #network_utilization
    
    
    def network_utilization() -> ::Google::Cloud::AppEngine::V1::NetworkUtilization

**Returns**

  * ([::Google::Cloud::AppEngine::V1::NetworkUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-NetworkUtilization)) — Target scaling by network usage. 



### #network_utilization=
    
    
    def network_utilization=(value) -> ::Google::Cloud::AppEngine::V1::NetworkUtilization

**Parameter**

  * **value** ([::Google::Cloud::AppEngine::V1::NetworkUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-NetworkUtilization)) — Target scaling by network usage. 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::NetworkUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-NetworkUtilization)) — Target scaling by network usage. 



### #request_utilization
    
    
    def request_utilization() -> ::Google::Cloud::AppEngine::V1::RequestUtilization

**Returns**

  * ([::Google::Cloud::AppEngine::V1::RequestUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-RequestUtilization)) — Target scaling by request utilization. 



### #request_utilization=
    
    
    def request_utilization=(value) -> ::Google::Cloud::AppEngine::V1::RequestUtilization

**Parameter**

  * **value** ([::Google::Cloud::AppEngine::V1::RequestUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-RequestUtilization)) — Target scaling by request utilization. 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::RequestUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-RequestUtilization)) — Target scaling by request utilization. 



### #standard_scheduler_settings
    
    
    def standard_scheduler_settings() -> ::Google::Cloud::AppEngine::V1::StandardSchedulerSettings

**Returns**

  * ([::Google::Cloud::AppEngine::V1::StandardSchedulerSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-StandardSchedulerSettings)) — Scheduler settings for standard environment. 



### #standard_scheduler_settings=
    
    
    def standard_scheduler_settings=(value) -> ::Google::Cloud::AppEngine::V1::StandardSchedulerSettings

**Parameter**

  * **value** ([::Google::Cloud::AppEngine::V1::StandardSchedulerSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-StandardSchedulerSettings)) — Scheduler settings for standard environment. 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::StandardSchedulerSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-StandardSchedulerSettings)) — Scheduler settings for standard environment. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
