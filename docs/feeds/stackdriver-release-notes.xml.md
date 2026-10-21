---
url: https://docs.cloud.google.com/feeds/stackdriver-release-notes.xml
title: Google Cloud Observability - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:25.519681+00:00
---

# Google Cloud Observability - Release notes

> Source: https://docs.cloud.google.com/feeds/stackdriver-release-notes.xml

tag:google.com,2016:stackdriver-release-notesGoogle Cloud Observability - Release notesGoogle Cloud Platform2026-10-06T00:00:00-07:00October 06, 2026tag:google.com,2016:stackdriver-release-notes#October_06_20262026-10-06T00:00:00-07:00Cloud Monitoring 

### Feature

Bulk registration of discovered services and workloads to an App Hub application is [generally available (GA)](https://docs.cloud.google.com/products#product-launch-stages). For more information, see [Register one or more discovered services or workloads](https://docs.cloud.google.com/monitoring/docs/application-monitoring#register).

]]> September 30, 2026tag:google.com,2016:stackdriver-release-notes#September_30_20262026-09-30T00:00:00-07:00Cloud Monitoring 

### Announcement

The [application topology graph](https://docs.cloud.google.com/stackdriver/docs/observability/application-topology) is now [generally available (GA)](https://docs.cloud.google.com/products#product-launch-stages). This graph helps you to understand relationships between applications, services, and workloads, and shows you traffic flow and incidents in the context of your applications.

]]> September 28, 2026tag:google.com,2016:stackdriver-release-notes#September_28_20262026-09-28T00:00:00-07:00Cloud Logging 

### Deprecated

The legacy Logging agent has officially reached its end of support. All standard maintenance and regular bug fixes for the agent have ceased. We recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/logging/docs/agent/index). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents).

### Breaking

Only platform services can write log entries to billing accounts. These logs have names with the format `billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]`. For more information, see [`entries.write`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write).

## Cloud Monitoring

### Deprecated

The legacy Monitoring agent has officially reached its end of support. All standard maintenance and regular bug fixes for the agent have ceased. We recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/monitoring/agent/index). For more information about this deprecation, see [Legacy Monitoring and Logging agent end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents).

]]> September 23, 2026tag:google.com,2016:stackdriver-release-notes#September_23_20262026-09-23T00:00:00-07:00Cloud Trace **v2**

### Feature

The Google Cloud CLI version 586.0.0 includes the following changes:

  * Added `create` and `update` methods to the `gcloud observability buckets` command group.
  * Promoted the `gcloud observability` commands from `BETA` to `GA`.



For more information, see the [`gcloud observability`](https://docs.cloud.google.com/sdk/gcloud/reference/observability) reference pages.

For example usage, see the guides that describe how to configure and manage observability buckets:

  * [Create observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/create-observability-buckets)
  * [Update observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/update-observability-buckets)
  * [List buckets and manage datasets](https://docs.cloud.google.com/stackdriver/docs/observability/storage-manage)

]]> September 22, 2026tag:google.com,2016:stackdriver-release-notes#September_22_20262026-09-22T00:00:00-07:00Cloud Trace **v2**

### Feature

The following remote Google Cloud MCP servers automatically generate a trace span for `tools/call` operations.

  * Identity and Access Management
  * Organization Policy Service
  * Policy Analyzer
  * Security Command Center
  * Spanner
  * Unified Maintenance



These spans can help you understand the behavior of your agentic applications. For more information, see [Investigate MCP calls using Trace](https://docs.cloud.google.com/stackdriver/docs/instrumentation/trace-remote-mcp-server-calls).

### Feature

You can use Terraform to configure resources managed by the Observability API. For example, you can use Terraform to create and update observability buckets, create links on datasets, and configure default settings.

For more information, see the following documents:

  * [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets)
  * [Create observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/create-observability-buckets)
  * [Update observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/update-observability-buckets)
  * [List buckets and manage datasets](https://docs.cloud.google.com/stackdriver/docs/observability/storage-manage)

]]> September 14, 2026tag:google.com,2016:stackdriver-release-notes#September_14_20262026-09-14T00:00:00-07:00Cloud Logging 

### Feature

