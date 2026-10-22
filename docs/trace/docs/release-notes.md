---
url: https://docs.cloud.google.com/trace/docs/release-notes/
title: Trace release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:29.112163+00:00
---

# Trace release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Resources ](https://docs.cloud.google.com/trace/docs/quotas)



Send feedback 

#  Trace release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Trace. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

For a combined list of all release notes for the products in Google Cloud Observability, see [Consolidated release notes](https://docs.cloud.google.com/stackdriver/docs/release-notes).

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/stackdriver-release-notes.xml) directly. 

## September 23, 2026

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



## September 08, 2026

Feature

The Observability API supports VPC Service Controls. This integration is [generally available](https://cloud.google.com/products#product-launch-stages).

For more information, see the following:

  * [Use VPC Service Controls with Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs/observability/use-vpc-service-controls)
  * [Observability API overview](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview)
  * [Supported products: Observability API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_observability_api)



## August 31, 2026

Breaking

Starting August 31, 2026, you can no longer create or edit [trace sinks](https://docs.cloud.google.com/trace/docs/trace-export-overview). Trace sinks were deprecated on February 18, 2026. For more information, see [Export trace spans with sinks deprecation](https://docs.cloud.google.com/stackdriver/docs/deprecations/export-spans-with-sinks).

For information about how to analyze your trace data using SQL, see the following documents:

  * [Query and analyze traces using Observability Analytics](https://docs.cloud.google.com/trace/docs/analytics)
  * [Query a linked BigQuery dataset](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset)



## August 27, 2026

Feature

The following remote MCP server automatically generates a trace span for `tools/call` operations.

  * Datastream



These spans can help you understand the behavior of your agentic applications. For more information, see [Investigate MCP calls using Trace](https://docs.cloud.google.com/trace/docs/trace-remote-mcp-server-calls).

## August 24, 2026

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

Feature

The following limits associated with the Cloud Trace API, `cloudtrace.googleapis.com`, have increased:

  * Maximum attributes per span: 1,024
  * Maximum attribute value size: 65,532 bytes
  * Maximum attribute key size: 512 bytes
  * Maximum span name length: 1,024 bytes
  * Maximum events per span: 256



The new limits are consistent with those supported by the Telemetry API, which implements the [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp).

For more information, see [Cloud Trace API quotas and limits](https://docs.cloud.google.com/trace/docs/quotas#trace-api-quotas-and-limits).

## August 12, 2026

Feature

The following remote MCP servers automatically generate a trace span for `tools/call` operations. These spans can help you understand the behavior of your agentic applications. For more information, see [Investigate MCP calls using Trace](https://docs.cloud.google.com/stackdriver/docs/instrumentation/trace-remote-mcp-server-calls).

  * Cloud Billing
  * Personalized Service Health



Feature

Google Cloud Observability automatically generates trace exemplars for charts on custom dashboards that display the result of a SQL query when the query runs against your trace data and satisfies some constraints. The exemplars link the SQL query result to specific traces. This feature is in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

For more information, see [Generate and display trace exemplars](https://docs.cloud.google.com/trace/docs/analytics-chart#show-trace-exemplars).

## June 29, 2026

Feature

Google Cloud Observability has expanded the supported locations for observability buckets, which store your trace data, to include the following:

  * europe-west9



For a list of supported locations, see [Locations for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).

## June 18, 2026

Feature

You can collect, view, and analyze multimodal prompts and responses from your agentic applications that use the LangGraph or Agent Development Kit (ADK) frameworks. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

  * [Instrument generative AI applications](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-overview)
  * [Collect and view multimodal prompts and responses](https://docs.cloud.google.com/trace/docs/collect-view-multimodal-prompts-responses)



## June 08, 2026

Feature

The Trace API supports regional endpoints. For a list of supported endpoints, see the REST API reference pages:

  * [v1 REST reference](https://docs.cloud.google.com/trace/docs/reference/v1/rest?rep_location=global)
  * [v2 REST reference](https://docs.cloud.google.com/trace/docs/reference/v2/rest?rep_location=global)



## June 05, 2026

Feature

Custom dashboards can display trace data. You can view individual spans or aggregated data. This feature is [public preview](https://docs.cloud.google.com/products#product-launch-stages). For more information, see [Display traces on a custom dashboard](https://docs.cloud.google.com/trace/docs/display-traces-on-dashboards).

## June 04, 2026

Feature

To view the instrumentation scope or the schema associated with a span, open the **Details** view for the span and select the **Metadata & Links** tab. For more information, see [View attributes, log entries, and events](https://docs.cloud.google.com/trace/docs/finding-traces#attributes-events).

## June 02, 2026

Feature

The create-observability bucket flow enforces organization policies with constraints on resource locations. This flow also enforces policies that require customer-managed encryption keys (CMEKs) and that restrict the projects that store those keys. Your trace data is stored in an observability bucket.

For more information, see the following:

  * [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets)
  * [Support for CMEKs](https://docs.cloud.google.com/stackdriver/docs/observability/cmek)



## June 01, 2026

Feature

The details page for a span can display the call hierarchy of a trace using a directed acyclic graph (DAG). One way to view a span's details is to open the **Trace Explorer** page and select the span. The DAG view is also available for some integrations. For example, if you view an Application Monitoring dashboard and explore the trace data it displays, the flyout supports the DAG option.

For more information, see the following:

  * [Trace Explorer: Explore a trace](https://docs.cloud.google.com/trace/docs/finding-traces#explore)
  * [Application Monitoring: Explore a trace](https://docs.cloud.google.com/monitoring/docs/application-monitoring#explore-trace)



## May 28, 2026

Announcement

You can view the available regional endpoints for the Observability API and for the Telemetry API on their REST reference pages. For more information, see [API overview](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview).

## May 26, 2026

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



## May 11, 2026

Feature

Google Cloud Observability has expanded the supported locations for observability buckets, which store your trace data, to include the following:

  * asia-northeast1
  * asia-southeast1
  * me-west2
  * southamerica-east1
  * us-west4



For a list of supported locations, see [Locations for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).

## May 06, 2026

Feature

The following remote MCP servers automatically generate a trace span for `tools/call` operations. These spans can help you understand the behavior of your agentic applications. For more information, see [Investigate MCP calls using Trace](https://docs.cloud.google.com/stackdriver/docs/instrumentation/trace-remote-mcp-server-calls).

  * Agent Search
  * AlloyDB for PostgreSQL
  * Google Security Operations



## May 01, 2026

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

Feature

Cloud Trace is a service covered by the [Cloud Observability (Monitoring, Logging, Trace) Service Level Agreement (SLA)](https://cloud.google.com/operations/sla).

## April 15, 2026

Feature

Your trace data can be encrypted with a customer-managed encryption key (CMEK). To enable CMEK, set a default storage location and for that location, set a default Cloud Key Management Service key.

You can set these defaults for an organization, a folder, or a project. When set for an organization or folder, the settings apply to that resource and to its descendants. For more information, see [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets).

Feature

When you configure a default storage location, you control the location of your new observability buckets. These buckets store your trace data.

You can set a default storage location for an organization, a folder, or a project. When set for an organization or folder, the setting applies to that resource and to its descendants. For more information, see [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets).

## April 10, 2026

Feature

Use Cloud Trace to troubleshoot your MCP server usage, tool failures, and latency causes. For more information, see [Investigate MCP calls using Trace](https://docs.cloud.google.com/trace/docs/trace-remote-mcp-server-calls).

## April 08, 2026

Feature

Google Cloud CLI lets you configure trace scopes, manage observability buckets, and set default observability settings. These features are in Public Preview. For more information, see the following documents:

  * Configure trace scopes by using the Google Cloud console, the Google Cloud CLI, Terraform, or the Observability API. For more information, see [Create and manage trace scopes](https://docs.cloud.google.com/trace/docs/trace-scope/create-and-manage).

  * Manage trace storage by using the Google Cloud CLI or the Observability API. For more information, see [Manage trace storage](https://docs.cloud.google.com/trace/docs/storage-manage).

  * Configure default settings by using the Google Cloud CLI, Terraform, or the Observability API. For more information, see [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets).




## March 30, 2026

Change

For any new project that is created on or after March 30, 2026, if the project enables the Cloud Trace API, then Google Cloud Observability also enables the [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview).

Feature

You can use the [Cloud Trace API MCP server](https://docs.cloud.google.com/trace/docs/reference/mcp/mcp) to let agents and AI applications interact with your trace data. This feature is in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

## March 24, 2026

Feature

The Telemetry API supports trace ingestion of up to 2.4GB per minute for the following regions:

  * asia-east1, asia-northeast1, asia-southeast1, and asia-south1
  * europe-west1, europe-west2, europe-west3, and europe-west4
  * us-central1, us-east4, and us-west1.



For all other regions, the Telemetry API supports trace ingestion of up to 300 MB per minute.

These regional byte-based quotas replace a global quota which limited the number of requests per minute. To learn more, see [Telemetry API limits and quotas](https://docs.cloud.google.com/trace/docs/quotas#telemetry-api-limits).

## March 19, 2026

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

## March 09, 2026

Change

You can send trace data to your Google Cloud project by using the Cloud Trace API or the Telemetry API. These two APIs are enabled individually.

If you send trace data to the Telemetry API endpoint, then Google Cloud Observability requires that the Cloud Trace API be enabled on your Google Cloud project before it stores the trace data. If the Cloud Trace API is disabled, then Google Cloud Observability discards the trace data.

To learn more, see [APIs that ingest trace data](https://docs.cloud.google.com/trace/docs/overview#supported-apis).

## February 26, 2026

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

Deprecated

Starting February 18, 2026, [trace sinks](https://docs.cloud.google.com/trace/docs/trace-export-overview) are deprecated. For more information, see [Export trace spans with sinks deprecation](https://docs.cloud.google.com/stackdriver/docs/deprecations/export-spans-with-sinks).

You can use the Observability Analytics page, which provides a SQL query interface, to query both your trace and log data. To learn more, see the following documents:

  * To migrate to using Observability Analytics page from a sink-based export of trace data to BigQuery, see [Migrate to Observability Analytics](https://docs.cloud.google.com/trace/docs/analytics-migrate).

  * To query your trace data by using the Observability Analytics page, see [Query and analyze traces](https://docs.cloud.google.com/trace/docs/analytics).

  * To query your trace data by using BigQuery services, see [Query a linked BigQuery dataset](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset).




## February 02, 2026

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



## January 26, 2026

Change

To support correlation between log and trace data, the following changes have been made:

  * The required format for the `LogEntry.trace` field has been relaxed. The preferred format for this field is the trace ID. However, you can continue to provide the full resource name. For more information, see [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).

  * If you open the **Trace Details flyout** page by using options provided in a log entry, then the resources listed in the default trace scope are searched for the trace data.

  * If you open the **Logs Explorer** page by using options on span data, then the resources listed in the default log scope are searched for log data.




To learn more about default scopes, see [Configure observability scopes for multi-project queries](https://docs.cloud.google.com/stackdriver/docs/observability/scopes).

## January 05, 2026

Feature

You can now collect, view, and analyze multimodal prompts and responses from your agentic applications that use the LangGraph or Agent Development Kit (ADK) frameworks. This feature is in [Public Preview](https://cloud.google.com/products#product-launch-stages).

To learn more, see the following documents:

  * [Collect and view multimodal prompts and responses](https://docs.cloud.google.com/trace/docs/collect-view-multimodal-prompts-responses)
  * [Instrument generative AI applications](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-overview)



## December 15, 2025

Feature

The Trace Explorer has been updated to include annotations that let you identify App Hub-registered services and workloads. The link provided with a service or workload lets you open the corresponding Application Monitoring dashboard. To learn more, see the following documents:

  * [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces) describes how to use the Trace Explorer page to filter and explore your trace data.
  * [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring).
  * [View application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring) describes how to view the telemetry for a registered application.



## November 06, 2025

Feature

You can now collect, view, and analyze prompts and responses from your agentic applications when they are built with the Agent Development Kit (ADK). This feature is in Public Preview.

[Collect and view multimodal prompts and responses](https://docs.cloud.google.com/trace/docs/collect-view-multimodal-prompts-responses) describes how to do the following:

  * Configure your project and ADK to collect multimodal data.
  * View a conversation and the multimodal data by using the Trace Explorer.
  * Find log entries that contain references to multimodal data.
  * Query your prompts and responses by using BigQuery.
  * Evaluate your prompts and responses by using the Vertex AI SDK for Python.



## August 27, 2025

Feature

You can now create and manage the trace scope programmatically. This feature is in Public Preview. For more information, see the following documents:

  * [Create and manage trace scopes](https://docs.cloud.google.com/trace/docs/trace-scope/create-and-manage)
  * [Trace scopes API overview](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.traceScopes)



## July 17, 2025

Feature

Application-specific resource attributes are attached to your trace data when your App Hub applications use supported Google Cloud resources, or when you instrument an application with OpenTelemetry and use the Google Cloud Telemetry endpoint. You can use the Trace Explorer to filter by your application, your service, or your workload. To learn more, see the following:

  * [Find and explore traces](https://cloud.google.com/trace/docs/finding-traces)
  * [Application Monitoring overview](https://cloud.google.com/monitoring/docs/about-application-monitoring)
  * [View application telemetry](https://cloud.google.com/monitoring/docs/application-monitoring)
  * [Telemetry (OTLP) API overview](https://cloud.google.com/stackdriver/docs/reference/telemetry/overview)



## June 13, 2025

Change

The **Analysis reports** page has been removed. To analyze your trace data, use the **Trace explorer** page. You can use filters and the time-range selector to view and analyze historical data.

## May 27, 2025

Feature

Learn how to instrument your generative AI applications by using OpenTelemetry and the LangGraph framework to collect information about the actions taken by your AI agent. You can view generative AI events by using the **Trace Explorer** :

  * [Instrument generative AI applications](https://cloud.google.com/stackdriver/docs/instrumentation/ai-agent-overview)
  * [Instrument a LangGraph ReAct Agent with OpenTelemetry](https://cloud.google.com/stackdriver/docs/instrumentation/ai-agent-langgraph)
  * [View generative AI events](https://cloud.google.com/trace/docs/finding-traces#view_generative_ai_events)



## March 25, 2025

Feature

To send trace data to your Google Cloud project, we recommend that you use the new Telemetry API, which implements the OpenTelemetry OTLP API and provides compatibility and support for the open source ecosystem. The limits for the Telemetry API are often more generous than those for the proprietary Cloud Trace API, which you can continue to use. The Telemetry API supports VPC Service Controls. For more information about the Telemetry API, see the following documents:

  * [Telemetry API overview](https://cloud.google.com/stackdriver/docs/reference/telemetry/overview)
  * [Migrate from the Trace exporter to the OTLP endpoint](https://cloud.google.com/trace/docs/migrate-to-otlp-endpoints)
  * [Quotas and limits](https://cloud.google.com/trace/docs/quotas)



## January 24, 2025

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



## May 28, 2024

Feature

You can now search a trace for keywords. For more information, see [Search a trace](https://cloud.google.com/trace/docs/finding-traces#search-trace).

Feature

Announcing new Open Telemetry samples that show how to instrument your Python and Node.js applications to collect metrics, logs, and traces:

  * [Python example](https://cloud.google.com/stackdriver/docs/instrumentation/setup/python)
  * [Node.js example](https://cloud.google.com/stackdriver/docs/instrumentation/setup/nodejs)



For general instrumentation information and recommendations, and for links to other samples, see:

  * [Instrumentation and observability overview](https://cloud.google.com/stackdriver/docs/instrumentation/overview)
  * [Choose an instrumentation approach](https://cloud.google.com/stackdriver/docs/instrumentation/choose-approach)



## February 20, 2024

Change

For information and recommendations about how to instrument your applications to collect metrics, logs, and traces, see the following documents:

  * [Instrumentation and observability overview](https://cloud.google.com/stackdriver/docs/instrumentation/overview)
  * [Choose an instrumentation approach](https://cloud.google.com/stackdriver/docs/instrumentation/choose-approach)
  * [Go instrumentation example](https://cloud.google.com/stackdriver/docs/instrumentation/setup/go)
  * [Java instrumentation example](https://cloud.google.com/stackdriver/docs/instrumentation/setup/java)



## January 16, 2024

Change

Announcing a common navigation pane in the Google Cloud console for Logging, Monitoring, Trace, and Error Reporting. When you are troubleshooting an issue, the new navigation pane simplifies accessing the pages you need to explore different types of telemetry:

  * The **Explore** section list the pages to view and analyze telemetry data.
  * The **Detect** section lists the pages you use to ensure that you are notified when errors occur.
  * The **Configure** section lists configuration and management pages.



You can continue to use the search bar to locate pages in the Google Cloud console and to find documentation.

## October 05, 2023

Change

You can now show logs and events as inline messages when exploring a trace. For more information, see [Find and explore traces](https://cloud.google.com/trace/docs/finding-traces).

## August 14, 2023

Change

Version 2.37.0 of the Ops Agent introduces GA support for an OpenTelemetry Protocol (OTLP) receiver. You can use this receiver to collect custom traces and metrics from applications written by using OpenTelemetry SDKs. For more information, see [Use the Ops Agent and OpenTelemetry Protocol (OTLP)](https://cloud.google.com/trace/docs/otlp).

## July 21, 2023

Change

When viewing a span, you can now also view the linked spans. For more information, see [View span details](https://cloud.google.com/trace/docs/finding-traces#span-details).

## June 12, 2023

Change

The **Trace list** page has been replaced with the **Trace explorer** page, which contains a more responsive and interactive **Trace details** section. The new design delivers an improved user experience when traversing spans and when viewing span details. For more information, see [Find and explore traces](https://cloud.google.com/trace/docs/finding-traces).

## May 15, 2023

Feature

Version 2.31.0 of the Ops Agent introduces preview support for an OpenTelemetry Protocol (OTLP) receiver. You can use this receiver to collect custom traces and metrics from applications written by using OpenTelemetry SDKs. For more information, see [Collect OTLP traces](https://cloud.google.com/trace/docs/otlp).

## November 08, 2022

Change

The Trace scatterplot now indicates traces with error codes as red. For more information, see [Finding and viewing traces](https://cloud.google.com/trace/docs/finding-traces).

## October 24, 2022

Feature

You can now instrument gRPC applications to use [Microservices observability](https://cloud.google.com/stackdriver/docs/solutions/grpc).

Pricing for Microservices observability is the same as [Cloud Operations Pricing](https://cloud.google.com/stackdriver/pricing). There are no separate charges for using Cloud Trace, Cloud Monitoring, or Cloud Logging Microservices observability plugins.

## July 09, 2021

Feature

Cloud Trace announces that the OpenTelemetry library for Java is now generally available. For information about configuring your Java application to use Open Telemetry, see [Java and OpenTelemetry](https://cloud.google.com/trace/docs/setup/java-ot).

## April 19, 2021

Feature

Cloud Trace announces that the OpenTelemetry library for Python is now generally available. For information about configuring your Python application to use Open Telemetry, see [Python and OpenTelemetry](https://cloud.google.com/trace/docs/setup/python-ot).

## August 28, 2020

Feature

Cloud Trace exemplars can now be viewing in Cloud Monitoring. For more information about Trace exemplars, see [Cloud Trace exemplars](https://cloud.google.com/trace/docs/setup#create-exemplars). For more information about viewing exemplars, see [Exploring charted data](https://cloud.google.com/monitoring/charts/working-with-charts).

## August 17, 2020

Feature

The Cloud Trace viewer now supports search by the trace ID. For more information, see [Viewing Trace Details](https://cloud.google.com/trace/docs/viewing-details).

## March 30, 2020

Feature

You can now use [OpenTelemetry](https://opentelemetry.io/) with [Go](https://cloud.google.com/trace/docs/setup/go-ot) and [Node.js](https://cloud.google.com/trace/docs/setup/nodejs-ot) to instrument your applications running on GKE and Compute Engine.

## February 20, 2020

Change

Integration of Cloud Trace with Virtual Private Cloud Service Controls is now generally available. For more information, see [VPC Service Controls documentation](https://cloud.google.com/vpc-service-controls/docs/).

## February 19, 2020

Feature

[Beta release](https://cloud.google.com/products/#product-launch-stages): Export of Stackdriver Trace data to BigQuery. For more information, see [Managing Trace exports](https://cloud.google.com/trace/docs/trace-export-overview).

## February 06, 2020

Change

The [Stackdriver Trace API v2](https://cloud.google.com/trace/docs/reference) is now Generally Available.

## December 16, 2019

Feature

Integration of Stackdriver Trace with Virtual Private Cloud Service Controls is now beta. For more information, see [VPC Service Controls documentation](https://cloud.google.com/vpc-service-controls/docs/).

## November 20, 2019

Feature

The **Trace list** page has a new menu-driven filtering solution that is in Beta release testing. For more information, see [Finding and viewing traces](https://cloud.google.com/trace/docs/finding-traces).

## December 18, 2018

Change

Trace list now limits HTTP method and HTTP status matches to trace root spans. See [Filter traces](https://cloud.google.com/trace/docs/finding-traces#filter_traces) for more details.

Feature

You can now filter traces for analysis reports by the full URI, by the URI prefix, or by using trace filter. See [Create a new analysis report](https://cloud.google.com/trace/docs/analysis-reports#create_a_new_analysis_report) for details.

## October 31, 2018

Change

Stackdriver Trace enforces consumption-based pricing as of November 1, 2018 at 00:00 PDT. For more information, see [Stackdriver Pricing](https://cloud.google.com/stackdriver/pricing).

Change

On November 1, 2018, Stackdriver Trace begins enforcing a daily trace spans ingestion quota. See [Stackdriver Trace Quotas & Limits](https://cloud.google.com/trace/docs/quotas) for details.

## September 05, 2018

Feature

Billing enforcement for Trace has been postponed to November 1, 2018, rather than the previously announced date of September 30, 2018. You can now estimate your bill for your usage of Trace, according to the new pricing and in advance of billing enforcement. See [Estimating your bills](https://cloud.google.com/stackdriver/estimating-bills) for details.

## April 04, 2018

Feature

The Trace Viewer now allows you to view trace spans for related Google Cloud Platform projects in one view. See [Viewing traces across projects](https://cloud.google.com/trace/docs/cross-project-traces) for details.

## March 28, 2018

Feature

Stackdriver Trace Data Access audit logs are now Generally Available. See [Stackdriver Trace Audit Logging](https://cloud.google.com/trace/docs/audit-logging) for details.

## March 12, 2018

Change

Beginning on June 30, 2018, Stackdriver is switching to consumption-based pricing, including revised quotas. For more information, see [Stackdriver Upcoming Pricing](https://cloud.google.com/stackdriver/pricing_v2).

## February 27, 2018

Feature

The Trace Viewer now associates logs entries with trace spans when the LogEntry `span_id` field is specified. See [Integrating with Cloud Logging](https://cloud.google.com/trace/docs/trace-log-integration) for details.

Fixed

The Trace Viewer now follows your scroll through the span details page, making it easier to see span details of large traces.

## January 12, 2018

Feature

The Trace viewer now shows sub-millisecond resolution for Trace spans.

## January 09, 2018

Feature

The Trace viewer now displays span annotations and message events written with the [Stackdriver Trace API v2](https://cloud.google.com/trace/docs/reference/v2/rest/). See [Viewing Trace Details](https://cloud.google.com/trace/docs/viewing-details#annotating_spans) for more information.

## October 31, 2017

Feature

The [Stackdriver Trace API v2](https://cloud.google.com/trace/docs/reference/v2/rest/) is now in Beta release. For a comparison of the v1 and v2 APIs, see [Stackdriver Trace API](https://cloud.google.com/trace/docs/reference).

## October 02, 2017

Feature

The Trace viewer now shows parent-child relationships between trace spans. You can expand or collapse the parent spans. See [Viewing Trace Details](https://cloud.google.com/trace/docs/viewing-details) for more information.

## August 01, 2017

Feature

The Trace Viewer now allows you to view associated log entries in line with trace spans and links to VM logs for Google Cloud Load Balancer spans. See the [Integrating with Cloud Logging](https://cloud.google.com/trace/docs/trace-log-integration).

## June 05, 2017

Feature

**Advanced trace filters** : The Trace List page and Trace API now allow filtering traces by custom labels, latencies, child spans, and methods in addition to URIs. See [Trace Filters](https://cloud.google.com/trace/docs/trace-filters).

## February 06, 2017

Feature

**Zipkin tracer compatibility** : Stackdriver Trace is now compatible with Zipkin tracers. For more information, see this [blog post](https://cloudplatform.googleblog.com/2016/12/Stackdriver-Trace-Zipkin-distributed-tracing-and-performance-analysis-for-everyone.html).

Feature

**Scatter plots** : We've added a new scatter-plot selection tool to the Stackdriver Trace UI. This lets you more quickly identify, view, and compare interesting traces.

## October 20, 2016

Feature

**Analysis Reports** : Compare your application's latency profile across time and versions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
