---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-HealthCheck/
title: App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::HealthCheck (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:51.645054+00:00
---

# App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::HealthCheck (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-HealthCheck/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::HealthCheck (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API class Google::Cloud::AppEngine::V1::HealthCheck.

Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances. Only applicable for instances in App Engine flexible environment.

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



### #disable_health_check
    
    
    def disable_health_check() -> ::Boolean

**Returns**

  * (::Boolean) — Whether to explicitly disable health checks for this instance. 



### #disable_health_check=
    
    
    def disable_health_check=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether to explicitly disable health checks for this instance. 



**Returns**

  * (::Boolean) — Whether to explicitly disable health checks for this instance. 



### #healthy_threshold
    
    
    def healthy_threshold() -> ::Integer

**Returns**

  * (::Integer) — Number of consecutive successful health checks required before receiving traffic. 



### #healthy_threshold=
    
    
    def healthy_threshold=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Number of consecutive successful health checks required before receiving traffic. 



**Returns**

  * (::Integer) — Number of consecutive successful health checks required before receiving traffic. 



### #host
    
    
    def host() -> ::String

**Returns**

  * (::String) — Host header to send when performing an HTTP health check. Example: "myapp.appspot.com" 



### #host=
    
    
    def host=(value) -> ::String

**Parameter**

  * **value** (::String) — Host header to send when performing an HTTP health check. Example: "myapp.appspot.com" 



**Returns**

  * (::String) — Host header to send when performing an HTTP health check. Example: "myapp.appspot.com" 



### #restart_threshold
    
    
    def restart_threshold() -> ::Integer

**Returns**

  * (::Integer) — Number of consecutive failed health checks required before an instance is restarted. 



### #restart_threshold=
    
    
    def restart_threshold=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Number of consecutive failed health checks required before an instance is restarted. 



**Returns**

  * (::Integer) — Number of consecutive failed health checks required before an instance is restarted. 



### #timeout
    
    
    def timeout() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Time before the health check is considered failed. 



### #timeout=
    
    
    def timeout=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Time before the health check is considered failed. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Time before the health check is considered failed. 



### #unhealthy_threshold
    
    
    def unhealthy_threshold() -> ::Integer

**Returns**

  * (::Integer) — Number of consecutive failed health checks required before removing traffic. 



### #unhealthy_threshold=
    
    
    def unhealthy_threshold=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Number of consecutive failed health checks required before removing traffic. 



**Returns**

  * (::Integer) — Number of consecutive failed health checks required before removing traffic. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
