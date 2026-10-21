---
url: https://docs.cloud.google.com/logging/quotas/
title: Quotas and limits \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:05.897270+00:00
---

# Quotas and limits  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Resources ](https://docs.cloud.google.com/logging/quotas)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

To help you plan capacity and avoid service disruptions, Cloud Logging applies quotas and system limits to API requests, storage, and resource configurations. You can request increases for most quotas, but system limits are fixed and can't be changed.

## Logging quotas and usage limits

The following table lists quotas and limits that apply to the usage of Cloud Logging. In general, you can request an increase for a quota. However, limits can't be changed.

Some entries are listed as being per project, but the note indicates that the entry also applies to billing accounts, folders, and organizations and isn't hierarchical. For example, if you have multiple Google Cloud projects in an organization, then you could configure up to 200 sinks for each Google Cloud project; for that same organization, you could also configure up to 200 sinks at the organization level.

Category | Maximum value of limit or  
initial quota value | Notes  
---|---|---  
Size of a [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) | 256 KiB | This limit is approximate and is based on internal data sizes, not the actual REST API request size. Cannot be increased.  
Size of an [audit log entry](https://docs.cloud.google.com/logging/docs/audit) | 512 KiB | Cannot be increased.  
Number of labels  | 64 per `LogEntry` | Cannot be increased.  
Length of a `LogEntry` label key  | 512 B | Cloud Logging truncates oversized label keys when the associated log entry is written. Cannot be increased.  
Length of a `LogEntry` label value | 64 KiB | Cloud Logging truncates oversized label values when the associated log entry is written. Cannot be increased.  
Length of a [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language) query | 20,000 characters | Cannot be increased.  
Query fanout | 200 buckets | This limit is the maximum number of buckets that might contain log entries for a resource. For more information, see [Query returns an error](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#invalid-query). Cannot be increased. For performance reasons, minimize the number of log buckets and create your log buckets in one region. If you frequently need to query log entries that originate in different resources, then consider routing log entries to a few centralized log buckets.  
Number of [sinks](https://docs.cloud.google.com/logging/docs/routing/overview#sinks) | 200 per Google Cloud project | Can be increased to 4,000. This quota also applies to billing accounts, folders, and organizations and isn't hierarchical.  
Length of a [sink inclusion filter](https://docs.cloud.google.com/logging/docs/routing/overview#inclusion-filters) | 20,000 characters | Cannot be increased.  
Length of a [sink exclusion filter](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions) | 20,000 characters | Cannot be increased.  
Number of [exclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions) | 50 per sink | Cannot be increased. If you need more than 50 exclusion filters, then refine the inclusion filter.  
Number of [log buckets](https://docs.cloud.google.com/logging/docs/buckets) | 100 per Google Cloud project | Can be increased to 2,500. This quota is the maximum number of buckets that might contain log entries for a resource and it includes buckets that are [pending deletion](https://docs.cloud.google.com/logging/docs/buckets#deleting-logs-bucket). This quota also applies to billing accounts, folders, and organizations and isn't hierarchical. If you increase the maximum number of log buckets, then you might have a degraded user experience because the default log scope can't include all log buckets in a project.  
Number of [custom indexed fields](https://docs.cloud.google.com/logging/docs/analyze/custom-index) | 20 per log bucket | Cannot be increased. Cloud Logging supports full-text indexing. Therefore, we don't recommend that you define custom indexing.  
Number of [log views](https://docs.cloud.google.com/logging/docs/logs-views) | 30 per log bucket | Can be increased to 1,000 log views on a single log bucket. If you increase the maximum number of log views, then you might have a degraded user experience because the default log scope can't include all log views in a project.  
Oldest timestamp that can be stored in log buckets | Determined by the retention period of the log bucket. | For a custom log bucket with the default retention period, this value is 30 days in the past. The Logging API accepts log entries with older timestamps, and those log entries are routed to sink destinations. However, if log entries with older timestamps are routed to a log bucket, then they aren't stored.  
Future timestamp that can be stored in log buckets | Up to 1 day in the future | The Logging API rejects entries with timestamps more than 1 day in the future and returns an `INVALID_ARGUMENT` error. Cannot be increased.   
Number of [log scopes](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage) per resource | 100 | Can be increased to 10,000.   
Number of log views and projects included in a log scope | 100 | We recommend that a log scope list log views instead of projects when possible. Listing log views results in reduced query time and increased clarity as to which log entries are being queried.  
Number of projects included in a log scope | 5 | We recommend that a log scope list log views instead of projects, when possible. The log views can be in different projects.  
Maximum number of analytics views per Google Cloud project | 100 | Cannot be increased.This feature is in Public Preview.  
Per Google Cloud project, the maximum number of analytics views per region | 50 | Cannot be increased.This feature is in Public Preview.  
Per Google Cloud project, the maximum number of regions that can store analytics views | 10 | Cannot be increased.This feature is in Public Preview.  
  
## Logging API quotas and limits

The following limits apply to your usage of the Logging API. You can request changes to your Logging API quotas and limits; for instructions, see Request changes to Cloud Logging API quotas on this page.

To view your API quotas, go to the [API dashboard](https://console.cloud.google.com/apis/dashboard), select an API, and then select **Quotas**.

Category | Maximum value of limit or   
initial quota value | Notes  
---|---|---  
Lifetime of API page tokens | 24 hours | Cannot be increased.  
Number of open live-tailing sessions | 10 per Google Cloud project | Cannot be increased. This limit also applies to billing accounts, folders, and organizations and isn't hierarchical.  
Number of live-tailing entries returned | 60,000 per minute | Cannot be increased.  
Number of [restricted fields](https://docs.cloud.google.com/logging/docs/field-level-acl) | 20 per bucket | Cannot be increased.  
Size of a restricted field | 800 B | Cannot be increased.  
Size of an `entries.write` request | 10 MB | Cannot be increased.  
Rate of `entries.write` requests, by region | 4.8 GB per minute, per Google Cloud project in the regions `asia-east1`, `asia-northeast1`, `asia-southeast1`, `asia-south1`, `europe-west1`, `europe-west2`, `europe-west3`, `europe-west4`, `us-central1`, `us-east4`, `us-west1`   
  
300 MB per minute, per Google Cloud project in all remaining regions | You can request a quota increase. This quota also applies to billing accounts, folders, and organizations and isn't hierarchical. For more information about these quotas, see  Per-region ingestion quotas. Using [exclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions) doesn't reduce the rate of write requests because log entries are excluded after the `entries.write` request is made.  
Number of `entries.list` requests | 60 per minute, per Google Cloud project | Cannot be increased. This limit also applies to billing accounts, folders, and organizations and isn't hierarchical. To query large volumes of logs, consider using BigQuery APIs. For transferring large volumes of logs, consider using a log sink or [copying log entries](https://docs.cloud.google.com/logging/docs/routing/copy-logs).  
Number of different resource names in a single `entries.write` command | 1000 | Cannot be increased. The `logName` field of a log entry specifies the log entry's resource name.  
Control requests per minute | 600 | Cannot be increased. This quota applies to all requests included in the daily control-request quota, plus API requests for deleting logs and managing log-based metrics.  
Control requests per day | 1,000 per Google Cloud project | Cannot be increased. This quota applies to API requests for creating and updating exclusions and sinks.  
Number of Google Cloud projects or other resource names in a  
single `entries.list` request | 100 | Cannot be increased.  
Number of concurrent copy operations | 1 per Google Cloud project | Cannot be increased. This limit also applies to billing accounts, folders, and organizations and isn't hierarchical.  
Rate of exports to Pub/Sub topics | 60 GB/min per Google Cloud project, folder, or organization where the sink is defined | You can file a support request to raise your quota. An increased quota is granted based on Pub/Sub availability. If the rate of exports exceeds the quota, then the error is recorded in a log entry. The summary field indicates a sink configuration error, and the error code is listed as `topic_over_quota`. For troubleshooting information, see [Quota issues with sinks](https://docs.cloud.google.com/logging/docs/export/troubleshoot#quota-issues).  
  
### Per-region ingestion quotas

To improve isolation and protect regional resources from ingestion overload, Cloud Logging quotas restrict the volume of data written to an ingestion region on a per-Google Cloud project basis.

The following table shows the default quota for each region:

Ingestion region | Default value  
---|---  
`asia-east1`, `asia-northeast1`, `asia-southeast1`, `asia-south1`, `europe-west1`, `europe-west2`, `europe-west3`, `europe-west4`, `us-central1`, `us-east4`, `us-west1` | 4.8 GB per minute, per Google Cloud project  
All remaining regions | 300 MB per minute, per Google Cloud project  
  
The default values for the regional quotas exceed the ingestion volumes of most users. However, if your project's ingestion volume from a region was close to or higher than the default quota in the six or more months before quotas were enforced, then your initial quota includes an automatic, one-time increase. Therefore, your quotas might be higher than the defaults in the preceding table. For information about reviewing quotas, see Review your Cloud Logging API quotas.

If you exceed a regional quota, then your write requests to the Cloud Logging API might be rejected with a "resource exhausted" error message. For recommendations to help you avoid exceeding quotas, see Manage and monitor your Logging quotas.

### Review your Cloud Logging API quotas

To review your Cloud Logging API quotas, do the following:

  1. In the Google Cloud console, go to the **Quotas & System Limits** page: 

[Go to **Quotas & System Limits**](https://console.cloud.google.com/iam-admin/quotas)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

  2. Filter the list of quotas for the Cloud Logging API service.



### Request changes to Cloud Logging API quotas

To determine whether you can request a higher or lower Logging API limit for quota by using the Google Cloud console, go to the **Quotas & System Limits** page and search for the quota of interest.

  * If the quota is listed, then you can use that page to request a change to the limit. For information about those steps, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).


  * If the quota isn't listed or if you request a quota update and get the error `Edit is not allowed for this quota`, then [contact Cloud Customer Care](https://cloud.google.com/support) and request a change to the quota. Billing must be enabled on the Google Cloud project to edit quotas in the Google Cloud console.



### Manage and monitor your Cloud Logging API quotas

To prevent service disruptions caused by exceeding quotas, you can do the following:

  * Use automatic quota adjustment to monitor your quota usage and request increases for you. For more information, see [Quota adjuster](https://docs.cloud.google.com/docs/quotas/quota-adjuster).
  * Create alerts on quotas to notify you about usage. For more information, see [Set up quota alerts](https://docs.cloud.google.com/docs/quotas/set-up-quota-alerts).



### Optimize usage of `entries.list`

The expected usage of [`entries.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list) is to search for matching logs. This method isn't intended for high-volume retrieval of log entries. If you're regularly exhausting your `entries.list` quota, then consider the following options:

  * Ensure that you are using the Cloud Logging API effectively. For more information, see [Optimize usage of the API](https://docs.cloud.google.com/logging/docs/reference/api-overview#logging-api-tips).

  * If you know in advance that the log entries you want to analyze exceed the `entries.list` quota, then [configure a log sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) to export your logs to a supported destination.



  * To analyze log entries outside of Logging, you can retroactively [copy log entries](https://docs.cloud.google.com/logging/docs/routing/copy-logs) that already exist in Logging to Cloud Storage buckets. When you copy logs to a Cloud Storage bucket, you can share log entries with auditors outside of Logging and run scripts in Cloud Storage.


  * To aggregate and analyze your log entries within Logging, store your log entries in a log bucket and then upgrade that log bucket to use Observability Analytics. For information about these steps, see [Configure log buckets](https://docs.cloud.google.com/logging/docs/buckets).

Observability Analytics lets you query your log entries by using [BigQuery-standard SQL](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql).




## Log-based metrics

**This entry applies only to metric data that Google Cloud Observability derives from your log data (log-based metrics). This section doesn't apply to metric data that is written by Google Cloud services or your applications.**

The following limits apply to your usage of [user-defined log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics#user-defined_metrics). With the exception of the number of metric descriptors, these limits are fixed; you can't increase or decrease them.

Category | Maximum value  
---|---  
Number of [labels](https://docs.cloud.google.com/logging/docs/logs-based-metrics/labels) | 10 per metric  
Length of [label](https://docs.cloud.google.com/logging/docs/logs-based-metrics/labels) value | 1,024 B  
Length of [label](https://docs.cloud.google.com/logging/docs/logs-based-metrics/labels) description | 800 B  
Length of the filter1 | 20,000 characters  
Length of [metric descriptors](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics) | 8,000 B  
Number of [metric descriptors](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics) | 500 per Google Cloud project2  
Number of active [time series](https://docs.cloud.google.com/monitoring/api/v3/metrics#model-intro-timeseries)3 | 30,000 per metric4  
Number of [histogram buckets](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries#BucketOptions) | 200 per custom [distribution metric](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries#Distribution)  
Data retention | See [Cloud Monitoring: Data retention](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy)  
  
1 Each log-based metric contains a filter. When a log entry matches the filter, the log entry is counted. Filters are defined by using the [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language).  
2 This limit also applies to billing accounts, folders, and organizations and isn't hierarchical.  
3 A [time series](https://docs.cloud.google.com/monitoring/api/v3/metrics#model-intro-timeseries) is active if you have written data points to it within the last 24 hours.  
4 The system limits the number of active time series per monitored resource to 1,000,000. For project-level log-based metrics, the resource is defined by the resource in the log entry. For [bucket-scoped log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/bucket-lbm), the resource is [`logging_bucket`](https://docs.cloud.google.com/monitoring/api/resources#tag_logging_bucket). When that limit is met, the system throttles metric data for the resource. You can reduce the number of time series for a log-based metric by reducing its cardinality. 

## Audit logging

The maximum sizes of [audit logs](https://docs.cloud.google.com/logging/docs/audit) are shown in the following table. These values can help you estimate the space you need in your [sink destinations](https://docs.cloud.google.com/logging/docs/routing/overview#sinks).

Audit log type | Maximum size  
---|---  
[Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) | 512 KiB  
[Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) | 512 KiB  
[System Event](https://docs.cloud.google.com/logging/docs/audit#system-event) | 512 KiB  
[Policy Denied](https://docs.cloud.google.com/logging/docs/audit#policy_denied) | 512 KiB  
  
## Logs retention periods

**Note:** Effective April 1, 2023, retention costs apply to logs data retained longer than the [default retention period](https://docs.cloud.google.com/logging/quotas#logs_retention_periods) of the `_Default` bucket and user-defined log buckets. For pricing details, see the Cloud Logging sections of the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page. To review the billable storage for your log buckets, go to the **Logs Storage** page of the Google Cloud console. 

The following Cloud Logging retention periods apply to [log buckets](https://docs.cloud.google.com/logging/docs/store-log-entries), regardless of which types of logs are included in the bucket or whether they were copied from another location:

Bucket | Resources | Default retention period | Custom retention | `_Required` | project, folder, organization | 400 days | Not configurable  
---|---|---|---  
`_Default` | folder, organization | 30 days | Not configurable  
`_Default` | project | 30 days | Configurable  
User-defined | project | 30 days | Configurable  
  
For `_Default` and user-defined log buckets that are in projects, you can configure Cloud Logging to retain your logs between 1 day and 3650 days. For information about setting retention rules, see [Configure custom retention](https://docs.cloud.google.com/logging/docs/buckets#custom-retention).

To store log entries from a folder or organization for longer than 30 days, create a log sink and route those log entries to a log bucket in a project.

## Pricing

For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page. If you route log data to other Google Cloud services, then see the following documents:

  * [Cloud Storage pricing](https://cloud.google.com/storage/pricing)
  * [BigQuery pricing](https://cloud.google.com/bigquery/pricing#data_ingestion_pricing)
  * [Pub/Sub pricing](https://cloud.google.com/pubsub/pricing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