Starting with version 2.71.0, you can use an Ops Agent configuration option to export your metrics, logs, and traces by using the OpenTelemetry-based [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) rather than by using the Cloud Monitoring API, Logging API, or Trace API. For more information, see [Use the Telemetry API](https://docs.cloud.google.com/monitoring/agent/ops-agent/use-telemetry-api).

## Cloud Monitoring

### Feature

Starting with version 2.71.0, you can use an Ops Agent configuration option to export your metrics, logs, and traces by using the OpenTelemetry-based [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) rather than by using the Cloud Monitoring API, Logging API, or Trace API For more information, see [Use the Telemetry API](https://docs.cloud.google.com/monitoring/agent/ops-agent/use-telemetry-api).

]]> September 09, 2026tag:google.com,2016:stackdriver-release-notes#September_09_20262026-09-09T00:00:00-07:00Cloud Monitoring 

### Feature

A chart on a dashboard can override the dashboard's time-range setting. This feature lets you view trends over a long period or metric data with low sampling rates alongside charts that show only recent data, and is [Generally Available (GA)](https://cloud.google.com/products#product-launch-stages).

For more information, see the following documents:

  * Google Cloud console: [Set a time-range override for a chart or group](https://docs.cloud.google.com/monitoring/charts/chart-view-options#override-dashboard-time-range)
  * API: [Dashboard with an `XyChart` widget that sets a time-range override](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_a_time_range)

]]> September 08, 2026tag:google.com,2016:stackdriver-release-notes#September_08_20262026-09-08T00:00:00-07:00Cloud Trace **v2**

### Feature

The Observability API supports VPC Service Controls. This integration is [generally available](https://cloud.google.com/products#product-launch-stages).

For more information, see the following:

  * [Use VPC Service Controls with Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs/observability/use-vpc-service-controls)
  * [Observability API overview](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview)
  * [Supported products: Observability API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_observability_api)

]]> September 01, 2026tag:google.com,2016:stackdriver-release-notes#September_01_20262026-09-01T00:00:00-07:00Cloud Monitoring 

### Feature

You can opt out of alert notifications from an SMS notification channel by sending a text message to the phone number associated with the notification channel. For more information, see [Opt out of SMS notifications](https://docs.cloud.google.com/feeds/monitoring/alerts/sms-opt-out).

]]> August 31, 2026tag:google.com,2016:stackdriver-release-notes#August_31_20262026-08-31T00:00:00-07:00Cloud Trace **v2**

### Breaking

Starting August 31, 2026, you can no longer create or edit [trace sinks](https://docs.cloud.google.com/trace/docs/trace-export-overview). Trace sinks were deprecated on February 18, 2026. For more information, see [Export trace spans with sinks deprecation](https://docs.cloud.google.com/stackdriver/docs/deprecations/export-spans-with-sinks).

For information about how to analyze your trace data using SQL, see the following documents:

  * [Query and analyze traces using Observability Analytics](https://docs.cloud.google.com/trace/docs/analytics)
  * [Query a linked BigQuery dataset](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset)

]]> August 27, 2026tag:google.com,2016:stackdriver-release-notes#August_27_20262026-08-27T00:00:00-07:00Cloud Trace **v2**

### Feature

The following remote MCP server automatically generates a trace span for `tools/call` operations.

  * Datastream



These spans can help you understand the behavior of your agentic applications. For more information, see [Investigate MCP calls using Trace](https://docs.cloud.google.com/trace/docs/trace-remote-mcp-server-calls).

]]> August 26, 2026tag:google.com,2016:stackdriver-release-notes#August_26_20262026-08-26T00:00:00-07:00Cloud Logging 

### Change

VM Extension Manager extension policies for the Ops Agent are [Generally Available (GA)](https://docs.cloud.google.com/products#product-launch-stages). Extension policies provide zonal and project-wide Ops Agent installation, version upgrades, and configuration management. For more information, see [Install and manage the Ops Agent by using VM Extension Manager policies](https://docs.cloud.google.com/logging/docs/agent/ops-agent/agent-vmem-policies).

## Cloud Monitoring

### Change

VM Extension Manager extension policies for the Ops Agent are [Generally Available (GA)](https://docs.cloud.google.com/products#product-launch-stages). Extension policies provide zonal and project-wide Ops Agent installation, version upgrades, and configuration management. For more information, see [Install and manage the Ops Agent by using VM Extension Manager policies](https://docs.cloud.google.com/monitoring/agent/ops-agent/agent-vmem-policies).

]]> August 24, 2026tag:google.com,2016:stackdriver-release-notes#August_24_20262026-08-24T00:00:00-07:00Cloud Trace **v2**

### Feature

You can update the display name, description, and Cloud KMS key applied to a `_Trace` observability bucket.

