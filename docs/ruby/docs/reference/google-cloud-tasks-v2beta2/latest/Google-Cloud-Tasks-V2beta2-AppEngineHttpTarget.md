---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AppEngineHttpTarget/
title: Cloud Tasks V2beta2 API - Class Google::Cloud::Tasks::V2beta2::AppEngineHttpTarget (v0.18.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:02.545055+00:00
---

# Cloud Tasks V2beta2 API - Class Google::Cloud::Tasks::V2beta2::AppEngineHttpTarget (v0.18.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AppEngineHttpTarget/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Tasks V2beta2 API - Class Google::Cloud::Tasks::V2beta2::AppEngineHttpTarget (v0.18.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.2 (latest)  0.18.1  0.17.0  0.16.1  0.15.0  0.14.1  0.13.0  0.12.1  0.11.3  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.5 

Reference documentation and code samples for the Cloud Tasks V2beta2 API class Google::Cloud::Tasks::V2beta2::AppEngineHttpTarget.

App Engine HTTP target.

The task will be delivered to the App Engine application hostname specified by its [AppEngineHttpTarget](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AppEngineHttpTarget "Google::Cloud::Tasks::V2beta2::AppEngineHttpTarget \(class\)") and [AppEngineHttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AppEngineHttpRequest "Google::Cloud::Tasks::V2beta2::AppEngineHttpRequest \(class\)"). The documentation for [AppEngineHttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AppEngineHttpRequest "Google::Cloud::Tasks::V2beta2::AppEngineHttpRequest \(class\)") explains how the task's host URL is constructed.

Using [AppEngineHttpTarget](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AppEngineHttpTarget "Google::Cloud::Tasks::V2beta2::AppEngineHttpTarget \(class\)") requires [`appengine.applications.get`](https://cloud.google.com/appengine/docs/admin-api/access-control) Google IAM permission for the project and the following scope:

`<https://www.googleapis.com/auth/cloud-platform>`

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #app_engine_routing_override
    
    
    def app_engine_routing_override() -> ::Google::Cloud::Tasks::V2beta2::AppEngineRouting

**Returns**

  * ([::Google::Cloud::Tasks::V2beta2::AppEngineRouting](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AppEngineRouting)) — Overrides for the [task-level app_engine_routing][google.cloud.tasks.v2beta2.AppEngineHttpRequest.app_engine_routing].

If set, `app_engine_routing_override` is used for all tasks in the queue, no matter what the setting is for the [task-level app_engine_routing][google.cloud.tasks.v2beta2.AppEngineHttpRequest.app_engine_routing]. 




### #app_engine_routing_override=
    
    
    def app_engine_routing_override=(value) -> ::Google::Cloud::Tasks::V2beta2::AppEngineRouting

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2beta2::AppEngineRouting](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AppEngineRouting)) — Overrides for the [task-level app_engine_routing][google.cloud.tasks.v2beta2.AppEngineHttpRequest.app_engine_routing].

If set, `app_engine_routing_override` is used for all tasks in the queue, no matter what the setting is for the [task-level app_engine_routing][google.cloud.tasks.v2beta2.AppEngineHttpRequest.app_engine_routing]. 




**Returns**

  * ([::Google::Cloud::Tasks::V2beta2::AppEngineRouting](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AppEngineRouting)) — Overrides for the [task-level app_engine_routing][google.cloud.tasks.v2beta2.AppEngineHttpRequest.app_engine_routing].

If set, `app_engine_routing_override` is used for all tasks in the queue, no matter what the setting is for the [task-level app_engine_routing][google.cloud.tasks.v2beta2.AppEngineHttpRequest.app_engine_routing]. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
