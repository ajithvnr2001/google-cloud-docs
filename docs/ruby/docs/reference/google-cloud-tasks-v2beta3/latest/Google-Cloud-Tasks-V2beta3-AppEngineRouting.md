---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting/
title: Cloud Tasks V2beta3 API - Class Google::Cloud::Tasks::V2beta3::AppEngineRouting (v0.20.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:15:03.512302+00:00
---

# Cloud Tasks V2beta3 API - Class Google::Cloud::Tasks::V2beta3::AppEngineRouting (v0.20.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Tasks V2beta3 API - Class Google::Cloud::Tasks::V2beta3::AppEngineRouting (v0.20.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.2 (latest)  0.20.1  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.0  0.13.1  0.12.3  0.11.0  0.10.2  0.9.0  0.8.0  0.7.0  0.6.6 

Reference documentation and code samples for the Cloud Tasks V2beta3 API class Google::Cloud::Tasks::V2beta3::AppEngineRouting.

App Engine Routing.

Defines routing characteristics specific to App Engine - service, version, and instance.

For more information about services, versions, and instances see [An Overview of App Engine](https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine), [Microservices Architecture on Google App Engine](https://cloud.google.com/appengine/docs/python/microservices-on-app-engine), [App Engine Standard request routing](https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed), and [App Engine Flex request routing](https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed).

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #host
    
    
    def host() -> ::String

**Returns**

  * (::String) — Output only. The host that the task is sent to.

The host is constructed from the domain name of the app associated with the queue's project ID (for example 

For more information, see [How Requests are Routed](https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed). 




### #host=
    
    
    def host=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. The host that the task is sent to.

The host is constructed from the domain name of the app associated with the queue's project ID (for example 

For more information, see [How Requests are Routed](https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed). 




**Returns**

  * (::String) — Output only. The host that the task is sent to.

The host is constructed from the domain name of the app associated with the queue's project ID (for example 

For more information, see [How Requests are Routed](https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed). 




### #instance
    
    
    def instance() -> ::String

**Returns**

  * (::String) — App instance.

By default, the task is sent to an instance which is available when the task is attempted.

Requests can only be sent to a specific instance if [manual scaling is used in App Engine Standard](https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine?hl=en_US#scaling_types_and_instance_classes). App Engine Flex does not support instances. For more information, see [App Engine Standard request routing](https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed) and [App Engine Flex request routing](https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed). 




### #instance=
    
    
    def instance=(value) -> ::String

**Parameter**

  * **value** (::String) — App instance.

By default, the task is sent to an instance which is available when the task is attempted.

Requests can only be sent to a specific instance if [manual scaling is used in App Engine Standard](https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine?hl=en_US#scaling_types_and_instance_classes). App Engine Flex does not support instances. For more information, see [App Engine Standard request routing](https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed) and [App Engine Flex request routing](https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed). 




**Returns**

  * (::String) — App instance.

By default, the task is sent to an instance which is available when the task is attempted.

Requests can only be sent to a specific instance if [manual scaling is used in App Engine Standard](https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine?hl=en_US#scaling_types_and_instance_classes). App Engine Flex does not support instances. For more information, see [App Engine Standard request routing](https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed) and [App Engine Flex request routing](https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed). 




### #service
    
    
    def service() -> ::String

**Returns**

  * (::String) — App service.

By default, the task is sent to the service which is the default service when the task is attempted.

For some queues or tasks which were created using the App Engine Task Queue API, [host](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_host_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#host \(method\)") is not parsable into [service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_service_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#service \(method\)"), [version](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_version_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#version \(method\)"), and [instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_instance_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#instance \(method\)"). For example, some tasks which were created using the App Engine SDK use a custom domain name; custom domains are not parsed by Cloud Tasks. If [host](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_host_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#host \(method\)") is not parsable, then [service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_service_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#service \(method\)"), [version](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_version_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#version \(method\)"), and [instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_instance_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#instance \(method\)") are the empty string. 




### #service=
    
    
    def service=(value) -> ::String

**Parameter**

  * **value** (::String) — App service.

By default, the task is sent to the service which is the default service when the task is attempted.

For some queues or tasks which were created using the App Engine Task Queue API, [host](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_host_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#host \(method\)") is not parsable into [service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_service_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#service \(method\)"), [version](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_version_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#version \(method\)"), and [instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_instance_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#instance \(method\)"). For example, some tasks which were created using the App Engine SDK use a custom domain name; custom domains are not parsed by Cloud Tasks. If [host](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_host_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#host \(method\)") is not parsable, then [service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_service_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#service \(method\)"), [version](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_version_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#version \(method\)"), and [instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_instance_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#instance \(method\)") are the empty string. 




**Returns**

  * (::String) — App service.

By default, the task is sent to the service which is the default service when the task is attempted.

For some queues or tasks which were created using the App Engine Task Queue API, [host](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_host_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#host \(method\)") is not parsable into [service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_service_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#service \(method\)"), [version](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_version_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#version \(method\)"), and [instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_instance_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#instance \(method\)"). For example, some tasks which were created using the App Engine SDK use a custom domain name; custom domains are not parsed by Cloud Tasks. If [host](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_host_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#host \(method\)") is not parsable, then [service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_service_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#service \(method\)"), [version](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_version_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#version \(method\)"), and [instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_instance_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#instance \(method\)") are the empty string. 




### #version
    
    
    def version() -> ::String

**Returns**

  * (::String) — App version.

By default, the task is sent to the version which is the default version when the task is attempted.

For some queues or tasks which were created using the App Engine Task Queue API, [host](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_host_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#host \(method\)") is not parsable into [service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_service_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#service \(method\)"), [version](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_version_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#version \(method\)"), and [instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_instance_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#instance \(method\)"). For example, some tasks which were created using the App Engine SDK use a custom domain name; custom domains are not parsed by Cloud Tasks. If [host](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_host_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#host \(method\)") is not parsable, then [service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_service_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#service \(method\)"), [version](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_version_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#version \(method\)"), and [instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_instance_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#instance \(method\)") are the empty string. 




### #version=
    
    
    def version=(value) -> ::String

**Parameter**

  * **value** (::String) — App version.

By default, the task is sent to the version which is the default version when the task is attempted.

For some queues or tasks which were created using the App Engine Task Queue API, [host](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_host_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#host \(method\)") is not parsable into [service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_service_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#service \(method\)"), [version](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_version_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#version \(method\)"), and [instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_instance_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#instance \(method\)"). For example, some tasks which were created using the App Engine SDK use a custom domain name; custom domains are not parsed by Cloud Tasks. If [host](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_host_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#host \(method\)") is not parsable, then [service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_service_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#service \(method\)"), [version](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_version_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#version \(method\)"), and [instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_instance_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#instance \(method\)") are the empty string. 




**Returns**

  * (::String) — App version.

By default, the task is sent to the version which is the default version when the task is attempted.

For some queues or tasks which were created using the App Engine Task Queue API, [host](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_host_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#host \(method\)") is not parsable into [service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_service_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#service \(method\)"), [version](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_version_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#version \(method\)"), and [instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_instance_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#instance \(method\)"). For example, some tasks which were created using the App Engine SDK use a custom domain name; custom domains are not parsed by Cloud Tasks. If [host](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_host_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#host \(method\)") is not parsable, then [service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_service_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#service \(method\)"), [version](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_version_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#version \(method\)"), and [instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineRouting#Google__Cloud__Tasks__V2beta3__AppEngineRouting_instance_instance_ "Google::Cloud::Tasks::V2beta3::AppEngineRouting#instance \(method\)") are the empty string. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
