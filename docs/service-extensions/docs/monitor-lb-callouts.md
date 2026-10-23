---
url: https://docs.cloud.google.com/service-extensions/docs/monitor-lb-callouts/
title: Logging and monitoring for Cloud Load Balancing callouts \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:13.236153+00:00
---

# Logging and monitoring for Cloud Load Balancing callouts  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/monitor-lb-callouts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Logging and monitoring for Cloud Load Balancing callouts Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to configure and use [Cloud Logging](https://docs.cloud.google.com/logging) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring) with Service Extensions callouts for Cloud Load Balancing.

## Logging

This section describes logging for Application Load Balancer callouts.

### Enable logging on a backend service

You can enable logging for Application Load Balancer callouts while creating the service by enabling logging on the backend service that's the _target_ of a request (and not on the backend service associated with the extension).

**Note:** Logging settings, if any, on the callout backend service, which is the backend service pointing to the callout, are ignored.

To enable logging for the target backend service, use the [`gcloud compute backend-services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update).
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --enable-logging \
        --logging-sample-rate=RATE \
        --region=REGION \
        --logging-optional=LOGGING_OPTIONAL_MODE \
        --logging-optional-fields=OPTIONAL_FIELDS
    

Replace the following:

  * `BACKEND_SERVICE`: the name of the backend service
  * `RATE`: a value from `0.0` through `1.0`, where `0.0` means no requests are logged and `1.0` means 100% of requests are logged. The default value is `1.0`. This setting is effective only when used with the `enable-logging` parameter. When you omit `enable-logging`, logging is disabled.
  * `REGION`: the region of the backend
  * `LOGGING_OPTIONAL_MODE`: enables logging for optional fields in one of these modes:

    * `INCLUDE_ALL_OPTIONAL` includes all optional fields.
    * `EXCLUDE_ALL_OPTIONAL` (default) excludes all optional fields.
    * `CUSTOM` includes a custom list of optional fields.
  * `OPTIONAL_FIELDS`: a comma-separated list of optional fields when you select the `CUSTOM` mode



After you enable logging on the backend service, HTTP or HTTPS requests are logged by using [Cloud Logging](https://docs.cloud.google.com/logging/docs) logs requests.

To view logs, in the Google Cloud console, go to the the [Logs Explorer](https://console.cloud.google.com/logs) page.

For more information, see the "Monitor and troubleshoot" pages of the Application Load Balancer documentation, such as [Internal Application Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring).

### Log messages for a backend service

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

This section describes how to monitor callouts [configured using Service Extensions](https://docs.cloud.google.com/service-extensions/docs/configure-callout-backend-service) for Cloud Load Balancing.

### View a Monitoring dashboard

Application Load Balancers export monitoring data to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs).

Use Monitoring metrics for the following purposes:

  * Evaluating a load balancer's configuration, usage, and performance
  * Troubleshooting problems
  * Improving resource utilization and user experience



To view a predefined dashboard, follow these steps:

  1. In the Google Cloud console, go to the **Dashboards overview** page. 

[ Go to Dashboards overview](https://console.cloud.google.com/monitoring/dashboards)

  2. In the **Categories** section, click **GCP**. 
     * To view a list of dashboards for _all_ your load balancers, in the **GCP Dashboards** list, click the dashboard named **Google Cloud Load Balancers**. To view a specific load balancer's dashboard, locate the load balancer in the list and click its name.
     * To view the predefined dashboards for only your load balancers, select the appropriate dashboard.



In addition to the predefined dashboards in Monitoring, you can create custom dashboards, set up alerts, and query the metrics through the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api).

For more information, see the "Monitor and troubleshoot" pages of the Application Load Balancer documentation, such as [Internal Application Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring).

### Monitoring metrics for callouts

You can monitor the following metrics for callout backend services.

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
  
You can also monitor the following metrics. These metrics have the prefix `loadbalancing.googleapis.com/`. The prefix is omitted from the entries in the table.

Metric type | Display name   
Kind, Type, Unit   
Description  
---|---  
`https/backend_request_count`,   
`https/external/regional/backend_request_count`,   
`https/internal/backend_request_count` | Backend request count   
`DELTA`, `INT64`, `1`   
The number of times that a callout backend service is called from the Application Load Balancer.  
`https/backend_request_bytes_count`,   
`https/external/regional/backend_request_bytes_count`,   
`https/internal/backend_request_bytes_count` | Backend request bytes   
`DELTA`, `INT64`, `By`   
The number of bytes sent from the load balancer to the callout backend service.  
`https/backend_response_bytes_count`,   
`https/external/regional/backend_response_bytes_count`,   
`https/internal/backend_response_bytes_count` | Backend response bytes   
`DELTA`, `INT64`, `By`   
The number of bytes received by the load balancer from the extension backend.  
`https/backend_latencies`,   
`https/external/regional/backend_latencies`,   
`https/internal/backend_latencies` | Backend latency   
`DELTA`, `DISTRIBUTION`, `ms`   
A distribution calculated from the sum of latencies of each extension invocation between the load balancer and the callout backend service. Sampled every 60 seconds.   
  
## What's next

  * [View log messages for callouts](https://docs.cloud.google.com/service-extensions/docs/view-callout-log-messages)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
