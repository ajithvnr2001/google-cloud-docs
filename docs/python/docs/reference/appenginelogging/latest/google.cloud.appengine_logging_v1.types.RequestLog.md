---
url: https://docs.cloud.google.com/python/docs/reference/appenginelogging/latest/google.cloud.appengine_logging_v1.types.RequestLog
title: Class RequestLog (1.11.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:29.599535+00:00
---

# Class RequestLog (1.11.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/appenginelogging/latest/google.cloud.appengine_logging_v1.types.RequestLog

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RequestLog (1.11.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.0 (latest)  1.10.0  1.9.0  1.8.0  1.7.0  1.6.2  1.5.0  1.4.5  1.3.2  1.2.0  1.1.6  1.0.0  0.2.0  0.1.5 
    
    
    RequestLog(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Complete log information about a single HTTP request to an App Engine application.

## Attributes  
  
---  
**Name** | **Description**  
`app_id` |  `str`   
Application that handled this request.   
`module_id` |  `str`   
Module of the application that handled this request.   
`version_id` |  `str`   
Version of the application that handled this request.   
`request_id` |  `str`   
Globally unique identifier for a request, which is based on the request start time. Request IDs for requests which started later will compare greater as strings than those for requests which started earlier.   
`ip` |  `str`   
Origin IP address.   
`start_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Time when the request started.   
`end_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Time when the request finished.   
`latency` |  `google.protobuf.duration_pb2.Duration`   
Latency of the request.   
`mega_cycles` |  `int`   
Number of CPU megacycles used to process request.   
`method` |  `str`   
Request method. Example: `"GET"`, `"HEAD"`, `"PUT"`, `"POST"`, `"DELETE"`.   
`resource` |  `str`   
Contains the path and query portion of the URL that was requested. For example, if the URL was "http://example.com/app?name=val", the resource would be "/app?name=val". The fragment identifier, which is identified by the `#` character, is not included.   
`http_version` |  `str`   
HTTP version of request. Example: `"HTTP/1.1"`.   
`status` |  `int`   
HTTP response status code. Example: 200, 404.   
`response_size` |  `int`   
Size in bytes sent back to client by request.   
`referrer` |  `str`   
Referrer URL of request.   
`user_agent` |  `str`   
User agent that made the request.   
`nickname` |  `str`   
The logged-in user who made the request. Most likely, this is the part of the user's email before the `@` sign. The field value is the same for different requests from the same user, but different users can have similar names. This information is also available to the application via the App Engine Users API. This field will be populated starting with App Engine 1.9.21.   
`url_map_entry` |  `str`   
File or class that handled the request.   
`host` |  `str`   
Internet host and port number of the resource being requested.   
`cost` |  `float`   
An indication of the relative cost of serving this request.   
`task_queue_name` |  `str`   
Queue name of the request, in the case of an offline request.   
`task_name` |  `str`   
Task name of the request, in the case of an offline request.   
`was_loading_request` |  `bool`   
Whether this was a loading request for the instance.   
`pending_time` |  `google.protobuf.duration_pb2.Duration`   
Time this request spent in the pending request queue.   
`instance_index` |  `int`   
If the instance processing this request belongs to a manually scaled module, then this is the 0-based index of the instance. Otherwise, this value is -1.   
`finished` |  `bool`   
Whether this request is finished or active.   
`first` |  `bool`   
Whether this is the first `RequestLog` entry for this request. If an active request has several `RequestLog` entries written to Stackdriver Logging, then this field will be set for one of them.   
`instance_id` |  `str`   
An identifier for the instance that handled the request.   
`line` |  `MutableSequence[[google.cloud.appengine_logging_v1.types.LogLine](https://docs.cloud.google.com/python/docs/reference/appenginelogging/latest/google.cloud.appengine_logging_v1.types.LogLine)]`   
A list of log lines emitted by the application while serving this request.   
`app_engine_release` |  `str`   
App Engine release version.   
`trace_id` |  `str`   
Stackdriver Trace identifier for this request.   
`trace_sampled` |  `bool`   
If true, the value in the 'trace_id' field was sampled for storage in a trace backend.   
`source_reference` |  `MutableSequence[[google.cloud.appengine_logging_v1.types.SourceReference](https://docs.cloud.google.com/python/docs/reference/appenginelogging/latest/google.cloud.appengine_logging_v1.types.SourceReference)]`   
Source code for the application that handled this request. There can be more than one source reference per deployed application if source code is distributed among multiple repositories.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
