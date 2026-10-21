---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/haproxy/
title: HAProxy \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:20.158454+00:00
---

# HAProxy  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/haproxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  HAProxy Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from HAProxy. This document shows you how to do the following: 

  * Set up HAProxy to report metrics.
  * Access a predefined dashboard in Cloud Monitoring to view the metrics.
  * Configure alerting rules to monitor the metrics.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [HAProxy documentation](https://github.com/haproxy/haproxy/blob/master/addons/promex/README) for installation information.

These instructions are provided as an example and are expected to work in most Kubernetes environments. If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

For information about HAProxy, see [HAProxy](https://www.haproxy.com/). 

## Prerequisites

To collect metrics from the PROMEX service for HAProxy by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements: 

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).
  * To use dashboards available in Cloud Monitoring for the HAProxy integration, you must use `haproxy_promex` version 2.4 or later. 

For more information about available dashboards, see View dashboards. 


HAProxy exposes Prometheus-format metrics only when it is [built with the service enabled](https://github.com/haproxy/haproxy/blob/master/addons/promex/README) and an appropriate `frontend` is included in the configuration. 

Most of the official Docker images for versions greater than or equal to 2.4 are built with this service enabled.

The following configuration example was built referencing [HAProxy Enterprise documentation](https://www.haproxy.com/documentation/hapee/latest/observability/metrics/prometheus/). It works with the community edition and can be modified to suit specific needs:

## Modify the HAProxy configuration

Modify the HAProxy configuration as shown in the following example:
    
    
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
      name: haproxy
    data:
      haproxy.cfg: |
        ...
    +   frontend prometheus
    +     mode http
    +     bind *:8404
    +     http-request use-service prometheus-exporter if { path /metrics }
        ...
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: haproxy
    spec:
      selector:
        matchLabels:
    +     app.kubernetes.io/name: haproxy
      template:
        metadata:
          labels:
    +       app.kubernetes.io/name: haproxy
        spec:
          containers:
          - name: haproxy
            image: haproxy:2.8
            ports:
    +       - containerPort: 8404
    +         name: prometheus
            volumeMounts:
            - mountPath: /usr/local/etc/haproxy/haproxy.cfg
              subPath: haproxy.cfg
              name: haproxy
          volumes:
          - name: haproxy
            configMap:
              name: haproxy
              items:
              - key: haproxy.cfg
                path: haproxy.cfg

You must add any lines preceded by the `+` symbol to your configuration.

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

To verify that the PROMEX service for HAProxy is emitting metrics on the expected endpoints,do the following:

  1. Set up port forwarding by using the following command: 
         
         kubectl -n NAMESPACE_NAME port-forward POD_NAME 8404
         

  2. Access the endpoint `localhost:8404/metrics` by using the browser or the `curl` utility in another terminal session.



## Define a PodMonitoring resource

For target discovery, the Managed Service for Prometheus Operator requires a PodMonitoring resource that corresponds to the PROMEX service for HAProxy in the same namespace.

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
      name: haproxy
      labels:
        app.kubernetes.io/name: haproxy
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      endpoints:
      - port: prometheus
        scheme: http
        interval: 30s
        path: /metrics
      selector:
        matchLabels:
          app.kubernetes.io/name: haproxy

Ensure that the values of the `port` and `matchLabels` fields match those of the HAProxy pods you want to monitor. 

HAProxy exposes metrics from targets defined in the `bind` configuration option. This option requires a user to define the IP address and port to be listened on for scraping metrics. 

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define rules and alerts

You can use the following `Rules` configuration to define alerts on your HAProxy metrics:
    
    
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
      name: haproxy-rules
      labels:
        app.kubernetes.io/component: rules
        app.kubernetes.io/name: haproxy-rules
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      groups:
      - name: haproxy
        interval: 30s
        rules:
        - alert: HAProxyDown
          annotations:
            description: |-
              HAProxy instance is down
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: HAProxy down (instance {{ $labels.instance }})
          expr: haproxy_server_up{job="haproxy"} == 0
          for: 5m
          labels:
            severity: critical
        - alert: HAProxyTooManyConnections
          annotations:
            description: |-
              HAProxy instance has too many connections
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: HAProxy too many connections (instance {{ $labels.instance }})
          expr: haproxy_frontend_current_sessions{job="haproxy"} / haproxy_frontend_limit_sessions{job="haproxy"} * 100 > 90
          for: 5m
          labels:
            severity: warning

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

For more information about applying rules to your cluster, see [Managed rule evaluation and alerting](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed).

## Verify the configuration

You can use Metrics Explorer to verify that you correctly configured the PROMEX service for HAProxy. It might take one or two minutes for Cloud Monitoring to ingest your metrics.

To verify the metrics are ingested, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter and run the following query:  

         
         up{job="haproxy", cluster="CLUSTER_NAME", namespace="NAMESPACE_NAME"}




## View dashboards

The Cloud Monitoring integration includes the **HAProxy Prometheus Overview** dashboard. Dashboards are automatically installed when you configure the integration. You can also view static previews of dashboards without installing the integration. 

To view an installed dashboard, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab.
  3. Choose the **Integrations** category.
  4. Click the name of the dashboard, for example, **HAProxy Prometheus Overview**.



To view a static preview of the dashboard, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Kubernetes Engine** deployment-platform filter.
  3. Locate the HAProxy integration and click **View Details**.
  4. Select the **Dashboards** tab.



## Troubleshooting

For information about troubleshooting metric ingestion problems, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
