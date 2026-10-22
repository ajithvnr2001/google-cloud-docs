---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/nginx/
title: Nginx \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:37.290719+00:00
---

# Nginx  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/nginx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Nginx Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from Nginx. This document shows you how to do the following: 

  * Set up the exporter for Nginx to report metrics.
  * Access a predefined dashboard in Cloud Monitoring to view the metrics.
  * Configure alerting rules to monitor the metrics.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [source repository](https://github.com/nginxinc/nginx-prometheus-exporter) for the Nginx exporter for installation information.

These instructions are provided as an example and are expected to work in most Kubernetes environments. If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

For information about Nginx, see [Nginx](https://www.nginx.com/). 

## Prerequisites

To collect metrics from Nginx by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements: 

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).
  * To use dashboards available in Cloud Monitoring for the Nginx integration, you must use `nginx-prometheus-exporter` version v0.10.0 or later. 

For more information about available dashboards, see View dashboards. 




## Install the Nginx exporter

We recommend that you install the Nginx exporter, [`nginx-prometheus-exporter`](https://github.com/nginxinc/nginx-prometheus-exporter), as a sidecar to your Nginx workload. For information about using sidecars, see [Extended applications on Kubernetes with multi-container pods](https://learnk8s.io/sidecar-containers-patterns).

To install `nginx-prometheus-exporter` as a sidecar to Nginx, modify your Nginx configuration as shown in the following example:
    
    
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
    
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: nginx
    data:
      default.conf: |
        server {
            listen       80 default_server;
            server_name  _;
            location / {
                root   /usr/share/nginx/html;
                index  index.html index.htm;
            }
            error_page   500 502 503 504  /50x.html;
            location = /50x.html {
                root   /usr/share/nginx/html;
            }
    +       location /status {
    +           stub_status on;
    +           access_log off;
    +           allow 127.0.0.1;
    +           allow 10.0.0.0/8;
    +           allow 172.16.0.0/12;
    +           allow 192.168.0.0/16;
    +           deny all;
    +       }
        }
    ---
    apiVersion: apps/v1
    kind: Deployment
    spec:
      ...
      template:
        metadata:
          labels:
    +       app.kubernetes.io/name: nginx
        spec:
          containers:
    +     - name: nginx-exporter
    +       image: nginx/nginx-prometheus-exporter:0.10.0
    +       args:
    +       - "-nginx.scrape-uri=http://localhost/status"
    +       ports:
    +       - containerPort: 9113
    +         name: prometheus
    +       readinessProbe:
    +         httpGet:
    +           path: /metrics
    +           port: prometheus
    +       livenessProbe:
    +         httpGet:
    +           path: /metrics
    +           port: prometheus
          - name: nginx
            image: nginx:1.14.2
    +       ports:
    +       - containerPort: 80
    +         name: http
    +       readinessProbe:
    +         httpGet:
    +           path: /status
    +           port: http
    +       livenessProbe:
    +         httpGet:
    +           path: /status
    +           port: http
    +       volumeMounts:
    +       - mountPath: /etc/nginx/conf.d/default.conf
    +         subPath: default.conf
    +         name: config
    +     volumes:
    +     - name: config
    +       configMap:
    +         name: nginx
    +         items:
    +         - key: default.conf
    +           path: default.conf
    

You must add any lines preceded by the `+` symbol to your configuration.

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define a PodMonitoring resource

For target discovery, the Managed Service for Prometheus Operator requires a PodMonitoring resource that corresponds to the Nginx exporter in the same namespace.

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
      name: nginx
      labels:
        app.kubernetes.io/name: nginx
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      endpoints:
      - port: prometheus
        scheme: http
        interval: 30s
        path: /metrics
      selector:
        matchLabels:
          app.kubernetes.io/name: nginx
    

Ensure that the label selectors and the port match the selectors and port used in Install the Nginx exporter.

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define rules and alerts

You can use the following `Rules` configuration to define alerts on your Nginx metrics:
    
    
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
      name: nginx-rules
      labels:
        app.kubernetes.io/component: rules
        app.kubernetes.io/name: nginx-rules
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      groups:
      - name: nginx
        interval: 30s
        rules:
        - alert: NginxDown
          annotations:
            description: |-
              Nginx instance is down
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Nginx down (instance {{ $labels.instance }})
          expr: nginx_up{job="nginx"} == 0
          for: 5m
          labels:
            severity: critical
        - alert: NginxDroppedConnections
          annotations:
            description: |-
             Too many dropped connections (> 5%)
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Number of dropped connections is high (instance {{ $labels.instance }})
          expr: (rate(nginx_connections_accepted{job="nginx"}[1m]) - rate(nginx_connections_handled{job="nginx"}[1m])) / rate(nginx_connections_accepted{job="nginx"}[1m]) > 0.05
          for: 5m
          labels:
            severity: warning
        - alert: NginxTrafficSpike
          annotations:
            description: |-
              Increase in total number of HTTP requests received (> 20%)
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Spike in HTTP traffic (instance {{ $labels.instance }})
          expr: rate(nginx_http_requests_total{job="nginx"}[1m])/ rate(nginx_http_requests_total{job="nginx"}[1m] offset 5m) > 1.2
          for: 5m
          labels:
            severity: warning
        - alert: NginxTrafficDrop
          annotations:
            description: |-
               Decrease in total number of HTTP requests received (> 20%)
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Drop in HTTP traffic (instance {{ $labels.instance }})
          expr: rate(nginx_http_requests_total{job="nginx"}[1m])/ rate(nginx_http_requests_total{job="nginx"}[1m] offset 5m) < 0.8
          for: 5m
          labels:
            severity: warning
    

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

For more information about applying rules to your cluster, see [Managed rule evaluation and alerting](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed).

You can adjust the alert thresholds to suit your application. 

## Verify the configuration

You can use Metrics Explorer to verify that you correctly configured the Nginx exporter. It might take one or two minutes for Cloud Monitoring to ingest your metrics.

To verify the metrics are ingested, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter and run the following query:  

         
         up{job="nginx", cluster="CLUSTER_NAME", namespace="NAMESPACE_NAME"}
         




## View dashboards

The Cloud Monitoring integration includes the **Nginx Prometheus Overview** dashboard. Dashboards are automatically installed when you configure the integration. You can also view static previews of dashboards without installing the integration. 

To view an installed dashboard, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab.
  3. Choose the **Integrations** category.
  4. Click the name of the dashboard, for example, **Nginx Prometheus Overview**.



To view a static preview of the dashboard, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Kubernetes Engine** deployment-platform filter.
  3. Locate the Nginx integration and click **View Details**.
  4. Select the **Dashboards** tab.



## Troubleshooting

For information about troubleshooting metric ingestion problems, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
