---
url: https://docs.cloud.google.com/stackdriver/docs/release-notes/
title: Google Cloud Observability release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:56:00.357504+00:00
---

# Google Cloud Observability release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Resources ](https://docs.cloud.google.com/stackdriver/quotas)



Send feedback 

#  Google Cloud Observability release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a consolidated list of the release notes for all of the products in Google Cloud Observability. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality.

You can find the release notes for the individual products on the following pages:

  * [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/release-notes)
  * [Cloud Logging](https://docs.cloud.google.com/logging/docs/release-notes)
  * [Error Reporting](https://docs.cloud.google.com/error-reporting/docs/release-notes)
  * [Cloud Profiler](https://docs.cloud.google.com/profiler/docs/release-notes)
  * [Cloud Trace](https://docs.cloud.google.com/trace/docs/release-notes)



You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/stackdriver-release-notes.xml) directly. 

## October 06, 2026

**Cloud Monitoring**

v3

Feature

Bulk registration of discovered services and workloads to an App Hub application is [generally available (GA)](https://docs.cloud.google.com/products#product-launch-stages). For more information, see [Register one or more discovered services or workloads](https://docs.cloud.google.com/monitoring/docs/application-monitoring#register).

## September 30, 2026

**Cloud Monitoring**

v3

Announcement

The [application topology graph](https://docs.cloud.google.com/stackdriver/docs/observability/application-topology) is now [generally available (GA)](https://docs.cloud.google.com/products#product-launch-stages). This graph helps you to understand relationships between applications, services, and workloads, and shows you traffic flow and incidents in the context of your applications.

## September 28, 2026

**Cloud Logging**

v2

Deprecated

The legacy Logging agent has officially reached its end of support. All standard maintenance and regular bug fixes for the agent have ceased. We recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/logging/docs/agent). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents).

Breaking

Only platform services can write log entries to billing accounts. These logs have names with the format `billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]`. For more information, see [`entries.write`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write).

**Cloud Monitoring**

v3

Deprecated

The legacy Monitoring agent has officially reached its end of support. All standard maintenance and regular bug fixes for the agent have ceased. We recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/monitoring/agent). For more information about this deprecation, see [Legacy Monitoring and Logging agent end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents).

## September 23, 2026

**Cloud Trace**

v2

Feature

The Google Cloud CLI version 586.0.0 includes the following changes:

  * Added `create` and `update` methods to the `gcloud observability buckets` command group.
  * Promoted the `gcloud observability` commands from `BETA` to `GA`.



For more information, see the [`gcloud observability`](https://docs.cloud.google.com/sdk/gcloud/reference/observability) reference pages.

For example usage, see the guides that describe how to configure and manage observability buckets:

  * [Create observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/create-observability-buckets)
  * [Update observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/update-observability-buckets)
  * [List buckets and manage datasets](https://docs.cloud.google.com/stackdriver/docs/observability/storage-manage)



## September 22, 2026

**Cloud Trace**

v2

Feature

The following remote Google Cloud MCP servers automatically generate a trace span for `tools/call` operations.

  * Identity and Access Management
  * Organization Policy Service
  * Policy Analyzer
  * Security Command Center
  * Spanner
  * Unified Maintenance



These spans can help you understand the behavior of your agentic applications. For more information, see [Investigate MCP calls using Trace](https://docs.cloud.google.com/stackdriver/docs/instrumentation/trace-remote-mcp-server-calls).

Feature

You can use Terraform to configure resources managed by the Observability API. For example, you can use Terraform to create and update observability buckets, create links on datasets, and configure default settings.

For more information, see the following documents:

  * [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets)
  * [Create observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/create-observability-buckets)
  * [Update observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/update-observability-buckets)
  * [List buckets and manage datasets](https://docs.cloud.google.com/stackdriver/docs/observability/storage-manage)



## September 14, 2026

**Cloud Logging**

v2

Feature

Starting with version 2.71.0, you can use an Ops Agent configuration option to export your metrics, logs, and traces by using the OpenTelemetry-based [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) rather than by using the Cloud Monitoring API, Logging API, or Trace API. For more information, see [Use the Telemetry API](https://docs.cloud.google.com/monitoring/agent/ops-agent/use-telemetry-api).

**Cloud Monitoring**

v3

Feature

Starting with version 2.71.0, you can use an Ops Agent configuration option to export your metrics, logs, and traces by using the OpenTelemetry-based [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) rather than by using the Cloud Monitoring API, Logging API, or Trace API For more information, see [Use the Telemetry API](https://docs.cloud.google.com/monitoring/agent/ops-agent/use-telemetry-api).

## September 09, 2026

**Cloud Monitoring**

v3

Feature

A chart on a dashboard can override the dashboard's time-range setting. This feature lets you view trends over a long period or metric data with low sampling rates alongside charts that show only recent data, and is [Generally Available (GA)](https://cloud.google.com/products#product-launch-stages).

For more information, see the following documents:

  * Google Cloud console: [Set a time-range override for a chart or group](https://docs.cloud.google.com/monitoring/charts/chart-view-options#override-dashboard-time-range)
  * API: [Dashboard with an `XyChart` widget that sets a time-range override](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_a_time_range)



## September 08, 2026

**Cloud Trace**

v2

Feature

The Observability API supports VPC Service Controls. This integration is [generally available](https://cloud.google.com/products#product-launch-stages).

For more information, see the following:

  * [Use VPC Service Controls with Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs/observability/use-vpc-service-controls)
  * [Observability API overview](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview)
  * [Supported products: Observability API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_observability_api)



## September 01, 2026

**Cloud Monitoring**

v3

Feature

You can opt out of alert notifications from an SMS notification channel by sending a text message to the phone number associated with the notification channel. For more information, see [Opt out of SMS notifications](https://docs.cloud.google.com/release-notes/monitoring/alerts/sms-opt-out).

## August 31, 2026

**Cloud Trace**

v2

Breaking

Starting August 31, 2026, you can no longer create or edit [trace sinks](https://docs.cloud.google.com/trace/docs/trace-export-overview). Trace sinks were deprecated on February 18, 2026. For more information, see [Export trace spans with sinks deprecation](https://docs.cloud.google.com/stackdriver/docs/deprecations/export-spans-with-sinks).

For information about how to analyze your trace data using SQL, see the following documents:

  * [Query and analyze traces using Observability Analytics](https://docs.cloud.google.com/trace/docs/analytics)
  * [Query a linked BigQuery dataset](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset)



## August 27, 2026

**Cloud Trace**

v2

Feature

The following remote MCP server automatically generates a trace span for `tools/call` operations.

  * Datastream



These spans can help you understand the behavior of your agentic applications. For more information, see [Investigate MCP calls using Trace](https://docs.cloud.google.com/trace/docs/trace-remote-mcp-server-calls).

## August 26, 2026

**Cloud Logging**

v2

Change

VM Extension Manager extension policies for the Ops Agent are [Generally Available (GA)](https://docs.cloud.google.com/products#product-launch-stages). Extension policies provide zonal and project-wide Ops Agent installation, version upgrades, and configuration management. For more information, see [Install and manage the Ops Agent by using VM Extension Manager policies](https://docs.cloud.google.com/logging/docs/agent/ops-agent/agent-vmem-policies).

**Cloud Monitoring**

v3

Change

VM Extension Manager extension policies for the Ops Agent are [Generally Available (GA)](https://docs.cloud.google.com/products#product-launch-stages). Extension policies provide zonal and project-wide Ops Agent installation, version upgrades, and configuration management. For more information, see [Install and manage the Ops Agent by using VM Extension Manager policies](https://docs.cloud.google.com/monitoring/agent/ops-agent/agent-vmem-policies).

## August 24, 2026

**Cloud Trace**

v2

Feature

You can update the display name, description, and Cloud KMS key applied to a `_Trace` observability bucket.

For more information, see [Update observability buckets](https://docs.cloud.google.com/trace/docs/update-observability-buckets).

Feature

You can manually create the `_Trace` observability bucket before your project receives trace data. When creating the bucket, you must specify a storage location. Google Cloud Observability applies the Cloud KMS key defined in your default settings unless you explicitly specify a different key in your create request.

For more information, see the following documents:

  * [Create observability buckets](https://docs.cloud.google.com/trace/docs/create-observability-buckets)
  * [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets)



Feature

The following remote MCP servers automatically generate a trace span for `tools/call` operations.

  * Policy Troubleshooter
  * Managed Service for Apache Airflow



These spans can help you understand the behavior of your agentic applications. For more information, see [Investigate MCP calls using Trace](https://docs.cloud.google.com/trace/docs/trace-remote-mcp-server-calls).

## August 17, 2026

**Cloud Trace**

v2

Feature

The following limits associated with the Cloud Trace API, `cloudtrace.googleapis.com`, have increased:

  * Maximum attributes per span: 1,024
  * Maximum attribute value size: 65,532 bytes
  * Maximum attribute key size: 512 bytes
  * Maximum span name length: 1,024 bytes
  * Maximum events per span: 256



The new limits are consistent with those supported by the Telemetry API, which implements the [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp).

For more information, see [Cloud Trace API quotas and limits](https://docs.cloud.google.com/trace/docs/quotas#trace-api-quotas-and-limits).

## August 14, 2026

**Cloud Logging**

v2

Announcement

The Telemetry API for logs ingestion is [generally available (GA)](https://docs.cloud.google.com/products#product-launch-stages). You can ingest OTLP logs into Cloud Logging by using an OpenTelemetry Collector, an OTLP exporter, and the Telemetry API. For more information, see [OTLP ingestion overview](https://docs.cloud.google.com/stackdriver/docs/otlp/overview).

## August 13, 2026

**Error Reporting**

v1beta1

Announcement

Error Reporting can report stack traces collected from Rust applications using [`std::backtrace`](https://doc.rust-lang.org/std/backtrace/index.html). To enable, set the `RUST_BACKTRACE=1` environment variable and make sure debug symbols are enabled.

For more information, see [ReportedErrorEvent](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report.html?rep_location=global#reportederrorevent).

## August 12, 2026

**Cloud Trace**

v2

Feature

The following remote MCP servers automatically generate a trace span for `tools/call` operations. These spans can help you understand the behavior of your agentic applications. For more information, see [Investigate MCP calls using Trace](https://docs.cloud.google.com/stackdriver/docs/instrumentation/trace-remote-mcp-server-calls).

  * Cloud Billing
  * Personalized Service Health



Feature

Google Cloud Observability automatically generates trace exemplars for charts on custom dashboards that display the result of a SQL query when the query runs against your trace data and satisfies some constraints. The exemplars link the SQL query result to specific traces. This feature is in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

For more information, see [Generate and display trace exemplars](https://docs.cloud.google.com/trace/docs/analytics-chart#show-trace-exemplars).

## August 05, 2026

**Cloud Monitoring**

v3

Announcement

The Telemetry API for metric ingestion is [generally available (GA)](https://docs.cloud.google.com/products#product-launch-stages). You can ingest OTLP metrics into Cloud Monitoring by using an OpenTelemetry Collector, an OTLP exporter, and the Telemetry API. For more information, see [OTLP metric ingestion overview](https://docs.cloud.google.com/stackdriver/docs/otlp-metrics/overview).

## June 29, 2026

**Cloud Monitoring**

v3

Feature

Alerting policies based on PromQL queries can now operate over more than 25 hours of data. For more information, see [Query over 2 years of metric data](https://docs.cloud.google.com/monitoring/alerts/using-promql#promql-2years) and [Limits for alerting](https://docs.cloud.google.com/monitoring/quotas#alerting_uptime_limits).

**Cloud Trace**

v2

Feature

Google Cloud Observability has expanded the supported locations for observability buckets, which store your trace data, to include the following:

  * europe-west9



For a list of supported locations, see [Locations for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).

## June 25, 2026

**Cloud Monitoring**

v3

Feature

Support for applying role-based access controls (RBAC) to Cloud Monitoring dashboards and alerting policies using Tags is [generally available](https://docs.cloud.google.com/products#product-launch-stages).

You can use Tags to protect Terraform-managed Cloud Monitoring resources and configure team-scoped access. For more information, see [Use Tags to control access to resources](https://docs.cloud.google.com/monitoring/docs/access-control-with-tags).

## June 22, 2026

**Cloud Logging**

v2

Security

If the parent project for a Cloud Storage bucket changes, a log sink stops routing log entries to that bucket. For more information about error messages and recovery options, see [Errors routing to Cloud Storage](https://docs.cloud.google.com/logging/docs/export/troubleshoot#errors_exporting_to_cloud_storage).

**Cloud Monitoring**

v3

Feature

Metrics Explorer can automatically break down a chart into a series of tiles, with each displaying time-series data for a specific label key. This view helps you identify spikes, dips, or trends that the aggregation settings might otherwise hide.

To learn more, see [Break down a chart by labels](https://docs.cloud.google.com/monitoring/charts/breakdown-chart-by-labels).

## June 18, 2026

**Cloud Logging**

v2

Change

The Cloud Logging API adds support for the `ca` regional endpoint. For a complete list of regional endpoints, see the [REST reference pages](https://docs.cloud.google.com/logging/docs/reference/v2/rest?rep_location=global).

**Cloud Trace**

v2

Feature

You can collect, view, and analyze multimodal prompts and responses from your agentic applications that use the LangGraph or Agent Development Kit (ADK) frameworks. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

  * [Instrument generative AI applications](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-overview)
  * [Collect and view multimodal prompts and responses](https://docs.cloud.google.com/trace/docs/collect-view-multimodal-prompts-responses)



## June 12, 2026

**Cloud Monitoring**

v3

Change

All `agent.googleapis.com/processes` metrics are retained for 24 months. For more information, see [Data retention](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy).

## June 08, 2026

**Cloud Trace**

v2

Feature

The Trace API supports regional endpoints. For a list of supported endpoints, see the REST API reference pages:

  * [v1 REST reference](https://docs.cloud.google.com/trace/docs/reference/v1/rest?rep_location=global)
  * [v2 REST reference](https://docs.cloud.google.com/trace/docs/reference/v2/rest?rep_location=global)



## June 05, 2026

**Cloud Monitoring**

v3

Feature

Custom dashboards can display trace data. You can view individual spans or aggregated data. This feature is [public preview](https://docs.cloud.google.com/products#product-launch-stages). For more information, see the following:

  * [Display trace data (Google Cloud console)](https://docs.cloud.google.com/monitoring/dashboards/display-traces-on-dashboards)
  * [Dashboard with trace data (API)](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard-with-trace-data)



**Cloud Trace**

v2

Feature

Custom dashboards can display trace data. You can view individual spans or aggregated data. This feature is [public preview](https://docs.cloud.google.com/products#product-launch-stages). For more information, see [Display traces on a custom dashboard](https://docs.cloud.google.com/trace/docs/display-traces-on-dashboards).

## June 04, 2026

**Cloud Trace**

v2

Feature

To view the instrumentation scope or the schema associated with a span, open the **Details** view for the span and select the **Metadata & Links** tab. For more information, see [View attributes, log entries, and events](https://docs.cloud.google.com/trace/docs/finding-traces#attributes-events).

## June 02, 2026

**Cloud Monitoring**

v3

Feature

Support for **Histogram** widgets on custom dashboards is [generally available](https://docs.cloud.google.com/products#product-launch-stages). These widgets extract the most recent value from each time series, group those values into ranges, and then provide a graphical representation of the result. Unlike tables or other widgets that display the most recent values, **Histograms** display information about the relative frequency of ranges of values.

This widget is one of several visualizations that you can use to display the most recent values. For more information, see the following documents:

  * [Configure a histogram (Google Cloud console)](https://docs.cloud.google.com/monitoring/charts#add_histogram)
  * [Dashboard with an XyChart configured as a histogram (API)](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_a_histogram_widget)



**Cloud Trace**

v2

Feature

The create-observability bucket flow enforces organization policies with constraints on resource locations. This flow also enforces policies that require customer-managed encryption keys (CMEKs) and that restrict the projects that store those keys. Your trace data is stored in an observability bucket.

For more information, see the following:

  * [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets)
  * [Support for CMEKs](https://docs.cloud.google.com/stackdriver/docs/observability/cmek)



## June 01, 2026

**Cloud Monitoring**

v3

Feature

The details page for a span can display the call hierarchy of a trace by using a directed acyclic graph (DAG). If you view an Application Monitoring dashboard and explore the trace data that it displays, the flyout supports the DAG option. If you open the **Trace Explorer** page and explore a span, the DAG option is also available.

For more information, see the following:

  * [Application Monitoring: Explore a trace](https://docs.cloud.google.com/monitoring/docs/application-monitoring#explore-trace)
  * [Trace Explorer: Explore a trace](https://docs.cloud.google.com/trace/docs/finding-traces#explore)



**Cloud Trace**

v2

Feature

The details page for a span can display the call hierarchy of a trace using a directed acyclic graph (DAG). One way to view a span's details is to open the **Trace Explorer** page and select the span. The DAG view is also available for some integrations. For example, if you view an Application Monitoring dashboard and explore the trace data it displays, the flyout supports the DAG option.

For more information, see the following:

  * [Trace Explorer: Explore a trace](https://docs.cloud.google.com/trace/docs/finding-traces#explore)
  * [Application Monitoring: Explore a trace](https://docs.cloud.google.com/monitoring/docs/application-monitoring#explore-trace)



## May 28, 2026

**Cloud Logging**

v2

Announcement

You can view the available regional endpoints for the Cloud Logging API on the REST reference pages. For an example, see [Method: projects.locations.buckets.list](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets/list?rep_location=global).

**Cloud Trace**

v2

Announcement

You can view the available regional endpoints for the Observability API and for the Telemetry API on their REST reference pages. For more information, see [API overview](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview).

**Error Reporting**

v1beta1

Announcement

You can view the available regional endpoints for the Error Reporting API on the REST reference pages. For an example, see [Method: projects.events.list](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/list?rep_location=global).

## May 26, 2026

**Cloud Trace**

v2

Announcement

Cloud Trace in Observability Analytics is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Observability Analytics lets you query and analyze your trace data by using SQL. You can chart your query results, save your queries, and join your trace and log data.

For more information, see the following documents:

  * [Query and analyze telemetry with Observability Analytics](https://docs.cloud.google.com/stackdriver/docs/observability/analytics).
  * [Chart SQL query results](https://docs.cloud.google.com/stackdriver/docs/observability/analytics-chart)
  * [Sample SQL queries](https://docs.cloud.google.com/stackdriver/docs/observability/analytics-samples)
  * [Analyze trace data with BigQuery](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset).



Announcement

The Observability API is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). This API lets you configure the following:

  * The default storage location and the default encryption key for your trace data.
  * The observability scope.
  * A linked BigQuery dataset, which lets your use BigQuery services to analyze your trace data.



For more information, see the following documents:

  * [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets)
  * [Configure observability scopes for multi-project queries](https://docs.cloud.google.com/stackdriver/docs/observability/scopes)
  * [Manage observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/storage-manage)
  * [API overview](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview)



Announcement

Trace scopes are generally available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Create and manage trace scopes](https://docs.cloud.google.com/trace/docs/trace-scope/create-and-manage).

Feature

The following remote MCP servers automatically generate a trace span for `tools/call` operations. These spans can help you understand the behavior of your agentic applications. For more information, see [Investigate MCP calls using Trace](https://docs.cloud.google.com/stackdriver/docs/instrumentation/trace-remote-mcp-server-calls).

  * BigQuery
  * Cloud SQL



## May 15, 2026

**Cloud Logging**

v2

Feature

Starting with version 2.66.0, the Ops Agent can export your logs and metrics by using the OpenTelemetry-based [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) rather than by using the Cloud Logging API and Cloud Monitoring API. During the preview [Preview](https://docs.cloud.google.com/products#product-launch-stages) period, you can opt-in to using the Telemetry API. For more information, see [Use the Telemetry API](https://docs.cloud.google.com/monitoring/agent/ops-agent/use-telemetry-api).

**Cloud Monitoring**

v3

Feature

Starting with version 2.66.0, the Ops Agent can export your metrics and logs by using the OpenTelemetry-based [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) rather than by using the Cloud Monitoring API and Cloud Logging API. During the preview [Preview](https://docs.cloud.google.com/products#product-launch-stages) period, you can opt-in to using the Telemetry API. For more information, see [Use the Telemetry API](https://docs.cloud.google.com/monitoring/agent/ops-agent/use-telemetry-api).

## May 11, 2026

**Cloud Trace**

v2

Feature

Google Cloud Observability has expanded the supported locations for observability buckets, which store your trace data, to include the following:

  * asia-northeast1
  * asia-southeast1
  * me-west2
  * southamerica-east1
  * us-west4



For a list of supported locations, see [Locations for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).

## May 06, 2026

**Cloud Trace**

v2

Feature

The following remote MCP servers automatically generate a trace span for `tools/call` operations. These spans can help you understand the behavior of your agentic applications. For more information, see [Investigate MCP calls using Trace](https://docs.cloud.google.com/stackdriver/docs/instrumentation/trace-remote-mcp-server-calls).

  * Agent Search
  * AlloyDB for PostgreSQL
  * Google Security Operations



## May 01, 2026

**Cloud Trace**

v2

Feature

Google Cloud Observability has expanded the supported locations for observability buckets, which store your trace data, to include the following:

  * australia-southeast1
  * europe-central2
  * europe-north1
  * europe-southwest1
  * europe-west2
  * europe-west10
  * europe-west12
  * me-central2
  * northamerica-northeast1
  * us-east4



For a list of supported locations, see [Locations for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).

## April 27, 2026

**Cloud Trace**

v2

Feature

Cloud Trace is a service covered by the [Cloud Observability (Monitoring, Logging, Trace) Service Level Agreement (SLA)](https://cloud.google.com/operations/sla).

## April 23, 2026

**Cloud Monitoring**

v3

Feature

The [Cloud Monitoring API MCP server](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp) is generally available (GA). To learn about using the Monitoring MCP server to let agents and AI applications interact with your metrics data, see [Use the Cloud Monitoring remote MCP server](https://docs.cloud.google.com/monitoring/docs/use-monitoring-mcp).

## April 22, 2026

**Cloud Logging**

v2

Feature

The [Cloud Logging API MCP server](https://docs.cloud.google.com/logging/docs/reference/v2_mcp/mcp) is generally available (GA). To learn about using the Logging MCP server to let agents and AI applications interact with your log entries, see [Use the Cloud Logging remote MCP server](https://docs.cloud.google.com/logging/docs/use-logging-mcp).

**Cloud Monitoring**

v3

Feature

Application Monitoring in Google Cloud provides both agent observability and application observability. Your Application Monitoring dashboards display performance metrics, including the error rates and token usage of your AI resources. Those metrics can help you understand the health and performance of your AI resources.

To learn more, see the following:

  * [Agent observability](https://docs.cloud.google.com/stackdriver/docs/observability/agent-observability)
  * [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring)
  * [Investigate applications, services, and workloads](https://docs.cloud.google.com/stackdriver/docs/observability/application-monitoring)
  * [View AI resources](https://docs.cloud.google.com/stackdriver/docs/observability/application-monitoring-ai-resources)



## April 20, 2026

**Cloud Logging**

v2

Libraries

### Go

#### [v1.16.0](https://github.com/googleapis/google-cloud-go/compare/logging/v1.15.0...logging/v1.16.0) (2026-04-13)

## April 15, 2026

**Cloud Trace**

v2

Feature

Your trace data can be encrypted with a customer-managed encryption key (CMEK). To enable CMEK, set a default storage location and for that location, set a default Cloud Key Management Service key.

You can set these defaults for an organization, a folder, or a project. When set for an organization or folder, the settings apply to that resource and to its descendants. For more information, see [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets).

Feature

When you configure a default storage location, you control the location of your new observability buckets. These buckets store your trace data.

You can set a default storage location for an organization, a folder, or a project. When set for an organization or folder, the setting applies to that resource and to its descendants. For more information, see [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets).

## April 13, 2026

**Cloud Logging**

v2

Libraries

### Go

#### [v1.15.0](https://github.com/googleapis/google-cloud-go/compare/logging/v1.14.0...logging/v1.15.0) (2026-04-09)

**Cloud Monitoring**

v3

Feature

Application Monitoring can display a single, dynamic topology map showing your App Hub applications and your registered and discovered services and workloads. This interactive map identifies services and workloads that have open incidents. It also displays the error rates and P95 latency between your services and workloads.

To learn more, see the following:

  * [View application topology](https://docs.cloud.google.com/monitoring/docs/application-topology)
  * [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring)
  * [View application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring)



## April 10, 2026

**Cloud Trace**

v2

Feature

Use Cloud Trace to troubleshoot your MCP server usage, tool failures, and latency causes. For more information, see [Investigate MCP calls using Trace](https://docs.cloud.google.com/trace/docs/trace-remote-mcp-server-calls).

## April 08, 2026

**Cloud Trace**

v2

Feature

Google Cloud CLI lets you configure trace scopes, manage observability buckets, and set default observability settings. These features are in Public Preview. For more information, see the following documents:

  * Configure trace scopes by using the Google Cloud console, the Google Cloud CLI, Terraform, or the Observability API. For more information, see [Create and manage trace scopes](https://docs.cloud.google.com/trace/docs/trace-scope/create-and-manage).

  * Manage trace storage by using the Google Cloud CLI or the Observability API. For more information, see [Manage trace storage](https://docs.cloud.google.com/trace/docs/storage-manage).

  * Configure default settings by using the Google Cloud CLI, Terraform, or the Observability API. For more information, see [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets).




## April 07, 2026

**Cloud Logging**

v2

Feature

You can now ingest OTLP-formatted logs into Cloud Logging by using an OpenTelemetry Collector, an OTLP exporter, and the Telemetry API. For more information, see [OTLP log ingestion overview](https://docs.cloud.google.com/stackdriver/docs/otlp-logs/overview). The Telemetry API for log ingestion is in [Preview](https://docs.cloud.google.com/products#product-launch-stages). 

## April 06, 2026

**Cloud Logging**

v2

Libraries

### Go

#### [v1.14.0](https://github.com/googleapis/google-cloud-go/compare/logging/v1.13.2...logging/v1.14.0) (2026-04-02)

## April 03, 2026

**Cloud Logging**

v2

Announcement

Cloud Logging adds support for the `ca` multi-region. For a complete list of supported regions, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions). This note is incorrect; see entry for June 18, 2026.

**Cloud Monitoring**

v3

Feature

Application Monitoring has added a **Services and Workloads** tab, which lists your registered and discovered services and workloads. From this tab, you can do the following:

  * Register discovered services and workloads.
  * Search for services and workloads by functional type, such as `Agent` or `MCP server`.
  * Open dashboards that display telemetry. For discovered services and workload, Google Cloud Observability uses the [Cloud Asset Inventory name](https://docs.cloud.google.com/asset-inventory/docs/asset-names) to identify relevant information.



To learn more, see the following:

  * [List registered and discovered services and workloads](https://docs.cloud.google.com/monitoring/docs/application-monitoring#list-reg-disc)
  * [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring)
  * [View application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring)



## April 02, 2026

**Cloud Logging**

v2

Feature

The filter capabilities for log views have been extended to include support for disjunctive clauses, negation statements, and labels. To learn more, see [Filters for log views](https://docs.cloud.google.com/logging/docs/logs-views#view-filter).

**Cloud Monitoring**

v3

Feature

Application Monitoring has added support for the following resources:

  * Vertex AI Workbench
  * GKE Gateway
  * GKE Ingress
  * Layer 7 cross-regional Application Load Balancers



Additionally, dashboards for Kubernetes workloads display L4 and L7 traffic metrics, when both are available. For more information, see [Application Monitoring supported infrastructure](https://docs.cloud.google.com/monitoring/docs/application-monitoring-services).

## March 30, 2026

**Cloud Logging**

v2

Change

For any new project that is created on or after March 30, 2026, if the project enables the Cloud Logging API, then Google Cloud Observability also enables the [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview).

**Cloud Monitoring**

v3

Change

For any new project that is created on or after March 30, 2026, if the project enables the Cloud Monitoring API, [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview).

**Cloud Trace**

v2

Change

For any new project that is created on or after March 30, 2026, if the project enables the Cloud Trace API, then Google Cloud Observability also enables the [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview).

Feature

You can use the [Cloud Trace API MCP server](https://docs.cloud.google.com/trace/docs/reference/mcp/mcp) to let agents and AI applications interact with your trace data. This feature is in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

## March 26, 2026

**Error Reporting**

v1beta1

Feature

You can use the [Error Reporting API MCP server](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp) to let agents and AI applications interact with your error data. This feature is in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

## March 24, 2026

**Cloud Monitoring**

v3

Feature

The Telemetry API's supports up to 60,000 metric-ingestion requests per minute per region. The regional quota replaces the global quota. To learn more, see [Telemetry API quotas and limits for metric ingestion](https://docs.cloud.google.com/monitoring/quotas#telemetry-api-metric-limits).

**Cloud Trace**

v2

Feature

The Telemetry API supports trace ingestion of up to 2.4GB per minute for the following regions:

  * asia-east1, asia-northeast1, asia-southeast1, and asia-south1
  * europe-west1, europe-west2, europe-west3, and europe-west4
  * us-central1, us-east4, and us-west1.



For all other regions, the Telemetry API supports trace ingestion of up to 300 MB per minute.

These regional byte-based quotas replace a global quota which limited the number of requests per minute. To learn more, see [Telemetry API limits and quotas](https://docs.cloud.google.com/trace/docs/quotas#telemetry-api-limits).

## March 19, 2026

**Cloud Trace**

v2

Feature

Google Cloud Observability has expanded the supported locations for observability buckets, which store your trace data, to include the following:

  * africa-south1
  * asia-east1
  * asia-east2
  * asia-northeast2
  * asia-northeast3
  * asia-south1
  * asia-south2
  * asia-southeast2
  * asia-southeast3
  * australia-southeast2
  * europe-north2
  * europe-west1
  * europe-west4
  * europe-west6
  * europe-west8
  * me-central1
  * northamerica-northeast2
  * northamerica-south1
  * southamerica-west1
  * us-east5
  * us-south1
  * us-west2
  * us-west3



For a list of supported locations, see [Locations for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).

Feature

You can create alerting policies that monitor the results of your SQL queries. For more information, see [Monitor your SQL query results with an alerting policy](https://docs.cloud.google.com/trace/docs/sql-in-alerting). This feature is in public preview.

## March 12, 2026

**Cloud Logging**

v2

Issue

The automatic backfill operation performed on a log bucket that has been upgraded to use Log Analytics has been temporarily paused. To manually initiate the backfill operation, contact [Cloud Customer Care](https://docs.cloud.google.com/stackdriver/docs/getting-support).

## March 09, 2026

**Cloud Monitoring**

v3

Feature

You can configure legend templates for PromQL-formatted charts. To learn more, see [Configure the name of a legend column](https://docs.cloud.google.com/monitoring/charts/working-with-legends#descr_template).

**Cloud Trace**

v2

Change

You can send trace data to your Google Cloud project by using the Cloud Trace API or the Telemetry API. These two APIs are enabled individually.

If you send trace data to the Telemetry API endpoint, then Google Cloud Observability requires that the Cloud Trace API be enabled on your Google Cloud project before it stores the trace data. If the Cloud Trace API is disabled, then Google Cloud Observability discards the trace data.

To learn more, see [APIs that ingest trace data](https://docs.cloud.google.com/trace/docs/overview#supported-apis).

## March 02, 2026

**Cloud Monitoring**

v3

Feature

The SQL queries issued by **Observability Analytics** can now use a system-defined variable which resolves to the project ID. If a dashboard template uses the project ID variable, then you don't need to update the SQL query after installing the template.

For more information, see the following documents:

  * [Google Cloud console: Charts with SQL queries](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent#sql)
  * [API: Charts with SQL queries](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard#sql)



## February 26, 2026

**Cloud Trace**

v2

Feature

For organizations, folders, and projects, you can now configure default settings for observability buckets. Default settings let you specify the following for new observability buckets:

  * A location.
  * A Cloud KMS key.



This feature is in public preview. To learn more, see [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets).

Feature

You can now configure observability buckets to be in the following [locations](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations):

  * us
  * eu
  * us-central1
  * us-west1



Your trace data is stored in an observability bucket. To learn more, see [Trace storage overview](https://docs.cloud.google.com/trace/docs/storage-overview).

## February 17, 2026

**Cloud Trace**

v2

Deprecated

Starting February 18, 2026, [trace sinks](https://docs.cloud.google.com/trace/docs/trace-export-overview) are deprecated. For more information, see [Export trace spans with sinks deprecation](https://docs.cloud.google.com/stackdriver/docs/deprecations/export-spans-with-sinks).

You can use the Observability Analytics page, which provides a SQL query interface, to query both your trace and log data. To learn more, see the following documents:

  * To migrate to using Observability Analytics page from a sink-based export of trace data to BigQuery, see [Migrate to Observability Analytics](https://docs.cloud.google.com/trace/docs/analytics-migrate).

  * To query your trace data by using the Observability Analytics page, see [Query and analyze traces](https://docs.cloud.google.com/trace/docs/analytics).

  * To query your trace data by using BigQuery services, see [Query a linked BigQuery dataset](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset).




## February 12, 2026

**Cloud Logging**

v2

Feature

You no longer need to configure BigQuery reservation assignments to create SQL-based alerting policies or run Log Analytics queries on BigQuery slots. These queries now use on-demand slots by default if no BigQuery reservation assignment exists.

For more information, see the following documents:

  * [Query a linked BigQuery dataset](https://docs.cloud.google.com/logging/docs/analyze/query-linked-dataset#dedicated)
  * [Monitor your SQL query results with an alerting policy](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting#sql-policies-bigquery)



## February 09, 2026

**Cloud Logging**

v2

Feature

You can use the [Cloud Logging API MCP server](https://docs.cloud.google.com/logging/docs/reference/v2_mcp/mcp) to let agents and AI applications interact with your log entries. This feature is in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

## February 06, 2026

**Cloud Monitoring**

v3

Feature

You can use the [Cloud Monitoring API MCP server](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp) to let agents and AI applications interact with your time series data. This feature is in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

Feature

You can now ingest OTLP metrics into Cloud Monitoring by using an OpenTelemetry Collector, an OTLP exporter, and the Telemetry API. For more information, see [OTLP metric ingestion overview](https://docs.cloud.google.com/stackdriver/docs/otlp-metrics/overview). The Telemetry API for metric ingestion is in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

## February 02, 2026

**Cloud Logging**

v2

Libraries

### Java

#### [3.24.0](https://github.com/googleapis/java-logging/compare/v3.23.11...v3.24.0) (2026-01-26)

##### Features

  * Bump minor version ([#1923](https://github.com/googleapis/java-logging/issues/1923)) ([ad7958c](https://github.com/googleapis/java-logging/commit/ad7958c789a86fd7fe2c10e3ce4ea57174aee379))



**Cloud Trace**

v2

Feature

You can now analyze your trace data by using the **Log Analytics** page in the Google Cloud console. This page supports SQL queries and lets you view your query results as a table or as a chart. Your SQL queries can also join your trace and log data. This feature is in Public Preview.

To learn more about analyzing and viewing trace data, see the following documents:

  * [Query and analyze traces](https://docs.cloud.google.com/trace/docs/analytics)
  * [Find and explore traces by using the Trace Explorer](https://docs.cloud.google.com/trace/docs/finding-traces)



Feature

Cloud Trace now stores your trace data in an observability dataset. You can continue to view your trace data by using the **Trace Explorer** page. If you create a link on your dataset, then you can use services like BigQuery to query and analyze your trace data. To learn more, see the following documents:

  * [Trace storage overview](https://docs.cloud.google.com/trace/docs/storage-overview)
  * [Manage trace storage](https://docs.cloud.google.com/trace/docs/storage-manage)
  * [Query a linked BigQuery dataset](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset)



## January 29, 2026

**Cloud Logging**

v2

Feature

You can now export your Crashlytics data and (optionally) Firebase sessions data to Cloud Logging. Once the data is exported, it's also available to Cloud Monitoring, so you can filter your logs, build custom dashboards, set up custom alerts, and even export the data to other services. For information about how to export your Crashlytics data, see [Export Crashlytics data to Cloud Logging](https://firebase.google.com/docs/crashlytics/cloud-logging-export), and for information about how you can use this data, see [What can you do with Crashlytics data in Cloud Logging](https://firebase.google.com/docs/crashlytics/cloud-logging-what-can-you-do).

## January 26, 2026

**Cloud Logging**

v2

Change

To support correlation between log and trace data, the following changes have been made:

  * The required format for the `LogEntry.trace` field has been relaxed. The preferred format for this field is the trace ID. However, you can continue to provide the full resource name. For more information, see [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).

  * If you open the **Trace Details flyout** page by using options provided in a log entry, then the resources listed in the default trace scope are searched for the trace data.

  * If you open the **Logs Explorer** page by using options on span data, then the resources listed in the default log scope are searched for log data.




To learn more about default scopes, see [Configure observability scopes for multi-project queries](https://docs.cloud.google.com/stackdriver/docs/observability/scopes).

Feature

You can now install and manage the Ops Agent on virtual machines across zones in your Google Cloud project by using global VM Extension Manager extension policies. Global and zonal extension policies can keep the installed version of the agent current, keep a specified version of the agent installed, and other tasks. For more information, see [Install and manage the Ops Agent by using VM Extension Manager policies](https://docs.cloud.google.com/logging/docs/agent/ops-agent/agent-vmem-policies).

**Cloud Monitoring**

v3

Feature

You can now install and manage the Ops Agent on virtual machines across zones in your Google Cloud project by using global VM Extension Manager extension policies. Global and zonal extension policies can keep the installed version of the agent current, keep a specified version of the agent installed, and other tasks. For more information, see [Install and manage the Ops Agent by using VM Extension Manager policies](https://docs.cloud.google.com/monitoring/agent/ops-agent/agent-vmem-policies).

**Cloud Trace**

v2

Change

To support correlation between log and trace data, the following changes have been made:

  * The required format for the `LogEntry.trace` field has been relaxed. The preferred format for this field is the trace ID. However, you can continue to provide the full resource name. For more information, see [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).

  * If you open the **Trace Details flyout** page by using options provided in a log entry, then the resources listed in the default trace scope are searched for the trace data.

  * If you open the **Logs Explorer** page by using options on span data, then the resources listed in the default log scope are searched for log data.




To learn more about default scopes, see [Configure observability scopes for multi-project queries](https://docs.cloud.google.com/stackdriver/docs/observability/scopes).

## January 21, 2026

**Cloud Monitoring**

v3

Feature

Your Application Monitoring dashboards now display the trace spans that are associated with your registered App Hub applications. The display includes annotations that let you identify services and workloads. You can also open the Trace Explorer page from your Application Monitoring dashboards. To learn more, see the following documents:

  * [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring).
  * [View application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring).
  * [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces) describes how to use the Trace Explorer page to filter and explore your trace data.



## January 20, 2026

**Cloud Logging**

v2

Announcement

Cloud Logging adds support for the `asia-southeast3` region. For a complete list of supported regions, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## January 19, 2026

**Cloud Logging**

v2

Libraries

### Java

#### [3.23.10](https://github.com/googleapis/java-logging/compare/v3.23.9...v3.23.10) (2026-01-15)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.65.1 ([e0ca81e](https://github.com/googleapis/java-logging/commit/e0ca81e148d4f7dd6426640c574b453905cbe000))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.55.1 ([#1911](https://github.com/googleapis/java-logging/issues/1911)) ([93eadba](https://github.com/googleapis/java-logging/commit/93eadbaba65210e8686ea5240430fdbc86038fd5))
  * Update googleapis/sdk-platform-java action to v2.65.1 ([#1910](https://github.com/googleapis/java-logging/issues/1910)) ([3853159](https://github.com/googleapis/java-logging/commit/3853159f7255910dd33900086d410351f4cb0e98))



## January 05, 2026

**Cloud Trace**

v2

Feature

You can now collect, view, and analyze multimodal prompts and responses from your agentic applications that use the LangGraph or Agent Development Kit (ADK) frameworks. This feature is in [Public Preview](https://cloud.google.com/products#product-launch-stages).

To learn more, see the following documents:

  * [Collect and view multimodal prompts and responses](https://docs.cloud.google.com/trace/docs/collect-view-multimodal-prompts-responses)
  * [Instrument generative AI applications](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-overview)



## December 22, 2025

**Cloud Logging**

v2

Libraries

### Python

#### [3.13.0](https://github.com/googleapis/python-logging/compare/v3.12.1...v3.13.0) (2025-12-15)

##### Features

  * Add support for python 3.14 (#1065) ([6be3df6a](https://github.com/googleapis/python-logging/commit/6be3df6a))



##### Bug Fixes

  * remove setup.cfg configuration for creating universal wheels (#981) ([70f612c3](https://github.com/googleapis/python-logging/commit/70f612c3))



### Java

#### [3.24.0-rc1](https://github.com/googleapis/java-logging/compare/v3.23.9...v3.24.0-rc1) (2025-12-16)

##### Features

  * [java] allow passing libraries_bom_version from env ([#1967](https://github.com/googleapis/java-logging/issues/1967)) ([#1615](https://github.com/googleapis/java-logging/issues/1615)) ([dc00cd0](https://github.com/googleapis/java-logging/commit/dc00cd0da891b59f3c22cd7ce281868f5ce8b433))
  * Add an API method for reordering firewall policies ([#1538](https://github.com/googleapis/java-logging/issues/1538)) ([9cd6b96](https://github.com/googleapis/java-logging/commit/9cd6b96d9946828c02ccff2ff846a06cc6fff329))
  * Add Cloud Run Jobs support ([#1574](https://github.com/googleapis/java-logging/issues/1574)) ([1dd64d0](https://github.com/googleapis/java-logging/commit/1dd64d078e0d4cbb1e16cb1d050ba192492d6a60))
  * enable hermetic library generation ([#1620](https://github.com/googleapis/java-logging/issues/1620)) ([034b9c4](https://github.com/googleapis/java-logging/commit/034b9c42ac8ba12f20dbde9e90ae8e59ea4c5748))
  * introduce `java.time` methods ([#1729](https://github.com/googleapis/java-logging/issues/1729)) ([323eb33](https://github.com/googleapis/java-logging/commit/323eb332a65f39c5588cf65ecae0a3454903a1c6))
  * Log Analytics features of the Cloud Logging API ([#1335](https://github.com/googleapis/java-logging/issues/1335)) ([7d43b80](https://github.com/googleapis/java-logging/commit/7d43b8049c71187fffcde39274db38ebb54cddfa))
  * **logging:** OpenTelemetry trace/span ID integration for Java logging library ([#1596](https://github.com/googleapis/java-logging/issues/1596)) ([67db829](https://github.com/googleapis/java-logging/commit/67db829621fd1c4a876d158fe1afb4927821fa54))
  * next release from main branch is 3.22.0 ([#1776](https://github.com/googleapis/java-logging/issues/1776)) ([7736073](https://github.com/googleapis/java-logging/commit/773607312a1dc6f5f569f2518587ffba4743bb43))
  * next release from main branch is 3.23.0 ([#1826](https://github.com/googleapis/java-logging/issues/1826)) ([f0ef15f](https://github.com/googleapis/java-logging/commit/f0ef15f609a3400460bd8074bdd05014cc388743))
  * update with latest from main ([#1904](https://github.com/googleapis/java-logging/issues/1904)) ([d613362](https://github.com/googleapis/java-logging/commit/d61336242d51197207c94698735dfea72ec94c12))
  * Upgrade protobuf gen code to 4.33 ([#1905](https://github.com/googleapis/java-logging/issues/1905)) ([e25b532](https://github.com/googleapis/java-logging/commit/e25b5323d0ff7ca6d1c195d0eb342408621cdd76))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.31.0 ([#1502](https://github.com/googleapis/java-logging/issues/1502)) ([c7a20de](https://github.com/googleapis/java-logging/commit/c7a20de29bf6fae079f8d73e3062025a79c220c9))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.32.0 ([#1511](https://github.com/googleapis/java-logging/issues/1511)) ([e2f574c](https://github.com/googleapis/java-logging/commit/e2f574caa0b8c2a2cdb3b186fbf2d599d6ef4c2b))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.37.0 ([#1553](https://github.com/googleapis/java-logging/issues/1553)) ([15b05fc](https://github.com/googleapis/java-logging/commit/15b05fc4a8e6c4069414110b749525082821e509))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.39.0 ([#1587](https://github.com/googleapis/java-logging/issues/1587)) ([848418b](https://github.com/googleapis/java-logging/commit/848418b426c2e93e636dbd9de71985c386ccb9d2))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.47.0 ([90b88ee](https://github.com/googleapis/java-logging/commit/90b88ee70ee84bdcb0af4aced50b5ee61e0a706c))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.49.0 ([a1ec68d](https://github.com/googleapis/java-logging/commit/a1ec68d539e4d0720fb2cf72314deb4f485f3d4a))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.50.0 ([afcf63c](https://github.com/googleapis/java-logging/commit/afcf63cc063c4e0f5159c3ac5dbe2d372c335beb))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.51.0 ([04d8868](https://github.com/googleapis/java-logging/commit/04d886849a4b41fad17f501f2c40ae54e6daa71a))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.51.1 ([705dba2](https://github.com/googleapis/java-logging/commit/705dba2d6c12bd9f9e281c962cfb232ab28b31a9))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.52.0 ([888a885](https://github.com/googleapis/java-logging/commit/888a885dc229960c26fae5098c4b43b7b0ef4fa6))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.54.0 ([67fa9fb](https://github.com/googleapis/java-logging/commit/67fa9fbbc48dd8df9c176ba0bb3d1acf6b975bfc))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.55.1 ([dd25992](https://github.com/googleapis/java-logging/commit/dd259929b01a2dd50ca2d09005fedf1631b97877))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.56.2 ([7cce5b5](https://github.com/googleapis/java-logging/commit/7cce5b509c904209f0a92e239e836afac4169ec4))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.56.3 ([844f4fa](https://github.com/googleapis/java-logging/commit/844f4fa48f878a7da77ff9ab13652dc93f079920))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.58.0 ([45b4878](https://github.com/googleapis/java-logging/commit/45b4878eeec35f8c19a3cd3cd33331e9ece6b5c6))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.59.0 ([f2362fb](https://github.com/googleapis/java-logging/commit/f2362fb4c05d34fda4a1c9788ea87822ac887d9e))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.60.2 ([6a268f8](https://github.com/googleapis/java-logging/commit/6a268f8dbb33b38fa5e4d35d8dfcd196f8fcf9db))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.61.0 ([0a21b83](https://github.com/googleapis/java-logging/commit/0a21b83377e6e6a2f4cf98149424a47dcd490c1c))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.62.1 ([1438bff](https://github.com/googleapis/java-logging/commit/1438bff5bc7028fbf125895f0bdd2bb50490effa))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.62.2 ([eeca440](https://github.com/googleapis/java-logging/commit/eeca440da06c24afc07e669f6f087246d91cd933))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.62.3 ([5d5d8a7](https://github.com/googleapis/java-logging/commit/5d5d8a76c58c3329f90e4fa84f5e81a1d3296894))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.63.0 ([385a1dc](https://github.com/googleapis/java-logging/commit/385a1dc67fcdd8706238ba2f95f694bbb647f5f8))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.64.1 ([9187dcd](https://github.com/googleapis/java-logging/commit/9187dcd1314a6be4df8f8c6eed95092724c6da69))
  * enable v2.LogEntry Protobufs converter functions ([#1509](https://github.com/googleapis/java-logging/issues/1509)) ([9ef4d90](https://github.com/googleapis/java-logging/commit/9ef4d9048b1ecdc887ebc9cb4898a4bfe3f6c154))
  * Fixed outdated link to X-Cloud-Trace-Context header description ([#1713](https://github.com/googleapis/java-logging/issues/1713)) ([d474313](https://github.com/googleapis/java-logging/commit/d4743138b9e5c9fd4e9c59b0793028f1e424e6e4))
  * **java:** handle empty modules ([09eeff0](https://github.com/googleapis/java-logging/commit/09eeff0b4608bad1e854252ff73688a867a071f1))
  * **java:** skip fixing poms for special modules ([#1744](https://github.com/googleapis/java-logging/issues/1744)) ([#1256](https://github.com/googleapis/java-logging/issues/1256)) ([09eeff0](https://github.com/googleapis/java-logging/commit/09eeff0b4608bad1e854252ff73688a867a071f1))
  * next release candidate ([31ee5a3](https://github.com/googleapis/java-logging/commit/31ee5a3b89701fbd9468a6ed903a9fc1951d65d5))
  * regenerate gapic yaml and service yaml for logging by augmentation configs ([9023895](https://github.com/googleapis/java-logging/commit/9023895fd56381c1f4309843a269975763a89d40))
  * Remove org.jspecify dependency ([#1364](https://github.com/googleapis/java-logging/issues/1364)) ([8138f46](https://github.com/googleapis/java-logging/commit/8138f463e170f1927280d3c083fa403b184fca47))
  * Replace internal Structs class with google-cloud-core version ([#1501](https://github.com/googleapis/java-logging/issues/1501)) ([21e1929](https://github.com/googleapis/java-logging/commit/21e19295923a33759229e2e992d003409ab1feb3))



##### Dependencies

  * update actions/checkout action to v4 ([#1570](https://github.com/googleapis/java-logging/issues/1570)) ([ea0db35](https://github.com/googleapis/java-logging/commit/ea0db3579da6e965e778233b3cba4862b3fff65c))
  * update actions/github-script action to v7 ([#1571](https://github.com/googleapis/java-logging/issues/1571)) ([16d6192](https://github.com/googleapis/java-logging/commit/16d61928b6d4887faebbdd48a694a2edff8cb752))
  * update actions/setup-java action to v4 ([#1572](https://github.com/googleapis/java-logging/issues/1572)) ([9eb8834](https://github.com/googleapis/java-logging/commit/9eb88346fac9688c0e56bec83f7407c5690a5b7f))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.1.1 ([#1243](https://github.com/googleapis/java-logging/issues/1243)) ([fdf6b7a](https://github.com/googleapis/java-logging/commit/fdf6b7a44435286a47e1143a53a8307bb5b8fc63))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.1.2 ([#1258](https://github.com/googleapis/java-logging/issues/1258)) ([d4bc663](https://github.com/googleapis/java-logging/commit/d4bc663a0a0295594fb6333cf9bf2a6fd7a7b7e8))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.10.1 ([#1354](https://github.com/googleapis/java-logging/issues/1354)) ([b2f1111](https://github.com/googleapis/java-logging/commit/b2f1111fc8df71b40a85505e1b8209d315cc2c90))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.11.0 ([#1367](https://github.com/googleapis/java-logging/issues/1367)) ([8cd2a53](https://github.com/googleapis/java-logging/commit/8cd2a53b396d4671514bf8cca1b4c2a62cfb457c))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.12.0 ([#1382](https://github.com/googleapis/java-logging/issues/1382)) ([8241302](https://github.com/googleapis/java-logging/commit/824130227897ed17c5b8a1becf32a695d844b2bb))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.13.0 ([#1388](https://github.com/googleapis/java-logging/issues/1388)) ([03179b0](https://github.com/googleapis/java-logging/commit/03179b0697f17bfc114ff114e454464ed76f8d5b))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.13.1 ([#1395](https://github.com/googleapis/java-logging/issues/1395)) ([1a29b9d](https://github.com/googleapis/java-logging/commit/1a29b9da803238ff1dee0c69d9449d97d4324477))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.14.0 ([#1409](https://github.com/googleapis/java-logging/issues/1409)) ([f9af381](https://github.com/googleapis/java-logging/commit/f9af381b302aeefa401e5bc2f51d97c09f1484e5))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.15.0 ([#1424](https://github.com/googleapis/java-logging/issues/1424)) ([4f82f33](https://github.com/googleapis/java-logging/commit/4f82f339e47014821eca217f5200080e6b78e03f))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.16.1 ([#1434](https://github.com/googleapis/java-logging/issues/1434)) ([e9e9835](https://github.com/googleapis/java-logging/commit/e9e9835e6c7b52364104a1e4a503027efb722422))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.17.0 ([#1444](https://github.com/googleapis/java-logging/issues/1444)) ([748e8a2](https://github.com/googleapis/java-logging/commit/748e8a29026b6eb782a559df207a70555289f906))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.18.0 ([#1454](https://github.com/googleapis/java-logging/issues/1454)) ([dc25a87](https://github.com/googleapis/java-logging/commit/dc25a87cb6e1d64c2e2c811a928ea2553a684daa))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.19.0 ([#1468](https://github.com/googleapis/java-logging/issues/1468)) ([5835a7d](https://github.com/googleapis/java-logging/commit/5835a7dc1c839eb3bc379470846451bd51fdfc24))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.2.0 ([#1269](https://github.com/googleapis/java-logging/issues/1269)) ([e196a80](https://github.com/googleapis/java-logging/commit/e196a802d0d004dcec2ddfb352ed9aebebe68810))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.20.0 ([#1484](https://github.com/googleapis/java-logging/issues/1484)) ([f3227db](https://github.com/googleapis/java-logging/commit/f3227dbbb6ef7f8b16ff4a6d39882f57868915f1))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.21.0 ([#1500](https://github.com/googleapis/java-logging/issues/1500)) ([6cce3c9](https://github.com/googleapis/java-logging/commit/6cce3c9bbe051180789c7ff4fbdde4c45fe46888))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.22.0 ([#1510](https://github.com/googleapis/java-logging/issues/1510)) ([b40e846](https://github.com/googleapis/java-logging/commit/b40e8465590dadec7c9ff26eb27e92c16b059489))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.23.0 ([#1518](https://github.com/googleapis/java-logging/issues/1518)) ([30ba9ed](https://github.com/googleapis/java-logging/commit/30ba9ed687f5469d36138a138f68cd998cf60b53))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.3.0 ([#1282](https://github.com/googleapis/java-logging/issues/1282)) ([58ac608](https://github.com/googleapis/java-logging/commit/58ac608ddbf5803bb394bb4833cf8af0bbb22e91))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.4.0 ([#1290](https://github.com/googleapis/java-logging/issues/1290)) ([84d42ae](https://github.com/googleapis/java-logging/commit/84d42ae6da926785462088de23947bc742f9dc0a))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.5.0 ([#1301](https://github.com/googleapis/java-logging/issues/1301)) ([9fa6f05](https://github.com/googleapis/java-logging/commit/9fa6f05a9ea1444d9abad4e0eae5fd854bb2608c))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.6.0 ([#1308](https://github.com/googleapis/java-logging/issues/1308)) ([febcf49](https://github.com/googleapis/java-logging/commit/febcf49085ed0fb6be02aaf9108805dd4cce31b8))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.7.0 ([#1318](https://github.com/googleapis/java-logging/issues/1318)) ([973d260](https://github.com/googleapis/java-logging/commit/973d2601bc1639b09d4dd89dd2b6f90cd1b779e9))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.8.0 ([#1326](https://github.com/googleapis/java-logging/issues/1326)) ([5a56f1b](https://github.com/googleapis/java-logging/commit/5a56f1b5087e65bc097d5c8a85d000d12bbbca8c))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.9.0 ([#1342](https://github.com/googleapis/java-logging/issues/1342)) ([8b14ae1](https://github.com/googleapis/java-logging/commit/8b14ae17514481a5925ae3ff079cc4f1b4ad6d94))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.24.0 ([#1526](https://github.com/googleapis/java-logging/issues/1526)) ([235f1aa](https://github.com/googleapis/java-logging/commit/235f1aa380d4f34f65d4cc957b3d26fa6a35e226))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.25.0 ([#1535](https://github.com/googleapis/java-logging/issues/1535)) ([7fde779](https://github.com/googleapis/java-logging/commit/7fde7795f03ac96353912829b42adc0035a41d26))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.27.0 ([#1552](https://github.com/googleapis/java-logging/issues/1552)) ([6c5464d](https://github.com/googleapis/java-logging/commit/6c5464d1c5a74962fcd459a1e03282747e148a44))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.28.0 ([#1560](https://github.com/googleapis/java-logging/issues/1560)) ([d52e623](https://github.com/googleapis/java-logging/commit/d52e62343aa814183baa4fa8ea39d41a5e7c423f))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.28.1 ([#1563](https://github.com/googleapis/java-logging/issues/1563)) ([81aa3e6](https://github.com/googleapis/java-logging/commit/81aa3e6b6662d62844b289a22e8aba50dff36a51))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.28.1 ([#1569](https://github.com/googleapis/java-logging/issues/1569)) ([8eb0781](https://github.com/googleapis/java-logging/commit/8eb0781b1e1e6e369a6ff0a03d1db4cd0462a6a7))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.29.0 ([#1586](https://github.com/googleapis/java-logging/issues/1586)) ([edcaf8d](https://github.com/googleapis/java-logging/commit/edcaf8de643a7f7f419ee6059c706d0ef0ef4873))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.30.0 ([#1603](https://github.com/googleapis/java-logging/issues/1603)) ([16967e5](https://github.com/googleapis/java-logging/commit/16967e5ba704a75419904ba2aaabce0cbc116352))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.30.1 ([#1611](https://github.com/googleapis/java-logging/issues/1611)) ([e7a0904](https://github.com/googleapis/java-logging/commit/e7a0904a1faf04b0de400c1778f976494246e39e))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.31.0 ([#1625](https://github.com/googleapis/java-logging/issues/1625)) ([9db8f3b](https://github.com/googleapis/java-logging/commit/9db8f3b948e20fa406f315b670341da2b00f0856))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.32.0 ([#1649](https://github.com/googleapis/java-logging/issues/1649)) ([cb428d1](https://github.com/googleapis/java-logging/commit/cb428d19a1ea750520d336c9d1042d50f3801f15))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.33.0 ([#1664](https://github.com/googleapis/java-logging/issues/1664)) ([cb6de76](https://github.com/googleapis/java-logging/commit/cb6de767ba726a1178b4ebd0b481a4fc2454b910))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.34.0 ([#1677](https://github.com/googleapis/java-logging/issues/1677)) ([dbd050c](https://github.com/googleapis/java-logging/commit/dbd050c354cee5272c37dd323358b222cea5e87e))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.35.0 ([#1683](https://github.com/googleapis/java-logging/issues/1683)) ([31ec2b9](https://github.com/googleapis/java-logging/commit/31ec2b972d5e11e12fe0432f42e3e5b8f23312c6))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.36.1 ([#1698](https://github.com/googleapis/java-logging/issues/1698)) ([9491512](https://github.com/googleapis/java-logging/commit/94915125fd2425ffba5ef86da0c54af3c1d2c138))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.37.0 ([#1702](https://github.com/googleapis/java-logging/issues/1702)) ([1f7da17](https://github.com/googleapis/java-logging/commit/1f7da17810fa22b8437edc88e4f95b3ed5cb8349))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.41.1 ([#1745](https://github.com/googleapis/java-logging/issues/1745)) ([6a7280d](https://github.com/googleapis/java-logging/commit/6a7280d0851024c1b44457fa7064a7f3d6fc2d5b))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.42.0 ([#1755](https://github.com/googleapis/java-logging/issues/1755)) ([d404381](https://github.com/googleapis/java-logging/commit/d4043815246423efe542356dc50ba663092b8df0))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.43.0 ([#1763](https://github.com/googleapis/java-logging/issues/1763)) ([e0f9f27](https://github.com/googleapis/java-logging/commit/e0f9f271be10cec0d9400bc464bcc0a175078d97))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.44.0 ([#1768](https://github.com/googleapis/java-logging/issues/1768)) ([a69e699](https://github.com/googleapis/java-logging/commit/a69e6990e5cc7ab920382599510bb14f29a12d7d))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.45.1 ([#1779](https://github.com/googleapis/java-logging/issues/1779)) ([a643ab0](https://github.com/googleapis/java-logging/commit/a643ab03600fa25cee41df23b2daf65c0fc4e70a))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.46.2 ([#1796](https://github.com/googleapis/java-logging/issues/1796)) ([1f88271](https://github.com/googleapis/java-logging/commit/1f882712aeb7e48a2339ffbad783813e11e74401))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.46.3 ([#1801](https://github.com/googleapis/java-logging/issues/1801)) ([d7aa7bc](https://github.com/googleapis/java-logging/commit/d7aa7bcd4e1235491f30ab4dd88ff80c07966185))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.47.0 ([#1803](https://github.com/googleapis/java-logging/issues/1803)) ([5967ffe](https://github.com/googleapis/java-logging/commit/5967ffe459d9e1d00a36727ae433303005bf15d8))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.48.0 ([#1808](https://github.com/googleapis/java-logging/issues/1808)) ([6327c51](https://github.com/googleapis/java-logging/commit/6327c51f3a8ecfb7af678c8c040b066e7f938863))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.49.0 ([#1813](https://github.com/googleapis/java-logging/issues/1813)) ([c15da84](https://github.com/googleapis/java-logging/commit/c15da84716d6d554ae26919412e8d4313fd980bc))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.50.0 ([#1821](https://github.com/googleapis/java-logging/issues/1821)) ([af4edc5](https://github.com/googleapis/java-logging/commit/af4edc5b1399b3563d9cf07e171c4281fde2bb79))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.50.1 ([#1828](https://github.com/googleapis/java-logging/issues/1828)) ([44c3094](https://github.com/googleapis/java-logging/commit/44c3094e23450f1a8e6bb397f209b17cf37a4345))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 ([#1834](https://github.com/googleapis/java-logging/issues/1834)) ([2e46f6e](https://github.com/googleapis/java-logging/commit/2e46f6ef44278af5031167106c216dcdb0a16357))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 ([#1843](https://github.com/googleapis/java-logging/issues/1843)) ([975d8ae](https://github.com/googleapis/java-logging/commit/975d8aeca38ff2f2f8317df93a661910969c5fc1))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.52.0 ([#1848](https://github.com/googleapis/java-logging/issues/1848)) ([162ef56](https://github.com/googleapis/java-logging/commit/162ef563793270c236ecf7ca2524ad3b560d7a12))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 ([#1853](https://github.com/googleapis/java-logging/issues/1853)) ([c21a635](https://github.com/googleapis/java-logging/commit/c21a635f054b1cd8a6e5aea7450017af85ba03c7))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.52.2 ([#1858](https://github.com/googleapis/java-logging/issues/1858)) ([0252352](https://github.com/googleapis/java-logging/commit/0252352ca34dd494c4471f3a90391df762d676df))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.52.3 ([#1869](https://github.com/googleapis/java-logging/issues/1869)) ([94405fa](https://github.com/googleapis/java-logging/commit/94405fa929c48db114dd10ae39a0f3e520865bbf))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.53.0 ([#1875](https://github.com/googleapis/java-logging/issues/1875)) ([b79fd2b](https://github.com/googleapis/java-logging/commit/b79fd2b0cd2c358e3d3e69ddc76fcbfa16a47b5b))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.54.1 ([#1883](https://github.com/googleapis/java-logging/issues/1883)) ([acc56db](https://github.com/googleapis/java-logging/commit/acc56db1ea0389ca91a09e435662b802db63abe6))
  * update dependency io.opentelemetry:opentelemetry-bom to v1.45.0 ([#1638](https://github.com/googleapis/java-logging/issues/1638)) ([7e007d4](https://github.com/googleapis/java-logging/commit/7e007d4f966ed7e9c75cbf0ce951441052e8735c))
  * update dependency io.opentelemetry:opentelemetry-bom to v1.46.0 ([#1747](https://github.com/googleapis/java-logging/issues/1747)) ([5ef2853](https://github.com/googleapis/java-logging/commit/5ef285387d63b79bff7e43b233c7f9770f378dba))
  * update dependency org.apache.maven.plugins:maven-deploy-plugin to v3.1.3 ([2b6ea70](https://github.com/googleapis/java-logging/commit/2b6ea703aad05e714f5634fbd74e0b9bca0c51f9))
  * update dependency org.easymock:easymock to v5.2.0 ([#1421](https://github.com/googleapis/java-logging/issues/1421)) ([f931544](https://github.com/googleapis/java-logging/commit/f9315443ba97104f1a23e5695ed72cb4bd2dfa10))
  * update dependency org.easymock:easymock to v5.5.0 ([#1639](https://github.com/googleapis/java-logging/issues/1639)) ([f559d89](https://github.com/googleapis/java-logging/commit/f559d89bf36201fce609ef752f27baa0c5f6f1c1))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.10.0 ([#1528](https://github.com/googleapis/java-logging/issues/1528)) ([b3e4f9b](https://github.com/googleapis/java-logging/commit/b3e4f9b77bffc49a4f9569d4b7a9318a0d5ea5c0))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.9.20 ([#1279](https://github.com/googleapis/java-logging/issues/1279)) ([296cce1](https://github.com/googleapis/java-logging/commit/296cce153cbd263e620c1fbb028466f62f7251dd))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.9.21 ([#1319](https://github.com/googleapis/java-logging/issues/1319)) ([5aef8d6](https://github.com/googleapis/java-logging/commit/5aef8d6492c9ebf8e989ee652dcf4a1d82cac8a4))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.9.22 ([#1340](https://github.com/googleapis/java-logging/issues/1340)) ([b3b9d5f](https://github.com/googleapis/java-logging/commit/b3b9d5ffe078a3203725f3709c1840cb88f6e9ea))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.9.23 ([#1374](https://github.com/googleapis/java-logging/issues/1374)) ([dce3c4c](https://github.com/googleapis/java-logging/commit/dce3c4c9413c2d1674b6ddaf6fe9351a28f0673a))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.9.24 ([#1411](https://github.com/googleapis/java-logging/issues/1411)) ([0487cdf](https://github.com/googleapis/java-logging/commit/0487cdff06c0ce9529d4c662991cf84ad25b9f40))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.9.26 ([#1420](https://github.com/googleapis/java-logging/issues/1420)) ([ff581a6](https://github.com/googleapis/java-logging/commit/ff581a67270777fe15e291794df3b49041c111e3))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.9.27 ([#1430](https://github.com/googleapis/java-logging/issues/1430)) ([9e750a3](https://github.com/googleapis/java-logging/commit/9e750a3c3685671ee573a7e8190622d7f9002b51))
  * update dependency org.graalvm.buildtools:junit-platform-native to v0.9.28 ([#1455](https://github.com/googleapis/java-logging/issues/1455)) ([3080cec](https://github.com/googleapis/java-logging/commit/3080cec373f8d9d61ce57363553925a07702d552))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.10.0 ([#1456](https://github.com/googleapis/java-logging/issues/1456)) ([f27713e](https://github.com/googleapis/java-logging/commit/f27713ed55159754715cca5ff205364e315a7c05))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.10.1 ([#1542](https://github.com/googleapis/java-logging/issues/1542)) ([af784bc](https://github.com/googleapis/java-logging/commit/af784bce7c5272a346ce5016464c87af7d69b442))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.20 ([#1280](https://github.com/googleapis/java-logging/issues/1280)) ([6363196](https://github.com/googleapis/java-logging/commit/63631966432aac89883dd80c0087576454616cc2))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.21 ([#1320](https://github.com/googleapis/java-logging/issues/1320)) ([fc2d065](https://github.com/googleapis/java-logging/commit/fc2d0655e5b3d2ea9aedf1a4fd65fad8cf815462))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.22 ([#1341](https://github.com/googleapis/java-logging/issues/1341)) ([cfc0106](https://github.com/googleapis/java-logging/commit/cfc0106c359c153031bddcac7dadc292a9bb561e))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.23 ([#1375](https://github.com/googleapis/java-logging/issues/1375)) ([a15c73c](https://github.com/googleapis/java-logging/commit/a15c73cbf8c22971f690d38fa87b6b349851d5c8))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.26 ([#1412](https://github.com/googleapis/java-logging/issues/1412)) ([bd9be4e](https://github.com/googleapis/java-logging/commit/bd9be4e8aecd5b7a532a6f2eb91151201a41334f))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.27 ([#1431](https://github.com/googleapis/java-logging/issues/1431)) ([7c2aa2c](https://github.com/googleapis/java-logging/commit/7c2aa2cc3b5651674591dc4e6cb89774d14e6513))
  * update dependency org.junit.vintage:junit-vintage-engine to v5.10.0 ([#1397](https://github.com/googleapis/java-logging/issues/1397)) ([f15d246](https://github.com/googleapis/java-logging/commit/f15d2462962c261be5726d5a68b6a1d31aa916fc))
  * update dependency org.junit.vintage:junit-vintage-engine to v5.10.1 ([#1471](https://github.com/googleapis/java-logging/issues/1471)) ([debc77f](https://github.com/googleapis/java-logging/commit/debc77f4ce57d768474c27eb6c056f7c10c7d743))
  * update dependency org.junit.vintage:junit-vintage-engine to v5.10.2 ([#1530](https://github.com/googleapis/java-logging/issues/1530)) ([20981dc](https://github.com/googleapis/java-logging/commit/20981dc90ca1b73b74d9f5a0c7f0dfa4d9960ab9))
  * update dependency org.junit.vintage:junit-vintage-engine to v5.9.2 ([#1245](https://github.com/googleapis/java-logging/issues/1245)) ([e73a704](https://github.com/googleapis/java-logging/commit/e73a704fa92d8f2abfe3b979e741b7f00ab89bca))
  * update dependency org.junit.vintage:junit-vintage-engine to v5.9.3 ([#1329](https://github.com/googleapis/java-logging/issues/1329)) ([dfb98f4](https://github.com/googleapis/java-logging/commit/dfb98f47098d4560fc3ef93f126af1770ae4faf6))
  * update googleapis/sdk-platform-java action to v2.51.1 ([#1742](https://github.com/googleapis/java-logging/issues/1742)) ([3c7a2c7](https://github.com/googleapis/java-logging/commit/3c7a2c70fd46cc7196ef7b037d6017971e8a020a))
  * update googleapis/sdk-platform-java action to v2.52.0 ([#1753](https://github.com/googleapis/java-logging/issues/1753)) ([3dcf86a](https://github.com/googleapis/java-logging/commit/3dcf86adc3e1ef3d5866cd043149808601c213b8))
  * update googleapis/sdk-platform-java action to v2.54.0 ([#1762](https://github.com/googleapis/java-logging/issues/1762)) ([d50a8d2](https://github.com/googleapis/java-logging/commit/d50a8d2fbef588138b4d47cbd3440d7217d690b0))
  * update googleapis/sdk-platform-java action to v2.55.1 ([#1780](https://github.com/googleapis/java-logging/issues/1780)) ([505557e](https://github.com/googleapis/java-logging/commit/505557e1b9b14c910aec402335bf9fc9ca96975c))
  * update googleapis/sdk-platform-java action to v2.57.0 ([#1804](https://github.com/googleapis/java-logging/issues/1804)) ([e9a27ec](https://github.com/googleapis/java-logging/commit/e9a27ec2a1b148c40ea13d541b4c7a96cef07901))
  * update googleapis/sdk-platform-java action to v2.58.0 ([#1806](https://github.com/googleapis/java-logging/issues/1806)) ([b94da77](https://github.com/googleapis/java-logging/commit/b94da779d8263ce6c1845bb8baa6a9e9aedc2ccf))
  * update googleapis/sdk-platform-java action to v2.60.0 ([#1822](https://github.com/googleapis/java-logging/issues/1822)) ([0a96dd5](https://github.com/googleapis/java-logging/commit/0a96dd52dc1594767b7dd60da99a17bac8ac14ba))
  * update googleapis/sdk-platform-java action to v2.62.1 ([#1855](https://github.com/googleapis/java-logging/issues/1855)) ([b6ce498](https://github.com/googleapis/java-logging/commit/b6ce4988391dba73e019aa9f597ce6cc23f81a8c))
  * update googleapis/sdk-platform-java action to v2.62.3 ([#1868](https://github.com/googleapis/java-logging/issues/1868)) ([cac5cd9](https://github.com/googleapis/java-logging/commit/cac5cd99e6a1738100248c9d235f4fa2987967d0))
  * update googleapis/sdk-platform-java action to v2.64.1 ([#1882](https://github.com/googleapis/java-logging/issues/1882)) ([abdd374](https://github.com/googleapis/java-logging/commit/abdd37434c76f615cdc9affb5d770970fbcbbf72))
  * update sdk platform java dependencies ([#1707](https://github.com/googleapis/java-logging/issues/1707)) ([2359040](https://github.com/googleapis/java-logging/commit/23590409f5c4aaff5c741e860fc0916f7ec4c963))
  * update sdk platform java dependencies ([#1717](https://github.com/googleapis/java-logging/issues/1717)) ([ee9ef91](https://github.com/googleapis/java-logging/commit/ee9ef91a9ebaed9faa5870a29be40b0c1531a226))
  * update sdk platform java dependencies ([#1725](https://github.com/googleapis/java-logging/issues/1725)) ([531f8c5](https://github.com/googleapis/java-logging/commit/531f8c5089a260840eee7ff97d315307f074f5e6))
  * update sdk platform java dependencies ([#1736](https://github.com/googleapis/java-logging/issues/1736)) ([88b4cdf](https://github.com/googleapis/java-logging/commit/88b4cdf71463285e50a815e0635d36301d583e4c))
  * update sdk-platform-java-config to 3.55.0-rc1 ([#1903](https://github.com/googleapis/java-logging/issues/1903)) ([750a9d7](https://github.com/googleapis/java-logging/commit/750a9d7ed49e1134a94cd88819398459b32a815a))



##### Documentation

  * Documentation update for OpenTelemetry and tracing ([#1657](https://github.com/googleapis/java-logging/issues/1657)) ([e3c6670](https://github.com/googleapis/java-logging/commit/e3c667094170ac7d404addc797facbe997ca51d3))
  * Fix typo in code comments ([#1520](https://github.com/googleapis/java-logging/issues/1520)) ([0440fc6](https://github.com/googleapis/java-logging/commit/0440fc6dfa3c5cd19f0d7d941af242872da1bbd3))



### Python

#### [3.13.0](https://github.com/googleapis/python-logging/compare/v3.12.1...v3.13.0) (2025-12-15)

##### Features

  * Add support for python 3.14 (#1065) ([6be3df6a](https://github.com/googleapis/python-logging/commit/6be3df6a))



##### Bug Fixes

  * remove setup.cfg configuration for creating universal wheels (#981) ([70f612c3](https://github.com/googleapis/python-logging/commit/70f612c3))



### Python

#### [3.13.0](https://github.com/googleapis/python-logging/compare/v3.12.1...v3.13.0) (2025-12-15)

##### Features

  * Add support for python 3.14 (#1065) ([6be3df6a](https://github.com/googleapis/python-logging/commit/6be3df6a))



##### Bug Fixes

  * remove setup.cfg configuration for creating universal wheels (#981) ([70f612c3](https://github.com/googleapis/python-logging/commit/70f612c3))



### Python

#### [3.13.0](https://github.com/googleapis/python-logging/compare/v3.12.1...v3.13.0) (2025-12-15)

##### Features

  * Add support for python 3.14 (#1065) ([6be3df6a](https://github.com/googleapis/python-logging/commit/6be3df6a))



##### Bug Fixes

  * remove setup.cfg configuration for creating universal wheels (#981) ([70f612c3](https://github.com/googleapis/python-logging/commit/70f612c3))



### Python

#### [3.13.0](https://github.com/googleapis/python-logging/compare/v3.12.1...v3.13.0) (2025-12-15)

##### Features

  * Add support for python 3.14 (#1065) ([6be3df6a](https://github.com/googleapis/python-logging/commit/6be3df6a))



##### Bug Fixes

  * remove setup.cfg configuration for creating universal wheels (#981) ([70f612c3](https://github.com/googleapis/python-logging/commit/70f612c3))



### Python

#### [3.13.0](https://github.com/googleapis/python-logging/compare/v3.12.1...v3.13.0) (2025-12-15)

##### Features

  * Add support for python 3.14 (#1065) ([6be3df6a](https://github.com/googleapis/python-logging/commit/6be3df6a))



##### Bug Fixes

  * remove setup.cfg configuration for creating universal wheels (#981) ([70f612c3](https://github.com/googleapis/python-logging/commit/70f612c3))



### Python

#### [3.13.0](https://github.com/googleapis/python-logging/compare/v3.12.1...v3.13.0) (2025-12-15)

##### Features

  * Add support for python 3.14 (#1065) ([6be3df6a](https://github.com/googleapis/python-logging/commit/6be3df6a))



##### Bug Fixes

  * remove setup.cfg configuration for creating universal wheels (#981) ([70f612c3](https://github.com/googleapis/python-logging/commit/70f612c3))



### Python

#### [3.13.0](https://github.com/googleapis/python-logging/compare/v3.12.1...v3.13.0) (2025-12-15)

##### Features

  * Add support for python 3.14 (#1065) ([6be3df6a](https://github.com/googleapis/python-logging/commit/6be3df6a))



##### Bug Fixes

  * remove setup.cfg configuration for creating universal wheels (#981) ([70f612c3](https://github.com/googleapis/python-logging/commit/70f612c3))



## December 16, 2025

**Cloud Monitoring**

v3

Other

On December 15, 2025, it was announced that your Application Monitoring dashboards will display the trace spans that are associated with your registered App Hub applications. Those dashboards don't display trace data. To view your trace data, use the Trace Explorer page.

## December 15, 2025

**Cloud Logging**

v2

Libraries

### Java

#### [3.23.9](https://github.com/googleapis/java-logging/compare/v3.23.8...v3.23.9) (2025-12-11)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.64.2 ([fcb7ec1](https://github.com/googleapis/java-logging/commit/fcb7ec1ba7ae7c9a041d68c76e7b72a7e0861cf7))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.54.2 ([#1897](https://github.com/googleapis/java-logging/issues/1897)) ([ab9862f](https://github.com/googleapis/java-logging/commit/ab9862f655bc89fa3e4e381567dcd0a9d8afdbf9))
  * Update googleapis/sdk-platform-java action to v2.64.2 ([#1898](https://github.com/googleapis/java-logging/issues/1898)) ([5860f51](https://github.com/googleapis/java-logging/commit/5860f516596686ef3054969b8c69de7eb48629e3))



**Cloud Monitoring**

v3

Feature

Your Application Monitoring dashboards now display the trace spans that are associated with your registered App Hub applications. The display includes annotations that let you identify services and workloads. You can also open the Trace Explorer page from your Application Monitoring dashboards. To learn more, see the following documents:

  * [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring).
  * [View application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring).
  * [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces) describes how to use the Trace Explorer page to filter and explore your trace data.



**Cloud Trace**

v2

Feature

The Trace Explorer has been updated to include annotations that let you identify App Hub-registered services and workloads. The link provided with a service or workload lets you open the corresponding Application Monitoring dashboard. To learn more, see the following documents:

  * [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces) describes how to use the Trace Explorer page to filter and explore your trace data.
  * [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring).
  * [View application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring) describes how to view the telemetry for a registered application.



## December 12, 2025

**Cloud Logging**

v2

Change

The default setting for the time-range selector for the Logs Explorer is now five minutes. The previous default was one hour.

## December 11, 2025

**Cloud Monitoring**

v3

Feature

You can now add a widget to a dashboard that lets you manage the settings for a variable. To learn more, see the following documents:

  * [Google Cloud console: Add widget to manage the value of a variable](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent#add-filter-control-widget)
  * [API: Dashboard with a FilterControl widget](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_filter_control)



Feature

The Google Cloud CLI (`gcloud`) commands to manage Cloud Monitoring alerting policies are now generally available. For more information, see [`gcloud monitoring policies`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies).

## December 08, 2025

**Cloud Logging**

v2

Feature

You can now install and manage the Ops Agent on virtual machines in a specified zone by using VM Extension Manager extension policies. You can use extension policies to keep the installed version of the agent current, keep a specified version of the agent installed, and other tasks. For more information, see [Install and manage the Ops Agent by using VM Extension Manager policies](https://docs.cloud.google.com/logging/docs/agent/ops-agent/agent-vmem-policies).

**Cloud Monitoring**

v3

Feature

You can now install and manage the Ops Agent on virtual machines in a specified zone by using VM Extension Manager extension policies. You can use extension policies to keep the installed version of the agent current, keep a specified version of the agent installed, and other tasks. For more information, see [Install and manage the Ops Agent by using VM Extension Manager policies](https://docs.cloud.google.com/monitoring/agent/ops-agent/agent-vmem-policies).

## November 17, 2025

**Cloud Logging**

v2

Libraries

### Java

#### [3.23.8](https://github.com/googleapis/java-logging/compare/v3.23.7...v3.23.8) (2025-11-13)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.64.1 ([9187dcd](https://github.com/googleapis/java-logging/commit/9187dcd1314a6be4df8f8c6eed95092724c6da69))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.54.1 ([#1883](https://github.com/googleapis/java-logging/issues/1883)) ([acc56db](https://github.com/googleapis/java-logging/commit/acc56db1ea0389ca91a09e435662b802db63abe6))
  * Update googleapis/sdk-platform-java action to v2.64.1 ([#1882](https://github.com/googleapis/java-logging/issues/1882)) ([abdd374](https://github.com/googleapis/java-logging/commit/abdd37434c76f615cdc9affb5d770970fbcbbf72))



### Java

#### [3.23.8](https://github.com/googleapis/java-logging/compare/v3.23.7...v3.23.8) (2025-11-13)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.64.1 ([9187dcd](https://github.com/googleapis/java-logging/commit/9187dcd1314a6be4df8f8c6eed95092724c6da69))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.54.1 ([#1883](https://github.com/googleapis/java-logging/issues/1883)) ([acc56db](https://github.com/googleapis/java-logging/commit/acc56db1ea0389ca91a09e435662b802db63abe6))
  * Update googleapis/sdk-platform-java action to v2.64.1 ([#1882](https://github.com/googleapis/java-logging/issues/1882)) ([abdd374](https://github.com/googleapis/java-logging/commit/abdd37434c76f615cdc9affb5d770970fbcbbf72))



## November 06, 2025

**Cloud Trace**

v2

Feature

You can now collect, view, and analyze prompts and responses from your agentic applications when they are built with the Agent Development Kit (ADK). This feature is in Public Preview.

[Collect and view multimodal prompts and responses](https://docs.cloud.google.com/trace/docs/collect-view-multimodal-prompts-responses) describes how to do the following:

  * Configure your project and ADK to collect multimodal data.
  * View a conversation and the multimodal data by using the Trace Explorer.
  * Find log entries that contain references to multimodal data.
  * Query your prompts and responses by using BigQuery.
  * Evaluate your prompts and responses by using the Vertex AI SDK for Python.



## November 04, 2025

**Cloud Monitoring**

v3

Feature

You can now view the topology for applications that you register with App Hub. The topology map provides a graphical view of the relationships between the services and workloads in your App Hub application. The topology map also displays alerts and traffic latency, which can help you understand how your application is performing and diagnose issues. This feature is in Public Preview.

To learn more, see the following:

  * [View application topology](https://docs.cloud.google.com/monitoring/docs/application-topology)
  * [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring)



## November 03, 2025

**Cloud Logging**

v2

Libraries

### Go

#### [1.13.1](https://github.com/googleapis/google-cloud-go/compare/logging/v1.13.0...logging/v1.13.1) (2025-10-28)

##### Bug Fixes

  * **logging:** Upgrade gRPC service registration func ([486bd40](https://github.com/googleapis/google-cloud-go/commit/486bd406336fe91eae7c9040f2496ebfc8aee342))
  * **logging:** Upgrade gRPC service registration func ([#13139](https://github.com/googleapis/google-cloud-go/issues/13139)) ([39af2f9](https://github.com/googleapis/google-cloud-go/commit/39af2f9683b76ab290cc66b009ddc366fe63986b))



### Go

#### [1.13.1](https://github.com/googleapis/google-cloud-go/compare/logging/v1.13.0...logging/v1.13.1) (2025-10-28)

##### Bug Fixes

  * **logging:** Upgrade gRPC service registration func ([486bd40](https://github.com/googleapis/google-cloud-go/commit/486bd406336fe91eae7c9040f2496ebfc8aee342))
  * **logging:** Upgrade gRPC service registration func ([#13139](https://github.com/googleapis/google-cloud-go/issues/13139)) ([39af2f9](https://github.com/googleapis/google-cloud-go/commit/39af2f9683b76ab290cc66b009ddc366fe63986b))



### Go

#### [1.13.1](https://github.com/googleapis/google-cloud-go/compare/logging/v1.13.0...logging/v1.13.1) (2025-10-28)

##### Bug Fixes

  * **logging:** Upgrade gRPC service registration func ([486bd40](https://github.com/googleapis/google-cloud-go/commit/486bd406336fe91eae7c9040f2496ebfc8aee342))
  * **logging:** Upgrade gRPC service registration func ([#13139](https://github.com/googleapis/google-cloud-go/issues/13139)) ([39af2f9](https://github.com/googleapis/google-cloud-go/commit/39af2f9683b76ab290cc66b009ddc366fe63986b))



## October 27, 2025

**Cloud Logging**

v2

Libraries

### Java

#### [3.23.7](https://github.com/googleapis/java-logging/compare/v3.23.6...v3.23.7) (2025-10-20)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.63.0 ([385a1dc](https://github.com/googleapis/java-logging/commit/385a1dc67fcdd8706238ba2f95f694bbb647f5f8))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.53.0 ([#1875](https://github.com/googleapis/java-logging/issues/1875)) ([b79fd2b](https://github.com/googleapis/java-logging/commit/b79fd2b0cd2c358e3d3e69ddc76fcbfa16a47b5b))



### Java

#### [3.23.7](https://github.com/googleapis/java-logging/compare/v3.23.6...v3.23.7) (2025-10-20)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.63.0 ([385a1dc](https://github.com/googleapis/java-logging/commit/385a1dc67fcdd8706238ba2f95f694bbb647f5f8))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.53.0 ([#1875](https://github.com/googleapis/java-logging/issues/1875)) ([b79fd2b](https://github.com/googleapis/java-logging/commit/b79fd2b0cd2c358e3d3e69ddc76fcbfa16a47b5b))



### Java

#### [3.23.7](https://github.com/googleapis/java-logging/compare/v3.23.6...v3.23.7) (2025-10-20)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.63.0 ([385a1dc](https://github.com/googleapis/java-logging/commit/385a1dc67fcdd8706238ba2f95f694bbb647f5f8))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.53.0 ([#1875](https://github.com/googleapis/java-logging/issues/1875)) ([b79fd2b](https://github.com/googleapis/java-logging/commit/b79fd2b0cd2c358e3d3e69ddc76fcbfa16a47b5b))



## October 23, 2025

**Cloud Monitoring**

v3

Feature

You can now use the Google Cloud CLI and the Cloud Monitoring API to list incidents and get incident details. This feature is in Public Preview. For more information, see the following pages:

  * [Incidents for metric-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/incidents-events)
  * [`gcloud` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/alerts)
  * [API documentation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts)



## October 13, 2025

**Cloud Logging**

v2

Libraries

### Java

#### [3.23.6](https://github.com/googleapis/java-logging/compare/v3.23.5...v3.23.6) (2025-10-08)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.62.3 ([5d5d8a7](https://github.com/googleapis/java-logging/commit/5d5d8a76c58c3329f90e4fa84f5e81a1d3296894))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.52.3 ([#1869](https://github.com/googleapis/java-logging/issues/1869)) ([94405fa](https://github.com/googleapis/java-logging/commit/94405fa929c48db114dd10ae39a0f3e520865bbf))
  * Update googleapis/sdk-platform-java action to v2.62.3 ([#1868](https://github.com/googleapis/java-logging/issues/1868)) ([cac5cd9](https://github.com/googleapis/java-logging/commit/cac5cd99e6a1738100248c9d235f4fa2987967d0))



## October 09, 2025

**Cloud Logging**

v2

Feature

The query builder in the Log Analytics page is [generally available](https://docs.cloud.google.com/products#product-launch-stages) (GA). For more information, see [Build, edit, and run a query](https://docs.cloud.google.com/logging/docs/analyze/query-and-view#query-builder).

## October 02, 2025

**Cloud Monitoring**

v3

Feature

Application Monitoring is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages). Application Monitoring lets you monitor the resources and infrastructure from the perspective of an [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) application. The out-of-the-box dashboards that Application Monitoring creates can help you understand how your application's resources are performing, and they can help you diagnose issues.

  * [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring) provides a brief overview of this feature.
  * [Set up application monitoring](https://docs.cloud.google.com/monitoring/docs/setup-application-monitoring) describes how to configure an observability scope so that you have an aggregated view of your log, metric, and trace data.
  * [View application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring) describes the labels attached to your telemetry data and provides guidance about how to explore the OOTB dashboards.
  * [Supported infrastructure](https://docs.cloud.google.com/monitoring/docs/application-monitoring-services).



## September 29, 2025

**Cloud Logging**

v2

Libraries

### Java

#### [3.23.5](https://github.com/googleapis/java-logging/compare/v3.23.4...v3.23.5) (2025-09-24)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.62.2 ([eeca440](https://github.com/googleapis/java-logging/commit/eeca440da06c24afc07e669f6f087246d91cd933))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.52.2 ([#1858](https://github.com/googleapis/java-logging/issues/1858)) ([0252352](https://github.com/googleapis/java-logging/commit/0252352ca34dd494c4471f3a90391df762d676df))



## September 22, 2025

**Cloud Logging**

v2

Announcement

Cloud Logging has removed the quota for write requests per minute, which has been replaced by volume-based regional quotas. We've also removed the references to August dates for the removal of the old quota from the public documentation. For more information, see [Logging API quotas and limits](https://cloud.google.com/logging/quotas#api-limits).

## September 15, 2025

**Cloud Logging**

v2

Libraries

### Java

#### [3.23.4](https://github.com/googleapis/java-logging/compare/v3.23.3...v3.23.4) (2025-09-11)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.62.1 ([1438bff](https://github.com/googleapis/java-logging/commit/1438bff5bc7028fbf125895f0bdd2bb50490effa))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 ([#1853](https://github.com/googleapis/java-logging/issues/1853)) ([c21a635](https://github.com/googleapis/java-logging/commit/c21a635f054b1cd8a6e5aea7450017af85ba03c7))
  * Update googleapis/sdk-platform-java action to v2.62.1 ([#1855](https://github.com/googleapis/java-logging/issues/1855)) ([b6ce498](https://github.com/googleapis/java-logging/commit/b6ce4988391dba73e019aa9f597ce6cc23f81a8c))



**Cloud Monitoring**

v3

Feature

When viewing a chart, you can now open a flyout that displays the chart and related log entries. To explore your metric and log data in more detail, you can then use the toolbars and menus in the flyout. To learn more, see the following:

  * [Correlate metric and log data](https://docs.cloud.google.com/monitoring/charts/working-with-charts#correlate-telemetry)
  * [Explore application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring#explore-application)



## September 08, 2025

**Cloud Logging**

v2

Libraries

### Node.js

#### [11.2.1](https://github.com/googleapis/nodejs-logging/compare/v11.2.0...v11.2.1) (2025-09-03)

##### Bug Fixes

  * **logging:** Specifying resourceNames should fetch logs only from those resources ([#1597](https://github.com/googleapis/nodejs-logging/issues/1597)) ([ff7899f](https://github.com/googleapis/nodejs-logging/commit/ff7899f5e91da6540d3f68476b2d9acd58ff0993))



## August 27, 2025

**Cloud Trace**

v2

Feature

You can now create and manage the trace scope programmatically. This feature is in Public Preview. For more information, see the following documents:

  * [Create and manage trace scopes](https://docs.cloud.google.com/trace/docs/trace-scope/create-and-manage)
  * [Trace scopes API overview](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.traceScopes)



## August 25, 2025

**Cloud Logging**

v2

Libraries

### Java

#### [3.23.3](https://github.com/googleapis/java-logging/compare/v3.23.2...v3.23.3) (2025-08-20)

##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.52.0 ([#1848](https://github.com/googleapis/java-logging/issues/1848)) ([162ef56](https://github.com/googleapis/java-logging/commit/162ef563793270c236ecf7ca2524ad3b560d7a12))



**Cloud Monitoring**

v3

Feature

Your Application Monitoring dashboards will display latency, error rates, and traffic level for workloads deployed on Google Kubernetes Engine, when you instrument your application with OpenTelemetry. To learn more, see [Instrument an application for Application Monitoring](https://cloud.google.com/monitoring/docs/instrument-for-application-monitoring).

## August 21, 2025

**Cloud Monitoring**

v3

Feature

The following infrastructure is now integrated with Application Monitoring, which is in public preview.

  * AlloyDB for PostgreSQL clusters and services
  * Bigtable clusters and services
  * Dataproc Metastore services
  * Cloud Deploy delivery pipelines
  * Firestore databases
  * Secret Manager secrets



To learn more, see [Application Monitoring overview](https://cloud.google.com/monitoring/docs/about-application-monitoring) and [Supported infrastructure](https://cloud.google.com/monitoring/docs/application-monitoring-services).

## August 11, 2025

**Cloud Logging**

v2

Libraries

### Java

#### [3.23.2](https://github.com/googleapis/java-logging/compare/v3.23.1...v3.23.2) (2025-08-05)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.61.0 ([0a21b83](https://github.com/googleapis/java-logging/commit/0a21b83377e6e6a2f4cf98149424a47dcd490c1c))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 ([#1843](https://github.com/googleapis/java-logging/issues/1843)) ([975d8ae](https://github.com/googleapis/java-logging/commit/975d8aeca38ff2f2f8317df93a661910969c5fc1))



### Java

#### [3.23.2](https://github.com/googleapis/java-logging/compare/v3.23.1...v3.23.2) (2025-08-05)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.61.0 ([0a21b83](https://github.com/googleapis/java-logging/commit/0a21b83377e6e6a2f4cf98149424a47dcd490c1c))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 ([#1843](https://github.com/googleapis/java-logging/issues/1843)) ([975d8ae](https://github.com/googleapis/java-logging/commit/975d8aeca38ff2f2f8317df93a661910969c5fc1))



### Java

#### [3.23.2](https://github.com/googleapis/java-logging/compare/v3.23.1...v3.23.2) (2025-08-05)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.61.0 ([0a21b83](https://github.com/googleapis/java-logging/commit/0a21b83377e6e6a2f4cf98149424a47dcd490c1c))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 ([#1843](https://github.com/googleapis/java-logging/issues/1843)) ([975d8ae](https://github.com/googleapis/java-logging/commit/975d8aeca38ff2f2f8317df93a661910969c5fc1))



## August 05, 2025

**Cloud Monitoring**

v3

Feature

You can now use the [`time_series_billed_for_queries_count`](https://cloud.google.com/monitoring/api/metrics_gcp_i_o#monitoring/billing/time_series_billed_for_queries_count) metric to estimate charges based on the number of time series that have been queried. For more information, see [View the number of time series billed for queries](https://cloud.google.com/stackdriver/estimating-bills#mon-billable-api-reads).

Billing by time series queried isn't enforced until October 2, 2025. For more information, see [Cloud Monitoring pricing summary](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary).

## August 04, 2025

**Cloud Logging**

v2

Libraries

### Java

#### [3.23.1](https://github.com/googleapis/java-logging/compare/v3.23.0...v3.23.1) (2025-07-28)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 ([6a268f8](https://github.com/googleapis/java-logging/commit/6a268f8dbb33b38fa5e4d35d8dfcd196f8fcf9db))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 ([#1834](https://github.com/googleapis/java-logging/issues/1834)) ([2e46f6e](https://github.com/googleapis/java-logging/commit/2e46f6ef44278af5031167106c216dcdb0a16357))



### Java

#### [3.23.1](https://github.com/googleapis/java-logging/compare/v3.23.0...v3.23.1) (2025-07-28)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 ([6a268f8](https://github.com/googleapis/java-logging/commit/6a268f8dbb33b38fa5e4d35d8dfcd196f8fcf9db))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 ([#1834](https://github.com/googleapis/java-logging/issues/1834)) ([2e46f6e](https://github.com/googleapis/java-logging/commit/2e46f6ef44278af5031167106c216dcdb0a16357))



### Java

#### [3.23.1](https://github.com/googleapis/java-logging/compare/v3.23.0...v3.23.1) (2025-07-28)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 ([6a268f8](https://github.com/googleapis/java-logging/commit/6a268f8dbb33b38fa5e4d35d8dfcd196f8fcf9db))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 ([#1834](https://github.com/googleapis/java-logging/issues/1834)) ([2e46f6e](https://github.com/googleapis/java-logging/commit/2e46f6ef44278af5031167106c216dcdb0a16357))



### Java

#### [3.23.1](https://github.com/googleapis/java-logging/compare/v3.23.0...v3.23.1) (2025-07-28)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 ([6a268f8](https://github.com/googleapis/java-logging/commit/6a268f8dbb33b38fa5e4d35d8dfcd196f8fcf9db))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 ([#1834](https://github.com/googleapis/java-logging/issues/1834)) ([2e46f6e](https://github.com/googleapis/java-logging/commit/2e46f6ef44278af5031167106c216dcdb0a16357))



Feature

You can now build queries without manually writing SQL in the Log Analytics page by using the query builder. This feature is in Public Preview. For more information, see [Build and run a SQL query](https://docs.cloud.google.com/logging/docs/analyze/query-and-view#query-builder).

## July 24, 2025

**Cloud Monitoring**

v3

Feature

You can now monitor and understand the costs and utilization of resources in your Google Cloud project or App Hub application by using the Cost Explorer. This feature is in Public Preview. For more information, see [Optimize costs with the Cost Explorer](https://cloud.google.com//stackdriver/docs/costs/optimize-costs).

## July 17, 2025

**Cloud Monitoring**

v3

Feature

Application-specific resource attributes are attached to your trace data when your App Hub applications use supported Google Cloud resources, or when you instrument an application with OpenTelemetry and use the Google Cloud Telemetry endpoint. To learn more, see the following:

  * [Application Monitoring overview](https://cloud.google.com/monitoring/docs/about-application-monitoring)
  * [View application telemetry](https://cloud.google.com/monitoring/docs/application-monitoring)
  * [Find and explore traces](https://cloud.google.com/trace/docs/finding-traces)
  * [Telemetry (OTLP) API overview](https://cloud.google.com/stackdriver/docs/reference/telemetry/overview)



**Cloud Trace**

v2

Feature

Application-specific resource attributes are attached to your trace data when your App Hub applications use supported Google Cloud resources, or when you instrument an application with OpenTelemetry and use the Google Cloud Telemetry endpoint. You can use the Trace Explorer to filter by your application, your service, or your workload. To learn more, see the following:

  * [Find and explore traces](https://cloud.google.com/trace/docs/finding-traces)
  * [Application Monitoring overview](https://cloud.google.com/monitoring/docs/about-application-monitoring)
  * [View application telemetry](https://cloud.google.com/monitoring/docs/application-monitoring)
  * [Telemetry (OTLP) API overview](https://cloud.google.com/stackdriver/docs/reference/telemetry/overview)



## July 14, 2025

**Cloud Logging**

v2

Libraries

### Java

#### [3.23.0](https://github.com/googleapis/java-logging/compare/v3.22.6...v3.23.0) (2025-07-11)

##### Features

  * Next release from main branch is 3.23.0 ([#1826](https://github.com/googleapis/java-logging/issues/1826)) ([f0ef15f](https://github.com/googleapis/java-logging/commit/f0ef15f609a3400460bd8074bdd05014cc388743))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.1 ([#1828](https://github.com/googleapis/java-logging/issues/1828)) ([44c3094](https://github.com/googleapis/java-logging/commit/44c3094e23450f1a8e6bb397f209b17cf37a4345))



### Java

#### [3.23.0](https://github.com/googleapis/java-logging/compare/v3.22.6...v3.23.0) (2025-07-11)

##### Features

  * Next release from main branch is 3.23.0 ([#1826](https://github.com/googleapis/java-logging/issues/1826)) ([f0ef15f](https://github.com/googleapis/java-logging/commit/f0ef15f609a3400460bd8074bdd05014cc388743))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.1 ([#1828](https://github.com/googleapis/java-logging/issues/1828)) ([44c3094](https://github.com/googleapis/java-logging/commit/44c3094e23450f1a8e6bb397f209b17cf37a4345))



## June 30, 2025

**Cloud Logging**

v2

Libraries

### Java

#### [3.22.6](https://github.com/googleapis/java-logging/compare/v3.22.5...v3.22.6) (2025-06-25)

##### Bug Fixes

  * Regenerate gapic yaml and service yaml for logging by augmentation configs ([9023895](https://github.com/googleapis/java-logging/commit/9023895fd56381c1f4309843a269975763a89d40))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.0 ([#1821](https://github.com/googleapis/java-logging/issues/1821)) ([af4edc5](https://github.com/googleapis/java-logging/commit/af4edc5b1399b3563d9cf07e171c4281fde2bb79))
  * Update googleapis/sdk-platform-java action to v2.60.0 ([#1822](https://github.com/googleapis/java-logging/issues/1822)) ([0a96dd5](https://github.com/googleapis/java-logging/commit/0a96dd52dc1594767b7dd60da99a17bac8ac14ba))



### Java

#### [3.22.6](https://github.com/googleapis/java-logging/compare/v3.22.5...v3.22.6) (2025-06-25)

##### Bug Fixes

  * Regenerate gapic yaml and service yaml for logging by augmentation configs ([9023895](https://github.com/googleapis/java-logging/commit/9023895fd56381c1f4309843a269975763a89d40))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.0 ([#1821](https://github.com/googleapis/java-logging/issues/1821)) ([af4edc5](https://github.com/googleapis/java-logging/commit/af4edc5b1399b3563d9cf07e171c4281fde2bb79))
  * Update googleapis/sdk-platform-java action to v2.60.0 ([#1822](https://github.com/googleapis/java-logging/issues/1822)) ([0a96dd5](https://github.com/googleapis/java-logging/commit/0a96dd52dc1594767b7dd60da99a17bac8ac14ba))



## June 13, 2025

**Cloud Trace**

v2

Change

The **Analysis reports** page has been removed. To analyze your trace data, use the **Trace explorer** page. You can use filters and the time-range selector to view and analyze historical data.

## June 09, 2025

**Cloud Logging**

v2

Libraries

### Java

#### [3.22.5](https://github.com/googleapis/java-logging/compare/v3.22.4...v3.22.5) (2025-06-05)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.59.0 ([f2362fb](https://github.com/googleapis/java-logging/commit/f2362fb4c05d34fda4a1c9788ea87822ac887d9e))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.49.0 ([#1813](https://github.com/googleapis/java-logging/issues/1813)) ([c15da84](https://github.com/googleapis/java-logging/commit/c15da84716d6d554ae26919412e8d4313fd980bc))



## June 06, 2025

**Cloud Logging**

v2

Announcement

Cloud Logging begins enforcement of the new volume-based regional quotas. For more information, see [Logging API quotas and limits](https://docs.cloud.google.com/logging/quotas#api-limits).

## June 04, 2025

**Cloud Logging**

v2

Feature

You can now cancel a running query in the Logs Explorer by clicking the **Stop query** button.

## June 02, 2025

**Cloud Monitoring**

v3

Feature

You can now add treemap widgets to your custom dashboards. Treemaps display the most recent value of aggregated data as a series of nested rectangles, the color saturation of a rectangle is proportional to the represented value. For more information, see the following:

  * [Display the most recent value as a treemap](https://cloud.google.com/monitoring/charts#dashboard_with_a_treemap_widget)
  * [API: Dashboard with a Treemap widget](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_a_treemap_widget)



## May 29, 2025

**Cloud Logging**

v2

Feature

You can now configure the observability scope or set the default log scope by using the Google Cloud CLI. You must use version 254.0 or higher. For more information, see [Configure observability scopes](https://docs.cloud.google.com/stackdriver/docs/scopes/configure) and [Set the default log scope](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage#set-default).

## May 27, 2025

**Cloud Trace**

v2

Feature

Learn how to instrument your generative AI applications by using OpenTelemetry and the LangGraph framework to collect information about the actions taken by your AI agent. You can view generative AI events by using the **Trace Explorer** :

  * [Instrument generative AI applications](https://cloud.google.com/stackdriver/docs/instrumentation/ai-agent-overview)
  * [Instrument a LangGraph ReAct Agent with OpenTelemetry](https://cloud.google.com/stackdriver/docs/instrumentation/ai-agent-langgraph)
  * [View generative AI events](https://cloud.google.com/trace/docs/finding-traces#view_generative_ai_events)



## May 26, 2025

**Cloud Logging**

v2

Libraries

### Java

#### [3.22.4](https://github.com/googleapis/java-logging/compare/v3.22.3...v3.22.4) (2025-05-20)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.58.0 ([45b4878](https://github.com/googleapis/java-logging/commit/45b4878eeec35f8c19a3cd3cd33331e9ece6b5c6))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.48.0 ([#1808](https://github.com/googleapis/java-logging/issues/1808)) ([6327c51](https://github.com/googleapis/java-logging/commit/6327c51f3a8ecfb7af678c8c040b066e7f938863))
  * Update googleapis/sdk-platform-java action to v2.58.0 ([#1806](https://github.com/googleapis/java-logging/issues/1806)) ([b94da77](https://github.com/googleapis/java-logging/commit/b94da779d8263ce6c1845bb8baa6a9e9aedc2ccf))



## May 12, 2025

**Cloud Logging**

v2

Libraries

### Java

#### [3.22.3](https://github.com/googleapis/java-logging/compare/v3.22.2...v3.22.3) (2025-05-06)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.56.3 ([844f4fa](https://github.com/googleapis/java-logging/commit/844f4fa48f878a7da77ff9ab13652dc93f079920))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.46.3 ([#1801](https://github.com/googleapis/java-logging/issues/1801)) ([d7aa7bc](https://github.com/googleapis/java-logging/commit/d7aa7bcd4e1235491f30ab4dd88ff80c07966185))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.47.0 ([#1803](https://github.com/googleapis/java-logging/issues/1803)) ([5967ffe](https://github.com/googleapis/java-logging/commit/5967ffe459d9e1d00a36727ae433303005bf15d8))
  * Update googleapis/sdk-platform-java action to v2.57.0 ([#1804](https://github.com/googleapis/java-logging/issues/1804)) ([e9a27ec](https://github.com/googleapis/java-logging/commit/e9a27ec2a1b148c40ea13d541b4c7a96cef07901))



### Java

#### [3.22.3](https://github.com/googleapis/java-logging/compare/v3.22.2...v3.22.3) (2025-05-06)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.56.3 ([844f4fa](https://github.com/googleapis/java-logging/commit/844f4fa48f878a7da77ff9ab13652dc93f079920))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.46.3 ([#1801](https://github.com/googleapis/java-logging/issues/1801)) ([d7aa7bc](https://github.com/googleapis/java-logging/commit/d7aa7bcd4e1235491f30ab4dd88ff80c07966185))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.47.0 ([#1803](https://github.com/googleapis/java-logging/issues/1803)) ([5967ffe](https://github.com/googleapis/java-logging/commit/5967ffe459d9e1d00a36727ae433303005bf15d8))
  * Update googleapis/sdk-platform-java action to v2.57.0 ([#1804](https://github.com/googleapis/java-logging/issues/1804)) ([e9a27ec](https://github.com/googleapis/java-logging/commit/e9a27ec2a1b148c40ea13d541b4c7a96cef07901))



## May 08, 2025

**Cloud Logging**

v2

Feature

Log Analytics can now automatically infer fields of a column when the data type is JSON. You can also view how often these inferred fields appear in your data.

## May 07, 2025

**Cloud Monitoring**

v3

Issue

Version 2.56.0 of the Ops Agent using the Prometheus receiver can fail to send metrics and report negative start times. To resolve this issue, downgrade to version 2.55.0. For more information, see [Known issue: Ops Agent version 2.56.0 fails to send metrics](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-run-ingest#known-2.56.0-issue).

## May 06, 2025

**Cloud Monitoring**

v3

Feature

When you create a snooze for a single alerting policy, you can now use resource, metric, and metadata label types to filter applicable incidents. For more information, see [Create a snooze](https://cloud.google.com/monitoring/alerts/manage-snooze#create).

## May 02, 2025

**Cloud Monitoring**

v3

Change

The limit for the number of widgets on a custom dashboard has increased to 100, from 40. For information about dashboards, see the following:

  * [Create and manage custom dashboards](https://cloud.google.com/monitoring/charts/dashboards)
  * [Install a dashboard template](https://cloud.google.com/monitoring/dashboards/dashboard-templates)
  * [Import Grafana dashboards](https://cloud.google.com/monitoring/dashboards/import-grafana-dashboards)



## April 28, 2025

**Cloud Logging**

v2

Libraries

### Python

#### [3.12.1](https://github.com/googleapis/python-logging/compare/v3.12.0...v3.12.1) (2025-04-21)

##### Bug Fixes

  * Make logging handler close conditional to having the transport opened ([#990](https://github.com/googleapis/python-logging/issues/990)) ([66c6b91](https://github.com/googleapis/python-logging/commit/66c6b91725eb479a0af138a2be13f3c25f369d7e))



### Java

#### [3.22.2](https://github.com/googleapis/java-logging/compare/v3.22.1...v3.22.2) (2025-04-25)

##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.46.2 ([#1796](https://github.com/googleapis/java-logging/issues/1796)) ([1f88271](https://github.com/googleapis/java-logging/commit/1f882712aeb7e48a2339ffbad783813e11e74401))



### Python

#### [3.12.1](https://github.com/googleapis/python-logging/compare/v3.12.0...v3.12.1) (2025-04-21)

##### Bug Fixes

  * Make logging handler close conditional to having the transport opened ([#990](https://github.com/googleapis/python-logging/issues/990)) ([66c6b91](https://github.com/googleapis/python-logging/commit/66c6b91725eb479a0af138a2be13f3c25f369d7e))



### Java

#### [3.22.1](https://github.com/googleapis/java-logging/compare/v3.22.0...v3.22.1) (2025-04-25)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.56.2 ([7cce5b5](https://github.com/googleapis/java-logging/commit/7cce5b509c904209f0a92e239e836afac4169ec4))



### Python

#### [3.12.1](https://github.com/googleapis/python-logging/compare/v3.12.0...v3.12.1) (2025-04-21)

##### Bug Fixes

  * Make logging handler close conditional to having the transport opened ([#990](https://github.com/googleapis/python-logging/issues/990)) ([66c6b91](https://github.com/googleapis/python-logging/commit/66c6b91725eb479a0af138a2be13f3c25f369d7e))



### Python

#### [3.12.1](https://github.com/googleapis/python-logging/compare/v3.12.0...v3.12.1) (2025-04-21)

##### Bug Fixes

  * Make logging handler close conditional to having the transport opened ([#990](https://github.com/googleapis/python-logging/issues/990)) ([66c6b91](https://github.com/googleapis/python-logging/commit/66c6b91725eb479a0af138a2be13f3c25f369d7e))



### Python

#### [3.12.1](https://github.com/googleapis/python-logging/compare/v3.12.0...v3.12.1) (2025-04-21)

##### Bug Fixes

  * Make logging handler close conditional to having the transport opened ([#990](https://github.com/googleapis/python-logging/issues/990)) ([66c6b91](https://github.com/googleapis/python-logging/commit/66c6b91725eb479a0af138a2be13f3c25f369d7e))



### Python

#### [3.12.1](https://github.com/googleapis/python-logging/compare/v3.12.0...v3.12.1) (2025-04-21)

##### Bug Fixes

  * Make logging handler close conditional to having the transport opened ([#990](https://github.com/googleapis/python-logging/issues/990)) ([66c6b91](https://github.com/googleapis/python-logging/commit/66c6b91725eb479a0af138a2be13f3c25f369d7e))



### Python

#### [3.12.1](https://github.com/googleapis/python-logging/compare/v3.12.0...v3.12.1) (2025-04-21)

##### Bug Fixes

  * Make logging handler close conditional to having the transport opened ([#990](https://github.com/googleapis/python-logging/issues/990)) ([66c6b91](https://github.com/googleapis/python-logging/commit/66c6b91725eb479a0af138a2be13f3c25f369d7e))



### Python

#### [3.12.1](https://github.com/googleapis/python-logging/compare/v3.12.0...v3.12.1) (2025-04-21)

##### Bug Fixes

  * Make logging handler close conditional to having the transport opened ([#990](https://github.com/googleapis/python-logging/issues/990)) ([66c6b91](https://github.com/googleapis/python-logging/commit/66c6b91725eb479a0af138a2be13f3c25f369d7e))



### Python

#### [3.12.1](https://github.com/googleapis/python-logging/compare/v3.12.0...v3.12.1) (2025-04-21)

##### Bug Fixes

  * Make logging handler close conditional to having the transport opened ([#990](https://github.com/googleapis/python-logging/issues/990)) ([66c6b91](https://github.com/googleapis/python-logging/commit/66c6b91725eb479a0af138a2be13f3c25f369d7e))



Libraries

### Java

#### [3.22.2](https://github.com/googleapis/java-logging/compare/v3.22.1...v3.22.2) (2025-04-25)

##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.46.2 ([#1796](https://github.com/googleapis/java-logging/issues/1796)) ([1f88271](https://github.com/googleapis/java-logging/commit/1f882712aeb7e48a2339ffbad783813e11e74401))



Libraries

### Java

#### [3.22.1](https://github.com/googleapis/java-logging/compare/v3.22.0...v3.22.1) (2025-04-25)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.56.2 ([7cce5b5](https://github.com/googleapis/java-logging/commit/7cce5b509c904209f0a92e239e836afac4169ec4))



## April 21, 2025

**Cloud Logging**

v2

Libraries

### Python

#### [3.12.0](https://github.com/googleapis/python-logging/compare/v3.11.4...v3.12.0) (2025-04-10)

##### Features

  * Add REST Interceptors which support reading metadata ([681bcc5](https://github.com/googleapis/python-logging/commit/681bcc5c1f983bb5a43e1d5ebcdb14e5e3f25a77))
  * Add support for opt-in debug logging ([681bcc5](https://github.com/googleapis/python-logging/commit/681bcc5c1f983bb5a43e1d5ebcdb14e5e3f25a77))
  * Added flushes/close functionality to logging handlers ([#917](https://github.com/googleapis/python-logging/issues/917)) ([d179304](https://github.com/googleapis/python-logging/commit/d179304b344277e349456f72cd90c56f28011286))



##### Bug Fixes

  * Allow protobuf 6.x ([#977](https://github.com/googleapis/python-logging/issues/977)) ([6757890](https://github.com/googleapis/python-logging/commit/675789001344fdae68ee20ec14e14c11c83a0433))
  * **deps:** Require google-cloud-audit-log >= 0.3.1 ([#979](https://github.com/googleapis/python-logging/issues/979)) ([1cc00ec](https://github.com/googleapis/python-logging/commit/1cc00ecf646a7a36eb32afd2e5df3d9aa7f564b1))
  * Fix typing issue with gRPC metadata when key ends in -bin ([681bcc5](https://github.com/googleapis/python-logging/commit/681bcc5c1f983bb5a43e1d5ebcdb14e5e3f25a77))



##### Documentation

  * Added documentation on log_level and excluded_loggers params in setup_logging ([#971](https://github.com/googleapis/python-logging/issues/971)) ([70d9d25](https://github.com/googleapis/python-logging/commit/70d9d25bf8c3c85a3c5523ecc7fbdbf72f08c583))
  * Update README to break infinite redirect loop ([#972](https://github.com/googleapis/python-logging/issues/972)) ([52cd907](https://github.com/googleapis/python-logging/commit/52cd907bb313df2766ec11e3d24c7e10cda31ca7))



### Python

#### [3.12.0](https://github.com/googleapis/python-logging/compare/v3.11.4...v3.12.0) (2025-04-10)

##### Features

  * Add REST Interceptors which support reading metadata ([681bcc5](https://github.com/googleapis/python-logging/commit/681bcc5c1f983bb5a43e1d5ebcdb14e5e3f25a77))
  * Add support for opt-in debug logging ([681bcc5](https://github.com/googleapis/python-logging/commit/681bcc5c1f983bb5a43e1d5ebcdb14e5e3f25a77))
  * Added flushes/close functionality to logging handlers ([#917](https://github.com/googleapis/python-logging/issues/917)) ([d179304](https://github.com/googleapis/python-logging/commit/d179304b344277e349456f72cd90c56f28011286))



##### Bug Fixes

  * Allow protobuf 6.x ([#977](https://github.com/googleapis/python-logging/issues/977)) ([6757890](https://github.com/googleapis/python-logging/commit/675789001344fdae68ee20ec14e14c11c83a0433))
  * **deps:** Require google-cloud-audit-log >= 0.3.1 ([#979](https://github.com/googleapis/python-logging/issues/979)) ([1cc00ec](https://github.com/googleapis/python-logging/commit/1cc00ecf646a7a36eb32afd2e5df3d9aa7f564b1))
  * Fix typing issue with gRPC metadata when key ends in -bin ([681bcc5](https://github.com/googleapis/python-logging/commit/681bcc5c1f983bb5a43e1d5ebcdb14e5e3f25a77))



##### Documentation

  * Added documentation on log_level and excluded_loggers params in setup_logging ([#971](https://github.com/googleapis/python-logging/issues/971)) ([70d9d25](https://github.com/googleapis/python-logging/commit/70d9d25bf8c3c85a3c5523ecc7fbdbf72f08c583))
  * Update README to break infinite redirect loop ([#972](https://github.com/googleapis/python-logging/issues/972)) ([52cd907](https://github.com/googleapis/python-logging/commit/52cd907bb313df2766ec11e3d24c7e10cda31ca7))



Announcement

Cloud Logging adds support for the `europe-north2` region. For a complete list of supported regions, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## April 17, 2025

**Cloud Logging**

v2

Feature

In the Logs Explorer, you can now view the most frequently occurring fields and values in the JSON payload of your logs. For more information, see the [**Fields** pane](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#logs-field-panel) documentation.

## April 09, 2025

**Cloud Monitoring**

v3

Feature

Application Monitoring lets you monitor the resources and infrastructure from the perspective of an [App Hub](https://cloud.google.com/app-hub/docs/overview) application. The out-of-the-box (OOTB) dashboards generated for your application display log, metric, and incident data. These dashboards can help you understand how your application's resources are performing, and they can help you to diagnose issues. This feature is in Public Preview. 

  * [Application Monitoring overview](https://cloud.google.com/monitoring/docs/about-application-monitoring) provides a brief overview of this feature.
  * [Set up application monitoring](https://cloud.google.com/monitoring/docs/setup-application-monitoring) describes how to configure an observability scope so that you have an aggregated view of your log, metric, and trace data.
  * [View application telemetry](https://cloud.google.com/monitoring/docs/application-monitoring) describes the labels attached to your telemetry data, and it provides guidance about how to explore the OOTB dashboards.



Feature

Application Monitoring now supports [app-enabled folders](https://cloud.google.com/app-hub/docs/overview#app-enabled-folder) and [App Hub host projects](https://cloud.google.com/app-hub/docs/overview#host-project). For app-enabled folders, the metrics scope of the management project is automatically synchronized with the list of projects in the folder, provided quota is available. This feature is in Public Preview.

  * [Metrics scopes for app-enabled folders](https://cloud.google.com/monitoring/settings/metrics-scope-app-enabled-folders) describes the synchronization algorithm and how to view your usage of the metrics scope quota.



## April 04, 2025

**Cloud Logging**

v2

Feature

You can include pipe syntax in the SQL queries you run on the [Log Analytics](https://docs.cloud.google.com/logging/docs/analyze/query-and-view) page. [Pipe syntax](https://docs.cloud.google.com/bigquery/docs/pipe-syntax-guide) supports a linear query structure designed to make your queries easier to read, write, and maintain. The pipe syntax feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

**Cloud Monitoring**

v3

Feature

If you have enabled logging for failures of an uptime check, you can view the logs from the **Uptime details** page. For more information, see [View details of an uptime check](https://cloud.google.com/monitoring/uptime-checks/manage#get).

## March 25, 2025

**Cloud Trace**

v2

Feature

To send trace data to your Google Cloud project, we recommend that you use the new Telemetry API, which implements the OpenTelemetry OTLP API and provides compatibility and support for the open source ecosystem. The limits for the Telemetry API are often more generous than those for the proprietary Cloud Trace API, which you can continue to use. The Telemetry API supports VPC Service Controls. For more information about the Telemetry API, see the following documents:

  * [Telemetry API overview](https://cloud.google.com/stackdriver/docs/reference/telemetry/overview)
  * [Migrate from the Trace exporter to the OTLP endpoint](https://cloud.google.com/trace/docs/migrate-to-otlp-endpoints)
  * [Quotas and limits](https://cloud.google.com/trace/docs/quotas)



## March 24, 2025

**Cloud Logging**

v2

Libraries

### Java

#### [3.22.0](https://github.com/googleapis/java-logging/compare/v3.21.4...v3.22.0) (2025-03-18)

##### Features

  * Next release from main branch is 3.22.0 ([#1776](https://github.com/googleapis/java-logging/issues/1776)) ([7736073](https://github.com/googleapis/java-logging/commit/773607312a1dc6f5f569f2518587ffba4743bb43))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.55.1 ([dd25992](https://github.com/googleapis/java-logging/commit/dd259929b01a2dd50ca2d09005fedf1631b97877))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.45.1 ([#1779](https://github.com/googleapis/java-logging/issues/1779)) ([a643ab0](https://github.com/googleapis/java-logging/commit/a643ab03600fa25cee41df23b2daf65c0fc4e70a))
  * Update googleapis/sdk-platform-java action to v2.55.1 ([#1780](https://github.com/googleapis/java-logging/issues/1780)) ([505557e](https://github.com/googleapis/java-logging/commit/505557e1b9b14c910aec402335bf9fc9ca96975c))



### Java

#### [3.22.0](https://github.com/googleapis/java-logging/compare/v3.21.4...v3.22.0) (2025-03-18)

##### Features

  * Next release from main branch is 3.22.0 ([#1776](https://github.com/googleapis/java-logging/issues/1776)) ([7736073](https://github.com/googleapis/java-logging/commit/773607312a1dc6f5f569f2518587ffba4743bb43))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.55.1 ([dd25992](https://github.com/googleapis/java-logging/commit/dd259929b01a2dd50ca2d09005fedf1631b97877))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.45.1 ([#1779](https://github.com/googleapis/java-logging/issues/1779)) ([a643ab0](https://github.com/googleapis/java-logging/commit/a643ab03600fa25cee41df23b2daf65c0fc4e70a))
  * Update googleapis/sdk-platform-java action to v2.55.1 ([#1780](https://github.com/googleapis/java-logging/issues/1780)) ([505557e](https://github.com/googleapis/java-logging/commit/505557e1b9b14c910aec402335bf9fc9ca96975c))



## March 21, 2025

**Cloud Monitoring**

v3

Announcement

The Google-Built OpenTelemetry Collector is now available. This Collector is an open-source, production-ready build of the upstream OpenTelemetry Collector that is built with upstream OpenTelemetry Collector components. The Google-built Collector lets you send correlated OTLP traces, metrics, and logs to Cloud Observability and other backends from applications instrumented by using OpenTelemetry SDKs. The Collector also captures metadata for Google Cloud resources, so you can correlate application performance data with infrastructure telemetry data.

For information about using this Collector, see [Overview of the Google-Built OpenTelemetry Collector](https://cloud.google.com/stackdriver/docs/instrumentation/google-built-otel).

## March 17, 2025

**Cloud Monitoring**

v3

Change

You can now enable and disable uptime-checks by using the [`disabled` field](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#uptimeCheckConfig.FIELDS.disabled) in the Cloud Monitoring API.

## March 13, 2025

**Cloud Logging**

v2

Feature

[App Hub application](https://docs.cloud.google.com/app-hub/docs/overview) labels are now attached to your log entries. The **Log Fields** pane of the **Logs Explorer** now includes facets for application, service, and workload labels. For more information, see [**Log Fields** pane](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#logs-field-panel).

**Cloud Monitoring**

v3

Feature

Documentation for Slack notification channels now supports Markdown. For more information, see [Annotate notifications with user-defined documentation](https://cloud.google.com/monitoring/alerts/doc-variables).

Feature

You can now see changes made to a dashboard by viewing the version history. For more information, see [View dashboard version history](https://cloud.google.com/monitoring/charts/dashboards#version-history).

## March 12, 2025

**Cloud Logging**

v2

Feature

You can now use the Observability API to set the default log scope. This feature is in Public Preview. For more information, see the following documents:

  * [Create and manage log scopes](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage)
  * [Observability scopes overview](https://docs.cloud.google.com/stackdriver/docs/scopes/configure)
  * [Observability API reference](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest)



## March 11, 2025

**Cloud Logging**

v2

Change

The API to create and manage Log Scopes is now Generally Available (GA). You can create and manage log scopes by using the Cloud Console, the Google Cloud CLI, and Terraform. For more information, see [Create and manage log scopes](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage).

## March 03, 2025

**Cloud Logging**

v2

Libraries

### Java

#### [3.21.4](https://github.com/googleapis/java-logging/compare/v3.21.3...v3.21.4) (2025-02-26)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.54.0 ([67fa9fb](https://github.com/googleapis/java-logging/commit/67fa9fbbc48dd8df9c176ba0bb3d1acf6b975bfc))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.44.0 ([#1768](https://github.com/googleapis/java-logging/issues/1768)) ([a69e699](https://github.com/googleapis/java-logging/commit/a69e6990e5cc7ab920382599510bb14f29a12d7d))
  * Update googleapis/sdk-platform-java action to v2.54.0 ([#1762](https://github.com/googleapis/java-logging/issues/1762)) ([d50a8d2](https://github.com/googleapis/java-logging/commit/d50a8d2fbef588138b4d47cbd3440d7217d690b0))



### Java

#### [3.21.4](https://github.com/googleapis/java-logging/compare/v3.21.3...v3.21.4) (2025-02-26)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.54.0 ([67fa9fb](https://github.com/googleapis/java-logging/commit/67fa9fbbc48dd8df9c176ba0bb3d1acf6b975bfc))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.44.0 ([#1768](https://github.com/googleapis/java-logging/issues/1768)) ([a69e699](https://github.com/googleapis/java-logging/commit/a69e6990e5cc7ab920382599510bb14f29a12d7d))
  * Update googleapis/sdk-platform-java action to v2.54.0 ([#1762](https://github.com/googleapis/java-logging/issues/1762)) ([d50a8d2](https://github.com/googleapis/java-logging/commit/d50a8d2fbef588138b4d47cbd3440d7217d690b0))



## February 27, 2025

**Cloud Monitoring**

v3

Feature

On your custom dashboards, you can reduce the load time of the dashboard by using group widgets. The tab-group widget displays one member of a collection, and it provides tabs on the toolbar to let you select which member to display:

  * [Organize dashboard widgets](https://cloud.google.com/monitoring/dashboards/text-and-grouping#organize_widgets) describes grouping widgets and provides configuration information for the different types.

  * [Dashboard with a `SingleViewGroup` widget](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_svgroup) describes which API fields to use to configure a tab-group widget.




## February 26, 2025

**Cloud Monitoring**

v3

Change

You can now enable and disable the logging of uptime-check failures by using the [`log_check_failures` field](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#uptimeCheckConfig.FIELDS.log_check_failures) in the Cloud Monitoring API.

## February 20, 2025

**Cloud Monitoring**

v3

Feature

When you add an Observability Analytics widget to a custom Cloud Monitoring dashboard, you can now select other log views and analytics views to query in the Views & Schema section. For more information, see [Display charts generated from a Log Analytics query](https://cloud.google.com/monitoring/charts/view-logs#add-sql-chart).

## February 18, 2025

**Cloud Logging**

v2

Feature

You can now use custom constraints with Organization Policy to provide more granular control over your Cloud Logging resources. For more information, see [Use custom organization policies](https://docs.cloud.google.com/logging/docs/custom-constraints).

## February 17, 2025

**Cloud Logging**

v2

Libraries

### Java

#### [3.21.3](https://github.com/googleapis/java-logging/compare/v3.21.2...v3.21.3) (2025-02-12)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.52.0 ([888a885](https://github.com/googleapis/java-logging/commit/888a885dc229960c26fae5098c4b43b7b0ef4fa6))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.43.0 ([#1763](https://github.com/googleapis/java-logging/issues/1763)) ([e0f9f27](https://github.com/googleapis/java-logging/commit/e0f9f271be10cec0d9400bc464bcc0a175078d97))



### Java

#### [3.21.3](https://github.com/googleapis/java-logging/compare/v3.21.2...v3.21.3) (2025-02-12)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.52.0 ([888a885](https://github.com/googleapis/java-logging/commit/888a885dc229960c26fae5098c4b43b7b0ef4fa6))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.43.0 ([#1763](https://github.com/googleapis/java-logging/issues/1763)) ([e0f9f27](https://github.com/googleapis/java-logging/commit/e0f9f271be10cec0d9400bc464bcc0a175078d97))



### Java

#### [3.21.3](https://github.com/googleapis/java-logging/compare/v3.21.2...v3.21.3) (2025-02-12)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.52.0 ([888a885](https://github.com/googleapis/java-logging/commit/888a885dc229960c26fae5098c4b43b7b0ef4fa6))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.43.0 ([#1763](https://github.com/googleapis/java-logging/issues/1763)) ([e0f9f27](https://github.com/googleapis/java-logging/commit/e0f9f271be10cec0d9400bc464bcc0a175078d97))



## February 14, 2025

**Cloud Monitoring**

v3

Change

The **Dashboards** page of the Cloud Console has been refreshed. For more information about dashboards, see the following documents:

  * [Dashboards overview](https://cloud.google.com/monitoring/dashboards).
  * [Install a dashboard by uploading a template from GitHub](https://cloud.google.com/monitoring/dashboards/dashboard-templates). 
  * [Create and manage custom dashboards](https://cloud.google.com/monitoring/charts/dashboards).



## February 10, 2025

**Cloud Monitoring**

v3

Feature

You can now use a variable to control the visibility of a dashboard widget. For more information, see the following documents:

  * [Create and manage variables and pinned filters](https://cloud.google.com/monitoring/dashboards/filter-permanent)
  * [Configure dashboard filters and variables by using the API](https://cloud.google.com/monitoring/dashboards/api-dashboard#define_filters)



## February 06, 2025

**Cloud Logging**

v2

Feature

You can now create and manage your log views by using the Google Cloud console. For more information, see [Configure log views on a log bucket](https://docs.cloud.google.com/logging/docs/logs-views).

## February 04, 2025

**Cloud Monitoring**

v3

Feature

When you create a snooze from the **Incident details** page, you can now apply the snooze to other incidents that have one or more of the same resource labels. For more information, see [Create a snooze](https://cloud.google.com/monitoring/alerts/manage-snooze#create).

## February 03, 2025

**Cloud Logging**

v2

Libraries

### Java

#### [3.21.2](https://github.com/googleapis/java-logging/compare/v3.21.1...v3.21.2) (2025-01-29)

##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.42.0 ([#1755](https://github.com/googleapis/java-logging/issues/1755)) ([d404381](https://github.com/googleapis/java-logging/commit/d4043815246423efe542356dc50ba663092b8df0))
  * Update dependency io.opentelemetry:opentelemetry-bom to v1.46.0 ([#1747](https://github.com/googleapis/java-logging/issues/1747)) ([5ef2853](https://github.com/googleapis/java-logging/commit/5ef285387d63b79bff7e43b233c7f9770f378dba))
  * Update googleapis/sdk-platform-java action to v2.52.0 ([#1753](https://github.com/googleapis/java-logging/issues/1753)) ([3dcf86a](https://github.com/googleapis/java-logging/commit/3dcf86adc3e1ef3d5866cd043149808601c213b8))



Libraries

### Python

#### [3.11.4](https://github.com/googleapis/python-logging/compare/v3.11.3...v3.11.4) (2025-01-22)

##### Bug Fixes

  * Made `write_entries` raise `ValueError` on `ParseError`s ([#958](https://github.com/googleapis/python-logging/issues/958)) ([5309478](https://github.com/googleapis/python-logging/commit/5309478c054d0f2b9301817fd835f2098f51dc3a))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([7baed8e](https://github.com/googleapis/python-logging/commit/7baed8e968f0bfa6abdbf0715dc43822f2fba8ba))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([002b1fc](https://github.com/googleapis/python-logging/commit/002b1fcb395d77d94d7216560c30015b9aefca81))



### Python

#### [3.11.4](https://github.com/googleapis/python-logging/compare/v3.11.3...v3.11.4) (2025-01-22)

##### Bug Fixes

  * Made `write_entries` raise `ValueError` on `ParseError`s ([#958](https://github.com/googleapis/python-logging/issues/958)) ([5309478](https://github.com/googleapis/python-logging/commit/5309478c054d0f2b9301817fd835f2098f51dc3a))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([7baed8e](https://github.com/googleapis/python-logging/commit/7baed8e968f0bfa6abdbf0715dc43822f2fba8ba))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([002b1fc](https://github.com/googleapis/python-logging/commit/002b1fcb395d77d94d7216560c30015b9aefca81))



### Python

#### [3.11.4](https://github.com/googleapis/python-logging/compare/v3.11.3...v3.11.4) (2025-01-22)

##### Bug Fixes

  * Made `write_entries` raise `ValueError` on `ParseError`s ([#958](https://github.com/googleapis/python-logging/issues/958)) ([5309478](https://github.com/googleapis/python-logging/commit/5309478c054d0f2b9301817fd835f2098f51dc3a))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([7baed8e](https://github.com/googleapis/python-logging/commit/7baed8e968f0bfa6abdbf0715dc43822f2fba8ba))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([002b1fc](https://github.com/googleapis/python-logging/commit/002b1fcb395d77d94d7216560c30015b9aefca81))



### Python

#### [3.11.4](https://github.com/googleapis/python-logging/compare/v3.11.3...v3.11.4) (2025-01-22)

##### Bug Fixes

  * Made `write_entries` raise `ValueError` on `ParseError`s ([#958](https://github.com/googleapis/python-logging/issues/958)) ([5309478](https://github.com/googleapis/python-logging/commit/5309478c054d0f2b9301817fd835f2098f51dc3a))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([7baed8e](https://github.com/googleapis/python-logging/commit/7baed8e968f0bfa6abdbf0715dc43822f2fba8ba))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([002b1fc](https://github.com/googleapis/python-logging/commit/002b1fcb395d77d94d7216560c30015b9aefca81))



### Python

#### [3.11.4](https://github.com/googleapis/python-logging/compare/v3.11.3...v3.11.4) (2025-01-22)

##### Bug Fixes

  * Made `write_entries` raise `ValueError` on `ParseError`s ([#958](https://github.com/googleapis/python-logging/issues/958)) ([5309478](https://github.com/googleapis/python-logging/commit/5309478c054d0f2b9301817fd835f2098f51dc3a))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([7baed8e](https://github.com/googleapis/python-logging/commit/7baed8e968f0bfa6abdbf0715dc43822f2fba8ba))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([002b1fc](https://github.com/googleapis/python-logging/commit/002b1fcb395d77d94d7216560c30015b9aefca81))



### Python

#### [3.11.4](https://github.com/googleapis/python-logging/compare/v3.11.3...v3.11.4) (2025-01-22)

##### Bug Fixes

  * Made `write_entries` raise `ValueError` on `ParseError`s ([#958](https://github.com/googleapis/python-logging/issues/958)) ([5309478](https://github.com/googleapis/python-logging/commit/5309478c054d0f2b9301817fd835f2098f51dc3a))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([7baed8e](https://github.com/googleapis/python-logging/commit/7baed8e968f0bfa6abdbf0715dc43822f2fba8ba))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([002b1fc](https://github.com/googleapis/python-logging/commit/002b1fcb395d77d94d7216560c30015b9aefca81))



### Python

#### [3.11.4](https://github.com/googleapis/python-logging/compare/v3.11.3...v3.11.4) (2025-01-22)

##### Bug Fixes

  * Made `write_entries` raise `ValueError` on `ParseError`s ([#958](https://github.com/googleapis/python-logging/issues/958)) ([5309478](https://github.com/googleapis/python-logging/commit/5309478c054d0f2b9301817fd835f2098f51dc3a))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([7baed8e](https://github.com/googleapis/python-logging/commit/7baed8e968f0bfa6abdbf0715dc43822f2fba8ba))
  * Require proto-plus >= 1.25 for Python 3.13 ([#955](https://github.com/googleapis/python-logging/issues/955)) ([002b1fc](https://github.com/googleapis/python-logging/commit/002b1fcb395d77d94d7216560c30015b9aefca81))



**Cloud Monitoring**

v3

Feature

You can now create custom organization policies on alerting policies, notification channels, and snoozes. For more information, see [Use custom organization policies](https://cloud.google.com/monitoring/docs/custom-constraints).

## January 31, 2025

**Cloud Monitoring**

v3

Feature

You can now monitor usage, throughput, and latency, and troubleshoot 429 errors on Vertex AI foundation models like Google Gemini and Anthropic Claude by using a new predefined dashboard. After querying a model from the [Vertex AI Model Garden](https://cloud.google.com/model-garden), you can find the models associated with your project from the Vertex AI **Dashboard** page under the "Model observability" heading.

To customize the dashboard and explore relevant metrics in Cloud Monitoring, click **Show All Metrics**. For information about using dashboards in Cloud Monitoring, see [View and customize Google Cloud dashboards](https://cloud.google.com/monitoring/charts/predefined-dashboards).

## January 24, 2025

**Cloud Trace**

v2

Feature

Introducing trace scopes. Trace scopes are persistent, project-level resources that the **Trace Explorer** page uses to determine which projects to search for trace data. You can create, edit, and delete trace scopes. You can also set one trace scope as the default trace scope, which determines the projects that the **Trace Explorer** searches when the page is opened.

For more information, see the following documents:

  * [Observability scopes overview](https://cloud.google.com/stackdriver/docs/scopes/configure)
  * [Create and manage trace scopes](https://cloud.google.com//trace/docs/trace-scope/create-and-manage).
  * [View traces across projects](https://cloud.google.com/trace/docs/cross-project-traces)



Change

The **Trace Explorer** page in the Google Cloud console has been refreshed. The new page aggregates and displays information about spans using visualizations like heatmaps. You can use menus to apply filters and to group traces by span and service name. You can also explore individual traces and share traces. For more information, see the following documents:

  * [Find and explore traces](https://cloud.google.com/trace/docs/finding-traces)
  * [View traces across projects](https://cloud.google.com/trace/docs/cross-project-traces)
  * [Share trace or span](https://cloud.google.com/trace/docs/share-trace-or-span)



## January 21, 2025

**Cloud Logging**

v2

Announcement

On April 22, 2025, Cloud Logging will replace the single, global quota for the number of calls to write log entries with a set of volume-based regional quotas. For more information, see [Logging API quotas and limits](https://docs.cloud.google.com/logging/quotas#api-limits).

## January 20, 2025

**Cloud Logging**

v2

Libraries

### Java

#### [3.21.1](https://github.com/googleapis/java-logging/compare/v3.21.0...v3.21.1) (2025-01-13)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.51.1 ([705dba2](https://github.com/googleapis/java-logging/commit/705dba2d6c12bd9f9e281c962cfb232ab28b31a9))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.41.1 ([#1745](https://github.com/googleapis/java-logging/issues/1745)) ([6a7280d](https://github.com/googleapis/java-logging/commit/6a7280d0851024c1b44457fa7064a7f3d6fc2d5b))
  * Update dependency org.easymock:easymock to v5.5.0 ([#1639](https://github.com/googleapis/java-logging/issues/1639)) ([f559d89](https://github.com/googleapis/java-logging/commit/f559d89bf36201fce609ef752f27baa0c5f6f1c1))
  * Update googleapis/sdk-platform-java action to v2.51.1 ([#1742](https://github.com/googleapis/java-logging/issues/1742)) ([3c7a2c7](https://github.com/googleapis/java-logging/commit/3c7a2c70fd46cc7196ef7b037d6017971e8a020a))



### Java

#### [3.21.1](https://github.com/googleapis/java-logging/compare/v3.21.0...v3.21.1) (2025-01-13)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.51.1 ([705dba2](https://github.com/googleapis/java-logging/commit/705dba2d6c12bd9f9e281c962cfb232ab28b31a9))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.41.1 ([#1745](https://github.com/googleapis/java-logging/issues/1745)) ([6a7280d](https://github.com/googleapis/java-logging/commit/6a7280d0851024c1b44457fa7064a7f3d6fc2d5b))
  * Update dependency org.easymock:easymock to v5.5.0 ([#1639](https://github.com/googleapis/java-logging/issues/1639)) ([f559d89](https://github.com/googleapis/java-logging/commit/f559d89bf36201fce609ef752f27baa0c5f6f1c1))
  * Update googleapis/sdk-platform-java action to v2.51.1 ([#1742](https://github.com/googleapis/java-logging/issues/1742)) ([3c7a2c7](https://github.com/googleapis/java-logging/commit/3c7a2c70fd46cc7196ef7b037d6017971e8a020a))



### Java

#### [3.21.1](https://github.com/googleapis/java-logging/compare/v3.21.0...v3.21.1) (2025-01-13)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.51.1 ([705dba2](https://github.com/googleapis/java-logging/commit/705dba2d6c12bd9f9e281c962cfb232ab28b31a9))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.41.1 ([#1745](https://github.com/googleapis/java-logging/issues/1745)) ([6a7280d](https://github.com/googleapis/java-logging/commit/6a7280d0851024c1b44457fa7064a7f3d6fc2d5b))
  * Update dependency org.easymock:easymock to v5.5.0 ([#1639](https://github.com/googleapis/java-logging/issues/1639)) ([f559d89](https://github.com/googleapis/java-logging/commit/f559d89bf36201fce609ef752f27baa0c5f6f1c1))
  * Update googleapis/sdk-platform-java action to v2.51.1 ([#1742](https://github.com/googleapis/java-logging/issues/1742)) ([3c7a2c7](https://github.com/googleapis/java-logging/commit/3c7a2c70fd46cc7196ef7b037d6017971e8a020a))



## January 13, 2025

**Cloud Logging**

v2

Feature

You can now create analytics views, which let you transform your log data into a custom format. You can then use SQL to query your analytics views. This feature is in Public Preview. For more information, see the following documents:

  * [About analytics views](https://docs.cloud.google.com/logging/docs/analyze/about-analytics-views)
  * [Create, query, and manage analytics views](https://docs.cloud.google.com/logging/docs/analyze/create-and-manage-analytics-views)



## January 06, 2025

**Cloud Logging**

v2

Libraries

### Go

#### [1.13.0](https://github.com/googleapis/google-cloud-go/compare/logging/v1.12.0...logging/v1.13.0) (2025-01-02)

##### Features

  * **logging:** Change go gapic transport to grpc+rest in logging ([#11289](https://github.com/googleapis/google-cloud-go/issues/11289)) ([a5f250b](https://github.com/googleapis/google-cloud-go/commit/a5f250baf8085bdb07807869a7c4a3a0ca3f535d))



##### Bug Fixes

  * **logging:** Update golang.org/x/net to v0.33.0 ([e9b0b69](https://github.com/googleapis/google-cloud-go/commit/e9b0b69644ea5b276cacff0a707e8a5e87efafc9))
  * **logging:** Update google.golang.org/api to v0.203.0 ([8bb87d5](https://github.com/googleapis/google-cloud-go/commit/8bb87d56af1cba736e0fe243979723e747e5e11e))
  * **logging:** WARNING: On approximately Dec 1, 2024, an update to Protobuf will change service registration function signatures to use an interface instead of a concrete type in generated .pb.go files. This change is expected to affect very few if any users of this client library. For more information, see https://togithub.com/googleapis/google-cloud-go/issues/11020. ([8bb87d5](https://github.com/googleapis/google-cloud-go/commit/8bb87d56af1cba736e0fe243979723e747e5e11e))



### Go

#### [1.13.0](https://github.com/googleapis/google-cloud-go/compare/logging/v1.12.0...logging/v1.13.0) (2025-01-02)

##### Features

  * **logging:** Change go gapic transport to grpc+rest in logging ([#11289](https://github.com/googleapis/google-cloud-go/issues/11289)) ([a5f250b](https://github.com/googleapis/google-cloud-go/commit/a5f250baf8085bdb07807869a7c4a3a0ca3f535d))



##### Bug Fixes

  * **logging:** Update golang.org/x/net to v0.33.0 ([e9b0b69](https://github.com/googleapis/google-cloud-go/commit/e9b0b69644ea5b276cacff0a707e8a5e87efafc9))
  * **logging:** Update google.golang.org/api to v0.203.0 ([8bb87d5](https://github.com/googleapis/google-cloud-go/commit/8bb87d56af1cba736e0fe243979723e747e5e11e))
  * **logging:** WARNING: On approximately Dec 1, 2024, an update to Protobuf will change service registration function signatures to use an interface instead of a concrete type in generated .pb.go files. This change is expected to affect very few if any users of this client library. For more information, see https://togithub.com/googleapis/google-cloud-go/issues/11020. ([8bb87d5](https://github.com/googleapis/google-cloud-go/commit/8bb87d56af1cba736e0fe243979723e747e5e11e))



## December 18, 2024

**Cloud Logging**

v2

Feature

You can now create custom roles that let you create and manage Log Scopes. Log Scopes are in Public Preview. For more information, see [Create and manage log scopes: Before you begin](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage#before-you-begin).

Announcement

Cloud Logging adds support for the `northamerica-south1` region. For a complete list of supported regions, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## December 13, 2024

**Cloud Logging**

v2

Feature

Reporting of the "pending" status of the Ops Agent on the Cloud Monitoring **VM Instances** dashboard has been refined to include additional states. For more information, see [Use **VM Instances** dashboard](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#verify-agent-running-with-vm-instance-dashboard).

**Cloud Monitoring**

v3

Feature

Reporting of the "pending" status of the Ops Agent on the Cloud Monitoring **VM Instances** dashboard has been refined to include additional states. For more information, see [Use **VM Instances** dashboard](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#verify-agent-running-with-vm-instance-dashboard).

## December 12, 2024

**Cloud Monitoring**

v3

Feature

You can now override the validation that checks for metric existence when you create a PromQL-based alerting policy. For more information, see [Disable check for metric existence](https://cloud.google.com/monitoring/promql/create-promql-alerts#disable-validation).

Feature

Text widgets can now link to sections of a dashboard and they can render variables. For more information, see the following documents:

  * [Add text to a dashboard](https://cloud.google.com/monitoring/dashboards/text-and-grouping#add_text_box)
  * [Add sections to a dashboard](https://cloud.google.com/monitoring/dashboards/text-and-grouping#add_section_header)
  * [Create and manage variables and pinned filters](https://cloud.google.com/monitoring/dashboards/filter-permanent)



## December 06, 2024

**Cloud Logging**

v2

Feature

Editing Log Analytics charts that are saved to a dashboard directly in the **Dashboards** page is now generally available (GA).

## November 11, 2024

**Cloud Monitoring**

v3

Feature

Dashboard variables and dashboard-level filtering is now GA. Pinned filters and variables can have multiple default values and they support selection of multiple values. For more information, see the following documents:

  * [Create and manage variables and pinned filters](https://cloud.google.com/monitoring/dashboards/filter-permanent)
  * [Apply a variable to a widget](https://cloud.google.com/monitoring/dashboards/filter-permanent#apply-permanent-filter)



## November 08, 2024

**Cloud Logging**

v2

Change

Audit Logging now populates the [`status.details`](https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog#status) field in the audit log with the `google.rpc.ErrorInfo` and `google.rpc.Help` proto payload types in cases where an API returns an error status and that status includes one of those types in the details field.

## October 29, 2024

**Cloud Logging**

v2

Feature

You can now create and manage log scopes by using the Google Cloud CLI, in addition to using the Cloud Console and Terraform. Log scopes are in Public Preview. For more information, see

  * [Create and manage log scopes](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage)
  * [gcloud logging scopes](https://docs.cloud.google.com/sdk/gcloud/reference/logging/scopes)



## October 28, 2024

**Cloud Logging**

v2

Feature

You can now use tags to annotate your log buckets and use the tags to manage access to the log buckets. For more information, see [Manage log buckets by using tags](https://docs.cloud.google.com/logging/docs/manage-log-buckets-with-tags).

**Cloud Monitoring**

v3

Feature

The capabilities for dashboard-level filtering has been enhanced. You can now configure pinned filters and variables to have multiple default values and support selection of multiple values. You can also create value-only variables and generate the list of possible values for a variable by running a SQL query. These features are in Public Preview. For more information, see the following documents:

  * [Create and manage variables and pinned filters](https://cloud.google.com/monitoring/dashboards/filter-permanent)
  * [Apply a variable to a widget](https://cloud.google.com/monitoring/dashboards/filter-permanent#apply-permanent-filter)



## October 24, 2024

**Cloud Logging**

v2

Feature

You can now create alerting policies that monitor the results of your SQL queries. For more information about SQL-based alerting policies, see the following documents:

  * [Monitor your SQL query results with an alerting policy](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting)
  * [Manage incidents for SQL-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/sql-based-incidents)



**Cloud Monitoring**

v3

Feature

You can now create alerting policies that monitor the results of your SQL queries. For more information about SQL-based alerting policies, see the following documents:

  * [Monitor your SQL query results with an alerting policy](https://cloud.google.com/logging/docs/analyze/sql-in-alerting)
  * [Incidents for SQL-based alerting policies](https://cloud.google.com/monitoring/alerts/sql-based-incidents)



## October 14, 2024

**Cloud Monitoring**

v3

Feature

You can now use the Monitoring API to configure a metric-based alerting policy to send notifications when incidents are closed. For more information, see [AlertStrategy](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#alertstrategy) in the Monitoring API documentation.

## October 09, 2024

**Cloud Logging**

v2

Change

Ops Agent release 2.51.0 adds support for Compute Engine Arm VMs that are running Rocky Linux 8.

**Cloud Monitoring**

v3

Feature

Your App Hub applications are now writing metadata labels. You can use these labels to filter the data displayed by a chart or monitored by an alerting policy. App Hub labels have the prefix of `apphub_`. 

From the context of an App Hub host, you can now view system metrics for your applications. To view system metrics stored in multiple projects, configure the metrics scope of the App Hub host project. For more information, see the following documents:

  * [Configure a metrics scope](https://cloud.google.com/monitoring/settings/multiple-projects)
  * [App Hub overview](https://cloud.google.com/app-hub/docs/overview)



Feature

With the Ops Agent version 2.51.0, you can now collect a set of observability metrics from NVIDIA Data Center GPU Manager (DCGM). For more information, see [NVIDIA Data Center GPU Manager (DCGM)](https://cloud.google.com/monitoring/agent/ops-agent/third-party-nvidia).

Change

Ops Agent release 2.51.0 adds support for Compute Engine Arm VMs that are running Rocky Linux 8.

## October 07, 2024

**Cloud Logging**

v2

Feature

You can now include pipe syntax in the SQL queries you run on the Log Analytics page. For more information, see the BigQuery documentation about [pipe syntax](https://docs.cloud.google.com/bigquery/docs/pipe-syntax).

**Cloud Monitoring**

v3

Change

The user interface for configuring which events to show on a dashboard has been simplified. For more information, see [Show events on a dashboard](https://cloud.google.com/monitoring/dashboards/show-events).

## October 02, 2024

**Cloud Logging**

v2

Feature

You can now use Terraform commands to a create or update a log scope. For more information, see [Create a log scope](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage#create).

## September 30, 2024

**Cloud Logging**

v2

Change

The layout of the Logs Explorer page has been changed. For more information, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

Change

The pricing for vended network logs has changed. For more information see the following:

  * [Cloud Logging pricing summary](https://cloud.google.com/stackdriver/pricing#logging-pricing-summary)
  * [Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing#logging-costs)
  * [Network telemetry log pricing](https://docs.cloud.google.com/vpc/network-pricing#network-telemetry)



**Cloud Monitoring**

v3

Feature

You can now apply and modify dashboard-wide filters by selecting the filter option within the cell of a table. For example, if a table has a column named `zone` and a cell that displays `us-east5-b`, then selecting the filter button in that cell applies the dashboard-wide filter `zone: us-east5-b`. For more information about filtering your dashboard, see the following documents:

  * [Add temporary filters](https://cloud.google.com/monitoring/charts/filter-dashboard)
  * [Add and mange permanent filters and variables](https://cloud.google.com/monitoring/dashboards/filter-permanent)



## September 23, 2024

**Cloud Monitoring**

v3

Change

The layout of the incident detail page has been updated. You can now view related incidents, and switch between viewing only the time series that caused the condition to be met and viewing all time series that the alerting policy evaluated. For more information, see [Incidents for metric-based alerting policies](https://cloud.google.com/monitoring/alerts/incidents-events) and [Incidents for log-based alerting policies](https://cloud.google.com/monitoring/alerts/log-based-incidents).

## September 19, 2024

**Cloud Logging**

v2

Feature

You can now query your log data from the Log Analytics page by using reserved BigQuery slots. For more information, see [Query and view logs in Log Analytics](https://docs.cloud.google.com/logging/docs/analyze/query-and-view).

## September 16, 2024

**Cloud Logging**

v2

Feature

There is a new Cloud Observability Overview page in the Google Cloud console. The new page, which you can customize, introduces the Cloud Observability products, and provides information about your logs, dashboards, incidents, and more. This page can help you detect issues in your resources, view relevant events, and view signals that matter to you.

Feature

You can now create and manage your log scopes by using the Logging API in addition to using the Cloud Console. This feature is in public preview. For more information, see [Create and manage log scopes](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage).

**Cloud Monitoring**

v3

Feature

There is a new Cloud Observability Overview page in the Google Cloud console. The new page, which you can customize, introduces the Cloud Observability products, and provides information about your logs, dashboards, incidents, and more. This page can help you detect issues in your resources, view relevant events, and view signals that matter to you.

## September 09, 2024

**Cloud Monitoring**

v3

Feature

Table and TopList widgets can now display the results of multiple queries. You can also configure the column headers, data alignment, and color-code cells based on how a numeric value compares to a threshold. For more information, see the following documents:

  * [Display the most recent data in tabular form](https://cloud.google.com/monitoring/charts#add_table)
  * [API Example: Dashboard with a `TimeSeriesTable` widget](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_a_table_widget)



## September 06, 2024

**Cloud Monitoring**

v3

Feature

The **Metrics management** page in Cloud Monitoring now shows you the [sources of metric reads](https://cloud.google.com/monitoring/docs/metrics-management#metric-read-sources) and lets you [exclude unneeded metrics](https://cloud.google.com/monitoring/docs/metrics-management#exclude-metrics) entirely, eliminating the cost of ingesting them. For more information, see [View and manage metric usage](https://cloud.google.com/monitoring/docs/metrics-management).

Feature

The fleetwide and per-instance **Observability** tabs on the Compute Engine **VM instances** page now include charts for GPU metrics the from NVIDIA Management Library (NVML). To view the fleetwide GPU charts, select **Compute Engine** > **VM instances** > **Observability**. To view the GPU charts for a VM instance, select **Compute Engine** > **VM instances** , click on the name of a VM instance, and then select **Observability**. These charts are available only for VM instances with attached GPUs, with both the Ops Agent and the NVIDIA GPU driver installed. For information about configuring these VMs, see [About the `gpu` metrics](https://cloud.google.com/monitoring/agent/ops-agent/configuration#receiver-nvml-metrics).

## September 02, 2024

**Cloud Monitoring**

v3

Feature

You can now import Grafana dashboards into Cloud Monitoring by using the console. For more information, see [Import Grafana dashboards into Cloud Monitoring](https://cloud.google.com/monitoring/dashboards/import-grafana-dashboards).

## August 22, 2024

**Cloud Monitoring**

v3

Deprecated

Cloud Monitoring has ended support for the ingestion of [AWS CloudWatch metrics](https://cloud.google.com/monitoring/api/metrics_aws) by using AWS connector projects. This is a breaking change. For information about this deprecation, see [Deprecations: AWS CloudWatch metrics in Connector projects](https://cloud.google.com/stackdriver/docs/deprecations/aws-cloudwatch-metrics-ingestion).

You can continue to collect AWS CloudWatch metrics by using the open source Prometheus CloudWatch exporter and the Ops Agent. For information about this solution, see [Collect AWS CloudWatch metrics by using the Prometheus CloudWatch exporter](https://cloud.google.com/monitoring/custom-metrics/aws-prometheus-cloudwatch).

## August 16, 2024

**Error Reporting**

v1beta1

Feature

Error Reporting can now analyze log entries that have been routed to a log bucket in a non-global region, provided the log sink is in the same project as the log bucket.

## August 13, 2024

**Cloud Logging**

v2

Feature

Introducing log scopes. Log scopes are persistent, project-level resources that list a set of resources to be searched for log entries. For example, you might configure a log scope to contain multiple projects and several log views. If you select your log scope when using the Logs Explorer, it displays the log entries that originate in the specified projects and those in the specified log views.

You can create, edit, and delete log scopes. You can also set one log scope as the default log scope, which determines the resources that the Logs Explorer searches for log entries.

For more information, see [Create and manage log scopes](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage).

## July 30, 2024

**Cloud Monitoring**

v3

Feature

You can now troubleshoot Compute Engine issues involving host events, MIG autoscaling and health-check failures, resource-availability errors, and VM performance by using the new "interactive playbook" dashboards in Cloud Monitoring. You can access the playbook dashboards from the **Dashboards** page by selecting the **GCP** category or by filtering for "GCE Interactive Playbook".

## July 23, 2024

**Cloud Monitoring**

v3

Deprecated

Starting October 22, 2024, [Monitoring Query Language (MQL)](https://cloud.google.com/monitoring/mql) will no longer be a recommended query language for Cloud Monitoring, and we will begin to turn off certain usability features. For more information, see the [deprecation note for MQL](https://cloud.google.com/stackdriver/docs/deprecations/mql).

## July 19, 2024

**Cloud Logging**

v2

Feature

The [permissions](https://docs.cloud.google.com/logging/docs/access-control#saved-queries) required to use saved and recent queries have changed. You can also define a location in your [default resource settings](https://docs.cloud.google.com/logging/docs/default-settings) where saved and recent queries are saved. This location must align with your organization policy.

## July 09, 2024

**Cloud Monitoring**

v3

Announcement

Starting no sooner than January 7, 2025, Cloud Monitoring will begin charging for alerting. For information about the pricing model and examples of pricing scenarios, see [Pricing for alerting](https://cloud.google.com/stackdriver/pricing#pricing-alerting).

## July 08, 2024

**Cloud Logging**

v2

Change

Log buckets in all regions supported by Cloud Logging can now be upgraded to use Log Analytics. For more information, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

**Cloud Monitoring**

v3

Feature

Your dashboards will now recommend event types for display. For more information, see [Show events on a dashboard](https://cloud.google.com/monitoring/dashboards/show-events).

## July 03, 2024

**Cloud Logging**

v2

Change

Agent-installation policies for the Ops Agent are now GA. For more information, see [Overview of agent policies for the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/agent-policies-overview).

Feature

You can now view the estimated number of byte processed along with the validation status of your SQL query when running queries in Log Analytics. You can use this information to understand the relative volume of data that your SQL query will scan.

**Cloud Monitoring**

v3

Change

Agent-installation policies for the Ops Agent are now GA. For more information, see [Overview of agent policies for the Ops Agent](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/agent-policies-overview).

## July 01, 2024

**Cloud Monitoring**

v3

Feature

You can now create private uptime checks that issue TCP requests. For more information, see [Create private uptime checks](https://cloud.google.com/monitoring/uptime-checks/private-checks).

## June 26, 2024

**Cloud Logging**

v2

Feature

You can now analyze your billable log volume when using Log Analytics. This feature is in Public Preview. For more information, see [Analyze log volume with Log Analytics](https://docs.cloud.google.com/logging/docs/analyze/log-volume).

**Cloud Monitoring**

v3

Feature

You can now configure your dashboards to show disruptions in Google Cloud Services. This feature is GA. For more information, see the following pages:

  * For event information, see [Personalized Service Health events](https://cloud.google.com/monitoring/dashboards/event-types#psh-events).
  * For information about enabling events, see [Show events on a dashboard](https://cloud.google.com/monitoring/dashboards/show-events).



## June 25, 2024

**Cloud Logging**

v2

Feature

Ops Agent version 2.48.0 introduces support for Compute Engine VMs that are running Deep Learning VM Images based on Debian 11 (Bullseye). For more information, see [Operating systems](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#supported_operating_systems).

**Cloud Monitoring**

v3

Feature

Ops Agent version 2.48.0 introduces support for Compute Engine VMs that are running Deep Learning VM Images based on Debian 11 (Bullseye). For more information, see [Operating systems](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#supported_operating_systems).

## June 24, 2024

**Cloud Logging**

v2

Feature

Gauges and scorecards are now available to visualize the results of your SQL queries. For more information, see [Chart query results with Log Analytics](https://docs.cloud.google.com/logging/docs/analyze/charts).

**Cloud Monitoring**

v3

Feature

You can now configure your dashboards to show when incidents were opened. For more information, see [Alert events](https://cloud.google.com/monitoring/dashboards/event-types#alert-events).

## June 17, 2024

**Cloud Monitoring**

v3

Feature

In the Monitoring API, you can now configure documentation links for your notifications. For more information, see [Links](https://cloud.google.com/monitoring/alerts/doc-variables#add-links).

## June 13, 2024

**Cloud Logging**

v2

Feature

You can now use Terraform commands to attach an IAM role binding to a log view that grants a principal access to the log view. For more information about log views and about controlling access to log views, see [Configure log views on a log bucket](https://docs.cloud.google.com/logging/docs/logs-views).

## June 06, 2024

**Cloud Monitoring**

v3

Feature

You can now pin your event type selections for custom dashboards. Pinning saves your selections to the dashboard configuration, so they are applied when you reopen the dashboard. For more information, see [Show events on a dashboard](https://cloud.google.com/monitoring/dashboards/show-events).

## May 29, 2024

**Cloud Logging**

v2

Change

Ops Agent version 2.47.0 introduces support for Compute Engine VMs that are running Ubuntu 24.04 LTS (Noble Numbat). For more information, see [Operating systems](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#supported_operating_systems).

**Cloud Monitoring**

v3

Change

Ops Agent version 2.47.0 introduces support for Compute Engine VMs that are running Ubuntu 24.04 LTS (Noble Numbat). For more information, see [Operating systems](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#supported_operating_systems).

## May 28, 2024

**Cloud Monitoring**

v3

Feature

Announcing new Open Telemetry samples that show how to instrument your Python and Node.js applications to collect metrics, logs, and traces:

  * [Python example](https://cloud.google.com/stackdriver/docs/instrumentation/setup/python)
  * [Node.js example](https://cloud.google.com/stackdriver/docs/instrumentation/setup/nodejs)



For general instrumentation information and recommendations, and for links to other samples, see:

  * [Instrumentation and observability overview](https://cloud.google.com/stackdriver/docs/instrumentation/overview)
  * [Choose an instrumentation approach](https://cloud.google.com/stackdriver/docs/instrumentation/choose-approach)



**Cloud Trace**

v2

Feature

You can now search a trace for keywords. For more information, see [Search a trace](https://cloud.google.com/trace/docs/finding-traces#search-trace).

Feature

Announcing new Open Telemetry samples that show how to instrument your Python and Node.js applications to collect metrics, logs, and traces:

  * [Python example](https://cloud.google.com/stackdriver/docs/instrumentation/setup/python)
  * [Node.js example](https://cloud.google.com/stackdriver/docs/instrumentation/setup/nodejs)



For general instrumentation information and recommendations, and for links to other samples, see:

  * [Instrumentation and observability overview](https://cloud.google.com/stackdriver/docs/instrumentation/overview)
  * [Choose an instrumentation approach](https://cloud.google.com/stackdriver/docs/instrumentation/choose-approach)



## May 15, 2024

**Cloud Logging**

v2

Change

You can now attach an IAM role binding to a log view that grants a principal access to the log view. For more information about log views and about controlling access to log views, see [Configure log views on a log bucket](https://docs.cloud.google.com/logging/docs/logs-views).

## May 13, 2024

**Cloud Monitoring**

v3

Feature

You can now configure dashboards to display events by using the Monitoring API.

  * For event information, see [Event types](https://cloud.google.com/monitoring/dashboards/event-types#psh-events).
  * For information about enabling events, see [Show events on a dashboard](https://cloud.google.com/monitoring/dashboards/show-events).
  * For an example, see [API examples: Enable dashboard events and filters](https://cloud.google.com/monitoring/dashboards/api-examples#filters-events).



## May 09, 2024

**Cloud Monitoring**

v3

Feature

You can now configure a logs panel widget to display log entries by log view. For more information, see [Display logs and errors on a custom dashboard](https://cloud.google.com/monitoring/charts/view-logs).

## May 06, 2024

**Cloud Monitoring**

v3

Feature

Synthetic monitors no longer require that the ingress rule be set to allow all traffic. For more information, see [Cloud Function configuration](https://cloud.google.com/monitoring/synthetic-monitors/create#function-configuration).

Feature

A Selenium WebDriver sample is now available for [synthetic monitors](https://cloud.google.com/monitoring/uptime-checks/introduction). For more information, see [Selenium WebDriver template](https://cloud.google.com/monitoring/synthetic-monitors/samples#selenium-sample).

## April 26, 2024

**Cloud Monitoring**

v3

Feature

Broken-link checkers collect screenshots of failing tests in a Cloud Storage bucket. You can configure this feature to collect screenshots for all tests or disable this feature. For more information, see [Create a broken-link checker](https://cloud.google.com/monitoring/synthetic-monitors/broken-links).

## April 03, 2024

**Cloud Logging**

v2

Feature

The Logging query language now supports the `cast` and `regexp_extract` functions. For more information, see the [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language) documentation.

## March 28, 2024

**Cloud Logging**

v2

Feature

Pie charts are now available for visualizing data in the **Log Analytics** page. For more information, see [Change chart type](https://docs.cloud.google.com/logging/docs/analyze/charts#change_chart_type).

**Cloud Monitoring**

v3

Feature

Uptime checks now support authentication by using a service account and a generated OpenID Connect (OIDC) token, as an alternative to providing a username and password. For more information, see [Create public uptime checks](https://cloud.google.com/monitoring/uptime-checks).

## March 26, 2024

**Cloud Logging**

v2

Feature

You can now configure your aggregated sink to be intercepting, which prevents logs from being passed through the Log Router of child resources. For more information, see [Collate and route organization-level logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks).

Change

Duet AI in Google Cloud is now Gemini for Google Cloud. See our [blog post](https://blog.google/technology/ai/google-gemini-update-sundar-pichai-2024/) for more information.

**Cloud Monitoring**

v3

Change

Duet AI in Google Cloud is now Gemini for Google Cloud. See our [blog post](https://blog.google/technology/ai/google-gemini-update-sundar-pichai-2024/) for more information.

## March 18, 2024

**Cloud Monitoring**

v3

Change

You can now use Duet AI for Developers to help you create a synthetic monitor. This feature is in Public Preview. For more information, see [Create a synthetic monitor](https://cloud.google.com/monitoring/synthetic-monitors/create).

## March 11, 2024

**Cloud Logging**

v2

Change

You can now use SQL `JOIN` and `UNION` operators on the **Log Analytics** page to combine tables in multiple Google Cloud projects.

**Error Reporting**

v1beta1

Change

Error Reporting can now analyze logs routed by project sinks to different projects than the source project. For more information, see [Route logs to supported destinations](https://cloud.google.com/logging/docs/export/configure_export_v2).

## March 07, 2024

**Cloud Logging**

v2

Change

Log buckets in the `africa-south1` region can now be upgraded to use Log Analytics. For more information, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

**Cloud Monitoring**

v3

Feature

You can display events, such as the crash of a GKE pod, on your dashboards. This feature is now GA. This feature is available for dashboards managed by Cloud Monitoring, and for the observability dashboards managed by Compute Engine, Google Kubernetes Engine and Cloud Run. 

  * For a list of supported events, see [Event types](https://cloud.google.com/monitoring/dashboards/event-types).
  * For information about enabling events, see [Show events on a dashboard](https://cloud.google.com/monitoring/dashboards/show-events).



## February 20, 2024

**Cloud Logging**

v2

Feature

You can now configure and save a Log Analytics chart directly in Monitoring. For more information, see [Add charts generated from a Log Analytics query](https://docs.cloud.google.com/monitoring/charts/view-logs#add-sql-chart).

Change

For information and recommendations about how to instrument your applications to collect metrics, logs, and traces, see the following documents:

  * [Instrumentation and observability overview](https://docs.cloud.google.com/stackdriver/docs/instrumentation/overview)
  * [Choose an instrumentation approach](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach)
  * [Go instrumentation example](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/go)
  * [Java instrumentation example](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/java)



**Cloud Monitoring**

v3

Change

For information and recommendations about how to instrument your applications to collect metrics, logs, and traces, see the following documents:

  * [Instrumentation and observability overview](https://cloud.google.com/stackdriver/docs/instrumentation/overview)
  * [Choose an instrumentation approach](https://cloud.google.com/stackdriver/docs/instrumentation/choose-approach)
  * [Go instrumentation example](https://cloud.google.com/stackdriver/docs/instrumentation/setup/go)
  * [Java instrumentation example](https://cloud.google.com/stackdriver/docs/instrumentation/setup/java)



**Cloud Trace**

v2

Change

For information and recommendations about how to instrument your applications to collect metrics, logs, and traces, see the following documents:

  * [Instrumentation and observability overview](https://cloud.google.com/stackdriver/docs/instrumentation/overview)
  * [Choose an instrumentation approach](https://cloud.google.com/stackdriver/docs/instrumentation/choose-approach)
  * [Go instrumentation example](https://cloud.google.com/stackdriver/docs/instrumentation/setup/go)
  * [Java instrumentation example](https://cloud.google.com/stackdriver/docs/instrumentation/setup/java)



## February 13, 2024

**Cloud Logging**

v2

Feature

[Copying log entries](https://docs.cloud.google.com/logging/docs/routing/copy-logs) is now [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

## February 12, 2024

**Cloud Logging**

v2

Feature

You can now display Log Analytics query results as a table in your Monitoring dashboards by selecting **Table** as the widget type.

**Cloud Monitoring**

v3

Change

You can now create a broken-link checker, which periodically validates the links contained in your website. This feature is GA. For more information, see [Create a broken-link checker](https://cloud.google.com/monitoring/synthetic-monitors/broken-links).

Feature

[Alerting policies with a PromQL-based condition](https://cloud.google.com/monitoring/promql/promql-in-alerting) are [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## February 08, 2024

**Cloud Logging**

v2

Change

You can now create log buckets in the `africa-south1` region. For a complete list of supported regions, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## February 07, 2024

**Cloud Logging**

v2

Change

Log buckets in the following regions can now be upgraded to use Log Analytics:

  * europe-west10



For more information, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## January 31, 2024

**Cloud Logging**

v2

Fixed

Fixed a bug that caused the audit log associated with an API that performs both Data Access and Admin Activity operations to be classified as a Data Access log. These logs are now always classified as Admin Activity audit logs.

## January 29, 2024

**Cloud Monitoring**

v3

Change

New event types for VM instances and for GKE Pods, Clusters, and Nodes, are now available to display on your dashboards. This feature is in Public Preview. 

  * For a list of supported events, see [Events overview](https://cloud.google.com/monitoring/dashboards/event-types).
  * For information about enabling events, see [Show events on a dashboard](https://cloud.google.com/monitoring/dashboards/show-events).



## January 22, 2024

**Cloud Monitoring**

v3

Feature

You can now create and manage your uptime checks and synthetic monitors by using the Google Cloud CLI. For more information, see [Create public uptime checks](https://cloud.google.com/monitoring/uptime-checks) and [Create a synthetic monitor](https://cloud.google.com/monitoring/synthetic-monitors/create).

## January 19, 2024

**Cloud Monitoring**

v3

Feature

Ops Agent version 2.46.0 introduces a new health check, LogPingOpsAgent, an informational payload message written every 10 minutes to the `ops-agent-health` log. You can use the resulting log entries to verify that the agent is sending logs. For more information, see [Agent health checks](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-find-info#health-checks).

## January 16, 2024

**Cloud Logging**

v2

Feature

You can now edit Log Analytics charts that are saved to a dashboard directly in the **Dashboards** page. For more information, see [Edit a chart saved to a custom dashboard](https://docs.cloud.google.com/logging/docs/analyze/charts#edit_a_chart_saved_to_a_custom_dashboard).

Change

Announcing a common navigation pane in the Cloud console for Logging, Monitoring, Trace, and Error Reporting. When you are troubleshooting an issue, the new navigation pane simplifies accessing the pages you need to explore different types of telemetry:

  * The **Explore** section list the pages to view and analyze telemetry data.
  * The **Detect** section lists the pages you use to ensure that you are notified when errors occur.
  * The **Configure** section lists configuration and management pages.



You can continue to use the search bar to locate pages in the Cloud console and to find documentation.

**Cloud Monitoring**

v3

Feature

Observability for Google Kubernetes Engine: You can now enable the package of kube state metrics from the **Observability** tab of a GKE deployment. For more information, see [Package: Kube state metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#ksm-package).

Change

Announcing a common navigation pane in the Cloud console for Logging, Monitoring, Trace, and Error Reporting. When you are troubleshooting an issue, the new navigation pane simplifies accessing the pages you need to explore different types of telemetry:

  * The **Explore** section list the pages to view and analyze telemetry data.
  * The **Detect** section lists the pages you use to ensure that you are notified when errors occur.
  * The **Configure** section lists configuration and management pages.



You can continue to use the search bar to locate pages in the Cloud console and to find documentation.

**Cloud Trace**

v2

Change

Announcing a common navigation pane in the Google Cloud console for Logging, Monitoring, Trace, and Error Reporting. When you are troubleshooting an issue, the new navigation pane simplifies accessing the pages you need to explore different types of telemetry:

  * The **Explore** section list the pages to view and analyze telemetry data.
  * The **Detect** section lists the pages you use to ensure that you are notified when errors occur.
  * The **Configure** section lists configuration and management pages.



You can continue to use the search bar to locate pages in the Google Cloud console and to find documentation.

**Error Reporting**

v1beta1

Change

Announcing a common navigation pane in the Cloud console for Logging, Monitoring, Trace, and Error Reporting. When you are troubleshooting an issue, the new navigation pane simplifies accessing the pages you need to explore different types of telemetry:

  * The **Explore** section list the pages to view and analyze telemetry data.
  * The **Detect** section lists the pages you use to ensure that you are notified when errors occur.
  * The **Configure** section lists configuration and management pages.



You can continue to use the search bar to locate pages in the Cloud console and to find documentation.

## January 08, 2024

**Cloud Logging**

v2

Feature

You can now go to the Log Analytics page from the Logs Explorer page by clicking the **Analyze results** button, which automatically translates the Logging query language query into a SQL query. For more information, see [Analyze results](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#analyze-results).

## December 20, 2023

**Cloud Monitoring**

v3

Feature

Observability for Google Kubernetes Engine: The collection of kube state metrics is enabled by default for new GKE Autopilot clusters, starting with version 1.27.4-gke.900. For more information, see [Package: Kube state metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#ksm-package).

**Error Reporting**

v1beta1

Change

The Error Reporting API is now [generally available](https://cloud.google.com/products/#product-launch-stages). For more information about the API, see [Overview](https://cloud.google.com/error-reporting/reference).

## December 19, 2023

**Cloud Monitoring**

v3

Feature

On your custom dashboards, you can add section widgets that create a table of contents for your dashboard. You can use the table of contents to navigate to a specific section of your dashboard. For more information, see [Organize dashboard widgets](https://cloud.google.com/monitoring/dashboards/text-and-grouping#organize_widgets).

## December 18, 2023

**Cloud Monitoring**

v3

Feature

On your custom dashboards, you can group widgets into a single-view widget or into a collapsible group. Single-view widgets let you display one member of the group. For more information, see [Organize dashboard widgets](https://cloud.google.com/monitoring/dashboards/text-and-grouping#organize_widgets).

## December 15, 2023

**Cloud Monitoring**

v3

Change

Starting with Ops Agent version 2.45.0, you can configure the Ops Agent to exclude individual metrics and metrics from third-party integrations. For more information, see [Metrics processors](https://cloud.google.com/monitoring/agent/ops-agent/configuration#metrics-processors)

Feature

You can now collect Prometheus metrics from Cloud Run services by using the [Managed Service for Prometheus sidecar for Cloud Run](https://cloud.google.com/stackdriver/docs/managed-prometheus/cloudrun-sidecar).

## December 13, 2023

**Cloud Logging**

v2

Feature

Charting in the **Log Analytics** page is now generally available (GA). In addition to features available in the preview, the GA release includes the ability to select `none` as an aggregation function on a chart.

## December 12, 2023

**Cloud Monitoring**

v3

Feature

You can now configure the severity of your alerting policies. This field lets you define the severity level of incidents. For more information, see [Structure of an alerting policy](https://cloud.google.com/monitoring/alerts/policies-in-api#api-alertpol-struct).

## December 11, 2023

**Cloud Monitoring**

v3

Change

Support for pie charts on your custom dashboards is now GA. For information when using the Cloud Console, see [Graph the most recent data with a pie chart](https://cloud.google.com/monitoring/charts#add_pie). For information about using the API, see [Dashboard with a PieChart widget](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_a_pie_widget).

Change

The new query interface for creating charts is now GA. The new interface provides a style update and simplifies building a query by automatically configuring your aggregation settings. For more information, see [Create charts with Metrics Explorer](https://cloud.google.com/monitoring/charts/metrics-explorer).

## December 07, 2023

**Cloud Monitoring**

v3

Feature

You can now create a broken-link checker, which periodically validates the links contained in your website. This feature is in Public Preview. For more information, see [Create a broken-link checker](https://cloud.google.com/monitoring/synthetic-monitors/broken-links).

## December 05, 2023

**Cloud Logging**

v2

Feature

You can now query for a specific error group in the **Logs Explorer** and **Log Analytics** pages by using the error group ID. For more information, see [Find error group details for a log entry](https://docs.cloud.google.com/logging/docs/analyze/find-logs-error-groups#details).

## December 01, 2023

**Cloud Logging**

v2

Feature

Ops Agent version 2.44.0 introduces the following features:

  * Support for Compute Engine VMs that are running Ubuntu 23.10 (Mantic Minotaur). For more information, see [Operating systems](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#supported_operating_systems).
  * Support for Compute Engine Arm VMs that are running Debian 12 (Bookworm). For more information, see [Support for Compute Engine Arm VMs](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#oagent-arm-support).
  * An option to prevent the agent from collecting self logs and sending them to Cloud Logging. For more information, see [Collection of self logs](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#self-log-collection).



**Cloud Monitoring**

v3

Feature

Ops Agent version 2.44.0 introduces the following features:

  * Support for Compute Engine VMs that are running Ubuntu 23.10 (Mantic Minotaur). For more information, see [Operating systems](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#supported_operating_systems).
  * Support for Compute Engine Arm VMs that are running Debian 12 (Bookworm). For more information, see [Support for Compute Engine Arm VMs](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#oagent-arm-support).
  * An option to prevent the agent from collecting self logs and sending them to Cloud Logging. For more information, see [Collection of self logs](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#self-log-collection).



## November 29, 2023

**Cloud Logging**

v2

Feature

You can now specify an inclusion filter or exclusion filter that is applied to the `_Default` sinks of new resources. For more information, see [Configure default filter of `_Default` sinks](https://docs.cloud.google.com/logging/docs/default-settings#default-sink-filter).

## November 17, 2023

**Cloud Monitoring**

v3

Feature

Observability for Google Kubernetes Engine: The **Observability** tab for a GKE cluster adds a dashboard for GPU metrics. The charts on this dashboard are populated only if the cluster has GPU nodes. For more information, see [View observability metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).

## November 13, 2023

**Cloud Monitoring**

v3

Change

A new query interface for creating charts is now in Public Preview. The new interface provides a style update and simplifies building a query by automatically configuring your aggregation settings. For more information, see [Create charts with Metrics Explorer](https://cloud.google.com/monitoring/charts/metrics-explorer).

## November 10, 2023

**Cloud Logging**

v2

Feature

You can now load saved queries in the **Log Analytics** page by using the **Load** button. The **Load** button lets you edit the query in the **Query** pane before running the query.

## November 09, 2023

**Cloud Monitoring**

v3

Feature

You can now display events, such as the crash of a GKE pod, on your dashboards. This feature is in Public Preview. 

  * For a list of supported events, see [Events overview](https://cloud.google.com/monitoring/dashboards/event-types).
  * For information about enabling events, see [Show events on a dashboard](https://cloud.google.com/monitoring/dashboards/show-events).



## November 08, 2023

**Cloud Monitoring**

v3

Change

Observability for Google Kubernetes Engine: The curated set of kube state metrics is now Generally Available. You can enable this package of metrics from the **Observability** tab for your GKE cluster and preview the available charts and metrics before you enable the metrics. For more information, see [Package: Kube state metrics](https://cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#ksm-package).

## November 07, 2023

**Cloud Monitoring**

v3

Feature

Observability for Google Kubernetes Engine: The **Observability** tab for a GKE deployment now shows application performance metrics if the metrics are available. The supported metric sources include Istio, GKE Ingress, NGINX Ingress and gRPC and HTTP metrics collected by using Google Managed Service for Prometheus. For more information, see [Use application performance metrics](https://cloud.google.com/stackdriver/docs/solutions/gke/app-performance-metrics).

## November 06, 2023

**Cloud Logging**

v2

Change

Log buckets in the following regions can now be upgraded to use Log Analytics:

  * me-central2



For more information, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## November 03, 2023

**Cloud Monitoring**

v3

Change

Synthetic monitors are now GA. You can create synthetic monitors by using Terraform, the Cloud console, and the Monitoring API. You can configure your synthetic monitors to collect log data and trace data. When you use the Cloud console, the generic and Mocha templates are available:

  * For general information, see [Synthetic monitoring overview](https://cloud.google.com/monitoring/uptime-checks/introduction).
  * For information about creating a synthetic monitor, see [Create a synthetic monitor](https://cloud.google.com/monitoring/synthetic-monitors/create).



## November 02, 2023

**Cloud Logging**

v2

Feature

You can now set a custom time interval for charts in the **Log Analytics** page. The custom time interval can be specified in minutes, hours, or days.

## November 01, 2023

**Cloud Logging**

v2

Feature

[Summarizing log entries with Duet AI assistance](https://docs.cloud.google.com/logging/docs/view/summarize-log-entries-duet-ai) is now [generally available](https://cloud.google.com/products/#product-launch-stages).

**Error Reporting**

v1beta1

Feature

[Troubleshooting errors with Duet AI assistance](https://cloud.google.com/error-reporting/docs/troubleshoot-errors-duet-ai) is now [generally available](https://cloud.google.com/products/#product-launch-stages).

## October 24, 2023

**Cloud Logging**

v2

Feature

Ops Agent version 2.43.0 introduces support for Compute Engine Arm VMs that are running SLES 15 and OpenSUSE Leap 15. For more information, see [Support for Compute Engine Arm VMs](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#oagent-arm-support).

**Cloud Monitoring**

v3

Feature

Ops Agent version 2.43.0 introduces support for Compute Engine Arm VMs that are running SLES 15 and OpenSUSE Leap 15. For more information, see [Support for Compute Engine Arm VMs](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#oagent-arm-support).

## October 23, 2023

**Cloud Monitoring**

v3

Change

You can configure your synthetic monitors to collect log data and trace data for your outbound HTTP requests when you use the generic template. This feature is in Public Preview. For more information, see [Samples for synthetic monitors](https://cloud.google.com/monitoring/synthetic-monitors/samples).

## October 17, 2023

**Cloud Monitoring**

v3

Feature

You can now view error groups on your custom dashboards. This feature is GA. For information when using the Cloud Console, see [Display logs and errors on a custom dashboard](https://cloud.google.com/monitoring/charts/view-logs). For information about using the API, see [Dashboard with an ErrorReportingPanel widget](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_er_panel).

**Error Reporting**

v1beta1

Feature

You can now view error groups on your custom dashboards. This feature is GA. For information when using the Cloud Console, see [Display logs and errors on a custom dashboard](https://cloud.google.com/monitoring/charts/view-logs). For information about using the API, see [Dashboard with an ErrorReportingPanel widget](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_er_panel).

## October 16, 2023

**Cloud Logging**

v2

Change

You can now create log buckets in the us-west8 region. For a complete list of supported regions, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## October 12, 2023

**Cloud Logging**

v2

Change

You can now configure the format of the timestamp in your query results in the **Logs Explorer**. For more information, see [Logs Explorer overview: Configure the Time column](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#customize_time).

## October 09, 2023

**Cloud Logging**

v2

Change

When you install the Ops Agent on a Compute Engine VM by using the Cloud Monitoring **VM Instances** dashboard or the **Observability** tab on a Compute Engine VM details page, the agent is now installed with an Ops Agent OS policy. This installation method replaces the prior set of manual steps. For more information, see [Installing the agent by using the Google Cloud console](https://docs.cloud.google.com/logging/docs/agent/ops-agent/installation#gce-ui-install).

**Cloud Monitoring**

v3

Change

When you install the Ops Agent on a Compute Engine VM by using the Cloud Monitoring **VM Instances** dashboard or the **Observability** tab on a Compute Engine VM details page, the agent is now installed with an Ops Agent OS policy. This installation method replaces the prior set of manual steps. For more information, see [Installing the agent by using the Google Cloud console](https://cloud.google.com/monitoring/agent/ops-agent/installation#gce-ui-install).

## October 05, 2023

**Cloud Monitoring**

v3

Feature

Ops Agent version 2.42.0 introduces support for Compute Engine Arm VMs that are running Ubuntu 22.04 LTS (Jammy Jellyfish). For more information, see [Support for Compute Engine Arm VMs](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#oagent-arm-support).

Change

Dashboard-wide filters now apply to the Logs Panel widget. For more information, see [Filter the log entries](https://cloud.google.com/monitoring/charts/view-logs#filter_the_log_entries).

**Cloud Trace**

v2

Change

You can now show logs and events as inline messages when exploring a trace. For more information, see [Find and explore traces](https://cloud.google.com/trace/docs/finding-traces).

## October 02, 2023

**Cloud Monitoring**

v3

Feature

You can now configure notifications for Google Chat spaces. For more information, see [Create and manage notification channels](https://cloud.google.com/monitoring/support/notification-options#google-chat).

Change

The **Metrics management** page in Cloud Monitoring now lets you create alerting policies and charts for metrics that have no associated alerting policies or custom dashboards. For more information, see [View and manage metric usage](https://cloud.google.com/monitoring/docs/metrics-management).

Feature

You can now import your Grafana dashboards into Cloud Monitoring. For more information, see [Import Grafana dashboards into Cloud Monitoring](https://cloud.google.com/monitoring/dashboards/import-grafana-dashboards).

## September 29, 2023

**Cloud Logging**

v2

Issue

Ops Agent versions 2.39.0 and 2.40.0 crash if you use them on Compute Engine VMs with attached GPUs. Use Ops Agent version 2.38.0, or versions 2.41.0 and newer, on VMs with attached GPUs.

**Cloud Monitoring**

v3

Issue

Ops Agent versions 2.39.0 and 2.40.0 crash if you use them on Compute Engine VMs with attached GPUs. Use Ops Agent version 2.38.0, or versions 2.41.0 and newer, on VMs with attached GPUs.

## September 28, 2023

**Cloud Monitoring**

v3

Change

You can now configure your alerting policy documentation with custom subject lines. For more information, see [Configure the subject line of notifications](https://cloud.google.com/monitoring/alerts/doc-variables#subjects).

## September 18, 2023

**Cloud Logging**

v2

Feature

You can now save charts generated from a Log Analytics SQL query to a custom dashboard. For more information, see [Save a chart to a custom dashboard](https://docs.cloud.google.com/logging/docs/analyze/charts#save-chart-dashboard).

Change

You can now customize the **Logs Dashboard** page by using custom dashboards. For more information, see [Visualize log severity and error metrics](https://docs.cloud.google.com/logging/docs/view/dashboard).

Change

You can now use the **Log fields** pane of the **Logs Explorer** to filter your Kubernetes Container logs by their service name. The service name is extracted from the value of the `pod_name` label. For more information, see [Logs fields pane](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#logs-field-panel).

## September 14, 2023

**Cloud Monitoring**

v3

Feature

Ops Agent version 2.40.0 introduces support for Compute Engine Arm VMs that are running RHEL 9 or Rocky Linux 9. For more information, see [Support for Compute Engine Arm VMs](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#oagent-arm-support).

## September 12, 2023

**Cloud Logging**

v2

Change

Log buckets in the following regions can now be upgraded to use Log Analytics:

  * us-east5
  * us-south1
  * me-central1
  * europe-west12



For more information, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## September 11, 2023

**Error Reporting**

v1beta1

Change

Error Reporting now supports Cloud Run Jobs as a monitored resource type. For more information, see [Supported monitored resources](https://cloud.google.com/error-reporting/docs/formatting-error-messages#supported_monitored_resources).

## September 07, 2023

**Cloud Monitoring**

v3

Feature

Ops Agent version 2.39.0 introduces support for Compute Engine Arm VMs that are running Ubuntu 20.04 LTS (Focal Fossa). For more information, see [Support for Compute Engine Arm VMs](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#oagent-arm-support).

Change

Starting with version 2.39.0, the Ops Agent supports ingesting Prometheus metrics with unknown types. In earlier versions, untyped metrics are treated by the Ops Agent as gauges, but starting with Ops Agent version 2.39.0, untyped metrics are treated as both gauges and counters, and you can apply cumulative operations to the metrics.

If you have charts or alterting policies based on untyped metrics and written with MQL, you must adjust your queries. For more information, see [Prometheus untyped metrics change metric type starting with Ops Agent version 2.39.0](https://cloud.google.com/monitoring/agent/ops-agent/troubleshoot-run-ingest.md#untyped-metrics).

## September 05, 2023

**Error Reporting**

v1beta1

Feature

[Troubleshooting errors with Duet AI assistance](https://cloud.google.com/error-reporting/docs/troubleshoot-errors-duet-ai) is now available in [Preview](https://cloud.google.com/products/#product-launch-stages).

## August 29, 2023

**Cloud Logging**

v2

Feature

[Summarizing log entries with Duet AI assistance](https://docs.cloud.google.com/logging/docs/view/summarize-log-entries-duet-ai) is now available in [Preview](https://cloud.google.com/products/#product-launch-stages).

## August 21, 2023

**Cloud Logging**

v2

Feature

You can now view your query results as a chart in the **Log Analytics** page. For more information, see [Chart query results with Log Analytics](https://docs.cloud.google.com/logging/docs/analyze/charts).

Feature

Identity and Access Management (IAM) deny policies can now include Cloud Logging permissions. For a list of Cloud Logging permissions that are supported by deny policies, see [Permissions supported in deny policies](https://docs.cloud.google.com/iam/docs/deny-permissions-support).

**Cloud Monitoring**

v3

Feature

You can now add pie charts to your custom dashboards. Support for pie charts is in public preview. For information when using the Cloud Console, see [Graph the most recent data with a pie chart](https://cloud.google.com/monitoring/charts#add_pie). For information about using the API, see [Dashboard with a PieChart widget](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_a_pie_widget).

Feature

Observability for Google Kubernetes Engine: The **Observability** tab for each of your GKE clusters now includes filters for recommended and configured integrations. To see the recommended integrations for your cluster, select **Integrations > Overview**. To see the integrations configured for your cluster, select **Integrations > Configured**.

## August 18, 2023

**Cloud Monitoring**

v3

Deprecated

Cloud Monitoring is ending support for the ingestion of [AWS CloudWatch metrics](https://cloud.google.com/monitoring/api/metrics_aws) in AWS connector projects. This is a breaking change. For information about this deprecation, see [Deprecations: AWS CloudWatch metrics in Connector projects](https://cloud.google.com/stackdriver/docs/deprecations/aws-cloudwatch-metrics-ingestion).

You can continue to collect AWS CloudWatch metrics by using the open source Prometheus CloudWatch exporter and the Ops Agent. For information about migrating to this solution, see [Collect AWS CloudWatch metrics by using the Prometheus CloudWatch exporter](https://cloud.google.com/monitoring/custom-metrics/aws-prometheus-cloudwatch).

## August 17, 2023

**Cloud Monitoring**

v3

Change

Version 2.38.0 of the Ops Agent provides GA support for NVIDIA GPU metrics, including metrics reported from the NVIDIA Management Library (NVML) and the Data Center GPU Manager (DCGM).

NVML metrics are collected automatically if you have installed the NVIDIA Management Library. For more information, see [Configure the Ops Agent](http://cloud.google.com/monitoring/agent/ops-agent/configuration). DGCM metrics are available as a third-party integration. For information about configuring the integration, see [NVIDIA Data Center GPU Manager](https://cloud.google.com/monitoring/agent/ops-agent/third-party-nvidia).

Change

The improved dashboard building experience is now GA:

  * Improved the performance
  * Simplified the layout and expanded the configurable settings
  * Improved the widget drag and drop experience
  * Enhanced the [text widget](https://cloud.google.com/monitoring/dashboards/text-and-grouping)
  * Unified the chart-configuration experience between dashboards and the Metrics Explorer



For more information, see [Add charts and tables to a custom dashboard](https://cloud.google.com/monitoring/charts).

## August 16, 2023

**Cloud Logging**

v2

Change

The behavior of simple text searches as changed. To improve the performance, the [Search function](https://docs.cloud.google.com/logging/docs/view/logging-query-language#search-functions) is automatically invoked when you don't wrap the search terms in double quotes.

**Cloud Monitoring**

v3

Feature

You can now troubleshoot GKE issues involving CPU and memory utilization by using the new "interactive playbook" dashboards in Cloud Monitoring. You can access these playbook dashboards from the **Dashboards** list and from the **Incident details** page associated with alerts you've set up for CPU utilization or memory utilization.

Feature

Observability for Google Kubernetes Engine: You can now enable a curated set of kube state metrics from the **Observability** tab for your GKE cluster. You can also preview the available charts and metrics before you enable the metrics. For more information, see [Package: Kube state metrics](https://cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#ksm-package).

## August 14, 2023

**Cloud Logging**

v2

Feature

Version 2.37.0 of the Ops Agent introduces runtime health checks for errors in the configuration of logging pipelines and in parsing logs. These errors are reported to Cloud Logging. For more information, see [Agent health checks](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-find-info#health-checks).

**Cloud Monitoring**

v3

Feature

Version 2.37.0 of the Ops Agent introduces runtime health checks for errors in the configuration of logging pipelines and in parsing logs. These errors are reported to Cloud Logging. For more information, see [Agent health checks](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-find-info#health-checks).

Change

Version 2.37.0 of the Ops Agent introduces GA support for an OpenTelemetry Protocol (OTLP) receiver. You can use this receiver to collect custom metrics and traces from applications written by using OpenTelemetry SDKs. For more information, see [Collect OpenTelemetry protocol (OTLP) metrics and traces](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/otlp).

**Cloud Trace**

v2

Change

Version 2.37.0 of the Ops Agent introduces GA support for an OpenTelemetry Protocol (OTLP) receiver. You can use this receiver to collect custom traces and metrics from applications written by using OpenTelemetry SDKs. For more information, see [Use the Ops Agent and OpenTelemetry Protocol (OTLP)](https://cloud.google.com/trace/docs/otlp).

**Error Reporting**

v1beta1

Feature

Error Reporting now reports recent application errors for Google Kubernetes Engine services and clusters on a new **App Errors** tab.

  * To view service errors, go to **Kubernetes Engine** in the Google Cloud console and select **Services & Ingress**, then select a specific service and click the **App Errors** tab.
  * To view cluster errors, go to **Kubernetes Engine** in the Google Cloud console and select **Clusters** , then select a specific cluster and click the **App Errors** tab.



## August 10, 2023

**Cloud Monitoring**

v3

Feature

PromQL alerting for Cloud Monitoring is in Public Preview. You can now use PromQL queries in your alerting policies. You can also migrate your Prometheus alerting rules to Cloud Monitoring alerting rules with a PromQL query, and migrate your Prometheus receivers to Cloud Monitoring notification channels. For more information, see [Alerting policies with PromQL](https://cloud.google.com/monitoring/promql/promql-in-alerting).

**Error Reporting**

v1beta1

Feature

In the Error Reporting page's resource filter, you can now filter GKE resources by location, cluster, namespace, and container or pod. For more information, see [Filter errors](https://cloud.google.com/error-reporting/docs/viewing-errors#filtering).

## August 08, 2023

**Cloud Monitoring**

v3

Change

The price of Managed Service for Prometheus samples ingested into Cloud Monitoring has dropped by 60 percent. For more information, see [Cloud Monitoring pricing summary](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary), and for worked examples, see [Pricing examples based on samples ingested](https://cloud.google.com/stackdriver/pricing#pricing_examples_samples).

## August 07, 2023

**Cloud Logging**

v2

Change

Cloud Logging now supports the following regions:

  * europe-west10
  * europe-west12
  * me-central2



For more information, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

**Cloud Monitoring**

v3

Change

The **Metrics management** page in Cloud Monitoring replaces the **Metrics diagnostics** page, extending the information available about the chargeable metrics in your Google Cloud projects. For more information, see [View metric usage and diagnostics](https://cloud.google.com/monitoring/docs/metrics-management).

Feature

Observability for Google Kubernetes Engine: Charts on the **Observability** tab for each of your GKE clusters and workloads now includes an optional fleet ID filter, where applicable. If the current project is a host project for a fleet, the cluster and workload charts show metrics from all projects in the fleet, even if the metrics are hosted in a different project.

## August 01, 2023

**Cloud Logging**

v2

Feature

Ops Agent version 2.36.0 introduces support for Compute Engine Arm VMs that are running Debian 11 (Bullseye). For more information, see [Support for Compute Engine Arm VMs](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#oagent-arm-support).

**Cloud Monitoring**

v3

Feature

You can now snooze an alerting policy from an Incident details page related to the alerting policy. For more information, see [Snooze an alerting policy](https://cloud.google.com/monitoring/alerts/incidents-events#snoozing).

Feature

Ops Agent version 2.36.0 introduces support for Compute Engine Arm VMs that are running Debian 11 (Bullseye). For more information, see [Support for Compute Engine Arm VMs](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#oagent-arm-support).

## July 26, 2023

**Cloud Logging**

v2

Change

Starting with version 2.35.0, the Ops Agent health-check log is renamed `ops-agent-health`; earlier versions of the Ops Agent that support health checks use the name `ops-agent-health-checks`.

**Cloud Monitoring**

v3

Change

Starting with version 2.35.0, the Ops Agent health-check log is renamed `ops-agent-health`; earlier versions of the Ops Agent that support health checks use the name `ops-agent-health-checks`.

## July 21, 2023

**Cloud Logging**

v2

Feature

You can now view logs that are stored in log buckets in different projects by using the **Refine scope** button in the **Logs Explorer**. For more information, see [Refine scope](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#refine_scope).

Change

The Cloud Logging agent for Windows version 1-21 is now available. This version has no user-visible changes but upgrades the `grpc` gem and others to fix vulnerabilities. This also includes the switch to Ruby 3, from version 1-20 of the Logging agent.

**Cloud Trace**

v2

Change

When viewing a span, you can now also view the linked spans. For more information, see [View span details](https://cloud.google.com/trace/docs/finding-traces#span-details).

## July 20, 2023

**Cloud Logging**

v2

Change

Support for routing your logs through the Log Router of another Google Cloud project is now Generally Available (GA). For more information, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

**Cloud Monitoring**

v3

Change

We made improvements to the dashboard building experience:

  * Improved the performance
  * Simplified the layout and expanded the configurable settings
  * Improved the widget drag and drop experience
  * Enhanced the [text widget](https://cloud.google.com/monitoring/dashboards/text-and-grouping)
  * Unified the chart-configuration experience between dashboards and the Metrics Explorer



For more information, see [Add charts and tables to a custom dashboard](https://cloud.google.com/monitoring/charts).

## July 19, 2023

**Cloud Logging**

v2

Change

The pricing language for Cloud Logging has changed; however, the free allotments and the rates haven't changed. For more information, see [Cloud Logging pricing summary](https://cloud.google.com/stackdriver/pricing#logging-pricing-summary).

## July 18, 2023

**Cloud Logging**

v2

Change

You can now upgrade log buckets in **most** regions to use Log Analytics. To determine if the region of a log bucket is supported, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## July 17, 2023

**Cloud Monitoring**

v3

Feature

You can now create synthetic monitors, which let you continuously test the availability, consistency, and performance of your services and application web pages and APIs, by using automated script based tests. Synthetic monitors periodically probe the endpoints of your application and they record whether or not a probe was successful, along with additional data about the request. For more information, see [Synthetic monitoring overview](https://cloud.google.com/monitoring/uptime-checks/introduction).

## July 10, 2023

**Cloud Logging**

v2

Feature

Time ranges are now synchronized between select Logging and Monitoring pages.

## July 07, 2023

**Cloud Monitoring**

v3

Feature

You can now troubleshoot common GKE issues like unschedulable pods and crashlooping containers by using the new "interactive playbook" dashboards in Cloud Monitoring. For information about using these dashboards, see the GKE troubleshooting documentation for [unschedulable pods](https://cloud.google.com/kubernetes-engine/docs/troubleshooting#PodUnschedulable) and [crashlooping](https://cloud.google.com/kubernetes-engine/docs/troubleshooting#CrashLoopBackOff).

## July 06, 2023

**Cloud Logging**

v2

Feature

The Google Cloud console can now automatically install the Ops Agent for you when you create a VM instance. During the installation process, the Compute Engine VM Manager creates an Ops Agent OS policy that installs the agent and reinstalls it when necessary. For more information, see [Install the Ops Agent during VM creation](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-agent-vm-creation).

**Cloud Monitoring**

v3

Feature

The Google Cloud console can now automatically install the Ops Agent for you when you create a VM instance. During the installation process, the Compute Engine VM Manager creates an Ops Agent OS policy that installs the agent and reinstalls it when necessary. For more information, see [Install the Ops Agent during VM creation](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-agent-vm-creation).

## June 20, 2023

**Cloud Logging**

v2

Change

Log buckets in the following regions can now be upgraded to use Log Analytics:

  * asia-east1
  * europe-north1
  * northamerica-northeast2
  * us-east4



For more information, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## June 13, 2023

**Cloud Monitoring**

v3

Feature

You can now grant a predefined role that only lets you view and manage incidents. For more information, see [Access control: Incidents](https://cloud.google.com/monitoring/access-control#incident_roles_desc).

## June 12, 2023

**Cloud Logging**

v2

Feature

You can now create log sinks with user-defined service accounts. For more information, see [Configure log sinks with user-managed service accounts](https://docs.cloud.google.com/logging/docs/routing/user-managed-service-accounts).

**Cloud Trace**

v2

Change

The **Trace list** page has been replaced with the **Trace explorer** page, which contains a more responsive and interactive **Trace details** section. The new design delivers an improved user experience when traversing spans and when viewing span details. For more information, see [Find and explore traces](https://cloud.google.com/trace/docs/finding-traces).

## June 09, 2023

**Cloud Monitoring**

v3

Feature

**Google Cloud Managed Service for Prometheus** can now ingest exemplars attached to histogram metrics. Exemplars are commonly used to attach trace data to latency metrics, to help you find the cause of a sudden change in metric values. For information, see [Use Prometheus exemplars](https://cloud.google.com/stackdriver/docs/managed-prometheus/exemplars).

Change

A new version of Managed Service for Prometheus is now available. Version 0.7.0 of managed collection for Kubernetes has been released. Users who deploy managed collection using `kubectl` should [reapply the manifests](https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#config-mgd-collection). Users who deploy the service using `gcloud` or the GKE UI are already upgraded on clusters running version 1.25 or newer. Self-deployed collection users should upgrade their binaries to use [gke.gcr.io/prometheus-engine/prometheus:v2.35.0-gmp.5-gke.0](http://gke.gcr.io/prometheus-engine/prometheus:v2.35.0-gmp.5-gke.0).

For details about the changes included, see the [release page on GitHub](https://github.com/GoogleCloudPlatform/prometheus-engine/releases/tag/v0.7.0).

## June 05, 2023

**Cloud Logging**

v2

Feature

You can now configure CMEK and a default storage location for individual folders, in addition to organizations. For more information, see [Configure default settings for organizations and folders](https://docs.cloud.google.com/logging/docs/default-settings) and [Configure CMEK for Cloud Logging](https://docs.cloud.google.com/logging/docs/routing/managed-encryption).

## May 31, 2023

**Cloud Logging**

v2

Change

Cloud Logging no longer creates a dedicated service account for each log sink. Instead, Logging reuses an existing service account when one is available for the resource type. Logging creates a service account when none are available. For more information, see [Set destination permissions](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks#dest-auth).

## May 26, 2023

**Cloud Monitoring**

v3

Feature

**Observability for Google Kubernetes Engine** : The **Observability** tab for each of your GKE clusters now includes metrics for ephemeral storage. For more information, see [View observability metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics#metrics_for_clusters_and_workloads).

## May 22, 2023

**Cloud Logging**

v2

Feature

You can now use SQL `JOIN` and `UNION` operators in queries on the **Log Analytics** page. For more information, see [Combine data from multiple sources](https://docs.cloud.google.com/logging/docs/analyze/examples#multi-query-ops).

## May 19, 2023

**Cloud Logging**

v2

Change

Log buckets with Log Analytics enabled now support the use of Customer Managed Encryption Keys (CMEK). For information about enabling Log Analytics on log buckets, see [Create a bucket](https://docs.cloud.google.com/logging/docs/buckets#create_bucket) or [Upgrade a bucket to use Log Analytics](https://docs.cloud.google.com/logging/docs/buckets#upgrade-bucket).

## May 17, 2023

**Cloud Monitoring**

v3

Change

Cloud Monitoring now provides GA support to prevent alerting policies from sending notifications and creating incidents during specific time periods. For general information, see [Snooze notifications and alerts](https://cloud.google.com/monitoring/alerts/snooze). For information about how to create, view, and modify a snooze, see [Create and manage snoozes](https://cloud.google.com/monitoring/alerts/manage-snooze).

## May 15, 2023

**Cloud Logging**

v2

Feature

You can now customize the time range of your queries in the **Log Analytics** page by using the time-range selector. There are several time range options, such as preset times, custom start and end times, and relative time ranges. For more information, see [Filter by time](https://docs.cloud.google.com/logging/docs/analyze/examples#filter-time).

**Cloud Monitoring**

v3

Feature

Version 2.31.0 of the Ops Agent introduces preview support for an OpenTelemetry Protocol (OTLP) receiver. You can use this receiver to collect custom metrics and traces from applications written by using OpenTelemetry SDKs. For more information, see [Collect OTLP metrics and traces](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/otlp).

Change

The new interface for creating charts with Metrics Explorer is GA. For more information, see [Create charts with Metrics Explorer](https://cloud.google.com/monitoring/charts/metrics-explorer).

**Cloud Trace**

v2

Feature

Version 2.31.0 of the Ops Agent introduces preview support for an OpenTelemetry Protocol (OTLP) receiver. You can use this receiver to collect custom traces and metrics from applications written by using OpenTelemetry SDKs. For more information, see [Collect OTLP traces](https://cloud.google.com/trace/docs/otlp).

## May 12, 2023

**Cloud Monitoring**

v3

Change

The new flow for creating uptime checks, which includes usability improvements and offers a seamless way to create uptime checks on your private resources, is now GA. For more information, see [Create public uptime checks](https://cloud.google.com/monitoring/uptime-checks) and [Create private uptime checks](https://cloud.google.com/monitoring/uptime-checks/private-checks).

## May 02, 2023

**Cloud Monitoring**

v3

Feature

Observability for Google Kubernetes Engine: You can now enable GKE control plane metrics from the **Observability** tab for your GKE cluster. You can also preview the available charts and metrics before you enable the metrics. For more information, see [Configuring collection of control plane metrics](https://cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#enable-control-plane-metrics).

## April 26, 2023

**Cloud Logging**

v2

Feature

Version 2.31.0 of the Ops Agent introduces built-in support for log rotation. For more information, see [Configure log rotation in the Ops Agent](https://stackdriver/docs/solutions/agents/ops-agent/rotate-logs#configure-log-rotation).

**Cloud Monitoring**

v3

Feature

Version 2.31.0 of the Ops Agent introduces built-in support for log rotation. For more information, see [Configure log rotation in the Ops Agent](https://cloud.google.com//stackdriver/docs/solutions/agents/ops-agent/rotate-logs#configure-log-rotation).

## April 25, 2023

**Cloud Monitoring**

v3

Feature

The **Observability** tab on the **VM instances** page for Compute Engine has been enhanced. Disk and Network sections with additional charts have been added. The Integrations > Detected section lets you navigate to the dashboards for the third-party integrations, like Apache or NGINX, that you have configured. The page also includes a set of Recommended Alerts for setting up pre-configured alerting policies for CPU, memory, and disk utilization and for host errors.

## April 18, 2023

**Cloud Logging**

v2

Feature

You can now configure Log Analytics on Cloud Logging buckets and BigQuery linked datasets by using the following Terraform modules:

  * [google_logging_project_bucket_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/logging_project_bucket_config)

  * [google_logging_linked_dataset](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/logging_linked_dataset)




## April 13, 2023

**Cloud Monitoring**

v3

Change

Chart legends in select Cloud Monitoring pages have been updated. The default chart legend is simplified, with the option to expand the legend to view more details about your metrics. For more information, see [Configure legends](https://cloud.google.com/monitoring/charts/working-with-legends).

## April 11, 2023

**Cloud Logging**

v2

Change

The Logging Query Language now supports a built-in `SEARCH` function that you can use to find strings in your log data. The `SEARCH` function is now GA. For more information, see [`SEARCH` function](https://docs.cloud.google.com/logging/docs/view/logging-query-language#search-functions).

## April 05, 2023

**Cloud Monitoring**

v3

Feature

A new interface for creating charts with Metrics Explorer is in Public Preview. For more information, see [Create charts with Metrics Explorer](https://cloud.google.com/monitoring/charts/metrics-explorer).

## April 03, 2023

**Cloud Monitoring**

v3

Change

The time-range selector in select Cloud Monitoring pages has been updated to support a larger set of time range options, such as preset times, custom start and end times, and relative time ranges.

Feature

You can now configure metric-based alerting policies to send repeated notifications for open and acknowledged incidents. For more information, see [Send repeated notifications](https://cloud.google.com/monitoring/alerts/concepts-indepth#send-repeated-notifications).

## March 31, 2023

**Cloud Logging**

v2

Change

Effective 1 April 2023, storage costs apply to logs data retained longer than 30 days. For pricing details, see [ Cloud Logging pricing summary](https://cloud.google.com/stackdriver/pricing#logging-pricing-summary). Prior to 1 April 2023, there are no charges for retaining logs longer than 30 days. To review the billable storage for your log buckets, go to the **Logs Storage** page of the Google Cloud console.

## March 30, 2023

**Cloud Monitoring**

v3

Change

The link for the **Managed Prometheus** page in Cloud Monitoring now goes to the PromQL tab on the **Metrics Explorer** page.

## March 29, 2023

**Cloud Logging**

v2

Change

When you create a [log view](https://docs.cloud.google.com/logging/docs/logs-views) and use the [`source()`](https://docs.cloud.google.com/logging/docs/view/logging-query-language#source) function in your filter, the argument to the function is now validated to ensure that it is a single string representing a project, folder, billing account or organization.

## March 27, 2023

**Cloud Logging**

v2

Feature

The Cloud Logging API now supports the following region:

  * Doha: `me-central1`



## March 24, 2023

**Cloud Monitoring**

v3

Feature

**Google Cloud Managed Service for Prometheus** : You can use the OpenTelemetry Collector to scrape standard Prometheus metrics and report them to Managed Service for Prometheus. For more information, see [Get started with the OpenTelemetry Collector](https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-otel).

## March 22, 2023

**Cloud Logging**

v2

Change

Log buckets in the following regions can now be upgraded to use Log Analytics:

  * `asia-northeast1`
  * `australia-southeast1`
  * `europe-west1`
  * `europe-west2`
  * `northamerica-northeast1`
  * `us-east1`
  * `us-west2`



For more information, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## March 14, 2023

**Cloud Logging**

v2

Feature

The Logging Query Language now supports a built-in `SEARCH` function that you can use to find strings in your log data. The `SEARCH` function is in preview. For more information, see [`SEARCH` function](https://docs.cloud.google.com/logging/docs/view/logging-query-language#search-functions).

## March 10, 2023

**Cloud Logging**

v2

Feature

Starting with version 2.28.0, the Ops Agent limits the amount of disk space it can use to store buffer chunks. The Ops Agent creates buffer chunks when logging data can't be sent to the Logging API. Without a limit, these chunks might consume all available space, interrupting other services on the VM. When a network outage causes buffer chunks to be written to disk, the Ops Agent now uses a platform-specific amount of disk space to store the chunks.

Feature

[Log-based metrics on log buckets](https://docs.cloud.google.com/logging/docs/logs-based-metrics/bucket-lbm) are now [generally available](https://cloud.google.com/products/#product-launch-stages) (GA). In addition to features available in the preview, the GA release includes the ability to create bucket-level log-based metrics in the Google Cloud console.

**Cloud Monitoring**

v3

Feature

You can now have Cloud Monitoring send an email that contains a dashboard URL to people or groups in your organization. For more information, see [Share dashboards](https://cloud.google.com/monitoring/charts/share-dashboards).

## March 09, 2023

**Cloud Logging**

v2

Feature

You can now route logs through the Log Router of another Google Cloud project. The logs can then be managed by the other Google Cloud project, which includes log-based metrics, log-based alerts, and other log sinks. For more information, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

## March 08, 2023

**Cloud Monitoring**

v3

Feature

You can now use the gcloud CLI to configure a snooze, which prevents Cloud Monitoring from sending notifications or creating incidents during specific time periods. You can also configure a snooze by using the Google Cloud console and the API. For more information see [Create and manage snoozes](https://cloud.google.com/monitoring/alerts/manage-snooze).

## March 06, 2023

**Cloud Monitoring**

v3

Feature

You can now view and list incidents on your custom dashboards. For more information, see [Display incidents on a dashboard](https://cloud.google.com//monitoring/charts#add_incident_chart).

## March 01, 2023

**Cloud Logging**

v2

Change

Log buckets in the following regions can now be upgraded to use Log Analytics:

  * `us-central1`
  * `us-west1`
  * `asia-south1`



For more information, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

Change

You can now use the gcloud CLI to do the following:

  * Create a log bucket and upgrade that bucket to use Log Analytics.
  * Upgrade an existing log bucket to use Log Analytics.
  * Create a linked dataset in BigQuery.



For more information, see [Configure log buckets](https://docs.cloud.google.com/logging/docs/buckets).

## February 23, 2023

**Cloud Logging**

v2

Feature

The time-range selector in the Logs Explorer has been updated to support a larger set of time range options, such as preset times, custom start and end times, and relative time ranges. For more information, see [Use the time-range selector](https://docs.cloud.google.com/logging/docs/view/building-queries#time-range).

## February 17, 2023

**Cloud Logging**

v2

Feature

You can create log buckets that use Log Analytics and upgrade existing log buckets to use Log Analytics by using the Logging API. For more information, see [Create a bucket](https://docs.cloud.google.com/logging/docs/buckets#api).

**Cloud Monitoring**

v3

Feature

You can now install pre-defined alerting policies for services integrated with Cloud Monitoring from the Monitoring **Integrations** page and from the **Observability** tab on the pages for Kubernetes Engine clusters and workloads. For more information about these installable policies, see [Install alerting policies](https://cloud.google.com/monitoring/agent/integrations#install-alertpols).

Change

To view details of your user-defined metrics, use the **Metrics diagnostics** page, which can now be accessed through the navigation pane of Cloud Monitoring. For more information, see [View information about your user-defined metrics](https://cloud.google.com/monitoring/custom-metrics/diagnostics).

## February 16, 2023

**Cloud Logging**

v2

Feature

Version 2.25.1 of the Ops Agent introduces health checks. When the Ops Agent starts, it performs a series of checks for conditions that prevent the agent from running correctly. If the agent detects one of the conditions, it writes a message to its health-check log and exits. For more information, see [Find Ops Agent troubleshooting information](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-find-info).

**Cloud Monitoring**

v3

Feature

The Ops Agent now provides Preview support for NVIDIA GPU metrics, including metrics reported from the NVIDIA Management Library (NVML) and the Data Center GPU Manager (DCGM).

When you [install the GPU-enabled version of the Ops Agent](https://cloud.google.com/monitoring/agent/ops-agent/third-party-nvidia#install-oagent), NVML metrics are collected automatically. DGCM metrics are available as a third-party integration. For information about configuring the integration, see [NVIDIA Data Center GPU Manager](https://cloud.google.com/monitoring/agent/ops-agent/third-party-nvidia). The reference document for Ops Agent metrics includes tables for the [NVML metrics](https://cloud.google.com/monitoring/api/metrics_opsagent#agent-gpu) and the [DCGM metrics](https://cloud.google.com/monitoring/api/metrics_opsagent#agent-dcgm).

Feature

Version 2.25.1 of the Ops Agent introduces health checks. When the Ops Agent starts, it performs a series of checks for conditions that prevent the agent from running correctly. If the agent detects one of the conditions, it writes a message to its health-check log and exits. For more information, see [Find Ops Agent troubleshooting information](https://cloud.google.com/monitoring/agent/ops-agent/troubleshoot-find-info).

## February 15, 2023

**Cloud Monitoring**

v3

Change

You can now configure uptime checks to include a user-defined content-type header. For more information, see the [`customContentType`](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#HttpCheck.FIELDS.custom_content_type) field of the `UptimeCheckConfig` structure.

## February 09, 2023

**Cloud Monitoring**

v3

Change

The **Observability** tab is now available for GKE Deployments. To view the tab, navigate to the Kubernetes Engine **Workloads** page, click on the name of a Deployment, and then click the **Observability** tab.

## February 03, 2023

**Error Reporting**

v1beta1

Feature

Error Reporting now reports recent application errors for Google Kubernetes Engine workloads of type `Deployment` or `Pod`. Go to **Kubernetes Engine** in the Google Cloud console, and select **Workloads**. From the overview list, select an entry with type "Deployment" or "Pod" to see details about the workload, including recent application errors.

## February 01, 2023

**Cloud Logging**

v2

Change

To help you manage your costs, the **Logs Storage** page now displays the billable storage for the current month for each log bucket. For reference, this page also displays each log bucket's ingested bytes for the current and previous months.

## January 27, 2023

**Cloud Monitoring**

v3

Feature

The Ops Agent version 2.25.0 supports a receiver for Prometheus metrics. By using this receiver, you can collect Prometheus metrics from applications running on Compute Engine instances. For more information, see [Collect Prometheus metrics](https://cloud.google.com/monitoring/agent/ops-agent/prometheus).

## January 25, 2023

**Cloud Monitoring**

v3

Feature

Now the alerting policy can forecast, or predict, that the threshold will be violated within a configurable time window. These policies are designed to monitor constraint metrics like those that record quota, memory, and storage usage. Forecasting alerts is in Public Preview. For more information, see [Forecast condition](https://cloud.google.com/monitoring/alerts/types-of-conditions#forecast).

## January 20, 2023

**Cloud Monitoring**

v3

Change

You can now use the **Observability** tab on the Compute Engine **VM instances** page to see the five virtual machines consuming the most of a resource. For more information, see [Troubleshooting VM performance issues](https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-performance#viewing-performance-metrics).

## January 17, 2023

**Cloud Logging**

v2

Change

You can now save your SQL queries, and you can set custom retention periods on log buckets upgraded to use Log Analytics. For more information, see [Save a query](https://docs.cloud.google.com/logging/docs/analyze/query-and-view#save-query).

Change

Log Analytics is now GA. For more information, see [Configure log buckets](https://docs.cloud.google.com/logging/docs/buckets).

## January 12, 2023

**Error Reporting**

v1beta1

Change

Errors generated by GKE applications (that is, applications with a [`MonitoredResource`](https://cloud.google.com/logging/docs/reference/v2/rest/v2/MonitoredResource) type of `k8s_container`) now support additional labels for metadata extraction. The values of the following labels will now appear in the resource filter and in various tables and displays on **Error Reporting** pages in the Google Cloud console:

  * The `app` value from your [GKE YAML configuration](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) is now used for the primary resource label (also referred to as "service").
  * The `pod_name` label of the [`k8s_container`](https://cloud.google.com/logging/docs/api/v2/resource-list#tag_k8s_container) monitored-resource type is now used for the secondary resource label (also referred to as "version").



We continue to support the use of the YAML `metadata` labels `k8s-pod/serving_knative_dev/service` and `k8s-pod/serving_knative_dev/revision`. These labels are prioritized for users already using them over the `k8s-pod/app` and `pod_name` labels described in this note. But we encourage users to begin using the new labels.

If you do not set the `k8s-pod/app` label, GKE application errors continue to use the default service name of `gke_instances`.

## January 10, 2023

**Cloud Monitoring**

v3

Feature

**Managed Service for Prometheus** : Dashboards for exporter integrations are available and automatically installed when you configure the integration. You can also view static previews of dashboards without configuring the integration. For more information, see the exporter documentation at [Set up commonly used exporters](https://cloud.google.com/stackdriver/docs/managed-prometheus/exporters/introduction).

## January 09, 2023

**Cloud Monitoring**

v3

Change

Charts defined by Prometheus Query Language (PromQL) now support dashboard-wide filters and can be configured to support template variables. For more information, see [Create a permanent filter](https://cloud.google.com/monitoring/charts/filter-dashboard#create-permanent-filter).

## December 19, 2022

**Cloud Logging**

v2

Feature

Cloud Logging now supports the following regions:

  * `US`

  * `EU`




For more information, see [Data regionality for Cloud Logging](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## December 14, 2022

**Cloud Monitoring**

v3

Feature

You can now use the **Observability** tab on the Kubernetes Engine **Workloads** page to see the five workloads consuming the most of a resource. For more information, see [View cluster and workload observability metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics#view_metrics).

## December 13, 2022

**Cloud Monitoring**

v3

Feature

You can use the new **Map** view on the **VM Instances** dashboard to visualize the health of the resources in your fleet. Using the map, you can group VMs by resource labels, like "instance group" or "zone", and color the VMs by the value of a metric, like CPU utilization, to highlight hotspots and anomalies in your fleet.

## December 12, 2022

**Cloud Monitoring**

v3

Change

You can now use the Monitoring API to configure a snooze, which prevents Cloud Monitoring from sending notifications or creating incidents during specific time periods. You can also configure a snooze by using the Google Cloud console. For information about how to create, view, and modify a snooze, see [Create and manage snoozes](https://cloud.google.com/monitoring/alerts/manage-snooze).

## December 07, 2022

**Cloud Monitoring**

v3

Change

For public and private uptime checks, a new create flow is available in Public Preview. For private uptime checks, the Public Preview flow lets you create the Service Directory service and perform other prerequisite steps by using the Google Cloud console. For more information, see [Create public uptime checks](https://cloud.google.com/monitoring/uptime-checks) and [Create private uptime checks](https://cloud.google.com/monitoring/uptime-checks/private-checks).

## December 06, 2022

**Error Reporting**

v1beta1

Feature

On the Error Reporting page, use the new resource filter to filter error groups by resource type. For more information, see [Filter errors](https://cloud.google.com/error-reporting/docs/viewing-errors#filtering).

## December 01, 2022

**Error Reporting**

v1beta1

Feature

Error Reporting is a Virtual Private Cloud (VPC) supported service.

## November 11, 2022

**Cloud Monitoring**

v3

Change

Prometheus Query Language (PromQL) for creating charts and dashboards in Cloud Monitoring is now Generally Available. For more information, see [PromQL in Cloud Monitoring](https://cloud.google.com/monitoring/promql).

Feature

Cloud Monitoring now provides a **GKE Clusters** dashboard for enabling Managed Service for Prometheus on clusters in your project. For more information, see [Get started with managed collection](https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).

## November 08, 2022

**Cloud Trace**

v2

Change

The Trace scatterplot now indicates traces with error codes as red. For more information, see [Finding and viewing traces](https://cloud.google.com/trace/docs/finding-traces).

## November 07, 2022

**Cloud Logging**

v2

Feature

You can now dynamically include your log content in your alert notifications for easier troubleshooting. For more information about extracting log content into labels, see [Create a log-based alert (Monitoring API)](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-by-api).

**Cloud Monitoring**

v3

Feature

You can now dynamically include your log content in your alert notifications for easier troubleshooting. For more information about extracting log content into labels, see [Create a log-based alert (Monitoring API)](https://cloud.google.com/logging/docs/alerting/log-based-alerts#lba-by-api).

## November 04, 2022

**Cloud Logging**

v2

Feature

The **Logs** tab available for each cluster on the **Kubernetes Engine > Clusters** page now includes suggested queries for your logs. For more information about using your GKE logs, see [Viewing your GKE logs](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/using-logs#accessing_your_logs).

## November 03, 2022

**Cloud Logging**

v2

Change

You can now collect Aerospike logs from the Ops Agent, starting with version 2.22.0. For more information, see [Monitoring third-party applications: Aerospike](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/aerospike).

**Cloud Monitoring**

v3

Feature

You can now add table widgets to custom dashboards that let you limit the number of table rows, persiste specific columns, display only those rows with the highest, or lowest values, and that display a visual indicator of the value as compared to the range of possible values. For more information, see [Display data in tabular form on a dashboard](https://cloud.google.com/monitoring/charts#add_table).

## October 24, 2022

**Cloud Logging**

v2

Feature

You can now instrument gRPC applications to use [Microservices observability](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc).

Pricing for Microservices observability is the same as [Cloud Operations Pricing](https://cloud.google.com/stackdriver/pricing). There are no separate charges for using Cloud Trace, Cloud Monitoring, or Cloud Logging Microservices observability plugins.

**Cloud Monitoring**

v3

Feature

You can now instrument gRPC applications to use [Microservices observability](https://cloud.google.com/stackdriver/docs/solutions/grpc).

Pricing for Microservices observability is the same as [Cloud Operations Pricing](https://cloud.google.com/stackdriver/pricing). There are no separate charges for using Cloud Trace, Cloud Monitoring, or Cloud Logging Microservices observability plugins.

Change

A new version of Managed Service for Prometheus is now available. Version 0.5.0 of managed collection for Kubernetes has been released. Users who deploy managed collection using `kubectl` should [reapply the manifests](https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#config-mgd-collection). Users who deploy the service using `gcloud` or the GKE UI will be upgraded on a rolling basis over the coming weeks. This release has no impact on users of self-deployed collection.

For details about the changes included, see the [release page on GitHub](https://github.com/GoogleCloudPlatform/prometheus-engine/releases/tag/v0.5.0).

**Cloud Trace**

v2

Feature

You can now instrument gRPC applications to use [Microservices observability](https://cloud.google.com/stackdriver/docs/solutions/grpc).

Pricing for Microservices observability is the same as [Cloud Operations Pricing](https://cloud.google.com/stackdriver/pricing). There are no separate charges for using Cloud Trace, Cloud Monitoring, or Cloud Logging Microservices observability plugins.

## October 21, 2022

**Cloud Logging**

v2

Feature

To show or hide log entries similar to a log entry displayed in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), expand the log entry and use the **Similar entries** menu.

**Cloud Monitoring**

v3

Feature

The Cloud Monitoring **Integrations** page now provides access to logs collected by logs-enabled integrations from the **Details** page for each integration.

## October 20, 2022

**Cloud Monitoring**

v3

Change

Logs panels now display log entries on rows with separate columns for severity, the timestamp, and a summary of the log entry. You can click the **View log details** button to view the JSON-formatted representation of a log entry. For more information, see [View logs on a custom dashboard](https://cloud.google.com/monitoring/charts/view-logs).

## October 13, 2022

**Cloud Monitoring**

v3

Change

**SLO monitoring** : You can now define a set of generic services by using the Service Monitoring API. This change streamlines integration with tools like Terraform. For more information about defining generic services, see [Services](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#svc-structs).

## October 04, 2022

**Cloud Logging**

v2

Feature

You can now collect Oracle Database logs and metrics from the Ops Agent, starting with version 2.22.0. For more information, see [Monitoring third-party applications: Oracle Database](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/oracledb).

**Cloud Monitoring**

v3

Feature

You can now collect Oracle Database logs and metrics from the Ops Agent, starting with version 2.22.0. For more information, see [Monitoring third-party applications: Oracle Database](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/oracledb).

## September 30, 2022

**Cloud Monitoring**

v3

Feature

The set of pre-configured Monitoring dashboards now includes a **Microservices gRPC Overview** dashboard. If apps in your project emit [gRPC](https://github.com/census-instrumentation/opencensus-specs/blob/master/stats/gRPC.md#default-views) metrics, then this dashboard is automatically added to your list of available dashboards.

## September 28, 2022

**Cloud Monitoring**

v3

Change

You can now collect additional PostgreSQL metrics from the Ops Agent, starting with version 2.21.0. For more information, see [Monitoring third-party applications: PostgreSQL](https://cloud.google.com/monitoring/agent/ops-agent/third-party/postgresql).

Change

You can now collect additional Elasticsearch metrics from the Ops Agent, starting with version 2.21.0. For more information, see [Monitoring third-party applications: Elasticsearch](https://cloud.google.com/monitoring/agent/ops-agent/third-party/elasticsearch).

## September 27, 2022

**Cloud Logging**

v2

Feature

Using Log Analytics, you can run SQL queries that analyze your log data to generate useful insights. Log Analytics also let you use [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) to query your log data. For more information, see [Log Analytics](https://docs.cloud.google.com/logging/docs/log-analytics).

## September 26, 2022

**Cloud Monitoring**

v3

Feature

You can now use Prometheus Query Language (PromQL) when creating charts and dashboards in Cloud Monitoring. For more information, see [PromQL in Cloud Monitoring](https://cloud.google.com/monitoring/promql).

## September 20, 2022

**Cloud Logging**

v2

Feature

The Cloud Logging API now supports the following region:

  * Israel: `me-west1`.



## September 15, 2022

**Cloud Logging**

v2

Change

Support for adding [custom indexed `LogEntry` fields](https://docs.cloud.google.com/logging/docs/analyze/custom-index) to your Cloud Logging buckets is now Generally Available. These indexes make querying your logs data faster.

## September 13, 2022

**Cloud Monitoring**

v3

Change

You can now configure public uptime checks to send ICMP pings as part of the check. The results of the pings are sent to Cloud Logging to help you troubleshoot failed checks. For more information, see [Use ICMP pings](https://cloud.google.com/monitoring/uptime-checks#ping).

## September 08, 2022

**Cloud Logging**

v2

Change

Cloud Audit Logging no longer redacts the principal email associated with service accounts in audit logs. For more information, see [Caller identities in audit logs](https://docs.cloud.google.com/logging/docs/audit#user-id).

## August 30, 2022

**Cloud Monitoring**

v3

Change

You can now collect additional MongoDB metrics from the Ops Agent, starting with version 2.19.0. For more information, see [Monitoring third-party applications: MongoDB](https://cloud.google.com/monitoring/agent/ops-agent/third-party/mongodb).

## August 29, 2022

**Cloud Monitoring**

v3

Feature

You can now manage Monitoring-specific roles by using the Cloud Monitoring pages in the Google Cloud console. For more information, see [Grant access to Cloud Monitoring](https://cloud.google.com/monitoring/access-control#grant-monitoring-access).

## August 25, 2022

**Cloud Monitoring**

v3

Change

There are new filtering capabilities for the [`projects.uptimeCheckConfig.list`](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/list) API method. For more information, see [`UptimeCheckConfig`](https://cloud.google.com/monitoring/api/v3/sorting-and-filtering#uptimecheckconfig).

## August 17, 2022

**Cloud Monitoring**

v3

Announcement

Cloud Monitoring is introducing pricing for uptime checks, effective October 1, 2022. For more information, see [Cloud Monitoring pricing summary](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary).

## August 15, 2022

**Cloud Logging**

v2

Feature

Bucket-level log-based metrics are now available in [Preview](https://cloud.google.com/products#product-launch-stages). You can now create log-based metrics that are computed from the logs routed to a specific log bucket. For more information, see [Log-based metrics on log buckets](https://docs.cloud.google.com/logging/docs/logs-based-metrics/bucket-lbm).

**Cloud Monitoring**

v3

Feature

The GKE **Clusters List** page now includes a new **Observability** tab that displays Monitoring data. This tab shows infrastructure health metric trends such as CPU, memory, container restarts and control-plane metrics. It also provides visibility into ingestion into Google Cloud Managed Service for Prometheus and Cloud Logging. For more information, see [View observability metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).

## August 11, 2022

**Cloud Monitoring**

v3

Feature

You can now prevent Cloud Monitoring from sending notifications or creating incidents during specific time periods. For general information, see [Snooze notifications and alerts](https://cloud.google.com/monitoring/alerts/snooze). For information about how to create, view, and modify a snooze, see [Create and manage snoozes](https://cloud.google.com/monitoring/alerts/manage-snooze).

Change

You can now update older versions of the Ops Agent from the Cloud Monitoring **VM Instances** page and from the **Details** panel for a selected Compute Engine instance. The "Install" option for a new agent now also supports "update" for upgrading an older agent.

Change

The Cloud Monitoring **Integrations** page now provides information about integrations with other Google Cloud services, enhanced filtering, and additional information about available third-party integrations. For more information, see [Manage integrations](https://cloud.google.com/monitoring/agent/integrations).

## August 10, 2022

**Cloud Monitoring**

v3

Change

You can now create uptime checks for Cloud Run public endpoints by using the [Monitoring API](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#UptimeCheckConfig.FIELDS.monitored_resource) and specifying the [Cloud Run Revision](https://cloud.google.com/monitoring/api/resources#tag_cloud_run_revision) monitored-resource type.

## August 09, 2022

**Cloud Monitoring**

v3

Change

The organization of the SLO monitoring **Services Overview** page has been improved. The new layout provides a better experience when you don't yet have any services. When you have services, the new **Supported Services** list indicates how many of each type you have. You can also use the list to filter the services table to include all services of a selected type. For more information, see [Services Overview dashboard](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/svc-overview#svc-overview).

## August 04, 2022

**Cloud Logging**

v2

Feature

The Logs Explorer query results now show an icon for log entries that are part of error groups. You can click the icon to view details about the error group, exclude or show only log entries from the error group in the query results, or view related documentation. For more information, see [Find log entries with error groups](https://docs.cloud.google.com/logging/docs/analyze/find-logs-error-groups).

## July 29, 2022

**Cloud Monitoring**

v3

Feature

You can now add table widgets to custom dashboards that let you limit the number of table rows, display only those rows with the highest, or lowest values, and that display a visual indicator of the value as compared to the range of possible values. For more information, see [Display data in tabular form on a dashboard](https://cloud.google.com/monitoring/charts#add_table).

## July 28, 2022

**Cloud Monitoring**

v3

Change

You can now configure the acceptable response codes for public and private HTTP Uptime checks. For more information, see [Create public uptime checks](https://cloud.google.com/monitoring/uptime-checks).

Feature

You can now add user-defined labels to public and private Uptime checks. For more information, see [Create public uptime checks](https://cloud.google.com/monitoring/uptime-checks).

## July 26, 2022

**Cloud Logging**

v2

Feature

You can now collect Couchbase logs and metrics from the Ops Agent, starting with version 2.18.2. For more information, see [Monitoring third-party applications: Couchbase](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/couchbase).

**Cloud Monitoring**

v3

Feature

You can now collect Aerospike metrics from the Ops Agent, starting with version 2.18.2. For more information, see [Monitoring third-party applications: Aerospike](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/aerospike).

Feature

You can now collect Couchbase logs and metrics from the Ops Agent, starting with version 2.18.2. For more information, see [Monitoring third-party applications: Couchbase](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/couchbase).

Feature

You can now collect Vault metrics from the Ops Agent, starting with version 2.18.2. For more information, see [Monitoring third-party applications: Vault](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/vault).

## July 19, 2022

**Cloud Monitoring**

v3

Change

A new version of Managed Service for Prometheus is now available. Version 0.4.3-gke-0 of managed collection for Kubernetes has been released. Users who deploy managed collection using `kubectl` should [reapply the manifests](https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#config-mgd-collection). Users who deploy the service using `gcloud` or the GKE UI will be upgraded on a rolling basis over the coming weeks. This release has no impact on users of self-deployed collection.

For details about the changes included, see the [release page on GitHub](https://github.com/GoogleCloudPlatform/prometheus-engine/releases/tag/v0.4.3-gke.0).

## July 18, 2022

**Cloud Logging**

v2

Feature

You can now search your correlated log entries in the Logs Explorer. For more information, see [Correlate log entries](https://docs.cloud.google.com/logging/docs/view/correlate-logs).

## July 15, 2022

**Cloud Logging**

v2

Feature

You can now collect SAP HANA logs and metrics from the Ops Agent, starting with version 2.18.1. For more information, see [Monitoring third-party applications: SAP HANA](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/saphana).

Feature

You can now collect Vault logs from the Ops Agent, starting with version 2.18.1. For more information, see [Monitoring third-party applications: Vault](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party#vault).

**Cloud Monitoring**

v3

Feature

You can now collect SAP HANA logs and metrics from the Ops Agent, starting with version 2.18.1. For more information, see [Monitoring third-party applications: SAP HANA](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/saphana).

Feature

You can now collect Flink metrics from the Ops Agent, starting with version 2.18.1. For more information, see [Monitoring third-party applications: Flink](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/flink).

## July 14, 2022

**Cloud Logging**

v2

Change

Log-based alerting is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Log-based alerts match on the content of your logs. When triggered, a log-based alert notifies you that a match has appeared in your logs and opens an incident in Cloud Monitoring. The minimum autoclose duration for incidents is now 30 minutes. For more information, see [Monitor your logs](https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs) and [Use log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

**Cloud Monitoring**

v3

Change

Log-based alerting is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Log-based alerts match on the content of your logs. When triggered, a log-based alert notifies you that a match has appeared in your logs and opens an incident in Cloud Monitoring. The minimum autoclose duration for incidents is now 30 minutes. For more information, see [Monitor your logs](https://cloud.google.com/logging/docs/alerting/monitoring-logs) and [Use log-based alerts](https://cloud.google.com/logging/docs/alerting/log-based-alerts).

## July 11, 2022

**Error Reporting**

v1beta1

Feature

The Logs Explorer now shows an Error Group button for log entries that are part of error groups. Click the button to access grouping details or to change which log entries the Logs Explorer shows. For more information, see [Find log entries with error groups](https://cloud.google.com/logging/docs/analyze/find-logs-error-groups).

## June 30, 2022

**Cloud Monitoring**

v3

Feature

**Managed Service for Prometheus** : You can now query Cloud Monitoring metrics by using PromQL. For more information, see [Mapping Monitoring metric names to PromQL](https://cloud.google.com/stackdriver/docs/managed-prometheus/promql#transforming-names).

## June 29, 2022

**Cloud Logging**

v2

Feature

You can now collect Apache Flink logs from the Ops Agent, starting with version 2.17.0. For more information, see [Monitoring third-party applications: Flink](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/flink).

## June 28, 2022

**Cloud Monitoring**

v3

Change

The new experience for creating metric-based alerting policies by using the Google Cloud console is now Generally Available. For more information, see [Create metric-based alert policy](https://cloud.google.com/monitoring/alerts/using-alerting-ui).

## June 27, 2022

**Cloud Logging**

v2

Change

The Cloud Logging agent version 1-18 for Windows is now available. This version updates the location of the position files so they are retained across upgrades. For installation information, see [Installing the Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging/install-index).

## June 24, 2022

**Cloud Monitoring**

v3

Feature

You can now collect Jetty metrics from the Ops Agent, starting with version 2.17.0. For more information, see [Monitoring third-party applications: Jetty](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/jetty).

Feature

You can now view the configuration of charts on a dashboard while the dashboard is in read-only mode. For more information, see [Show the chart configuration](https://cloud.google.com/monitoring/charts/working-with-charts#view-config).

## June 03, 2022

**Cloud Monitoring**

v3

Feature

You can now add, edit, and remove alerting policy user labels by using the Cloud console when you use the preview alerting interface. To configure policy labels, edit the policy and go to the **Notifications and name** step. For more information, see [Create an alerting policy](https://cloud.google.com/monitoring/alerts/using-alerting-ui#create-policy).

## May 30, 2022

**Cloud Logging**

v2

Announcement

The Logs Explorer has now replaced the Legacy Log Viewer.

The Logs Explorer is the updated version of the Logging interface, and lets you quickly and efficiently retrieve, view, and analyze logs from your queries. For a detailed tour of the Logs Explorer's features, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

## May 27, 2022

**Cloud Logging**

v2

Change

Support has been removed for two previously deprecated system metrics: `logging.googleapis.com/excluded_log_entry_count` and `logging.googleapis.com/excluded_byte_count`.

## May 26, 2022

**Cloud Logging**

v2

Feature

You can now collect IIS logs and additional metrics from the Ops Agent, starting with versions 2.14.0 (logs) and 2.15.0 (additional metrics). For more information, see [Monitoring third-party applications: IIS](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/iis).

Feature

You can now collect Jetty logs from the Ops Agent, starting with version 2.16.0. For more information, see [Monitoring third-party applications: Jetty](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/jetty).

Feature

You can now collect Active Directory Domain Services logs and metrics from the Ops Agent, starting with version 2.15.0. For more information, see [Monitoring third-party applications: Active Directory Domain Services](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/active_directory_ds).

Feature

You can now collect Varnish logs and metrics from the Ops Agent, starting with versions 2.16.0 (logs) and 2.15.0 (metrics). For more information, see [Monitoring third-party applications: Varnish](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/varnish).

**Cloud Monitoring**

v3

Change

A new version of Managed Service for Prometheus is now available. Version 0.4.1 of managed collection has been released, along with v2.35.0-gmp.2 of the managed-service binary that v0.4.1 depends on (container image: `gke.gcr.io/prometheus-engine/prometheus:v2.35.0-gmp.2-gke.0`). For details about the changes included, see the [release page on GitHub](https://github.com/GoogleCloudPlatform/prometheus-engine/releases/tag/v0.4.1).

Feature

You can now configure an uptime check to validate a specific JSONpath. For more information, see [Validate response data](https://cloud.google.com/monitoring/uptime-checks/response-validation).

Feature

You can now collect IIS logs and additional metrics from the Ops Agent, starting with versions 2.14.0 (logs) and 2.15.0 (additional metrics). For more information, see [Monitoring third-party applications: IIS](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/iis).

Feature

You can now collect Varnish logs and metrics from the Ops Agent, starting with versions 2.16.0 (logs) and 2.15.0 (metrics). For more information, see [Monitoring third-party applications: Varnish](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/varnish).

Feature

You can now collect Active Directory Domain Services logs and metrics from the Ops Agent, starting with version 2.15.0. For more information, see [Monitoring third-party applications: Active Directory Domain Services](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/active_directory_ds).

## May 20, 2022

**Cloud Logging**

v2

Feature

You can now see more log entries in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) as a result of several style changes.

## May 16, 2022

**Cloud Monitoring**

v3

Change

The pricing for [Google Cloud Managed Service for Prometheus](https://cloud.google.com/stackdriver/docs/managed-prometheus) has been reduced by 25-50%, depending on volume and usage. Existing pricing tiers have been reduced by 25%, and a new high-volume tier has been added at 50% of the current cost. For pricing details, see [Cloud Monitoring pricing summary](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary), and for a set of examples, see [Pricing examples based on samples ingested](https://cloud.google.com/stackdriver/pricing#pricing_examples_samples).

## May 11, 2022

**Cloud Monitoring**

v3

Change

Private uptime checks are now generally available. Private uptime checks enable HTTP requests into a customer Virtual Private Cloud (VPC) network while enforcing Identity and Access Management (IAM) restrictions and VPC Service Controls perimeters. Private uptime checks can send requests over the private network to resources like a virtual machine (VM) or an L4 internal load balancer (ILB).

For more information, see [Create private uptime checks](https://cloud.google.com/monitoring/uptime-checks/private-checks).

## May 06, 2022

**Cloud Monitoring**

v3

Feature

You can now configure Metrics Explorer and charts on dashboards to display a ratio of metrics by using the Cloud Console. For more information, see [Ratios of metrics](https://cloud.google.com/monitoring/charts/metric-ratios).

## May 05, 2022

**Cloud Logging**

v2

Feature

You can now hide large amounts of similar log entries from your query results in the Logs Explorer. To learn more, see [Hide similar logs](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#hide-similar-logs).

**Cloud Monitoring**

v3

Change

**SLO monitoring** : Cloud Monitoring can now detect potential GKE- and Cloud Run-based services in your project. Monitoring provides a list of such candidate services, and you can now identify the candidates you want to monitor and create SLOs for them by using the Cloud Console. For more information, see [Defining a microservice](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/define-svc).

## April 28, 2022

**Cloud Logging**

v2

Feature

You can now comment within your Logging queries. For more information, see [Logging query language: comments](https://docs.cloud.google.com/logging/docs/view/logging-query-language#comments).

**Error Reporting**

v1beta1

Feature

**Preview** : You can now get notification recommendations and insights for Error Reporting. For more information, see [Error Reporting notification recommender and insights](https://cloud.google.com/recommender/docs/error-reporting/notification-recommender).

## April 26, 2022

**Cloud Logging**

v2

Feature

You can now do the following in the improved Logs Explorer:

  * Use the new [plain-text search field](https://docs.cloud.google.com/logging/docs/view/building-queries#search-text) and [filter menus ](https://docs.cloud.google.com/logging/docs/view/building-queries#query-builder-menus) to construct queries without using the query language
  * Customize your [date and time format preferences](https://docs.cloud.google.com/logging/docs/view/building-queries#time-range) for building queries and to display dates and times in the UI.
  * Toggle on and off the default [summary fields](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#add_summary_fields) to see a raw-text view of your logs.



Feature

When querying your logs data in the Logs Explorer, you can now [select queries from a library](https://logging/docs/view/building-queries#library-queries), making it easier to explore your data and find logs during time-critical troubleshooting sessions.

## April 25, 2022

**Cloud Logging**

v2

Feature

The Cloud Logging API now supports the following regions:

  * Europe: 
    * `europe-southwest1`
    * `europe-west6`
    * `europe-west8`
    * `europe-west9`
  * South America: 
    * `southamerica-west1`



For more information, see [Data Regionality for Cloud Logging](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

## April 14, 2022

**Cloud Logging**

v2

Feature

In the Logs Explorer, pinning log entries has been improved and new options to view pinned log entries in different resource contexts have been added. To learn more, see [Pin log entries](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#pin-logs).

**Cloud Monitoring**

v3

Feature

You can now define template variables and permanent filters for your dashboards. For more information, see [Create a template variable or permanent filter](https://cloud.google.com/monitoring/charts/filter-dashboard#create-permanent-filter).

## April 04, 2022

**Cloud Logging**

v2

Change

You can now [add indexed `LogEntry` fields](https://docs.cloud.google.com/logging/docs/analyze/custom-index) to your Cloud Logging buckets to make querying your logs data faster.

## March 28, 2022

**Cloud Monitoring**

v3

Feature

User-defined labels are now included in PagerDuty, Pub/Sub, Webhooks, and email notifications, and you can also view these labels on the details pages of alerting policies and incidents. To learn how you can create user-defined labels that contain severity information and attach those labels to alerting policies or incidents, see [Add severity levels to an alerting policy](https://cloud.google.com/monitoring/alerts/labels).

**Error Reporting**

v1beta1

Change

Error Reporting now supports Webhooks and Slack as notification channels. For more information, see [Create notification channel](https://cloud.google.com/error-reporting/docs/notifications).

## March 25, 2022

**Cloud Logging**

v2

Feature

Cloud Logging now supports organization policies that can enforce CMEK protection. For information, see [CMEK organization policies](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage#org-policy).

## March 21, 2022

**Cloud Logging**

v2

Change

Customer-managed encryption keys (CMEK) for Logs Storage are now Generally Available (GA). CMEK lets you create, control, and manage encryption keys to meet your data compliance needs. For details, see [Manage the keys that protect Logging storage data ](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage).

## March 11, 2022

**Cloud Logging**

v2

Feature

You can now collect RabbitMQ logs from the Ops Agent, starting with version 2.12.0. For more information, see [Monitoring third-party applications: RabbitMQ](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/rabbitmq).

**Cloud Monitoring**

v3

Feature

You can now collect WildFly metrics from the Ops Agent, starting with version 2.12.0. For more information, see [Monitoring third-party applications: WildFly](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/wildfly).

## March 04, 2022

**Cloud Monitoring**

v3

Feature

You can now organize your dashboard widgets into collapsible groups. For more information, see [Organize dashboard widgets](https://cloud.google.com/monitoring/charts#organize_widgets).

## February 28, 2022

**Cloud Monitoring**

v3

Change

**GA** : Google Cloud Managed Service for Prometheus, Google Cloud's fully managed, Prometheus-compatible monitoring solution, is now generally available. You can use the managed service anywhere that you use standard Prometheus today. The collector retains all expected Prometheus functionality, such as local storage and rule evaluation.

Managed Service for Prometheus also offers managed data collection in Kubernetes environments, reducing the complexity of deploying, scaling, sharding, configuring, and maintaining the collectors. For more information, see [Google Cloud Managed Service for Prometheus](https://cloud.google.com/stackdriver/docs/managed-prometheus/).

## February 22, 2022

**Cloud Logging**

v2

Feature

You can now collect Apache CouchDB logs from the Ops Agent, starting with version 2.11.0. For more information, see [Monitoring third-party applications: CouchDB](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/couchdb).

Feature

You can now collect Apache HBase logs and metrics from the Ops Agent, starting with version 2.11.0. For more information, see [Monitoring third-party applications: HBase](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/hbase).

Feature

You can now collect Apache Hadoop logs and metrics from the Ops Agent, starting with version 2.11.0. For more information, see [Monitoring third-party applications: Hadoop](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/hadoop).

Feature

You can now collect Apache ZooKeeper logs from the Ops Agent, starting with version 2.11.0. For more information, see [Monitoring third-party applications: ZooKeeper](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/zookeeper).

Feature

You can now collect WildFly logs from the Ops Agent, starting with version 2.11.0. For more information, see [Monitoring third-party applications: WildFly](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/wildfly).

**Cloud Monitoring**

v3

Feature

You can now collect Apache HBase metrics and logs from the Ops Agent, starting with version 2.11.0. For more information, see [Monitoring third-party applications: HBase](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/hbase).

Feature

You can now collect MongoDB metrics from the Ops Agent, starting with version 2.11.0. For more information, see [Monitoring third-party applications: MongoDB](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/mongodb).

Change

Metrics Explorer and charts on dashboards have a new metric selection interface. For more information, see [Select metrics when using Metrics Explorer](https://cloud.google.com/monitoring/charts/metrics-selector).

Feature

You can now collect RabbitMQ metrics from the Ops Agent, starting with version 2.11.0. For more information, see [Monitoring third-party applications: RabbitMQ](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/rabbitmq).

Feature

You can now collect Apache ActiveMQ metrics from the Ops Agent, starting with version 2.11.0. For more information, see [Monitoring third-party applications: ActiveMQ](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/activemq).

Feature

You can now collect Apache Hadoop metrics and logs from the Ops Agent, starting with version 2.11.0. For more information, see [Monitoring third-party applications: Hadoop](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/hadoop).

## February 17, 2022

**Cloud Monitoring**

v3

Change

You can now configure how missing data is treated in alerting policies. Currently, if data stops arriving, the alerting policy repeats the previous measurement, so open incidents stay open. You can now treat missing data as violating the condition so an active condition stays active, or treat it as non-violating so that an active condition closes. For more information, see [Partial metric data](https://cloud.google.com/monitoring/alerts/concepts-indepth#partial-metric-data).

Breaking

The `install-monitoring-agent.sh` installation script for the Cloud Monitoring agent for Linux [has been decommissioned](https://cloud.google.com/stackdriver/docs/deprecations/mon-agent-install). See the [Installing the Cloud Monitoring agent](https://cloud.google.com/monitoring/agent/install-agent#joint-install) guide for the latest installation procedures.

## February 14, 2022

**Cloud Logging**

v2

Feature

You can now configure default storage regions and disabled `_Default` sinks for your Google Cloud organizations and all of their new projects and folders. For details, see [Configure default resource settings for Logging](https://docs.cloud.google.com/logging/docs/default-settings).

Feature

You can now collect Apache Kafka metrics and logs from the Ops Agent, starting with version 2.10.0. For more information, see [Monitoring third-party applications: Kafka](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/kafka).

Feature

You can now collect MongoDB logs from the Ops Agent, starting with version 2.10.0. For more information, see [Collect logs from third-party applications: MongoDB](https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/mongodb).

Feature

You can now collect Apache Solr metrics and logs from the Ops Agent, starting with version 2.10.0. For more information, see [Monitoring third-party applications: Solr](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/solr).

**Cloud Monitoring**

v3

Feature

You can now collect Apache Solr metrics and logs from the Ops Agent, starting with version 2.10.0. For more information, see [Monitoring third-party applications: Solr](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/solr).

Feature

You can now collect Elasticsearch metrics from the Ops Agent, starting with version 2.10.0. For more information, see [Monitoring third-party applications: Elasticsearch](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/elasticsearch).

Feature

You can now collect Apache CouchDB metrics from the Ops Agent, starting with version 2.10.0. For more information, see [Monitoring third-party applications: CouchDB](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/couchdb).

Feature

You can now collect Apache Kafka metrics and logs from the Ops Agent, starting with version 2.10.0. For more information, see [Monitoring third-party applications: Kafka](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/kafka).

Feature

You can now collect Apache ZooKeeper metrics from the Ops Agent, starting with version 2.10.0. For more information, see [Monitoring third-party applications: ZooKeeper](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/zookeeper).

## February 10, 2022

**Cloud Logging**

v2

Feature

Your regional preferences, including date and time formatting, are now supported in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#time-range).

## February 09, 2022

**Cloud Logging**

v2

Feature

Compute Engine resource names, alongside their corresponding resource IDs, are now supported in the Logs Explorer. For details, see [View Compute Engine logs](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#compute-engine).

## February 08, 2022

**Cloud Monitoring**

v3

Change

You can now configure private uptime checks by using the Cloud Console. For more information, see [Create private uptime checks](https://cloud.google.com/monitoring/uptime-checks/private-checks).

Feature

You can now view information about your user-defined metrics by using the **Diagnostics** tab located on the **Metrics Explorer** page. The **Diagnostics** tab displays summary information about the user-defined metrics your project injests, charts usage metrics, lists all user-defined metrics. You can use features on this page to create alerts, view audit logs, and get detailed information about individual metrics. For more information, see [View metric diagnostics](https://cloud.google.com/monitoring/custom-metrics/diagnostics).

## February 07, 2022

**Cloud Monitoring**

v3

Feature

Using the new **Integrations** page in the Google Cloud console, you can now configure third-party application integrations that the [Ops Agent](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent) supports. The **Integrations** page provides links to install instructions, displays example dashboards, and lists the metrics and logs that the Ops Agent collects for each integration. For more information, see [Manage integrations](https://cloud.google.com/monitoring/agent/integrations)

## February 03, 2022

**Cloud Monitoring**

v3

Feature

You can now save a copy of a chart on a predefined dashboard to one of your custom dashboards by selecting **Add to Custom Dashboard** from the **More Options** menu on the chart. When you select a custom dashboard, you also have the option of renaming the copied chart.

## February 01, 2022

**Cloud Monitoring**

v3

Feature

You can now view SLOs on a custom dashboard. For more information, see [Display SLOs on a dashboard](https://cloud.google.com/monitoring/charts#add_slo_chart).

## January 26, 2022

**Cloud Logging**

v2

Feature

You can now collect Apache Tomcat metrics and logs from the Ops Agent, starting with version 2.9.0. For more information, see [Monitoring third-party applications: Apache Tomcat](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/tomcat).

Feature

You can now collect PostgreSQL metrics and logs from the Ops Agent, starting with version 2.9.0. For more information, see [Monitoring third-party applications: PostgreSQL](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/postgresql).

Feature

Starting with Ops Agent version 2.9.0, you can use the `exclude_logs` logging processor to prevent the Ops Agent from ingesting specific logs. For more information, see [Logging processors](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#logging-processors).

Feature

You can now collect Elasticsearch logs from the Ops Agent, starting with version 2.9.0. For more information, see [Monitoring third-party applications: Elasticsearch](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/elasticsearch).

**Cloud Monitoring**

v3

Feature

You can now collect Apache Tomcat metrics and logs from the Ops Agent, starting with version 2.9.0. For more information, see [Monitoring third-party applications: Apache Tomcat](https://cloud.google.com/monitoring/agent/ops-agent/third-party/tomcat).

Feature

You can now collect PostgreSQL metrics and logs from the Ops Agent, starting with version 2.9.0. For more information, see [Monitoring third-party applications: PostgreSQL](https://cloud.google.com/monitoring/agent/ops-agent/third-party/postgresql).

## January 21, 2022

**Cloud Monitoring**

v3

Change

Private uptime checks are now available in Preview. Private uptime checks enable HTTP requests into a customer Virtual Private Cloud (VPC) network while enforcing Identity and Access Management (IAM) restrictions and VPC Service Controls perimeters. Private uptime checks can send requests over the private network to resources like a virtual machine (VM) or an L4 internal load balancer (ILB).

For more information, see [Create private uptime checks](https://cloud.google.com/monitoring/uptime-checks/private-checks).

## January 18, 2022

**Cloud Monitoring**

v3

Change

When you click on an entry in the **Instances** table on the Monitoring **VM Instances** dashboard, a sliding panel now appears with the instance details, replacing the **VM Instance Details** page.

## January 11, 2022

**Cloud Monitoring**

v3

Change

Cloud Monitoring now supports configuring HTTP POST uptime checks in the UI. For more information, see [Managing uptime checks](https://cloud.google.com/monitoring/uptime-checks).

## January 07, 2022

**Cloud Logging**

v2

Feature

You can now collect MariaDB metrics and logs from the Ops Agent, starting with version 2.8.0. For more information, see [Monitoring third-party applications: MariaDB](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/mariadb).

**Cloud Monitoring**

v3

Feature

You can now collect MariaDB metrics and logs from the Ops Agent, starting with version 2.8.0. For more information, see [Monitoring third-party applications: MariaDB](https://cloud.google.com/monitoring/agent/ops-agent/third-party/mariadb).

Feature

Starting with version 2.8.0, the Ops Agent supports Ubuntu 21.10. For more information, see [Linux operating systems](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#linux_operating_systems).

Feature

You can now collect Memcached metrics from the Ops Agent, starting with version 2.8.0. For more information, see [Monitoring third-party applications: Memcached](https://cloud.google.com/monitoring/agent/ops-agent/third-party/memcached).

Feature

You can now collect MySQL metrics from the Ops Agent, starting with version 2.8.0. For more information, see [Monitoring third-party applications: MySQL](https://cloud.google.com/monitoring/agent/ops-agent/third-party/mysql).

## December 15, 2021

**Cloud Monitoring**

v3

Change

The Slack notification channel for alerting is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). You can now test your connection from Google Cloud when adding new Slack channels. The notification has been updated with the latest template and now includes your resource, system, and user labels. For more information, see [Creating channels](https://cloud.google.com/monitoring/support/notification-options#slack).

## December 14, 2021

**Cloud Monitoring**

v3

Change

The Pub/Sub notification channel for alerting is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). You can now test your connection from Google Cloud when adding new Pub/Sub channels. For more information, see [Creating channels](https://cloud.google.com/monitoring/support/notification-options#pubsub).

## November 24, 2021

**Cloud Monitoring**

v3

Change

The date on which pricing for Monitoring data ingested by using GKE workload metrics goes into effect has changed. [Pricing](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary) is now effective on February 1, 2022.

## November 22, 2021

**Cloud Logging**

v2

Deprecated

On or after March 1, 2022, the [Legacy Logs Viewer will be shut down](https://docs.cloud.google.com/logging/docs/view/log-viewer-shutdown) and all users will be redirected to use the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-viewer-preview).

## November 18, 2021

**Cloud Monitoring**

v3

Feature

Cloud Monitoring now supports dashboard-wide grouping and filtering. For more information, see [Dashboard-wide filters](https://cloud.google.com/monitoring/charts/filter-dashboard).

## November 15, 2021

**Cloud Monitoring**

v3

Announcement

**Preview** : Google Cloud Managed Service for Prometheus, Google Cloud's fully managed, Prometheus-compatible monitoring solution, is now available in Preview. You can use the managed service anywhere that you use standard Prometheus today. The collector retains all expected Prometheus functionality, such as local storage and rule evaluation.

Managed Service for Prometheus also offers managed data collection in Kubernetes environments, reducing the complexity of deploying, scaling, sharding, configuring, and maintaining the collectors. For more information, see [Google Cloud Managed Service for Prometheus](https://cloud.google.com/stackdriver/docs/managed-prometheus/).

## November 11, 2021

**Cloud Monitoring**

v3

Feature

You can now view the project-scoped log entries for all projects in a metrics scope on a custom dashboard. For more information, see [View logs on a dashboard](https://cloud.google.com/monitoring/charts/view-logs).

## November 08, 2021

**Cloud Monitoring**

v3

Feature

You can now save a copy of a chart from the **Observability** tab on Compute Engine's **VM instance details** page to one of your custom dashboards. To save a copy of the chart, select **Add to Custom Dashboard** from the **More Options** menu on the chart. You then select a new or existing custom dashboard, and have the option of renaming the new copy of the chart.

Change

The API to manage the [metrics scope](https://cloud.google.com/monitoring/settings#concept-scope) of a Google Cloud project is now Generally Available. For more information, see [Manage metrics scopes with the API](https://cloud.google.com/monitoring/settings/manage-api).

Terraform now supports use of the metrics scope API. For sample code, see [`google_monitoring_monitored_project`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/monitoring_monitored_project).

## November 05, 2021

**Cloud Monitoring**

v3

Feature

You can now collect Redis metrics from the Ops Agent, starting with version 2.7.0. For more information, see [Monitoring third-party applications: Redis](https://cloud.google.com/monitoring/agent/ops-agent/third-party/redis).

Feature

You can now collect Apache Web Server metrics from the Ops Agent, starting with version 2.7.0. For more information, see [Monitoring third-party applications: Apache Web Server](https://cloud.google.com/monitoring/agent/ops-agent/third-party/apache).

## November 04, 2021

**Cloud Monitoring**

v3

Feature

You can now create an alerting policy from the alert chart dialog on a custom dashboard, and you can create an alerting policy by converting a chart on custom dashboard to an alert chart. For more information, see [Alert charts](https://cloud.google.com/monitoring/charts#add_alert_chart).

Change

Data from closed incidents is now retained for 13 months instead of 90 days, so you can see patterns over longer periods of time and investigate them. For information about investigating incidents, see [Incidents](https://cloud.google.com/monitoring/alerts/incidents-events).

## November 01, 2021

**Cloud Monitoring**

v3

Feature

You can now collect Cassandra metrics from the Ops Agent, starting with version 2.6.0. For more information, see [Monitoring third-party applications: Cassandra](https://cloud.google.com/monitoring/agent/ops-agent/third-party/cassandra).

## October 20, 2021

**Cloud Logging**

v2

Feature

You can now collect Redis logs from the Ops Agent, starting with version 2.5.0. For more information, see [Collecting logs from third-party applications: Redis](https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/redis).

Feature

You can now collect MySQL logs from the Ops Agent, starting with version 2.5.0. For more information, see [Collecting logs from third-party applications: MySQL](https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/mysql).

Feature

You can now collect Cassandra logs from the Ops Agent, starting with version 2.5.0. For more information, see [Collecting logs from third-party applications: Cassandra](https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/cassandra).

## October 11, 2021

**Cloud Logging**

v2

Change

Cloud Logging now supports the asia-south2, asia-southeast2, australia-southeast2, northamerica-northeast2, and us-west4 regions. For a full list or regions, see [Regionalization](https://docs.cloud.google.com/logging/docs/storage#regionalization).

## October 06, 2021

**Cloud Logging**

v2

Feature

The Ops Agent now supports collecting logs from the systemd-journald service, starting with Ops Agent version 2.4.0. For information on configuring the `systemd_journald` receiver, see [Configuring the Ops Agent: Logging receivers](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#logging-receivers).

Feature

You can now collect Apache httpd logs from the Ops Agent, starting with version 2.4.0. For more information, see [Collecting logs from third-party applications: Apache httpd](https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/apache).

## October 04, 2021

**Cloud Monitoring**

v3

Feature

GKE version 1.20.8-gke.2100 or later offers a [Preview](https://cloud.google.com/products#product-launch-stages) of a fully managed metric collection pipeline to scrape Prometheus-style metrics exposed by any GKE workload and send those metrics to Cloud Monitoring for dashboards, alerts, and SLOs. Compared to the Prometheus Stackdriver sidecar, this new pipeline is easy to set up, allows filtering to control cost, supports larger clusters, is fully managed, supports Autopilot and horizontal Pod autoscaling, and offers better pricing. Get started with [GKE workload metrics](https://cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#workload-metrics).

## September 30, 2021

**Cloud Monitoring**

v3

Feature

Cloud Monitoring dashboards now support displays of data in tabular form. For information about this feature, see [Configure tables with the Cloud Console](https://cloud.google.com/monitoring/charts/index#add_table) and [Configure tables by using the API](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_a_table_widget).

## September 27, 2021

**Cloud Monitoring**

v3

Feature

You can now install the Ops Agent on one or more Compute Engine VMs from the **Inventory** tab of the Monitoring **VM Instances** dashboard. The dashboard generates Cloud Shell commands you can use to install the Ops Agent (recommended) or the legacy agents (if needed) on the selected VMs.

## September 09, 2021

**Cloud Monitoring**

v3

Feature

You can now collect JVM metrics from the Ops Agent, starting with version 2.2.0. For more information, see [Monitoring third-party applications: JVM](https://cloud.google.com/monitoring/agent/ops-agent/third-party/jvm).

## September 03, 2021

**Cloud Monitoring**

v3

Feature

Cloud Monitoring now lets you configure how long Monitoring waits to close an incident when observations stop arriving. For more information, see [Closing incidents](https://cloud.google.com/monitoring/alerts/incidents-events#closing).

## August 31, 2021

**Cloud Logging**

v2

Feature

You can now collect nginx metrics and logs from the Ops Agent, starting with version 2.1.0. For more information, see [Monitoring third-party applications: nginx](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/nginx).

**Cloud Monitoring**

v3

Feature

You can now collect nginx metrics and logs from the Ops Agent, starting with version 2.1.0. For more information, see [Monitoring third-party applications: nginx](https://cloud.google.com/monitoring/agent/ops-agent/third-party/nginx).

## August 30, 2021

**Cloud Monitoring**

v3

Feature

The **VM Instances** page features enhanced scorecards for VM health. The new scorecards now include both "maintenance" and "system" events that might affect your VMs and agents, along with other metrics and statistics about the health of your VMs. The filtering and sorting of the **Inventory** table have also been enhanced.

## August 18, 2021

**Cloud Logging**

v2

Feature

You can now use Chef to install and manage the [Google Cloud operations suite agents](https://docs.cloud.google.com/stackdriver/docs/solutions/agents) across your fleet of Linux and Windows VMs. For more information, refer to the [Chef Integration](https://github.com/GoogleCloudPlatform/google-cloud-ops-agents-chef/blob/master/README.md) documentation.

**Cloud Monitoring**

v3

Feature

You can now use Chef to install and manage the [Google Cloud operations suite agents](https://cloud.google.com/stackdriver/docs/solutions/agents) across your fleet of Linux and Windows VMs. For more information, refer to the [Chef Integration](https://github.com/GoogleCloudPlatform/google-cloud-ops-agents-chef/blob/master/README.md) documentation.

## August 12, 2021

**Cloud Monitoring**

v3

Change

Cloud Monitoring now supports creating an uptime check against a Kubernetes LoadBalancer Service hosted on GKE. For more information, see [Managing uptime checks](https://cloud.google.com/monitoring/uptime-checks).

## August 09, 2021

**Cloud Monitoring**

v3

Feature

When you create a line chart on a dashboard, you can now specify whether the selected metric is charted against the left Y-axis or the right Y-axis. This feature lets you display different metrics with different scales on the same chart. For an API example, see [Dashboard with an `XyChart` and a threshold](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_an_xychart_and_a_threshold).

## August 05, 2021

**Cloud Monitoring**

v3

Feature

A new UI for creating alerting policies is available in Preview. This interface offers fine-grained control over the selection of the metrics used in alerting conditions. See [Managing Alerting Policies](https://cloud.google.com/monitoring/alerts/using-alerting-ui) for more information.

Change

The **Processes** tab in the **VM instances** page is now Generally Available. This tab adds charts for [process metrics](https://cloud.google.com/monitoring/api/metrics_agent#agent-processes) to the charts provided by the existing **CPU** , **Memory** , **Disk** , and **Network** tabs.

## August 02, 2021

**Cloud Logging**

v2

Feature

You can now use Puppet to install and manage the [Google Cloud operations suite agents](https://docs.cloud.google.com/stackdriver/docs/solutions/agents) across your fleet of Linux and Windows VMs. For more information, refer to the [Puppet Integration](https://github.com/GoogleCloudPlatform/google-cloud-ops-agents-puppet/blob/master/README.md) documentation.

**Cloud Monitoring**

v3

Feature

The API to manage the [metrics scope](https://cloud.google.com/monitoring/settings#concept-scope) of a Google Cloud project is now in Preview. For more information, see [Manage metrics scopes with the API](https://cloud.google.com/monitoring/settings/manage-api).

Feature

You can now use Puppet to install and manage the [Google Cloud operations suite agents](https://cloud.google.com/stackdriver/docs/solutions/agents) across your fleet of Linux and Windows VMs. For more information, refer to the [Puppet Integration](https://github.com/GoogleCloudPlatform/google-cloud-ops-agents-puppet/blob/master/README.md) documentation.

## July 30, 2021

**Cloud Logging**

v2

Feature

Cloud Logging now lets you control access to individual log entry fields using field-level access control. To learn more, see [Field-level access control](https://docs.cloud.google.com/logging/docs/field-level-acl).

## July 29, 2021

**Cloud Logging**

v2

Change

Cloud Logging now supports the asia-east2 and europe-central2 regions. For a full list or regions, see [Regionalization](https://docs.cloud.google.com/logging/docs/storage#regionalization).

**Cloud Monitoring**

v3

Change

Monitoring Query Language (MQL) no longer requires you to use strict form when you create MQL-based alerting policies by using the Monitoring API. You can now provide queries in concise form. The query is stored as you provide it; concise queries are not converted to strict form.

## July 26, 2021

**Cloud Logging**

v2

Change

Log entries that are exported to BigQuery that result in a schema mismatch are now being written to an error table. For more information, see [Mismatches in schema](https://docs.cloud.google.com/logging/docs/export/bigquery#mismatch).

**Cloud Monitoring**

v3

Feature

The new **External HTTP(S) Load Balancers** dashboard in Monitoring provides powerful visualizations to help you understand and troubleshoot connectivity issues on your external load balancers.

## July 23, 2021

**Cloud Logging**

v2

Feature

You can now use [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm) keys for organization-level Log Router CMEK. For more information, see [Enabling customer-managed encryption keys for Log Router](https://docs.cloud.google.com/logging/docs/routing/managed-encryption).

## July 15, 2021

**Cloud Logging**

v2

Change

You can now view Monitoring data and link to the resources in the Cloud Console for Compute Engine logs in the Logs Explorer. For more information, see [Viewing Monitoring data](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#monitoring_data).

## July 13, 2021

**Cloud Logging**

v2

Change

Starting on October 12, 2021, your Dataflow logs that are ingested and stored in Cloud Logging will be charged at the standard [Cloud Logging prices](https://cloud.google.com/stackdriver/pricing#logging-pricing-summary). It's recommended that you review the volume of Dataflow logs ingested into Cloud Logging through [Metrics Explorer in Cloud Monitoring](https://console.cloud.google.com/monitoring/metrics-explorer?pageState=%7B%22xyChart%22:%7B%22dataSets%22:%5B%7B%22timeSeriesQuery%22:%22fetch%20dataflow_job%5Cn%7C%20metric%20%27logging.googleapis.com%2Fbyte_count%27%5Cn%7C%20group_by%2030d,%20%5Bvalue_byte_count_aggregate:%20aggregate\(value.byte_count\)%5D%5Cn%7C%20every%2030d%5Cn%7C%20group_by%20%5B%5D,%5Cn%20%20%20%5Bvalue_byte_count_aggregate_aggregate:%5Cn%20%20%20%20%20%20aggregate\(value_byte_count_aggregate\)%5D%5Cn%7C%20group_by%20%5B%5D,%5Cn%20%20%20%5Bvalue_byte_count_aggregate_aggregate_aggregate:%5Cn%20%20%20%20%20%20aggregate\(value_byte_count_aggregate_aggregate\)%5D%22,%22targetAxis%22:%22Y1%22,%22plotType%22:%22STACKED_BAR%22%7D%5D,%22options%22:%7B%22mode%22:%22COLOR%22%7D,%22constantLines%22:%5B%5D,%22timeshiftDuration%22:%220s%22,%22y1Axis%22:%7B%22label%22:%22y1Axis%22,%22scale%22:%22LINEAR%22%7D%7D,%22isAutoRefresh%22:true,%22timeSelection%22:%7B%22timeRange%22:%221m%22%7D%7D). For information on optimizing the log volume for your Dataflow jobs, see [Controlling log volume](https://docs.cloud.google.com/dataflow/docs/guides/logging#LogControls).

Change

The Cloud Console now supports creating Logging sinks at the organization or folder level. For information on creating sinks, see [Exporting logs with the Google Cloud console](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

**Cloud Monitoring**

v3

Change

Metrics Explorer, a stand-alone charting tool that lets you quickly chart and explore time-series data, has a new interface and supports enhanced aggregation options. For more information, see [Metrics Explorer](https://cloud.google.com/monitoring/charts/metrics-explorer).

Feature

The **VM instances** page has a new **Processes** tab in Preview. This tab adds charts for [process metrics](https://cloud.google.com/monitoring/api/metrics_agent#agent-processes) to the charts provided by the existing **CPU** , **Memory** , **Disk** , and **Network** tabs.

## July 12, 2021

**Cloud Logging**

v2

Feature

You can now install the Logging and Monitoring agents on multiple VMs from the **Inventory** tab on the Cloud Monitoring **VM Instances** page. You can select multiple VMs in your fleet for agent installation. The page generates the necessary installation command and provides a link to Cloud Shell, where you can run the command.

**Cloud Monitoring**

v3

Change

A warning annotation is now added to charts when they are missing data due to a data outage. When the annotation is absent, data gaps aren't due to a data outage. For common reasons why a chart might contain a data gap, see [Gaps in chart data](https://cloud.google.com/monitoring/charts/troubleshooting-charts#gaps).

Feature

You can now install the Logging and Monitoring agents on multiple VMs from the **Inventory** tab on the Cloud Monitoring **VM Instances** page. You can select multiple VMs in your fleet for agent installation. The page generates the necessary installation command and provides a link to Cloud Shell, where you can run the command.

## July 09, 2021

**Cloud Trace**

v2

Feature

Cloud Trace announces that the OpenTelemetry library for Java is now generally available. For information about configuring your Java application to use Open Telemetry, see [Java and OpenTelemetry](https://cloud.google.com/trace/docs/setup/java-ot).

## July 08, 2021

**Error Reporting**

v1beta1

Change

Error Reporting notifications has been upgraded to use the Alerting infrastructure. For more information, see the [Notifications](https://cloud.google.com/error-reporting/docs/notifications) guide.

## July 07, 2021

**Cloud Logging**

v2

Feature

The **Share link** feature for queries in the Logs Explorer now lets you choose whether to include an absolute time range or a relative time range. With an absolute time range, the query includes static time values for the results, so the query always returns the same results. With a relative time range, you can set a value like "last 1 hour", and the results change as time passes.

Feature

**Preview** : Cloud Logging now supports alerts based on matching the content of your logs. When triggered, a log-based alert notifies you that a match has appeared in your logs and opens an incident in Cloud Monitoring. You can create log-based alerts by using the Logs Explorer or the Monitoring API. For more information, see [Monitoring your logs](https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs) and [Using log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

**Cloud Monitoring**

v3

Feature

**Preview** : Cloud Logging now supports alerts based on matching the content of your logs. When triggered, a log-based alert notifies you that a match has appeared in your logs and opens an incident in Cloud Monitoring. You can create log-based alerts by using the Logs Explorer or the Monitoring API. For more information, see [Monitoring your logs](https://cloud.google.com/logging/docs/alerting/monitoring-logs) and [Using log-based alerts](https://cloud.google.com/logging/docs/alerting/log-based-alerts).

## July 02, 2021

**Cloud Monitoring**

v3

Change

Dashboard-wide filters now apply to all charts on a dashboard. Prior to this change, these filters didn't apply to MQL-configured charts.

Feature

You can now display summaries of single-condition alerting policies on a custom dashboard. A policy summary includes a display of the monitored time series, the threshold, and chips that show the number of open incidents and whether the policy is disabled. For more information about Alert charts, see the following pages:

  * [Managing dashboards by API](https://cloud.google.com/monitoring/dashboards/api-dashboard)
  * [Adding an alerting policy to a dashboard by using the Cloud Console](https://cloud.google.com/monitoring/alerts/using-alerting-ui#viewing_policies).



## June 30, 2021

**Cloud Logging**

v2

Feature

Cloud Logging lets you copy logs from a Cloud Logging bucket to a Cloud Storage bucket. To learn more, see [Copying log entries](https://docs.cloud.google.com/logging/docs/routing/copy-logs).

Change

The Ops Agent is now Generally Available as version 2.0.0. This agent combines logging and metrics into a single agent. The Ops Agent is targeted toward specialized logging workloads that require higher throughput and improved resource efficiency.

For installation information, see [Installing the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/install-index). For information about migrating from an earlier version, see the [transition guide](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/transition).

The GA version of the Ops Agent can be configured to collect specific sets of metrics, as described in [Configuring the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration). There is a small number of metrics that the GA version of the Ops Agent handles differently from the Preview versions of the Ops Agent and the Monitoring agent; see [Differences in metric collection](https://docs.cloud.google.com/monitoring/api/metrics_agent#metric-agent-diffs).

**Cloud Monitoring**

v3

Feature

The Monitoring dashboards page in the Cloud Console now includes a collection of sample dashboards. The sample dashboards provide support for many common applications. You can preview, install, and then customize these dashboards. For more information, see [Installing sample dashboards](https://cloud.google.com/monitoring/dashboards/dashboard-templates).

Change

The Ops Agent is now Generally Available as version 2.0.0. This agent combines logging and metrics into a single agent. The Ops Agent is targeted toward specialized logging workloads that require higher throughput and improved resource efficiency.

For installation information, see [Installing the Ops Agent](https://cloud.google.com/monitoring/agent/ops-agent/install-index). For information about migrating from an earlier version, see the [transition guide](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/transition).

The GA version of the Ops Agent can be configured to collect specific sets of metrics, as described in [Configuring the Ops Agent](https://cloud.google.com/monitoring/agent/ops-agent/configuration). There is a small number of metrics that the GA version of the Ops Agent handles differently from the Preview versions of the Ops Agent and the Monitoring agent; see [Differences in metric collection](https://cloud.google.com/monitoring/api/metrics_agent#metric-agent-diffs).

## June 28, 2021

**Cloud Monitoring**

v3

Change

The **Incidents** page now provides an option to permanently close incidents if no data for that incident has arrived in the most recent alerting period. For more information, see [Closing incidents](https://cloud.google.com/monitoring/alerts/incidents-events#closing_incidents).

Feature

Cloud Monitoring is launching a new **Observability** tab on Compute Engine's **VM instance details** page. This tab replaces the **Monitoring** tab. The enhanced **Observability** tab provides access to logs and greater visibility into CPU, disk, and network metrics.

## June 25, 2021

**Cloud Logging**

v2

Change

Log entries viewed in JSON format in the Cloud Console are now displayed with the field names in alphabetical order.

## June 15, 2021

**Cloud Logging**

v2

Change

You can now view Monitoring data and link to the resources in the Cloud Console for certain logs, such as Google Kubernetes Engine logs, in the Logs Explorer. For more information, see [Viewing Monitoring data](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#monitoring_data).

**Cloud Monitoring**

v3

Change

You can now view Monitoring data for certain logs, such as Google Kubernetes Engine logs, in the Logs Explorer. For more information, see [Viewing Monitoring data](https://cloud.google.com/logging/docs/view/logs-viewer-interface#monitoring_data).

## June 01, 2021

**Cloud Monitoring**

v3

Feature

A JSON editor has been integrated with the dashboard page. In addition to using the JSON editor to change the contents of the dashboard, you can save the current dashboard definition to a local system, and you can upload a dashboard definition to your Google Cloud project. For more information, see [Managing dashboards through the Cloud Console](https://cloud.google.com/monitoring/charts/dashboards).

## May 12, 2021

**Cloud Monitoring**

v3

Feature

Cloud Monitoring is introducing [metrics scopes](https://cloud.google.com/monitoring/settings#concept-scope). For a Google Cloud project, its metrics scope defines the projects whose metrics the project can view and monitor:

  * When you create a project, its metrics scope is set to self.
  * You can modify a project's metrics scope to include other Google Cloud projects, or to include AWS accounts. For more information, see [Viewing metrics for multiple projects](https://cloud.google.com/monitoring/settings/multiple-projects).
  * A Google Cloud project can be included in multiple metrics scopes.



For more information about metrics scopes, see [Configuring your project for Cloud Monitoring](https://cloud.google.com/monitoring/settings).

Change

The replacement of Cloud Monitoring Workspaces with [metrics scopes](https://cloud.google.com/monitoring/settings#concept-scope) is complete.

All of your existing Cloud Monitoring Workspaces have been migrated to the new data model. 

  * To access the metrics for a Google Cloud project, select that project in the Console project picker and then access the Monitoring page. 
  * To determine the projects whose metrics the current project can view, see [Determining visibility of metrics](https://cloud.google.com/monitoring/settings#visibility).
  * For information about metrics scopes, see [Configuring your project for Cloud Monitoring](https://cloud.google.com/monitoring/settings).



## May 06, 2021

**Cloud Logging**

v2

Feature

The Logs Explorer Histogram offers new time controls, including zooming and scrolling, to give you more in-depth analysis of your logs data. For details, see [Analyzing logs using time controls](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#analyzing_logs_histogram).

## May 05, 2021

**Cloud Monitoring**

v3

Feature

Cloud Monitoring has added new ways to interact with charts. You can now select a range of lines displayed on chart, shift the time axis by using your pointer, and have new controls to expand the chart around a specific point in time. Charts displaying distribution data include 50th, 95th, and 99th percentile lines as an optional overlay. For more information, see [Exploring charted data](https://cloud.google.com/monitoring/charts/working-with-charts).

## May 04, 2021

**Cloud Monitoring**

v3

Change

The Query Editor for Monitoring Query Language (MQL) has been reimplemented. In addition to autocompletion and error detection, it now supports code folding and a find-and-replace capability. For more information, see [Using the Query Editor](https://cloud.google.com/monitoring/mql/query-editor).

## May 03, 2021

**Cloud Logging**

v2

Feature

You can now add custom fields in the Logs Explorer to better analyze logs and refine your queries. For more information, see [Adding fields to **Log fields** pane ](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#custom-fields).

**Cloud Monitoring**

v3

Feature

The **Inventory** tab on the Cloud Monitoring **VM Instances** dashboard now offers the ability to filter and sort the instance table by any combination of columns. In addition, new health scorecards report a variety of metrics and statistics related to the health and status of your VMs and agents.

## April 27, 2021

**Cloud Logging**

v2

Feature

You can now install the [Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent), [Cloud Monitoring agent](https://docs.cloud.google.com/monitoring/agent), and [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent) on VMs running OpenSUSE Leap versions 15, 15.1, and 15.2.

**Cloud Monitoring**

v3

Feature

You can now install the [Cloud Logging agent](https://cloud.google.com/logging/docs/agent), [Cloud Monitoring agent](https://cloud.google.com/monitoring/agent), and [Ops Agent](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent) on VMs running OpenSUSE Leap versions 15, 15.1, and 15.2.

## April 21, 2021

**Cloud Logging**

v2

Feature

You can now provision and manage the [Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent) on Windows using Ansible. For more information, refer to the [Ansible Role for Cloud Ops](https://github.com/GoogleCloudPlatform/google-cloud-ops-agents-ansible/blob/master/README.md) documentation.

## April 19, 2021

**Cloud Monitoring**

v3

Change

Cloud Monitoring [Workspaces](https://cloud.google.com/monitoring/workspaces) are changing. Over the next few weeks, new capabilities are being deployed:

  * A Cloud Monitoring Workspace will be created automatically for a Google Cloud project. This change replaces the manual creation process.
  * The restriction that you can view the metrics for a project from only one Workspace is being eliminated. You'll be able to view the metrics for a project from multiple Workspaces.
  * Navigation to a Workspace that manages metrics from multiple projects is changing. For information on this change, see [Navigating to a Workspace](https://cloud.google.com/monitoring/settings#navigation).



**Cloud Trace**

v2

Feature

Cloud Trace announces that the OpenTelemetry library for Python is now generally available. For information about configuring your Python application to use Open Telemetry, see [Python and OpenTelemetry](https://cloud.google.com/trace/docs/setup/python-ot).

## April 16, 2021

**Cloud Monitoring**

v3

Feature

The Cloud Operations for GKE monitoring dashboard now allows you to manage and display service-level objectives (SLOs) that you define for your applications. For more information, see the **Managing SLOs** section of the [Observing your GKE clusters](https://cloud.google.com/stackdriver/docs/solutions/gke/observing#managing_slos) guide.

## April 15, 2021

**Cloud Monitoring**

v3

Feature

The Cloud Operations for GKE monitoring dashboard now includes a column called **Error logs** that displays the number of error logs associated with an entity based on the selected time range. You can also select which columns to display in the tables. For more information, see the **Configuring the dashboard tables** section of the [Observing your GKE clusters](https://cloud.google.com/stackdriver/docs/solutions/gke/observing#configure-tables) guide.

Change

Compute Engine's **Instance Groups Monitoring** tab now includes charts for your managed instance groups. Charted metrics include group size, CPU utilization, disk I/O, and more. You can select the time window for the charts and view the corresponding logs from the integrated logs viewer panel. You can also use the links on each chart to create alerting policies or to analyze the data in Metrics Explorer.

## April 13, 2021

**Cloud Monitoring**

v3

Feature

The Cloud Operations for GKE monitoring dashboard now provides a **Metrics** tab in the resource details panel. This tab also includes a menu option to create a new alert policy. For more information, see [Observing your GKE clusters](https://cloud.google.com/stackdriver/docs/solutions/gke/observing).

## April 12, 2021

**Cloud Logging**

v2

Feature

Shared queries are now generally available (GA). To learn more, see [Shared queries](https://docs.cloud.google.com/logging/docs/view/building-queries#shared-queries).

**Cloud Monitoring**

v3

Feature

The Cloud Operations for GKE monitoring dashboard now provides an **Alerts** tab in the resource details panel. This tab also includes a link to create a new alert policy. For more information, see [Observing your GKE clusters](https://cloud.google.com/stackdriver/docs/solutions/gke/observing).

Change

The dashboard save feature now displays the date and time of the last save operation. You can also disable and enable autosave. For more information, see [Configuring dashboards](https://cloud.google.com/monitoring/charts/dashboards#configuring_dashboards).

## April 09, 2021

**Cloud Monitoring**

v3

Change

For new alerts created through the Cloud Console, the default behavior is to send a notification only when the incident is created. For alerts created by using the API, the default behavior is to send notifications when incidents are opened and closed. For all alerts, the alert's **Policy detail** page displays when notifications are sent. To change this behavior, you must use the Cloud Console to edit the policy. For more information, see [Managing Policies](https://cloud.google.com/monitoring/alerts/using-alerting-ui#managing_policies).

## April 08, 2021

**Cloud Logging**

v2

Feature

The Google Cloud [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/ops-agent) is now available in Preview. This agent combines logging and metrics into a single agent that is targeted toward specialized logging workloads that require higher throughput and improved resource efficiency. It supports both Linux and Windows Compute Engine VMs.

Feature

Cloud Operations now offers the ability to install the Google Cloud Ops Agent via [Ansible](https://github.com/GoogleCloudPlatform/google-cloud-ops-agents-ansible) on Linux and Windows Compute Engine VMs.

Feature

Cloud Operations now offers the ability to provision the Google Cloud Ops Agent via [Terraform](https://registry.terraform.io/modules/terraform-google-modules/cloud-operations/google/latest/submodules/agent-policy) on Linux and Windows Compute Engine VMs.

**Cloud Monitoring**

v3

Feature

The Google Cloud [Ops Agent](https://cloud.google.com/stackdriver/docs/solutions/ops-agent) is now available in Preview. This agent combines logging and metrics into a single agent that is targeted toward specialized logging workloads that require higher throughput and improved resource efficiency. It supports both Linux and Windows Compute Engine VMs.

Feature

Cloud Operations now offers the ability to install the Google Cloud Ops Agent via [Ansible](https://github.com/GoogleCloudPlatform/google-cloud-ops-agents-ansible) on Linux and Windows Compute Engine VMs.

Feature

Cloud Operations now offers the ability to provision the Google Cloud Ops Agent via [Terraform](https://registry.terraform.io/modules/terraform-google-modules/cloud-operations/google/latest/submodules/agent-policy) on Linux and Windows Compute Engine VMs.

## April 06, 2021

**Cloud Logging**

v2

Change

Cloud Logging now supports [22 regions](https://docs.cloud.google.com/logging/docs/storage#regionalization) in which you can create a log bucket so that you can meet compliance and audit requirements when storing your logs.

## March 31, 2021

**Error Reporting**

v1beta1

Change

Service Errors is now available Generally Available (GA). Service Errors automatically captures and groups Google Cloud service errors and notifies you when these errors occur. For more information, refer to the [Managing Service Errors](https://cloud.google.com/error-reporting/docs/service-errors) documentation.

## March 29, 2021

**Cloud Logging**

v2

Change

Logs Views are now Generally Available (GA). Using Logs Views, you can control who has access to the logs within your Logs Buckets. For more information on this feature, refer to the [Managing Logs Views](https://docs.cloud.google.com/logging/docs/logs-views) guide.

## March 18, 2021

**Cloud Logging**

v2

Feature

Cloud Logging now shows the breakdown of log severity levels in the Histogram pane. To learn more, see the [Histogram section](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#histogram-panel) on the Logs Explorer page.

## March 12, 2021

**Cloud Logging**

v2

Change

Suggested queries is now generally available (GA). To learn more, go to [Suggested queries](https://docs.cloud.google.com/logging/docs/view/building-queries#suggested_queries).

## March 04, 2021

**Cloud Logging**

v2

Feature

Compute Engine's **VM Instances** dashboard now provides an **Operations** menu. The "View metrics" menu option brings you to the **Infrastructure summary** dashboard in Monitoring. The "View logs" menu option brings you to the **Logs Explorer** page in Logging.

Feature

Kubernetes Engine's **Clusters** and **Workloads** dashboards now provide an **Operations** menu. The "View metrics" menu option brings you to the **GKE Dashboard** in Monitoring. The "View logs" menu option brings you to the **Logs Explorer** page in Logging.

**Cloud Monitoring**

v3

Feature

Compute Engine's **VM Instances** dashboard now provides an **Operations** menu. The "View metrics" menu option brings you to the **Infrastructure summary** dashboard in Monitoring. The "View logs" menu option brings you to the **Logs Explorer** page in Logging.

Feature

Kubernetes Engine's **Clusters** and **Workloads** dashboards now provide an **Operations** menu. The "View metrics" menu option brings you to the **GKE Dashboard** in Monitoring. The "View logs" menu option brings you to the **Logs Explorer** page in Logging.

Change

Compute Engine's **VM instance details** page now offers a guided installation path for the [Monitoring agent](https://cloud.google.com/monitoring/agent) when it is not detected on the VM.

## March 03, 2021

**Error Reporting**

v1beta1

Change

Error Reporting has been updated to only analyze logs that are stored in global buckets in the same project where they are ingested. For more information, see [Using Error Reporting with regionalized logs](https://cloud.google.com/error-reporting/docs/regionalization).

## February 19, 2021

**Cloud Monitoring**

v3

Feature

The **Incident details** page has been completely revised, making it easier to investigate and manage incidents. New features include a timeline of incidents, the addition of a chart with time-range controls and a link to Metrics Explorer, a log for recording the investigative history. For more information, see [Investigating incidents](https://cloud.google.com/monitoring/alerts/incidents-events#details-page).

## February 18, 2021

**Cloud Logging**

v2

Change

Cloud Logging agent for Windows version 1-14 is now available. This version changes the default Windows configuration from using gRPC to REST for sending logs to the Cloud Logging API. For more information, refer to the [release information on GitHub](https://github.com/GoogleCloudPlatform/google-fluentd/releases/tag/windows-v1-14).

## February 08, 2021

**Cloud Logging**

v2

Change

Logging truncates oversized [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) label keys and values. For details, see [Quotas and limits](https://docs.cloud.google.com/logging/quotas#log-limits).

## January 29, 2021

**Cloud Logging**

v2

Change

Cloud Logging has increased the number of `entries.write` API calls from 60,000 to 120,000 per minute. For more information on quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/logging/quotas).

## January 26, 2021

**Cloud Logging**

v2

Feature

The `gcloud` commands for [managing Agent Policies](https://docs.cloud.google.com/stackdriver/docs/solutions/managing-agent-policies) are now available in beta. For more information, refer to the [`gcloud` documentation for Agent Policies](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/ops-agents/policies).

**Cloud Monitoring**

v3

Feature

The `gcloud` commands for [managing Agent Policies](https://cloud.google.com/stackdriver/docs/solutions/managing-agent-policies) are now available in beta. For more information, refer to the [`gcloud` documentation for Agent Policies](https://cloud.google.com/sdk/gcloud/reference/beta/compute/instances/ops-agents/policies).

## January 22, 2021

**Cloud Logging**

v2

Change

The Logs Explorer now provides a higher degree of contrast that improves readability.

## January 14, 2021

**Cloud Logging**

v2

Change

Cloud Logging now lets you share your saved queries with other users of a project. To learn more, go to the [Shared queries section on the Building queries page](https://docs.cloud.google.com/logging/docs/view/building-queries#shared-queries).

## December 23, 2020

**Cloud Monitoring**

v3

Change

Alerting is now Generally Available for Monitoring Query Language (MQL). For more information, see [Alerting policies with MQL](https://cloud.google.com/monitoring/mql/alerts).

## December 16, 2020

**Cloud Logging**

v2

Announcement

Logs regionalization is now generally available. You can set the region in which you want to store your logs data. For information about this feature, refer to the [Regionalization](https://docs.cloud.google.com/logging/docs/storage#regionalization) documentation.

**Cloud Monitoring**

v3

Change

The dashboard editor that lets you create and edit all dashboard widget types, including gauges, scorecards, and text boxes, is now Generally Available. With this editor, you can quickly configure dashboard widgets by using Basic Mode, you can access all aggregation options with Advanced Mode, and you can use Monitoring Query Language when you select MQL Mode. When you set the dashboard layout to mosaic mode, you can resize and reposition widgets. For more information, see [Custom dashboards](https://cloud.google.com/monitoring/charts/dashboards#custom_dashboards).

## December 08, 2020

**Cloud Logging**

v2

Fixed

Cloud Logging calculates the system logs-based metrics `byte_count` and `log_entry_count` on stored logs only, unlike user-defined logs-based metrics which are calculated on both stored and excluded logs. For more information, see [System logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics#system_logs-based_metrics).

This change is currently rolling out and affects all users after December 11, 2020.

## December 07, 2020

**Cloud Logging**

v2

Feature

In the Logs Explorer, you can now stream your log entries in real time as Cloud Logging ingests them. To learn more, see [Streaming logs](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#stream-logs).

## December 04, 2020

**Cloud Monitoring**

v3

Announcement

Slack notification channels: All notification channels created before November 20 have been fixed, and new notification channels will be created correctly. Notification channels created between November 21 and December 3 need to be manually updated, as described in [Adding the Monitoring app to a Slack channel](https://cloud.google.com/monitoring/support/notification-options#slack-add-app).

## November 25, 2020

**Cloud Monitoring**

v3

Announcement

If you created Slack notification channels after November 20, 2020, your channels are not receiving notifications. For information about resolving this issue, see [Adding the Monitoring app to a Slack channel](https://cloud.google.com/monitoring/support/notification-options#slack-add-app).

## November 16, 2020

**Cloud Monitoring**

v3

Feature

A new dashboard editor is available in Preview. The new editor lets you create and edit all dashboard widget types, including gauges, scorecards, and text boxes. With mosaic-mode, you can resize and reposition widgets. The configuration tabs - Basic, Advanced, MQL - let you choose how you want to configure your widgets. For more information, see [Custom dashboards](https://cloud.google.com/monitoring/charts/dashboards#custom_dashboards).

## November 13, 2020

**Cloud Logging**

v2

Feature

You can now use the **Share link** button in the Logs Explorer to create and share a shortened URL of your current query. For more information, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface).

## November 12, 2020

**Cloud Monitoring**

v3

Change

Compute Engine's **VM instance details** page now displays "Memory Utilization" and "Disk Space Utilization" charts. In addition, a new "Monitor VM Instances" link lets you go directly to the [**VM instances** dashboard](https://console.cloud.google.com/monitoring/dashboards/resourceList/gce_instance) in Cloud Monitoring.

## November 09, 2020

**Cloud Monitoring**

v3

Change

Monitoring Query Language (MQL) adds Preview support for macros. For more information, see [MQL macros](https://cloud.google.com/monitoring/mql/query-language#ql-macros).

## November 06, 2020

**Cloud Logging**

v2

Feature

By using the new `gcloud` command and API for live tailing, you can now stream your logs in real time as your applications write them to the Cloud Logging API. To learn more, see [Live tailing log entries](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging#live-tailing).

## November 05, 2020

**Cloud Logging**

v2

Announcement

Beta release: You can set the region in which you want to store your logs data. For information about this feature, refer to the [Regionalization](https://docs.cloud.google.com/logging/docs/storage#regionalization) documentation.

**Cloud Monitoring**

v3

Feature

Enhancements to the **VM Details** page. A new **Event Timeline** shows important events as bars on a timeline. Hovering over any event bar displays summary information about the event and provides a link to the **Incident Details** page for the event.

## October 28, 2020

**Cloud Logging**

v2

Feature

You can now create sinks from within the **Logs Explorer** and **Logs Router** pages. To learn more, see [Exporting logs with the Google Cloud console](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

Announcement

To help you understand your logs volume and usage within the context of your Logs Buckets, the **Resource Usage** page has been moved to the **Logs Storage** page, which now contains your resource usage information. To learn more, see [Tracking logs usage](https://docs.cloud.google.com/logging/docs/exclusions#tracking).

## October 26, 2020

**Cloud Monitoring**

v3

Feature

Enhancements to the pre-configured Monitoring **VM Instances** dashboard. The inventory table now includes a **Logging Agent Status** column, and the Logging agent can be installed by using a UI workflow from the table.

## October 22, 2020

**Cloud Logging**

v2

Change

Cloud Logging now calculates logs-based metrics from both ingested and excluded logs. In other words, you can now calculate logs-based metrics from logs without ingesting them into a Logs Bucket. 

This change started rolling out **October 18, 2020** and will finish rolling out **October, 30 2020**.

For more information, see [Overview of logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics).

Announcement

Logs Views are now available in Preview. Using Logs Views, you can control who has access to the logs within your Logs Buckets. For more information on this feature, refer to the [Managing Logs Views](https://docs.cloud.google.com/logging/docs/logs-views) guide.

## October 20, 2020

**Cloud Logging**

v2

Change

Recent queries is now generally available (GA). To learn more, go to [Recent queries](https://docs.cloud.google.com/logging/docs/view/building-queries#recent-queries).

## October 19, 2020

**Cloud Logging**

v2

Feature

In the Logs Explorer you can now download your logs in JSON and CSV to your computer, Google Drive, or view them in a new tab. To learn more, see [Downloading logs](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#download_logs).

## October 15, 2020

**Cloud Logging**

v2

Feature

The [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/ops-agent) is now available in Preview. Ops Agent provides a single agent to collect logs and metrics on Compute Engine instances.

Note that the Ops Agent uses new configuration files that are not compatible with the standalone Cloud Monitoring and Cloud Logging agents.

**Cloud Monitoring**

v3

Feature

The [Ops Agent](https://cloud.google.com/stackdriver/docs/solutions/ops-agent) is now available in Preview. Ops Agent provides a single agent to collect logs and metrics on Compute Engine instances.

Note that the Ops Agent uses new configuration files that are not compatible with the standalone Cloud Monitoring and Cloud Logging agents.

## October 13, 2020

**Cloud Logging**

v2

Announcement

We've renamed the Logs Viewer (Preview) to the Logs Explorer. The Logs Explorer offers a robust set of tools for analyzing your logs data and is now the default viewer for Cloud Logging. To learn more, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface). 

The Logs Viewer (Classic) is now called the Legacy Logs Viewer. It will continue to be available and maintained until March 2021, but won't be actively developed further.

## October 12, 2020

**Cloud Logging**

v2

Change

Cloud Logging has deprecated the following two logs-based metrics related to exclusions:

  * `logging.googleapis.com/excluded_log_entry_count`
  * `logging.googleapis.com/excluded_byte_count`



Cloud Logging will stop populating these metrics on October 1, 2021.

## October 05, 2020

**Cloud Monitoring**

v3

Feature

Alerting is now available for Monitoring Query Language (MQL). For more information, see [Alerting policies with MQL](https://cloud.google.com/monitoring/mql/alerts).

## September 29, 2020

**Cloud Profiler**

v2

Feature

Cloud Profiler history view is available in beta. For more information, see [Viewing historical trends](https://cloud.google.com/profiler/docs/history-view).

## September 22, 2020

**Cloud Logging**

v2

Feature

The histogram panel in the Logs Viewer (Preview) now contains a viewport to help you quickly understand the time range of the log entries you're viewing within the Query results pane. To learn more, go to the [Histogram panel](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#histogram-panel).

## September 21, 2020

**Cloud Logging**

v2

Change

Logs Buckets are now generally available. For information about this feature, refer to the [Managing logs buckets](https://docs.cloud.google.com/logging/docs/buckets) guide.

## September 17, 2020

**Cloud Logging**

v2

Feature

In the Logs Viewer (Preview), you can now pin log entries within the **Query results** and **Histogram** panes. To learn more, go to [Pinning logs](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#pin-logs).

Feature

In the Logs Viewer (Preview), you can now view a log entry in its resource context. To learn more, go to [Viewing a pinned log entry in its resource context](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#resource-context).

Feature

You can now copy a link to a log entry in the Logs Viewer (Preview). To learn more, go to [Copy a link to a log entry](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#copy-link).

## September 14, 2020

**Cloud Logging**

v2

Feature

Cloud Logging now offers the ability to view a history of your ran queries through the **Recent** queries tab. To learn more, go to the [Recent queries section on the Building queries page](https://docs.cloud.google.com/logging/docs/view/building-queries#recent-queries).

## September 09, 2020

**Cloud Monitoring**

v3

Change

The API for creating and managing alerting policies is now Generally Available. For information on using this API, see [Managing alerting policies by API](https://cloud.google.com/monitoring/alerts/using-alerting-api).

## September 01, 2020

**Cloud Logging**

v2

Change

Cloud Logging updated IAM custom role permissions. Users with custom roles should verify their permissions are correct. For a list of the permissions and roles, go to the [Permissions and Roles section on the Access control page](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles).

## August 28, 2020

**Cloud Monitoring**

v3

Feature

Cloud Trace exemplars can now be viewed in Cloud Monitoring. For more information about Trace exemplars, see [Cloud Trace exemplars](https://cloud.google.com/trace/docs/setup#create-exemplars). For more information about viewing exemplars, see [Exploring charted data](https://cloud.google.com/monitoring/charts/working-with-charts).

**Cloud Trace**

v2

Feature

Cloud Trace exemplars can now be viewing in Cloud Monitoring. For more information about Trace exemplars, see [Cloud Trace exemplars](https://cloud.google.com/trace/docs/setup#create-exemplars). For more information about viewing exemplars, see [Exploring charted data](https://cloud.google.com/monitoring/charts/working-with-charts).

## August 24, 2020

**Cloud Logging**

v2

Feature

You can now view Cloud Trace information from within the Logs Viewer. To learn more, go to the [Trace data section on the Using Logs Viewer (Preview) page](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#trace_data).

## August 17, 2020

**Cloud Logging**

v2

Feature

To help you explore your logs more efficiently, Cloud Logging now provides suggested queries based on the context of your Google Cloud project. For more information, go to [Suggested queries](https://docs.cloud.google.com/logging/docs/view/building-queries#suggested_queries).

**Cloud Trace**

v2

Feature

The Cloud Trace viewer now supports search by the trace ID. For more information, see [Viewing Trace Details](https://cloud.google.com/trace/docs/viewing-details).

## August 13, 2020

**Cloud Monitoring**

v3

Feature

The new, out-of-the-box **Infrastructure Summary** dashboard for Compute Engine VMs provides a single-pane-of-glass view into your VM fleet and load balancers. At a glance, you can see the top 5 VMs across a variety of key metrics including memory, CPU, sent/received traffic, latency, disk read/write, and more.

## August 12, 2020

**Cloud Monitoring**

v3

Feature

Enhancements to the pre-configured Monitoring **VM Instances** dashboard. The inventory table now includes a **Monitoring Agent Status** column, and the Monitoring agent can be installed by using a UI workflow from the table. The **Explore** tab gives an overview of additional metrics being sent (including agent metrics, custom metrics, and logs-based metrics) as well as a set of quick links to learn more about each type of metric. You can also use the **Recommended Alerts** button on the dashboard to configure fleet-wide alerts.

## August 11, 2020

**Cloud Logging**

v2

Feature

Beta release: You can now use Logs Buckets to centralize or divide your logs based on your needs. For information about this feature, refer to the [Managing logs buckets](https://docs.cloud.google.com/logging/docs/buckets) guide.

Change

Users now manage logs exclusions through logs sinks. As a result, custom roles that have the `logging.sinks.*` permissions can now control the volume of logs ingested into Cloud Logging through logs sinks.

We recommend that you review any custom roles with the `logging.sinks.*` permissions so that you can make adjustments as needed.

## August 03, 2020

**Cloud Logging**

v2

Feature

Alpha release: You can now use Logs Buckets to centralize or divide your logs based on your needs. For information about this feature, refer to the [Managing logs buckets](https://docs.cloud.google.com/logging/docs/buckets) guide. To participate in the alpha or to get notified when Logs Buckets goes beta, fill out the [sign up form](https://docs.google.com/forms/d/e/1FAIpQLSeBVpNBivnTAAd4G3rdait9t94uG9TWc07oGwNRGcE071TeCA/viewform).

## July 30, 2020

**Cloud Logging**

v2

Change

The Logs field explorer panel is now generally available (GA). To learn more, see the [Logs field explorer section on Logs Viewer (Preview) interface page](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface#logs-field-panel).

## July 10, 2020

**Cloud Monitoring**

v3

Feature

SLO monitoring for microservices is now Generally Available in the Cloud Console. This feature lets you create service-level objectives (SLOs) and set up alerting policies to monitor their performance using auto-generated dashboards with metrics, logs, and alerts in a single place. For more information, see [SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring).

## July 07, 2020

**Cloud Monitoring**

v3

Change

Monitoring Query Language (MQL) is now Generally Available for querying data and creating charts. MQL is an expressive, text-based interface to Cloud Monitoring time-series data. With MQL, you can create charts you can't create any other way. You can access MQL from both the Cloud Console and the Monitoring API. For more information, see [Introduction to Monitoring Query Language](https://cloud.google.com/monitoring/mql/).

## June 30, 2020

**Cloud Logging**

v2

Feature

Cloud Logging now contains a Logs Dashboard page that provides a high-level overview into the health of your systems running within a project. To learn more, see [Logs Dashboard](https://docs.cloud.google.com/logging/docs/view/dashboard).

## June 15, 2020

**Cloud Monitoring**

v3

Change

The Service Monitoring API is now Generally Available. You can use this feature to create services, set service-level objectives (SLOs), and create alerting policies to monitor your SLOs. See [Service monitoring](https://cloud.google.com/monitoring/service-monitoring/) for documentation, and [`services`](https://cloud.google.com/monitoring/api/v3/#service-monitoring) for reference material.

## June 08, 2020

**Cloud Monitoring**

v3

Feature

Enhancements to the pre-configured Compute Engine **VM Instances** dashboard. Compute Engine cross-fleet metrics and detail views specific to CPU, Disk, Memory, and Network are now available. Use filters to narrow down the set of VMs being inspected, and use the time selector or in-chart time selection to change the time window. VMs with the Monitoring agent installed get detailed memory and disk analysis out of the box.

## June 05, 2020

**Cloud Logging**

v2

Change

Custom retention is now generally available (GA). In order to have time to explore this feature, you won't be charged for extended retention of logs until March 31, 2021. To learn more, see the [Logging pricing section on the Pricing for Google Cloud's operations suite page](https://cloud.google.com/stackdriver/pricing#logging-costs).

## June 03, 2020

**Cloud Logging**

v2

Feature

In the Logs Viewer (Preview), you can now save your queries, which can then be viewed and run from the **Saved** queries tab. For more information, see the [Saved queries section on the Building queries page](https://docs.cloud.google.com/logging/docs/view/building-queries#saved-queries).

## May 20, 2020

**Cloud Monitoring**

v3

Feature

Cloud Monitoring introduces an improved experience for viewing and managing incidents. Improvements include performance optimizations for Workspaces with large numbers of incidents, summary statics, and the ability to filter by alerting policy name, metric type, and resource type. For more information, see [Incidents and events](https://cloud.google.com/monitoring/alerts/incidents-events).

## May 19, 2020

**Cloud Monitoring**

v3

Change

Alert notifications delivered by email now come from "alerting-noreply@google.com" instead of "alerts@stackdriver.com".

## May 18, 2020

**Cloud Logging**

v2

Feature

**Logs Viewer** now contains the **Logs field explorer** panel, which lets you view aggregation-based results for your project's log fields and makes it more efficient to refine queries. To learn more, go to the [Logs Viewer (Preview) page](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface).

## May 14, 2020

**Cloud Monitoring**

v3

Change

Starting in version 6.0.2, the Cloud Monitoring agent is available for the Ubuntu LTS 20.04 (Focal Fossa) distribution.

## May 12, 2020

**Cloud Profiler**

v2

Change

The Cloud Profiler Python agent is now generally available. See [Profiling Python applications](https://cloud.google.com/profiler/docs/profiling-python) for information on configuring your Python application.

## May 11, 2020

**Cloud Logging**

v2

Feature

You can now use regular expressions to query your logs data and create filters. For more information, go to [Using regular expressions](https://docs.cloud.google.com/logging/docs/view/logging-query-language#regular-expressions).

## May 08, 2020

**Cloud Monitoring**

v3

Feature

Monitoring Query Language (MQL) is now available in Beta. MQL is an expressive, text-based interface to Cloud Monitoring time-series data. With MQL, you can create charts you can't create any other way. You can access MQL from both the Cloud Console and the Monitoring API. For more information, see [Introduction to Monitoring Query Language](https://cloud.google.com/monitoring/mql/).

## April 28, 2020

**Cloud Monitoring**

v3

Deprecated

The `stack-install.sh` and the `install-monitoring-agent.sh` installation scripts for the Cloud Monitoring agent for Linux [are deprecated](https://cloud.google.com/stackdriver/docs/deprecations/mon-agent-install). Refer to the [Installing the Cloud Monitoring agent](https://cloud.google.com/monitoring/agent/install-agent#joint-install) guide for the latest installation procedures.

Deprecated

The 5.x version of the Cloud Monitoring agent for Linux is deprecated. Users are encouraged [to upgrade their agents](https://cloud.google.com/monitoring/agent/install-agent#upgrade) as soon as possible.

## April 27, 2020

**Cloud Logging**

v2

Change

The Logs Viewer (Preview) is now GA. To learn more, go to the [Logs Viewer (Preview) Overview page](https://docs.cloud.google.com/logging/docs/view/logs-viewer-preview).

## April 20, 2020

**Cloud Profiler**

v2

Change

The Cloud Profiler Node.js agent no longer supports release 8 of Node.js.

Change

The Cloud Profiler Node.js agent is now generally available. See [Profiling Node.js applications](https://cloud.google.com/profiler/docs/profiling-nodejs) for information on configuring your Node.js application.

Feature

The Cloud Profiler Node.js agent now supports release 12 of Node.js. See [Profiling Node.js applications](https://cloud.google.com/profiler/docs/profiling-nodejs) for information on configuring your Node.js application.

## March 30, 2020

**Cloud Monitoring**

v3

Feature

You can now write time-series data for custom and Prometheus metrics at the rate of 1 data point every 10 seconds. This was previously limited to 1 point every minute.

Change

Data for custom and Prometheus metrics is now retained for 24 months. Previously, the retention period was 6 weeks.

**Cloud Trace**

v2

Feature

You can now use [OpenTelemetry](https://opentelemetry.io/) with [Go](https://cloud.google.com/trace/docs/setup/go-ot) and [Node.js](https://cloud.google.com/trace/docs/setup/nodejs-ot) to instrument your applications running on GKE and Compute Engine.

## March 24, 2020

**Cloud Profiler**

v2

Change

Integration of Stackdriver Profiler with Virtual Private Cloud Service Controls is now Generally Available. For more information, see [VPC Service Controls documentation](https://cloud.google.com/vpc-service-controls/docs/).

## March 17, 2020

**Cloud Logging**

v2

Change

Incoming log entries must have timestamps that don't exceed the [logs retention periods](https://docs.cloud.google.com/logging/quotas#logs_retention_periods) in the past, and that don't exceed 24 hours in the future. Log entries outside those time boundaries aren't ingested by Cloud Logging.

## March 12, 2020

**Cloud Logging**

v2

Change

Cloud Logging Agent for Windows version 1-11 is now available. This version upgrades `fluentd` from 1.4.2 to 1.7.4. Go to [Installing the Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent/installation) for information on installing this version of the agent.

## March 10, 2020

**Cloud Logging**

v2

Feature

Logs Viewer (Preview) now contains a histogram panel. The histogram panel lets you visualize your logs data to more easily spot patterns and troubleshoot issues. For more information, see [Using Logs Viewer (Preview)](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface).

## February 24, 2020

**Cloud Logging**

v2

Feature

Beta release: You can now use the new Logs Viewer (Preview) to view, parse and analyze log data, and refine your query parameters. Go to [Logs Viewer interface (Preview)](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface) for more information.

**Cloud Monitoring**

v3

Feature

Stackdriver Monitoring agent version 6.0.0 is now available for the following distributions:

  * CentOS 7
  * Ubuntu LTS 16.04 (Xenial Xerus) and Ubuntu LTS 18.04 (Bionic Beaver)
  * Ubuntu Minimal LTS 16.04 (Xenial Xerus) and Ubuntu Minimal LTS 18.04 (Bionic Beaver)
  * Amazon Linux AMI (except Amazon Linux 2.0 AMI)



Change

Stackdriver Monitoring is available exclusively in the Cloud Console. For more information, see [Monitoring in the Google Cloud console](https://cloud.google.com/monitoring/docs/monitoring_in_console).

## February 20, 2020

**Cloud Trace**

v2

Change

Integration of Cloud Trace with Virtual Private Cloud Service Controls is now generally available. For more information, see [VPC Service Controls documentation](https://cloud.google.com/vpc-service-controls/docs/).

## February 19, 2020

**Cloud Monitoring**

v3

Feature

Starting in version 6.0.0, the Stackdriver Monitoring agent is available for the Ubuntu 19.10 (Eoan Ermine) distribution.

**Cloud Trace**

v2

Feature

[Beta release](https://cloud.google.com/products/#product-launch-stages): Export of Stackdriver Trace data to BigQuery. For more information, see [Managing Trace exports](https://cloud.google.com/trace/docs/trace-export-overview).

## February 18, 2020

**Cloud Monitoring**

v3

Feature

Stackdriver Monitoring agent version 6.0.0 is now available for the Debian 9 distribution.

## February 17, 2020

**Cloud Logging**

v2

Change

BETA: You can now configure the retention periods of your logs data. For more information, go to [Storing logs](https://docs.cloud.google.com/logging/docs/storage).

## February 14, 2020

**Cloud Monitoring**

v3

Feature

You can now send notifications from your alerting policies to Cloud Pub/Sub topics. For more information, see [Notification options](https://cloud.google.com/monitoring/support/notification-options).

Change

The Stackdriver Monitoring Dashboard API is now Generally Available. You can use this feature to programmatically manage your dashboards and charts. See [Managing dashboards by API](https://cloud.google.com//monitoring/dashboards/api-dashboard) for documentation, and [`Dashboard`](https://cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards) for reference material.

## February 11, 2020

**Cloud Monitoring**

v3

Feature

Stackdriver Monitoring agent version 6.0.0 has been released to the CentOS 8 distribution.

## February 06, 2020

**Cloud Monitoring**

v3

Feature

Starting in version 6.0.0, the Stackdriver Monitoring agent is available for the Debian 10 distribution.

**Cloud Trace**

v2

Change

The [Stackdriver Trace API v2](https://cloud.google.com/trace/docs/reference) is now Generally Available.

## January 31, 2020

**Cloud Monitoring**

v3

Feature

Stackdriver Monitoring Agent version 6.0.0 is now available, and the release will gradually roll out to the various Linux distributions. This version is built on a [fork of `collectd` version 5.8.1](https://github.com/Stackdriver/collectd) and includes the following changes:

  * drops support for [various third-party integrations](https://cloud.google.com/stackdriver/docs/deprecations/third-party-apps).
  * changes the file path for configuring an HTTP proxy when [installing the agent](https://cloud.google.com/monitoring/agent/install-agent#joint-install).



Feature

Stackdriver Monitoring agent version 6.0.0 is now available for the SUSE and SUSE Linux Enterprise Server (SLES) Linux distributions.

## January 17, 2020

**Cloud Logging**

v2

Feature

Customer-managed encryption keys (CMEK) for the Logs Router are now Generally Available (GA). CMEK lets you create, control, and manage encryption keys to meet your data compliance needs. For details, go to [Enabling customer-managed encryption keys for Logs Router](https://docs.cloud.google.com/logging/docs/routing/managed-encryption).

## January 13, 2020

**Cloud Monitoring**

v3

Change

Stackdriver Monitoring in the Cloud Console is Generally Available and is the default option. For a limited period of time, you also have the option to use the classic Stackdriver Monitoring Console. Your configuration information, such as uptime checks and alerting policies, is accessible and changeable, from the Cloud Console and from the classic Stackdriver Monitoring Console. For more information, see [Monitoring in the Google Cloud console](https://cloud.google.com/monitoring/docs/monitoring_in_console).

## December 16, 2019

**Cloud Logging**

v2

Feature

GA release: You can now use partitioned tables for logs exports to BigQuery. For details, go to [Partitioned tables](https://docs.cloud.google.com/logging/docs/export/bigquery#partition-tables).

**Cloud Trace**

v2

Feature

Integration of Stackdriver Trace with Virtual Private Cloud Service Controls is now beta. For more information, see [VPC Service Controls documentation](https://cloud.google.com/vpc-service-controls/docs/).

## December 13, 2019

**Cloud Logging**

v2

Change

Google Kubernetes Engine (GKE) version 1.15, which is now generally available, drops support for GKE versions 1.12 and earlier. As a result, the beta version of Stackdriver Kubernetes Engine Monitoring is no longer supported. If your GKE clusters are running version 1.12 or earlier, then you must upgrade them as soon as possible.

**Cloud Monitoring**

v3

Change

Google Kubernetes Engine (GKE) version 1.15, which is now generally available, drops support for GKE versions 1.12 and earlier. As a result, the beta version of Stackdriver Kubernetes Engine Monitoring is no longer supported. If your GKE clusters are running version 1.12 or earlier, then you must upgrade them as soon as possible.

**Cloud Profiler**

v2

Feature

Strackdriver Profiler supports Istio on Google Kubernetes Engine for [Go](https://cloud.google.com/profiler/docs/profiling-go), [Java](https://cloud.google.com/profiler/docs/profiling-java), [Python](https://cloud.google.com/profiler/docs/profiling-python), and [Node.js](https://cloud.google.com/profiler/docs/profiling-nodejs) services. This feature is now in **Beta**.

**Error Reporting**

v1beta1

Change

Error Reporting now infers the service name and version from the `logEntry` fields named `k8s-pod/serving_knative_dev/service` and `k8s-pod/serving_knative_dev/revision` for Knative Serving labels on Cloud Run on Google Kubernetes Engine. This replaces the current default value of `gke_instances` for service name.

## December 11, 2019

**Cloud Logging**

v2

Deprecated

Legacy Stackdriver support for Google Kubernetes Engine (GKE) is deprecated. If you're using Legacy Stackdriver, then you must [migrate to Stackdriver Kubernetes Engine Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine/migration) before Legacy Stackdriver is decommissioned. For more information, see [Legacy Stackdriver support for GKE deprecation](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy).

**Cloud Monitoring**

v3

Deprecated

Legacy Stackdriver support for Google Kubernetes Engine (GKE) is deprecated. If you're using Legacy Stackdriver, then you must [migrate to Stackdriver Kubernetes Engine Monitoring](https://cloud.google.com/monitoring/kubernetes-engine/migration) before Legacy Stackdriver is decommissioned. For more information, see [Legacy Stackdriver support for GKE deprecation](https://cloud.google.com/stackdriver/docs/deprecations/legacy).

## December 10, 2019

**Cloud Profiler**

v2

Feature

Integration of Stackdriver Profiler with Virtual Private Cloud Service Controls is now beta. For more information, see [VPC Service Controls documentation](https://cloud.google.com/vpc-service-controls/docs/).

## December 09, 2019

**Cloud Monitoring**

v3

Feature

The Stackdriver Monitoring Dashboard API is now in Beta release. You can use this feature to programmatically manage your dashboards and charts. See [Managing dashboards by API](https://cloud.google.com//monitoring/dashboards/api-dashboard) for documentation, and [`Dashboard`](https://cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards) for reference material.

## December 04, 2019

**Cloud Monitoring**

v3

Feature

Stackdriver Monitoring in the Cloud Console is in beta release. Your configuration information, such as uptime checks and alerting policies, is accessible and changeable, from the Cloud Console and from the classic Stackdriver Monitoring Console. For more information about the beta, see [Monitoring in the Google Cloud console](https://cloud.google.com/monitoring/docs/monitoring_in_console).

## November 20, 2019

**Cloud Trace**

v2

Feature

The **Trace list** page has a new menu-driven filtering solution that is in Beta release testing. For more information, see [Finding and viewing traces](https://cloud.google.com/trace/docs/finding-traces).

## November 18, 2019

**Cloud Logging**

v2

Feature

Customer-managed encryption keys (CMEK) for the Logs Router are now available in Beta. CMEK lets you create, control, and manage encryption keys to meet your data compliance needs. For details, go to [Enabling customer-managed encryption keys for Logs Router](https://docs.cloud.google.com/logging/docs/routing/managed-encryption).

## November 14, 2019

**Cloud Monitoring**

v3

Feature

The Service Monitoring API is now in Beta release. You can use this feature to create services, set service-level objectives (SLOs), and create alerting policies to monitor your SLOs. See [Service monitoring](https://cloud.google.com/monitoring/service-monitoring/) for documentation, and [`services`](https://cloud.google.com/monitoring/api/v3/#service-monitoring) for reference material.

## September 20, 2019

**Cloud Logging**

v2

Feature

Beta release: Stackdriver Logging now offers partitioned tables for exports to BigQuery. For details, go to [Partitioned tables](https://docs.cloud.google.com/logging/docs/export/bigquery#partition-tables).

## September 10, 2019

**Cloud Logging**

v2

Feature

Stackdriver Logging now lets you save your advanced log queries to a Saved Searches library, where they can be managed and shared. Go to [Saved searches](http://cloud.google.com/logging/docs/view/overview#saved-searches) for details.

Change

When creating a new Google Kubernetes Engine (GKE) cluster, Stackdriver Kubernetes Engine Monitoring is now the default Stackdriver support option. This is a change from prior versions where Stackdriver Logging and Stackdriver Monitoring were the default Stackdriver support option. For more information, see [Overview of Stackdriver support for GKE](https://docs.cloud.google.com/monitoring/kubernetes-engine).

**Cloud Monitoring**

v3

Change

When creating a new Google Kubernetes Engine (GKE) cluster, Stackdriver Kubernetes Engine Monitoring is now the default Stackdriver support option. This is a change from prior versions where Stackdriver Logging and Stackdriver Monitoring were the default Stackdriver support option. For more information, see [Overview of Stackdriver support for GKE](https://cloud.google.com/monitoring/kubernetes-engine/).

## August 08, 2019

**Cloud Monitoring**

v3

Feature

[Stackdriver Monitoring](https://cloud.google.com/monitoring/uptime-checks) has two new uptime check features: SSL certificate validation and regex negation content matching.

## May 21, 2019

**Cloud Logging**

v2

Feature

[Stackdriver Kubernetes Engine Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine) is now generally available. Users of the legacy Stackdriver support for [monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine/legacy-stackdriver/monitoring) and [logging](https://docs.cloud.google.com/monitoring/kubernetes-engine/legacy-stackdriver/logging) for Google Kubernetes Engine are encouraged to [migrate to Stackdriver Kubernetes Engine Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine/migration) as soon as possible.

**Cloud Monitoring**

v3

Feature

[Stackdriver Kubernetes Engine Monitoring](https://cloud.google.com/monitoring/kubernetes-engine/) is now generally available. Users of the legacy Stackdriver support for [monitoring](https://cloud.google.com/monitoring/kubernetes-engine/legacy-stackdriver/monitoring) and [logging](https://cloud.google.com/monitoring/kubernetes-engine/legacy-stackdriver/logging) for Google Kubernetes Engine are encouraged to [migrate to Stackdriver Kubernetes Engine Monitoring](https://cloud.google.com/monitoring/kubernetes-engine/migration) as soon as possible.

## May 08, 2019

**Cloud Profiler**

v2

Feature

Java 11 is now supported. For more information, see [Profiling Java](https://cloud.google.com/profiler/docs/profiling-java).

**Error Reporting**

v1beta1

Feature

**API**

Error events written as instances of [`ReportedErrorEvent`](https://cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report#ReportedErrorEvent) generate properly formatted error messages in Stackdriver Logging.

## May 02, 2019

**Cloud Monitoring**

v3

Feature

Stackdriver Workspace creation is now a one-step operation.

## April 23, 2019

**Cloud Logging**

v2

Change

The maximum size of a log entry has been increased to 256 KB from 100 KB. For details on logging usage limits, go to [Quotas and limits](https://docs.cloud.google.com/logging/quotas).

**Cloud Monitoring**

v3

Feature

The OpenCensus library is now generally available as the official library for user-defined metrics in Stackdriver Monitoring. The [Custom metrics with OpenCensus](https://cloud.google.com/monitoring/custom-metrics/open-census) page includes samples in Go, Java, Node.js, and Python.

## April 15, 2019

**Cloud Logging**

v2

Feature

A new Windows version (v1-9) of the Stackdriver Logging agent is now available. The new version saves the agent service logs on disk for easier troubleshooting and supports the `config.d` configuration extension directory.

## March 26, 2019

**Cloud Profiler**

v2

Feature

Stackdriver Profiler is now generally available. Stackdriver Profiler lets you analyze and understand the performance of your Go, Java, Node.js or Python applications. For more information, see [About Stackdriver Profiler](https://cloud.google.com/profiler/docs/about-profiler).

## March 18, 2019

**Cloud Monitoring**

v3

Feature

The [Uptime Configuration API](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs) is now complete and GA. The API, part of the [Stackdriver Monitoring API](https://cloud.google.com/monitoring/api/ref_v3/rest/), lets you create, edit, and manage [uptime checks](https://cloud.google.com/monitoring/uptime-checks/).

## March 15, 2019

**Cloud Logging**

v2

Change

Stackdriver agents are subject to an updated [deprecation policy](https://cloud.google.com/stackdriver/docs/agent-deprecation-policy). As part of this transition, the next major version of the Stackdriver Monitoring and Stackdriver Logging agents will stop supporting operating systems that are at the end of their lifecycle, as well as some [third-party agent plugins](https://monitoring/agent/plugins/).

**Cloud Monitoring**

v3

Change

Stackdriver agents are subject to an updated [deprecation policy](https://cloud.google.com/stackdriver/docs/agent-deprecation-policy). As part of this transition, the next major version of the Stackdriver Monitoring and Stackdriver Logging agents will stop supporting operating systems that are at the end of their lifecycle, as well as some [third-party agent plugins](https://cloud.google.com/monitoring/agent/plugins/).

## March 12, 2019

**Cloud Profiler**

v2

Feature

Python is now supported. For more information, see [Profiling Python](https://cloud.google.com/profiler/docs/profiling-python).

## February 28, 2019

**Cloud Profiler**

v2

Feature

The new **Color mode** filter option lets you color the flame graph frames by package name, by the metric consumption of the function, or by the metric consumption of the function and its children. For more information, see [Color mode](https://cloud.google.com/profiler/docs/filtering-profiles#color-filter).

## February 22, 2019

**Cloud Logging**

v2

Change

You now have two choices for the access control model when creating a Cloud Storage bucket: bucket-only (new) and object-level. Select **Set object-level and bucket-level permissions** as the access control model during bucket creation if you intend to use the bucket as a sink destination. See [Errors exporting to Cloud Storage](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#errors_exporting_to_cloud_storage) for details.

## February 08, 2019

**Cloud Monitoring**

v3

Feature

The Stackdriver Monitoring Agent now supports Ubuntu 18.04 LTS ("Bionic Beaver").

## January 22, 2019

**Cloud Logging**

v2

Change

In the Stackdriver Logging API, log sinks, metrics, and exclusions have two new output-only fields: create time and last update time. See [LogSink](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/sinks) for an example. If this information isn't available for older resources, these fields aren't present.

## January 18, 2019

**Error Reporting**

v1beta1

Feature

**Error detection for Python applications** has been improved. You might see more newly detected error groups or receive more notifications.

## December 18, 2018

**Cloud Trace**

v2

Change

Trace list now limits HTTP method and HTTP status matches to trace root spans. See [Filter traces](https://cloud.google.com/trace/docs/finding-traces#filter_traces) for more details.

Feature

You can now filter traces for analysis reports by the full URI, by the URI prefix, or by using trace filter. See [Create a new analysis report](https://cloud.google.com/trace/docs/analysis-reports#create_a_new_analysis_report) for details.

## December 07, 2018

**Cloud Profiler**

v2

Feature

Go 1.11 for App Engine standard environment is now supported. For more information, see [Profiling Go](https://cloud.google.com/profiler/docs/profiling-go).

## December 06, 2018

**Cloud Monitoring**

v3

Change

A mechanism to collect monitoring data from Prometheus clients, which can be deployed as a sidecar in the same Kubernetes pod as a working Prometheus server, is now available. See [Using Prometheus](https://cloud.google.com/monitoring/kubernetes-engine/prometheus) for more information.

## December 05, 2018

**Cloud Monitoring**

v3

Feature

Documentation for using [OpenCensus](https://opencensus.io) to capture custom metrics in Java applications is now available. See [Custom metrics with OpenCensus](https://cloud.google.com/monitoring/custom-metrics/open-census) for more information.

## December 03, 2018

**Cloud Logging**

v2

Feature

The Logs Viewer has a new option to display a log entry in its resource context. It can also pin a log entry while allowing you to change the display context. See [Viewing Logs](https://docs.cloud.google.com/logging/docs/view/overview) for details.

## November 16, 2018

**Cloud Monitoring**

v3

Change

The new UI for creating alerting policies is now complete and Generally Available. This interface, based on Metrics Explorer, offers fine-grained control over the selection of the metrics used in alerting conditions. See [Managing Alerting Policies](https://cloud.google.com/monitoring/alerts/using-alerting-ui) for more information.

## November 01, 2018

**Cloud Logging**

v2

Feature

You can now view error and success metrics for your log sinks using [export system metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics#system_logs-based_metrics).

## October 31, 2018

**Cloud Trace**

v2

Change

Stackdriver Trace enforces consumption-based pricing as of November 1, 2018 at 00:00 PDT. For more information, see [Stackdriver Pricing](https://cloud.google.com/stackdriver/pricing).

Change

On November 1, 2018, Stackdriver Trace begins enforcing a daily trace spans ingestion quota. See [Stackdriver Trace Quotas & Limits](https://cloud.google.com/trace/docs/quotas) for details.

## October 19, 2018

**Cloud Logging**

v2

Feature

You can now link from certain App Engine request logs to a detailed trace that explains the request's latency. You can also filter log entries according to their latencies, and if they contain detailed trace data viewable by Stackdriver Trace. See [Viewing latency in Trace](http://cloud.google.com/logging/docs/view/overview#show-latency) for details.

## October 10, 2018

**Cloud Monitoring**

v3

Feature

A new UI for creating alerting policies is available in Beta. This interface, based on Metrics Explorer, offers fine-grained control over the selection of the metrics used in alerting conditions. See [Managing Alerting Policies](https://cloud.google.com/monitoring/alerts/using-alerting-ui) for more information.

## October 01, 2018

**Cloud Logging**

v2

Feature

The Logs Viewer can now download up to 300 log entries in JSON or CSV format. See [Viewing Logs](https://docs.cloud.google.com/logging/docs/view/overview) for details.

## September 19, 2018

**Cloud Monitoring**

v3

Change

[Stackdriver Kubernetes Monitoring](https://cloud.google.com/monitoring/kubernetes-engine/) (Beta) for Kubernetes version 1.10.6 and above, restores the managed support for Kubernetes Monitoring. You can also [upgrade your existing clusters](https://cloud.google.com/stackdriver/docs/solutions/gke/installing#migrating) to this release, no matter which (if any) Stackdriver support they had before. Note the warnings about [incompatibilities](https://cloud.google.com/monitoring/kubernetes-engine/migration) between the old and new Stackdriver support.

## September 18, 2018

**Cloud Monitoring**

v3

Feature

The legends for Stackdriver charts have been significantly improved. Legends now support more than one labeled column. The legend provides a selected set of columns as a default, but users can choose the columns they want to see in the legend. All columns are sortable. The legend detects a configuration of columns that exceeds the available space, and provides scrollbars. The resizing of the legends is also improved. For details, see [Configuring Legends](https://cloud.google.com/monitoring/charts/working-with-legends).

## September 14, 2018

**Cloud Logging**

v2

Feature

The format of service account names for older log [sinks](https://docs.cloud.google.com/logging/docs/export#sink-terms) is being changed so that all log sinks will have consistent service account names. This naming format has already been applied to project-level sinks on BigQuery, Cloud Pub/Sub, and Cloud Storage permission pages. In the coming weeks, this naming format will be applied to organization-level sinks and folder-level sinks, and to sinks listed on the **Logs Exports** page in the Logs Viewer. There are no associated changes to functionality or granted permissions.

## September 10, 2018

**Cloud Monitoring**

v3

Change

"Stackdriver accounts" have been renamed "Workspaces" to reflect their use as a "single pane of glass" through which you view resources from multiple projects and AWS accounts. There is no change in their functionality, but we have improved the documentation for them.

## September 05, 2018

**Cloud Logging**

v2

Feature

**Access Transparency** logging is now Generally Available. See [Overview of Access Transparency](https://cloud.google.com/logging/docs/audit/access-transparency-overview) for details.

**Cloud Trace**

v2

Feature

Billing enforcement for Trace has been postponed to November 1, 2018, rather than the previously announced date of September 30, 2018. You can now estimate your bill for your usage of Trace, according to the new pricing and in advance of billing enforcement. See [Estimating your bills](https://cloud.google.com/stackdriver/estimating-bills) for details.

## August 02, 2018

**Cloud Profiler**

v2

Feature

The new **Weight** filter lets you select and graph profiles that consume the most of the profile's measured metric. For more information, see [Weight filter](https://cloud.google.com/profiler/docs/selecting-profiles#weight-filter).

## July 25, 2018

**Cloud Logging**

v2

Change

Audit logs exports to BigQuery now feature a compact format. On March 1, 2019, the older extended format will be removed.

## July 24, 2018

**Cloud Profiler**

v2

Feature

The new **Compare To** option lets you compare profiles that differ by end time, zone, or service version. For more information, see [Comparing profiles](https://cloud.google.com/profiler/docs/comparing-profiles).

## June 29, 2018

**Cloud Logging**

v2

Change

On July 1, 2018 at 00:00 PDT, Stackdriver switches to consumption-based pricing. For more information, see [Stackdriver Pricing](https://cloud.google.com/stackdriver/pricing_v2).

**Cloud Monitoring**

v3

Change

On July 1, 2018 at 00:00 PDT, Stackdriver switches to consumption-based pricing. For more information, see [Stackdriver Pricing](https://cloud.google.com/stackdriver/pricing_v2).

## June 26, 2018

**Cloud Logging**

v2

Feature

You can now immediately disable all logs ingestion. For instructions, see [Stopping all logs ingestion](https://docs.cloud.google.com/logging/docs/exclusions#stop-logs).

## June 19, 2018

**Cloud Logging**

v2

Feature

Google Cloud Storage logs streaming time has been reduced from 12 hours to 3 hours. For details, see [Using Exported Logs](https://docs.cloud.google.com/logging/docs/export/using_exported_logs#gcs-availability).

**Cloud Monitoring**

v3

Feature

If you want to minimize the **AWS permissions** you give to Stackdriver, then see [Minimal AWS Permissions](https://cloud.google.com/monitoring/support/minimal-aws-permissions).

## June 18, 2018

**Cloud Logging**

v2

Change

**Between June 18, 2018 at 06:00 PDT and July 1, 2018 at 00:00 PDT, your use of Stackdriver is free**. The service tiers have been removed, and you can experience all features without incurring costs. Thereafter, Stackdriver switches to consumption-based pricing. For more information, see [Upcoming Pricing](https://cloud.google.com/stackdriver/pricing_v2).

**Cloud Monitoring**

v3

Change

**Between June 18, 2018 at 06:00 PDT and July 1, 2018 at 00:00 PDT, your use of Stackdriver is free**. The service tiers have been removed, and you can experience all features without incurring costs. Thereafter, Stackdriver switches to consumption-based pricing. For more information, see [Upcoming Pricing](https://cloud.google.com/stackdriver/pricing_v2).

## June 12, 2018

**Cloud Logging**

v2

Feature

You can now enable and configure your Data Access audit logs using the Google Cloud console. For details, see [Configuring Data Access logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).

## May 24, 2018

**Cloud Monitoring**

v3

Change

Any Stackdriver free trials created after May 29, 2018 will expire on June 30, 2018. After June 30, 2018, free trials will be replaced with a free monthly allocation of logs and metrics. For more information about Stackdriver's new consumption-based pricing, see [Stackdriver Upcoming Pricing](https://cloud.google.com/stackdriver/pricing_v2).

## May 23, 2018

**Cloud Monitoring**

v3

Change

Custom dashboards and pages for resource groups are now limited to 25 charts. Any dashboards or groups pages with more than 25 charts will continue to work, but you will not be able to add additional charts to them.

## May 22, 2018

**Cloud Monitoring**

v3

Feature

You can now see your Monitoring usage metrics and estimate your bill for your usage of Monitoring, according to the new Stackdriver pricing and in advance of billing enforcement. See [Estimating your bills](https://cloud.google.com/stackdriver/estimating-bills) for details.

## May 21, 2018

**Cloud Monitoring**

v3

Feature

A new UI for creating conditions in alerting policies is available in Beta. This UI, based on Metrics Explorer, offers fine-grained control over the selection of the metrics used in alerting conditions. See [Managing Alerting Policies](https://cloud.google.com/monitoring/alerts/using-alerting-ui) for more information.

## May 17, 2018

**Cloud Logging**

v2

Feature

You can now see your Logging usage and estimate your bill according to the new Stackdriver pricing and in advance of billing enforcement. See [Estimating your bills](https://docs.cloud.google.com/stackdriver/estimating-bills) for details.

## May 15, 2018

**Cloud Profiler**

v2

Feature

The new **Focus** filter lets you analyze the aggregate resource consumption of a specific function and the proportion of time spent in the function by different callers. For more information, see [Using the **Focus** Filter](https://cloud.google.com/profiler/docs/filtering-profiles#focus-filter).

## May 11, 2018

**Cloud Monitoring**

v3

Change

If you are using custom IAM roles, any roles that load Stackdriver Monitoring dashboards now require additional IAM permissions. The `monitoring.dashboards.*` and `monitoring.publicWidgets.*` permissions are now public, and custom roles used to load dashboards must now include them. See [Stackdriver Monitoring Access Control](https://cloud.google.com/monitoring/access-control#roles) for more information.

## May 08, 2018

**Cloud Logging**

v2

Feature

You can now specify custom fields in your Logs Viewer log-entry summary lines. See [Add custom fields](https://docs.cloud.google.com/logging/docs/view/overview#custom-fields) for details.

## May 02, 2018

**Cloud Logging**

v2

Feature

[Stackdriver Kubernetes Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine) is released in Beta for Kubernetes 1.10 clusters running in [Kubernetes Engine](https://cloud.google.com/kubernetes-engine/docs/). The previous Stackdriver support is still available for those who do not opt into this Beta release. This release affects Logging by introducing new [monitored resource types](https://cloud.google.com/logging/docs/api/v2/resource-list#tag_k8s_cluster) and new [Kubernetes metrics](https://cloud.google.com/monitoring/api/metrics_kubernetes).

**Cloud Monitoring**

v3

Feature

[Stackdriver Kubernetes Monitoring](https://cloud.google.com//monitoring/kubernetes-engine) is released in Beta for Kubernetes 1.10 clusters running in [Kubernetes Engine](https://cloud.google.com//kubernetes-engine/docs/). The previous Stackdriver support is still available for those who do not opt into this Beta release. The release introduces new [monitored resource types](https://cloud.google.com//monitoring/api/resources#tag_k8s_cluster) and new [Kubernetes metrics](https://cloud.google.com//monitoring/api/metrics_kubernetes#kubernetes). The monitoring features are free to customers during the Beta period.

## April 26, 2018

**Cloud Monitoring**

v3

Change

You can now use variables in the documentation associated with alerting policies to pull specific details about the alert into notifications, to create playbook information for responders. See [Additional documentation tools](https://cloud.google.com/monitoring/alerts/doc-variables) for more information. The Webhooks and Slack notification channels now receive a copy of this enhanced documentation as part of alert notifications. Additionally, email notifications from alerting policies now use HTML-formatted messages.

## April 19, 2018

**Cloud Monitoring**

v3

Feature

Boolean metrics can now be queried and charted.

## April 17, 2018

**Cloud Monitoring**

v3

Change

The [Using Alerting Policies](https://cloud.google.com/monitoring/alerts) documentation has been updated to provide additional guides and links to sample code for managing alerting policies and notification channels programmatically. The update also removes some obsolete service-tier information.

## April 10, 2018

**Cloud Logging**

v2

Feature

You can now specify that the Stackdriver Logging agent converts your payloads to JSON format for certain log inputs. For details on enabling this feature, see [Structured Logging](https://docs.cloud.google.com/logging/docs/structured-logging).

## April 04, 2018

**Cloud Trace**

v2

Feature

The Trace Viewer now allows you to view trace spans for related Google Cloud Platform projects in one view. See [Viewing traces across projects](https://cloud.google.com/trace/docs/cross-project-traces) for details.

## March 28, 2018

**Cloud Monitoring**

v3

Change

Stackdriver now loads charts much more quickly, especially when the chart contains a long time span.

**Cloud Profiler**

v2

Feature

Stackdriver Profiler is released in Beta.

**Cloud Trace**

v2

Feature

Stackdriver Trace Data Access audit logs are now Generally Available. See [Stackdriver Trace Audit Logging](https://cloud.google.com/trace/docs/audit-logging) for details.

## March 26, 2018

**Cloud Monitoring**

v3

Change

A new option on the Dashboards menu, **Public Charts** , lets you see a list of all the shared charts. You can also use this page to remove sharing from a chart. The on-chart indicator that the chart is shared has been removed.

## March 12, 2018

**Cloud Logging**

v2

Change

Beginning on June 30, 2018, Stackdriver is switching to consumption-based pricing, including revised quotas. For more information, see [Stackdriver Upcoming Pricing](https://cloud.google.com/stackdriver/pricing_v2).

Feature

Logging data retention has been increased to 30 days for all projects.

**Cloud Monitoring**

v3

Change

Beginning on June 30, 2018, Stackdriver is switching to consumption-based pricing, including revised quotas. For more information, see [Stackdriver Upcoming Pricing](https://cloud.google.com//stackdriver/pricing_v2).

**Cloud Trace**

v2

Change

Beginning on June 30, 2018, Stackdriver is switching to consumption-based pricing, including revised quotas. For more information, see [Stackdriver Upcoming Pricing](https://cloud.google.com/stackdriver/pricing_v2).

## March 08, 2018

**Cloud Monitoring**

v3

Feature

The `AlertPolicy` and `NotificationChannels` APIs are now in Beta release. See [Alerting policies](https://cloud.google.com/monitoring/api/v3/#alerting-policies) and [Notification channels](https://cloud.google.com/monitoring/api/v3/#notification-channels) for more information.

## February 27, 2018

**Cloud Trace**

v2

Feature

The Trace Viewer now associates logs entries with trace spans when the LogEntry `span_id` field is specified. See [Integrating with Cloud Logging](https://cloud.google.com/trace/docs/trace-log-integration) for details.

Fixed

The Trace Viewer now follows your scroll through the span details page, making it easier to see span details of large traces.

## February 01, 2018

**Cloud Logging**

v2

Feature

The Logging agent now supports partial success for logs ingestion. Any invalid log entries in a full set will be dropped, and the valid log entries now will be successfully ingested into the Stackdriver Logging API; previously, the full set would have been dropped if it contained any invalid log entries. To enable partial success, upgrade your Logging agent to [google-fluentd v1.5.27](https://github.com/GoogleCloudPlatform/google-fluentd/releases/tag/v1.5.27).

## January 29, 2018

**Cloud Monitoring**

v3

Fixed

The Stackdriver email reports that you can configure for your Stackdriver account have been improved. Issues with the content and the delivery of reports have been fixed, and the _from_ address for the reports has been changed from `monitoring-noreply@stackdriver.google.com` to `monitoring-noreply@google.com`. The Utilization section, present only if the Monitoring Agent is installed, now lists the 10 groups with the highest utilization, and a new summary row reports overall utilization for the Stackdriver account.

## January 17, 2018

**Cloud Monitoring**

v3

Change

The name of the Monitoring agent process on Windows has been updated. It now shows up in the system process list as `StackdriverMonitoring`.

## January 12, 2018

**Cloud Trace**

v2

Feature

The Trace viewer now shows sub-millisecond resolution for Trace spans.

## January 09, 2018

**Cloud Trace**

v2

Feature

The Trace viewer now displays span annotations and message events written with the [Stackdriver Trace API v2](https://cloud.google.com/trace/docs/reference/v2/rest/). See [Viewing Trace Details](https://cloud.google.com/trace/docs/viewing-details#annotating_spans) for more information.

## January 08, 2018

**Cloud Monitoring**

v3

Change

The performance of the Monitoring dashboards and charts has been improved. Additionally, a new version of Metrics Explorer is available, and the metric-selection interface has been greatly improved, allowing arbitrary label filtering and group-by functionality. This interface is also used for creating dashboard charts, making the process consistent across the two tasks. See [Using Charts](https://cloud.google.com/monitoring/charts) for more information.

## December 19, 2017

**Error Reporting**

v1beta1

Feature

**Resolution Status** features are now Generally Available. You can now assign a status to your error groups, making it easier to triage errors.

## December 14, 2017

**Cloud Monitoring**

v3

Change

**Alerting events page** : An updated implementation has required some user interface changes. The alerting events page (**Alerting > Events**) no longer shows a heatmap or counts of events in each category.

## December 13, 2017

**Cloud Logging**

v2

Feature

Filtering logs by **time range** is now available in the Logs Viewer. For more information, see [Scroll to a time](https://docs.cloud.google.com/logging/docs/view/overview#scroll-to-time).

## December 04, 2017

**Cloud Logging**

v2

Change

**Logging agent recommendation** : VM instances should have at least 1 GB of memory to run the Logging agent.

Feature

**Google Cloud Platform HTTP(S) load balancing logging** now includes logs for **rejected requests** , such as those due to invalid or expired URL signatures, and aligns **httpRequest.requestSize** with metrics from the [Stackdriver Monitoring API](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-loadbalancing). For more information, see [HTTP(S) Load Balancing Logging](https://docs.cloud.google.com/compute/docs/load-balancing/http#logging).

## November 29, 2017

**Cloud Logging**

v2

Feature

**Logs-based metrics** are now Generally Available. For more information, see [Overview of Logs-based Metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics).

Change

**Logging agent installation instructions** : The checksum validation step for the installation script has been removed. You can see the new instructions on the [logging agent installation](https://docs.cloud.google.com/logging/docs/agent/installation) page.

Fixed

**Logs Viewer** update: Fixes a problem related to the daylight saving time transition in the U.K. If you see your logs displaying in the wrong time zone, you can set your default time zone by using the **Jump to date** drop-down menu to select a different time zone. For more information, see [Logs Viewer user interfaces](https://docs.cloud.google.com/logging/docs/view/overview#the_user_interfaces).

## November 08, 2017

**Cloud Monitoring**

v3

Change

The Monitoring agents for Linux and Windows VM instances now report errors for unrecognized metrics. The errors are written to the agent log on your VM instance. If the [Logging agent](https://cloud.google.com/logging/docs/agent/) is also running on the VM instance, then the logs are also available in Stackdriver Logging. The error messages are, "Unsupported collectd plugin/type combination" and "Unsupported collectd ID." Previously, these metrics were dropped silently. See the agent's [Troubleshooting Checklist](https://cloud.google.com/monitoring/agent/troubleshooting#checklist) for more information.

## November 05, 2017

**Cloud Monitoring**

v3

Deprecated

Documentation for the deprecated Cloud Monitoring API v2 has been removed. The API was turned down in August, 2017.

## November 01, 2017

**Cloud Logging**

v2

Change

**Pricing changes** : Billing for logs overages will begin **March 31, 2018**. This date extends the one that was previously communicated to give Stackdriver customers more time to apply the [exclusion filters](https://docs.cloud.google.com/logging/docs/exclusions) feature to control which logs are stored in Logging. Billing for custom and user-defined logs-based metrics is still postponed. For more information, see [Stackdriver Pricing](https://cloud.google.com/stackdriver/pricing).

## October 31, 2017

**Cloud Trace**

v2

Feature

The [Stackdriver Trace API v2](https://cloud.google.com/trace/docs/reference/v2/rest/) is now in Beta release. For a comparison of the v1 and v2 APIs, see [Stackdriver Trace API](https://cloud.google.com/trace/docs/reference).

## October 30, 2017

**Cloud Logging**

v2

Feature

**Exclusion filters** are now Generally Available. For more information, see [Excluding Logs](https://docs.cloud.google.com/logging/docs/exclusions), and the **Resource Usage** page in the Logs Viewer.

## October 24, 2017

**Cloud Logging**

v2

Change

The **`gcloud logging` command group** is now generally available. `gcloud beta logging` will be removed at the end of December 2017. For more information, see [gcloud logging](https://docs.cloud.google.com/sdk/gcloud/reference/logging).

## October 19, 2017

**Cloud Monitoring**

v3

Feature

Beta release: The Monitoring agent can now export collectd and statsd metrics as Stackdriver [custom metrics](https://cloud.google.com/monitoring/custom-metrics/). For more information, see [Custom Metrics from the Agent](https://cloud.google.com/monitoring/agent/custom-metrics-agent) and the agent's [StatsD plugin](https://cloud.google.com/monitoring/agent/plugins/statsd)

## October 17, 2017

**Cloud Monitoring**

v3

Feature

Beta release: The [Uptime Configuration API](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs) and [uptime metrics](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-monitoring) are now available. The API, part of the [Stackdriver Monitoring API](https://cloud.google.com/monitoring/api/ref_v3/rest/), lets you create and edit [uptime checks](https://cloud.google.com/monitoring/uptime-checks/). The status of your checks is recorded in the uptime metrics.

## October 02, 2017

**Cloud Monitoring**

v3

Fixed

Calls to [createTimeSeries](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/create) now fail without writing any data points if the request includes more than one point in the same time series. Formerly, in some cases, one data point would be written in each time series and a status of 500 would be returned by the call.

**Cloud Trace**

v2

Feature

The Trace viewer now shows parent-child relationships between trace spans. You can expand or collapse the parent spans. See [Viewing Trace Details](https://cloud.google.com/trace/docs/viewing-details) for more information.

## September 13, 2017

**Cloud Monitoring**

v3

Change

**Object Stores Resources** : Google Cloud Storage metrics and Amazon S3 metrics are now separated in the Stackdriver UI into their own service dashboards. The "Object Stores" dashboard is replaced by "Cloud Storage" or "S3", depending on which service you are using.

## September 12, 2017

**Cloud Logging**

v2

Feature

**Admin Activity audit logs** retention has been extended to 400 days for both the Stackdriver Basic and Premium service tiers. For more information, see [Audit log retention](https://docs.cloud.google.com/logging/docs/audit#audit_log_retention).

Feature

**Logging agent update** to 1.5.18-1. Allows enabling JSON detection via configuration, fixes a problem with string-valued timestamps, and allows setting the following [`LogEntry`](https://logging/docs/api/reference/rest/v2/LogEntry) fields: `trace`, `sourceLocation`, and `operation`.

## September 08, 2017

**Cloud Monitoring**

v3

Feature

**HTTPS(S) Load Balancer** metrics are available in Beta release to use in Monitoring. For details, see the Google Cloud [`loadbalancing`](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-loadbalancing) metrics and the [`https_lb_rule`](https://cloud.google.com/monitoring/api/resources#tag_https_lb_rule) monitored resource.

Feature

**Cloud Interconnect** custom dashboards and alert monitoring are available in Beta release. For details, see the Google Cloud [`interconnect`](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-interconnect) metrics and the [`interconnect`](https://cloud.google.com/monitoring/api/resources#tag_interconnect) and [`interconnect_attachment`](https://cloud.google.com/monitoring/api/resources#tag_interconnect_attachment) monitored resources.

Feature

**HTTPS(S) Load Balancer** metrics are available in Beta release to use in Monitoring. For details, see the Google Cloud [`loadbalancing`](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-loadbalancing) metrics and the [`https_lb_rule`](https://cloud.google.com/monitoring/api/resources#tag_https_lb_rule) monitored resource.

## August 31, 2017

**Cloud Logging**

v2

Feature

**Logs-based metrics** now support extracting values from log entries to create distribution metrics and to populate user-defined metric labels. This lets you create multiple time series in a single logs-based metric. Also, the latency of logs-based metrics has dropped from approximately 5 minutes to 1 minute, so you can respond more quickly to the metrics. For more information, see [Overview of Logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics).

Feature

**Exclusion filters** let you control which logs are kept in Stackdriver Logging. The **Resource Usage** page in the Logs Viewer breaks down log volume by resource type. For more information, see [Excluding Logs](https://docs.cloud.google.com/logging/docs/exclusions).

Change

**Logging agent** : The Stackdriver Logging agent package has been updated to version 1.5.17. The agent will now send smaller requests, improving log delivery latency and increasing queries per second, which may affect users with high log volumes. Also, the package's bundled Ruby has been updated to version 2.2.7. If you have configuration snippets or extra gems that depend on older Ruby features, you may have to update them.

Change

**Pricing changes** : The free per-project allotment of logs is being increased from 5 GB to 50 GB. Beginning December 1, 2017, we will enforce the new limits and begin charging for logs kept in Stackdriver Logging above the limits. For more information, see [Stackdriver Pricing](https://cloud.google.com/stackdriver/pricing).

## August 23, 2017

**Cloud Logging**

v2

Feature

**Aggregated Exports** : Organizations and folders can now export selected log entries from all of their projects with a single sink created in the organization or folder. For more information, see [Aggregated Exports](https://docs.cloud.google.com/logging/docs/export/aggregated_exports).

Change

**Timestamp handling**. The following changes to log entry timestamps have been made or are planned. 1\. Logging does not modify the user-provided `timestamp` field, except to set it to the current time if it is omitted. A second field, `receivedTimestamp`, is set to the time Logging receives the entry. 2\. The `timestamp` field is used to compute the age of log entries and to enforce the [log retention period](https://docs.cloud.google.com/logging/quotas). Prior to the change, the `receivedTimestamp` field is used for that purpose. 3\. Logging discards log entries whose timestamps are more than 24 hours in the future or are further in the past than the log entry's retention period. Prior to the change, future timestamps and very old timestamps are handled in an unpredictable fashion. For more information, see [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) and [`entries.write`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write).

**Cloud Monitoring**

v3

Feature

**Dashboard filtering** : Custom dashboards and resource list pages now support filtering on groups. Each page that supports filtering now has a filter bar under the header where you specify the group.

## August 01, 2017

**Cloud Trace**

v2

Feature

The Trace Viewer now allows you to view associated log entries in line with trace spans and links to VM logs for Google Cloud Load Balancer spans. See the [Integrating with Cloud Logging](https://cloud.google.com/trace/docs/trace-log-integration).

## July 10, 2017

**Cloud Logging**

v2

Change

**API Migration**. Information about the deprecated v1 API is being removed from general documentation. Note: Obsolete link to migration information removed on December 13, 2017. For updated information, see [APIs & Reference](https://docs.cloud.google.com/logging/docs/apis).

Feature

**IAM support** for Logging now includes custom roles. For more information, see Logging [Access Control](https://docs.cloud.google.com/logging/docs/access-control).

**Cloud Monitoring**

v3

Feature

**Heatmaps for distribution metrics** : Heatmaps are available in dashboard charts. Select a distribution metric from either the **Custom** or **Logging** metric groups and specify **Heatmap**.

Feature

**IAM for Stackdriver Monitoring** is now complete and GA. New IAM roles include **Monitoring Editor** and **Monitoring Admin** , and there is full support for custom roles. For more information, see Monitoring [Access Control](https://cloud.google.com/monitoring/access-control).

Change

**Agent permissions** in VM instances: The agent no longer needs the **Project Editor** IAM role; it only needs the **Monitoring Metric Writer** role (`roles/monitoring.metricWriter`). For more information, see Monitoring [Access Control](https://cloud.google.com/monitoring/access-control).

Feature

**Windows process metrics** now include all processes accessible to the Monitoring agent. See [Agent process metrics](https://cloud.google.com/monitoring/api/metrics_agent#agent-processes).

Change

**Stacked charts** : The order of data streams in stacked charts has been reversed, so that the first stream is on the top and the last stream is on the bottom. This order is consistent with the chart legend and hovercard.

Feature

**Windows Server 2016** is supported by the current Monitoring agent.

## June 05, 2017

**Cloud Logging**

v2

Issue

**Exported audit logs in BigQuery** : The BigQuery schema for exported audit log entries changed on June 5, 2017. The following audit log components now have shortened field names when they are exported to BigQuery: `protoPayload`, `protoPayload.serviceData`, `protoPayload.request`, and `protoPayload.response`. This is a breaking change for queries involving these fields. For more information see [Audit log field changes](https://docs.cloud.google.com/logging/docs/export/using_exported_logs#bigquery-overview).

Feature

**Apps Script** : You can access your Apps Script logs in Logging.

Feature

**Logs Viewer** : You can more easily expand all fields in a log entry.

**Cloud Monitoring**

v3

Feature

**Uptime checks** have a new overview and detail dashboards. See [Uptime Checks](https://cloud.google.com/monitoring/alerts/uptime-checks).

Feature

**Singapore region support** : Stackdriver now supports the Singapore region, `asia-southeast1`.

**Cloud Trace**

v2

Feature

**Advanced trace filters** : The Trace List page and Trace API now allow filtering traces by custom labels, latencies, child spans, and methods in addition to URIs. See [Trace Filters](https://cloud.google.com/trace/docs/trace-filters).

**Error Reporting**

v1beta1

Feature

**IAM roles** : Stackdriver Error Reporting IAM roles are now available. See [Error Reporting IAM roles](https://cloud.google.com/error-reporting/docs/iam#iam_roles).

## May 01, 2017

**Cloud Logging**

v2

Feature

Data access logs are now available and are user-configurable. See [Configuring Data Access Logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).

Feature

**Aggregated exports of logs** : You can now create log sinks in organizations, billing accounts, and folders. Those sinks can export log entries from all included projects. See [Aggregated Exports](https://docs.cloud.google.com/logging/docs/export/aggregated_exports).

Deprecated

**v1 API turndown: writeLogEntries** : As a final step in the v1 API turndown, the v1 `WriteLogEntries` method will be shut down on October 1, 2017. You must migrate any applications that write log entries using the v1 API. You must also upgrade any manually-installed Logging agents in your VM instances. Note: Obsolete link to migration information removed on December 13, 2017. For updated information, see [APIs & Reference](https://cloud.google.com/logging/docs/apis).

Deprecated

**v1 API turndown: sinks and logs-based metrics** : Migrate your remaining v1 export sinks and v1 logs-based metrics. If you do not, Logging will migrate them by mid-July, 2017. Note: Obsolete link to migration information removed on December 13, 2017. For updated information, see [APIs & Reference](https://docs.cloud.google.com/logging/docs/apis).

**Cloud Monitoring**

v3

Feature

New metric and resource types: There are new Cloud Platform metric and resource types, including those for Cloud Bigtable, Cloud Dataflow, Cloud DNS, Cloud Internet of Things, Cloud Pub/Sub, Cloud Spanner, and Stackdriver Logging. Microsoft Windows system and application metrics (`iis`,`mssql`, `pagefile`) are available as Agent metrics and can be used for charting and alerting.

**Error Reporting**

v1beta1

Feature

**Error filters** : You can now filter errors by custom text in addition to filtering by time, service, and version.

## April 02, 2017

**Cloud Monitoring**

v3

Issue

**v2beta2 API turndown** : The deprecated v2beta1 and v2beta2 APIs will be shut down during August 2017.

## April 01, 2017

**Cloud Logging**

v2

Feature

**Resource types** : Several new resource types are added, including types for Cloud Bigtable, Cloud Dataflow, and Cloud Container Engine.

## March 31, 2017

**Cloud Logging**

v2

Change

**V1 API turndown** : The date of the v1 API turndown has changed. See the release note for May 2017.

Change

**Logging agent for Windows** : If you install the Logging agent on VM instances running Microsoft Windows, be aware that there are restrictions on the folders used for the installer and the installed agent. For details, [Installing on Linux and Windows](https://docs.cloud.google.com/logging/docs/agent/installation#joint-install).

**Cloud Monitoring**

v3

Feature

**Time shifting (Beta)** : You can now compare your current metric data with data from 1 day, 1 week, or 4 weeks ago. See **Compare to past** in the **Advanced options** for line chart creation.

Feature

**Faster chart legends** : Charts involving custom and logs-based metrics now have faster legends that include instance names with the metric name where available. You can quickly identify instances and sort the metrics by name.

Feature

**Faster user interface** : Initial page load times have been reduced across the user interface.

Feature

**Cloud ML** : [Cloud Machine Learning Engine metrics](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-ml) are available for dashboards and alerting.

Feature

**Cloud Dataflow** : [Cloud Dataflow](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-dataflow) is now integrated with Monitoring. For more details, see the [Big Data and Machine Learning Blog](https://cloud.google.com/blog/products/management-tools).

Feature

**Cloud Spanner** : [Cloud Spanner metrics](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-spanner) are available for dashboards and alerting.

Change

**Monitoring agent** : Although the statsd plugin is distributed with the Monitoring agent, there are not yet any instructions for using the plugin with Monitoring.

## February 06, 2017

**Cloud Logging**

v2

Feature

**App Engine Flexible Environment** : For App Engine Flexible Environment, the Logs Viewer can now display application log entries ("log lines") inside the log entry for the associated service request. This is similar to the functionality in the App Engine Standard Environment.

Feature

**Resuming log streaming** : The Logs Viewer now automatically resumes streaming logs when its browser window or tab is selected. You no longer have to restart streaming when returning to the page.

Feature

**Exporting logs from organizations, folders, and billing accounts** : The [`gcloud logging`](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging) command-line tool now supports creating log sinks to export audit logs from organizations, folders, and billing accounts. This feature also supported in the API.

Feature

**Viewing multiple logs** : Previously in the Logs Viewer, you could view a single log or "all logs" from a single resource type. Now you can select any number of logs within a resource type to view, using the log name dropdown menu.

For example, when viewing App Engine applications, the default is now to display log entries from any of these logs: `ngnix.request`, `stdout`, `request log`, and `stderr`.

Change

**Remove daily API quotas** : The Logging API no longer includes daily API quotas. The API still enforces short-term (per 100s) quotas on API calls, as displayed in the Stackdriver Logging API dashboard.

Change

**Deleting logs-based metrics in alerting policies** : Attempting to delete a [logs-based metric](https://docs.cloud.google.com/logging/docs/view/logs_based_metrics) that is used in one or more Stackdriver Monitoring alerting policies now fails with the status `FAILED_PRECONDITION`. You must remove the metric from the alerting policies or delete the alerting policies prior to deleting the logs-based metric.

Issue

**Logs retention and source restriction** : With the implementation of the Basic and Premium service tiers in December 2016, Stackdriver Logging began enforcing retention and log source restrictions for projects that are in the Stackdriver Basic tier or are not associated with a Stackdriver account. In the Basic tier, log entries are visible for 7 days after they are received, and logs from non-Google Cloud sources, including Amazon Web Services, are rejected.

**Cloud Monitoring**

v3

Fixed

**Process owner** : When sending process metrics, the Stackdriver Monitoring agent now returns a stringified UID if the process owner name is not set. Previously, the agent would not send process owner information, which was then treated by the Monitoring API as malformed input and discarded. Available in stackdriver-agent/5.5.2-359. See [Determining the agent version](https://cloud.google.com/monitoring/agent/install-agent#agent-version).

Fixed

**Lost input from the Monitoring agent** : Malformed data from the Monitoring agent could cause Stackdriver Monitoring to lose well-formed input bundled in the same request. Now, only the malformed input is lost. You do not have to update your agent for this fix.

Feature

**Selectable uptime check regions** : Stackdriver Monitoring now lets you select the geographic region(s) that check your service.

**Cloud Trace**

v2

Feature

**Zipkin tracer compatibility** : Stackdriver Trace is now compatible with Zipkin tracers. For more information, see this [blog post](https://cloudplatform.googleblog.com/2016/12/Stackdriver-Trace-Zipkin-distributed-tracing-and-performance-analysis-for-everyone.html).

Feature

**Scatter plots** : We've added a new scatter-plot selection tool to the Stackdriver Trace UI. This lets you more quickly identify, view, and compare interesting traces.

## January 18, 2017

**Cloud Monitoring**

v3

Feature

**New AWS regions** : Monitoring now supports the AWS Canada (**ca-central-1**) and London (**eu-west-2**) regions.

## December 12, 2016

**Cloud Logging**

v2

Change

**Logs Viewer v2** : The Logs Viewer has been migrated to the Stackdriver Logging API v2. For the full documentation, [Viewing Logs (v2)](https://docs.cloud.google.com/logging/docs/view/overview). Note: Obsolete link to migration information removed on December 13, 2017. For updated information, see [APIs & Reference](https://docs.cloud.google.com/logging/docs/apis).

Feature

**New LogEntry fields** : Fields `trace` and `sourceLocation` were added to [`LogEntry`](https://docs.cloud.google.com/logging/docs/api/reference/rest/v2/LogEntry).

Feature

**List logs** : the Stackdriver Logging API now has "list logs" methods: [`organizations.logs.list`](https://docs.cloud.google.com/logging/docs/api/reference/rest/v2/organizations.logs/list) and [`projects.logs.list`](https://docs.cloud.google.com/logging/docs/api/reference/rest/v2/projects.logs/list).

**Cloud Monitoring**

v3

Feature

**Account IDs in URLs** : Monitoring has added the Stackdriver account ID to its URLs. You can now open multiple tabs for different accounts and more easily share links with coworkers. URLs without the account ID use the most recently accessed Stackdriver account.

## December 08, 2016

**Cloud Monitoring**

v3

Feature

**Incident pages** (Beta): See **Alerting > Incidents**. Each open incident now has a detail page that collects a graph of the incident, links to affected resources, and the comments made on the incident.

Feature

**Metrics Explorer** (Beta): See **Resources > Metric Explorer**. Select a monitored resource type and metric. You can aggregate data across your instances.

## November 21, 2016

**Cloud Logging**

v2

Feature

**Sinks** : The Stackdriver Logging API now allows both projects and organizations to own sinks. In addition, sinks can now export log entries to destinations in other projects. See [`LogSink`](https://docs.cloud.google.com/logging/docs/api/reference/rest/v2/organizations.sinks).

Feature

**Organizations** : The Stackdriver Logging API now allows both projects and organizations to own logs. A log belonging to an organization is named `"organizations/[ORGANIZATION_ID]/logs/[LOG_ID]"`. See [`organizations.logs.delete`](https://docs.cloud.google.com/logging/docs/api/reference/rest/v2/organizations.logs/delete).

**Cloud Monitoring**

v3

Change

**Time series** : The recommended maximum rate of writing data points to a single time series is changed from 1/sec to 1/min. See [Writing metric data](https://cloud.google.com/monitoring/custom-metrics/creating-metrics#writing-ts).

Feature

**Chart options** : You can now display data as stacked bar charts and stacked area charts, using the **Stacked** option under **Chart Types**. Stacked bar charts are automatically aligned to hour boundaries. Stacked area charts work best with metrics received at 1-minute intervals.

Feature

**New AWS region** : Monitoring now supports the AWS region **us-east-2**.

Feature

**Chart snapshots** : You can now download images of charts in PNG format. Choose **Download Image** from the **More** menu. The chart legend is not presently rendered.

Feature

**Group support for metrics** : When charting custom and logs-based metrics, a new **Group** filter appears under **Advanced Options**. The effect of the filter is not shown until after you save the chart.

## October 20, 2016

**Cloud Logging**

v2

Feature

Logging is generally available to Google Cloud Platform customers. Individual features that are in Alpha or Beta release are marked as such in the documentation.

Change

**Pricing** : Stackdriver is now available in Basic and Premium service tiers. All existing and new Stackdriver accounts are entered into a 30-day free trial of the Premium Tier. At the end of the trial period, you could lose some functionality you had during the Beta release unless you upgrade to the Premium Tier. For more details, see [Pricing](https://cloud.google.com/stackdriver/pricing).

Feature

**API v2** : The Stackdriver Logging API v2 is generally available, providing a simplified log format. During a transition period, you can use the same API at either of these two endpoints: `https://logging.googleapis.com/v2beta1/...` or `https://logging.googleapis.com/v2/...`.

Deprecated

**API v1** : The Stackdriver Logging API v1 (v1beta3) is deprecated. Users of this API should migrate to the v2 API. The v1 API will be removed from service on March 30, 2017. Note: Obsolete link to migration information removed on December 13, 2017. For updated information, see [APIs & Reference](https://docs.cloud.google.com/logging/docs/apis).

**Cloud Monitoring**

v3

Feature

**GA** : Monitoring is generally available to Google Cloud Platform customers. Individual features that are in Alpha or Beta release are marked as such in the documentation.

Change

**Pricing** : Stackdriver is now available in Basic and Premium service tiers. All existing and new Stackdriver accounts are entered into a 30-day free trial of the Premium Tier. At the end of the trial period, you could lose some functionality you had during the Beta release unless you upgrade to the Premium Tier. For more details, see [Pricing](https://cloud.google.com/stackdriver/pricing).

Feature

**API v3** : The Stackdriver Monitoring API v3 is now generally available.

Feature

**Monitoring agent** : A new version of the Stackdriver Monitoring Agent, v5.5.2-349, is available. Its improvements include an update to collectd 5.5.2, support MongoDB 3.0, [agent health metrics](https://cloud.google.com/monitoring/api/metrics_agent#agent-agent), and bundled `statsd`, tail, and network plugins. For more information, see [Installing the Monitoring Agent](https://cloud.google.com/monitoring/agent/install-agent).

Feature

**Creating alerts** : We have introduced a new, more streamlined user interface for creating and editing alerting policies.

Feature

**Charting** : You can use log scales in your charts, and you can zoom both the x- and y-axes by clicking-and-dragging.

Feature

**New metrics** : New metrics are now available from Cloud Router, BigQuery, and TaskQueues (pull metrics). See the [Metrics List](https://cloud.google.com/monitoring/api/metrics).

Feature

**Custom metrics** : Custom metric descriptors are created as needed when you write time series data. See [Auto-creation of custom metrics](https://cloud.google.com/monitoring/custom-metrics/creating-metrics#auto-creation).

**Cloud Trace**

v2

Feature

**Analysis Reports** : Compare your application's latency profile across time and versions.

**Error Reporting**

v1beta1

Feature

**Cloud Functions** : Cloud Functions automatically reports unhandled JavaScript exceptions to Stackdriver Error Reporting.

## September 11, 2016

**Cloud Monitoring**

v3

Change

The Google Monitoring API (v3) is now known as the Stackdriver Monitoring API (v3). This change does not affect any code.

Deprecated

The Monitoring v2 API is now deprecated. It is still named the Google Cloud Monitoring API in **APIs & services**.

## September 09, 2016

**Cloud Logging**

v2

Change

The Google Cloud Logging API is now known as the Stackdriver Logging API. This change does not affect any code.

## September 08, 2016

**Error Reporting**

v1beta1

Feature

**C++** and **Ruby** are now supported.

Fixed

**PHP** stack traces are better supported.

## August 16, 2016

**Error Reporting**

v1beta1

Feature

[**Cloud Console mobile app**](https://cloud.google.com/console-app) now supports Error Reporting.

## July 26, 2016

**Cloud Monitoring**

v3

Change

Some documentation pages have moved in the table of contents, but their URLs are the same or have redirections. All agent-related pages are now part of the How-To section, [Using the Monitoring Agent](https://cloud.google.com//monitoring/agent/). The former "Using Metrics" page has been reorganized into several pages under [Using Custom Metrics](https://cloud.google.com/monitoring/agent/).

## July 18, 2016

**Error Reporting**

v1beta1

Feature

**App Engine** : Error Reporting is now generally available for Google App Engine standard environment.

## July 12, 2016

**Error Reporting**

v1beta1

Feature

**API** : The Stackdriver Error Reporting API has a new endpoint to report errors: [`projects.events.report`](https://cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report).

## June 27, 2016

**Error Reporting**

v1beta1

Feature

The Google Cloud console home page now has an Error Reporting card.

## June 15, 2016

**Cloud Logging**

v2

Change

A change to the v2beta1 API might affect some existing code. In the following methods, the parameter `projectName` has been changed to `parent`: `sinks.create`, `sinks.list`, `metrics.list`, `metrics.create`.

Change

The Google Logging API v2beta1 reference documentation now includes code snippets for each method. For example, see [`entries.list`](https://docs.cloud.google.com/logging/docs/api/ref_v2beta1/rest/v2beta1/entries/list).

## June 09, 2016

**Cloud Monitoring**

v3

Change

The documentation for metrics and custom metrics has been reorganized and extended for the Monitoring API v3. See [Metrics](https://cloud.google.com//monitoring/api/v3/metrics), [Using Metrics](https://cloud.google.com//monitoring/api/v3/using-metrics), and [Metrics List](https://cloud.google.com//monitoring/api/metrics).

Change

The [Stackdriver Monitoring API v3 reference documentation](https://cloud.google.com/monitoring/api/ref_v3/rest/) now includes code samples for each method. For example, see [metricDescriptors.list](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/list). [Sample Code](https://cloud.google.com/monitoring/docs/tutorials) will continue to be available on GitHub.

## June 06, 2016

**Cloud Monitoring**

v3

Change

[Metrics List](https://cloud.google.com//monitoring/api/metrics) is now a comprehensive list of all metrics available in Monitoring, including metrics gathered by the monitoring agent and metrics from Amazon Web Services.

## April 27, 2016

**Cloud Logging**

v2

Change

The user documentation has been reorganized. The [documentation landing page](https://docs.cloud.google.com/logging/docs) and the left-side navigation entries have changed. Existing URLs to individual documentation pages will be redirected if necessary.

**Cloud Monitoring**

v3

Change

The documentation has been reorganized. The [documentation landing page](https://cloud.google.com/monitoring/docs/) and the left-side navigation entries have changed. Existing URLs to individual documentation pages will be redirected if necessary.

Change

The [Quickstart](https://cloud.google.com//monitoring/quickstart-lamp) has been simplified. It now includes setting up a virtual machine instance and installing both the monitoring and logging agents.

## March 23, 2016

**Cloud Logging**

v2

Change

Google Cloud Logging is now **Stackdriver Logging** , part of the [Google Stackdriver](https://cloud.google.com/products/operations) suite of products. You can now manage logs from Amazon EC2 virtual machine instances alongside your Google Cloud projects. See [Logging agent](https://docs.cloud.google.com/logging/docs/agent) for more details.

**Cloud Monitoring**

v3

Change

Google Cloud Monitoring is now **Stackdriver Monitoring** , part of the [Google Stackdriver](https://cloud.google.com/products/operations) suite of products.

Feature

You can now monitor Amazon Web Services (AWS) accounts alongside your Google Cloud projects. Read about Stackdriver Accounts and install the new [monitoring agent](https://cloud.google.com/monitoring/agent/).

Issue

When installing the monitoring agent on an Amazon EC2 VM instance running Microsoft Windows, ignore the following error message if you get it only once after the service is started: "StackdriverAgent is running on an AWS instance but project ID is not set."

## March 17, 2016

**Cloud Monitoring**

v3

Feature

The [Monitoring API v3](https://cloud.google.com/monitoring/api/ref_v3/rest/) is now available. Users are encouraged to begin upgrading from the Cloud Monitoring API v2. See [What's new](https://cloud.google.com/monitoring/api/v3/) in the v3 API and look at the new [code samples](https://cloud.google.com/monitoring/docs/tutorials) on GitHub.

**Error Reporting**

v1beta1

Feature

**Beta release** of Stackdriver Error Reporting.

## February 18, 2016

**Cloud Logging**

v2

Change

The [logging agent authorization](https://docs.cloud.google.com/logging/docs/agent/authorization) instructions now recommend storing private-key credentials as `/etc/google/auth/application_default_credentials.json`. You do not have to move your existing file at `/root/.config/gcloud/application_default_credentials.json`.

## January 29, 2016

**Cloud Logging**

v2

Change

The [Logs Viewer](https://docs.cloud.google.com/logging/docs/view/logs_viewer) now lets you [view the structure](https://docs.cloud.google.com/logging/docs/view/logs_viewer#expanding) of log entries. You can also [show or hide](https://docs.cloud.google.com/logging/docs/view/logs_viewer#similar) log entries with similar field values.

## December 10, 2015

**Cloud Logging**

v2

Change

Version 2 of the [Cloud Logging API](https://docs.cloud.google.com/logging/docs/apis) is now available. Among other changes, the V2 API lets you retrieve log entries from Logging using the [`entries.list`](https://docs.cloud.google.com/logging/docs/api/ref_v2beta1/rest/v2beta1/entries/list) method.

## October 22, 2015

**Cloud Logging**

v2

Change

The [Logs Viewer](https://docs.cloud.google.com/logging/docs/view/logs_viewer) now has cascading menus for selecting log entries from Google App Engine and Google Compute Engine.

## October 13, 2015

**Cloud Logging**

v2

Change

See [logs-based-metrics](https://docs.cloud.google.com/logging/docs/view/logs_based_metrics) to learn how to create Google Cloud Monitoring metrics using logs filters.

Change

The list of [log types](https://docs.cloud.google.com/logging/docs/view/logs_index) has been expanded.

## September 29, 2015

**Cloud Monitoring**

v3

Feature

Charts now have a [View Logs](https://cloud.google.com/monitoring/quickstart-lamp#charts-to-logs) option in their settings menu.

## September 15, 2015

**Cloud Logging**

v2

Change

Added [Java examples](https://docs.cloud.google.com/logging/docs/api/tasks) of Logging API usage. Simplified the [authorization code](https://docs.cloud.google.com/logging/docs/api/tasks/authorization) for Java and Python, and the same code now runs on App Engine, Compute Engine, and your development workstation.

## September 09, 2015

**Cloud Logging**

v2

Change

The [command-line interface](https://docs.cloud.google.com/logging/docs/api/gcloud-logging) in the Google Cloud SDK is now named `gcloud beta logging`.

## August 12, 2015

**Cloud Logging**

v2

Feature

The [Cloud Logging API](https://docs.cloud.google.com/logging/docs/reference/api-overview) and [command-line interface](https://docs.cloud.google.com/logging/docs/api/gcloud-logging) now support project sinks. A project sink can export log entries from any combination of logs, based on [advanced logs filters](https://docs.cloud.google.com/logging/docs/view/advanced-queries).

## August 03, 2015

**Cloud Logging**

v2

Feature

Cloud Logging now has advanced logs filters that let you specify arbitrary Boolean expressions that match on log entries. See [Using advanced logs filters](https://docs.cloud.google.com/logging/docs/view/advanced-queries) in the Logs Viewer, and the [Advanced Logs Filters guide](https://docs.cloud.google.com/logging/docs/view/advanced-queries).

## June 15, 2015

**Cloud Logging**

v2

Change

The logging agent has new, simpler [installation instructions](https://docs.cloud.google.com/logging/docs/agent/installation) You no longer have to edit the agent's configuration file to install [private-key authorization](https://docs.cloud.google.com/logging/docs/agent/authorization).

Change

The Logging documentation has been reorganized. The [table of contents](https://docs.cloud.google.com/logging/docs) now groups all information about the logging agent, viewing logs, and exporting logs in individual sections.

## May 21, 2015

**Cloud Logging**

v2

Change

A new Google Cloud console UI panel for the [logs export feature](https://docs.cloud.google.com/logging/docs/export/configure_export) was released. The UI lets you export a subset of your logs from a logs service. For example, you could export `syslog` from Google Compute Engine without exporting `activity_log`.

## April 28, 2015

**Cloud Logging**

v2

Feature

You can now stream logs from Cloud Logging to [Google Cloud Pub/Sub](https://docs.cloud.google.com/pubsub/docs) and from there to your own endpoints. This involves changes to [logs export](https://docs.cloud.google.com/logging/docs/export/using_exported_logs#pubsub-overview). For example, use Cloud Pub/Sub to route logs through [Google Cloud Dataflow](https://docs.cloud.google.com/dataflow/docs) and into tools like [Google BigQuery](https://docs.cloud.google.com/bigquery/docs).

## March 19, 2015

**Cloud Logging**

v2

Feature

The `google-fluentd` logging agent supports [two dozen third-party logs](https://docs.cloud.google.com/logging/docs/view/logs_index).

Feature

Cloud Logging is now available in Beta release, allowing you to configure, visualize, analyze and export your Google Compute Engine and Google App Engine logs.

Feature

The [Google Cloud Logging API](https://docs.cloud.google.com/logging/docs/api) is now available in Beta release. The API lets you write logs, create logs, and control the export of logs. Client libraries make it easy to use the API in your favorite programming language.

Feature

The `google-fluentd` logging agent runs with [additional operating systems](https://docs.cloud.google.com/logging/docs/agent/installation), including Debian, Ubuntu, Red Hat, and CentOS. A single script installs the agent on any supported operating system.

Feature

The [`glcoud logging`](https://docs.cloud.google.com/logging/docs/api/gcloud-logging) command-line interface, which uses the API, is now available in Beta release. The commands provide an easy way to perform administrative tasks such configuring logs export.

Change

The [Logs Viewer refresh](https://docs.cloud.google.com/logging/docs/view/logs_viewer) brings more search options and quicker access to [logs export configurations](https://docs.cloud.google.com/logging/docs/export/configure_export). Regex-search has been removed as part of this refresh.

Change

The Cloud Logging documentation has been improved with more set-up options, [simpler procedures](https://docs.cloud.google.com/logging/docs/agent/installation) and [more examples](https://docs.cloud.google.com/logging/docs/export/using_exported_logs).

## January 15, 2015

**Cloud Logging**

v2

Feature

Beta release: App Engine logs can be exported to Cloud Storage and BigQuery.

## January 07, 2015

**Cloud Monitoring**

v3

Feature

First beta release of [Google Cloud Monitoring powered by Stackdriver](https://cloud.google.com/monitoring).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
