---
url: https://docs.cloud.google.com/monitoring/api/troubleshooting/
title: Troubleshoot the Monitoring API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:23.091055+00:00
---

# Troubleshoot the Monitoring API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Troubleshoot the Monitoring API Stay organized with collections  Save and categorize content based on your preferences. 

To diagnose API errors, fix metric ingestion rejections, and resolve missing query results when using the Monitoring API, you can use the troubleshooting techniques and error resolutions in this guide.

The Monitoring API is part of Cloud APIs. For a list of shared error codes and general handling recommendations, see [Handling errors](https://docs.cloud.google.com/apis/design/errors#handling_errors).

## Use APIs Explorer for debugging

APIs Explorer is a widget built into the reference pages for API methods. It lets you invoke the method by filling out fields; it doesn't require you to write code.

If you are having trouble with a method invocation, use the APIs Explorer (**Try this API**) widget on the reference page for that method to debug your problem. For more information, see [APIs Explorer](https://docs.cloud.google.com/monitoring/api/apis-explorer).

## General API and authentication errors

This section lists error codes that can be returned by a variety of Monitoring API methods.

### `401 UNAUTHENTICATED`

The `401 UNAUTHENTICATED` error code indicates missing, expired, or invalid OAuth2 or IAM credentials.

The two common error messages for this error code are `Request is missing required authentication credential` and `User is not authorized to access the project (or metric)`.

  * **Cause:** Missing `Authorization: Bearer <token>` header, expired OAuth2 or OIDC token, or invalid service account credentials.
  * **Resolution:** Refresh authentication tokens using Application Default Credentials (ADC) or `gcloud auth print-access-token`. Also, verify that the service account key is valid.

If you aren't using APIs Explorer, then try using it. When your API call works in APIs Explorer, there is probably an authorization issue in the environment where you're making the API call. Go to the [API manager page](https://console.cloud.google.com/apis/enabled) to verify that the Monitoring API is enabled for your project. 

### `403 PERMISSION_DENIED` for project access and billing

The `403 PERMISSION_DENIED` error code indicates you don't have the required permissions to perform the requested action.

There are several different error messages that can be paired with this error code. Two common error messages are `Billing check failed for project [PROJECT_ID]` and `Billing account disabled`:

  * **Cause:** Cloud Billing is disabled or suspended on the Google Cloud project. Custom metric ingestion requires an active billing account.
  * **Resolution:** Link an active Cloud Billing account to the project in the Google Cloud console.



If you receive this error code when writing metric data, then also see `403 PERMISSION_DENIED` when writing metric data.

### `404 NOT_FOUND`

The `404 NOT_FOUND` error code indicates that the target project ID does not exist, or that the region or location is unrecognized.

The following lists common error messages for this error code:

  * `Project [PROJECT_ID] not found`

    * **Cause:** The project specified in the request URI does not exist or has been deleted.
    * **Resolution:** Check the project ID spelling and verify that the project is active in the Google Cloud console.
  * `Unavailable region or location` or `Unrecognized region or location`

    * **Cause:** The monitored resource location or region label is invalid or unrecognized.
    * **Resolution:** Use valid Google Cloud region and zone names, such as `us-central1` or `us-central1-a`.
  * `The requested URL was not found on this server`

    * **Cause:** The resource path in the URL is incorrect.
    * **Resolution:** Compare the URL against the URL for the method shown on the method's reference page. This error might mean that there is a spelling error, such as "project" instead of "projects", or a capitalization error, such as "TimeSeries" instead of "timeSeries".



### `500 INTERNAL`, `503 UNAVAILABLE`, `504 DEADLINE_EXCEEDED`

There are two common error messages for these error codes: `Internal error encountered. Please retry after a few seconds` and `The service is currently unavailable`.

  * **Cause:** Transient backend infrastructure errors, network issues, or internal database partition rebalancing.
  * **Resolution:** Implement truncated exponential backoff with jitter on retries, starting at 1 second up to 32 seconds. Set RPC client deadlines to 15 seconds or greater. For more information, see Retrying API errors.



## Missing results

When an API call returns the status code `200` and an empty response, consider the following:

  * When the call uses a filter, the filter might not have matched anything. The filter match is case-sensitive. To resolve filter problems, start by specifying only one filter component, such as `metric.type`, and verify that you get results. Add the other filter components one by one to build up your request.


  * When working with a custom metric, verify that the project that defines the metric is specified.



There are several reasons why data points might be missing when you use the [`timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method:

  * The data might have aged out. For more information, see [Data retention](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy).

  * The data might not have propagated to Monitoring yet. For more information, see [Latency of metric data](https://docs.cloud.google.com/monitoring/api/v3/latency-n-retention).

  * The interval is invalid:

    * Verify that the end time is correct.
    * Verify that the start time is correct and that it is earlier than the end time. When the start time is missing or malformed, the API sets the start time to the end time. For `GAUGE` metrics, this time interval only matches points whose start and end times are exactly the interval's end time. For `CUMULATIVE` or `DELTA` metrics, which measure across time intervals, no points are matched. For more information, see [Time intervals](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics#time_intervals).



## Errors querying metric data

This section provides information about the errors that can occur when you read metric data using a method such as the [`timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method.

### `400 INVALID_ARGUMENT` when querying metric data

The `400 INVALID_ARGUMENT` error code indicates some type of client-side validation error. The error message associated with the error code provides more detailed information and is specific to the API method.

For example, when querying metric data, you might get the following messages:

  * `Field filter had an invalid value` or `Field filter had an invalid value of "[FILTER]": [EXPLANATION]`

    * **Cause:** Indicates a problem with the monitoring filter.
    * **Resolution:** To resolve, verify the filter's spelling and formatting. For more information, see [Monitoring filters](https://docs.cloud.google.com/monitoring/api/v3/filters).
  * `Request was missing field interval.endTime` or `Field interval.endTime had an invalid value`

    * **Cause:** Indicates that the request is missing the end time or that the value is malformed.
    * **Resolution:** If you are using APIs Explorer, then don't quote the value of the time field. The following are valid formats:
          
          2026-05-11T01:23:45Z
          2026-05-11T01:23:45.678Z
          2026-05-11T01:23:45.678+05:00
          2026-05-11T01:23:45.678-04:30
          ```
          




## Errors writing metric data

This section provides information about the errors that can occur when you use the [`timeSeries.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/create) method to write metric data, including the following:

  * A summary of error codes.
  * A list of error messages associated with each error code. These entries include both a cause and information about resolution. The General API errors also apply to the `create` method.



If you don't enable data access audit logs for Monitoring, then failures with the `timeSeries.create` method might be silent. However, you can do the following:

  * Use the [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) to get information about error rates. Use the following settings:

    * **Metric:** `monitoring.googleapis.com/api/request_count`
    * **Filter:** `method = "google.monitoring.v3.MetricService.CreateTimeSeries"`
    * **Aggregation:** Group by `response_code`


  * Use the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) to query your Admin Activity logs, which the system creates when it attempts to auto-create a metric descriptor and that action fails. To view these log entries, run the following query, after replacing PROJECT_ID with the ID of your Google Cloud project:
        
        logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
        protoPayload.serviceName="monitoring.googleapis.com"
        protoPayload.methodName="google.monitoring.v3.MetricService.CreateMetricDescriptor"
        severity>=ERROR
        

  * Use the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) to query your client-side logs.




If you enable data access audit logs for Cloud Monitoring, then the system writes a log entry for every data access. In particular, these log entries include details about the number of points that failed to write and the cause of the failure:

  * For information about enabling data access audit logs, see [Configure Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).

  * To view these log entries, use the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) and run the following query, after replacing PROJECT_ID with the ID of your Google Cloud project:
        
        logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fdata_access"
        protoPayload.serviceName="monitoring.googleapis.com"
        protoPayload.methodName="google.monitoring.v3.MetricService.CreateTimeSeries"
        severity>=ERROR
        




