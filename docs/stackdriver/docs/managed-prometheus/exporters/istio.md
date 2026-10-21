---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/istio/
title: Istio \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:36.444240+00:00
---

# Istio  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/istio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Istio Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from Istio. This document shows you how to do the following: 

  * Set up Istio to report metrics.
  * Access a predefined dashboard in Cloud Monitoring to view the metrics.
  * Configure alerting rules to monitor the metrics.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [source repository](https://istio.io/latest/docs/ops/integrations/prometheus) for Istio for installation information.

These instructions are provided as an example and are expected to work in most Kubernetes environments. If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

For information about Istio, see [Istio](https://istio.io). 

## Prerequisites

To collect metrics from Istio by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements: 

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).



Istio exposes Prometheus-format metrics automatically; you do not have to install it separately. You can run the following checks to verify that the Istio Proxy has been injected as a sidecar and that both Istiod, the control plane of Istio, and Istio Proxy are emitting metrics on the expected endpoints.

  * To determine if Istio Proxy is injected as a sidecar, run the following command, which enumerates the containers running in the application's pods:
        
        kubectl get pod -l app=APPLICATION_NAME -n NAMESPACE_NAME -o jsonpath='{.items[0].spec.containers[*].name}'
        

If you see that the pods contain the `istio` sidecar container, then the exporter has been injected. If the sidecar is not injected, then follow the instructions at [Istio: Installing the sidecar](https://istio.io/latest/docs/setup/additional-setup/sidecar-injection/).

  * To verify that metrics are being emitted by the Istio Proxy, run the following command, which inspects the `/stats/prometheus` endpoint of the `istio` on the specified pod:
        
        kubectl exec POD_NAME -n NAMESPACE_NAME -c istio-proxy -- curl -sS 'localhost:15090/stats/prometheus'
        

If you see raw `istio_*` and `envoy_*` Prometheus metrics, then metrics are being emitted correctly.

  * To verify that metrics are being emitted similarly on Istiod, run the following command, which inspects the `/metrics` endpoint of Istiod on one of the pods in the `istiod` deployment:
        
        kubectl exec -n istio-system deployment/istiod -- curl -sS 'localhost:15014/metrics'
        




## Define a PodMonitoring resource

For target discovery, the Managed Service for Prometheus Operator requires a PodMonitoring resource that corresponds to Istio in the same namespace.

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
      name: istiod
      namespace: istio-system
      labels:
        app.kubernetes.io/name: istiod
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      selector:
        matchLabels:
          app: istiod
      endpoints:
      - port: 15014
        interval: 30s
        path: /metrics
      targetLabels:
        fromPod:
        - from: app
          to: app
    ---
    apiVersion: monitoring.googleapis.com/v1
    kind: PodMonitoring
    metadata:
      name: istio-proxy
      labels:
        app.kubernetes.io/name: istio-proxy
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      selector:
        matchLabels:
      endpoints:
      - port: http-envoy-prom
        scheme: http
        interval: 30s
        path: /stats/prometheus
    

Istio requires two separate PodMonitoring resources: One that monitors Istiod and another one that monitors the Istio Proxy sidecars and the ingress and egress gateways. To monitor Istio Proxy metrics across all namespaces in the cluster at once, apply the `istio-proxy` PodMonitoring to every namespace or set up a [ClusterPodMonitoring](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.4.3-gke.0/doc/api.md#clusterpodmonitoring) resource instead of a PodMonitoring resource per namespace. 

If you plan to use the [Istio-provided Grafana dashboards](https://istio.io/latest/docs/tasks/observability/metrics/using-istio-dashboard/) then in addition to the PodMonitoring resources described in this document ensure that you also configured [cAdvisor and Kubelet scraping](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kubelet-cadvisor). 

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define rules and alerts

You can use the following `Rules` configuration to define alerts on your Istio metrics:
    
    
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
      name: istio-rules
      labels:
        app.kubernetes.io/component: rules
        app.kubernetes.io/name: istio-rules
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      groups:
      - name: istio
        interval: 30s
        rules:
        - alert: IstioHighTotalRequestRate
          expr: sum(rate(istio_requests_total{reporter="destination"}[5m])) > 1000
          for: 2m
          labels:
            severity: warning
          annotations:
            summary: Istio high total request rate (instance {{ $labels.instance }})
            description: |-
              Global request rate in the service mesh is unusually high.
                VALUE = {{ $value }}
                LABELS = {{ $labels }}
        - alert: IstioLowTotalRequestRate
          expr: sum(rate(istio_requests_total{reporter="destination"}[5m])) < 100
          for: 2m
          labels:
            severity: warning
          annotations:
            summary: Istio low total request rate (instance {{ $labels.instance }})
            description: |-
              Global request rate in the service mesh is unusually low.
                VALUE = {{ $value }}
                LABELS = {{ $labels }}
        - alert: IstioHigh4xxErrorRate
          expr: sum(rate(istio_requests_total{reporter="destination", response_code=~"4.*"}[5m])) / sum(rate(istio_requests_total{reporter="destination"}[5m])) * 100 > 5
          for: 1m
          labels:
            severity: warning
          annotations:
            summary: Istio high 4xx error rate (instance {{ $labels.instance }})
            description: |-
              High percentage of HTTP 5xx responses in Istio (> 5%).
                VALUE = {{ $value }}
                LABELS = {{ $labels }}
        - alert: IstioHigh5xxErrorRate
          expr: sum(rate(istio_requests_total{reporter="destination", response_code=~"5.*"}[5m])) / sum(rate(istio_requests_total{reporter="destination"}[5m])) * 100 > 5
          for: 1m
          labels:
            severity: warning
          annotations:
            summary: Istio high 5xx error rate (instance {{ $labels.instance }})
            description: |-
              High percentage of HTTP 5xx responses in Istio (> 5%).
                VALUE = {{ $value }}
                LABELS = {{ $labels }}
        - alert: IstioHighRequestLatency
          expr: rate(istio_request_duration_milliseconds_sum{reporter="destination"}[1m]) / rate(istio_request_duration_milliseconds_count{reporter="destination"}[1m]) > 100
          for: 1m
          labels:
            severity: warning
          annotations:
            summary: Istio high request latency (instance {{ $labels.instance }})
            description: |-
              Istio average requests execution is longer than 100ms.
                VALUE = {{ $value }}
                LABELS = {{ $labels }}
        - alert: IstioLatency99Percentile
          expr: histogram_quantile(0.99, sum(rate(istio_request_duration_milliseconds_bucket[1m])) by (destination_canonical_service, destination_workload_namespace, source_canonical_service, source_workload_namespace, le)) > 1
          for: 1m
          labels:
            severity: warning
          annotations:
            summary: Istio latency 99 percentile (instance {{ $labels.instance }})
            description: |-
              Istio 1% slowest requests are longer than 1s.
                VALUE = {{ $value }}
                LABELS = {{ $labels }}
    

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

For more information about applying rules to your cluster, see [Managed rule evaluation and alerting](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed).

This `Rules` configuration was adapted from the [Istio rules](https://awesome-prometheus-alerts.grep.to/rules.html#istio-1) provided by [Awesome Prometheus Alerts](https://github.com/samber/awesome-prometheus-alerts/blob/master/LICENSE). You can adjust the alert thresholds to suit your application. 

## Verify the configuration

You can use Metrics Explorer to verify that you correctly configured Istio. It might take one or two minutes for Cloud Monitoring to ingest your metrics.

To verify the metrics are ingested, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter and run the following query:  

         
         sum(istio_build{cluster="CLUSTER_NAME"}) by (component)
         




## View dashboards

The Cloud Monitoring integration includes the **Istio Envoy Prometheus Overview** dashboard. Dashboards are automatically installed when you configure the integration. You can also view static previews of dashboards without installing the integration. 

To view an installed dashboard, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab.
  3. Choose the **Integrations** category.
  4. Click the name of the dashboard, for example, **Istio Envoy Prometheus Overview**.



To view a static preview of the dashboard, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Kubernetes Engine** deployment-platform filter.
  3. Locate the Istio integration and click **View Details**.
  4. Select the **Dashboards** tab.



## Troubleshooting

For information about troubleshooting metric ingestion problems, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