For more information, see [Update observability buckets](https://docs.cloud.google.com/trace/docs/update-observability-buckets).

### Feature

You can manually create the `_Trace` observability bucket before your project receives trace data. When creating the bucket, you must specify a storage location. Google Cloud Observability applies the Cloud KMS key defined in your default settings unless you explicitly specify a different key in your create request.

For more information, see the following documents:

  * [Create observability buckets](https://docs.cloud.google.com/trace/docs/create-observability-buckets)
  * [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets)



### Feature

The following remote MCP servers automatically generate a trace span for `tools/call` operations.

  * Policy Troubleshooter
  * Managed Service for Apache Airflow



These spans can help you understand the behavior of your agentic applications. For more information, see [Investigate MCP calls using Trace](https://docs.cloud.google.com/trace/docs/trace-remote-mcp-server-calls).

]]> August 17, 2026tag:google.com,2016:stackdriver-release-notes#August_17_20262026-08-17T00:00:00-07:00Cloud Trace **v2**

### Feature

The following limits associated with the Cloud Trace API, `cloudtrace.googleapis.com`, have increased:

  * Maximum attributes per span: 1,024
  * Maximum attribute value size: 65,532 bytes
  * Maximum attribute key size: 512 bytes
  * Maximum span name length: 1,024 bytes
  * Maximum events per span: 256



The new limits are consistent with those supported by the Telemetry API, which implements the [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp).

For more information, see [Cloud Trace API quotas and limits](https://docs.cloud.google.com/trace/docs/quotas#trace-api-quotas-and-limits).

]]> August 14, 2026tag:google.com,2016:stackdriver-release-notes#August_14_20262026-08-14T00:00:00-07:00Cloud Logging 

### Announcement

The Telemetry API for logs ingestion is [generally available (GA)](https://docs.cloud.google.com/products#product-launch-stages). You can ingest OTLP logs into Cloud Logging by using an OpenTelemetry Collector, an OTLP exporter, and the Telemetry API. For more information, see [OTLP ingestion overview](https://docs.cloud.google.com/stackdriver/docs/otlp/overview).

]]> August 13, 2026tag:google.com,2016:stackdriver-release-notes#August_13_20262026-08-13T00:00:00-07:00Error Reporting 

### Announcement

Error Reporting can report stack traces collected from Rust applications using [`std::backtrace`](https://doc.rust-lang.org/std/backtrace/index.html). To enable, set the `RUST_BACKTRACE=1` environment variable and make sure debug symbols are enabled.

For more information, see [ReportedErrorEvent](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report.html?rep_location=global#reportederrorevent).

]]> August 12, 2026tag:google.com,2016:stackdriver-release-notes#August_12_20262026-08-12T00:00:00-07:00Cloud Trace **v2**

### Feature

The following remote MCP servers automatically generate a trace span for `tools/call` operations. These spans can help you understand the behavior of your agentic applications. For more information, see [Investigate MCP calls using Trace](https://docs.cloud.google.com/stackdriver/docs/instrumentation/trace-remote-mcp-server-calls).

  * Cloud Billing
  * Personalized Service Health



### Feature

Google Cloud Observability automatically generates trace exemplars for charts on custom dashboards that display the result of a SQL query when the query runs against your trace data and satisfies some constraints. The exemplars link the SQL query result to specific traces. This feature is in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

For more information, see [Generate and display trace exemplars](https://docs.cloud.google.com/trace/docs/analytics-chart#show-trace-exemplars).

]]> August 05, 2026tag:google.com,2016:stackdriver-release-notes#August_05_20262026-08-05T00:00:00-07:00Cloud Monitoring 

### Announcement

The Telemetry API for metric ingestion is [generally available (GA)](https://docs.cloud.google.com/products#product-launch-stages). You can ingest OTLP metrics into Cloud Monitoring by using an OpenTelemetry Collector, an OTLP exporter, and the Telemetry API. For more information, see [OTLP metric ingestion overview](https://docs.cloud.google.com/stackdriver/docs/otlp-metrics/overview).

]]> June 29, 2026tag:google.com,2016:stackdriver-release-notes#June_29_20262026-06-29T00:00:00-07:00Cloud Monitoring 

### Feature

Alerting policies based on PromQL queries can now operate over more than 25 hours of data. For more information, see [Query over 2 years of metric data](https://docs.cloud.google.com/monitoring/alerts/using-promql#promql-2years) and [Limits for alerting](https://docs.cloud.google.com/monitoring/quotas#alerting_uptime_limits).

## Cloud Trace

**v2**

### Feature

Google Cloud Observability has expanded the supported locations for observability buckets, which store your trace data, to include the following:

  * europe-west9



For a list of supported locations, see [Locations for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).

]]> June 25, 2026tag:google.com,2016:stackdriver-release-notes#June_25_20262026-06-25T00:00:00-07:00Cloud Monitoring 