### Summary of `timeSeries.create` error codes

HTTP Code | gRPC Status Code | Primary Causes  
---|---|---  
`400` | `INVALID_ARGUMENT` | Payload validation failure—batch size, label size or key, timestamp ordering, schema or type mismatch, distribution histogram structure.  
`400` | `FAILED_PRECONDITION` | Sampling rate exceeded, unsupported metric kind, or late arrival outside retention window.  
`401` | `UNAUTHENTICATED` | Missing, expired, or invalid OAuth2 or IAM credentials.  
`403` | `PERMISSION_DENIED` | Missing `roles/monitoring.metricWriter` IAM role, disabled Cloud Billing, or unauthorized attempt to write to reserved system metric domains.  
`404` | `NOT_FOUND` | Target project ID does not exist, or unrecognized region/location.  
`429` | `RESOURCE_EXHAUSTED` | Active time series cardinality limit exceeded on a monitored resource, project metric descriptor limits reached, or API request rate limits exceeded.  
`500` | `INTERNAL` | Internal storage or schema service failure.  
`503` | `UNAVAILABLE` | Transient backend service unavailability.  
`504` | `DEADLINE_EXCEEDED` | Request timed out before writing data points to storage nodes.  
  
### `400 INVALID_ARGUMENT` when writing metric data

