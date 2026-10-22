---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/etcd/
title: etcd \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:53.782759+00:00
---

# etcd  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/etcd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  etcd Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from etcd. This document shows you how to do the following: 

  * Set up etcd to report metrics.
  * Access a predefined dashboard in Cloud Monitoring to view the metrics.
  * Configure alerting rules to monitor the metrics.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [etcd documentation](https://etcd.io/docs/v3.1/op-guide/monitoring/) for installation information.

These instructions are provided as an example and are expected to work in most Kubernetes environments. If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

For information about etcd, see [etcd](https://etcd.io/). 

## Prerequisites

To collect metrics from the etcd exporter by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements: 

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).

etcd exposes Prometheus-format metrics automatically; you do not have to install it separately. To verify that the etcd exporter is emitting metrics on the expected endpoints, do the following: 
  1. Set up port forwarding by using the following command:
         
         kubectl -n NAMESPACE_NAME port-forward POD_NAME 2379
         

  2. Access the endpoint `localhost:2379/metrics` by using the browser or the `curl` utility in another terminal session.


**Note:** these instructions are only applicable for scraping metrics from a self-deployed instance of etcd. Collecting metrics from the etcd instance that runs within the GKE control plane is not supported.

## Define a PodMonitoring resource

For target discovery, the Managed Service for Prometheus Operator requires a PodMonitoring resource that corresponds to the etcd exporter in the same namespace.

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
      name: etcd
      labels:
        app.kubernetes.io/name: etcd
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      endpoints:
      - port: 2379
        scheme: http
        interval: 30s
        path: /metrics
      selector:
        matchLabels:
          app.kubernetes.io/name: etcd
    

Ensure that the values of the `port` and `matchLabels` fields match those of the etcd pods you want to monitor. Deploying etcd using this [helm chart](https://artifacthub.io/packages/helm/bitnami/etcd) will contain the label `app.kubernetes.io/name: etcd` and `client` port. 

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define rules and alerts

You can use the following `Rules` configuration to define alerts on your etcd metrics:
    
    
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
      name: etcd-rules
      labels:
        app.kubernetes.io/component: rules
        app.kubernetes.io/name: etcd-rules
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      groups:
      - name: etcd
        interval: 30s
        rules:
        - alert: EtcdLongFsyncDuration
          annotations:
            description: |-
              Etcd long fsync duration
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Etcd long fsync duration (instance {{ $labels.instance }})
          expr: histogram_quantile(0.9, rate(etcd_disk_wal_fsync_duration_seconds_bucket[10m])) > 0.1
          for: 5m
          labels:
            severity: critical
        - alert: EtcdRapidLeaderChanges
          annotations:
            description: |-
              Etcd rapid leader changes
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Etcd rapid leader changes (instance {{ $labels.instance }})
          expr: etcd_server_leader_changes_seen_total >= 0.05
          for: 5m
          labels:
            severity: critical
    

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

For more information about applying rules to your cluster, see [Managed rule evaluation and alerting](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed).

You can adjust the alert thresholds to suit your application. 

## Verify the configuration

You can use Metrics Explorer to verify that you correctly configured the etcd exporter. It might take one or two minutes for Cloud Monitoring to ingest your metrics.

To verify the metrics are ingested, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter and run the following query:  

         
         up{job="etcd", cluster="CLUSTER_NAME", namespace="NAMESPACE_NAME"}




## View dashboards

The Cloud Monitoring integration includes the **etcd Prometheus Overview** dashboard. Dashboards are automatically installed when you configure the integration. You can also view static previews of dashboards without installing the integration. 

To view an installed dashboard, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab.
  3. Choose the **Integrations** category.
  4. Click the name of the dashboard, for example, **etcd Prometheus Overview**.



To view a static preview of the dashboard, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Kubernetes Engine** deployment-platform filter.
  3. Locate the etcd integration and click **View Details**.
  4. Select the **Dashboards** tab.



## Troubleshooting

For information about troubleshooting metric ingestion problems, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
