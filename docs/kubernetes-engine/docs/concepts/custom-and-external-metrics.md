---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/custom-and-external-metrics/
title: About autoscaling workloads based on metrics \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:56.571483+00:00
---

# About autoscaling workloads based on metrics  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/custom-and-external-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About autoscaling workloads based on metrics Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes the ways that you can automatically increase or decrease the number of replicas of a given workload using custom, external, or Prometheus metrics.

## Why autoscale based on metrics

Consider an application that pulls tasks from a queue and completes them. The application might have a Service-Level objective (SLO) for time to process a task, or for the number of tasks pending. If the queue is increasing, more replicas of the workload might meet the workloads SLO. If the queue is empty or is decreasing more quickly than expected, you could save money by running fewer replicas, while still meeting the workloads SLO.

## About custom, Prometheus, and external metrics

You can scale workloads based on custom, Prometheus, or external metrics.

A _custom metric_ is reported from your application running in Kubernetes. To learn more, see Custom and Prometheus metrics.

Metrics coming from [Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) are considered a type of custom metric.

An _external metric_ is reported from an application or service not running on your cluster, but whose performance impacts your Kubernetes application. For example, you can autoscale on any metric in Cloud Monitoring, including Pub/Sub or Dataflow. Prometheus metrics contain data emitted from your cluster that you can use to autoscale on. To learn more, see External metrics.

### Custom and Prometheus metrics

We recommend that you use Managed Service for Prometheus to create and manage custom metrics. You can use Prometheus Query Language (PromQL) to query all metrics in Monitoring. For more information, see [Horizontal Pod autoscaling for Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/hpa).

Your application can report a custom metric to Monitoring. You can configure Kubernetes to respond to these metrics and scale your workload automatically. For example, you can scale your application based on metrics such as queries per second, writes per second, network performance, latency when communicating with a different application, or other metrics that make sense for your workload. For more information, see [Expose custom metrics for autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/expose-custom-metrics-autoscaling).

Alternatively, you can [expose custom metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/expose-custom-metrics-autoscaling) (Preview) and send the metrics from a Pod or workload directly to the autoscaler.

### External metrics

If you need to scale your workload based on the performance of an application or service outside of Kubernetes, you can configure an external metric. For example, you might need to increase the capacity of your application to ingest messages from Pub/Sub if the number of undelivered messages is trending upward. The external application needs to export the metric to a Monitoring instance that the cluster can access. The trend of each metric over time causes Horizontal Pod Autoscaler to change the number of replicas in the workload automatically. For more information, see the [Pub/Sub HPA sample](https://docs.cloud.google.com/kubernetes-engine/docs/samples/container-pubsub-horizontal-pod-autoscaler).

## Import metrics to Monitoring

To import metrics to Monitoring, you can either:

  * Configure [Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) (recommended), **or**
  * Export metrics from the application using the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics).



## What's next

  * Learn how to [expose custom metrics for autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/expose-custom-metrics-autoscaling).
  * Learn more about the [horizontal Pod Autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler).
  * Learn how to [configure horizontal Pod Autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling).
  * Read about [scaling applications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/scaling-apps).
  * Learn more about the [vertical Pod Autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
