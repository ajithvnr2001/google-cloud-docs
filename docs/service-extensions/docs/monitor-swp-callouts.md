---
url: https://docs.cloud.google.com/service-extensions/docs/monitor-swp-callouts/
title: Logging and monitoring for Secure Web Proxy callouts \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:31.939196+00:00
---

# Logging and monitoring for Secure Web Proxy callouts  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/monitor-swp-callouts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Logging and monitoring for Secure Web Proxy callouts Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page shows you how to configure and use [Cloud Logging](https://docs.cloud.google.com/logging) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring) with Service Extensions callouts for Secure Web Proxy.

## Logging

Secure Web Proxy uses Logging to capture and store several types of logs, including those relating to extensions. For information about Secure Web Proxy logging, see [Logs](https://docs.cloud.google.com/secure-web-proxy/docs/monitor-logs#logs).

In general, Application Load Balancer log entries contain information that is useful for monitoring and debugging your HTTP or HTTPS traffic. Log entries contain the following types of information:

  * Information shown in most Google Cloud logs, such as severity, project ID, project number, and timestamp as described in the [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) log.
  * [HttpRequest](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#HttpRequest) log fields.



Request logs for HTTP and HTTPS load balancers contain a `service_extension_info` object in the load balancer log entry JSON payload with the following information:

Field | Type | Description  
---|---|---  
`backend_target_name` | string | Name of the backend target of the extension.  
`backend_target_type` | string | Type of the backend target.  
`chain` | string | Name of the extension chain within the service extension resource that matches the request.   
`extension` | string | Name of the extension within the extension chain.   
`failed_open` | boolean | When the extension configuration has `failOpen` set to `true`, the value `true` for this metric indicates that processing continued when the extension timed out or failed. Applies only to regional external Application Load Balancers, regional internal Application Load Balancers, and cross-region internal Application Load Balancers.  
`grpc_status` | enum | The most recent status on the gRPC stream. For more information, see [ gRPC status codes](https://grpc.io/docs/guides/status-codes/).   
`per_processing_request_info` | array | A list of either `ProcessingRequest` stats for `ext_proc` extensions or `CheckRequest` stats for `ext_authz` extensions that occur over the gRPC stream.   
`per_processing_request_info[].event_type` | enum | The event type of `ProcessingRequest`. Can be one of these: `REQUEST_HEADERS`, `REQUEST_BODY`, `RESPONSE_HEADERS`, or `RESPONSE_BODY`.   
`per_processing_request_info[].latency` | duration | The duration from when the first byte of the `ProcessingRequest` message is sent to the extension to when the last byte of the `ProcessingResponse` message is received.  
`per_processing_request_info[].processing_effect` | enum | The result of processing for each event in a processing request. Applies only to regional external Application Load Balancers, regional internal Application Load Balancers, and cross-region internal Application Load Balancers. Can be one of the following values:

  * `NONE`: indicates that contents were not changed.
  * `NONE_FAILED_OPEN`: indicates that no mutations were performed because the extension failed open.
  * `CONTENT_MODIFIED`: indicates that content was changed by a successfully applied mutation request.
  * `IMMEDIATE_RESPONSE`: indicates that an immediate response was sent by the extension to halt all further processing.
  * `MUTATION_REJECTED`: indicates that the extension requested at least one disallowed change and further processing was discontinued. Appropriate error messages are logged.
  * `UNSPECIFIED`: indicates that the effect of processing is not known.

  
`per_processing_request_info[].processing_effect_details` | string | When `processing_effect` is `MUTATION_REJECTED`, the details about why a mutation was rejected. Applies only to regional external Application Load Balancers, regional internal Application Load Balancers, and cross-region internal Application Load Balancers.  
`resource` | string | Name of the extension resource  
  
## Monitoring

For information about Monitoring metrics for Secure Web Proxy, see [Available metrics](https://docs.cloud.google.com/secure-web-proxy/docs/monitor-logs#available_metrics).

In [Preview](https://docs.cloud.google.com/products#product-launch-stages), you can monitor the following metrics for extensions on all types of Application Load Balancers. These metrics have the prefix `networkservices.googleapis.com`. The prefix is omitted from the entries in the following table.

The following table provides the metric type, display name, kind, type, unit, and description for each metric.

Metric type | Display name   
Kind, Type, Unit   
Description  
---|---  
`extension/invocation_count` | Extension invocation count   
`DELTA`, `INT64`, `1`   
The number of invocations sent to the extension.  
`extension/invocation_latencies` | Extension invocation latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
The distribution calculated from the latency of each extension invocation.  
`extension/sent_chunks_count` | Extension sent chunks count   
`DELTA`, `INT64`, `1`   
Applicable only for `request_body` and `response_body` events. The number of data chunks sent to the extension.  
`extension/received_chunks_count` | Extension received chunks count   
`DELTA`, `INT64`, `1`   
Applicable only for `request_body` and `response_body` events. The number of chunks received from the extension.  
`extension/failed_open_count` | Extension failed invocations with fail-open   
`DELTA`, `INT64`, `1`   
The number of times that an invocation failed when the system was configured to fail open and the request was allowed to proceed.  
`extension/mutation_rejections_count` | Extension mutation rejections count   
`DELTA`, `INT64`, `1`   
The number of invocations that requested header, body, or trailer mutations but were rejected. Rejections can occur for a variety of reasons, such as when the mutation is invalid or exceeds size limits.  
`extension/sent_bytes_count` | Extension sent bytes count   
`DELTA`, `INT64`, `By`   
The number of bytes sent to the extension.  
`extension/received_bytes_count` | Extension received bytes count   
`DELTA`, `INT64`, `By`   
The number of bytes received from the extension.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
