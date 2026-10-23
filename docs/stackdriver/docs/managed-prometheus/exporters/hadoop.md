---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/hadoop/
title: Apache Hadoop \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:48.052982+00:00
---

# Apache Hadoop  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/hadoop/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Apache Hadoop Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from Apache Hadoop. This document shows you how to do the following: 

  * Set up the exporter for Hadoop to report metrics.
  * Access a predefined dashboard in Cloud Monitoring to view the metrics.
  * Configure alerting rules to monitor the metrics.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [source repository](https://github.com/bitnami/containers/tree/main/bitnami/jmx-exporter) for the JMX exporter for installation information.

These instructions are provided as an example and are expected to work in most Kubernetes environments. If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

For information about Apache Hadoop, see [Apache Hadoop](https://hadoop.apache.org/). 

## Prerequisites

To collect metrics from Hadoop by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements: 

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).
  * To use dashboards available in Cloud Monitoring for the Hadoop integration, you must use `jmx-exporter` version 0.17.0 or later. 

For more information about available dashboards, see View dashboards. 


Ensure that the values of the `port` and `matchLabels` fields match those of the Hadoop pods you want to monitor. NameNodes and DataNodes must be configured to accept remote JMX connections. This configuration can be done by setting the `NAMENODE_HDFS_OPTS` and `DATANODE_HDFS_OPTS` environment variables as described in the Hadoop [Unix Shell Guide](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/UnixShellGuide.html). 

## Install the Hadoop exporter

We recommend that you install the Hadoop exporter, [`jmx-exporter`](https://github.com/bitnami/containers/tree/main/bitnami/jmx-exporter), as a sidecar to your Hadoop workload. For information about using sidecars, see [Extended applications on Kubernetes with multi-container pods](https://learnk8s.io/sidecar-containers-patterns).

To install `jmx-exporter` as a sidecar to Hadoop, modify your Hadoop configuration as shown in the following example:
    
    
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
    
    + apiVersion: v1
    + kind: ConfigMap
    + metadata:
    +   name: hadoop-exporter
    + data:
    +   config.yaml: |
    +     hostPort: localhost:1026
    +     lowercaseOutputName: true
    +     lowercaseOutputLabelNames: true
    ---
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: hadoop-hdfs
    spec:
      serviceName: hadoop-hdfs
      selector:
        matchLabels:
    +     app.kubernetes.io/name: hadoop
      template:
        metadata:
          labels:
    +       app.kubernetes.io/name: hadoop
        spec:
          containers:
          - name: hadoop-hdfs
            image: "farberg/apache-hadoop:3.3.2"
    +       env:
    +         - name: HDFS_NAMENODE_OPTS
    +           value: "-Dcom.sun.management.jmxremote=true -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.port=1026"
            command:
            - "/bin/bash"
            - "/tmp/hadoop-config/bootstrap.sh"
            - "-d"
    +       ports:
    +       - containerPort: 1026
    +         name: jmx
    +     - name: exporter
    +       image: bitnami/jmx-exporter:0.17.0
    +       command:
    +         - java
    +         - -jar
    +         - jmx_prometheus_httpserver.jar
    +       args:
    +         - "9900"
    +         - config.yaml
    +       ports:
    +       - containerPort: 9900
    +         name: prometheus
    +       volumeMounts:
    +       - mountPath: /opt/bitnami/jmx-exporter/config.yaml
    +         subPath: config.yaml
    +         name: hadoop-exporter
    +     volumes:
    +     - name: hadoop-exporter
    +       configMap:
    +         name: hadoop-exporter
    +         items:
    +         - key: config.yaml
    +           path: config.yaml
    

You must add any lines preceded by the `+` symbol to your configuration.

These instructions are based on changes made to a [helm chart](https://artifacthub.io/packages/helm/apache-hadoop-helm/hadoop). The templates can be downloaded and altered. The preceding example assumes everything is in a single YAML file. 

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
      name: hadoop
      labels:
        app.kubernetes.io/name: hadoop
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      endpoints:
      - port: prometheus
        scheme: http
        interval: 30s
        path: /metrics
      selector:
        matchLabels:
          app.kubernetes.io/name: hadoop
    

Ensure that the label selectors and the port match the selectors and port used in Install the Hadoop exporter.

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define rules and alerts

You can use the following `Rules` configuration to define alerts on your Hadoop metrics:
    
    
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
      name: hadoop-rules
      labels:
        app.kubernetes.io/component: rules
        app.kubernetes.io/name: hadoop-rules
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      groups:
      - name: hadoop
        interval: 30s
        rules:
        - alert: HadoopDown
          annotations:
            description: |-
              Hadoop instance is down
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Hadoop down (instance {{ $labels.instance }})
          expr: hadoop_namenode_numdeaddatanodes > 0
          for: 5m
          labels:
            severity: critical
        - alert: HadoopLowAvailableCapacity
          annotations:
            description: |-
              Hadoop low available capacity
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Hadoop low available capacity (instance {{ $labels.instance }})
          expr: (hadoop_namenode_capacityused/hadoop_namenode_capacitytotal) > 0.8
          for: 5m
          labels:
            severity: critical
        - alert: HadoopVolumeFailure
          annotations:
            description: |-
              Hadoop volume failure
                VALUE = {{ $value }}
                LABELS: {{ $labels }}
            summary: Hadoop volume failure (instance {{ $labels.instance }})
          expr: hadoop_namenode_volumefailurestotal > 0
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

         
         up{job="hadoop", cluster="CLUSTER_NAME", namespace="NAMESPACE_NAME"}




## View dashboards

The Cloud Monitoring integration includes the **Hadoop Prometheus Overview** dashboard. Dashboards are automatically installed when you configure the integration. You can also view static previews of dashboards without installing the integration. 

To view an installed dashboard, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab.
  3. Choose the **Integrations** category.
  4. Click the name of the dashboard, for example, **Hadoop Prometheus Overview**.



To view a static preview of the dashboard, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Kubernetes Engine** deployment-platform filter.
  3. Locate the Apache Hadoop integration and click **View Details**.
  4. Select the **Dashboards** tab.



## Troubleshooting

For information about troubleshooting metric ingestion problems, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