`400 INVALID_ARGUMENT` indicates client-side validation errors in the request structure, metric metadata, label definitions, timestamp alignment, or point values.

#### Request structure and batching violations

The following lists error messages related to structure and batching violations:

  * `Request was missing field timeSeries`

    * **Cause:** The `time_series` array in the request was empty.
    * **Resolution:** Include at least one `TimeSeries` object in each request.
  * `The maximum number of TimeSeries objects per Create request is 200`

    * **Cause:** The request contains more than 200 `TimeSeries` objects.
    * **Resolution:** Batch writes to no more than 200 time series per request.
  * `Field points had an invalid value: Only one point can be written per TimeSeries per request`

    * **Cause:** A single `TimeSeries` object contains more than one entry in its `points` field.
    * **Resolution:** Provide exactly one `Point` per `TimeSeries` object per request. To write multiple data points across time for the same metric, send them in separate requests.
  * `Duplicate TimeSeries encountered. Only one point can be written per TimeSeries per request`

    * **Cause:** Two or more `TimeSeries` objects in the same request share identical metric types, metric labels, and monitored resource labels.
    * **Resolution:** Deduplicate time series in client-side batches so each unique time series appears at most once per request.
  * `user defined metrics are not supported on the metric domain "[DOMAIN]"`

    * **Cause:** User-defined metrics aren't supported in the specified domain.
    * **Resolution:** None.



#### Labels and naming constraints

The following lists error messages related to labels and naming constraints:

  * `Field metric.labels had an invalid value of "[KEY]": Label value exceeds the maximum string size of 1024 characters`

    * **Cause:** A metric or resource label value exceeds 1024 characters.
    * **Resolution:** Configure your collector or application to truncate label values to 1024 characters or fewer. Avoid storing high-volume text in metric labels; write these details to Cloud Logging instead.
  * `Field metric.labels had an invalid value of "[KEY]": Label key contains invalid characters`

    * **Cause:** A label key contains characters outside the allowed pattern. Keys can contain alphanumeric characters and underscores, must be 100 characters or fewer, and must start with a letter.
    * **Resolution:** Rename label keys to use only valid characters.
  * `The metric type must be a URL-formatted string with a domain and non-empty path`

    * **Cause:** The `metric.type` is malformed or missing a domain prefix.
    * **Resolution:** Format custom metric types as `custom.googleapis.com/<category>/<name>` or `workload.googleapis.com/<name>`.
  * `Field metric.labels had an invalid value: The metric [METRIC_NAME] has more than [LIMIT] labels`

    * **Cause:** The number of labels on a custom metric descriptor exceeds 30 or, for Prometheus metrics, exceeds 200.
    * **Resolution:** Remove unnecessary labels to stay within the descriptor limit.
  * `unrecognized metric label "[LABEL_KEY]"`

    * **Cause:** The metric descriptor already exists, but the request supplies a label key that is not defined in the descriptor.
    * **Resolution:** Ensure label keys match the existing `MetricDescriptor`, or create a new metric descriptor if schema modification is needed.



