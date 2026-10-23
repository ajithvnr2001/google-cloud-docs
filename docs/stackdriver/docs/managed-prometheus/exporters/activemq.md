---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/activemq/
title: Apache ActiveMQ \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:37.282961+00:00
---

# Apache ActiveMQ  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/activemq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Apache ActiveMQ Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from Apache ActiveMQ. This document shows you how to do the following: 

  * Set up the exporter for ActiveMQ to report metrics.
  * Access a predefined dashboard in Cloud Monitoring to view the metrics.
  * Configure alerting rules to monitor the metrics.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [source repository](https://github.com/bitnami/containers/tree/main/bitnami/jmx-exporter#readme) for the JMX exporter for installation information.

These instructions are provided as an example and are expected to work in most Kubernetes environments. If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

For information about Apache ActiveMQ, see [ActiveMQ](https://activemq.apache.org/). 

## Prerequisites

To collect metrics from ActiveMQ by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements: 

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).
  * To use dashboards available in Cloud Monitoring for the ActiveMQ integration, you must use `jmx-exporter` version 0.17.0 or later. 

For more information about available dashboards, see View dashboards. 


ActiveMQ Brokers can be configured for [JMX](https://activemq.apache.org/jmx) by setting the `ACTIVEMQ_JMX` and `ACTIVEMQ_OPTS` environment variables. 

## Install the ActiveMQ exporter

We recommend that you install the ActiveMQ exporter, [`jmx-exporter`](https://github.com/bitnami/containers/tree/main/bitnami/jmx-exporter#readme), as a sidecar to your ActiveMQ workload. For information about using sidecars, see [Extended applications on Kubernetes with multi-container pods](https://learnk8s.io/sidecar-containers-patterns).

To install `jmx-exporter` as a sidecar to ActiveMQ, modify your ActiveMQ configuration as shown in the following example:
    
    
    # Copyright 2022 Google LLC
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
      name: activemq-exporter
    data:
      config.yaml: |
        hostPort: localhost:1099
        lowercaseOutputName: true
        lowercaseOutputLabelNames: true
        blacklistObjectNames:
          - "org.apache.activemq:clientId=*,*"
        whitelistObjectNames:
          - "org.apache.activemq:destinationType=Queue,*"
          - "org.apache.activemq:destinationType=Topic,*"
          - "org.apache.activemq:type=Broker,brokerName=*"
          - "org.apache.activemq:type=Topic,brokerName=*"
    
        rules:
        - pattern: org.apache.activemq<type=Broker, brokerName=(\S*), destinationType=Queue, destinationName=(\S*)><>(\w+)
          name: activemq_queue_$3
          attrNameSnakeCase: true
          labels:
            destination: $2
    
        - pattern: org.apache.activemq<type=Broker, brokerName=(\S*), destinationType=Topic, destinationName=(\S*)><>(\w+)
          name: activemq_topic_$3
          attrNameSnakeCase: true
          labels:
            destination: $2
    
        - pattern: org.apache.activemq<type=Broker, brokerName=(\S*)><>CurrentConnectionsCount
          name: activemq_connections
          type: GAUGE
    
        - pattern: org.apache.activemq<type=Broker, brokerName=(\S*)><>Total(.*)Count
          name: activemq_$2_total
          type: COUNTER
    
        - pattern: org.apache.activemq<type=Broker, brokerName=(\S*)><>(.*)PercentUsage
          name: activemq_$2_usage_ratio
          type: GAUGE
          valueFactor: 0.01
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: activemq
    spec:
      selector:
        matchLabels:
    +     app.kubernetes.io/name: activemq
      template:
        metadata:
          labels:
    +       app.kubernetes.io/name: activemq
        spec:
          containers:
          - name: activemq
            image: rmohr/activemq:5.15.9-alpine
    +       ports:
    +         - containerPort: 1099
    +           name: jmx
    +       env:
    +         - name: ACTIVEMQ_JMX
    +           value: "1099"
    +         - name: ACTIVEMQ_OPTS
    +           value: "-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=1099 -Dcom.sun.management.jmxremote.rmi.port=1099 -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=false"
    +     - name: exporter
    +       image: bitnami/jmx-exporter:0.17.0
    +       command:
    +         - java
    +         - -jar
    +         - jmx_prometheus_httpserver.jar
    +       args:
    +         - "9000"
    +         - config.yaml
    +       ports:
    +       - containerPort: 9000
    +         name: prometheus
    +       volumeMounts:
    +       - mountPath: /opt/bitnami/jmx-exporter/config.yaml
    +         subPath: config.yaml
    +         name: activemq-exporter
    +     volumes:
    +     - name: activemq-exporter
    +       configMap:
    +         name: activemq-exporter
    +         items:
    +         - key: config.yaml
    +           path: config.yaml

You must add any lines preceded by the `+` symbol to your configuration.

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define a PodMonitoring resource

For target discovery, the Managed Service for Prometheus Operator requires a PodMonitoring resource that corresponds to the JMX exporter in the same namespace.

You can use the following PodMonitoring configuration:
    
    
    # Copyright 2022 Google LLC
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
      name: activemq
      labels:
        app.kubernetes.io/name: activemq
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      endpoints:
      - port: prometheus
        scheme: http
        interval: 30s
        path: /metrics
      selector:
        matchLabels:
          app.kubernetes.io/name: activemq

Ensure that the label selectors and the port match the selectors and port used in Install the ActiveMQ exporter.

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define rules and alerts

You can use the following `Rules` configuration to define alerts on your ActiveMQ metrics:
    
    
    # Copyright 2022 Google LLC
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
      name: activemq-rules
      labels:
        app.kubernetes.io/component: rules
        app.kubernetes.io/name: activemq-rules
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      groups:
      - name: activemq
        interval: 30s
        rules:
        - alert: ActiveMQNoConnections
          annotations:
            description: |-
              ActiveMQ no connections
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: ActiveMQ down (instance {{ $labels.instance }})
          expr: activemq_connections_total{job="activemq"} == 0
          for: 5m
          labels:
            severity: warning
        - alert: ActiveMQHighStoreUsage
          annotations:
            description: |-
              ActiveMQ high store usage
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: ActiveMQ high store usage (instance {{ $labels.instance }})
          expr: activemq_store_usage_ratio{job="activemq"} > 0.9
          for: 5m
          labels:
            severity: warning
        - alert: ActiveMQHighTempStoreUsage
          annotations:
            description: |-
              ActiveMQ high temp store usage
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: ActiveMQ high temp store usage (instance {{ $labels.instance }})
          expr: activemq_temp_usage_ratio{job="activemq"} > 0.9
          for: 5m
          labels:
            severity: warning

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

For more information about applying rules to your cluster, see [Managed rule evaluation and alerting](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed).

## Verify the configuration

You can use Metrics Explorer to verify that you correctly configured the JMX exporter. It might take one or two minutes for Cloud Monitoring to ingest your metrics.

To verify the metrics are ingested, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter and run the following query:  

         
         up{job="activemq", cluster="CLUSTER_NAME", namespace="NAMESPACE_NAME"}




## View dashboards

The Cloud Monitoring integration includes the **ActiveMQ Prometheus Overview** dashboard. Dashboards are automatically installed when you configure the integration. You can also view static previews of dashboards without installing the integration. 

To view an installed dashboard, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab.
  3. Choose the **Integrations** category.
  4. Click the name of the dashboard, for example, **ActiveMQ Prometheus Overview**.



To view a static preview of the dashboard, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Kubernetes Engine** deployment-platform filter.
  3. Locate the Apache ActiveMQ integration and click **View Details**.
  4. Select the **Dashboards** tab.



## Troubleshooting

For information about troubleshooting metric ingestion problems, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
