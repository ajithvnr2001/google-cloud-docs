---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-LivenessCheck/
title: App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::LivenessCheck (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:32.148165+00:00
---

# App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::LivenessCheck (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-LivenessCheck/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::LivenessCheck (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API class Google::Cloud::AppEngine::V1::LivenessCheck.

Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #check_interval
    
    
    def check_interval() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Interval between health checks. 



### #check_interval=
    
    
    def check_interval=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Interval between health checks. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Interval between health checks. 



### #failure_threshold
    
    
    def failure_threshold() -> ::Integer

**Returns**

  * (::Integer) — Number of consecutive failed checks required before considering the VM unhealthy. 



### #failure_threshold=
    
    
    def failure_threshold=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Number of consecutive failed checks required before considering the VM unhealthy. 



**Returns**

  * (::Integer) — Number of consecutive failed checks required before considering the VM unhealthy. 



### #host
    
    
    def host() -> ::String

**Returns**

  * (::String) — Host header to send when performing a HTTP Liveness check. Example: "myapp.appspot.com" 



### #host=
    
    
    def host=(value) -> ::String

**Parameter**

  * **value** (::String) — Host header to send when performing a HTTP Liveness check. Example: "myapp.appspot.com" 



**Returns**

  * (::String) — Host header to send when performing a HTTP Liveness check. Example: "myapp.appspot.com" 



### #initial_delay
    
    
    def initial_delay() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — The initial delay before starting to execute the checks. 



### #initial_delay=
    
    
    def initial_delay=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — The initial delay before starting to execute the checks. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — The initial delay before starting to execute the checks. 



### #path
    
    
    def path() -> ::String

**Returns**

  * (::String) — The request path. 



### #path=
    
    
    def path=(value) -> ::String

**Parameter**

  * **value** (::String) — The request path. 



**Returns**

  * (::String) — The request path. 



### #success_threshold
    
    
    def success_threshold() -> ::Integer

**Returns**

  * (::Integer) — Number of consecutive successful checks required before considering the VM healthy. 



### #success_threshold=
    
    
    def success_threshold=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Number of consecutive successful checks required before considering the VM healthy. 



**Returns**

  * (::Integer) — Number of consecutive successful checks required before considering the VM healthy. 



### #timeout
    
    
    def timeout() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Time before the check is considered failed. 



### #timeout=
    
    
    def timeout=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Time before the check is considered failed. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Time before the check is considered failed. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
