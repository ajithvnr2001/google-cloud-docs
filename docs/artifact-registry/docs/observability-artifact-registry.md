---
url: https://docs.cloud.google.com/artifact-registry/docs/observability-artifact-registry/
title: Observability in Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:28.217463+00:00
---

# Observability in Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/observability-artifact-registry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Observability in Artifact Registry Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the resources available for administrators to monitor activity and growth in Artifact Registry resources using Google Cloud Observability services.

By default, Artifact Registry is configured to do the following:

  * Send system logs and audit logs to Cloud Logging
  * Send system metrics and resource metrics to Cloud Monitoring

For more information, read [Observability in Google Cloud](https://docs.cloud.google.com/stackdriver/docs). 

## Collected logs

Artifact Registry sends the following types of audit log data to Cloud Logging:

  * [Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
  * [Data Access logs](https://docs.cloud.google.com/logging/docs/audit#data-access)
  * [Events logs](https://docs.cloud.google.com/logging/docs/audit#system-event)
  * [Policy Denied logs](https://docs.cloud.google.com/logging/docs/audit#policy_denied).



Data Access audit logs are disabled by default because these audit logs can be quite large. For more information about Audit logs in Artifact Registry, see [Audit Logging](https://docs.cloud.google.com/artifact-registry/docs/audit-logging).

## Query and view logs

You can use following tools to view and analyze your logs:

  * **Logs Explorer** is designed to help you troubleshoot and analyze the performance of your services and applications. To learn how to view logs in the Logs Explorer, follow the instructions in [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).
  * **Observability Analytics** is designed to run queries to analyze your logs, and then view or chart the results. To learn how to use Observability Analytics, follow the instructions in [Query and analyze logs in Observability Analytics](https://docs.cloud.google.com/logging/docs/analyze/query-and-view).



You can filter for Artifact Registry logs in the Logs Explorer by searching for `artifactregistry` in the search field.

For more information about querying and analyzing logs, see [Query and view logs overview](https://docs.cloud.google.com/logging/docs/log-analytics).

For pricing information, see the Cloud Logging sections of the [Google Cloud Observability pricing page](https://cloud.google.com/stackdriver/pricing).

## Collected metrics

Artifact Registry sends metric data from the following monitored-resources to Google Cloud Observability.

  * [Artifact Registry location](https://docs.cloud.google.com/artifact-registry/docs/monitored-resource-location)
  * [Artifact Registry project](https://docs.cloud.google.com/artifact-registry/docs/monitored-resource-project)
  * [Artifact Registry repository](https://docs.cloud.google.com/artifact-registry/docs/monitored-resource-repository)



To view all metrics sent by Artifact Registry to Google Cloud Observability, see [Artifact Registry Metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-artifactregistry).

For more information about metrics, read [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics).

### Artifact Registry location

Both [logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) and [quota metrics](https://docs.cloud.google.com/monitoring/alerts/using-quota-metrics) write data against the location resource. 

### Artifact Registry project

Metrics that are written against the project resource include request counts and request latency per project for control plane API requests and data plane API requests. Requests to create and modify repositories are control plane API requests, while tools such as Docker, Maven, or pip send requests to the data plane API.

### Repository

Metrics that are written against the repository resource include request counts and request latency per repository for control plane API requests and data plane API requests, as well as repository size over time.

## Query and view metrics

You can use the **Metrics Explorer** to create a chart that displays data for a single metric type, or for multiple metric types. After you create a chart, you can discard it , save it to a custom dashboard, or share it.

To get started using the Metrics Explorer to view Artifact Registry metrics, follow the instructions in [Chart request counts per repository in the Metrics Explorer](https://docs.cloud.google.com/artifact-registry/docs/chart-request-counts).

For pricing information, see the Cloud Monitoring sections of the [Google Cloud Observability pricing page](https://cloud.google.com/stackdriver/pricing).

## What's next

  * [Configure monitoring alerts for repository growth](https://docs.cloud.google.com/artifact-registry/docs/configure-monitoring-notifications)
  * [Chart request counts per repository in the Metrics Explorer](https://docs.cloud.google.com/artifact-registry/docs/chart-request-counts)
  * Read more about how to [create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).
  * Learn about [Artifact Registry Audit Logs](https://docs.cloud.google.com/artifact-registry/docs/audit-logging).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
