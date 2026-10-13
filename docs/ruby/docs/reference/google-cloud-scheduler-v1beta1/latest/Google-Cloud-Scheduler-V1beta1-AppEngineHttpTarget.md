---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-scheduler-v1beta1/latest/Google-Cloud-Scheduler-V1beta1-AppEngineHttpTarget/
title: Cloud Scheduler V1beta1 API - Class Google::Cloud::Scheduler::V1beta1::AppEngineHttpTarget (v0.18.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:27.342017+00:00
---

# Cloud Scheduler V1beta1 API - Class Google::Cloud::Scheduler::V1beta1::AppEngineHttpTarget (v0.18.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-scheduler-v1beta1/latest/Google-Cloud-Scheduler-V1beta1-AppEngineHttpTarget/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Scheduler V1beta1 API - Class Google::Cloud::Scheduler::V1beta1::AppEngineHttpTarget (v0.18.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.2 (latest)  0.18.1  0.17.1  0.16.0  0.15.1  0.14.0  0.13.1  0.12.0  0.11.1  0.10.2  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.5 

Reference documentation and code samples for the Cloud Scheduler V1beta1 API class Google::Cloud::Scheduler::V1beta1::AppEngineHttpTarget.

App Engine target. The job will be pushed to a job handler by means of an HTTP request via an [http_method](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-scheduler-v1beta1/latest/Google-Cloud-Scheduler-V1beta1-AppEngineHttpTarget#Google__Cloud__Scheduler__V1beta1__AppEngineHttpTarget_http_method_instance_ "Google::Cloud::Scheduler::V1beta1::AppEngineHttpTarget#http_method \(method\)") such as HTTP POST, HTTP GET, etc. The job is acknowledged by means of an HTTP response code in the range [200 - 299]. Error 503 is considered an App Engine system error instead of an application error. Requests returning error 503 will be retried regardless of retry configuration and not counted against retry counts. Any other response code, or a failure to receive a response before the deadline, constitutes a failed attempt.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #app_engine_routing
    
    
    def app_engine_routing() -> ::Google::Cloud::Scheduler::V1beta1::AppEngineRouting

**Returns**

  * ([::Google::Cloud::Scheduler::V1beta1::AppEngineRouting](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-scheduler-v1beta1/latest/Google-Cloud-Scheduler-V1beta1-AppEngineRouting)) — App Engine Routing setting for the job. 



### #app_engine_routing=
    
    
    def app_engine_routing=(value) -> ::Google::Cloud::Scheduler::V1beta1::AppEngineRouting

**Parameter**

  * **value** ([::Google::Cloud::Scheduler::V1beta1::AppEngineRouting](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-scheduler-v1beta1/latest/Google-Cloud-Scheduler-V1beta1-AppEngineRouting)) — App Engine Routing setting for the job. 



**Returns**

  * ([::Google::Cloud::Scheduler::V1beta1::AppEngineRouting](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-scheduler-v1beta1/latest/Google-Cloud-Scheduler-V1beta1-AppEngineRouting)) — App Engine Routing setting for the job. 



### #body
    
    
    def body() -> ::String

**Returns**

  * (::String) — Body.

HTTP request body. A request body is allowed only if the HTTP method is POST or PUT. It will result in invalid argument error to set a body on a job with an incompatible [HttpMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-scheduler-v1beta1/latest/Google-Cloud-Scheduler-V1beta1-HttpMethod "Google::Cloud::Scheduler::V1beta1::HttpMethod \(module\)"). 




### #body=
    
    
    def body=(value) -> ::String

**Parameter**

  * **value** (::String) — Body.

HTTP request body. A request body is allowed only if the HTTP method is POST or PUT. It will result in invalid argument error to set a body on a job with an incompatible [HttpMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-scheduler-v1beta1/latest/Google-Cloud-Scheduler-V1beta1-HttpMethod "Google::Cloud::Scheduler::V1beta1::HttpMethod \(module\)"). 




**Returns**

  * (::String) — Body.

HTTP request body. A request body is allowed only if the HTTP method is POST or PUT. It will result in invalid argument error to set a body on a job with an incompatible [HttpMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-scheduler-v1beta1/latest/Google-Cloud-Scheduler-V1beta1-HttpMethod "Google::Cloud::Scheduler::V1beta1::HttpMethod \(module\)"). 




### #headers
    
    
    def headers() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — HTTP request headers.

This map contains the header field names and values. Headers can be set when the job is created.

Cloud Scheduler sets some headers to default values:

    * `User-Agent`: By default, this header is `"AppEngine-Google; (+http://code.google.com/appengine)"`. This header can be modified, but Cloud Scheduler will append `"AppEngine-Google; (+http://code.google.com/appengine)"` to the modified `User-Agent`.
    * `X-CloudScheduler`: This header will be set to true.
    * `X-CloudScheduler-JobName`: This header will contain the job name.
    * `X-CloudScheduler-ScheduleTime`: For Cloud Scheduler jobs specified in the unix-cron format, this header will contain the job schedule as an offset of UTC parsed according to RFC3339.

If the job has an [body](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-scheduler-v1beta1/latest/Google-Cloud-Scheduler-V1beta1-AppEngineHttpTarget#Google__Cloud__Scheduler__V1beta1__AppEngineHttpTarget_body_instance_ "Google::Cloud::Scheduler::V1beta1::AppEngineHttpTarget#body \(method\)"), Cloud Scheduler sets the following headers:

    * `Content-Type`: By default, the `Content-Type` header is set to `"application/octet-stream"`. The default can be overridden by explictly setting `Content-Type` to a particular media type when the job is created. For example, `Content-Type` can be set to `"application/json"`.
    * `Content-Length`: This is computed by Cloud Scheduler. This value is output only. It cannot be changed.

The headers below are output only. They cannot be set or overridden:

    * `X-Google-*`: For Google internal use only.
    * `X-AppEngine-*`: For Google internal use only.

In addition, some App Engine headers, which contain job-specific information, are also be sent to the job handler. 




### #headers=
    
    
    def headers=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — HTTP request headers.

This map contains the header field names and values. Headers can be set when the job is created.

Cloud Scheduler sets some headers to default values:

    * `User-Agent`: By default, this header is `"AppEngine-Google; (+http://code.google.com/appengine)"`. This header can be modified, but Cloud Scheduler will append `"AppEngine-Google; (+http://code.google.com/appengine)"` to the modified `User-Agent`.
    * `X-CloudScheduler`: This header will be set to true.
    * `X-CloudScheduler-JobName`: This header will contain the job name.
    * `X-CloudScheduler-ScheduleTime`: For Cloud Scheduler jobs specified in the unix-cron format, this header will contain the job schedule as an offset of UTC parsed according to RFC3339.

If the job has an [body](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-scheduler-v1beta1/latest/Google-Cloud-Scheduler-V1beta1-AppEngineHttpTarget#Google__Cloud__Scheduler__V1beta1__AppEngineHttpTarget_body_instance_ "Google::Cloud::Scheduler::V1beta1::AppEngineHttpTarget#body \(method\)"), Cloud Scheduler sets the following headers:

    * `Content-Type`: By default, the `Content-Type` header is set to `"application/octet-stream"`. The default can be overridden by explictly setting `Content-Type` to a particular media type when the job is created. For example, `Content-Type` can be set to `"application/json"`.
    * `Content-Length`: This is computed by Cloud Scheduler. This value is output only. It cannot be changed.

The headers below are output only. They cannot be set or overridden:

    * `X-Google-*`: For Google internal use only.
    * `X-AppEngine-*`: For Google internal use only.

In addition, some App Engine headers, which contain job-specific information, are also be sent to the job handler. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — HTTP request headers.

This map contains the header field names and values. Headers can be set when the job is created.

Cloud Scheduler sets some headers to default values:

    * `User-Agent`: By default, this header is `"AppEngine-Google; (+http://code.google.com/appengine)"`. This header can be modified, but Cloud Scheduler will append `"AppEngine-Google; (+http://code.google.com/appengine)"` to the modified `User-Agent`.
    * `X-CloudScheduler`: This header will be set to true.
    * `X-CloudScheduler-JobName`: This header will contain the job name.
    * `X-CloudScheduler-ScheduleTime`: For Cloud Scheduler jobs specified in the unix-cron format, this header will contain the job schedule as an offset of UTC parsed according to RFC3339.

If the job has an [body](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-scheduler-v1beta1/latest/Google-Cloud-Scheduler-V1beta1-AppEngineHttpTarget#Google__Cloud__Scheduler__V1beta1__AppEngineHttpTarget_body_instance_ "Google::Cloud::Scheduler::V1beta1::AppEngineHttpTarget#body \(method\)"), Cloud Scheduler sets the following headers:

    * `Content-Type`: By default, the `Content-Type` header is set to `"application/octet-stream"`. The default can be overridden by explictly setting `Content-Type` to a particular media type when the job is created. For example, `Content-Type` can be set to `"application/json"`.
    * `Content-Length`: This is computed by Cloud Scheduler. This value is output only. It cannot be changed.

The headers below are output only. They cannot be set or overridden:

    * `X-Google-*`: For Google internal use only.
    * `X-AppEngine-*`: For Google internal use only.

In addition, some App Engine headers, which contain job-specific information, are also be sent to the job handler. 




### #http_method
    
    
    def http_method() -> ::Google::Cloud::Scheduler::V1beta1::HttpMethod

**Returns**

  * ([::Google::Cloud::Scheduler::V1beta1::HttpMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-scheduler-v1beta1/latest/Google-Cloud-Scheduler-V1beta1-HttpMethod)) — The HTTP method to use for the request. PATCH and OPTIONS are not permitted. 



### #http_method=
    
    
    def http_method=(value) -> ::Google::Cloud::Scheduler::V1beta1::HttpMethod

**Parameter**

  * **value** ([::Google::Cloud::Scheduler::V1beta1::HttpMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-scheduler-v1beta1/latest/Google-Cloud-Scheduler-V1beta1-HttpMethod)) — The HTTP method to use for the request. PATCH and OPTIONS are not permitted. 



**Returns**

  * ([::Google::Cloud::Scheduler::V1beta1::HttpMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-scheduler-v1beta1/latest/Google-Cloud-Scheduler-V1beta1-HttpMethod)) — The HTTP method to use for the request. PATCH and OPTIONS are not permitted. 



### #relative_uri
    
    
    def relative_uri() -> ::String

**Returns**

  * (::String) — The relative URI.

The relative URL must begin with "/" and must be a valid HTTP relative URL. It can contain a path, query string arguments, and `#` fragments. If the relative URL is empty, then the root path "/" will be used. No spaces are allowed, and the maximum length allowed is 2083 characters. 




### #relative_uri=
    
    
    def relative_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — The relative URI.

The relative URL must begin with "/" and must be a valid HTTP relative URL. It can contain a path, query string arguments, and `#` fragments. If the relative URL is empty, then the root path "/" will be used. No spaces are allowed, and the maximum length allowed is 2083 characters. 




**Returns**

  * (::String) — The relative URI.

The relative URL must begin with "/" and must be a valid HTTP relative URL. It can contain a path, query string arguments, and `#` fragments. If the relative URL is empty, then the root path "/" will be used. No spaces are allowed, and the maximum length allowed is 2083 characters. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
