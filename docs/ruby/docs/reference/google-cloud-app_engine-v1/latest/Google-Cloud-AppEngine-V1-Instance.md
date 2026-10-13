---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instance/
title: App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Instance (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:52.146104+00:00
---

# App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Instance (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Instance (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API class Google::Cloud::AppEngine::V1::Instance.

An Instance resource is the computing unit that App Engine uses to automatically scale an application.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #app_engine_release
    
    
    def app_engine_release() -> ::String

**Returns**

  * (::String) — Output only. App Engine release this instance is running on. 



### #availability
    
    
    def availability() -> ::Google::Cloud::AppEngine::V1::Instance::Availability

**Returns**

  * ([::Google::Cloud::AppEngine::V1::Instance::Availability](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instance-Availability)) — Output only. Availability of the instance. 



### #average_latency
    
    
    def average_latency() -> ::Integer

**Returns**

  * (::Integer) — Output only. Average latency (ms) over the last minute. 



### #errors
    
    
    def errors() -> ::Integer

**Returns**

  * (::Integer) — Output only. Number of errors since this instance was started. 



### #id
    
    
    def id() -> ::String

**Returns**

  * (::String) — Output only. Relative name of the instance within the version. Example: `instance-1`. 



### #memory_usage
    
    
    def memory_usage() -> ::Integer

**Returns**

  * (::Integer) — Output only. Total memory in use (bytes). 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Full path to the Instance resource in the API. Example: `apps/myapp/services/default/versions/v1/instances/instance-1`. 



### #qps
    
    
    def qps() -> ::Float

**Returns**

  * (::Float) — Output only. Average queries per second (QPS) over the last minute. 



### #requests
    
    
    def requests() -> ::Integer

**Returns**

  * (::Integer) — Output only. Number of requests since this instance was started. 



### #start_time
    
    
    def start_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time that this instance was started. 



### #vm_debug_enabled
    
    
    def vm_debug_enabled() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Whether this instance is in debug mode. Only applicable for instances in App Engine flexible environment. 



### #vm_id
    
    
    def vm_id() -> ::String

**Returns**

  * (::String) — Output only. Virtual machine ID of this instance. Only applicable for instances in App Engine flexible environment. 



### #vm_ip
    
    
    def vm_ip() -> ::String

**Returns**

  * (::String) — Output only. The IP address of this instance. Only applicable for instances in App Engine flexible environment. 



### #vm_liveness
    
    
    def vm_liveness() -> ::Google::Cloud::AppEngine::V1::Instance::Liveness::LivenessState

**Returns**

  * ([::Google::Cloud::AppEngine::V1::Instance::Liveness::LivenessState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instance-Liveness-LivenessState)) — Output only. The liveness health check of this instance. Only applicable for instances in App Engine flexible environment. 



### #vm_name
    
    
    def vm_name() -> ::String

**Returns**

  * (::String) — Output only. Name of the virtual machine where this instance lives. Only applicable for instances in App Engine flexible environment. 



### #vm_status
    
    
    def vm_status() -> ::String

**Returns**

  * (::String) — Output only. Status of the virtual machine where this instance lives. Only applicable for instances in App Engine flexible environment. 



### #vm_zone_name
    
    
    def vm_zone_name() -> ::String

**Returns**

  * (::String) — Output only. Zone where the virtual machine is located. Only applicable for instances in App Engine flexible environment. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
