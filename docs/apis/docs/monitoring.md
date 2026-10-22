---
url: https://docs.cloud.google.com/apis/docs/monitoring/
title: Monitoring API usage \u00a0|\u00a0 Cloud APIs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:17.711532+00:00
---

# Monitoring API usage  |  Cloud APIs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apis/docs/monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)



Send feedback 

#  Monitoring API usage Stay organized with collections  Save and categorize content based on your preferences. 

_API metrics_ let you track signals such as request counts, error rates, and latencies for Google APIs and Google Cloud APIs, helping you monitor application performance and troubleshoot errors. You can inspect telemetry in the [API Dashboard](https://console.cloud.google.com/apis/dashboard) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs), where metrics reflect traffic for your project rather than overall service status. For API metric definitions, see the [Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-serviceruntime).

## Using the API Dashboard

The simplest way to view your API metrics is to use the Google Cloud console's [API Dashboard](https://console.cloud.google.com/apis/dashboard). You can see an overview of all your API usage, or you can drill down to your usage of a specific API.

To see an overview of your API usage:

  1. Visit Cloud console's [APIs and Services](https://console.cloud.google.com/apis/) section. The main API Dashboard is displayed by default. In this page you can see all the APIs you currently have enabled for your project, as well as overview charts for the following metrics:

     * **Traffic** : the number of requests per second made by or about your project to enabled APIs
     * **Errors** : the percentage of requests to enabled APIs that resulted in errors
     * **Median latency** : the median latency for requests to enabled APIs, if available".

**Note:** The "Project Viewer" IAM permission is sufficient to view this dashboard.

To view usage details for a specific API:

  1. Select the API you want to view in the main API Dashboard list of APIs. The API's Overview page shows a more detailed traffic chart with a breakdown by response code.
  2. For even more detailed usage information, select **View metrics**. By default, the following pre-built charts are displayed, though more are available:

     * Traffic by response code
     * Errors by API method
     * Overall latency at the 50th, 95th, and 99th percentile
     * Latency by API method (median)
  3. If you want to add more charts, you can select additional pre-built charts from the **Select Graphs** drop-down menu.




## Using Cloud Monitoring

If you use Cloud Monitoring, you can dive deeper into available metrics data using the Metrics Explorer to give you greater insight into your API usage. Cloud Monitoring supports a wide variety of metrics, which you can combine with filters and aggregations for new and insightful views into your application performance. For example, you can combine a request count metric with a filter on the HTTP Response Code class to build a dashboard that shows error rates over time, or you can look at the 95th percentile latency of requests to the Cloud Pub/Sub API.

#### Available metrics

The following table lists the available `serviceruntime` metrics. The API-usage metrics are those that include [ `consumed_api`](https://docs.cloud.google.com/monitoring/api/resources#tag_consumed_api) as a monitored resource.

The "metric type" strings in this table must be prefixed with `serviceruntime.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`api/request_count` GA ** _(project)_**   
Request count   
`DELTA`, `INT64`, `1`   
**[api](https://docs.cloud.google.com/monitoring/api/resources#tag_api)**   
**[consumed_api](https://docs.cloud.google.com/monitoring/api/resources#tag_consumed_api)**   
**[produced_api](https://docs.cloud.google.com/monitoring/api/resources#tag_produced_api)** |  _The count of completed requests. Sampled every 60 seconds. After sampling, data is not visible for up to 1800 seconds._   
`protocol`: The protocol of the request, e.g. "http", "grpc".   
`response_code`: The HTTP response code for HTTP requests, or HTTP equivalent code for gRPC requests. See code mapping in <https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto>.   
`response_code_class`: The response code class for HTTP requests, or HTTP equivalent class for gRPC requests, e.g. "2xx", "4xx".   
`grpc_status_code`: The numeric gRPC response code for gRPC requests, or gRPC equivalent code for HTTP requests. See code mapping in <https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto>.   
`api/request_latencies` GA ** _(project)_**   
Request latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[api](https://docs.cloud.google.com/monitoring/api/resources#tag_api)**   
**[consumed_api](https://docs.cloud.google.com/monitoring/api/resources#tag_consumed_api)**   
**[produced_api](https://docs.cloud.google.com/monitoring/api/resources#tag_produced_api)** |  _Distribution of latencies in seconds for non-streaming requests. Sampled every 60 seconds. After sampling, data is not visible for up to 1800 seconds._  
`api/request_latencies_backend` GA ** _(project)_**   
Request backend latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[api](https://docs.cloud.google.com/monitoring/api/resources#tag_api)**   
**[produced_api](https://docs.cloud.google.com/monitoring/api/resources#tag_produced_api)** |  _Distribution of backend latencies in seconds for non-streaming requests. Sampled every 60 seconds. After sampling, data is not visible for up to 1800 seconds._  
`api/request_latencies_overhead` GA ** _(project)_**   
Request overhead latencies   
`DELTA`, `DISTRIBUTION`, `s`   
**[api](https://docs.cloud.google.com/monitoring/api/resources#tag_api)**   
**[produced_api](https://docs.cloud.google.com/monitoring/api/resources#tag_produced_api)** |  _Distribution of request latencies in seconds for non-streaming requests excluding the backend. Sampled every 60 seconds. After sampling, data is not visible for up to 1800 seconds._  
`api/request_sizes` GA ** _(project)_**   
Request sizes   
`DELTA`, `DISTRIBUTION`, `By`   
**[api](https://docs.cloud.google.com/monitoring/api/resources#tag_api)**   
**[consumed_api](https://docs.cloud.google.com/monitoring/api/resources#tag_consumed_api)**   
**[produced_api](https://docs.cloud.google.com/monitoring/api/resources#tag_produced_api)** |  _Distribution of request sizes in bytes recorded at request completion. Sampled every 60 seconds. After sampling, data is not visible for up to 1800 seconds._  
`api/response_sizes` GA ** _(project)_**   
Response sizes   
`DELTA`, `DISTRIBUTION`, `By`   
**[api](https://docs.cloud.google.com/monitoring/api/resources#tag_api)**   
**[consumed_api](https://docs.cloud.google.com/monitoring/api/resources#tag_consumed_api)**   
**[produced_api](https://docs.cloud.google.com/monitoring/api/resources#tag_produced_api)** |  _Distribution of response sizes in bytes recorded at request completion. Sampled every 60 seconds. After sampling, data is not visible for up to 1800 seconds._  
`mcp/request_count` GA ** _(project)_**   
MCP Request Count   
`DELTA`, `INT64`, `1`   
**[consumed_mcp_api](https://docs.cloud.google.com/monitoring/api/resources#tag_consumed_mcp_api)** |  _The count of MCP requests._   
`response_code`: The HTTP response code for HTTP requests, or HTTP equivalent code for MCP requests.   
`response_code_class`: The response code class for HTTP requests, or HTTP equivalent class for gRPC requests, e.g. '2xx', '4xx'.   
`mcp/request_durations` GA ** _(project)_**   
MCP Request Duration   
`DELTA`, `DISTRIBUTION`, `s`   
**[consumed_mcp_api](https://docs.cloud.google.com/monitoring/api/resources#tag_consumed_mcp_api)** |  _The duration of the MCP request from the time it was sent until the response or ack is received._  
`quota/allocation/usage` GA ** _(project, folder, organization)_**   
Allocation quota usage   
`GAUGE`, `INT64`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)**   
**[producer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_producer_quota)** |  _The total consumed allocation quota. Values reported more than 1/min are dropped. If no changes are received in quota usage, the last value is repeated at least every 24 hours. Sampled every 60 seconds._   
`quota_metric`: The name of quota metric or quota group.   
`quota/concurrent/exceeded` ALPHA ** _(project, folder, organization)_**   
Concurrent Quota Exceeded   
`DELTA`, `INT64`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)** |  _The number of times exceeding the concurrent quota was attempted. Sampled every 86400 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`quota_metric`: The name of quota metric or quota group.   
`time_window`: The window size for concurrent operation limits.   
`quota/concurrent/limit` ALPHA ** _(project, folder, organization)_**   
Concurrent Quota limit   
`GAUGE`, `INT64`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)**   
**[producer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_producer_quota)** |  _The concurrent limit for the quota. Sampled every 86400 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`quota_metric`: The name of quota metric or quota group.   
`time_window`: The window size for concurrent operation limits.   
`quota/concurrent/usage` ALPHA ** _(project, folder, organization)_**   
Concurrent Quota usage   
`GAUGE`, `INT64`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)**   
**[producer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_producer_quota)** |  _The concurrent usage of the quota. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`quota_metric`: The name of quota metric or quota group.   
`time_window`: The window size for concurrent operation limits.   
`quota/exceeded` GA ** _(project, folder, organization)_**   
Quota exceeded error   
`GAUGE`, `BOOL`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)** |  _The error happened when the quota limit was exceeded. Sampled every 60 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`quota_metric`: The name of quota metric or quota group.   
`quota/limit` GA ** _(project, folder, organization)_**   
Quota limit   
`GAUGE`, `INT64`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)**   
**[producer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_producer_quota)** |  _The limit for the quota. Sampled every 86400 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`quota_metric`: The name of quota metric or quota group.   
`quota/rate/net_usage` GA ** _(project, folder, organization)_**   
Rate quota usage   
`DELTA`, `INT64`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)**   
**[producer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_producer_quota)** |  _The total consumed rate quota. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`method`: The API method name, such as "disks.list".   
`quota_metric`: The name of quota metric or quota group.   
`quota/ratev2/exceeded` BETA ** _(project, folder, organization)_**   
Windowed Rate Quota Exceeded   
`DELTA`, `INT64`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)** |  _The number of times exceeding the windowed rate quota was attempted. Sampled every 86400 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`quota_metric`: The name of quota metric or quota group.   
`window_size`: The window size for rate operation limits.   
`quota/ratev2/limit` BETA ** _(project, folder, organization)_**   
Windowed Rate Quota limit   
`GAUGE`, `INT64`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)**   
**[producer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_producer_quota)** |  _The windowed rate limit for the quota. Sampled every 86400 seconds. After sampling, data is not visible for up to 180 seconds._   
`limit_name`: The quota limit name, such as "Requests per day" or "In-use IP addresses".   
`quota_metric`: The name of quota metric or quota group.   
`window_size`: The window size for rate operation limits.   
`quota/ratev2/net_usage` BETA ** _(project, folder, organization)_**   
Windowed Rate Quota usage   
`GAUGE`, `INT64`, `1`   
**[consumer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_consumer_quota)**   
**[producer_quota](https://docs.cloud.google.com/monitoring/api/resources#tag_producer_quota)** |  _The windowed rate usage of the quota. Sampled every 60 seconds. After sampling, data is not visible for up to 240 seconds._   
`method`: The API method name, such as "disks.list".   
`limit_name`: The quota limit name, such as "RequestsPerDay" or "InUseIpAddresses".   
`quota_metric`: The name of quota metric or quota group.   
`window_size`: The window size for rate operation limits.   
`window_start_time`: The start time of the window.   
  
Table generated at 2026-10-14 20:24:33 UTC.

To see API metrics in Metrics Explorer, select **Consumed API** as the resource type, then select one of the `serviceruntime` metrics. Then use the filter and aggregation options to refine your data. After you've found the API usage information you want, you can use Cloud Monitoring to create custom dashboards and alerts that will help you continue to monitor and maintain a robust application. You can find out how to do this in the following pages:

  * [Building charts](https://docs.cloud.google.com/monitoring/charts)
  * [Introduction to alerting](https://docs.cloud.google.com/monitoring/alerts)
  * [Managing alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui)



For more information, see [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

## Troubleshooting with API metrics

API metrics can be particularly useful if you need to contact Google when something goes wrong, and may even show you that you don't need to contact support at all. For example:

  * If all of your calls to a service are failing for a single credential ID, but not any other, chances are there is something wrong with that account that you can easily fix yourself without opening a ticket.
  * You’re troubleshooting a problem with your app, and notice a correlation between your application’s degraded performance and a sustained increase in the 50th percentile latency of a critical GCP service. Definitely call us and point us to this data so we can start working on the problem as quickly as possible.
  * The latencies for a GCP service report look good and unchanged from before, but your in-app metrics report that the latency on calls to the service is abnormally high. That tells you that there is some trouble in the network. Call your network provider (in some cases, Google) to get the debugging process started.



## Best practices

While API metrics are an extremely useful tool, there are issues you need to consider to make sure they provide useful information, particularly when setting up alerts based on metric values. The following best practices will help you get the most from API metrics data.

### Is latency causing a problem?

While some services are quite latency-sensitive, for others scale and reliability matter more. Some APIs, [Cloud Storage](https://docs.cloud.google.com/storage/docs) or [BigQuery](https://docs.cloud.google.com/bigquery/docs) for example, can have a couple of seconds of high latency without customers noticing. With data from API metrics, you can learn what your users need from a given service.

### Look for changes from the norm

Before you decide to alert on a particular metric value, consider what actually counts as unusual behavior. Looking at your API metrics can show you that latency results for most services fall within a normal distribution: a big hump in the middle, and outliers on either side. The metrics will help you understand the normal distribution so that you can engineer your app to work well within the distribution curve. Metrics can also help you correlate distribution changes with times where your app is not working as intended, to help you find the root cause of an issue. We expect the 99th percentile to look very different than the median — what we don’t expect are dramatic changes in those percentiles over time.

Also you may see that some kinds of requests take longer than others. If the median size of a photo uploaded to Google Photos is 4 MB, but you normally upload 20 MB RAW files, your average time to upload 20 photos is likely to be substantially worse than that of most users, but is still _your_ normal behavior.

All this means that it's not particularly useful to alert the first time a second-long RPC or 5xx HTTP call is detected. Instead, when investigating a Google service as a possible cause for an issue your application is experiencing, compare the return codes and latency rates over time and **look for sustained changes from the norm that are correlated with observed issues in your application**.

### Traffic rate

API metrics are most useful where you have a high volume of traffic going to the API. If you call a service only intermittently, your API metrics won’t be statistically valid and won’t give you meaningful triage information.

For example, if you want to track the 99.5th percentile latency for a service, and you only do 100 calls an hour, watching the measurement over a two hour period would only give you one data point to represent the 99.5th percentile, which won't tell you much about the normal behavior of the API or your application. Make sure the traffic rate, the percentile you are tracking, and the time window you are considering generate many data points of interest or the monitoring data will not be helpful to you.

## Supported APIs

All Google APIs and Google Cloud APIs, as well as APIs built on top of Cloud Endpoints and API Gateway, support API metrics. If you are an API consumer, you can view the Consumed API metrics in the [API Dashboard](https://console.cloud.google.com/apis/dashboard). If you are an API producer, you can view the Produced API metrics in the [Endpoints Dashboard](https://console.cloud.google.com/endpoints).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
