---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability/
title: Observability for GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:11.993914+00:00
---

# Observability for GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Observability for GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes observability features in Google Kubernetes Engine (GKE) for monitoring application health and availability.

To help ensure the availability and reliability of your applications on GKE, you need to monitor their health and performance. GKE provides observability features, such as metrics and dashboards, that offer crucial insights into your containerized workloads, helping you to detect issues early and optimize performance. These capabilities can be particularly beneficial for demanding workloads, such as AI/ML applications, where control and performance are critical.

This document is for IT administrators, developers, and operators who want to monitor their workloads. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Default observability features

By default, GKE clusters are configured to do the following:

  * Send [system logs, audit logs, and application logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs#what_logs) to Cloud Logging.
  * Send [system metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#system-metrics) to Cloud Monitoring.
  * Use [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) to collect configured third-party and user-defined metrics and then send them to Cloud Monitoring. Google Cloud Managed Service for Prometheus lets you monitor and alert on your workloads using Prometheus, without manually managing and operating Prometheus at scale.



## Customize and enhance data collection

By default, GKE creates a Logging repository for storing logs for each cluster. You can control which logs and which metrics, if any, are sent from your GKE cluster to Cloud Logging and Cloud Monitoring.

You can also control whether to enable [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus).

For GKE Autopilot clusters, you cannot disable the Cloud Monitoring and Cloud Logging integration.

### Additional observability metrics

You can collect additional observability metrics by using methods like the following:

  * Enable one or more [observability metrics packages](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics), such as the following:

    * [Control plane metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/control-plane-metrics): Monitor the health of Kubernetes components by collecting metrics for the Kubernetes API server, Scheduler, and Controller Manager. These metrics are useful signals of service health for defining service level objectives (SLOs). 
    * [Kube state metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/kube-state-metrics): Monitor the health of Kubernetes objects such as Deployments, Nodes, and Pods.
    * [cAdvisor/Kubelet metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cadvisor-kubelet-metrics): Monitor the health of containers and the `kubelet`.
  * Configure Google Cloud Managed Service for Prometheus to [collect specific metrics from Kubernetes components](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/collect-specific-prometheus-metrics). This method is useful if you want to collect a metric that's not a part of a metrics package, or if you want only a subset of the metrics from a metrics package.




### Third-party and user-defined metrics

To monitor third-party applications running on your clusters such as Postgres, MongoDB, and Redis, use [Prometheus exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/introduction) with Google Cloud Managed Service for Prometheus.

You can also [write custom exporters](https://prometheus.io/docs/instrumenting/writing_exporters/) to monitor other signals of health and performance.

## Use collected data

Use the data you collect to analyze application health, debug, troubleshoot, and test as you develop, deploy, and maintain your applications.

GKE provides built-in observability features to get you started quickly:

  * View collected data for your clusters and workloads on in GKE [observability dashboards](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics). You can customize the provided dashboards for the following purposes:

    * View key cluster metrics, such as CPU utilization, memory utilization, and the number of open incidents.
    * View clusters by their infrastructure, workloads, or Services.
    * Inspect namespaces, Nodes, workloads, Services, Pods, and containers.
    * For Pods and containers, view metrics as a function of time and view log entries.

You can also [create your own dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards) or [import Grafana dashboards](https://docs.cloud.google.com/monitoring/dashboards/import-grafana-dashboards) to meet your needs.

**Note:** The provided GKE dashboards only display information for GKE clusters running on Google Cloud. They don't display information for GKE clusters running anywhere else, for example using on-premises or bare-metal servers.
  * View details for your AI/ML workloads in Google Cloud console, including resources such as JobSets, RayJobs, PyTorchJobs, and Deployments for inference serving.

[Go to the Google Cloud console](https://console.cloud.google.com/kubernetes/aiml)

  * From the **Observability** tab, you can create recommended alert policies so that you are notified about issues. To learn more about alerting, see the [Alerting overview](https://docs.cloud.google.com/monitoring/alerts).

  * [Create SLOs](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-slo) to monitor your service performance goals using collected GKE metrics.

  * Use GKE playbooks to troubleshoot common issues such as [unschedulable Pods](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/deployed-workloads#PodUnschedulable) and [containers that repeatedly crash after restart](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/deployed-workloads#CrashLoopBackOff).

  * Explore and analyze your data with tools such as [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) and [Error Reporting](https://docs.cloud.google.com/error-reporting/docs/grouping-errors).

  * Review GKE [audit logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging) that record administrative activities and accesses as part of [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit). [Audit log policy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/audit-policy) determines which events are recorded and whether a log entry belongs to an Admin Activity log or a Data Access log.




## Other features

GKE integrates with other Google Cloud services to help you monitor and manage your clusters and workloads.

  * Use the [security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard) to identify security concerns based on our standards and industry best practices.

  * View [insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders) to optimize your clusters.

  * Use [network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging) to help you troubleshoot issues with Kubernetes network policies. If you use [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2), then network policy logging is built-in.




## Pricing

Pricing for integration with Cloud Logging (including Cloud Audit Logs), Cloud Monitoring, and Google Cloud Managed Service for Prometheus is based on the amount of logs and metrics collected. See the [Pricing](https://cloud.google.com/stackdriver/pricing) page for details.

Features provided by other Google Cloud services listed in Other features have separate pricing. See the Pricing section of those documentation pages for more information.

## What's next

  * [Observe your clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics). Learn how to view dashboards, organize cluster information, and view alerting details.

  * [Enable verbose, OS-level audit logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/linux-auditd-logging) on GKE cluster nodes and how to export logs to Cloud Logging.

  * For more information about how to use observability features to troubleshoot GKE, see [Conduct historical analysis with Cloud Logging](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-logging) and [Perform proactive monitoring with Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-monitoring).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
