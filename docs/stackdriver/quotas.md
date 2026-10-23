---
url: https://docs.cloud.google.com/stackdriver/quotas/
title: Quotas and limits \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:03.995826+00:00
---

# Quotas and limits  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Resources ](https://docs.cloud.google.com/stackdriver/quotas)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document provides quota and limit information for Google Cloud Observability. For service-specific quota and limit information, see the following documents:

  * [Error Reporting quotas and limits](https://docs.cloud.google.com/error-reporting/quotas)
  * [Cloud Logging quotas and limits](https://docs.cloud.google.com/logging/quotas)
  * [Cloud Monitoring quotas and limits](https://docs.cloud.google.com/monitoring/quotas)
  * [Cloud Profiler quotas and limits](https://docs.cloud.google.com/profiler/quotas)
  * [Cloud Trace quotas and limits](https://docs.cloud.google.com/trace/docs/quotas)
  * Telemetry API quotas and limits

The [Telemetry (OTLP) API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) implements the [OpenTelemetry OTLP specification](https://opentelemetry.io/docs/specs/otlp/) for ingestion of data into Google Cloud Observability. After data is ingested, the other listed quotas and limits apply as well.




## Observability API limits

This section describes the quotas and limits that apply to the [Observability API](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview#about-obs-api).

Description | Value | Notes  
---|---|---  
Data retention for the `_Trace` bucket | 30 days | Not configurable.  
Maximum length of the display name of an observability bucket | 100 encoded bytes | Limit.  
Maximum length of the description of an observability bucket | 1000 encoded bytes | Limit.  
Maximum linked BigQuery datasets per observability dataset | 1 | Limit.  
  
## Telemetry API limits

This section describes only the quotas and limits that apply to the [Telemetry (OTLP) API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) for ingestion of trace, metric, and log data:

  * Limits for traces
  * Limits and quotas for metrics
  * Limits and quotas for logs



These quotas and limits apply only to the data being ingested by using the Telemetry API. After data is ingested, the following quotas and limits apply:

  * [Cloud Trace quotas and limits](https://docs.cloud.google.com/trace/docs/quotas)
  * [Cloud Monitoring quotas and limits](https://docs.cloud.google.com/monitoring/quotas)
  * [Cloud Logging quotas and limits](https://docs.cloud.google.com/logging/quotas)



### Limits for ingestion of traces

This section lists the limits that apply when the Telemetry API is used to ingest trace data. This API is designed for use with applications that are instrumented by using one of the [OpenTelemetry SDKs](https://opentelemetry.io/docs/languages/).

Description | Value | Note  
---|---|---  
Maximum size of attribute keys | 512 bytes | Limit.  
Maximum size of attribute values | 64 KiB | Limit.  
Maximum size of a `Span`* object's name | 1024 bytes | Limit.  
Maximum number of attributes attached to a `Span`* object | 1024 | Limit.  
Maximum number of resource attributes per `ResourceSpans`* object | 1024 | Limit.  
Maximum number of attributes per `ResourceSpan`* object  
Includes attributes attached to child objects of the following types:  
`Resource`, `Span`, `ScopeSpans`, `Event`, and `Link.` | 8192 | Limit.  
Maximum number of `Event`* objects per `Span`* object | 256 | Limit.  
Maximum number of `Link`* objects per `Span`* object | 128 | Limit.  
Maximum size of an `Event`* object's name | 1024 bytes | Limit.  
Maximum number of attributes per `Event`* object | 1024 | Limit.  
Maximum attributes per `Link`* object | 1024 | Limit.  
Maximum size of schema URLs | 8192 bytes | Limit.  
Maximum number of trace-ingestion bytes per minute | 2.4 GB for the following regions: `asia-east1, asia-northeast1, asia-southeast1, asia-south1, europe-west1, europe-west2, europe-west3, europe-west4, us-central1, us-east4, us-west1`. 300 MB for all other regions. | Quota.  
* For a definition of this structure, see the [`trace.proto`](https://github.com/open-telemetry/opentelemetry-proto/blob/v1.5.0/opentelemetry/proto/trace/v1/trace.proto) file.

The [Cloud Trace quotas and limits](https://docs.cloud.google.com/trace/docs/quotas) also apply when using the Telemetry API for trace ingestion.

### Limits and quotas for ingestion of metrics

This section lists the limits and quotas that apply when the Telemetry API is used to ingest metric data.

Description | Value | Note  
---|---|---  
Maximum number of datapoints per request | 200 | Limit  
Maximum number of ResourceMetrics per request | 200 | Limit  
Maximum number of quantiles per Summary metric | 10 | Limit  
Number of metric-ingestion requests per minute per region (quota) | 60,000 | Quota  
  
The [Cloud Monitoring quotas and limits](https://docs.cloud.google.com/monitoring/quotas) also apply when using the Telemetry API for metric ingestion.

### Limits and quotas for ingestion of logs

This section describes the limits and quotas that apply when the Telemetry API ingests log data.

Description | Value | Notes  
---|---|---  
Maximum number of logs per OTLP request | 8192 | Refers to the maximum number of `logRecords` in an OTLP `resourceLogs` structure. Limit.  
Maximum size of each request | 5 MiB | Limit.  
Maximum size of a [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)  
that is created from an OTLP log record | 256 KiB | Cloud Logging truncates or discards data from an OTLP log record when necessary. Limit.  
Maximum length of an attribute key | 512 B | Oversized label keys are truncated when the OTLP log record is converted into a [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry). Limit.  
Maximum length of an attribute value | 64 KiB | Oversized label values when the OTLP log record is converted into a [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry). Limit.  
Maximum depth of attribute nesting | 5 | Attributes that exceed this limit are truncated when the OTLP log record is converted into a [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).  
Maximum number of log-ingestion bytes per minute | 2.4 GB for the following regions: `asia-east1, asia-northeast1, asia-southeast1, asia-south1, europe-west1, europe-west2, europe-west3, europe-west4, us-central1, us-east4, us-west1`. 300 MB for all other regions. | Quota.  
  
The [Cloud Logging quotas and limits](https://docs.cloud.google.com/logging/quotas) also apply when the Telemetry API ingests log data.

## View and manage your quotas

For more information about quotas, including how to view and manage quotas, see the [Cloud Quotas documentation](https://docs.cloud.google.com/docs/quotas/overview).

To view your current quota usage, in the Google Cloud console, go to **APIs & Services** or click the following button:

[Go to **APIs & Services**](https://console.cloud.google.com/apis/dashboard)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
