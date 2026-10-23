---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/app-performance-metrics/
title: Use application performance metrics \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:05.108718+00:00
---

# Use application performance metrics  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/app-performance-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Use application performance metrics Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can configure your workloads on Google Kubernetes Engine (GKE) to send application performance metrics to Cloud Monitoring. You can then use these metrics to detect performance regressions in your application. Google Kubernetes Engine provides visualizations for the following kinds of performance measures for your workloads:

  * Requests: shows the per-second request rate, grouped by operation when available.
  * Errors: shows error rates, grouped by operation and response code.
  * Latency: shows 50th and 95th percentile response latency by operation.
  * CPU and memory: shows the utilization of CPU and memory as a percentage of a requested amount.



These metrics correspond to the [_golden signals_](https://sre.google/sre-book/monitoring-distributed-systems/#xref_monitoring_golden-signals) recommended in the Google [_Site Reliability Engineering_ book](https://sre.google/sre-book/monitoring-distributed-systems/) for monitoring distributed systems.

You can also view and explore logs for your workloads.

Before you can use application performance metrics, your application must have a way to send the metrics to Cloud Monitoring. For information about recommended approaches, see Collect application performance metrics.

## Collect application performance metrics

You can collect application performance metrics for Google Kubernetes Engine by using the following supported integrations:

  * **Cloud Service Mesh** : If you use Cloud Service Mesh, then application performance metrics are collected automatically.
  * **Istio** : If you use [open source Istio](https://istio.io), then we recommend that you [collect the metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/istio) by using Google Cloud Managed Service for Prometheus.
  * **GKE Ingress** : When you configure [GKE Ingress for Application Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress), performance metrics are automatically collected for the HTTP/S load balancers that route traffic to your GKE Service and Deployment resources behind GKE Ingress.
  * **NGINX Ingress** : If you are using [NGINX Ingress](https://kubernetes.github.io/ingress-nginx/), then we recommend that you [collect the metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/ingress-nginx) by using Google Cloud Managed Service for Prometheus.
  * **Prometheus HTTP and gRPC metrics** : If your application exposes Prometheus HTTP or gRPC metrics, then we recommend that you follow the [HTTP server](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/server/http) and [gRPC server](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/server/grpc) documents to collect the metrics by using Google Cloud Managed Service for Prometheus.



## View application performance metrics

After you configure the collection of application performance metrics and run workloads that generate the traffic, the performance data is available for analysis. You can then [view the metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics#app-perf-view) for a Deployment on the application dashboard.

If you do not see any available data in the dashboards, check that you have both configured collection and run workloads to generate traffic. If no metric data has been generated, then the dashboards are not populated.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
