---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-BasicScaling/
title: App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::BasicScaling (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:16.638428+00:00
---

# App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::BasicScaling (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-BasicScaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::BasicScaling (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API class Google::Cloud::AppEngine::V1::BasicScaling.

A service with basic scaling will create an instance when the application receives a request. The instance will be turned down when the app becomes idle. Basic scaling is ideal for work that is intermittent or driven by user activity.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #idle_timeout
    
    
    def idle_timeout() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Duration of time after the last request that an instance must wait before the instance is shut down. 



### #idle_timeout=
    
    
    def idle_timeout=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Duration of time after the last request that an instance must wait before the instance is shut down. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Duration of time after the last request that an instance must wait before the instance is shut down. 



### #max_instances
    
    
    def max_instances() -> ::Integer

**Returns**

  * (::Integer) — Maximum number of instances to create for this version. 



### #max_instances=
    
    
    def max_instances=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Maximum number of instances to create for this version. 



**Returns**

  * (::Integer) — Maximum number of instances to create for this version. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