#### Project and resource identifier mismatches

The following lists error messages related to project and resource identifier mismatches:

  * `Field resource.labels.project_id had an invalid value of "[VAL]": if present, must be the project number or ID in the request name ([PROJECT])` or `Field resource.labels.project_id had an invalid value of "[VAL]": if present, must be the resource container ID in the request name [PROJECT]`

    * **Cause:** The `project_id` or `resource_container` label specified in `resource.labels` does not match the project ID or number in the request name.
    * **Resolution:** Set the resource `project_id` label to match the request project, or omit the `project_id` label from `resource.labels` so that it defaults to the request project.
  * `unrecognized resource type "[RESOURCE_TYPE]"` or `missing resource type`

    * **Cause:** The `resource.type` is not recognized by Cloud Monitoring, or is omitted for a non-custom metric.
    * **Resolution:** Use a valid monitored resource type, such as `gce_instance`, `k8s_container`, `generic_task`, or `global`.



#### Timestamps and intervals

The following lists error messages related to timestamps and intervals:

  * `Points must be written in order. One or more of the points specified had an older end time than the most recent point`

    * **Cause:** The data point's `end_time` is older than or equal to the timestamp of the most recent data point previously ingested for that time series.
    * **Resolution:** Ingest points strictly in chronological order.
  * `Field points[0].interval.start_time had an invalid value of "[START]": The start time must be equal to the end time ([END]) for the gauge metric '[METRIC]'`

    * **Cause:** A `GAUGE` metric point was submitted where `start_time` does not equal `end_time`.
    * **Resolution:** For `GAUGE` metrics, set `start_time` equal to `end_time` or omit `start_time`.
  * `Field points[0].interval.start_time had an invalid value of "[START]": The start time must be before the end time ([END]) for the non-gauge metric '[METRIC]'`

    * **Cause:** A `CUMULATIVE` or `DELTA` metric point has a `start_time` value that is greater than or equal to the `end_time` value.
    * **Resolution:** Make sure that the `start_time` value is less than the `end_time` value and represents a non-zero time interval.
  * `Field points[0].interval.end_time had an invalid value of "[TIME]": Data points cannot be written more than 5m into the future.`

    * **Cause:** The point's timestamp is more than 5 minutes ahead of current server time.
    * **Resolution:** Synchronize the system clock with Google Public NTP (`time.google.com`).
  * `Field points[0].interval.end_time had an invalid value of "[TIME]": Data points cannot be written more than approximately 24 hours in the past`

    * **Cause:** The point's timestamp is older than the in-memory retention horizon, which is 24 hours.
    * **Resolution:** Write real-time data within 24 hours of generation.



#### Value types and distributions

