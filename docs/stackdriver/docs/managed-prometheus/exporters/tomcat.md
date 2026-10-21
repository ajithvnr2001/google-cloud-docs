---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/tomcat/
title: Apache Tomcat \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:17.985465+00:00
---

# Apache Tomcat  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/tomcat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Apache Tomcat Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from Apache Tomcat. This document shows you how to do the following: 

  * Set up the exporter for Tomcat to report metrics.
  * Access a predefined dashboard in Cloud Monitoring to view the metrics.
  * Configure alerting rules to monitor the metrics.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [source repository](https://github.com/bitnami/containers/tree/main/bitnami/jmx-exporter) for the JMX exporter for installation information.

These instructions are provided as an example and are expected to work in most Kubernetes environments. If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

For information about Apache Tomcat, see [Apache Tomcat](https://tomcat.apache.org/). 

## Prerequisites

To collect metrics from Tomcat by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements: 

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).
  * To use dashboards available in Cloud Monitoring for the Tomcat integration, you must use `jmx-exporter` version 0.17.0 or later. 

For more information about available dashboards, see View dashboards. 


Tomcat supports JMX, which can be enabled by configuring the `CATALINA_OPTS` environment variable. 

## Install the Tomcat exporter

We recommend that you install the Tomcat exporter, [`jmx-exporter`](https://github.com/bitnami/containers/tree/main/bitnami/jmx-exporter), as a sidecar to your Tomcat workload. For information about using sidecars, see [Extended applications on Kubernetes with multi-container pods](https://learnk8s.io/sidecar-containers-patterns).

To install `jmx-exporter` as a sidecar to Tomcat, modify your Tomcat configuration as shown in the following example:
    
    
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
      name: tomcat-exporter
    data:
      config.yml: |
        hostPort: 127.0.0.1:9010
        lowercaseOutputLabelNames: true
        lowercaseOutputName: true
        rules:
        - pattern: 'Catalina<type=GlobalRequestProcessor, name=\"(\w+-\w+)-(\d+)\"><>(\w+):'
          name: tomcat_$3_total
          labels:
            port: "$2"
            protocol: "$1"
          help: Tomcat global $3
          type: COUNTER
        - pattern: 'Catalina<j2eeType=Servlet, WebModule=//([-a-zA-Z0-9+&@#/%?=~_|!:.,;]*[-a-zA-Z0-9+&@#/%=~_|]), name=([-a-zA-Z0-9+/$%~_-|!.]*), J2EEApplication=none, J2EEServer=none><>(requestCount|maxTime|processingTime|errorCount):'
          name: tomcat_servlet_$3_total
          labels:
            module: "$1"
            servlet: "$2"
          help: Tomcat servlet $3 total
          type: COUNTER
        - pattern: 'Catalina<type=ThreadPool, name="(\w+-\w+)-(\d+)"><>(currentThreadCount|currentThreadsBusy|keepAliveCount|pollerThreadCount|connectionCount):'
          name: tomcat_threadpool_$3
          labels:
            port: "$2"
            protocol: "$1"
          help: Tomcat threadpool $3
          type: GAUGE
        - pattern: 'Catalina<type=Manager, host=([-a-zA-Z0-9+&@#/%?=~_|!:.,;]*[-a-zA-Z0-9+&@#/%=~_|]), context=([-a-zA-Z0-9+/$%~_-|!.]*)><>(processingTime|sessionCounter|rejectedSessions|expiredSessions):'
          name: tomcat_session_$3_total
          labels:
            context: "$2"
            host: "$1"
          help: Tomcat session $3 total
          type: COUNTER
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: tomcat
    spec:
      selector:
        matchLabels:
    +     app.kubernetes.io/name: tomcat
      template:
        metadata:
          labels:
    +       app.kubernetes.io/name: tomcat
        spec:
          containers:
            - name: tomcat
              image: tomcat:9.0.46-jdk11-openjdk-buster
              ports:
                - containerPort: 8080
                  name: http
              env:
    +           - name: CATALINA_OPTS
    +             value: "-Dcom.sun.management.jmxremote.local.only=false -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.port=9010 -Dcom.sun.management.jmxremote.rmi.port=9010"
    +       - name: exporter
    +         image: bitnami/jmx-exporter:0.17.0
    +         ports:
    +           - containerPort: 9113
    +             name: prometheus
    +         command:
    +           - java
    +           - -jar
    +           - jmx_prometheus_httpserver.jar
    +         args:
    +           - "9113"
    +           - /opt/jmx_exporter/config.yml
    +         volumeMounts:
    +           - mountPath: /opt/jmx_exporter/config.yml
    +             subPath: config.yml
    +             name: tomcat-exporter
    +     volumes:
    +       - name: tomcat-exporter
    +         configMap:
    +           name: tomcat-exporter
    +           items:
    +             - key: config.yml
    +               path: config.yml
    

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
      name: tomcat
      labels:
        app.kubernetes.io/name: tomcat
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      endpoints:
      - port: prometheus
        scheme: http
        interval: 30s
        path: /metrics
      selector:
        matchLabels:
          app.kubernetes.io/name: tomcat
    

Ensure that the label selectors and the port match the selectors and port used in Install the Tomcat exporter.

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define rules and alerts

You can use the following `Rules` configuration to define alerts on your Tomcat metrics:
    
    
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
      name: tomcat-rules
      labels:
        app.kubernetes.io/component: rules
        app.kubernetes.io/name: tomcat-rules
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      groups:
      - name: tomcat
        interval: 30s
        rules:
        - alert: TomcatHighRequestRate
          annotations:
            description: |-
              Tomcat high request rate
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Tomcat high request rate (instance {{ $labels.instance }})
          expr: rate(tomcat_requestcount_total[5m]) >= 100
          for: 5m
          labels:
            severity: warning
        - alert: TomcatLowRequestRate
          annotations:
            description: |-
              Tomcat low request rate
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Tomcat low request rate (instance {{ $labels.instance }})
          expr: rate(tomcat_requestcount_total[5m]) <= 10
          for: 5m
          labels:
            severity: warning
        - alert: TomcatHighErrorRate
          annotations:
            description: |-
              Tomcat high error rate
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Tomcat high error rate (instance {{ $labels.instance }})
          expr: rate(tomcat_errorcount_total[5m]) > 100
          for: 5m
          labels:
            severity: warning
    

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

         
         up{job="tomcat", cluster="CLUSTER_NAME", namespace="NAMESPACE_NAME"}




## View dashboards

The Cloud Monitoring integration includes the **Tomcat Prometheus Overview** dashboard. Dashboards are automatically installed when you configure the integration. You can also view static previews of dashboards without installing the integration. 

To view an installed dashboard, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab.
  3. Choose the **Integrations** category.
  4. Click the name of the dashboard, for example, **Tomcat Prometheus Overview**.



To view a static preview of the dashboard, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Kubernetes Engine** deployment-platform filter.
  3. Locate the Apache Tomcat integration and click **View Details**.
  4. Select the **Dashboards** tab.



## Troubleshooting

For information about troubleshooting metric ingestion problems, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
