---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/prometheus/
title: Prometheus (self-monitoring) \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:26.963884+00:00
---

# Prometheus (self-monitoring)  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/prometheus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Prometheus (self-monitoring) Stay organized with collections  Save and categorize content based on your preferences. 

To ingest Prometheus self-monitoring metrics from Managed Service for Prometheus, apply the following PodMonitoring manifest:
    
    
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
      namespace: gmp-system
      name: collector
      labels:
        app.kubernetes.io/name: collector
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      selector:
        matchLabels:
          app.kubernetes.io/name: collector
      endpoints:
      - port: prom-metrics
        interval: 30s
        metricRelabeling:
        - sourceLabels: [__name__]
          regex: > 
                prometheus_target.*|prometheus_sd.*|net_conntrack_.*
          action: drop
      - port: cfg-rel-metrics
        interval: 30s
    ---
    apiVersion: monitoring.googleapis.com/v1
    kind: PodMonitoring
    metadata:
      namespace: gmp-system
      name: rule-evaluator
      labels:
        app.kubernetes.io/name: rule-evaluator
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      selector:
        matchLabels:
          app.kubernetes.io/name: rule-evaluator
      endpoints:
      - port: r-eval-metrics
        interval: 30s
      - port: cfg-rel-metrics
        interval: 30s
    ---
    apiVersion: monitoring.googleapis.com/v1
    kind: PodMonitoring
    metadata:
      namespace: gmp-system
      name: gmp-operator
      labels:
        app.kubernetes.io/name: gmp-operator
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      selector:
        matchLabels:
          app.kubernetes.io/name: gmp-operator
      endpoints:
      - port: metrics
        interval: 30s
    ---
    apiVersion: monitoring.googleapis.com/v1
    kind: PodMonitoring
    metadata:
      namespace: gmp-system
      name: alertmanager
      labels:
        app.kubernetes.io/name: alertmanager
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      selector:
        matchLabels:
          app.kubernetes.io/name: alertmanager
      endpoints:
      - port: alertmanager
        interval: 30s
      - port: cfg-rel-metrics
        interval: 30s
    

You can install manifests by copying them to a local file and then running `kubectl apply -f FILE_NAME`. You can also [install manifests by using Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
