---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/jetty/
title: Jetty \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:45.408005+00:00
---

# Jetty  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/jetty/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Jetty Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from Jetty. This document shows you how to do the following: 

  * Set up the exporter for Jetty to report metrics.
  * Access a predefined dashboard in Cloud Monitoring to view the metrics.
  * Configure alerting rules to monitor the metrics.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [source repository](https://github.com/bitnami/containers/tree/main/bitnami/jmx-exporter) for the JMX exporter for installation information.

These instructions are provided as an example and are expected to work in most Kubernetes environments. If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

For information about Jetty, see [Jetty](https://www.eclipse.org/jetty/). 

## Prerequisites

To collect metrics from Jetty by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements: 

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).
  * To use dashboards available in Cloud Monitoring for the Jetty integration, you must use `jmx-exporter` version 0.17.0 or later. 

For more information about available dashboards, see View dashboards. 




## Install the Jetty exporter

We recommend that you install the Jetty exporter, [`jmx-exporter`](https://github.com/bitnami/containers/tree/main/bitnami/jmx-exporter), as a sidecar to your Jetty workload. For information about using sidecars, see [Extended applications on Kubernetes with multi-container pods](https://learnk8s.io/sidecar-containers-patterns).

To install `jmx-exporter` as a sidecar to Jetty, modify your Jetty configuration as shown in the following example:
    
    
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
    
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: jetty-exporter
    data:
      config.yaml: |
        hostPort: 127.0.0.1:1099
        rules:
        - pattern: "org.eclipse.jetty.deploy<(.*)><>(.*)"
          name: "jetty_deploy_$2"
          labels:
            labelList: "$1"
        - pattern: "org.eclipse.jetty.deploy.providers<type=(\\w+), id=(\\d+)><>(\\w+)"
          name: "jetty_deploy_providers_$3"
          labels:
            id: "$2"
            type: "$1"
        - pattern: "org.eclipse.jetty.io<context=(.*), type=(.*), id=(\\d+)><>(\\w+)"
          name: "jetty_io_$4"
          labels:
            id: "$3"
            type: "$2"
            context: "$1"
        - pattern: "org.eclipse.jetty.io<type=(.*), id=(\\d+)><>(\\w+)"
          name: "jetty_io_$3"
          labels:
            id: "$2"
            type: "$1"
        - pattern: "org.eclipse.jetty.jmx<type=(\\w+), id=(\\d+)><>(\\w+)"
          name: "jetty_jmx_$3"
          labels:
            id: "$2"
            type: "$1"
        - pattern: "org.eclipse.jetty.logging<type=(\\w+), id=(\\d+)><>(\\w+)"
          name: "jetty_logging_$3"
          labels:
            id: "$2"
            type: "$1"
        - pattern: "org.eclipse.jetty.server<type=(\\w+), id=(\\d+)><>(\\w+)"
          name: "jetty_server_$3"
          labels:
            id: "$2"
            type: "$1"
        - pattern: "org.eclipse.jetty.server<context=(.*), type=(.*), id=(\\d+)><>(\\w+)"
          name: "jetty_server_$4"
          labels:
            id: "$3"
            type: "$2"
            context: "$1"
        - pattern: "org.eclipse.jetty.server.handler<type=(\\w+), id=(\\d+)><>(\\w+)"
          name: "jetty_server_handler_$3"
          labels:
            id: "$2"
            type: "$1"
        - pattern: "org.eclipse.jetty.server.session<type=(.*), id=(\\d+)><>(\\w+)"
          name: "jetty_server_session_$3"
          labels:
            id: "$2"
            type: "$1"
        - pattern: "org.eclipse.jetty.server.session<context=(.*), type=(.*), id=(\\d+)><>(\\w+)"
          name: "jetty_server_session_$4"
          labels:
            id: "$3"
            type: "$2"
            context: "$1"
        - pattern: "org.eclipse.jetty.util<type=(\\w+), id=(\\d+)><>(\\w+)"
          name: "jetty_util_$3"
          labels:
            id: "$2"
            type: "$1"
        - pattern: "org.eclipse.jetty.util.component<type=(\\w+), id=(\\d+)><>(\\w+)"
          name: "jetty_util_component_$3"
          labels:
            id: "$2"
            type: "$1"
        - pattern: "org.eclipse.jetty.servlet<context=(.*), type=(\\w+), id=(\\d+)><>(\\w+)"
          name: "jetty_servlet_$4"
          labels:
            id: "$3"
            type: "$2"
            context: "$1"
        - pattern: "org.eclipse.jetty.servlet<context=(.*), type=(\\w+), name=(\\w+), id=(\\d+)><>(\\w+)"
          name: "jetty_servlet_$5"
          labels:
            id: "$4"
            type: "$2"
            name: "$3"
            context: "$1"
        - pattern: "org.eclipse.jetty.util.thread<type=(\\w+), id=(\\d+)><>(\\w+)"
          name: "jetty_util_thread_$3"
          labels:
            id: "$2"
            type: "$1"
        - pattern: "org.eclipse.jetty.util.thread.strategy<context=(.*), type=(\\w+), id=(\\d+)><>(\\w+)"
          name: "jetty_util_thread_strategy_$4"
          labels:
            id: "$3"
            type: "$2"
            context: "$1"
        - pattern: "org.eclipse.jetty.webapp<context=(.*), type=(\\w+), id=(\\d+)><>(\\w+)"
          name: "jetty_webapp_$4"
          labels:
            id: "$3"
            type: "$2"
            context: "$1"
        - pattern: "org.eclipse.jetty.websocket.common<context=(.*), type=(\\w+), id=(\\d+)><>(\\w+)"
          name: "jetty_websocket_jakarta_common_$4"
          labels:
            id: "$3"
            type: "$2"
            context: "$1"
        - pattern: "org.eclipse.jetty.websocket.jakarta.common<context=(.*), type=(\\w+), id=(\\d+)><>(\\w+)"
          name: "jetty_websocket_jakarta_common_$4"
          labels:
            id: "$3"
            type: "$2"
            context: "$1"
        - pattern: "org.eclipse.jetty.(.*)"
          name: jetty_metric_$1
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: jetty
    spec:
      selector:
        matchLabels:
    +      app.kubernetes.io/name: jetty
      replicas: 1
      template:
        metadata:
          labels:
    +        app.kubernetes.io/name: jetty
        spec:
          containers:
          - name: jetty
            image: jetty:11-jdk17-alpine
    +        ports:
    +        - containerPort: 1099
    +          name: jmx
    +        env:
    +        - name: JAVA_OPTIONS
    +          value: "-Dcom.sun.management.jmxremote.local.only=false -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.port=1099 -Dcom.sun.management.jmxremote.rmi.port=1099"
    +        args:
    +        - "--module=jmx"
    +        - "jetty.threadPool.maxThreads=500"
    +      - name: exporter
    +        image: bitnami/jmx-exporter:0.17.0
    +        ports:
    +        - containerPort: 9000
    +          name: prometheus
    +        command:
    +          - java
    +          - -jar
    +          - jmx_prometheus_httpserver.jar
    +        args:
    +          - "9000"
    +          - /opt/jmx_exporter/config.yaml
    +        volumeMounts:
    +        - mountPath: /opt/jmx_exporter/config.yaml
    +          subPath: config.yaml
    +          name: jetty-exporter
    +      volumes:
    +      - name: jetty-exporter
    +        configMap:
    +          name: jetty-exporter
    +          items:
    +          - key: config.yaml
    +            path: config.yaml
    ---
    

You must add any lines preceded by the `+` symbol to your configuration.

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define a PodMonitoring resource

For target discovery, the Managed Service for Prometheus Operator requires a PodMonitoring resource that corresponds to the JMX exporter in the same namespace.

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
      name: jetty
      labels:
        app.kubernetes.io/name: jetty
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      endpoints:
      - port: prometheus
        scheme: http
        interval: 30s
        path: /metrics
      selector:
        matchLabels:
          app.kubernetes.io/name: jetty
    

Ensure that the label selectors and the port match the selectors and port used in Install the Jetty exporter.

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define rules and alerts

You can use the following `Rules` configuration to define alerts on your Jetty metrics:
    
    
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
      name: jetty-rules
      labels:
        app.kubernetes.io/component: rules
        app.kubernetes.io/name: jetty-rules
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      groups:
      - name: jetty
        interval: 30s
        rules:
        - alert: JettyLongThreadQueue
          annotations:
            description: |-
              Jetty long thread queue
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Jetty long thread queue (instance {{ $labels.instance }})
          expr: jetty_util_thread_queueSize >= 10
          for: 5m
          labels:
            severity: critical
        - alert: JettyNoThreadsAvailable
          annotations:
            description: |-
              Jetty no threads available
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Jetty no threads available (instance {{ $labels.instance }})
          expr: jetty_util_thread_idleThreads == 0
          for: 5m
          labels:
            severity: critical
    

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

For more information about applying rules to your cluster, see [Managed rule evaluation and alerting](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed).

You can adjust the alert thresholds to suit your application. 

## Verify the configuration

You can use Metrics Explorer to verify that you correctly configured the JMX exporter. It might take one or two minutes for Cloud Monitoring to ingest your metrics.

To verify the metrics are ingested, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter and run the following query:  

         
         up{job="jetty", cluster="CLUSTER_NAME", namespace="NAMESPACE_NAME"}




## View dashboards

The Cloud Monitoring integration includes the **Jetty Prometheus Overview** dashboard. Dashboards are automatically installed when you configure the integration. You can also view static previews of dashboards without installing the integration. 

To view an installed dashboard, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab.
  3. Choose the **Integrations** category.
  4. Click the name of the dashboard, for example, **Jetty Prometheus Overview**.



To view a static preview of the dashboard, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Kubernetes Engine** deployment-platform filter.
  3. Locate the Jetty integration and click **View Details**.
  4. Select the **Dashboards** tab.



## Troubleshooting

For information about troubleshooting metric ingestion problems, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
