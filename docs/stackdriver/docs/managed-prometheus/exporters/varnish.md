---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/varnish/
title: Varnish \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:25.276533+00:00
---

# Varnish  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/varnish/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Varnish Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from Varnish. This document shows you how to do the following: 

  * Set up the exporter for Varnish to report metrics.
  * Access a predefined dashboard in Cloud Monitoring to view the metrics.
  * Configure alerting rules to monitor the metrics.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [source repository](https://github.com/jonnenauha/prometheus_varnish_exporter) for the Varnish exporter for installation information.

These instructions are provided as an example and are expected to work in most Kubernetes environments. If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

For information about Varnish, see [Varnish](https://varnish-cache.org/). 

## Prerequisites

To collect metrics from Varnish by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements: 

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).
  * To use dashboards available in Cloud Monitoring for the Varnish integration, you must use `prometheus_varnish_exporter` version "1.6.1" or later. 

For more information about available dashboards, see View dashboards. 


The Varnish exporter scrapes the output of the `varnishstat` command. It requires [process namespace sharing](https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/) and access to the Varnish container's `/var/lib/varnish` directory. 

The Varnish exporter is not published as a container image; you must build your own. The following example demonstrates how to build an exporter container image that contains the exporter and the `varnishstat` command.
    
    
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    FROM debian:stable-slim AS stage
    WORKDIR /exporter
    ADD https://github.com/jonnenauha/prometheus_varnish_exporter/releases/download/1.6.1/prometheus_varnish_exporter-1.6.1.linux-amd64.tar.gz /exporter/exporter.tar.gz
    RUN tar -xvf exporter.tar.gz
    RUN chmod +x /exporter/prometheus_varnish_exporter-1.6.1.linux-amd64/prometheus_varnish_exporter
    FROM varnish:9.1.0
    COPY --from=stage /exporter/prometheus_varnish_exporter-1.6.1.linux-amd64/prometheus_varnish_exporter /prometheus_varnish_exporter
    ENTRYPOINT [ "/prometheus_varnish_exporter" ]
    

## Install the Varnish exporter

We recommend that you install the Varnish exporter, [`prometheus_varnish_exporter`](https://github.com/jonnenauha/prometheus_varnish_exporter), as a sidecar to your Varnish workload. For information about using sidecars, see [Extended applications on Kubernetes with multi-container pods](https://learnk8s.io/sidecar-containers-patterns).

To install `prometheus_varnish_exporter` as a sidecar to Varnish, modify your Varnish configuration as shown in the following example:
    
    
    # Copyright 2023 Google LLC
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
      name: varnish
    spec:
      selector:
        matchLabels:
    +     app.kubernetes.io/name: varnish
      template:
        metadata:
          name: varnish
          labels:
    +       app.kubernetes.io/name: varnish
        spec:
          containers:
          - name: varnish
            image: varnish:7.2.0
    +       volumeMounts:
    +         - name: shared-data
    +           mountPath: /var/lib/varnish
    +       env:
    +       - name: VARNISH_HTTP_PORT
    +         value: "8080"
    +     - name: exporter
    +       image: <custom-docker-image>
    +       volumeMounts:
    +         - name: shared-data
    +           mountPath: /var/lib/varnish
    +           readOnly: true
    +       ports:
    +       - containerPort: 9131
    +         name: prometheus
    +     volumes:
    +       - name: shared-data
    +         emptyDir: {}
    +     shareProcessNamespace: true
    

You must add any lines preceded by the `+` symbol to your configuration.

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define a PodMonitoring resource

For target discovery, the Managed Service for Prometheus Operator requires a PodMonitoring resource that corresponds to the Varnish exporter in the same namespace.

You can use the following PodMonitoring configuration:
    
    
    # Copyright 2023 Google LLC
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
      name: varnish
      labels:
        app.kubernetes.io/name: varnish
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      endpoints:
      - port: prometheus
        scheme: http
        interval: 30s
        path: /metrics
      selector:
        matchLabels:
          app.kubernetes.io/name: varnish
    

Ensure that the label selectors and the port match the selectors and port used in Install the Varnish exporter.

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define rules and alerts

You can use the following `Rules` configuration to define alerts on your Varnish metrics:
    
    
    # Copyright 2023 Google LLC
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
    kind: Rules
    metadata:
      name: varnish-rules
      labels:
        app.kubernetes.io/component: rules
        app.kubernetes.io/name: varnish-rules
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      groups:
      - name: varnish
        interval: 30s
        rules:
        - alert: VarnishBackendConnectionFailure
          annotations:
            description: |-
              Varnish backend connection failure
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Varnish backend connection failure (instance {{ $labels.instance }})
          expr: varnish_backend_fail > 0
          for: 5m
          labels:
            severity: critical
        - alert: VarnishHighCacheEvictions
          annotations:
            description: |-
              Varnish high cache evictions
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Varnish high cache evictions (instance {{ $labels.instance }})
          expr: rate(varnish_main_n_obj_purged[5m]) >= 10
          for: 5m
          labels:
            severity: warning
        - alert: VarnishHighServerLimit
          annotations:
            description: |-
              Varnish high server limit
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Varnish high server limit (instance {{ $labels.instance }})
          expr: varnish_main_threads_failed > 0
          for: 5m
          labels:
            severity: critical
        - alert: VarnishSessionsDropped
          annotations:
            description: |-
              Varnish sessions dropped
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Varnish sessions dropped (instance {{ $labels.instance }})
          expr: varnish_main_sessions{type="dropped"} > 0
          for: 5m
          labels:
            severity: critical
    

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

For more information about applying rules to your cluster, see [Managed rule evaluation and alerting](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed).

You can adjust the alert thresholds to suit your application. 

## Verify the configuration

You can use Metrics Explorer to verify that you correctly configured the Varnish exporter. It might take one or two minutes for Cloud Monitoring to ingest your metrics.

To verify the metrics are ingested, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter and run the following query:  

         
         up{job="varnish", cluster="CLUSTER_NAME", namespace="NAMESPACE_NAME"}




## View dashboards

The Cloud Monitoring integration includes the **Varnish Prometheus Overview** dashboard. Dashboards are automatically installed when you configure the integration. You can also view static previews of dashboards without installing the integration. 

To view an installed dashboard, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab.
  3. Choose the **Integrations** category.
  4. Click the name of the dashboard, for example, **Varnish Prometheus Overview**.



To view a static preview of the dashboard, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Kubernetes Engine** deployment-platform filter.
  3. Locate the Varnish integration and click **View Details**.
  4. Select the **Dashboards** tab.



## Troubleshooting

For information about troubleshooting metric ingestion problems, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