The following lists error messages related to value types and distributions:

  * `value type for metric must be [EXPECTED], but is [ACTUAL]` or `metric kind for metric must be [EXPECTED], but is [ACTUAL]`

    * **Cause:** The incoming value type—`INT64`, `DOUBLE`, `STRING`, `BOOL`, `DISTRIBUTION`—or metric kind—`GAUGE`, `DELTA`, `CUMULATIVE`—conflicts with the existing `MetricDescriptor`.
    * **Resolution:** Make sure that the data types match the existing descriptor. Value types and metric kinds cannot be modified after creation.
  * `Field points[0].value had an invalid value: The metric value exceeds the maximum string size of 1024 characters`

    * **Cause:** A `STRING` value type metric point exceeds 1024 characters.
    * **Resolution:** Truncate string metric values to 1024 characters or fewer, or send logs to Cloud Logging instead.
  * `Field points[0].value had an invalid value: Bucket options must be specified for Distribution metric`

    * **Cause:** A `DISTRIBUTION` point doesn't specify `bucket_options`.
    * **Resolution:** Define `linear_buckets`, `exponential_buckets`, or `explicit_buckets` for distribution metrics.
  * `Field points[0].value.distributionValue had an invalid value: Distribution value has |bucket_counts| fields that sum to X which does not equal the |count| field value of Y`

    * **Cause:** The sum of counts in `bucket_counts` doesn't equal the `count` field.
    * **Resolution:** Make sure that the sum of all bucket counts equals the sample `count`.
  * `Field points[0].value had an invalid value: Distribution metric has too many buckets`

    * **Cause:** The number of histogram buckets exceeds 200.
    * **Resolution:** Adjust bucket parameters to keep the total bucket count at 200 or fewer.



### `400 FAILED_PRECONDITION`

The following lists error messages related to this error code:

  * `One or more points were written more frequently than the maximum sampling period configured for the metric`

    * **Cause:** Points for the same time series were submitted faster than the maximum allowed rate of one point each 5 seconds.
    * **Resolution:** Rate-limit ingestion so that consecutive points for a specific time series are spaced at least 5 seconds apart.
  * `ingestion of prometheus delta metrics is not supported in this API`

    * **Cause:** The request attempted to write Prometheus `DELTA` metrics through `timeSeries.create`.
    * **Resolution:** Use Prometheus `GAUGE` or `CUMULATIVE` metrics, or ingest through Google Cloud Managed Service for Prometheus OTLP endpoints.
  * `One or more points arrived late outside of its aggregation window`

    * **Cause:** Points arrived past the aggregation window for collection-aggregated metrics.
    * **Resolution:** Flush and stream points with lower buffer latencies.



### `403 PERMISSION_DENIED` when writing metric data

When writing metric data, you can receive a `403 PERMISSION_DENIED` response for reasons related to project access and billing, and for the following reasons:

  * `Permission monitoring.timeSeries.create denied on resource (or it may not exist)`

    * **Cause:** The caller lacks the `monitoring.timeSeries.create` permission on the target project.
    * **Resolution:** Grant the `Monitoring Metric Writer` role (`roles/monitoring.metricWriter`) to the service account or principal.
  * `Billing check failed for project [PROJECT_ID]` or `Billing account disabled`

    * **Cause:** Cloud Billing is disabled or suspended on the Google Cloud project. Custom metric ingestion requires an active billing account.
    * **Resolution:** Link an active Cloud Billing account to the project in the Google Cloud console.
  * `User does not have permission to write to metric [METRIC]`

    * **Cause:** The caller attempted to write custom metrics directly to system-reserved domains, such as `compute.googleapis.com` or `storage.googleapis.com`.
    * **Resolution:** Use custom metric domains such as `custom.googleapis.com/` or `workload.googleapis.com/`.



### `429 RESOURCE_EXHAUSTED`

