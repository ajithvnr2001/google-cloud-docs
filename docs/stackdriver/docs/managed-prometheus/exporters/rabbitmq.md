---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/rabbitmq/
title: RabbitMQ \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:37.398102+00:00
---

# RabbitMQ  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/rabbitmq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  RabbitMQ Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from RabbitMQ. This document shows you how to do the following: 

  * Set up RabbitMQ to report metrics.
  * Access a predefined dashboard in Cloud Monitoring to view the metrics.
  * Configure alerting rules to monitor the metrics.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [RabbitMQ documentation](https://rabbitmq.com/prometheus.html#overview-prometheus) for installation information.

These instructions are provided as an example and are expected to work in most Kubernetes environments. If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

For information about RabbitMQ, see [RabbitMQ](https://rabbitmq.com/). 

## Prerequisites

To collect metrics from the RabbitMQ exporter by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements: 

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).
  * To use dashboards available in Cloud Monitoring for the RabbitMQ integration, you must use `rabbitmq` version v3.8.0 or later. 

For more information about available dashboards, see View dashboards. 


RabbitMQ exposes Prometheus-format metrics automatically; you don't have to install it separately. To verify that the RabbitMQ exporter is emitting metrics on the expected endpoints, do the following: 
  1. Set up port forwarding by using the following command: 
         
         kubectl -n NAMESPACE_NAME port-forward POD_NAME 15692
         

  2. Access the endpoint `localhost:15692/metrics` by using the browser or the `curl` utility in another terminal session.



## Define a PodMonitoring resource

For target discovery, the Managed Service for Prometheus Operator requires a PodMonitoring resource that corresponds to the RabbitMQ exporter in the same namespace.

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
      name: rabbitmq
      labels:
        app.kubernetes.io/name: rabbitmq
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      endpoints:
      - port: prometheus
        scheme: http
        interval: 30s
        path: /metrics
      selector:
        matchLabels:
          # If RabbitMQ is installed via the operator, use this label selector
          app.kubernetes.io/component: rabbitmq
          # If installing RabbitMQ via GCP click-to-deploy, use this instead
          # app.kubernetes.io/component: rabbitmq-server
    

Ensure that the values of the `port` and `matchLabels` fields match those of the RabbitMQ pods that you want to monitor. RabbitMQ deployed by the [operator](https://www.rabbitmq.com/kubernetes/operator/operator-overview.html) contains the labels `app.kubernetes.io/component: rabbitmq` and `prometheus` port. 

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define rules and alerts

You can use the following `Rules` configuration to define alerts on your RabbitMQ metrics:
    
    
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
      name: rabbitmq-rules
      labels:
        app.kubernetes.io/component: rules
        app.kubernetes.io/name: rabbitmq-rules
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      groups:
      - name: rabbitmq
        interval: 30s
        rules:
        - alert: RabbitMQHighUnacknowledgedMessages
          annotations:
            description: |-
              RabbitMQ high unacknowledged messages
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: RabbitMQ high unacknowledged messages (instance {{ $labels.instance }})
          expr: rabbitmq_channel_messages_unacked > 5
          for: 5m
          labels:
            severity: critical
        - alert: RabbitMQHighUnroutableMessages
          annotations:
            description: |-
              RabbitMQ high unroutable messages
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: RabbitMQ high unroutable messages (instance {{ $labels.instance }})
          expr: rate(rabbitmq_channel_messages_unroutable_dropped_total[5m]) > 0
          for: 5m
          labels:
            severity: warning
        - alert: RabbitMQLowDeliveredMessages
          annotations:
            description: |-
              RabbitMQ low delivered messages
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: RabbitMQ low delivered messages (instance {{ $labels.instance }})
          expr: rate(rabbitmq_channel_messages_delivered_total[5m]) < 10
          for: 5m
          labels:
            severity: warning
    

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

For more information about applying rules to your cluster, see [Managed rule evaluation and alerting](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed).

You can adjust the alert thresholds to suit your application. 

## Verify the configuration

You can use Metrics Explorer to verify that you correctly configured the RabbitMQ exporter. It might take one or two minutes for Cloud Monitoring to ingest your metrics.

To verify the metrics are ingested, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter and run the following query:  

         
         up{job="rabbitmq", cluster="CLUSTER_NAME", namespace="NAMESPACE_NAME"}




## View dashboards

The Cloud Monitoring integration includes the **RabbitMQ Prometheus Overview** dashboard. Dashboards are automatically installed when you configure the integration. You can also view static previews of dashboards without installing the integration. 

To view an installed dashboard, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab.
  3. Choose the **Integrations** category.
  4. Click the name of the dashboard, for example, **RabbitMQ Prometheus Overview**.



To view a static preview of the dashboard, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Kubernetes Engine** deployment-platform filter.
  3. Locate the RabbitMQ integration and click **View Details**.
  4. Select the **Dashboards** tab.



## Troubleshooting

For information about troubleshooting metric ingestion problems, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