### Feature

Support for applying role-based access controls (RBAC) to Cloud Monitoring dashboards and alerting policies using Tags is [generally available](https://docs.cloud.google.com/products#product-launch-stages).

You can use Tags to protect Terraform-managed Cloud Monitoring resources and configure team-scoped access. For more information, see [Use Tags to control access to resources](https://docs.cloud.google.com/monitoring/docs/access-control-with-tags).

]]> June 22, 2026tag:google.com,2016:stackdriver-release-notes#June_22_20262026-06-22T00:00:00-07:00Cloud Logging 

### Security

If the parent project for a Cloud Storage bucket changes, a log sink stops routing log entries to that bucket. For more information about error messages and recovery options, see [Errors routing to Cloud Storage](https://docs.cloud.google.com/logging/docs/export/troubleshoot#errors_exporting_to_cloud_storage).

## Cloud Monitoring

### Feature

Metrics Explorer can automatically break down a chart into a series of tiles, with each displaying time-series data for a specific label key. This view helps you identify spikes, dips, or trends that the aggregation settings might otherwise hide.

To learn more, see [Break down a chart by labels](https://docs.cloud.google.com/monitoring/charts/breakdown-chart-by-labels).

]]> June 18, 2026tag:google.com,2016:stackdriver-release-notes#June_18_20262026-06-18T00:00:00-07:00Cloud Logging 

### Change

The Cloud Logging API adds support for the `ca` regional endpoint. For a complete list of regional endpoints, see the [REST reference pages](https://docs.cloud.google.com/logging/docs/reference/v2/rest?rep_location=global).

## Cloud Trace

**v2**

### Feature

You can collect, view, and analyze multimodal prompts and responses from your agentic applications that use the LangGraph or Agent Development Kit (ADK) frameworks. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

  * [Instrument generative AI applications](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-overview)
  * [Collect and view multimodal prompts and responses](https://docs.cloud.google.com/trace/docs/collect-view-multimodal-prompts-responses)

]]> June 12, 2026tag:google.com,2016:stackdriver-release-notes#June_12_20262026-06-12T00:00:00-07:00Cloud Monitoring 

### Change

All `agent.googleapis.com/processes` metrics are retained for 24 months. For more information, see [Data retention](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy).

]]> June 08, 2026tag:google.com,2016:stackdriver-release-notes#June_08_20262026-06-08T00:00:00-07:00Cloud Trace **v2**

### Feature

The Trace API supports regional endpoints. For a list of supported endpoints, see the REST API reference pages:

  * [v1 REST reference](https://docs.cloud.google.com/trace/docs/reference/v1/rest?rep_location=global)
  * [v2 REST reference](https://docs.cloud.google.com/trace/docs/reference/v2/rest?rep_location=global)

]]> June 05, 2026tag:google.com,2016:stackdriver-release-notes#June_05_20262026-06-05T00:00:00-07:00Cloud Monitoring 

### Feature

Custom dashboards can display trace data. You can view individual spans or aggregated data. This feature is [public preview](https://docs.cloud.google.com/products#product-launch-stages). For more information, see the following:

  * [Display trace data (Google Cloud console)](https://docs.cloud.google.com/monitoring/dashboards/display-traces-on-dashboards)
  * [Dashboard with trace data (API)](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard-with-trace-data)



## Cloud Trace

**v2**

### Feature

Custom dashboards can display trace data. You can view individual spans or aggregated data. This feature is [public preview](https://docs.cloud.google.com/products#product-launch-stages). For more information, see [Display traces on a custom dashboard](https://docs.cloud.google.com/trace/docs/display-traces-on-dashboards).

]]> June 04, 2026tag:google.com,2016:stackdriver-release-notes#June_04_20262026-06-04T00:00:00-07:00Cloud Trace **v2**

### Feature

To view the instrumentation scope or the schema associated with a span, open the **Details** view for the span and select the **Metadata & Links** tab. For more information, see [View attributes, log entries, and events](https://docs.cloud.google.com/trace/docs/finding-traces#attributes-events).

]]> June 02, 2026tag:google.com,2016:stackdriver-release-notes#June_02_20262026-06-02T00:00:00-07:00Cloud Monitoring 

### Feature