The following lists error messages related to this error code:

  * `Monitored resource ([RESOURCE_ID]) has too many time series (custom metrics)`

    * **Cause:** **Active time series limit exceeded (high cardinality).** The number of active time series for a single monitored resource exceeded the limit of 200,000 active series in a 24-hour window. For Prometheus metrics, the limit is 1,000,000 active series. This typically happens when ephemeral IDs, such as container IDs, pod UUIDs, request IDs, user IDs, or timestamps, are included in metric labels on churning resources.
    * **Resolution:**
      * Remove ephemeral or high-cardinality labels from your metrics.
      * If you must track metrics for individual ephemeral tasks, use the [`generic_task`](https://docs.cloud.google.com/monitoring/api/resources#tag_generic_task) monitored resource type instead of resource-specific types like `dataflow_job`. Map the ephemeral identifier to the `task_id` label of the `generic_task` resource.
  * `Your Metric Ingestion quota has been exhausted`

    * **Cause:** The project exceeded the API ingestion rate quota.
    * **Resolution:** Batch time series writes up to 200 series per request, or request a quota increase on the Quotas page in the Google Cloud console.
  * `Your Metric Descriptors quota has been exhausted`

    * **Cause:** The project reached the maximum limit of 10,000 custom metric descriptors per project. For Prometheus metrics, this limit is 25,000 per project.
    * **Resolution:** Delete unused metric descriptors by using `projects.metricDescriptors.delete` or reduce dynamic metric naming.
  * `Rate of metric descriptor creation exceeded`

    * **Cause:** The project attempted to create new metric descriptors faster than 6,000 per minute per project.
    * **Resolution:** Avoid dynamically creating new metric types during data ingestion; pre-create descriptors where possible.



## Retrying API errors

Two of the Cloud APIs error codes indicate circumstances in which it might be useful to retry the request:

  * `503 UNAVAILABLE`: retries are useful when the problem is a short-lived or transient condition.
  * `429 RESOURCE_EXHAUSTED`: retries are useful, after a delay, for long-running background jobs with time-based quota such as _n_ calls per _t_ seconds. Retries aren't useful when the problem is a short-lived or transient condition, or when you've exhausted a volume-based quota. For transient conditions, consider tolerating the failure. For quota-related issues, consider reducing your quota usage or requesting a quota increase.



When writing code that might retry requests, first ensure that the request is safe to retry.

### Is the request safe to retry?

If your request is idempotent, then it is safe to retry. An _idempotent_ action is one where any change in state does not depend on the current state. For example:

  * Reading _x_ is idempotent; there is no change to the value.
  * Setting _x_ to 10 is idempotent; this might change the state, if the value isn't already 10, but it doesn't matter what the current value is. And it doesn't matter how many times you attempt to set the value.
  * Incrementing _x_ is _not_ idempotent; the new value depends on the current value.



### Retry with exponential backoff

When implementing code to retry requests, you don't want to rapidly issue new requests indefinitely. If a system is overloaded, this approach contributes to the problem. 

Instead, use a _truncated exponential backoff_ approach. When requests fail because of transient overloads rather than true unavailability, the solution is reduce the load. A truncated exponential backoff follows this general pattern:

  * Establish how long you are willing to wait while retrying or how many attempts you are willing to make. When this limit is exceeded, consider the service unavailable and handle that condition appropriately for your application. This is what makes the backoff _truncated_ ; you stop retrying at some point.

  * Retry the request with increasingly long pauses to _back off_ the frequency of retries. Retry until the request succeeds or your established limit is reached.

The interval is typically increased by some function of the power of the retry count, making it an _exponential_ backoff.




There are many ways to implement an exponential backoff. The following is an example that adds an increasing backoff delay to a minimum delay of 1000ms. The initial backoff delay is 2ms, and it increases to 2 _retry_count_ ms with each attempt.

The following table shows the retry intervals using the initial values:

  * Minimum delay = 1s = 1000ms
  * Initial backoff = 2ms

Retry count | Additional delay (ms) | Retry after (ms)  
---|---|---  
0 | 20 = 1 | 1001  
1 | 21 = 2 | 1002  
2 | 22 = 4 | 1004  
3 | 23 = 8 | 1008  
4 | 24 = 16 | 1016  
... | ... | ...  
_n_ | 2 _n_ | 1000 + 2 _n_  
  
You can truncate the retry cycle by stopping either after _n_ attempts or when the time spent exceeds a reasonable value for your application.

For more information, see the Wikipedia article [Exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
