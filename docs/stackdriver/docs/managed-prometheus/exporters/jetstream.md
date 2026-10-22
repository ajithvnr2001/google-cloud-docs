---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/jetstream/
title: JetStream \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:17.357384+00:00
---

# JetStream  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/jetstream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  JetStream Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from JetStream. This document shows you how to do the following: 

  * Set up JetStream to report metrics.
  * Access a predefined dashboard in Cloud Monitoring to view the metrics.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [JetStream documentation](https://github.com/AI-Hypercomputer/JetStream/blob/main/docs/observability-prometheus-metrics-in-jetstream-server.md) for installation information.

These instructions are provided as an example and are expected to work in most Kubernetes environments. If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

For information about JetStream, see [JetStream](https://github.com/AI-Hypercomputer/JetStream). For information about setting up JetStream on Google Kubernetes Engine, see the GKE [ guide for JetStream](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-llm-tpu-jetstream-pytorch). 

## Prerequisites

To collect metrics from JetStream by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements: 

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).

To collect Prometheus-format metrics from JetStream, you must first [build and upload a JetStream PyTorch server image](https://github.com/AI-Hypercomputer/jetstream-pytorch/tree/main/docker/jetstream-pytorch-server). To verify that JetStream is emitting metrics on the expected endpoints, do the following: 

  1. Set up port forwarding by using the following command: 
         
         kubectl -n NAMESPACE_NAME port-forward POD_NAME 9090
         

  2. Access the endpoint `localhost:9090/metrics` by using the browser or the `curl` utility in another terminal session.



## Define a PodMonitoring resource

For target discovery, the Managed Service for Prometheus Operator requires a PodMonitoring resource that corresponds to JetStream in the same namespace.

You can use the following PodMonitoring configuration:
    
    
    # Copyright 2025 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    apiVersion: monitoring.googleapis.com/v1
    kind: PodMonitoring
    metadata:
      name: jetstream
      labels:
        app.kubernetes.io/name: jetstream
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      endpoints:
      - port: 9090
        scheme: http
        interval: 30s
        path: /metrics
      selector:
        matchLabels:
          app: jetstream-pytorch-server
    

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Verify the configuration

You can use Metrics Explorer to verify that you correctly configured JetStream. It might take one or two minutes for Cloud Monitoring to ingest your metrics.

To verify the metrics are ingested, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter and run the following query:  

         
         up{job="jetstream", cluster="CLUSTER_NAME", namespace="NAMESPACE_NAME"}




## View dashboards

The Cloud Monitoring integration includes the **JetStream Prometheus Overview** dashboard. Dashboards are automatically installed when you configure the integration. You can also view static previews of dashboards without installing the integration. 

To view an installed dashboard, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab.
  3. Choose the **Integrations** category.
  4. Click the name of the dashboard, for example, **JetStream Prometheus Overview**.



To view a static preview of the dashboard, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Kubernetes Engine** deployment-platform filter.
  3. Locate the JetStream integration and click **View Details**.
  4. Select the **Dashboards** tab.



## Troubleshooting

For information about troubleshooting metric ingestion problems, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
