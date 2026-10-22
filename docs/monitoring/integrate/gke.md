---
url: https://docs.cloud.google.com/monitoring/integrate/gke/
title: Collect Prometheus metrics from GKE \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:57.118107+00:00
---

# Collect Prometheus metrics from GKE  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/integrate/gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Collect Prometheus metrics from GKE Stay organized with collections  Save and categorize content based on your preferences. 

Collecting Prometheus metrics from Google Kubernetes Engine (GKE) clusters with Google Cloud Managed Service for Prometheus lets you monitor and alert on your clusters and workloads without managing Prometheus at scale. This document provides an overview of default system metrics and managed Prometheus collection on GKE.

## About Prometheus

[Prometheus](https://prometheus.io/) is a leading open-source tool for monitoring and alerting, and is a standard tool for Kubernetes monitoring.

[Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) is the Google Cloud fully managed solution for Prometheus. It lets you globally monitor and alert on your workloads by using Prometheus, without having to manually manage and operate Prometheus at scale.

## Metrics collection

[Managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke) of metrics by Google Cloud Managed Service for Prometheus is enabled by default when you create a cluster. You can enable managed collection on existing clusters.

By default, GKE clusters send [system metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes). You can also enable additional observability metrics packages for a cluster. For information about the types of metrics you can collect, see [Manage GKE metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics).

**Note:** For [GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) clusters, you can't disable collection of all GKE metrics.

## What's next

  * View [observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics) for clusters and workloads in predefined GKE dashboards in the Google Cloud console. You can also create recommended GKE alerts and view logs for events.
  * [Create service-level objectives (SLOs)](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-slo) that use GKE [control plane metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/control-plane-metrics) to monitor availability and latency.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
