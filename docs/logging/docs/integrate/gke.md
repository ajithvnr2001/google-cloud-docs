---
url: https://docs.cloud.google.com/logging/docs/integrate/gke/
title: Collect GKE logs \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:38.791779+00:00
---

# Collect GKE logs  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/integrate/gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Collect GKE logs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes options for collecting logs from Google Kubernetes Engine.

## Log collection

By default, GKE clusters send logs to Cloud Logging. You can choose the types of logs to collect when you create a cluster or enable log collection for an existing cluster.

**Note:** For [GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) clusters, you can't disable collection of all GKE logs.

For information about configuring log collection, see [Configuring logging and monitoring for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics).

For information about the types of GKE logs that Logging collects and details about managing your logs, see [Managing GKE logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs#collecting_logs).

## Multi-tenant logging

A multi-tenant cluster is a cluster that multiple teams share as _tenants_ of the cluster.

A common approach to multi-tenancy is to use one Google Cloud project for the shared cluster and separate projects for each application team. Cluster admins can configure a system where logs are stored in the same project as the cluster, and tenant logs are routed to the application team projects.

For information about configuring logging for multi-tenant clusters, see [Multi-tenant logging on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-tenant-logging).

## What's next

  * Explore logs for your GKE clusters and resources in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).


  * Learn how to [monitor your logs](https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs) with [predefined logs dashboards](https://docs.cloud.google.com/logging/docs/view/dashboard) for GKE, log-based alerts, and other features.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
