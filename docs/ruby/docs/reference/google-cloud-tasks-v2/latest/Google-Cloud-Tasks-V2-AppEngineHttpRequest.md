---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineHttpRequest/
title: Cloud Tasks V2 API - Class Google::Cloud::Tasks::V2::AppEngineHttpRequest (v1.7.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:21.283949+00:00
---

# Cloud Tasks V2 API - Class Google::Cloud::Tasks::V2::AppEngineHttpRequest (v1.7.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineHttpRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Tasks V2 API - Class Google::Cloud::Tasks::V2::AppEngineHttpRequest (v1.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.0 (latest)  1.6.1  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.11.0  0.10.2  0.9.0  0.8.2  0.7.0  0.6.0  0.5.0  0.4.6 

Reference documentation and code samples for the Cloud Tasks V2 API class Google::Cloud::Tasks::V2::AppEngineHttpRequest.

App Engine HTTP request.

The message defines the HTTP request that is sent to an App Engine app when the task is dispatched.

Using [AppEngineHttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineHttpRequest "Google::Cloud::Tasks::V2::AppEngineHttpRequest \(class\)") requires [`appengine.applications.get`](https://cloud.google.com/appengine/docs/admin-api/access-control) Google IAM permission for the project and the following scope:

`<https://www.googleapis.com/auth/cloud-platform>`

The task will be delivered to the App Engine app which belongs to the same project as the queue. For more information, see [How Requests are Routed](https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed) and how routing is affected by [dispatch files](https://cloud.google.com/appengine/docs/python/config/dispatchref). Traffic is encrypted during transport and never leaves Google datacenters. Because this traffic is carried over a communication mechanism internal to Google, you cannot explicitly set the protocol (for example, HTTP or HTTPS). The request to the handler, however, will appear to have used the HTTP protocol.

The [AppEngineRouting](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineRouting "Google::Cloud::Tasks::V2::AppEngineRouting \(class\)") used to construct the URL that the task is delivered to can be set at the queue-level or task-level:

  * If [app_engine_routing_override is set on the queue][google.cloud.tasks.v2.Queue.app_engine_routing_override], this value is used for all tasks in the queue, no matter what the setting is for the [task-level app_engine_routing][google.cloud.tasks.v2.AppEngineHttpRequest.app_engine_routing].



The `url` that the task will be sent to is:

  * `url =` [host](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineRouting#Google__Cloud__Tasks__V2__AppEngineRouting_host_instance_ "Google::Cloud::Tasks::V2::AppEngineRouting#host \(method\)") `+` [relative_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineHttpRequest#Google__Cloud__Tasks__V2__AppEngineHttpRequest_relative_uri_instance_ "Google::Cloud::Tasks::V2::AppEngineHttpRequest#relative_uri \(method\)")



Tasks can be dispatched to secure app handlers, unsecure app handlers, and URIs restricted with [`login: admin`](https://cloud.google.com/appengine/docs/standard/python/config/appref). Because tasks are not run as any user, they cannot be dispatched to URIs restricted with [`login: required`](https://cloud.google.com/appengine/docs/standard/python/config/appref) Task dispatches also do not follow redirects.

The task attempt has succeeded if the app's request handler returns an HTTP response code in the range [`200` \- `299`]. The task attempt has failed if the app's handler returns a non-2xx response code or Cloud Tasks does not receive response before the [deadline](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Task#Google__Cloud__Tasks__V2__Task_dispatch_deadline_instance_ "Google::Cloud::Tasks::V2::Task#dispatch_deadline \(method\)"). Failed tasks will be retried according to the [retry configuration][google.cloud.tasks.v2.Queue.retry_config]. `503` (Service Unavailable) is considered an App Engine system error instead of an application error and will cause Cloud Tasks' traffic congestion control to temporarily throttle the queue's dispatches. Unlike other types of task targets, a `429` (Too Many Requests) response from an app handler does not cause traffic congestion control to throttle the queue.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #app_engine_routing
    
    
    def app_engine_routing() -> ::Google::Cloud::Tasks::V2::AppEngineRouting

**Returns**

  * ([::Google::Cloud::Tasks::V2::AppEngineRouting](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineRouting)) — 

Task-level setting for App Engine routing.

    * If [app_engine_routing_override is set on the queue][google.cloud.tasks.v2.Queue.app_engine_routing_override], this value is used for all tasks in the queue, no matter what the setting is for the [task-level app_engine_routing][google.cloud.tasks.v2.AppEngineHttpRequest.app_engine_routing].



### #app_engine_routing=
    
    
    def app_engine_routing=(value) -> ::Google::Cloud::Tasks::V2::AppEngineRouting

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2::AppEngineRouting](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineRouting)) — 

Task-level setting for App Engine routing.

    * If [app_engine_routing_override is set on the queue][google.cloud.tasks.v2.Queue.app_engine_routing_override], this value is used for all tasks in the queue, no matter what the setting is for the [task-level app_engine_routing][google.cloud.tasks.v2.AppEngineHttpRequest.app_engine_routing].



**Returns**

  * ([::Google::Cloud::Tasks::V2::AppEngineRouting](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineRouting)) — 

Task-level setting for App Engine routing.

    * If [app_engine_routing_override is set on the queue][google.cloud.tasks.v2.Queue.app_engine_routing_override], this value is used for all tasks in the queue, no matter what the setting is for the [task-level app_engine_routing][google.cloud.tasks.v2.AppEngineHttpRequest.app_engine_routing].



### #body
    
    
    def body() -> ::String

**Returns**

  * (::String) — HTTP request body.

A request body is allowed only if the HTTP method is POST or PUT. It is an error to set a body on a task with an incompatible [HttpMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-HttpMethod "Google::Cloud::Tasks::V2::HttpMethod \(module\)"). 




### #body=
    
    
    def body=(value) -> ::String

**Parameter**

  * **value** (::String) — HTTP request body.

A request body is allowed only if the HTTP method is POST or PUT. It is an error to set a body on a task with an incompatible [HttpMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-HttpMethod "Google::Cloud::Tasks::V2::HttpMethod \(module\)"). 




**Returns**

  * (::String) — HTTP request body.

A request body is allowed only if the HTTP method is POST or PUT. It is an error to set a body on a task with an incompatible [HttpMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-HttpMethod "Google::Cloud::Tasks::V2::HttpMethod \(module\)"). 




### #headers
    
    
    def headers() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — HTTP request headers.

This map contains the header field names and values. Headers can be set when the [task is created](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_create_task_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#create_task \(method\)"). Repeated headers are not supported but a header value can contain commas.

Cloud Tasks sets some headers to default values:

    * `User-Agent`: By default, this header is `"AppEngine-Google; (+http://code.google.com/appengine)"`. This header can be modified, but Cloud Tasks will append `"AppEngine-Google; (+http://code.google.com/appengine)"` to the modified `User-Agent`.

If the task has a [body](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineHttpRequest#Google__Cloud__Tasks__V2__AppEngineHttpRequest_body_instance_ "Google::Cloud::Tasks::V2::AppEngineHttpRequest#body \(method\)"), Cloud Tasks sets the following headers:

    * `Content-Type`: By default, the `Content-Type` header is set to `"application/octet-stream"`. The default can be overridden by explicitly setting `Content-Type` to a particular media type when the [task is created](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_create_task_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#create_task \(method\)"). For example, `Content-Type` can be set to `"application/json"`.
    * `Content-Length`: This is computed by Cloud Tasks. This value is output only. It cannot be changed.

The headers below cannot be set or overridden:

    * `Host`
    * `X-Google-*`
    * `X-AppEngine-*`

In addition, Cloud Tasks sets some headers when the task is dispatched, such as headers containing information about the task; see [request headers](https://cloud.google.com/tasks/docs/creating-appengine-handlers#reading_request_headers). These headers are set only when the task is dispatched, so they are not visible when the task is returned in a Cloud Tasks response.

Although there is no specific limit for the maximum number of headers or the size, there is a limit on the maximum size of the [Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Task "Google::Cloud::Tasks::V2::Task \(class\)"). For more information, see the [CreateTask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_create_task_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#create_task \(method\)") documentation. 




### #headers=
    
    
    def headers=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — HTTP request headers.

This map contains the header field names and values. Headers can be set when the [task is created](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_create_task_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#create_task \(method\)"). Repeated headers are not supported but a header value can contain commas.

Cloud Tasks sets some headers to default values:

    * `User-Agent`: By default, this header is `"AppEngine-Google; (+http://code.google.com/appengine)"`. This header can be modified, but Cloud Tasks will append `"AppEngine-Google; (+http://code.google.com/appengine)"` to the modified `User-Agent`.

If the task has a [body](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineHttpRequest#Google__Cloud__Tasks__V2__AppEngineHttpRequest_body_instance_ "Google::Cloud::Tasks::V2::AppEngineHttpRequest#body \(method\)"), Cloud Tasks sets the following headers:

    * `Content-Type`: By default, the `Content-Type` header is set to `"application/octet-stream"`. The default can be overridden by explicitly setting `Content-Type` to a particular media type when the [task is created](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_create_task_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#create_task \(method\)"). For example, `Content-Type` can be set to `"application/json"`.
    * `Content-Length`: This is computed by Cloud Tasks. This value is output only. It cannot be changed.

The headers below cannot be set or overridden:

    * `Host`
    * `X-Google-*`
    * `X-AppEngine-*`

In addition, Cloud Tasks sets some headers when the task is dispatched, such as headers containing information about the task; see [request headers](https://cloud.google.com/tasks/docs/creating-appengine-handlers#reading_request_headers). These headers are set only when the task is dispatched, so they are not visible when the task is returned in a Cloud Tasks response.

Although there is no specific limit for the maximum number of headers or the size, there is a limit on the maximum size of the [Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Task "Google::Cloud::Tasks::V2::Task \(class\)"). For more information, see the [CreateTask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_create_task_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#create_task \(method\)") documentation. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — HTTP request headers.

This map contains the header field names and values. Headers can be set when the [task is created](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_create_task_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#create_task \(method\)"). Repeated headers are not supported but a header value can contain commas.

Cloud Tasks sets some headers to default values:

    * `User-Agent`: By default, this header is `"AppEngine-Google; (+http://code.google.com/appengine)"`. This header can be modified, but Cloud Tasks will append `"AppEngine-Google; (+http://code.google.com/appengine)"` to the modified `User-Agent`.

If the task has a [body](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineHttpRequest#Google__Cloud__Tasks__V2__AppEngineHttpRequest_body_instance_ "Google::Cloud::Tasks::V2::AppEngineHttpRequest#body \(method\)"), Cloud Tasks sets the following headers:

    * `Content-Type`: By default, the `Content-Type` header is set to `"application/octet-stream"`. The default can be overridden by explicitly setting `Content-Type` to a particular media type when the [task is created](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_create_task_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#create_task \(method\)"). For example, `Content-Type` can be set to `"application/json"`.
    * `Content-Length`: This is computed by Cloud Tasks. This value is output only. It cannot be changed.

The headers below cannot be set or overridden:

    * `Host`
    * `X-Google-*`
    * `X-AppEngine-*`

In addition, Cloud Tasks sets some headers when the task is dispatched, such as headers containing information about the task; see [request headers](https://cloud.google.com/tasks/docs/creating-appengine-handlers#reading_request_headers). These headers are set only when the task is dispatched, so they are not visible when the task is returned in a Cloud Tasks response.

Although there is no specific limit for the maximum number of headers or the size, there is a limit on the maximum size of the [Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Task "Google::Cloud::Tasks::V2::Task \(class\)"). For more information, see the [CreateTask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_create_task_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#create_task \(method\)") documentation. 




### #http_method
    
    
    def http_method() -> ::Google::Cloud::Tasks::V2::HttpMethod

**Returns**

  * ([::Google::Cloud::Tasks::V2::HttpMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-HttpMethod)) — The HTTP method to use for the request. The default is POST.

The app's request handler for the task's target URL must be able to handle HTTP requests with this http_method, otherwise the task attempt fails with error code 405 (Method Not Allowed). See [Writing a push task request handler](https://cloud.google.com/appengine/docs/java/taskqueue/push/creating-handlers#writing_a_push_task_request_handler) and the App Engine documentation for your runtime on [How Requests are Handled](https://cloud.google.com/appengine/docs/standard/python3/how-requests-are-handled). 




### #http_method=
    
    
    def http_method=(value) -> ::Google::Cloud::Tasks::V2::HttpMethod

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2::HttpMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-HttpMethod)) — The HTTP method to use for the request. The default is POST.

The app's request handler for the task's target URL must be able to handle HTTP requests with this http_method, otherwise the task attempt fails with error code 405 (Method Not Allowed). See [Writing a push task request handler](https://cloud.google.com/appengine/docs/java/taskqueue/push/creating-handlers#writing_a_push_task_request_handler) and the App Engine documentation for your runtime on [How Requests are Handled](https://cloud.google.com/appengine/docs/standard/python3/how-requests-are-handled). 




**Returns**

  * ([::Google::Cloud::Tasks::V2::HttpMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-HttpMethod)) — The HTTP method to use for the request. The default is POST.

The app's request handler for the task's target URL must be able to handle HTTP requests with this http_method, otherwise the task attempt fails with error code 405 (Method Not Allowed). See [Writing a push task request handler](https://cloud.google.com/appengine/docs/java/taskqueue/push/creating-handlers#writing_a_push_task_request_handler) and the App Engine documentation for your runtime on [How Requests are Handled](https://cloud.google.com/appengine/docs/standard/python3/how-requests-are-handled). 




### #relative_uri
    
    
    def relative_uri() -> ::String

**Returns**

  * (::String) — The relative URI.

The relative URI must begin with "/" and must be a valid HTTP relative URI. It can contain a path and query string arguments. If the relative URI is empty, then the root path "/" will be used. No spaces are allowed, and the maximum length allowed is 2083 characters. 




### #relative_uri=
    
    
    def relative_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — The relative URI.

The relative URI must begin with "/" and must be a valid HTTP relative URI. It can contain a path and query string arguments. If the relative URI is empty, then the root path "/" will be used. No spaces are allowed, and the maximum length allowed is 2083 characters. 




**Returns**

  * (::String) — The relative URI.

The relative URI must begin with "/" and must be a valid HTTP relative URI. It can contain a path and query string arguments. If the relative URI is empty, then the root path "/" will be used. No spaces are allowed, and the maximum length allowed is 2083 characters. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