Support for **Histogram** widgets on custom dashboards is [generally available](https://docs.cloud.google.com/products#product-launch-stages). These widgets extract the most recent value from each time series, group those values into ranges, and then provide a graphical representation of the result. Unlike tables or other widgets that display the most recent values, **Histograms** display information about the relative frequency of ranges of values.

This widget is one of several visualizations that you can use to display the most recent values. For more information, see the following documents:

  * [Configure a histogram (Google Cloud console)](https://docs.cloud.google.com/monitoring/charts#add_histogram)
  * [Dashboard with an XyChart configured as a histogram (API)](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_a_histogram_widget)



## Cloud Trace

**v2**

### Feature

The create-observability bucket flow enforces organization policies with constraints on resource locations. This flow also enforces policies that require customer-managed encryption keys (CMEKs) and that restrict the projects that store those keys. Your trace data is stored in an observability bucket.

For more information, see the following:

  * [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets)
  * [Support for CMEKs](https://docs.cloud.google.com/stackdriver/docs/observability/cmek)

]]> June 01, 2026tag:google.com,2016:stackdriver-release-notes#June_01_20262026-06-01T00:00:00-07:00Cloud Monitoring 

### Feature

The details page for a span can display the call hierarchy of a trace by using a directed acyclic graph (DAG). If you view an Application Monitoring dashboard and explore the trace data that it displays, the flyout supports the DAG option. If you open the **Trace Explorer** page and explore a span, the DAG option is also available.

For more information, see the following:

  * [Application Monitoring: Explore a trace](https://docs.cloud.google.com/monitoring/docs/application-monitoring#explore-trace)
  * [Trace Explorer: Explore a trace](https://docs.cloud.google.com/trace/docs/finding-traces#explore)



## Cloud Trace

**v2**

### Feature

The details page for a span can display the call hierarchy of a trace using a directed acyclic graph (DAG). One way to view a span's details is to open the **Trace Explorer** page and select the span. The DAG view is also available for some integrations. For example, if you view an Application Monitoring dashboard and explore the trace data it displays, the flyout supports the DAG option.

For more information, see the following:

  * [Trace Explorer: Explore a trace](https://docs.cloud.google.com/trace/docs/finding-traces#explore)
  * [Application Monitoring: Explore a trace](https://docs.cloud.google.com/monitoring/docs/application-monitoring#explore-trace)

]]> May 28, 2026tag:google.com,2016:stackdriver-release-notes#May_28_20262026-05-28T00:00:00-07:00Cloud Logging 

### Announcement

You can view the available regional endpoints for the Cloud Logging API on the REST reference pages. For an example, see [Method: projects.locations.buckets.list](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/list?rep_location=global).

## Cloud Trace

**v2**

### Announcement

You can view the available regional endpoints for the Observability API and for the Telemetry API on their REST reference pages. For more information, see [API overview](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview).

## Error Reporting

### Announcement

You can view the available regional endpoints for the Error Reporting API on the REST reference pages. For an example, see [Method: projects.events.list](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/list?rep_location=global).

]]> May 26, 2026tag:google.com,2016:stackdriver-release-notes#May_26_20262026-05-26T00:00:00-07:00Cloud Trace **v2**

### Announcement

Cloud Trace in Observability Analytics is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Observability Analytics lets you query and analyze your trace data by using SQL. You can chart your query results, save your queries, and join your trace and log data.

For more information, see the following documents:

  * [Query and analyze telemetry with Observability Analytics](https://docs.cloud.google.com/stackdriver/docs/observability/analytics).
  * [Chart SQL query results](https://docs.cloud.google.com/stackdriver/docs/observability/analytics-chart)
  * [Sample SQL queries](https://docs.cloud.google.com/stackdriver/docs/observability/analytics-samples)
  * [Analyze trace data with BigQuery](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset).



### Announcement

The Observability API is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). This API lets you configure the following:

  * The default storage location and the default encryption key for your trace data.
  * The observability scope.
  * A linked BigQuery dataset, which lets your use BigQuery services to analyze your trace data.



For more information, see the following documents:

  * [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets)
  * [Configure observability scopes for multi-project queries](https://docs.cloud.google.com/stackdriver/docs/observability/scopes)
  * [Manage observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/storage-manage)
  * [API overview](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview)



### Announcement

Trace scopes are generally available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Create and manage trace scopes](https://docs.cloud.google.com/trace/docs/trace-scope/create-and-manage).

### Feature

The following remote MCP servers automatically generate a trace span for `tools/call` operations. These spans can help you understand the behavior of your agentic applications. For more information, see [Investigate MCP calls using Trace](https://docs.cloud.google.com/stackdriver/docs/instrumentation/trace-remote-mcp-server-calls).

  * BigQuery
  * Cloud SQL

]]>
