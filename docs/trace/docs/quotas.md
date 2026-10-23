---
url: https://docs.cloud.google.com/trace/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:29.692402+00:00
---

# Quotas and limits  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Resources ](https://docs.cloud.google.com/trace/docs/quotas)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Trace enforces rate quotas, span ingestion limits, and data retention periods that depend on whether you send trace data by using the [Telemetry (OTLP) API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) or the [Cloud Trace API](https://docs.cloud.google.com/trace/api). Understanding these thresholds helps you monitor your usage so you don't lose observability into your applications.

## Trace API quotas and limits

This section provides information about quotas and limits that apply only to the Trace API. The quotas and limits listed in this section don't apply to the Telemetry API.

Cloud Trace enforces two different types of quotas: a rate quota on your Cloud Trace API requests and an ingestion quota on spans you send to Trace.

### Quotas

The following table summarizes the quota units available for read and write operations, and the daily quota for ingesting spans for the Trace API. For example, you have a total of 300 per 60 seconds for the three API commands `GetTrace`, `ListTraces`, and `ListSpan`. Here are two different examples of how you could use all of the available quota units:

  * Make 12 `ListTraces` API calls per 60 seconds.
  * Make 10 `ListTraces` API calls and 50 `GetTrace` API calls per 60 seconds.

Category | Total quota units  
---|---  
Read operations1 | 300 per 60 seconds  
Write operations2 | 4,800 per 60 seconds  
Ingested spans3,4 | 3,000,000 per day - 5,000,000,000 per day  
  
1 Read operations include `GetTrace`, `ListTraces`, `ListSpan`. A call to `ListTraces` consumes 25 quota units. Calls to `GetTrace` consume `ListSpan` 1 quota unit. Querying and viewing traces using the **Trace Explorer** in the Google Cloud console doesn't consume this quota.  
2 Write operations include `PatchTraces`, `BatchWrite`, and `CreateSpan`. Each write operation consumes 1 quota unit.  
3 This quota only applies to spans ingested using the Cloud Trace API. Ingestion through the Telemetry API is unrestricted. 4 Your daily trace span ingestion quota for the Cloud Trace API is determined by your billing account history and requests you have made for quota increases. 

### Limits

This table lists the limits for the Cloud Trace API.

Description | Value  
---|---  
Maximum number of spans per `GetTrace` call | 10,000  
Maximum number of spans per `PatchTraces` call | 25,000  
Maximum number of traces per `ListTraces` call | 1,000 in the `ROOTSPAN` and `MINIMAL` views  
100 in the `COMPLETE` view  
Maximum length of a span name | 1024 bytes  
Maximum number of labels or attributes per span | 1024  
Maximum size of key for a label or attribute | 512 bytes  
Maximum size of value for a label or attribute | 65,532 bytes  
Maximum number of events per span | 256  
Maximum past timestamp for a span to be ingested | 14 days  
Maximum future timestamp for a span to be ingested | 3 days  
Maximum past timestamp for event relative to span timestamp | 365 days  
  
Exceeding a limit might not result in an API call failing with an error. For example, an error isn't reported when the number of attributes attached a span exceeds 1024. Instead, in this scenario, the Cloud Trace API uses a non-deterministic algorithm to select 1024 attributes to ingest. The remaining attributes are discarded.

The [Cloud Trace API](https://docs.cloud.google.com/trace/api) provides details about the [`GetTrace`](https://docs.cloud.google.com/trace/docs/reference/v1/rest/v1/projects.traces/get), [`PatchTraces`](https://docs.cloud.google.com/trace/docs/reference/v1/rest/v1/projects/patchTraces), and [`ListTraces`](https://docs.cloud.google.com/trace/docs/reference/v1/rest/v1/projects.traces/list) endpoints.

How you annotate spans depends on the Cloud Trace API endpoint. If you use the `batchWrite` endpoint, then add attributes to the [`Span`](https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2/projects.traces/batchWrite#Span) object. If you use the `patchTraces` endpoint, then add labels to the [`TraceSpan`](https://docs.cloud.google.com/trace/docs/reference/v1/rest/v1/projects.traces#TraceSpan) object.

## Telemetry API limits and quotas

This section lists the limits that apply only when the [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) is used to ingest trace data. The Telemetry API, which implements the OpenTelemetry OTLP API, is designed for use with applications that are instrumented by using one of the [OpenTelemetry SDKs](https://opentelemetry.io/docs/languages/). The limits listed in this section don't apply to the Cloud Trace API.

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

## Limits on trace scopes

Limits on trace scopes | Value  
---|---  
Maximum number of trace scopes per project | 100  
Maximum number of views per trace scope | 20  
  
## Trace retention periods

Category | Retention period  
---|---  
Spans stored in the [`_Trace` bucket](https://docs.cloud.google.com/trace/docs/storage-overview) | 30 days  
  
## Manage your quota

This section describes how to request a change in a quota and how to monitor your quota usage.

### Request changes to Cloud Trace API quotas

To determine whether you can request a higher or lower Cloud Trace API limit for quota by using the Google Cloud console, go to the **Quotas & System Limits** page and search for the quota of interest.

  * If the quota is listed, then you can use that page to request a change to the limit. For information about those steps, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).


  * If the quota isn't listed or if you request a quota update and get the error `Edit is not allowed for this quota`, then [contact Cloud Customer Care](https://cloud.google.com/support) and request a change to the quota. Billing must be enabled on the Google Cloud project to edit quotas in the Google Cloud console.



### Monitor you quota usage

To make sure that you don't run out of quota and lose observability into your apps' performance, verify that you batch your updates and monitor your quota usage. For example, you might create an alerting policy that notifies you when your usage exceeds a threshold. For detailed information on monitoring your API requests and understanding their responses, see [Monitoring your API usage](https://docs.cloud.google.com/apis/docs/monitoring).

  * To view your **Cloud Trace API** and your daily span ingestion quotas, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).

  * To learn how to decrease your API quota units and your daily span ingestion quota units, see [Capping usage](https://docs.cloud.google.com/docs/quotas/view-manage#capping_usage).

  * To request an increase in your API quota units or your daily span ingestion quotas, see [Request more quota](https://docs.cloud.google.com/trace/docs/quotas#more-quota).

  * See [Creating an over-quota alert](https://docs.cloud.google.com/trace/docs/trace-alerting#over-quota-alert) for detailed information on creating alerting policies to monitor your Trace API quota and your rate trace span ingestion.




### High-volume querying

For high-volume querying of your trace data, create a [linked BigQuery dataset](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset) and then use the BigQuery API.

Don't use the Cloud Trace API for high-volume querying because calls to the Trace API are rate limited.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
