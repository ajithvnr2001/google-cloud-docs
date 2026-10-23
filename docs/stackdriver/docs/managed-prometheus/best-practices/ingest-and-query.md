---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/best-practices/ingest-and-query/
title: Ingestion and querying with managed and self-deployed collection \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:50.330855+00:00
---

# Ingestion and querying with managed and self-deployed collection  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/best-practices/ingest-and-query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Ingestion and querying with managed and self-deployed collection Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you might set up an environment that mixes self-deployed collectors with managed collectors, across different Google Cloud projects and clusters.

We strongly recommend using managed collection for all Kubernetes environments; doing so practically eliminates the overhead of running Prometheus collectors within your cluster. You can run managed and self-deployed collectors within the same cluster. We recommend using a consistent approach to monitoring, but you might choose to mix deployment methods for some specific use cases, such as hosting a push gateway, as illustrated in this document. 

The following diagram illustrates a configuration that uses two Google Cloud projects, three clusters, and mixes managed and self-deployed collection. If you use only managed or self-deployed collection, then the diagram is still applicable; just ignore the collection style you aren't using:

![You can set up Managed Service for Prometheus with a mix of managed and self-deployed collection.](https://docs.cloud.google.com/static/stackdriver/images/gmp-bp-ingest-and-query.png)

To set up and use a configuration like the one in the diagram, note the following:

  * You must install any necessary [exporters](https://prometheus.io/docs/instrumenting/exporters/) in your clusters. Google Cloud Managed Service for Prometheus does not install any exporters on your behalf.

  * Project 1 has a cluster running managed collection, which runs as a node agent. Collectors are configured with [PodMonitoring](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#podmonitoring) resources to scrape targets within a namespace and with [ClusterPodMonitoring](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#clusterpodmonitoring) resources to scrape targets across a cluster. PodMonitorings must be applied in every namespace in which you want to collect metrics. ClusterPodMonitorings are applied once per cluster.

All data collected in Project 1 is saved in Monarch under Project 1. This data is stored by default in the Google Cloud region from which it emitted.

  * Project 2 has a cluster running self-deployed collection using prometheus-operator and running as a standalone service. This cluster is configured to use prometheus-operator PodMonitors or ServiceMonitors to scrape exporters on pods or VMs.

Project 2 also hosts a push gateway sidecar to gather metrics from ephemeral workloads.

All data collected in Project 2 is saved in Monarch under Project 2. This data is stored by default in the Google Cloud region from which it emitted.

  * Project 1 also has a cluster running [Grafana](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query#ui-grafana) and the [data source syncer](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query#grafana-oauth). In this example, these components are hosted in a standalone cluster, but they can be hosted in any single cluster.

The data source syncer is configured to use scoping_project_A, and its underlying service account has [Monitoring Viewer](https://docs.cloud.google.com/monitoring/access-control#mon_roles_desc) permissions for scoping_project_A.

When a user issues queries from Grafana, Monarch expands scoping_project_A into its constituent monitored projects and returns results for both Project 1 and Project 2 across all Google Cloud regions. All metrics retain their original `project_id` and `location` (Google Cloud region) labels for grouping and filtering purposes.




If your cluster is not running inside Google Cloud, you must manually configure the `project_id` and `location` labels. For information about setting these values, see [Run Managed Service for Prometheus outside of Google Cloud](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged#gmp-outside-gcp).

**Do not federate when using Managed Service for Prometheus.** To reduce cardinality and cost by "rolling up" data before sending it to Monarch, use local aggregation instead. For more information, see [Configure local aggregation](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls#local-aggregation).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
