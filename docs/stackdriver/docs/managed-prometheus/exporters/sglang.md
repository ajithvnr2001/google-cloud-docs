---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/sglang/
title: SGLang \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:50.929967+00:00
---

# SGLang  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/sglang/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  SGLang Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from SGLang. This document shows you how to do the following: 

  * Enable automatic application monitoring for SGLang, or set up SGLang manually to report metrics.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [SGLang documentation](https://docs.sglang.ai/references/production_metrics.html) for installation information.

These instructions are provided as an example and are expected to work in most Kubernetes environments. If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

For information about SGLang, see [SGLang](https://docs.sglang.ai/). 

## Prerequisites

To collect metrics from SGLang by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements: 

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).

SGLang exposes Prometheus-format metrics when launched with the `--enable-metrics` flag; you do not have to install an exporter separately. To verify that SGLang is emitting metrics on the expected endpoints, do the following: 

  1. Set up port forwarding by using the following command: 
         
         kubectl -n NAMESPACE_NAME port-forward POD_NAME 30000
         

  2. Access the `localhost:30000/metrics` endpoint by using the browser or the `curl` utility in another terminal session.



## Use automatic application monitoring

SGLang supports the use of [automatic application monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-automatic-application-monitoring). When you use automatic application monitoring, Google Kubernetes Engine does the following: 

  * Detects deployed instances of SGLang workloads.
  * Deploys a PodMonitoring resource for each detected workload instance.
  * Installs Cloud Monitoring dashboards for the SGLang metrics.



To use automatic application monitoring, you must enable the feature on your GKE cluster. You can use the Google Cloud console, the Google Cloud CLI (version 492.0.0 or later), or the GKE API. For more information, see [Enable automatic application monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-automatic-application-monitoring#enable-auto-monitoring}}).

## Define a PodMonitoring resource

For target discovery, the Managed Service for Prometheus Operator requires a PodMonitoring resource that corresponds to SGLang in the same namespace.

You can use the following PodMonitoring configuration:
    
    
    
    apiVersion: monitoring.googleapis.com/v1
    kind: PodMonitoring
    metadata:
      name: sglang
      labels:
        app.kubernetes.io/name: sglang
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      endpoints:
      - port: 30000
        scheme: http
        interval: 15s
        path: /metrics
      selector:
        matchLabels:
          app: sglang-server
    
    

Ensure that the values of the `port` and `matchLabels` fields match those of the SGLang pods you want to monitor. 

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Verify the configuration

You can use Metrics Explorer to verify that you correctly configured SGLang. It might take one or two minutes for Cloud Monitoring to ingest your metrics.

To verify the metrics are ingested, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter and run the following query:  

         
         up{job=~"sglang|gke-ac-.*", cluster="CLUSTER_NAME", namespace="NAMESPACE_NAME"}




## Troubleshooting

For information about troubleshooting metric ingestion problems, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
