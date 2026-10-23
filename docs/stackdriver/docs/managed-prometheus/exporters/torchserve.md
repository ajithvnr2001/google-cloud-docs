---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/torchserve/
title: TorchServe \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:24.514734+00:00
---

# TorchServe  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/torchserve/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  TorchServe Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from TorchServe. This document shows you how to do the following: 

  * Set up TorchServe to report metrics.
  * Access a predefined dashboard in Cloud Monitoring to view the metrics.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [TorchServe documentation](https://pytorch.org/serve/metrics.html) for installation information.

These instructions are provided as an example and are expected to work in most Kubernetes environments. If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

For information about TorchServe, see [TorchServe](https://pytorch.org/serve/index.html). For information about setting up TorchServe on Google Kubernetes Engine, see the GKE [ guide for TorchServe](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scalable-ml-models-torchserve). 

## Prerequisites

To collect metrics from TorchServe by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements: 

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).

TorchServe exposes Prometheus-format metrics automatically when the `metrics_mode` flag is specified either in the `config.properties` file or as an environment variable. 

If you are setting up TorchServe yourself, then we recommend making the following additions to your `config.properties` file.

If you are following the Google Kubernetes Engine document [Serve scalable LLMs on GKE with TorchServe](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scalable-ml-models-torchserve), then these additions are part of the default setup.
    
    
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
    
      inference_address=http://0.0.0.0:8080
      management_address=http://0.0.0.0:8081
    + metrics_address=http://0.0.0.0:8082
    + metrics_mode=prometheus
      number_of_netty_threads=32
      job_queue_size=1000
      install_py_dep_per_model=true
      model_store=/home/model-server/model-store
      load_models=all
    

Also, when deploying this image to GKE, modify your deployment and service YAML to expose the added metrics port:
    
    
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
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: t5-inference
      labels:
        model: t5
        version: v1.0
        machine: gpu
    spec:
      replicas: 1
      selector:
        matchLabels:
          model: t5
          version: v1.0
          machine: gpu
      template:
        metadata:
          labels:
            model: t5
            version: v1.0
            machine: gpu
        spec:
          nodeSelector:
            cloud.google.com/gke-accelerator: nvidia-l4
          containers:
            - name: inference
              ...
              args: ["torchserve", "--start", "--foreground"]
              resources:
                ...
              ports:
                - containerPort: 8080
                  name: http
                - containerPort: 8081
                  name: management
    +           - containerPort: 8082
    +             name: metrics
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: t5-inference
      labels:
        model: t5
        version: v1.0
        machine: gpu
    spec:
      ...
      ports:
        - port: 8080
          name: http
          targetPort: http
        - port: 8081
          name: management
          targetPort: management
    +   - port: 8082
    +     name: metrics
    +     targetPort: metrics
    

To verify that TorchServe is emitting metrics on the expected endpoints, do the following:

  1. Set up port forwarding by using the following command: 
         
         kubectl -n NAMESPACE_NAME port-forward SERVICE_NAME 8082
         

  2. Access the endpoint `localhost:8082/metrics` by using the browser or the `curl` utility in another terminal session.



## Define a PodMonitoring resource

For target discovery, the Managed Service for Prometheus Operator requires a PodMonitoring resource that corresponds to TorchServe in the same namespace.

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
      name: torchserve
      labels:
        app.kubernetes.io/name: torchserve
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      endpoints:
      - port: 8082
        scheme: http
        interval: 30s
        path: /metrics
      selector:
        matchLabels:
          model: t5
          version: v1.0
          machine: gpu
    

Ensure that the values of the `port` and `matchLabels` fields match those of the TorchServe pods you want to monitor. 

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Verify the configuration

You can use Metrics Explorer to verify that you correctly configured TorchServe. It might take one or two minutes for Cloud Monitoring to ingest your metrics.

To verify the metrics are ingested, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter and run the following query:  

         
         up{job="torchserve", cluster="CLUSTER_NAME", namespace="NAMESPACE_NAME"}




## View dashboards

The Cloud Monitoring integration includes the **TorchServe Prometheus Overview** dashboard. Dashboards are automatically installed when you configure the integration. You can also view static previews of dashboards without installing the integration. 

To view an installed dashboard, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab.
  3. Choose the **Integrations** category.
  4. Click the name of the dashboard, for example, **TorchServe Prometheus Overview**.



To view a static preview of the dashboard, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Kubernetes Engine** deployment-platform filter.
  3. Locate the TorchServe integration and click **View Details**.
  4. Select the **Dashboards** tab.



## Troubleshooting

For information about troubleshooting metric ingestion problems, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
