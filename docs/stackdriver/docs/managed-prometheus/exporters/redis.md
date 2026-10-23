---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/redis/
title: Redis \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:10.637351+00:00
---

# Redis  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/redis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Redis Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from Redis. This document shows you how to do the following: 

  * Set up the exporter for Redis to report metrics.
  * Access a predefined dashboard in Cloud Monitoring to view the metrics.
  * Configure alerting rules to monitor the metrics.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [source repository](https://github.com/oliver006/redis_exporter) for the Redis exporter for installation information.

These instructions are provided as an example and are expected to work in most Kubernetes environments. If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

For information about Redis, see [Redis](https://redis.io/). 

## Prerequisites

To collect metrics from Redis by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements: 

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).
  * To use dashboards available in Cloud Monitoring for the Redis integration, you must use `redis_exporter` version v1.43.1 or later. 

For more information about available dashboards, see View dashboards. 




## Install the Redis exporter

We recommend that you install the Redis exporter, [`redis_exporter`](https://github.com/oliver006/redis_exporter), as a sidecar to your Redis workload. For information about using sidecars, see [Extended applications on Kubernetes with multi-container pods](https://learnk8s.io/sidecar-containers-patterns).

To install `redis_exporter` as a sidecar to Redis, modify your Redis configuration as shown in the following example:
    
    
    # Copyright 2022 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https:#www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: redis
      labels:
        app.kubernetes.io/name: redis
    spec:
      selector:
        matchLabels:
    +     app.kubernetes.io/name: redis
      template:
        metadata:
          labels:
    +       app.kubernetes.io/name: redis
        spec:
          containers:
          - name: redis
            image: "redis:6.2"
            ... 
    +     - name: redis-exporter
    +       image: oliver006/redis_exporter:v1.43.1
    +       args: [--include-system-metrics]
    +       resources:
    +         requests:
    +           cpu: 100m
    +           memory: 100Mi
    +       ports:
    +       - containerPort: 9121
        ...
    

You must add any lines preceded by the `+` symbol to your configuration.

These instructions assume you already have a working Redis installation and want to modify it to include an exporter. If you need to also set up Redis, you can configure and apply the [Bitnami Helm chart](https://github.com/bitnami/charts/tree/master/bitnami/redis). Pass in the following configuration values: 

  * `metrics.enabled = true`
  * `metrics.podLabels = {app.kubernetes.io/name: redis}`



To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define a PodMonitoring resource

For target discovery, the Managed Service for Prometheus Operator requires a PodMonitoring resource that corresponds to the Redis exporter in the same namespace.

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
      name: redis
      labels:
        app.kubernetes.io/name: redis
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      selector:
        matchLabels:
          app.kubernetes.io/name: redis
      endpoints:
      - port: 9121
        interval: 30s
    

Ensure that the label selectors and the port match the selectors and port used in Install the Redis exporter.

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define rules and alerts

You can use the following `Rules` configuration to define alerts on your Redis metrics:
    
    
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
      name: redis-rules
      labels:
        app.kubernetes.io/component: rules
        app.kubernetes.io/name: redis-rules
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      groups:
      - name: redis
        interval: 30s
        rules:
        - alert: RedisDown
          annotations:
            description: |-
              Redis instance is down 
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Redis down (instance {{ $labels.instance }})
          expr: redis_up{job="redis"} == 0
          for: 5m
          labels:
            severity: critical
        - alert: RedisOutOfMemory
          annotations:
            description: |-
              Redis is running out of memory (> 90%)
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Redis out of memory (instance {{ $labels.instance }})
          expr: redis_memory_used_bytes{job="redis"} / redis_total_system_memory_bytes{job="redis"}
            * 100 > 90
          for: 5m
          labels:
            severity: warning
        - alert: RedisTooManyConnections
          annotations:
            description: |-
              Redis instance has too many connections
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Redis too many connections (instance {{ $labels.instance }})
          expr: redis_connected_clients{job="redis"} > 100
          for: 5m
          labels:
            severity: warning
        - alert: RedisClusterSlotFail
          annotations:
            description: |-
              Redis cluster has slots fail
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Number of hash slots mapping to a node in FAIL state (instance {{ $labels.instance }})
          expr: redis_cluster_slots_fail{job="redis"} > 0
          for: 5m
          labels:
            severity: warning
        - alert: RedisClusterSlotPfail
          annotations:
            description: |-
              Redis cluster has slots pfail
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Number of hash slots mapping to a node in PFAIL state (instance {{ $labels.instance }})
          expr: redis_cluster_slots_pfail{job="redis"} > 0
          for: 5m
          labels:
            severity: warning
        - alert: RedisClusterStateNotOk
          annotations:
            description: |-
              Redis cluster is not ok 
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Redis cluster state is not ok (instance {{ $labels.instance }})
          expr: redis_cluster_state{job="redis"} == 0
          for: 5m
          labels:
            severity: critical
        - expr: redis_memory_used_rss_bytes{job="redis"} / redis_memory_used_bytes{job="redis"}
          record: redis_memory_fragmentation_ratio
    

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

For more information about applying rules to your cluster, see [Managed rule evaluation and alerting](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed).

This `Rules` configuration was adapted from the rules and alerts contributed to the [`redis_exporter`](https://github.com/oliver006/redis_exporter) repository. 

## Verify the configuration

You can use Metrics Explorer to verify that you correctly configured the Redis exporter. It might take one or two minutes for Cloud Monitoring to ingest your metrics.

To verify the metrics are ingested, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter and run the following query:  

         
         up{job="redis", cluster="CLUSTER_NAME", namespace="NAMESPACE_NAME"}
         




## View dashboards

The Cloud Monitoring integration includes the **Redis Prometheus Overview** dashboard. Dashboards are automatically installed when you configure the integration. You can also view static previews of dashboards without installing the integration. 

To view an installed dashboard, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab.
  3. Choose the **Integrations** category.
  4. Click the name of the dashboard, for example, **Redis Prometheus Overview**.



To view a static preview of the dashboard, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Kubernetes Engine** deployment-platform filter.
  3. Locate the Redis integration and click **View Details**.
  4. Select the **Dashboards** tab.



## Troubleshooting

For information about troubleshooting metric ingestion problems, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
