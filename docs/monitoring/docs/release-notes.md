---
url: https://docs.cloud.google.com/monitoring/docs/release-notes/
title: Monitoring release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:24.304644+00:00
---

# Monitoring release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Resources ](https://docs.cloud.google.com/monitoring/quotas)



Send feedback 

#  Monitoring release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Monitoring. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality.

For a combined list of all release notes for the products in Google Cloud Observability, see [Consolidated release notes](https://docs.cloud.google.com/stackdriver/docs/release-notes).

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/stackdriver-release-notes.xml) directly. 

## October 06, 2026

Feature

Bulk registration of discovered services and workloads to an App Hub application is [generally available (GA)](https://docs.cloud.google.com/products#product-launch-stages). For more information, see [Register one or more discovered services or workloads](https://docs.cloud.google.com/monitoring/docs/application-monitoring#register).

## September 30, 2026

Announcement

The [application topology graph](https://docs.cloud.google.com/stackdriver/docs/observability/application-topology) is now [generally available (GA)](https://docs.cloud.google.com/products#product-launch-stages). This graph helps you to understand relationships between applications, services, and workloads, and shows you traffic flow and incidents in the context of your applications.

## September 28, 2026

Deprecated

The legacy Monitoring agent has officially reached its end of support. All standard maintenance and regular bug fixes for the agent have ceased. We recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/monitoring/agent). For more information about this deprecation, see [Legacy Monitoring and Logging agent end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents).

## September 14, 2026

Feature

Starting with version 2.71.0, you can use an Ops Agent configuration option to export your metrics, logs, and traces by using the OpenTelemetry-based [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) rather than by using the Cloud Monitoring API, Logging API, or Trace API For more information, see [Use the Telemetry API](https://docs.cloud.google.com/monitoring/agent/ops-agent/use-telemetry-api).

## September 09, 2026

Feature

A chart on a dashboard can override the dashboard's time-range setting. This feature lets you view trends over a long period or metric data with low sampling rates alongside charts that show only recent data, and is [Generally Available (GA)](https://cloud.google.com/products#product-launch-stages).

For more information, see the following documents:

  * Google Cloud console: [Set a time-range override for a chart or group](https://docs.cloud.google.com/monitoring/charts/chart-view-options#override-dashboard-time-range)
  * API: [Dashboard with an `XyChart` widget that sets a time-range override](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_a_time_range)



## September 01, 2026

Feature

You can opt out of alert notifications from an SMS notification channel by sending a text message to the phone number associated with the notification channel. For more information, see [Opt out of SMS notifications](https://docs.cloud.google.com/monitoring/docs/release-notes/monitoring/alerts/sms-opt-out).

## August 26, 2026

Change

VM Extension Manager extension policies for the Ops Agent are [Generally Available (GA)](https://docs.cloud.google.com/products#product-launch-stages). Extension policies provide zonal and project-wide Ops Agent installation, version upgrades, and configuration management. For more information, see [Install and manage the Ops Agent by using VM Extension Manager policies](https://docs.cloud.google.com/monitoring/agent/ops-agent/agent-vmem-policies).

## August 05, 2026

Announcement

The Telemetry API for metric ingestion is [generally available (GA)](https://docs.cloud.google.com/products#product-launch-stages). You can ingest OTLP metrics into Cloud Monitoring by using an OpenTelemetry Collector, an OTLP exporter, and the Telemetry API. For more information, see [OTLP metric ingestion overview](https://docs.cloud.google.com/stackdriver/docs/otlp-metrics/overview).

## June 29, 2026

Feature

Alerting policies based on PromQL queries can now operate over more than 25 hours of data. For more information, see [Query over 2 years of metric data](https://docs.cloud.google.com/monitoring/alerts/using-promql#promql-2years) and [Limits for alerting](https://docs.cloud.google.com/monitoring/quotas#alerting_uptime_limits).

## June 25, 2026

Feature

Support for applying role-based access controls (RBAC) to Cloud Monitoring dashboards and alerting policies using Tags is [generally available](https://docs.cloud.google.com/products#product-launch-stages).

You can use Tags to protect Terraform-managed Cloud Monitoring resources and configure team-scoped access. For more information, see [Use Tags to control access to resources](https://docs.cloud.google.com/monitoring/docs/access-control-with-tags).

## June 22, 2026

Feature

Metrics Explorer can automatically break down a chart into a series of tiles, with each displaying time-series data for a specific label key. This view helps you identify spikes, dips, or trends that the aggregation settings might otherwise hide.

To learn more, see [Break down a chart by labels](https://docs.cloud.google.com/monitoring/charts/breakdown-chart-by-labels).

## June 12, 2026

Change

All `agent.googleapis.com/processes` metrics are retained for 24 months. For more information, see [Data retention](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy).

## June 05, 2026

Feature

Custom dashboards can display trace data. You can view individual spans or aggregated data. This feature is [public preview](https://docs.cloud.google.com/products#product-launch-stages). For more information, see the following:

  * [Display trace data (Google Cloud console)](https://docs.cloud.google.com/monitoring/dashboards/display-traces-on-dashboards)
  * [Dashboard with trace data (API)](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard-with-trace-data)



## June 02, 2026

Feature

Support for **Histogram** widgets on custom dashboards is [generally available](https://docs.cloud.google.com/products#product-launch-stages). These widgets extract the most recent value from each time series, group those values into ranges, and then provide a graphical representation of the result. Unlike tables or other widgets that display the most recent values, **Histograms** display information about the relative frequency of ranges of values.

This widget is one of several visualizations that you can use to display the most recent values. For more information, see the following documents:

  * [Configure a histogram (Google Cloud console)](https://docs.cloud.google.com/monitoring/charts#add_histogram)
  * [Dashboard with an XyChart configured as a histogram (API)](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_a_histogram_widget)



## June 01, 2026

Feature

The details page for a span can display the call hierarchy of a trace by using a directed acyclic graph (DAG). If you view an Application Monitoring dashboard and explore the trace data that it displays, the flyout supports the DAG option. If you open the **Trace Explorer** page and explore a span, the DAG option is also available.

For more information, see the following:

  * [Application Monitoring: Explore a trace](https://docs.cloud.google.com/monitoring/docs/application-monitoring#explore-trace)
  * [Trace Explorer: Explore a trace](https://docs.cloud.google.com/trace/docs/finding-traces#explore)



## May 15, 2026

Feature

Starting with version 2.66.0, the Ops Agent can export your metrics and logs by using the OpenTelemetry-based [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) rather than by using the Cloud Monitoring API and Cloud Logging API. During the preview [Preview](https://docs.cloud.google.com/products#product-launch-stages) period, you can opt-in to using the Telemetry API. For more information, see [Use the Telemetry API](https://docs.cloud.google.com/monitoring/agent/ops-agent/use-telemetry-api).

## April 23, 2026

Feature

The [Cloud Monitoring API MCP server](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp) is generally available (GA). To learn about using the Monitoring MCP server to let agents and AI applications interact with your metrics data, see [Use the Cloud Monitoring remote MCP server](https://docs.cloud.google.com/monitoring/docs/use-monitoring-mcp).

## April 22, 2026

Feature

Application Monitoring in Google Cloud provides both agent observability and application observability. Your Application Monitoring dashboards display performance metrics, including the error rates and token usage of your AI resources. Those metrics can help you understand the health and performance of your AI resources.

To learn more, see the following:

  * [Agent observability](https://docs.cloud.google.com/stackdriver/docs/observability/agent-observability)
  * [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring)
  * [Investigate applications, services, and workloads](https://docs.cloud.google.com/stackdriver/docs/observability/application-monitoring)
  * [View AI resources](https://docs.cloud.google.com/stackdriver/docs/observability/application-monitoring-ai-resources)



## April 13, 2026

Feature

Application Monitoring can display a single, dynamic topology map showing your App Hub applications and your registered and discovered services and workloads. This interactive map identifies services and workloads that have open incidents. It also displays the error rates and P95 latency between your services and workloads.

To learn more, see the following:

  * [View application topology](https://docs.cloud.google.com/monitoring/docs/application-topology)
  * [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring)
  * [View application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring)



## April 03, 2026

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

Feature

Application Monitoring has added support for the following resources:

  * Vertex AI Workbench
  * GKE Gateway
  * GKE Ingress
  * Layer 7 cross-regional Application Load Balancers



Additionally, dashboards for Kubernetes workloads display L4 and L7 traffic metrics, when both are available. For more information, see [Application Monitoring supported infrastructure](https://docs.cloud.google.com/monitoring/docs/application-monitoring-services).

## March 30, 2026

Change

For any new project that is created on or after March 30, 2026, if the project enables the Cloud Monitoring API, [Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview).

## March 24, 2026

Feature

The Telemetry API's supports up to 60,000 metric-ingestion requests per minute per region. The regional quota replaces the global quota. To learn more, see [Telemetry API quotas and limits for metric ingestion](https://docs.cloud.google.com/monitoring/quotas#telemetry-api-metric-limits).

## March 09, 2026

Feature

You can configure legend templates for PromQL-formatted charts. To learn more, see [Configure the name of a legend column](https://docs.cloud.google.com/monitoring/charts/working-with-legends#descr_template).

## March 02, 2026

Feature

The SQL queries issued by **Observability Analytics** can now use a system-defined variable which resolves to the project ID. If a dashboard template uses the project ID variable, then you don't need to update the SQL query after installing the template.

For more information, see the following documents:

  * [Google Cloud console: Charts with SQL queries](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent#sql)
  * [API: Charts with SQL queries](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard#sql)



## February 06, 2026

Feature

You can use the [Cloud Monitoring API MCP server](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp) to let agents and AI applications interact with your time series data. This feature is in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

Feature

You can now ingest OTLP metrics into Cloud Monitoring by using an OpenTelemetry Collector, an OTLP exporter, and the Telemetry API. For more information, see [OTLP metric ingestion overview](https://docs.cloud.google.com/stackdriver/docs/otlp-metrics/overview). The Telemetry API for metric ingestion is in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

## January 26, 2026

Feature

You can now install and manage the Ops Agent on virtual machines across zones in your Google Cloud project by using global VM Extension Manager extension policies. Global and zonal extension policies can keep the installed version of the agent current, keep a specified version of the agent installed, and other tasks. For more information, see [Install and manage the Ops Agent by using VM Extension Manager policies](https://docs.cloud.google.com/monitoring/agent/ops-agent/agent-vmem-policies).

## January 21, 2026

Feature

Your Application Monitoring dashboards now display the trace spans that are associated with your registered App Hub applications. The display includes annotations that let you identify services and workloads. You can also open the Trace Explorer page from your Application Monitoring dashboards. To learn more, see the following documents:

  * [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring).
  * [View application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring).
  * [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces) describes how to use the Trace Explorer page to filter and explore your trace data.



## December 16, 2025

Other

On December 15, 2025, it was announced that your Application Monitoring dashboards will display the trace spans that are associated with your registered App Hub applications. Those dashboards don't display trace data. To view your trace data, use the Trace Explorer page.

## December 15, 2025

Feature

Your Application Monitoring dashboards now display the trace spans that are associated with your registered App Hub applications. The display includes annotations that let you identify services and workloads. You can also open the Trace Explorer page from your Application Monitoring dashboards. To learn more, see the following documents:

  * [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring).
  * [View application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring).
  * [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces) describes how to use the Trace Explorer page to filter and explore your trace data.



## December 11, 2025

Feature

You can now add a widget to a dashboard that lets you manage the settings for a variable. To learn more, see the following documents:

  * [Google Cloud console: Add widget to manage the value of a variable](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent#add-filter-control-widget)
  * [API: Dashboard with a FilterControl widget](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_filter_control)



Feature

The Google Cloud CLI (`gcloud`) commands to manage Cloud Monitoring alerting policies are now generally available. For more information, see [`gcloud monitoring policies`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies).

## December 08, 2025

Feature

You can now install and manage the Ops Agent on virtual machines in a specified zone by using VM Extension Manager extension policies. You can use extension policies to keep the installed version of the agent current, keep a specified version of the agent installed, and other tasks. For more information, see [Install and manage the Ops Agent by using VM Extension Manager policies](https://docs.cloud.google.com/monitoring/agent/ops-agent/agent-vmem-policies).

## November 04, 2025

Feature

You can now view the topology for applications that you register with App Hub. The topology map provides a graphical view of the relationships between the services and workloads in your App Hub application. The topology map also displays alerts and traffic latency, which can help you understand how your application is performing and diagnose issues. This feature is in Public Preview.

To learn more, see the following:

  * [View application topology](https://docs.cloud.google.com/monitoring/docs/application-topology)
  * [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring)



## October 23, 2025

Feature

You can now use the Google Cloud CLI and the Cloud Monitoring API to list incidents and get incident details. This feature is in Public Preview. For more information, see the following pages:

  * [Incidents for metric-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/incidents-events)
  * [`gcloud` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/alerts)
  * [API documentation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts)



## October 02, 2025

Feature

Application Monitoring is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages). Application Monitoring lets you monitor the resources and infrastructure from the perspective of an [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) application. The out-of-the-box dashboards that Application Monitoring creates can help you understand how your application's resources are performing, and they can help you diagnose issues.

  * [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring) provides a brief overview of this feature.
  * [Set up application monitoring](https://docs.cloud.google.com/monitoring/docs/setup-application-monitoring) describes how to configure an observability scope so that you have an aggregated view of your log, metric, and trace data.
  * [View application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring) describes the labels attached to your telemetry data and provides guidance about how to explore the OOTB dashboards.
  * [Supported infrastructure](https://docs.cloud.google.com/monitoring/docs/application-monitoring-services).



## September 15, 2025

Feature

When viewing a chart, you can now open a flyout that displays the chart and related log entries. To explore your metric and log data in more detail, you can then use the toolbars and menus in the flyout. To learn more, see the following:

  * [Correlate metric and log data](https://docs.cloud.google.com/monitoring/charts/working-with-charts#correlate-telemetry)
  * [Explore application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring#explore-application)



## August 25, 2025

Feature

Your Application Monitoring dashboards will display latency, error rates, and traffic level for workloads deployed on Google Kubernetes Engine, when you instrument your application with OpenTelemetry. To learn more, see [Instrument an application for Application Monitoring](https://cloud.google.com/monitoring/docs/instrument-for-application-monitoring).

## August 21, 2025

Feature

The following infrastructure is now integrated with Application Monitoring, which is in public preview.

  * AlloyDB for PostgreSQL clusters and services
  * Bigtable clusters and services
  * Dataproc Metastore services
  * Cloud Deploy delivery pipelines
  * Firestore databases
  * Secret Manager secrets



To learn more, see [Application Monitoring overview](https://cloud.google.com/monitoring/docs/about-application-monitoring) and [Supported infrastructure](https://cloud.google.com/monitoring/docs/application-monitoring-services).

## August 05, 2025

Feature

You can now use the [`time_series_billed_for_queries_count`](https://cloud.google.com/monitoring/api/metrics_gcp_i_o#monitoring/billing/time_series_billed_for_queries_count) metric to estimate charges based on the number of time series that have been queried. For more information, see [View the number of time series billed for queries](https://cloud.google.com/stackdriver/estimating-bills#mon-billable-api-reads).

Billing by time series queried isn't enforced until October 2, 2025. For more information, see [Cloud Monitoring pricing summary](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary).

## July 24, 2025

Feature

You can now monitor and understand the costs and utilization of resources in your Google Cloud project or App Hub application by using the Cost Explorer. This feature is in Public Preview. For more information, see [Optimize costs with the Cost Explorer](https://cloud.google.com//stackdriver/docs/costs/optimize-costs).

## July 17, 2025

Feature

Application-specific resource attributes are attached to your trace data when your App Hub applications use supported Google Cloud resources, or when you instrument an application with OpenTelemetry and use the Google Cloud Telemetry endpoint. To learn more, see the following:

  * [Application Monitoring overview](https://cloud.google.com/monitoring/docs/about-application-monitoring)
  * [View application telemetry](https://cloud.google.com/monitoring/docs/application-monitoring)
  * [Find and explore traces](https://cloud.google.com/trace/docs/finding-traces)
  * [Telemetry (OTLP) API overview](https://cloud.google.com/stackdriver/docs/reference/telemetry/overview)



## June 02, 2025

Feature

You can now add treemap widgets to your custom dashboards. Treemaps display the most recent value of aggregated data as a series of nested rectangles, the color saturation of a rectangle is proportional to the represented value. For more information, see the following:

  * [Display the most recent value as a treemap](https://cloud.google.com/monitoring/charts#dashboard_with_a_treemap_widget)
  * [API: Dashboard with a Treemap widget](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_a_treemap_widget)



## May 07, 2025

Issue

Version 2.56.0 of the Ops Agent using the Prometheus receiver can fail to send metrics and report negative start times. To resolve this issue, downgrade to version 2.55.0. For more information, see [Known issue: Ops Agent version 2.56.0 fails to send metrics](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-run-ingest#known-2.56.0-issue).

## May 06, 2025

Feature

When you create a snooze for a single alerting policy, you can now use resource, metric, and metadata label types to filter applicable incidents. For more information, see [Create a snooze](https://cloud.google.com/monitoring/alerts/manage-snooze#create).

## May 02, 2025

Change

The limit for the number of widgets on a custom dashboard has increased to 100, from 40. For information about dashboards, see the following:

  * [Create and manage custom dashboards](https://cloud.google.com/monitoring/charts/dashboards)
  * [Install a dashboard template](https://cloud.google.com/monitoring/dashboards/dashboard-templates)
  * [Import Grafana dashboards](https://cloud.google.com/monitoring/dashboards/import-grafana-dashboards)



## April 09, 2025

Feature

Application Monitoring lets you monitor the resources and infrastructure from the perspective of an [App Hub](https://cloud.google.com/app-hub/docs/overview) application. The out-of-the-box (OOTB) dashboards generated for your application display log, metric, and incident data. These dashboards can help you understand how your application's resources are performing, and they can help you to diagnose issues. This feature is in Public Preview. 

  * [Application Monitoring overview](https://cloud.google.com/monitoring/docs/about-application-monitoring) provides a brief overview of this feature.
  * [Set up application monitoring](https://cloud.google.com/monitoring/docs/setup-application-monitoring) describes how to configure an observability scope so that you have an aggregated view of your log, metric, and trace data.
  * [View application telemetry](https://cloud.google.com/monitoring/docs/application-monitoring) describes the labels attached to your telemetry data, and it provides guidance about how to explore the OOTB dashboards.



Feature

Application Monitoring now supports [app-enabled folders](https://cloud.google.com/app-hub/docs/overview#app-enabled-folder) and [App Hub host projects](https://cloud.google.com/app-hub/docs/overview#host-project). For app-enabled folders, the metrics scope of the management project is automatically synchronized with the list of projects in the folder, provided quota is available. This feature is in Public Preview.

  * [Metrics scopes for app-enabled folders](https://cloud.google.com/monitoring/settings/metrics-scope-app-enabled-folders) describes the synchronization algorithm and how to view your usage of the metrics scope quota.



## April 04, 2025

Feature

If you have enabled logging for failures of an uptime check, you can view the logs from the **Uptime details** page. For more information, see [View details of an uptime check](https://cloud.google.com/monitoring/uptime-checks/manage#get).

## March 21, 2025

Announcement

The Google-Built OpenTelemetry Collector is now available. This Collector is an open-source, production-ready build of the upstream OpenTelemetry Collector that is built with upstream OpenTelemetry Collector components. The Google-built Collector lets you send correlated OTLP traces, metrics, and logs to Cloud Observability and other backends from applications instrumented by using OpenTelemetry SDKs. The Collector also captures metadata for Google Cloud resources, so you can correlate application performance data with infrastructure telemetry data.

For information about using this Collector, see [Overview of the Google-Built OpenTelemetry Collector](https://cloud.google.com/stackdriver/docs/instrumentation/google-built-otel).

## March 17, 2025

Change

You can now enable and disable uptime-checks by using the [`disabled` field](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#uptimeCheckConfig.FIELDS.disabled) in the Cloud Monitoring API.

## March 13, 2025

Feature

Documentation for Slack notification channels now supports Markdown. For more information, see [Annotate notifications with user-defined documentation](https://cloud.google.com/monitoring/alerts/doc-variables).

Feature

You can now see changes made to a dashboard by viewing the version history. For more information, see [View dashboard version history](https://cloud.google.com/monitoring/charts/dashboards#version-history).

## February 27, 2025

Feature

On your custom dashboards, you can reduce the load time of the dashboard by using group widgets. The tab-group widget displays one member of a collection, and it provides tabs on the toolbar to let you select which member to display:

  * [Organize dashboard widgets](https://cloud.google.com/monitoring/dashboards/text-and-grouping#organize_widgets) describes grouping widgets and provides configuration information for the different types.

  * [Dashboard with a `SingleViewGroup` widget](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_svgroup) describes which API fields to use to configure a tab-group widget.




## February 26, 2025

Change

You can now enable and disable the logging of uptime-check failures by using the [`log_check_failures` field](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#uptimeCheckConfig.FIELDS.log_check_failures) in the Cloud Monitoring API.

## February 20, 2025

Feature

When you add an Observability Analytics widget to a custom Cloud Monitoring dashboard, you can now select other log views and analytics views to query in the Views & Schema section. For more information, see [Display charts generated from a Log Analytics query](https://cloud.google.com/monitoring/charts/view-logs#add-sql-chart).

## February 14, 2025

Change

The **Dashboards** page of the Cloud Console has been refreshed. For more information about dashboards, see the following documents:

  * [Dashboards overview](https://cloud.google.com/monitoring/dashboards).
  * [Install a dashboard by uploading a template from GitHub](https://cloud.google.com/monitoring/dashboards/dashboard-templates). 
  * [Create and manage custom dashboards](https://cloud.google.com/monitoring/charts/dashboards).



## February 10, 2025

Feature

You can now use a variable to control the visibility of a dashboard widget. For more information, see the following documents:

  * [Create and manage variables and pinned filters](https://cloud.google.com/monitoring/dashboards/filter-permanent)
  * [Configure dashboard filters and variables by using the API](https://cloud.google.com/monitoring/dashboards/api-dashboard#define_filters)



## February 04, 2025

Feature

When you create a snooze from the **Incident details** page, you can now apply the snooze to other incidents that have one or more of the same resource labels. For more information, see [Create a snooze](https://cloud.google.com/monitoring/alerts/manage-snooze#create).

## February 03, 2025

Feature

You can now create custom organization policies on alerting policies, notification channels, and snoozes. For more information, see [Use custom organization policies](https://cloud.google.com/monitoring/docs/custom-constraints).

## January 31, 2025

Feature

You can now monitor usage, throughput, and latency, and troubleshoot 429 errors on Vertex AI foundation models like Google Gemini and Anthropic Claude by using a new predefined dashboard. After querying a model from the [Vertex AI Model Garden](https://cloud.google.com/model-garden), you can find the models associated with your project from the Vertex AI **Dashboard** page under the "Model observability" heading.

To customize the dashboard and explore relevant metrics in Cloud Monitoring, click **Show All Metrics**. For information about using dashboards in Cloud Monitoring, see [View and customize Google Cloud dashboards](https://cloud.google.com/monitoring/charts/predefined-dashboards).

## December 13, 2024

Feature

Reporting of the "pending" status of the Ops Agent on the Cloud Monitoring **VM Instances** dashboard has been refined to include additional states. For more information, see [Use **VM Instances** dashboard](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#verify-agent-running-with-vm-instance-dashboard).

## December 12, 2024

Feature

You can now override the validation that checks for metric existence when you create a PromQL-based alerting policy. For more information, see [Disable check for metric existence](https://cloud.google.com/monitoring/promql/create-promql-alerts#disable-validation).

Feature

Text widgets can now link to sections of a dashboard and they can render variables. For more information, see the following documents:

  * [Add text to a dashboard](https://cloud.google.com/monitoring/dashboards/text-and-grouping#add_text_box)
  * [Add sections to a dashboard](https://cloud.google.com/monitoring/dashboards/text-and-grouping#add_section_header)
  * [Create and manage variables and pinned filters](https://cloud.google.com/monitoring/dashboards/filter-permanent)



## November 11, 2024

Feature

Dashboard variables and dashboard-level filtering is now GA. Pinned filters and variables can have multiple default values and they support selection of multiple values. For more information, see the following documents:

  * [Create and manage variables and pinned filters](https://cloud.google.com/monitoring/dashboards/filter-permanent)
  * [Apply a variable to a widget](https://cloud.google.com/monitoring/dashboards/filter-permanent#apply-permanent-filter)



## October 28, 2024

Feature

The capabilities for dashboard-level filtering has been enhanced. You can now configure pinned filters and variables to have multiple default values and support selection of multiple values. You can also create value-only variables and generate the list of possible values for a variable by running a SQL query. These features are in Public Preview. For more information, see the following documents:

  * [Create and manage variables and pinned filters](https://cloud.google.com/monitoring/dashboards/filter-permanent)
  * [Apply a variable to a widget](https://cloud.google.com/monitoring/dashboards/filter-permanent#apply-permanent-filter)



## October 24, 2024

Feature

You can now create alerting policies that monitor the results of your SQL queries. For more information about SQL-based alerting policies, see the following documents:

  * [Monitor your SQL query results with an alerting policy](https://cloud.google.com/logging/docs/analyze/sql-in-alerting)
  * [Incidents for SQL-based alerting policies](https://cloud.google.com/monitoring/alerts/sql-based-incidents)



## October 14, 2024

Feature

You can now use the Monitoring API to configure a metric-based alerting policy to send notifications when incidents are closed. For more information, see [AlertStrategy](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#alertstrategy) in the Monitoring API documentation.

## October 09, 2024

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

Change

The user interface for configuring which events to show on a dashboard has been simplified. For more information, see [Show events on a dashboard](https://cloud.google.com/monitoring/dashboards/show-events).

## September 30, 2024

Feature

You can now apply and modify dashboard-wide filters by selecting the filter option within the cell of a table. For example, if a table has a column named `zone` and a cell that displays `us-east5-b`, then selecting the filter button in that cell applies the dashboard-wide filter `zone: us-east5-b`. For more information about filtering your dashboard, see the following documents:

  * [Add temporary filters](https://cloud.google.com/monitoring/charts/filter-dashboard)
  * [Add and mange permanent filters and variables](https://cloud.google.com/monitoring/dashboards/filter-permanent)



## September 23, 2024

Change

The layout of the incident detail page has been updated. You can now view related incidents, and switch between viewing only the time series that caused the condition to be met and viewing all time series that the alerting policy evaluated. For more information, see [Incidents for metric-based alerting policies](https://cloud.google.com/monitoring/alerts/incidents-events) and [Incidents for log-based alerting policies](https://cloud.google.com/monitoring/alerts/log-based-incidents).

## September 16, 2024

Feature

There is a new Cloud Observability Overview page in the Google Cloud console. The new page, which you can customize, introduces the Cloud Observability products, and provides information about your logs, dashboards, incidents, and more. This page can help you detect issues in your resources, view relevant events, and view signals that matter to you.

## September 09, 2024

Feature

Table and TopList widgets can now display the results of multiple queries. You can also configure the column headers, data alignment, and color-code cells based on how a numeric value compares to a threshold. For more information, see the following documents:

  * [Display the most recent data in tabular form](https://cloud.google.com/monitoring/charts#add_table)
  * [API Example: Dashboard with a `TimeSeriesTable` widget](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_a_table_widget)



## September 06, 2024

Feature

The **Metrics management** page in Cloud Monitoring now shows you the [sources of metric reads](https://cloud.google.com/monitoring/docs/metrics-management#metric-read-sources) and lets you [exclude unneeded metrics](https://cloud.google.com/monitoring/docs/metrics-management#exclude-metrics) entirely, eliminating the cost of ingesting them. For more information, see [View and manage metric usage](https://cloud.google.com/monitoring/docs/metrics-management).

Feature

The fleetwide and per-instance **Observability** tabs on the Compute Engine **VM instances** page now include charts for GPU metrics the from NVIDIA Management Library (NVML). To view the fleetwide GPU charts, select **Compute Engine** > **VM instances** > **Observability**. To view the GPU charts for a VM instance, select **Compute Engine** > **VM instances** , click on the name of a VM instance, and then select **Observability**. These charts are available only for VM instances with attached GPUs, with both the Ops Agent and the NVIDIA GPU driver installed. For information about configuring these VMs, see [About the `gpu` metrics](https://cloud.google.com/monitoring/agent/ops-agent/configuration#receiver-nvml-metrics).

## September 02, 2024

Feature

You can now import Grafana dashboards into Cloud Monitoring by using the console. For more information, see [Import Grafana dashboards into Cloud Monitoring](https://cloud.google.com/monitoring/dashboards/import-grafana-dashboards).

## August 22, 2024

Deprecated

Cloud Monitoring has ended support for the ingestion of [AWS CloudWatch metrics](https://cloud.google.com/monitoring/api/metrics_aws) by using AWS connector projects. This is a breaking change. For information about this deprecation, see [Deprecations: AWS CloudWatch metrics in Connector projects](https://cloud.google.com/stackdriver/docs/deprecations/aws-cloudwatch-metrics-ingestion).

You can continue to collect AWS CloudWatch metrics by using the open source Prometheus CloudWatch exporter and the Ops Agent. For information about this solution, see [Collect AWS CloudWatch metrics by using the Prometheus CloudWatch exporter](https://cloud.google.com/monitoring/custom-metrics/aws-prometheus-cloudwatch).

## July 30, 2024

Feature

You can now troubleshoot Compute Engine issues involving host events, MIG autoscaling and health-check failures, resource-availability errors, and VM performance by using the new "interactive playbook" dashboards in Cloud Monitoring. You can access the playbook dashboards from the **Dashboards** page by selecting the **GCP** category or by filtering for "GCE Interactive Playbook".

## July 23, 2024

Deprecated

Starting October 22, 2024, [Monitoring Query Language (MQL)](https://cloud.google.com/monitoring/mql) will no longer be a recommended query language for Cloud Monitoring, and we will begin to turn off certain usability features. For more information, see the [deprecation note for MQL](https://cloud.google.com/stackdriver/docs/deprecations/mql).

## July 09, 2024

Announcement

Starting no sooner than January 7, 2025, Cloud Monitoring will begin charging for alerting. For information about the pricing model and examples of pricing scenarios, see [Pricing for alerting](https://cloud.google.com/stackdriver/pricing#pricing-alerting).

## July 08, 2024

Feature

Your dashboards will now recommend event types for display. For more information, see [Show events on a dashboard](https://cloud.google.com/monitoring/dashboards/show-events).

## July 03, 2024

Change

Agent-installation policies for the Ops Agent are now GA. For more information, see [Overview of agent policies for the Ops Agent](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/agent-policies-overview).

## July 01, 2024

Feature

You can now create private uptime checks that issue TCP requests. For more information, see [Create private uptime checks](https://cloud.google.com/monitoring/uptime-checks/private-checks).

## June 26, 2024

Feature

You can now configure your dashboards to show disruptions in Google Cloud Services. This feature is GA. For more information, see the following pages:

  * For event information, see [Personalized Service Health events](https://cloud.google.com/monitoring/dashboards/event-types#psh-events).
  * For information about enabling events, see [Show events on a dashboard](https://cloud.google.com/monitoring/dashboards/show-events).



## June 25, 2024

Feature

Ops Agent version 2.48.0 introduces support for Compute Engine VMs that are running Deep Learning VM Images based on Debian 11 (Bullseye). For more information, see [Operating systems](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#supported_operating_systems).

## June 24, 2024

Feature

You can now configure your dashboards to show when incidents were opened. For more information, see [Alert events](https://cloud.google.com/monitoring/dashboards/event-types#alert-events).

## June 17, 2024

Feature

In the Monitoring API, you can now configure documentation links for your notifications. For more information, see [Links](https://cloud.google.com/monitoring/alerts/doc-variables#add-links).

## June 06, 2024

Feature

You can now pin your event type selections for custom dashboards. Pinning saves your selections to the dashboard configuration, so they are applied when you reopen the dashboard. For more information, see [Show events on a dashboard](https://cloud.google.com/monitoring/dashboards/show-events).

## May 29, 2024

Change

Ops Agent version 2.47.0 introduces support for Compute Engine VMs that are running Ubuntu 24.04 LTS (Noble Numbat). For more information, see [Operating systems](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#supported_operating_systems).

## May 28, 2024

Feature

Announcing new Open Telemetry samples that show how to instrument your Python and Node.js applications to collect metrics, logs, and traces:

  * [Python example](https://cloud.google.com/stackdriver/docs/instrumentation/setup/python)
  * [Node.js example](https://cloud.google.com/stackdriver/docs/instrumentation/setup/nodejs)



For general instrumentation information and recommendations, and for links to other samples, see:

  * [Instrumentation and observability overview](https://cloud.google.com/stackdriver/docs/instrumentation/overview)
  * [Choose an instrumentation approach](https://cloud.google.com/stackdriver/docs/instrumentation/choose-approach)



## May 13, 2024

Feature

You can now configure dashboards to display events by using the Monitoring API.

  * For event information, see [Event types](https://cloud.google.com/monitoring/dashboards/event-types#psh-events).
  * For information about enabling events, see [Show events on a dashboard](https://cloud.google.com/monitoring/dashboards/show-events).
  * For an example, see [API examples: Enable dashboard events and filters](https://cloud.google.com/monitoring/dashboards/api-examples#filters-events).



## May 09, 2024

Feature

You can now configure a logs panel widget to display log entries by log view. For more information, see [Display logs and errors on a custom dashboard](https://cloud.google.com/monitoring/charts/view-logs).

## May 06, 2024

Feature

Synthetic monitors no longer require that the ingress rule be set to allow all traffic. For more information, see [Cloud Function configuration](https://cloud.google.com/monitoring/synthetic-monitors/create#function-configuration).

Feature

A Selenium WebDriver sample is now available for [synthetic monitors](https://cloud.google.com/monitoring/uptime-checks/introduction). For more information, see [Selenium WebDriver template](https://cloud.google.com/monitoring/synthetic-monitors/samples#selenium-sample).

## April 26, 2024

Feature

Broken-link checkers collect screenshots of failing tests in a Cloud Storage bucket. You can configure this feature to collect screenshots for all tests or disable this feature. For more information, see [Create a broken-link checker](https://cloud.google.com/monitoring/synthetic-monitors/broken-links).

## March 28, 2024

Feature

Uptime checks now support authentication by using a service account and a generated OpenID Connect (OIDC) token, as an alternative to providing a username and password. For more information, see [Create public uptime checks](https://cloud.google.com/monitoring/uptime-checks).

## March 26, 2024

Change

Duet AI in Google Cloud is now Gemini for Google Cloud. See our [blog post](https://blog.google/technology/ai/google-gemini-update-sundar-pichai-2024/) for more information.

## March 18, 2024

Change

You can now use Duet AI for Developers to help you create a synthetic monitor. This feature is in Public Preview. For more information, see [Create a synthetic monitor](https://cloud.google.com/monitoring/synthetic-monitors/create).

## March 07, 2024

Feature

You can display events, such as the crash of a GKE pod, on your dashboards. This feature is now GA. This feature is available for dashboards managed by Cloud Monitoring, and for the observability dashboards managed by Compute Engine, Google Kubernetes Engine and Cloud Run. 

  * For a list of supported events, see [Event types](https://cloud.google.com/monitoring/dashboards/event-types).
  * For information about enabling events, see [Show events on a dashboard](https://cloud.google.com/monitoring/dashboards/show-events).



## February 20, 2024

Change

For information and recommendations about how to instrument your applications to collect metrics, logs, and traces, see the following documents:

  * [Instrumentation and observability overview](https://cloud.google.com/stackdriver/docs/instrumentation/overview)
  * [Choose an instrumentation approach](https://cloud.google.com/stackdriver/docs/instrumentation/choose-approach)
  * [Go instrumentation example](https://cloud.google.com/stackdriver/docs/instrumentation/setup/go)
  * [Java instrumentation example](https://cloud.google.com/stackdriver/docs/instrumentation/setup/java)



## February 12, 2024

Change

You can now create a broken-link checker, which periodically validates the links contained in your website. This feature is GA. For more information, see [Create a broken-link checker](https://cloud.google.com/monitoring/synthetic-monitors/broken-links).

Feature

[Alerting policies with a PromQL-based condition](https://cloud.google.com/monitoring/promql/promql-in-alerting) are [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## January 29, 2024

Change

New event types for VM instances and for GKE Pods, Clusters, and Nodes, are now available to display on your dashboards. This feature is in Public Preview. 

  * For a list of supported events, see [Events overview](https://cloud.google.com/monitoring/dashboards/event-types).
  * For information about enabling events, see [Show events on a dashboard](https://cloud.google.com/monitoring/dashboards/show-events).



## January 22, 2024

Feature

You can now create and manage your uptime checks and synthetic monitors by using the Google Cloud CLI. For more information, see [Create public uptime checks](https://cloud.google.com/monitoring/uptime-checks) and [Create a synthetic monitor](https://cloud.google.com/monitoring/synthetic-monitors/create).

## January 19, 2024

Feature

Ops Agent version 2.46.0 introduces a new health check, LogPingOpsAgent, an informational payload message written every 10 minutes to the `ops-agent-health` log. You can use the resulting log entries to verify that the agent is sending logs. For more information, see [Agent health checks](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-find-info#health-checks).

## January 16, 2024

Feature

Observability for Google Kubernetes Engine: You can now enable the package of kube state metrics from the **Observability** tab of a GKE deployment. For more information, see [Package: Kube state metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#ksm-package).

Change

Announcing a common navigation pane in the Cloud console for Logging, Monitoring, Trace, and Error Reporting. When you are troubleshooting an issue, the new navigation pane simplifies accessing the pages you need to explore different types of telemetry:

  * The **Explore** section list the pages to view and analyze telemetry data.
  * The **Detect** section lists the pages you use to ensure that you are notified when errors occur.
  * The **Configure** section lists configuration and management pages.



You can continue to use the search bar to locate pages in the Cloud console and to find documentation.

## December 20, 2023

Feature

Observability for Google Kubernetes Engine: The collection of kube state metrics is enabled by default for new GKE Autopilot clusters, starting with version 1.27.4-gke.900. For more information, see [Package: Kube state metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#ksm-package).

## December 19, 2023

Feature

On your custom dashboards, you can add section widgets that create a table of contents for your dashboard. You can use the table of contents to navigate to a specific section of your dashboard. For more information, see [Organize dashboard widgets](https://cloud.google.com/monitoring/dashboards/text-and-grouping#organize_widgets).

## December 18, 2023

Feature

On your custom dashboards, you can group widgets into a single-view widget or into a collapsible group. Single-view widgets let you display one member of the group. For more information, see [Organize dashboard widgets](https://cloud.google.com/monitoring/dashboards/text-and-grouping#organize_widgets).

## December 15, 2023

Change

Starting with Ops Agent version 2.45.0, you can configure the Ops Agent to exclude individual metrics and metrics from third-party integrations. For more information, see [Metrics processors](https://cloud.google.com/monitoring/agent/ops-agent/configuration#metrics-processors)

Feature

You can now collect Prometheus metrics from Cloud Run services by using the [Managed Service for Prometheus sidecar for Cloud Run](https://cloud.google.com/stackdriver/docs/managed-prometheus/cloudrun-sidecar).

## December 12, 2023

Feature

You can now configure the severity of your alerting policies. This field lets you define the severity level of incidents. For more information, see [Structure of an alerting policy](https://cloud.google.com/monitoring/alerts/policies-in-api#api-alertpol-struct).

## December 11, 2023

Change

Support for pie charts on your custom dashboards is now GA. For information when using the Cloud Console, see [Graph the most recent data with a pie chart](https://cloud.google.com/monitoring/charts#add_pie). For information about using the API, see [Dashboard with a PieChart widget](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_a_pie_widget).

Change

The new query interface for creating charts is now GA. The new interface provides a style update and simplifies building a query by automatically configuring your aggregation settings. For more information, see [Create charts with Metrics Explorer](https://cloud.google.com/monitoring/charts/metrics-explorer).

## December 07, 2023

Feature

You can now create a broken-link checker, which periodically validates the links contained in your website. This feature is in Public Preview. For more information, see [Create a broken-link checker](https://cloud.google.com/monitoring/synthetic-monitors/broken-links).

## December 01, 2023

Feature

Ops Agent version 2.44.0 introduces the following features:

  * Support for Compute Engine VMs that are running Ubuntu 23.10 (Mantic Minotaur). For more information, see [Operating systems](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#supported_operating_systems).
  * Support for Compute Engine Arm VMs that are running Debian 12 (Bookworm). For more information, see [Support for Compute Engine Arm VMs](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#oagent-arm-support).
  * An option to prevent the agent from collecting self logs and sending them to Cloud Logging. For more information, see [Collection of self logs](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#self-log-collection).



## November 17, 2023

Feature

Observability for Google Kubernetes Engine: The **Observability** tab for a GKE cluster adds a dashboard for GPU metrics. The charts on this dashboard are populated only if the cluster has GPU nodes. For more information, see [View observability metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).

## November 13, 2023

Change

A new query interface for creating charts is now in Public Preview. The new interface provides a style update and simplifies building a query by automatically configuring your aggregation settings. For more information, see [Create charts with Metrics Explorer](https://cloud.google.com/monitoring/charts/metrics-explorer).

## November 09, 2023

Feature

You can now display events, such as the crash of a GKE pod, on your dashboards. This feature is in Public Preview. 

  * For a list of supported events, see [Events overview](https://cloud.google.com/monitoring/dashboards/event-types).
  * For information about enabling events, see [Show events on a dashboard](https://cloud.google.com/monitoring/dashboards/show-events).



## November 08, 2023

Change

Observability for Google Kubernetes Engine: The curated set of kube state metrics is now Generally Available. You can enable this package of metrics from the **Observability** tab for your GKE cluster and preview the available charts and metrics before you enable the metrics. For more information, see [Package: Kube state metrics](https://cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#ksm-package).

## November 07, 2023

Feature

Observability for Google Kubernetes Engine: The **Observability** tab for a GKE deployment now shows application performance metrics if the metrics are available. The supported metric sources include Istio, GKE Ingress, NGINX Ingress and gRPC and HTTP metrics collected by using Google Managed Service for Prometheus. For more information, see [Use application performance metrics](https://cloud.google.com/stackdriver/docs/solutions/gke/app-performance-metrics).

## November 03, 2023

Change

Synthetic monitors are now GA. You can create synthetic monitors by using Terraform, the Cloud console, and the Monitoring API. You can configure your synthetic monitors to collect log data and trace data. When you use the Cloud console, the generic and Mocha templates are available:

  * For general information, see [Synthetic monitoring overview](https://cloud.google.com/monitoring/uptime-checks/introduction).
  * For information about creating a synthetic monitor, see [Create a synthetic monitor](https://cloud.google.com/monitoring/synthetic-monitors/create).



## October 24, 2023

Feature

Ops Agent version 2.43.0 introduces support for Compute Engine Arm VMs that are running SLES 15 and OpenSUSE Leap 15. For more information, see [Support for Compute Engine Arm VMs](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#oagent-arm-support).

## October 23, 2023

Change

You can configure your synthetic monitors to collect log data and trace data for your outbound HTTP requests when you use the generic template. This feature is in Public Preview. For more information, see [Samples for synthetic monitors](https://cloud.google.com/monitoring/synthetic-monitors/samples).

## October 17, 2023

Feature

You can now view error groups on your custom dashboards. This feature is GA. For information when using the Cloud Console, see [Display logs and errors on a custom dashboard](https://cloud.google.com/monitoring/charts/view-logs). For information about using the API, see [Dashboard with an ErrorReportingPanel widget](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_er_panel).

## October 09, 2023

Change

When you install the Ops Agent on a Compute Engine VM by using the Cloud Monitoring **VM Instances** dashboard or the **Observability** tab on a Compute Engine VM details page, the agent is now installed with an Ops Agent OS policy. This installation method replaces the prior set of manual steps. For more information, see [Installing the agent by using the Google Cloud console](https://cloud.google.com/monitoring/agent/ops-agent/installation#gce-ui-install).

## October 05, 2023

Feature

Ops Agent version 2.42.0 introduces support for Compute Engine Arm VMs that are running Ubuntu 22.04 LTS (Jammy Jellyfish). For more information, see [Support for Compute Engine Arm VMs](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#oagent-arm-support).

Change

Dashboard-wide filters now apply to the Logs Panel widget. For more information, see [Filter the log entries](https://cloud.google.com/monitoring/charts/view-logs#filter_the_log_entries).

## October 02, 2023

Feature

You can now configure notifications for Google Chat spaces. For more information, see [Create and manage notification channels](https://cloud.google.com/monitoring/support/notification-options#google-chat).

Change

The **Metrics management** page in Cloud Monitoring now lets you create alerting policies and charts for metrics that have no associated alerting policies or custom dashboards. For more information, see [View and manage metric usage](https://cloud.google.com/monitoring/docs/metrics-management).

Feature

You can now import your Grafana dashboards into Cloud Monitoring. For more information, see [Import Grafana dashboards into Cloud Monitoring](https://cloud.google.com/monitoring/dashboards/import-grafana-dashboards).

## September 29, 2023

Issue

Ops Agent versions 2.39.0 and 2.40.0 crash if you use them on Compute Engine VMs with attached GPUs. Use Ops Agent version 2.38.0, or versions 2.41.0 and newer, on VMs with attached GPUs.

## September 28, 2023

Change

You can now configure your alerting policy documentation with custom subject lines. For more information, see [Configure the subject line of notifications](https://cloud.google.com/monitoring/alerts/doc-variables#subjects).

## September 14, 2023

Feature

Ops Agent version 2.40.0 introduces support for Compute Engine Arm VMs that are running RHEL 9 or Rocky Linux 9. For more information, see [Support for Compute Engine Arm VMs](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#oagent-arm-support).

## September 07, 2023

Feature

Ops Agent version 2.39.0 introduces support for Compute Engine Arm VMs that are running Ubuntu 20.04 LTS (Focal Fossa). For more information, see [Support for Compute Engine Arm VMs](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#oagent-arm-support).

Change

Starting with version 2.39.0, the Ops Agent supports ingesting Prometheus metrics with unknown types. In earlier versions, untyped metrics are treated by the Ops Agent as gauges, but starting with Ops Agent version 2.39.0, untyped metrics are treated as both gauges and counters, and you can apply cumulative operations to the metrics.

If you have charts or alterting policies based on untyped metrics and written with MQL, you must adjust your queries. For more information, see [Prometheus untyped metrics change metric type starting with Ops Agent version 2.39.0](https://cloud.google.com/monitoring/agent/ops-agent/troubleshoot-run-ingest.md#untyped-metrics).

## August 21, 2023

Feature

You can now add pie charts to your custom dashboards. Support for pie charts is in public preview. For information when using the Cloud Console, see [Graph the most recent data with a pie chart](https://cloud.google.com/monitoring/charts#add_pie). For information about using the API, see [Dashboard with a PieChart widget](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_a_pie_widget).

Feature

Observability for Google Kubernetes Engine: The **Observability** tab for each of your GKE clusters now includes filters for recommended and configured integrations. To see the recommended integrations for your cluster, select **Integrations > Overview**. To see the integrations configured for your cluster, select **Integrations > Configured**.

## August 18, 2023

Deprecated

Cloud Monitoring is ending support for the ingestion of [AWS CloudWatch metrics](https://cloud.google.com/monitoring/api/metrics_aws) in AWS connector projects. This is a breaking change. For information about this deprecation, see [Deprecations: AWS CloudWatch metrics in Connector projects](https://cloud.google.com/stackdriver/docs/deprecations/aws-cloudwatch-metrics-ingestion).

You can continue to collect AWS CloudWatch metrics by using the open source Prometheus CloudWatch exporter and the Ops Agent. For information about migrating to this solution, see [Collect AWS CloudWatch metrics by using the Prometheus CloudWatch exporter](https://cloud.google.com/monitoring/custom-metrics/aws-prometheus-cloudwatch).

## August 17, 2023

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

Feature

You can now troubleshoot GKE issues involving CPU and memory utilization by using the new "interactive playbook" dashboards in Cloud Monitoring. You can access these playbook dashboards from the **Dashboards** list and from the **Incident details** page associated with alerts you've set up for CPU utilization or memory utilization.

Feature

Observability for Google Kubernetes Engine: You can now enable a curated set of kube state metrics from the **Observability** tab for your GKE cluster. You can also preview the available charts and metrics before you enable the metrics. For more information, see [Package: Kube state metrics](https://cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#ksm-package).

## August 14, 2023

Feature

Version 2.37.0 of the Ops Agent introduces runtime health checks for errors in the configuration of logging pipelines and in parsing logs. These errors are reported to Cloud Logging. For more information, see [Agent health checks](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/troubleshoot-find-info#health-checks).

Change

Version 2.37.0 of the Ops Agent introduces GA support for an OpenTelemetry Protocol (OTLP) receiver. You can use this receiver to collect custom metrics and traces from applications written by using OpenTelemetry SDKs. For more information, see [Collect OpenTelemetry protocol (OTLP) metrics and traces](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/otlp).

## August 10, 2023

Feature

PromQL alerting for Cloud Monitoring is in Public Preview. You can now use PromQL queries in your alerting policies. You can also migrate your Prometheus alerting rules to Cloud Monitoring alerting rules with a PromQL query, and migrate your Prometheus receivers to Cloud Monitoring notification channels. For more information, see [Alerting policies with PromQL](https://cloud.google.com/monitoring/promql/promql-in-alerting).

## August 08, 2023

Change

The price of Managed Service for Prometheus samples ingested into Cloud Monitoring has dropped by 60 percent. For more information, see [Cloud Monitoring pricing summary](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary), and for worked examples, see [Pricing examples based on samples ingested](https://cloud.google.com/stackdriver/pricing#pricing_examples_samples).

## August 07, 2023

Change

The **Metrics management** page in Cloud Monitoring replaces the **Metrics diagnostics** page, extending the information available about the chargeable metrics in your Google Cloud projects. For more information, see [View metric usage and diagnostics](https://cloud.google.com/monitoring/docs/metrics-management).

Feature

Observability for Google Kubernetes Engine: Charts on the **Observability** tab for each of your GKE clusters and workloads now includes an optional fleet ID filter, where applicable. If the current project is a host project for a fleet, the cluster and workload charts show metrics from all projects in the fleet, even if the metrics are hosted in a different project.

## August 01, 2023

Feature

You can now snooze an alerting policy from an Incident details page related to the alerting policy. For more information, see [Snooze an alerting policy](https://cloud.google.com/monitoring/alerts/incidents-events#snoozing).

Feature

Ops Agent version 2.36.0 introduces support for Compute Engine Arm VMs that are running Debian 11 (Bullseye). For more information, see [Support for Compute Engine Arm VMs](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#oagent-arm-support).

## July 26, 2023

Change

Starting with version 2.35.0, the Ops Agent health-check log is renamed `ops-agent-health`; earlier versions of the Ops Agent that support health checks use the name `ops-agent-health-checks`.

## July 20, 2023

Change

We made improvements to the dashboard building experience:

  * Improved the performance
  * Simplified the layout and expanded the configurable settings
  * Improved the widget drag and drop experience
  * Enhanced the [text widget](https://cloud.google.com/monitoring/dashboards/text-and-grouping)
  * Unified the chart-configuration experience between dashboards and the Metrics Explorer



For more information, see [Add charts and tables to a custom dashboard](https://cloud.google.com/monitoring/charts).

## July 17, 2023

Feature

You can now create synthetic monitors, which let you continuously test the availability, consistency, and performance of your services and application web pages and APIs, by using automated script based tests. Synthetic monitors periodically probe the endpoints of your application and they record whether or not a probe was successful, along with additional data about the request. For more information, see [Synthetic monitoring overview](https://cloud.google.com/monitoring/uptime-checks/introduction).

## July 07, 2023

Feature

You can now troubleshoot common GKE issues like unschedulable pods and crashlooping containers by using the new "interactive playbook" dashboards in Cloud Monitoring. For information about using these dashboards, see the GKE troubleshooting documentation for [unschedulable pods](https://cloud.google.com/kubernetes-engine/docs/troubleshooting#PodUnschedulable) and [crashlooping](https://cloud.google.com/kubernetes-engine/docs/troubleshooting#CrashLoopBackOff).

## July 06, 2023

Feature

The Google Cloud console can now automatically install the Ops Agent for you when you create a VM instance. During the installation process, the Compute Engine VM Manager creates an Ops Agent OS policy that installs the agent and reinstalls it when necessary. For more information, see [Install the Ops Agent during VM creation](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-agent-vm-creation).

## June 13, 2023

Feature

You can now grant a predefined role that only lets you view and manage incidents. For more information, see [Access control: Incidents](https://cloud.google.com/monitoring/access-control#incident_roles_desc).

## June 09, 2023

Feature

**Google Cloud Managed Service for Prometheus** can now ingest exemplars attached to histogram metrics. Exemplars are commonly used to attach trace data to latency metrics, to help you find the cause of a sudden change in metric values. For information, see [Use Prometheus exemplars](https://cloud.google.com/stackdriver/docs/managed-prometheus/exemplars).

Change

A new version of Managed Service for Prometheus is now available. Version 0.7.0 of managed collection for Kubernetes has been released. Users who deploy managed collection using `kubectl` should [reapply the manifests](https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#config-mgd-collection). Users who deploy the service using `gcloud` or the GKE UI are already upgraded on clusters running version 1.25 or newer. Self-deployed collection users should upgrade their binaries to use [gke.gcr.io/prometheus-engine/prometheus:v2.35.0-gmp.5-gke.0](http://gke.gcr.io/prometheus-engine/prometheus:v2.35.0-gmp.5-gke.0).

For details about the changes included, see the [release page on GitHub](https://github.com/GoogleCloudPlatform/prometheus-engine/releases/tag/v0.7.0).

## May 26, 2023

Feature

**Observability for Google Kubernetes Engine** : The **Observability** tab for each of your GKE clusters now includes metrics for ephemeral storage. For more information, see [View observability metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics#metrics_for_clusters_and_workloads).

## May 17, 2023

Change

Cloud Monitoring now provides GA support to prevent alerting policies from sending notifications and creating incidents during specific time periods. For general information, see [Snooze notifications and alerts](https://cloud.google.com/monitoring/alerts/snooze). For information about how to create, view, and modify a snooze, see [Create and manage snoozes](https://cloud.google.com/monitoring/alerts/manage-snooze).

## May 15, 2023

Feature

Version 2.31.0 of the Ops Agent introduces preview support for an OpenTelemetry Protocol (OTLP) receiver. You can use this receiver to collect custom metrics and traces from applications written by using OpenTelemetry SDKs. For more information, see [Collect OTLP metrics and traces](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/otlp).

Change

The new interface for creating charts with Metrics Explorer is GA. For more information, see [Create charts with Metrics Explorer](https://cloud.google.com/monitoring/charts/metrics-explorer).

## May 12, 2023

Change

The new flow for creating uptime checks, which includes usability improvements and offers a seamless way to create uptime checks on your private resources, is now GA. For more information, see [Create public uptime checks](https://cloud.google.com/monitoring/uptime-checks) and [Create private uptime checks](https://cloud.google.com/monitoring/uptime-checks/private-checks).

## May 02, 2023

Feature

Observability for Google Kubernetes Engine: You can now enable GKE control plane metrics from the **Observability** tab for your GKE cluster. You can also preview the available charts and metrics before you enable the metrics. For more information, see [Configuring collection of control plane metrics](https://cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#enable-control-plane-metrics).

## April 26, 2023

Feature

Version 2.31.0 of the Ops Agent introduces built-in support for log rotation. For more information, see [Configure log rotation in the Ops Agent](https://cloud.google.com//stackdriver/docs/solutions/agents/ops-agent/rotate-logs#configure-log-rotation).

## April 25, 2023

Feature

The **Observability** tab on the **VM instances** page for Compute Engine has been enhanced. Disk and Network sections with additional charts have been added. The Integrations > Detected section lets you navigate to the dashboards for the third-party integrations, like Apache or NGINX, that you have configured. The page also includes a set of Recommended Alerts for setting up pre-configured alerting policies for CPU, memory, and disk utilization and for host errors.

## April 13, 2023

Change

Chart legends in select Cloud Monitoring pages have been updated. The default chart legend is simplified, with the option to expand the legend to view more details about your metrics. For more information, see [Configure legends](https://cloud.google.com/monitoring/charts/working-with-legends).

## April 05, 2023

Feature

A new interface for creating charts with Metrics Explorer is in Public Preview. For more information, see [Create charts with Metrics Explorer](https://cloud.google.com/monitoring/charts/metrics-explorer).

## April 03, 2023

Change

The time-range selector in select Cloud Monitoring pages has been updated to support a larger set of time range options, such as preset times, custom start and end times, and relative time ranges.

Feature

You can now configure metric-based alerting policies to send repeated notifications for open and acknowledged incidents. For more information, see [Send repeated notifications](https://cloud.google.com/monitoring/alerts/concepts-indepth#send-repeated-notifications).

## March 30, 2023

Change

The link for the **Managed Prometheus** page in Cloud Monitoring now goes to the PromQL tab on the **Metrics Explorer** page.

## March 24, 2023

Feature

**Google Cloud Managed Service for Prometheus** : You can use the OpenTelemetry Collector to scrape standard Prometheus metrics and report them to Managed Service for Prometheus. For more information, see [Get started with the OpenTelemetry Collector](https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-otel).

## March 10, 2023

Feature

You can now have Cloud Monitoring send an email that contains a dashboard URL to people or groups in your organization. For more information, see [Share dashboards](https://cloud.google.com/monitoring/charts/share-dashboards).

## March 08, 2023

Feature

You can now use the gcloud CLI to configure a snooze, which prevents Cloud Monitoring from sending notifications or creating incidents during specific time periods. You can also configure a snooze by using the Google Cloud console and the API. For more information see [Create and manage snoozes](https://cloud.google.com/monitoring/alerts/manage-snooze).

## March 06, 2023

Feature

You can now view and list incidents on your custom dashboards. For more information, see [Display incidents on a dashboard](https://cloud.google.com//monitoring/charts#add_incident_chart).

## February 17, 2023

Feature

You can now install pre-defined alerting policies for services integrated with Cloud Monitoring from the Monitoring **Integrations** page and from the **Observability** tab on the pages for Kubernetes Engine clusters and workloads. For more information about these installable policies, see [Install alerting policies](https://cloud.google.com/monitoring/agent/integrations#install-alertpols).

Change

To view details of your user-defined metrics, use the **Metrics diagnostics** page, which can now be accessed through the navigation pane of Cloud Monitoring. For more information, see [View information about your user-defined metrics](https://cloud.google.com/monitoring/custom-metrics/diagnostics).

## February 16, 2023

Feature

The Ops Agent now provides Preview support for NVIDIA GPU metrics, including metrics reported from the NVIDIA Management Library (NVML) and the Data Center GPU Manager (DCGM).

When you [install the GPU-enabled version of the Ops Agent](https://cloud.google.com/monitoring/agent/ops-agent/third-party-nvidia#install-oagent), NVML metrics are collected automatically. DGCM metrics are available as a third-party integration. For information about configuring the integration, see [NVIDIA Data Center GPU Manager](https://cloud.google.com/monitoring/agent/ops-agent/third-party-nvidia). The reference document for Ops Agent metrics includes tables for the [NVML metrics](https://cloud.google.com/monitoring/api/metrics_opsagent#agent-gpu) and the [DCGM metrics](https://cloud.google.com/monitoring/api/metrics_opsagent#agent-dcgm).

Feature

Version 2.25.1 of the Ops Agent introduces health checks. When the Ops Agent starts, it performs a series of checks for conditions that prevent the agent from running correctly. If the agent detects one of the conditions, it writes a message to its health-check log and exits. For more information, see [Find Ops Agent troubleshooting information](https://cloud.google.com/monitoring/agent/ops-agent/troubleshoot-find-info).

## February 15, 2023

Change

You can now configure uptime checks to include a user-defined content-type header. For more information, see the [`customContentType`](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#HttpCheck.FIELDS.custom_content_type) field of the `UptimeCheckConfig` structure.

## February 09, 2023

Change

The **Observability** tab is now available for GKE Deployments. To view the tab, navigate to the Kubernetes Engine **Workloads** page, click on the name of a Deployment, and then click the **Observability** tab.

## January 27, 2023

Feature

The Ops Agent version 2.25.0 supports a receiver for Prometheus metrics. By using this receiver, you can collect Prometheus metrics from applications running on Compute Engine instances. For more information, see [Collect Prometheus metrics](https://cloud.google.com/monitoring/agent/ops-agent/prometheus).

## January 25, 2023

Feature

Now the alerting policy can forecast, or predict, that the threshold will be violated within a configurable time window. These policies are designed to monitor constraint metrics like those that record quota, memory, and storage usage. Forecasting alerts is in Public Preview. For more information, see [Forecast condition](https://cloud.google.com/monitoring/alerts/types-of-conditions#forecast).

## January 20, 2023

Change

You can now use the **Observability** tab on the Compute Engine **VM instances** page to see the five virtual machines consuming the most of a resource. For more information, see [Troubleshooting VM performance issues](https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-performance#viewing-performance-metrics).

## January 10, 2023

Feature

**Managed Service for Prometheus** : Dashboards for exporter integrations are available and automatically installed when you configure the integration. You can also view static previews of dashboards without configuring the integration. For more information, see the exporter documentation at [Set up commonly used exporters](https://cloud.google.com/stackdriver/docs/managed-prometheus/exporters/introduction).

## January 09, 2023

Change

Charts defined by Prometheus Query Language (PromQL) now support dashboard-wide filters and can be configured to support template variables. For more information, see [Create a permanent filter](https://cloud.google.com/monitoring/charts/filter-dashboard#create-permanent-filter).

## December 14, 2022

Feature

You can now use the **Observability** tab on the Kubernetes Engine **Workloads** page to see the five workloads consuming the most of a resource. For more information, see [View cluster and workload observability metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics#view_metrics).

## December 13, 2022

Feature

You can use the new **Map** view on the **VM Instances** dashboard to visualize the health of the resources in your fleet. Using the map, you can group VMs by resource labels, like "instance group" or "zone", and color the VMs by the value of a metric, like CPU utilization, to highlight hotspots and anomalies in your fleet.

## December 12, 2022

Change

You can now use the Monitoring API to configure a snooze, which prevents Cloud Monitoring from sending notifications or creating incidents during specific time periods. You can also configure a snooze by using the Google Cloud console. For information about how to create, view, and modify a snooze, see [Create and manage snoozes](https://cloud.google.com/monitoring/alerts/manage-snooze).

## December 07, 2022

Change

For public and private uptime checks, a new create flow is available in Public Preview. For private uptime checks, the Public Preview flow lets you create the Service Directory service and perform other prerequisite steps by using the Google Cloud console. For more information, see [Create public uptime checks](https://cloud.google.com/monitoring/uptime-checks) and [Create private uptime checks](https://cloud.google.com/monitoring/uptime-checks/private-checks).

## November 11, 2022

Change

Prometheus Query Language (PromQL) for creating charts and dashboards in Cloud Monitoring is now Generally Available. For more information, see [PromQL in Cloud Monitoring](https://cloud.google.com/monitoring/promql).

Feature

Cloud Monitoring now provides a **GKE Clusters** dashboard for enabling Managed Service for Prometheus on clusters in your project. For more information, see [Get started with managed collection](https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).

## November 07, 2022

Feature

You can now dynamically include your log content in your alert notifications for easier troubleshooting. For more information about extracting log content into labels, see [Create a log-based alert (Monitoring API)](https://cloud.google.com/logging/docs/alerting/log-based-alerts#lba-by-api).

## November 03, 2022

Feature

You can now add table widgets to custom dashboards that let you limit the number of table rows, persiste specific columns, display only those rows with the highest, or lowest values, and that display a visual indicator of the value as compared to the range of possible values. For more information, see [Display data in tabular form on a dashboard](https://cloud.google.com/monitoring/charts#add_table).

## October 24, 2022

Feature

You can now instrument gRPC applications to use [Microservices observability](https://cloud.google.com/stackdriver/docs/solutions/grpc).

Pricing for Microservices observability is the same as [Cloud Operations Pricing](https://cloud.google.com/stackdriver/pricing). There are no separate charges for using Cloud Trace, Cloud Monitoring, or Cloud Logging Microservices observability plugins.

Change

A new version of Managed Service for Prometheus is now available. Version 0.5.0 of managed collection for Kubernetes has been released. Users who deploy managed collection using `kubectl` should [reapply the manifests](https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#config-mgd-collection). Users who deploy the service using `gcloud` or the GKE UI will be upgraded on a rolling basis over the coming weeks. This release has no impact on users of self-deployed collection.

For details about the changes included, see the [release page on GitHub](https://github.com/GoogleCloudPlatform/prometheus-engine/releases/tag/v0.5.0).

## October 21, 2022

Feature

The Cloud Monitoring **Integrations** page now provides access to logs collected by logs-enabled integrations from the **Details** page for each integration.

## October 20, 2022

Change

Logs panels now display log entries on rows with separate columns for severity, the timestamp, and a summary of the log entry. You can click the **View log details** button to view the JSON-formatted representation of a log entry. For more information, see [View logs on a custom dashboard](https://cloud.google.com/monitoring/charts/view-logs).

## October 13, 2022

Change

**SLO monitoring** : You can now define a set of generic services by using the Service Monitoring API. This change streamlines integration with tools like Terraform. For more information about defining generic services, see [Services](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#svc-structs).

## October 04, 2022

Feature

You can now collect Oracle Database logs and metrics from the Ops Agent, starting with version 2.22.0. For more information, see [Monitoring third-party applications: Oracle Database](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/oracledb).

## September 30, 2022

Feature

The set of pre-configured Monitoring dashboards now includes a **Microservices gRPC Overview** dashboard. If apps in your project emit [gRPC](https://github.com/census-instrumentation/opencensus-specs/blob/master/stats/gRPC.md#default-views) metrics, then this dashboard is automatically added to your list of available dashboards.

## September 28, 2022

Change

You can now collect additional PostgreSQL metrics from the Ops Agent, starting with version 2.21.0. For more information, see [Monitoring third-party applications: PostgreSQL](https://cloud.google.com/monitoring/agent/ops-agent/third-party/postgresql).

Change

You can now collect additional Elasticsearch metrics from the Ops Agent, starting with version 2.21.0. For more information, see [Monitoring third-party applications: Elasticsearch](https://cloud.google.com/monitoring/agent/ops-agent/third-party/elasticsearch).

## September 26, 2022

Feature

You can now use Prometheus Query Language (PromQL) when creating charts and dashboards in Cloud Monitoring. For more information, see [PromQL in Cloud Monitoring](https://cloud.google.com/monitoring/promql).

## September 13, 2022

Change

You can now configure public uptime checks to send ICMP pings as part of the check. The results of the pings are sent to Cloud Logging to help you troubleshoot failed checks. For more information, see [Use ICMP pings](https://cloud.google.com/monitoring/uptime-checks#ping).

## August 30, 2022

Change

You can now collect additional MongoDB metrics from the Ops Agent, starting with version 2.19.0. For more information, see [Monitoring third-party applications: MongoDB](https://cloud.google.com/monitoring/agent/ops-agent/third-party/mongodb).

## August 29, 2022

Feature

You can now manage Monitoring-specific roles by using the Cloud Monitoring pages in the Google Cloud console. For more information, see [Grant access to Cloud Monitoring](https://cloud.google.com/monitoring/access-control#grant-monitoring-access).

## August 25, 2022

Change

There are new filtering capabilities for the [`projects.uptimeCheckConfig.list`](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/list) API method. For more information, see [`UptimeCheckConfig`](https://cloud.google.com/monitoring/api/v3/sorting-and-filtering#uptimecheckconfig).

## August 17, 2022

Announcement

Cloud Monitoring is introducing pricing for uptime checks, effective October 1, 2022. For more information, see [Cloud Monitoring pricing summary](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary).

## August 15, 2022

Feature

The GKE **Clusters List** page now includes a new **Observability** tab that displays Monitoring data. This tab shows infrastructure health metric trends such as CPU, memory, container restarts and control-plane metrics. It also provides visibility into ingestion into Google Cloud Managed Service for Prometheus and Cloud Logging. For more information, see [View observability metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).

## August 11, 2022

Feature

You can now prevent Cloud Monitoring from sending notifications or creating incidents during specific time periods. For general information, see [Snooze notifications and alerts](https://cloud.google.com/monitoring/alerts/snooze). For information about how to create, view, and modify a snooze, see [Create and manage snoozes](https://cloud.google.com/monitoring/alerts/manage-snooze).

Change

You can now update older versions of the Ops Agent from the Cloud Monitoring **VM Instances** page and from the **Details** panel for a selected Compute Engine instance. The "Install" option for a new agent now also supports "update" for upgrading an older agent.

Change

The Cloud Monitoring **Integrations** page now provides information about integrations with other Google Cloud services, enhanced filtering, and additional information about available third-party integrations. For more information, see [Manage integrations](https://cloud.google.com/monitoring/agent/integrations).

## August 10, 2022

Change

You can now create uptime checks for Cloud Run public endpoints by using the [Monitoring API](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#UptimeCheckConfig.FIELDS.monitored_resource) and specifying the [Cloud Run Revision](https://cloud.google.com/monitoring/api/resources#tag_cloud_run_revision) monitored-resource type.

## August 09, 2022

Change

The organization of the SLO monitoring **Services Overview** page has been improved. The new layout provides a better experience when you don't yet have any services. When you have services, the new **Supported Services** list indicates how many of each type you have. You can also use the list to filter the services table to include all services of a selected type. For more information, see [Services Overview dashboard](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/svc-overview#svc-overview).

## July 29, 2022

Feature

You can now add table widgets to custom dashboards that let you limit the number of table rows, display only those rows with the highest, or lowest values, and that display a visual indicator of the value as compared to the range of possible values. For more information, see [Display data in tabular form on a dashboard](https://cloud.google.com/monitoring/charts#add_table).

## July 28, 2022

Change

You can now configure the acceptable response codes for public and private HTTP Uptime checks. For more information, see [Create public uptime checks](https://cloud.google.com/monitoring/uptime-checks).

Feature

You can now add user-defined labels to public and private Uptime checks. For more information, see [Create public uptime checks](https://cloud.google.com/monitoring/uptime-checks).

## July 26, 2022

Feature

You can now collect Aerospike metrics from the Ops Agent, starting with version 2.18.2. For more information, see [Monitoring third-party applications: Aerospike](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/aerospike).

Feature

You can now collect Couchbase logs and metrics from the Ops Agent, starting with version 2.18.2. For more information, see [Monitoring third-party applications: Couchbase](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/couchbase).

Feature

You can now collect Vault metrics from the Ops Agent, starting with version 2.18.2. For more information, see [Monitoring third-party applications: Vault](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/vault).

## July 19, 2022

Change

A new version of Managed Service for Prometheus is now available. Version 0.4.3-gke-0 of managed collection for Kubernetes has been released. Users who deploy managed collection using `kubectl` should [reapply the manifests](https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#config-mgd-collection). Users who deploy the service using `gcloud` or the GKE UI will be upgraded on a rolling basis over the coming weeks. This release has no impact on users of self-deployed collection.

For details about the changes included, see the [release page on GitHub](https://github.com/GoogleCloudPlatform/prometheus-engine/releases/tag/v0.4.3-gke.0).

## July 15, 2022

Feature

You can now collect SAP HANA logs and metrics from the Ops Agent, starting with version 2.18.1. For more information, see [Monitoring third-party applications: SAP HANA](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/saphana).

Feature

You can now collect Flink metrics from the Ops Agent, starting with version 2.18.1. For more information, see [Monitoring third-party applications: Flink](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/flink).

## July 14, 2022

Change

Log-based alerting is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Log-based alerts match on the content of your logs. When triggered, a log-based alert notifies you that a match has appeared in your logs and opens an incident in Cloud Monitoring. The minimum autoclose duration for incidents is now 30 minutes. For more information, see [Monitor your logs](https://cloud.google.com/logging/docs/alerting/monitoring-logs) and [Use log-based alerts](https://cloud.google.com/logging/docs/alerting/log-based-alerts).

## June 30, 2022

Feature

**Managed Service for Prometheus** : You can now query Cloud Monitoring metrics by using PromQL. For more information, see [Mapping Monitoring metric names to PromQL](https://cloud.google.com/stackdriver/docs/managed-prometheus/promql#transforming-names).

## June 28, 2022

Change

The new experience for creating metric-based alerting policies by using the Google Cloud console is now Generally Available. For more information, see [Create metric-based alert policy](https://cloud.google.com/monitoring/alerts/using-alerting-ui).

## June 24, 2022

Feature

You can now collect Jetty metrics from the Ops Agent, starting with version 2.17.0. For more information, see [Monitoring third-party applications: Jetty](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/jetty).

Feature

You can now view the configuration of charts on a dashboard while the dashboard is in read-only mode. For more information, see [Show the chart configuration](https://cloud.google.com/monitoring/charts/working-with-charts#view-config).

## June 03, 2022

Feature

You can now add, edit, and remove alerting policy user labels by using the Cloud console when you use the preview alerting interface. To configure policy labels, edit the policy and go to the **Notifications and name** step. For more information, see [Create an alerting policy](https://cloud.google.com/monitoring/alerts/using-alerting-ui#create-policy).

## May 26, 2022

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

## May 16, 2022

Change

The pricing for [Google Cloud Managed Service for Prometheus](https://cloud.google.com/stackdriver/docs/managed-prometheus) has been reduced by 25-50%, depending on volume and usage. Existing pricing tiers have been reduced by 25%, and a new high-volume tier has been added at 50% of the current cost. For pricing details, see [Cloud Monitoring pricing summary](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary), and for a set of examples, see [Pricing examples based on samples ingested](https://cloud.google.com/stackdriver/pricing#pricing_examples_samples).

## May 11, 2022

Change

Private uptime checks are now generally available. Private uptime checks enable HTTP requests into a customer Virtual Private Cloud (VPC) network while enforcing Identity and Access Management (IAM) restrictions and VPC Service Controls perimeters. Private uptime checks can send requests over the private network to resources like a virtual machine (VM) or an L4 internal load balancer (ILB).

For more information, see [Create private uptime checks](https://cloud.google.com/monitoring/uptime-checks/private-checks).

## May 06, 2022

Feature

You can now configure Metrics Explorer and charts on dashboards to display a ratio of metrics by using the Cloud Console. For more information, see [Ratios of metrics](https://cloud.google.com/monitoring/charts/metric-ratios).

## May 05, 2022

Change

**SLO monitoring** : Cloud Monitoring can now detect potential GKE- and Cloud Run-based services in your project. Monitoring provides a list of such candidate services, and you can now identify the candidates you want to monitor and create SLOs for them by using the Cloud Console. For more information, see [Defining a microservice](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/define-svc).

## April 14, 2022

Feature

You can now define template variables and permanent filters for your dashboards. For more information, see [Create a template variable or permanent filter](https://cloud.google.com/monitoring/charts/filter-dashboard#create-permanent-filter).

## March 28, 2022

Feature

User-defined labels are now included in PagerDuty, Pub/Sub, Webhooks, and email notifications, and you can also view these labels on the details pages of alerting policies and incidents. To learn how you can create user-defined labels that contain severity information and attach those labels to alerting policies or incidents, see [Add severity levels to an alerting policy](https://cloud.google.com/monitoring/alerts/labels).

## March 11, 2022

Feature

You can now collect WildFly metrics from the Ops Agent, starting with version 2.12.0. For more information, see [Monitoring third-party applications: WildFly](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/wildfly).

## March 04, 2022

Feature

You can now organize your dashboard widgets into collapsible groups. For more information, see [Organize dashboard widgets](https://cloud.google.com/monitoring/charts#organize_widgets).

## February 28, 2022

Change

**GA** : Google Cloud Managed Service for Prometheus, Google Cloud's fully managed, Prometheus-compatible monitoring solution, is now generally available. You can use the managed service anywhere that you use standard Prometheus today. The collector retains all expected Prometheus functionality, such as local storage and rule evaluation.

Managed Service for Prometheus also offers managed data collection in Kubernetes environments, reducing the complexity of deploying, scaling, sharding, configuring, and maintaining the collectors. For more information, see [Google Cloud Managed Service for Prometheus](https://cloud.google.com/stackdriver/docs/managed-prometheus/).

## February 22, 2022

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

Change

You can now configure how missing data is treated in alerting policies. Currently, if data stops arriving, the alerting policy repeats the previous measurement, so open incidents stay open. You can now treat missing data as violating the condition so an active condition stays active, or treat it as non-violating so that an active condition closes. For more information, see [Partial metric data](https://cloud.google.com/monitoring/alerts/concepts-indepth#partial-metric-data).

Breaking

The `install-monitoring-agent.sh` installation script for the Cloud Monitoring agent for Linux [has been decommissioned](https://cloud.google.com/stackdriver/docs/deprecations/mon-agent-install). See the [Installing the Cloud Monitoring agent](https://cloud.google.com/monitoring/agent/install-agent#joint-install) guide for the latest installation procedures.

## February 14, 2022

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

## February 08, 2022

Change

You can now configure private uptime checks by using the Cloud Console. For more information, see [Create private uptime checks](https://cloud.google.com/monitoring/uptime-checks/private-checks).

Feature

You can now view information about your user-defined metrics by using the **Diagnostics** tab located on the **Metrics Explorer** page. The **Diagnostics** tab displays summary information about the user-defined metrics your project injests, charts usage metrics, lists all user-defined metrics. You can use features on this page to create alerts, view audit logs, and get detailed information about individual metrics. For more information, see [View metric diagnostics](https://cloud.google.com/monitoring/custom-metrics/diagnostics).

## February 07, 2022

Feature

Using the new **Integrations** page in the Google Cloud console, you can now configure third-party application integrations that the [Ops Agent](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent) supports. The **Integrations** page provides links to install instructions, displays example dashboards, and lists the metrics and logs that the Ops Agent collects for each integration. For more information, see [Manage integrations](https://cloud.google.com/monitoring/agent/integrations)

## February 03, 2022

Feature

You can now save a copy of a chart on a predefined dashboard to one of your custom dashboards by selecting **Add to Custom Dashboard** from the **More Options** menu on the chart. When you select a custom dashboard, you also have the option of renaming the copied chart.

## February 01, 2022

Feature

You can now view SLOs on a custom dashboard. For more information, see [Display SLOs on a dashboard](https://cloud.google.com/monitoring/charts#add_slo_chart).

## January 26, 2022

Feature

You can now collect Apache Tomcat metrics and logs from the Ops Agent, starting with version 2.9.0. For more information, see [Monitoring third-party applications: Apache Tomcat](https://cloud.google.com/monitoring/agent/ops-agent/third-party/tomcat).

Feature

You can now collect PostgreSQL metrics and logs from the Ops Agent, starting with version 2.9.0. For more information, see [Monitoring third-party applications: PostgreSQL](https://cloud.google.com/monitoring/agent/ops-agent/third-party/postgresql).

## January 21, 2022

Change

Private uptime checks are now available in Preview. Private uptime checks enable HTTP requests into a customer Virtual Private Cloud (VPC) network while enforcing Identity and Access Management (IAM) restrictions and VPC Service Controls perimeters. Private uptime checks can send requests over the private network to resources like a virtual machine (VM) or an L4 internal load balancer (ILB).

For more information, see [Create private uptime checks](https://cloud.google.com/monitoring/uptime-checks/private-checks).

## January 18, 2022

Change

When you click on an entry in the **Instances** table on the Monitoring **VM Instances** dashboard, a sliding panel now appears with the instance details, replacing the **VM Instance Details** page.

## January 11, 2022

Change

Cloud Monitoring now supports configuring HTTP POST uptime checks in the UI. For more information, see [Managing uptime checks](https://cloud.google.com/monitoring/uptime-checks).

## January 07, 2022

Feature

You can now collect MariaDB metrics and logs from the Ops Agent, starting with version 2.8.0. For more information, see [Monitoring third-party applications: MariaDB](https://cloud.google.com/monitoring/agent/ops-agent/third-party/mariadb).

Feature

Starting with version 2.8.0, the Ops Agent supports Ubuntu 21.10. For more information, see [Linux operating systems](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#linux_operating_systems).

Feature

You can now collect Memcached metrics from the Ops Agent, starting with version 2.8.0. For more information, see [Monitoring third-party applications: Memcached](https://cloud.google.com/monitoring/agent/ops-agent/third-party/memcached).

Feature

You can now collect MySQL metrics from the Ops Agent, starting with version 2.8.0. For more information, see [Monitoring third-party applications: MySQL](https://cloud.google.com/monitoring/agent/ops-agent/third-party/mysql).

## December 15, 2021

Change

The Slack notification channel for alerting is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). You can now test your connection from Google Cloud when adding new Slack channels. The notification has been updated with the latest template and now includes your resource, system, and user labels. For more information, see [Creating channels](https://cloud.google.com/monitoring/support/notification-options#slack).

## December 14, 2021

Change

The Pub/Sub notification channel for alerting is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). You can now test your connection from Google Cloud when adding new Pub/Sub channels. For more information, see [Creating channels](https://cloud.google.com/monitoring/support/notification-options#pubsub).

## November 24, 2021

Change

The date on which pricing for Monitoring data ingested by using GKE workload metrics goes into effect has changed. [Pricing](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary) is now effective on February 1, 2022.

## November 18, 2021

Feature

Cloud Monitoring now supports dashboard-wide grouping and filtering. For more information, see [Dashboard-wide filters](https://cloud.google.com/monitoring/charts/filter-dashboard).

## November 15, 2021

Announcement

**Preview** : Google Cloud Managed Service for Prometheus, Google Cloud's fully managed, Prometheus-compatible monitoring solution, is now available in Preview. You can use the managed service anywhere that you use standard Prometheus today. The collector retains all expected Prometheus functionality, such as local storage and rule evaluation.

Managed Service for Prometheus also offers managed data collection in Kubernetes environments, reducing the complexity of deploying, scaling, sharding, configuring, and maintaining the collectors. For more information, see [Google Cloud Managed Service for Prometheus](https://cloud.google.com/stackdriver/docs/managed-prometheus/).

## November 11, 2021

Feature

You can now view the project-scoped log entries for all projects in a metrics scope on a custom dashboard. For more information, see [View logs on a dashboard](https://cloud.google.com/monitoring/charts/view-logs).

## November 08, 2021

Feature

You can now save a copy of a chart from the **Observability** tab on Compute Engine's **VM instance details** page to one of your custom dashboards. To save a copy of the chart, select **Add to Custom Dashboard** from the **More Options** menu on the chart. You then select a new or existing custom dashboard, and have the option of renaming the new copy of the chart.

Change

The API to manage the [metrics scope](https://cloud.google.com/monitoring/settings#concept-scope) of a Google Cloud project is now Generally Available. For more information, see [Manage metrics scopes with the API](https://cloud.google.com/monitoring/settings/manage-api).

Terraform now supports use of the metrics scope API. For sample code, see [`google_monitoring_monitored_project`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/monitoring_monitored_project).

## November 05, 2021

Feature

You can now collect Redis metrics from the Ops Agent, starting with version 2.7.0. For more information, see [Monitoring third-party applications: Redis](https://cloud.google.com/monitoring/agent/ops-agent/third-party/redis).

Feature

You can now collect Apache Web Server metrics from the Ops Agent, starting with version 2.7.0. For more information, see [Monitoring third-party applications: Apache Web Server](https://cloud.google.com/monitoring/agent/ops-agent/third-party/apache).

## November 04, 2021

Feature

You can now create an alerting policy from the alert chart dialog on a custom dashboard, and you can create an alerting policy by converting a chart on custom dashboard to an alert chart. For more information, see [Alert charts](https://cloud.google.com/monitoring/charts#add_alert_chart).

Change

Data from closed incidents is now retained for 13 months instead of 90 days, so you can see patterns over longer periods of time and investigate them. For information about investigating incidents, see [Incidents](https://cloud.google.com/monitoring/alerts/incidents-events).

## November 01, 2021

Feature

You can now collect Cassandra metrics from the Ops Agent, starting with version 2.6.0. For more information, see [Monitoring third-party applications: Cassandra](https://cloud.google.com/monitoring/agent/ops-agent/third-party/cassandra).

## October 04, 2021

Feature

GKE version 1.20.8-gke.2100 or later offers a [Preview](https://cloud.google.com/products#product-launch-stages) of a fully managed metric collection pipeline to scrape Prometheus-style metrics exposed by any GKE workload and send those metrics to Cloud Monitoring for dashboards, alerts, and SLOs. Compared to the Prometheus Stackdriver sidecar, this new pipeline is easy to set up, allows filtering to control cost, supports larger clusters, is fully managed, supports Autopilot and horizontal Pod autoscaling, and offers better pricing. Get started with [GKE workload metrics](https://cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#workload-metrics).

## September 30, 2021

Feature

Cloud Monitoring dashboards now support displays of data in tabular form. For information about this feature, see [Configure tables with the Cloud Console](https://cloud.google.com/monitoring/charts/index#add_table) and [Configure tables by using the API](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_a_table_widget).

## September 27, 2021

Feature

You can now install the Ops Agent on one or more Compute Engine VMs from the **Inventory** tab of the Monitoring **VM Instances** dashboard. The dashboard generates Cloud Shell commands you can use to install the Ops Agent (recommended) or the legacy agents (if needed) on the selected VMs.

## September 09, 2021

Feature

You can now collect JVM metrics from the Ops Agent, starting with version 2.2.0. For more information, see [Monitoring third-party applications: JVM](https://cloud.google.com/monitoring/agent/ops-agent/third-party/jvm).

## September 03, 2021

Feature

Cloud Monitoring now lets you configure how long Monitoring waits to close an incident when observations stop arriving. For more information, see [Closing incidents](https://cloud.google.com/monitoring/alerts/incidents-events#closing).

## August 31, 2021

Feature

You can now collect nginx metrics and logs from the Ops Agent, starting with version 2.1.0. For more information, see [Monitoring third-party applications: nginx](https://cloud.google.com/monitoring/agent/ops-agent/third-party/nginx).

## August 30, 2021

Feature

The **VM Instances** page features enhanced scorecards for VM health. The new scorecards now include both "maintenance" and "system" events that might affect your VMs and agents, along with other metrics and statistics about the health of your VMs. The filtering and sorting of the **Inventory** table have also been enhanced.

## August 18, 2021

Feature

You can now use Chef to install and manage the [Google Cloud operations suite agents](https://cloud.google.com/stackdriver/docs/solutions/agents) across your fleet of Linux and Windows VMs. For more information, refer to the [Chef Integration](https://github.com/GoogleCloudPlatform/google-cloud-ops-agents-chef/blob/master/README.md) documentation.

## August 12, 2021

Change

Cloud Monitoring now supports creating an uptime check against a Kubernetes LoadBalancer Service hosted on GKE. For more information, see [Managing uptime checks](https://cloud.google.com/monitoring/uptime-checks).

## August 09, 2021

Feature

When you create a line chart on a dashboard, you can now specify whether the selected metric is charted against the left Y-axis or the right Y-axis. This feature lets you display different metrics with different scales on the same chart. For an API example, see [Dashboard with an `XyChart` and a threshold](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_an_xychart_and_a_threshold).

## August 05, 2021

Feature

A new UI for creating alerting policies is available in Preview. This interface offers fine-grained control over the selection of the metrics used in alerting conditions. See [Managing Alerting Policies](https://cloud.google.com/monitoring/alerts/using-alerting-ui) for more information.

Change

The **Processes** tab in the **VM instances** page is now Generally Available. This tab adds charts for [process metrics](https://cloud.google.com/monitoring/api/metrics_agent#agent-processes) to the charts provided by the existing **CPU** , **Memory** , **Disk** , and **Network** tabs.

## August 02, 2021

Feature

The API to manage the [metrics scope](https://cloud.google.com/monitoring/settings#concept-scope) of a Google Cloud project is now in Preview. For more information, see [Manage metrics scopes with the API](https://cloud.google.com/monitoring/settings/manage-api).

Feature

You can now use Puppet to install and manage the [Google Cloud operations suite agents](https://cloud.google.com/stackdriver/docs/solutions/agents) across your fleet of Linux and Windows VMs. For more information, refer to the [Puppet Integration](https://github.com/GoogleCloudPlatform/google-cloud-ops-agents-puppet/blob/master/README.md) documentation.

## July 29, 2021

Change

Monitoring Query Language (MQL) no longer requires you to use strict form when you create MQL-based alerting policies by using the Monitoring API. You can now provide queries in concise form. The query is stored as you provide it; concise queries are not converted to strict form.

## July 26, 2021

Feature

The new **External HTTP(S) Load Balancers** dashboard in Monitoring provides powerful visualizations to help you understand and troubleshoot connectivity issues on your external load balancers.

## July 13, 2021

Change

Metrics Explorer, a stand-alone charting tool that lets you quickly chart and explore time-series data, has a new interface and supports enhanced aggregation options. For more information, see [Metrics Explorer](https://cloud.google.com/monitoring/charts/metrics-explorer).

Feature

The **VM instances** page has a new **Processes** tab in Preview. This tab adds charts for [process metrics](https://cloud.google.com/monitoring/api/metrics_agent#agent-processes) to the charts provided by the existing **CPU** , **Memory** , **Disk** , and **Network** tabs.

## July 12, 2021

Change

A warning annotation is now added to charts when they are missing data due to a data outage. When the annotation is absent, data gaps aren't due to a data outage. For common reasons why a chart might contain a data gap, see [Gaps in chart data](https://cloud.google.com/monitoring/charts/troubleshooting-charts#gaps).

Feature

You can now install the Logging and Monitoring agents on multiple VMs from the **Inventory** tab on the Cloud Monitoring **VM Instances** page. You can select multiple VMs in your fleet for agent installation. The page generates the necessary installation command and provides a link to Cloud Shell, where you can run the command.

## July 07, 2021

Feature

**Preview** : Cloud Logging now supports alerts based on matching the content of your logs. When triggered, a log-based alert notifies you that a match has appeared in your logs and opens an incident in Cloud Monitoring. You can create log-based alerts by using the Logs Explorer or the Monitoring API. For more information, see [Monitoring your logs](https://cloud.google.com/logging/docs/alerting/monitoring-logs) and [Using log-based alerts](https://cloud.google.com/logging/docs/alerting/log-based-alerts).

## July 02, 2021

Change

Dashboard-wide filters now apply to all charts on a dashboard. Prior to this change, these filters didn't apply to MQL-configured charts.

Feature

You can now display summaries of single-condition alerting policies on a custom dashboard. A policy summary includes a display of the monitored time series, the threshold, and chips that show the number of open incidents and whether the policy is disabled. For more information about Alert charts, see the following pages:

  * [Managing dashboards by API](https://cloud.google.com/monitoring/dashboards/api-dashboard)
  * [Adding an alerting policy to a dashboard by using the Cloud Console](https://cloud.google.com/monitoring/alerts/using-alerting-ui#viewing_policies).



## June 30, 2021

Feature

The Monitoring dashboards page in the Cloud Console now includes a collection of sample dashboards. The sample dashboards provide support for many common applications. You can preview, install, and then customize these dashboards. For more information, see [Installing sample dashboards](https://cloud.google.com/monitoring/dashboards/dashboard-templates).

Change

The Ops Agent is now Generally Available as version 2.0.0. This agent combines logging and metrics into a single agent. The Ops Agent is targeted toward specialized logging workloads that require higher throughput and improved resource efficiency.

For installation information, see [Installing the Ops Agent](https://cloud.google.com/monitoring/agent/ops-agent/install-index). For information about migrating from an earlier version, see the [transition guide](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/transition).

The GA version of the Ops Agent can be configured to collect specific sets of metrics, as described in [Configuring the Ops Agent](https://cloud.google.com/monitoring/agent/ops-agent/configuration). There is a small number of metrics that the GA version of the Ops Agent handles differently from the Preview versions of the Ops Agent and the Monitoring agent; see [Differences in metric collection](https://cloud.google.com/monitoring/api/metrics_agent#metric-agent-diffs).

## June 28, 2021

Change

The **Incidents** page now provides an option to permanently close incidents if no data for that incident has arrived in the most recent alerting period. For more information, see [Closing incidents](https://cloud.google.com/monitoring/alerts/incidents-events#closing_incidents).

Feature

Cloud Monitoring is launching a new **Observability** tab on Compute Engine's **VM instance details** page. This tab replaces the **Monitoring** tab. The enhanced **Observability** tab provides access to logs and greater visibility into CPU, disk, and network metrics.

## June 15, 2021

Change

You can now view Monitoring data for certain logs, such as Google Kubernetes Engine logs, in the Logs Explorer. For more information, see [Viewing Monitoring data](https://cloud.google.com/logging/docs/view/logs-viewer-interface#monitoring_data).

## June 01, 2021

Feature

A JSON editor has been integrated with the dashboard page. In addition to using the JSON editor to change the contents of the dashboard, you can save the current dashboard definition to a local system, and you can upload a dashboard definition to your Google Cloud project. For more information, see [Managing dashboards through the Cloud Console](https://cloud.google.com/monitoring/charts/dashboards).

## May 12, 2021

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



## May 05, 2021

Feature

Cloud Monitoring has added new ways to interact with charts. You can now select a range of lines displayed on chart, shift the time axis by using your pointer, and have new controls to expand the chart around a specific point in time. Charts displaying distribution data include 50th, 95th, and 99th percentile lines as an optional overlay. For more information, see [Exploring charted data](https://cloud.google.com/monitoring/charts/working-with-charts).

## May 04, 2021

Change

The Query Editor for Monitoring Query Language (MQL) has been reimplemented. In addition to autocompletion and error detection, it now supports code folding and a find-and-replace capability. For more information, see [Using the Query Editor](https://cloud.google.com/monitoring/mql/query-editor).

## May 03, 2021

Feature

The **Inventory** tab on the Cloud Monitoring **VM Instances** dashboard now offers the ability to filter and sort the instance table by any combination of columns. In addition, new health scorecards report a variety of metrics and statistics related to the health and status of your VMs and agents.

## April 27, 2021

Feature

You can now install the [Cloud Logging agent](https://cloud.google.com/logging/docs/agent), [Cloud Monitoring agent](https://cloud.google.com/monitoring/agent), and [Ops Agent](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent) on VMs running OpenSUSE Leap versions 15, 15.1, and 15.2.

## April 19, 2021

Change

Cloud Monitoring [Workspaces](https://cloud.google.com/monitoring/workspaces) are changing. Over the next few weeks, new capabilities are being deployed:

  * A Cloud Monitoring Workspace will be created automatically for a Google Cloud project. This change replaces the manual creation process.
  * The restriction that you can view the metrics for a project from only one Workspace is being eliminated. You'll be able to view the metrics for a project from multiple Workspaces.
  * Navigation to a Workspace that manages metrics from multiple projects is changing. For information on this change, see [Navigating to a Workspace](https://cloud.google.com/monitoring/settings#navigation).



## April 16, 2021

Feature

The Cloud Operations for GKE monitoring dashboard now allows you to manage and display service-level objectives (SLOs) that you define for your applications. For more information, see the **Managing SLOs** section of the [Observing your GKE clusters](https://cloud.google.com/stackdriver/docs/solutions/gke/observing#managing_slos) guide.

## April 15, 2021

Feature

The Cloud Operations for GKE monitoring dashboard now includes a column called **Error logs** that displays the number of error logs associated with an entity based on the selected time range. You can also select which columns to display in the tables. For more information, see the **Configuring the dashboard tables** section of the [Observing your GKE clusters](https://cloud.google.com/stackdriver/docs/solutions/gke/observing#configure-tables) guide.

Change

Compute Engine's **Instance Groups Monitoring** tab now includes charts for your managed instance groups. Charted metrics include group size, CPU utilization, disk I/O, and more. You can select the time window for the charts and view the corresponding logs from the integrated logs viewer panel. You can also use the links on each chart to create alerting policies or to analyze the data in Metrics Explorer.

## April 13, 2021

Feature

The Cloud Operations for GKE monitoring dashboard now provides a **Metrics** tab in the resource details panel. This tab also includes a menu option to create a new alert policy. For more information, see [Observing your GKE clusters](https://cloud.google.com/stackdriver/docs/solutions/gke/observing).

## April 12, 2021

Feature

The Cloud Operations for GKE monitoring dashboard now provides an **Alerts** tab in the resource details panel. This tab also includes a link to create a new alert policy. For more information, see [Observing your GKE clusters](https://cloud.google.com/stackdriver/docs/solutions/gke/observing).

Change

The dashboard save feature now displays the date and time of the last save operation. You can also disable and enable autosave. For more information, see [Configuring dashboards](https://cloud.google.com/monitoring/charts/dashboards#configuring_dashboards).

## April 09, 2021

Change

For new alerts created through the Cloud Console, the default behavior is to send a notification only when the incident is created. For alerts created by using the API, the default behavior is to send notifications when incidents are opened and closed. For all alerts, the alert's **Policy detail** page displays when notifications are sent. To change this behavior, you must use the Cloud Console to edit the policy. For more information, see [Managing Policies](https://cloud.google.com/monitoring/alerts/using-alerting-ui#managing_policies).

## April 08, 2021

Feature

The Google Cloud [Ops Agent](https://cloud.google.com/stackdriver/docs/solutions/ops-agent) is now available in Preview. This agent combines logging and metrics into a single agent that is targeted toward specialized logging workloads that require higher throughput and improved resource efficiency. It supports both Linux and Windows Compute Engine VMs.

Feature

Cloud Operations now offers the ability to install the Google Cloud Ops Agent via [Ansible](https://github.com/GoogleCloudPlatform/google-cloud-ops-agents-ansible) on Linux and Windows Compute Engine VMs.

Feature

Cloud Operations now offers the ability to provision the Google Cloud Ops Agent via [Terraform](https://registry.terraform.io/modules/terraform-google-modules/cloud-operations/google/latest/submodules/agent-policy) on Linux and Windows Compute Engine VMs.

## March 04, 2021

Feature

Compute Engine's **VM Instances** dashboard now provides an **Operations** menu. The "View metrics" menu option brings you to the **Infrastructure summary** dashboard in Monitoring. The "View logs" menu option brings you to the **Logs Explorer** page in Logging.

Feature

Kubernetes Engine's **Clusters** and **Workloads** dashboards now provide an **Operations** menu. The "View metrics" menu option brings you to the **GKE Dashboard** in Monitoring. The "View logs" menu option brings you to the **Logs Explorer** page in Logging.

Change

Compute Engine's **VM instance details** page now offers a guided installation path for the [Monitoring agent](https://cloud.google.com/monitoring/agent) when it is not detected on the VM.

## February 19, 2021

Feature

The **Incident details** page has been completely revised, making it easier to investigate and manage incidents. New features include a timeline of incidents, the addition of a chart with time-range controls and a link to Metrics Explorer, a log for recording the investigative history. For more information, see [Investigating incidents](https://cloud.google.com/monitoring/alerts/incidents-events#details-page).

## January 26, 2021

Feature

The `gcloud` commands for [managing Agent Policies](https://cloud.google.com/stackdriver/docs/solutions/managing-agent-policies) are now available in beta. For more information, refer to the [`gcloud` documentation for Agent Policies](https://cloud.google.com/sdk/gcloud/reference/beta/compute/instances/ops-agents/policies).

## December 23, 2020

Change

Alerting is now Generally Available for Monitoring Query Language (MQL). For more information, see [Alerting policies with MQL](https://cloud.google.com/monitoring/mql/alerts).

## December 16, 2020

Change

The dashboard editor that lets you create and edit all dashboard widget types, including gauges, scorecards, and text boxes, is now Generally Available. With this editor, you can quickly configure dashboard widgets by using Basic Mode, you can access all aggregation options with Advanced Mode, and you can use Monitoring Query Language when you select MQL Mode. When you set the dashboard layout to mosaic mode, you can resize and reposition widgets. For more information, see [Custom dashboards](https://cloud.google.com/monitoring/charts/dashboards#custom_dashboards).

## December 04, 2020

Announcement

Slack notification channels: All notification channels created before November 20 have been fixed, and new notification channels will be created correctly. Notification channels created between November 21 and December 3 need to be manually updated, as described in [Adding the Monitoring app to a Slack channel](https://cloud.google.com/monitoring/support/notification-options#slack-add-app).

## November 25, 2020

Announcement

If you created Slack notification channels after November 20, 2020, your channels are not receiving notifications. For information about resolving this issue, see [Adding the Monitoring app to a Slack channel](https://cloud.google.com/monitoring/support/notification-options#slack-add-app).

## November 16, 2020

Feature

A new dashboard editor is available in Preview. The new editor lets you create and edit all dashboard widget types, including gauges, scorecards, and text boxes. With mosaic-mode, you can resize and reposition widgets. The configuration tabs - Basic, Advanced, MQL - let you choose how you want to configure your widgets. For more information, see [Custom dashboards](https://cloud.google.com/monitoring/charts/dashboards#custom_dashboards).

## November 12, 2020

Change

Compute Engine's **VM instance details** page now displays "Memory Utilization" and "Disk Space Utilization" charts. In addition, a new "Monitor VM Instances" link lets you go directly to the [**VM instances** dashboard](https://console.cloud.google.com/monitoring/dashboards/resourceList/gce_instance) in Cloud Monitoring.

## November 09, 2020

Change

Monitoring Query Language (MQL) adds Preview support for macros. For more information, see [MQL macros](https://cloud.google.com/monitoring/mql/query-language#ql-macros).

## November 05, 2020

Feature

Enhancements to the **VM Details** page. A new **Event Timeline** shows important events as bars on a timeline. Hovering over any event bar displays summary information about the event and provides a link to the **Incident Details** page for the event.

## October 26, 2020

Feature

Enhancements to the pre-configured Monitoring **VM Instances** dashboard. The inventory table now includes a **Logging Agent Status** column, and the Logging agent can be installed by using a UI workflow from the table.

## October 15, 2020

Feature

The [Ops Agent](https://cloud.google.com/stackdriver/docs/solutions/ops-agent) is now available in Preview. Ops Agent provides a single agent to collect logs and metrics on Compute Engine instances.

Note that the Ops Agent uses new configuration files that are not compatible with the standalone Cloud Monitoring and Cloud Logging agents.

## October 05, 2020

Feature

Alerting is now available for Monitoring Query Language (MQL). For more information, see [Alerting policies with MQL](https://cloud.google.com/monitoring/mql/alerts).

## September 09, 2020

Change

The API for creating and managing alerting policies is now Generally Available. For information on using this API, see [Managing alerting policies by API](https://cloud.google.com/monitoring/alerts/using-alerting-api).

## August 28, 2020

Feature

Cloud Trace exemplars can now be viewed in Cloud Monitoring. For more information about Trace exemplars, see [Cloud Trace exemplars](https://cloud.google.com/trace/docs/setup#create-exemplars). For more information about viewing exemplars, see [Exploring charted data](https://cloud.google.com/monitoring/charts/working-with-charts).

## August 13, 2020

Feature

The new, out-of-the-box **Infrastructure Summary** dashboard for Compute Engine VMs provides a single-pane-of-glass view into your VM fleet and load balancers. At a glance, you can see the top 5 VMs across a variety of key metrics including memory, CPU, sent/received traffic, latency, disk read/write, and more.

## August 12, 2020

Feature

Enhancements to the pre-configured Monitoring **VM Instances** dashboard. The inventory table now includes a **Monitoring Agent Status** column, and the Monitoring agent can be installed by using a UI workflow from the table. The **Explore** tab gives an overview of additional metrics being sent (including agent metrics, custom metrics, and logs-based metrics) as well as a set of quick links to learn more about each type of metric. You can also use the **Recommended Alerts** button on the dashboard to configure fleet-wide alerts.

## July 10, 2020

Feature

SLO monitoring for microservices is now Generally Available in the Cloud Console. This feature lets you create service-level objectives (SLOs) and set up alerting policies to monitor their performance using auto-generated dashboards with metrics, logs, and alerts in a single place. For more information, see [SLO monitoring](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring).

## July 07, 2020

Change

Monitoring Query Language (MQL) is now Generally Available for querying data and creating charts. MQL is an expressive, text-based interface to Cloud Monitoring time-series data. With MQL, you can create charts you can't create any other way. You can access MQL from both the Cloud Console and the Monitoring API. For more information, see [Introduction to Monitoring Query Language](https://cloud.google.com/monitoring/mql/).

## June 15, 2020

Change

The Service Monitoring API is now Generally Available. You can use this feature to create services, set service-level objectives (SLOs), and create alerting policies to monitor your SLOs. See [Service monitoring](https://cloud.google.com/monitoring/service-monitoring/) for documentation, and [`services`](https://cloud.google.com/monitoring/api/v3/#service-monitoring) for reference material.

## June 08, 2020

Feature

Enhancements to the pre-configured Compute Engine **VM Instances** dashboard. Compute Engine cross-fleet metrics and detail views specific to CPU, Disk, Memory, and Network are now available. Use filters to narrow down the set of VMs being inspected, and use the time selector or in-chart time selection to change the time window. VMs with the Monitoring agent installed get detailed memory and disk analysis out of the box.

## May 20, 2020

Feature

Cloud Monitoring introduces an improved experience for viewing and managing incidents. Improvements include performance optimizations for Workspaces with large numbers of incidents, summary statics, and the ability to filter by alerting policy name, metric type, and resource type. For more information, see [Incidents and events](https://cloud.google.com/monitoring/alerts/incidents-events).

## May 19, 2020

Change

Alert notifications delivered by email now come from "alerting-noreply@google.com" instead of "alerts@stackdriver.com".

## May 14, 2020

Change

Starting in version 6.0.2, the Cloud Monitoring agent is available for the Ubuntu LTS 20.04 (Focal Fossa) distribution.

## May 08, 2020

Feature

Monitoring Query Language (MQL) is now available in Beta. MQL is an expressive, text-based interface to Cloud Monitoring time-series data. With MQL, you can create charts you can't create any other way. You can access MQL from both the Cloud Console and the Monitoring API. For more information, see [Introduction to Monitoring Query Language](https://cloud.google.com/monitoring/mql/).

## April 28, 2020

Deprecated

The `stack-install.sh` and the `install-monitoring-agent.sh` installation scripts for the Cloud Monitoring agent for Linux [are deprecated](https://cloud.google.com/stackdriver/docs/deprecations/mon-agent-install). Refer to the [Installing the Cloud Monitoring agent](https://cloud.google.com/monitoring/agent/install-agent#joint-install) guide for the latest installation procedures.

Deprecated

The 5.x version of the Cloud Monitoring agent for Linux is deprecated. Users are encouraged [to upgrade their agents](https://cloud.google.com/monitoring/agent/install-agent#upgrade) as soon as possible.

## March 30, 2020

Feature

You can now write time-series data for custom and Prometheus metrics at the rate of 1 data point every 10 seconds. This was previously limited to 1 point every minute.

Change

Data for custom and Prometheus metrics is now retained for 24 months. Previously, the retention period was 6 weeks.

## February 24, 2020

Feature

Stackdriver Monitoring agent version 6.0.0 is now available for the following distributions:

  * CentOS 7
  * Ubuntu LTS 16.04 (Xenial Xerus) and Ubuntu LTS 18.04 (Bionic Beaver)
  * Ubuntu Minimal LTS 16.04 (Xenial Xerus) and Ubuntu Minimal LTS 18.04 (Bionic Beaver)
  * Amazon Linux AMI (except Amazon Linux 2.0 AMI)



Change

Stackdriver Monitoring is available exclusively in the Cloud Console. For more information, see [Monitoring in the Google Cloud console](https://cloud.google.com/monitoring/docs/monitoring_in_console).

## February 19, 2020

Feature

Starting in version 6.0.0, the Stackdriver Monitoring agent is available for the Ubuntu 19.10 (Eoan Ermine) distribution.

## February 18, 2020

Feature

Stackdriver Monitoring agent version 6.0.0 is now available for the Debian 9 distribution.

## February 14, 2020

Feature

You can now send notifications from your alerting policies to Cloud Pub/Sub topics. For more information, see [Notification options](https://cloud.google.com/monitoring/support/notification-options).

Change

The Stackdriver Monitoring Dashboard API is now Generally Available. You can use this feature to programmatically manage your dashboards and charts. See [Managing dashboards by API](https://cloud.google.com//monitoring/dashboards/api-dashboard) for documentation, and [`Dashboard`](https://cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards) for reference material.

## February 11, 2020

Feature

Stackdriver Monitoring agent version 6.0.0 has been released to the CentOS 8 distribution.

## February 06, 2020

Feature

Starting in version 6.0.0, the Stackdriver Monitoring agent is available for the Debian 10 distribution.

## January 31, 2020

Feature

Stackdriver Monitoring Agent version 6.0.0 is now available, and the release will gradually roll out to the various Linux distributions. This version is built on a [fork of `collectd` version 5.8.1](https://github.com/Stackdriver/collectd) and includes the following changes:

  * drops support for [various third-party integrations](https://cloud.google.com/stackdriver/docs/deprecations/third-party-apps).
  * changes the file path for configuring an HTTP proxy when [installing the agent](https://cloud.google.com/monitoring/agent/install-agent#joint-install).



Feature

Stackdriver Monitoring agent version 6.0.0 is now available for the SUSE and SUSE Linux Enterprise Server (SLES) Linux distributions.

## January 13, 2020

Change

Stackdriver Monitoring in the Cloud Console is Generally Available and is the default option. For a limited period of time, you also have the option to use the classic Stackdriver Monitoring Console. Your configuration information, such as uptime checks and alerting policies, is accessible and changeable, from the Cloud Console and from the classic Stackdriver Monitoring Console. For more information, see [Monitoring in the Google Cloud console](https://cloud.google.com/monitoring/docs/monitoring_in_console).

## December 13, 2019

Change

Google Kubernetes Engine (GKE) version 1.15, which is now generally available, drops support for GKE versions 1.12 and earlier. As a result, the beta version of Stackdriver Kubernetes Engine Monitoring is no longer supported. If your GKE clusters are running version 1.12 or earlier, then you must upgrade them as soon as possible.

## December 11, 2019

Deprecated

Legacy Stackdriver support for Google Kubernetes Engine (GKE) is deprecated. If you're using Legacy Stackdriver, then you must [migrate to Stackdriver Kubernetes Engine Monitoring](https://cloud.google.com/monitoring/kubernetes-engine/migration) before Legacy Stackdriver is decommissioned. For more information, see [Legacy Stackdriver support for GKE deprecation](https://cloud.google.com/stackdriver/docs/deprecations/legacy).

## December 09, 2019

Feature

The Stackdriver Monitoring Dashboard API is now in Beta release. You can use this feature to programmatically manage your dashboards and charts. See [Managing dashboards by API](https://cloud.google.com//monitoring/dashboards/api-dashboard) for documentation, and [`Dashboard`](https://cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards) for reference material.

## December 04, 2019

Feature

Stackdriver Monitoring in the Cloud Console is in beta release. Your configuration information, such as uptime checks and alerting policies, is accessible and changeable, from the Cloud Console and from the classic Stackdriver Monitoring Console. For more information about the beta, see [Monitoring in the Google Cloud console](https://cloud.google.com/monitoring/docs/monitoring_in_console).

## November 14, 2019

Feature

The Service Monitoring API is now in Beta release. You can use this feature to create services, set service-level objectives (SLOs), and create alerting policies to monitor your SLOs. See [Service monitoring](https://cloud.google.com/monitoring/service-monitoring/) for documentation, and [`services`](https://cloud.google.com/monitoring/api/v3/#service-monitoring) for reference material.

## September 10, 2019

Change

When creating a new Google Kubernetes Engine (GKE) cluster, Stackdriver Kubernetes Engine Monitoring is now the default Stackdriver support option. This is a change from prior versions where Stackdriver Logging and Stackdriver Monitoring were the default Stackdriver support option. For more information, see [Overview of Stackdriver support for GKE](https://cloud.google.com/monitoring/kubernetes-engine/).

## August 08, 2019

Feature

[Stackdriver Monitoring](https://cloud.google.com/monitoring/uptime-checks) has two new uptime check features: SSL certificate validation and regex negation content matching.

## May 21, 2019

Feature

[Stackdriver Kubernetes Engine Monitoring](https://cloud.google.com/monitoring/kubernetes-engine/) is now generally available. Users of the legacy Stackdriver support for [monitoring](https://cloud.google.com/monitoring/kubernetes-engine/legacy-stackdriver/monitoring) and [logging](https://cloud.google.com/monitoring/kubernetes-engine/legacy-stackdriver/logging) for Google Kubernetes Engine are encouraged to [migrate to Stackdriver Kubernetes Engine Monitoring](https://cloud.google.com/monitoring/kubernetes-engine/migration) as soon as possible.

## May 02, 2019

Feature

Stackdriver Workspace creation is now a one-step operation.

## April 23, 2019

Feature

The OpenCensus library is now generally available as the official library for user-defined metrics in Stackdriver Monitoring. The [Custom metrics with OpenCensus](https://cloud.google.com/monitoring/custom-metrics/open-census) page includes samples in Go, Java, Node.js, and Python.

## March 18, 2019

Feature

The [Uptime Configuration API](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs) is now complete and GA. The API, part of the [Stackdriver Monitoring API](https://cloud.google.com/monitoring/api/ref_v3/rest/), lets you create, edit, and manage [uptime checks](https://cloud.google.com/monitoring/uptime-checks/).

## March 15, 2019

Change

Stackdriver agents are subject to an updated [deprecation policy](https://cloud.google.com/stackdriver/docs/agent-deprecation-policy). As part of this transition, the next major version of the Stackdriver Monitoring and Stackdriver Logging agents will stop supporting operating systems that are at the end of their lifecycle, as well as some [third-party agent plugins](https://cloud.google.com/monitoring/agent/plugins/).

## February 08, 2019

Feature

The Stackdriver Monitoring Agent now supports Ubuntu 18.04 LTS ("Bionic Beaver").

## December 06, 2018

Change

A mechanism to collect monitoring data from Prometheus clients, which can be deployed as a sidecar in the same Kubernetes pod as a working Prometheus server, is now available. See [Using Prometheus](https://cloud.google.com/monitoring/kubernetes-engine/prometheus) for more information.

## December 05, 2018

Feature

Documentation for using [OpenCensus](https://opencensus.io) to capture custom metrics in Java applications is now available. See [Custom metrics with OpenCensus](https://cloud.google.com/monitoring/custom-metrics/open-census) for more information.

## November 16, 2018

Change

The new UI for creating alerting policies is now complete and Generally Available. This interface, based on Metrics Explorer, offers fine-grained control over the selection of the metrics used in alerting conditions. See [Managing Alerting Policies](https://cloud.google.com/monitoring/alerts/using-alerting-ui) for more information.

## October 10, 2018

Feature

A new UI for creating alerting policies is available in Beta. This interface, based on Metrics Explorer, offers fine-grained control over the selection of the metrics used in alerting conditions. See [Managing Alerting Policies](https://cloud.google.com/monitoring/alerts/using-alerting-ui) for more information.

## September 19, 2018

Change

[Stackdriver Kubernetes Monitoring](https://cloud.google.com/monitoring/kubernetes-engine/) (Beta) for Kubernetes version 1.10.6 and above, restores the managed support for Kubernetes Monitoring. You can also [upgrade your existing clusters](https://cloud.google.com/stackdriver/docs/solutions/gke/installing#migrating) to this release, no matter which (if any) Stackdriver support they had before. Note the warnings about [incompatibilities](https://cloud.google.com/monitoring/kubernetes-engine/migration) between the old and new Stackdriver support.

## September 18, 2018

Feature

The legends for Stackdriver charts have been significantly improved. Legends now support more than one labeled column. The legend provides a selected set of columns as a default, but users can choose the columns they want to see in the legend. All columns are sortable. The legend detects a configuration of columns that exceeds the available space, and provides scrollbars. The resizing of the legends is also improved. For details, see [Configuring Legends](https://cloud.google.com/monitoring/charts/working-with-legends).

## September 10, 2018

Change

"Stackdriver accounts" have been renamed "Workspaces" to reflect their use as a "single pane of glass" through which you view resources from multiple projects and AWS accounts. There is no change in their functionality, but we have improved the documentation for them.

## June 29, 2018

Change

On July 1, 2018 at 00:00 PDT, Stackdriver switches to consumption-based pricing. For more information, see [Stackdriver Pricing](https://cloud.google.com/stackdriver/pricing_v2).

## June 19, 2018

Feature

If you want to minimize the **AWS permissions** you give to Stackdriver, then see [Minimal AWS Permissions](https://cloud.google.com/monitoring/support/minimal-aws-permissions).

## June 18, 2018

Change

**Between June 18, 2018 at 06:00 PDT and July 1, 2018 at 00:00 PDT, your use of Stackdriver is free**. The service tiers have been removed, and you can experience all features without incurring costs. Thereafter, Stackdriver switches to consumption-based pricing. For more information, see [Upcoming Pricing](https://cloud.google.com/stackdriver/pricing_v2).

## May 24, 2018

Change

Any Stackdriver free trials created after May 29, 2018 will expire on June 30, 2018. After June 30, 2018, free trials will be replaced with a free monthly allocation of logs and metrics. For more information about Stackdriver's new consumption-based pricing, see [Stackdriver Upcoming Pricing](https://cloud.google.com/stackdriver/pricing_v2).

## May 23, 2018

Change

Custom dashboards and pages for resource groups are now limited to 25 charts. Any dashboards or groups pages with more than 25 charts will continue to work, but you will not be able to add additional charts to them.

## May 22, 2018

Feature

You can now see your Monitoring usage metrics and estimate your bill for your usage of Monitoring, according to the new Stackdriver pricing and in advance of billing enforcement. See [Estimating your bills](https://cloud.google.com/stackdriver/estimating-bills) for details.

## May 21, 2018

Feature

A new UI for creating conditions in alerting policies is available in Beta. This UI, based on Metrics Explorer, offers fine-grained control over the selection of the metrics used in alerting conditions. See [Managing Alerting Policies](https://cloud.google.com/monitoring/alerts/using-alerting-ui) for more information.

## May 11, 2018

Change

If you are using custom IAM roles, any roles that load Stackdriver Monitoring dashboards now require additional IAM permissions. The `monitoring.dashboards.*` and `monitoring.publicWidgets.*` permissions are now public, and custom roles used to load dashboards must now include them. See [Stackdriver Monitoring Access Control](https://cloud.google.com/monitoring/access-control#roles) for more information.

## May 02, 2018

Feature

[Stackdriver Kubernetes Monitoring](https://cloud.google.com//monitoring/kubernetes-engine) is released in Beta for Kubernetes 1.10 clusters running in [Kubernetes Engine](https://cloud.google.com//kubernetes-engine/docs/). The previous Stackdriver support is still available for those who do not opt into this Beta release. The release introduces new [monitored resource types](https://cloud.google.com//monitoring/api/resources#tag_k8s_cluster) and new [Kubernetes metrics](https://cloud.google.com//monitoring/api/metrics_kubernetes#kubernetes). The monitoring features are free to customers during the Beta period.

## April 26, 2018

Change

You can now use variables in the documentation associated with alerting policies to pull specific details about the alert into notifications, to create playbook information for responders. See [Additional documentation tools](https://cloud.google.com/monitoring/alerts/doc-variables) for more information. The Webhooks and Slack notification channels now receive a copy of this enhanced documentation as part of alert notifications. Additionally, email notifications from alerting policies now use HTML-formatted messages.

## April 19, 2018

Feature

Boolean metrics can now be queried and charted.

## April 17, 2018

Change

The [Using Alerting Policies](https://cloud.google.com/monitoring/alerts) documentation has been updated to provide additional guides and links to sample code for managing alerting policies and notification channels programmatically. The update also removes some obsolete service-tier information.

## March 28, 2018

Change

Stackdriver now loads charts much more quickly, especially when the chart contains a long time span.

## March 26, 2018

Change

A new option on the Dashboards menu, **Public Charts** , lets you see a list of all the shared charts. You can also use this page to remove sharing from a chart. The on-chart indicator that the chart is shared has been removed.

## March 12, 2018

Change

Beginning on June 30, 2018, Stackdriver is switching to consumption-based pricing, including revised quotas. For more information, see [Stackdriver Upcoming Pricing](https://cloud.google.com//stackdriver/pricing_v2).

## March 08, 2018

Feature

The `AlertPolicy` and `NotificationChannels` APIs are now in Beta release. See [Alerting policies](https://cloud.google.com/monitoring/api/v3/#alerting-policies) and [Notification channels](https://cloud.google.com/monitoring/api/v3/#notification-channels) for more information.

## January 29, 2018

Fixed

The Stackdriver email reports that you can configure for your Stackdriver account have been improved. Issues with the content and the delivery of reports have been fixed, and the _from_ address for the reports has been changed from `monitoring-noreply@stackdriver.google.com` to `monitoring-noreply@google.com`. The Utilization section, present only if the Monitoring Agent is installed, now lists the 10 groups with the highest utilization, and a new summary row reports overall utilization for the Stackdriver account.

## January 17, 2018

Change

The name of the Monitoring agent process on Windows has been updated. It now shows up in the system process list as `StackdriverMonitoring`.

## January 08, 2018

Change

The performance of the Monitoring dashboards and charts has been improved. Additionally, a new version of Metrics Explorer is available, and the metric-selection interface has been greatly improved, allowing arbitrary label filtering and group-by functionality. This interface is also used for creating dashboard charts, making the process consistent across the two tasks. See [Using Charts](https://cloud.google.com/monitoring/charts) for more information.

## December 14, 2017

Change

**Alerting events page** : An updated implementation has required some user interface changes. The alerting events page (**Alerting > Events**) no longer shows a heatmap or counts of events in each category.

## November 08, 2017

Change

The Monitoring agents for Linux and Windows VM instances now report errors for unrecognized metrics. The errors are written to the agent log on your VM instance. If the [Logging agent](https://cloud.google.com/logging/docs/agent/) is also running on the VM instance, then the logs are also available in Stackdriver Logging. The error messages are, "Unsupported collectd plugin/type combination" and "Unsupported collectd ID." Previously, these metrics were dropped silently. See the agent's [Troubleshooting Checklist](https://cloud.google.com/monitoring/agent/troubleshooting#checklist) for more information.

## November 05, 2017

Deprecated

Documentation for the deprecated Cloud Monitoring API v2 has been removed. The API was turned down in August, 2017.

## October 19, 2017

Feature

Beta release: The Monitoring agent can now export collectd and statsd metrics as Stackdriver [custom metrics](https://cloud.google.com/monitoring/custom-metrics/). For more information, see [Custom Metrics from the Agent](https://cloud.google.com/monitoring/agent/custom-metrics-agent) and the agent's [StatsD plugin](https://cloud.google.com/monitoring/agent/plugins/statsd)

## October 17, 2017

Feature

Beta release: The [Uptime Configuration API](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs) and [uptime metrics](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-monitoring) are now available. The API, part of the [Stackdriver Monitoring API](https://cloud.google.com/monitoring/api/ref_v3/rest/), lets you create and edit [uptime checks](https://cloud.google.com/monitoring/uptime-checks/). The status of your checks is recorded in the uptime metrics.

## October 02, 2017

Fixed

Calls to [createTimeSeries](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/create) now fail without writing any data points if the request includes more than one point in the same time series. Formerly, in some cases, one data point would be written in each time series and a status of 500 would be returned by the call.

## September 13, 2017

Change

**Object Stores Resources** : Google Cloud Storage metrics and Amazon S3 metrics are now separated in the Stackdriver UI into their own service dashboards. The "Object Stores" dashboard is replaced by "Cloud Storage" or "S3", depending on which service you are using.

## September 08, 2017

Feature

**HTTPS(S) Load Balancer** metrics are available in Beta release to use in Monitoring. For details, see the Google Cloud [`loadbalancing`](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-loadbalancing) metrics and the [`https_lb_rule`](https://cloud.google.com/monitoring/api/resources#tag_https_lb_rule) monitored resource.

Feature

**Cloud Interconnect** custom dashboards and alert monitoring are available in Beta release. For details, see the Google Cloud [`interconnect`](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-interconnect) metrics and the [`interconnect`](https://cloud.google.com/monitoring/api/resources#tag_interconnect) and [`interconnect_attachment`](https://cloud.google.com/monitoring/api/resources#tag_interconnect_attachment) monitored resources.

Feature

**HTTPS(S) Load Balancer** metrics are available in Beta release to use in Monitoring. For details, see the Google Cloud [`loadbalancing`](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-loadbalancing) metrics and the [`https_lb_rule`](https://cloud.google.com/monitoring/api/resources#tag_https_lb_rule) monitored resource.

## August 23, 2017

Feature

**Dashboard filtering** : Custom dashboards and resource list pages now support filtering on groups. Each page that supports filtering now has a filter bar under the header where you specify the group.

## July 10, 2017

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

Feature

**Uptime checks** have a new overview and detail dashboards. See [Uptime Checks](https://cloud.google.com/monitoring/alerts/uptime-checks).

Feature

**Singapore region support** : Stackdriver now supports the Singapore region, `asia-southeast1`.

## May 01, 2017

Feature

New metric and resource types: There are new Cloud Platform metric and resource types, including those for Cloud Bigtable, Cloud Dataflow, Cloud DNS, Cloud Internet of Things, Cloud Pub/Sub, Cloud Spanner, and Stackdriver Logging. Microsoft Windows system and application metrics (`iis`,`mssql`, `pagefile`) are available as Agent metrics and can be used for charting and alerting.

## April 02, 2017

Issue

**v2beta2 API turndown** : The deprecated v2beta1 and v2beta2 APIs will be shut down during August 2017.

## March 31, 2017

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

Fixed

**Process owner** : When sending process metrics, the Stackdriver Monitoring agent now returns a stringified UID if the process owner name is not set. Previously, the agent would not send process owner information, which was then treated by the Monitoring API as malformed input and discarded. Available in stackdriver-agent/5.5.2-359. See [Determining the agent version](https://cloud.google.com/monitoring/agent/install-agent#agent-version).

Fixed

**Lost input from the Monitoring agent** : Malformed data from the Monitoring agent could cause Stackdriver Monitoring to lose well-formed input bundled in the same request. Now, only the malformed input is lost. You do not have to update your agent for this fix.

Feature

**Selectable uptime check regions** : Stackdriver Monitoring now lets you select the geographic region(s) that check your service.

## January 18, 2017

Feature

**New AWS regions** : Monitoring now supports the AWS Canada (**ca-central-1**) and London (**eu-west-2**) regions.

## December 12, 2016

Feature

**Account IDs in URLs** : Monitoring has added the Stackdriver account ID to its URLs. You can now open multiple tabs for different accounts and more easily share links with coworkers. URLs without the account ID use the most recently accessed Stackdriver account.

## December 08, 2016

Feature

**Incident pages** (Beta): See **Alerting > Incidents**. Each open incident now has a detail page that collects a graph of the incident, links to affected resources, and the comments made on the incident.

Feature

**Metrics Explorer** (Beta): See **Resources > Metric Explorer**. Select a monitored resource type and metric. You can aggregate data across your instances.

## November 21, 2016

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

## September 11, 2016

Change

The Google Monitoring API (v3) is now known as the Stackdriver Monitoring API (v3). This change does not affect any code.

Deprecated

The Monitoring v2 API is now deprecated. It is still named the Google Cloud Monitoring API in **APIs & services**.

## July 26, 2016

Change

Some documentation pages have moved in the table of contents, but their URLs are the same or have redirections. All agent-related pages are now part of the How-To section, [Using the Monitoring Agent](https://cloud.google.com//monitoring/agent/). The former "Using Metrics" page has been reorganized into several pages under [Using Custom Metrics](https://cloud.google.com/monitoring/agent/).

## June 09, 2016

Change

The documentation for metrics and custom metrics has been reorganized and extended for the Monitoring API v3. See [Metrics](https://cloud.google.com//monitoring/api/v3/metrics), [Using Metrics](https://cloud.google.com//monitoring/api/v3/using-metrics), and [Metrics List](https://cloud.google.com//monitoring/api/metrics).

Change

The [Stackdriver Monitoring API v3 reference documentation](https://cloud.google.com/monitoring/api/ref_v3/rest/) now includes code samples for each method. For example, see [metricDescriptors.list](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/list). [Sample Code](https://cloud.google.com/monitoring/docs/tutorials) will continue to be available on GitHub.

## June 06, 2016

Change

[Metrics List](https://cloud.google.com//monitoring/api/metrics) is now a comprehensive list of all metrics available in Monitoring, including metrics gathered by the monitoring agent and metrics from Amazon Web Services.

## April 27, 2016

Change

The documentation has been reorganized. The [documentation landing page](https://cloud.google.com/monitoring/docs/) and the left-side navigation entries have changed. Existing URLs to individual documentation pages will be redirected if necessary.

Change

The [Quickstart](https://cloud.google.com//monitoring/quickstart-lamp) has been simplified. It now includes setting up a virtual machine instance and installing both the monitoring and logging agents.

## March 23, 2016

Change

Google Cloud Monitoring is now **Stackdriver Monitoring** , part of the [Google Stackdriver](https://cloud.google.com/products/operations) suite of products.

Feature

You can now monitor Amazon Web Services (AWS) accounts alongside your Google Cloud projects. Read about Stackdriver Accounts and install the new [monitoring agent](https://cloud.google.com/monitoring/agent/).

Issue

When installing the monitoring agent on an Amazon EC2 VM instance running Microsoft Windows, ignore the following error message if you get it only once after the service is started: "StackdriverAgent is running on an AWS instance but project ID is not set."

## March 17, 2016

Feature

The [Monitoring API v3](https://cloud.google.com/monitoring/api/ref_v3/rest/) is now available. Users are encouraged to begin upgrading from the Cloud Monitoring API v2. See [What's new](https://cloud.google.com/monitoring/api/v3/) in the v3 API and look at the new [code samples](https://cloud.google.com/monitoring/docs/tutorials) on GitHub.

## September 29, 2015

Feature

Charts now have a [View Logs](https://cloud.google.com/monitoring/quickstart-lamp#charts-to-logs) option in their settings menu.

## January 07, 2015

Feature

First beta release of [Google Cloud Monitoring powered by Stackdriver](https://cloud.google.com/monitoring).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
