---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/collect-metrics/
title: Collect metrics from your workloads \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:23:23.470172+00:00
---

# Collect metrics from your workloads  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/collect-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Collect metrics from your workloads Stay organized with collections  Save and categorize content based on your preferences. 

This page outlines the process for scraping metrics from workloads in Google Distributed Cloud (GDC) air-gapped environments to facilitate monitoring and data observability.

You can scrape and collect metrics your components produce over time. The monitoring platform offers a custom API to scrape metrics from running workloads within your Distributed Cloud project namespace. To scrape metrics, you deploy a `MonitoringTarget` custom resource to your project namespace in the Management API server. Upon deployment of this resource, the monitoring platform initiates data collection.

The `MonitoringTarget` custom resource directs the monitoring pipeline to scrape designated pods within your project. These pods must expose an HTTP endpoint that delivers metrics in a Prometheus exposition format, such as OpenMetrics. The scraped metrics are then displayed in your project's Grafana instance, providing insights into your application's operational state.

To configure the `MonitoringTarget` custom resource, you must specify the pods within your project namespace for metric collection. You can customize various settings, including the scraping frequency, the pods' metrics endpoint, labels, and annotations.

## Before you begin

To manage `MonitoringRule` custom resources, request the necessary permissions from your administrator.

### Required IAM roles

Contact your IAM Project Admin to request the following roles:

  * **MonitoringRule Creator** (`monitoringrule-creator`): create `MonitoringRule` custom resources in the project namespace.
  * **MonitoringRule Editor** (`monitoringrule-editor`): edit or modify `MonitoringRule` custom resources in the project namespace.
  * **MonitoringRule Viewer** (`monitoringrule-viewer`): view `MonitoringRule` custom resources in the project namespace.



## Configure the `MonitoringTarget` custom resource

The `MonitoringTarget` custom resource tells the monitoring platform where to collect metrics from. You can specify the pods for which you are collecting metrics, the metrics endpoint of those pods, the scrapping frequency, and any additional settings.

This resource defines the following configurations:

  * **Targets** : The pods and their endpoints within your project that expose metrics.
  * **Scrape interval** : How frequently you want to pull metrics from the selected endpoints.
  * **Label customizations** : Optional rules with any label modifications for metrics.



Choose one of the following methods for specifying metrics endpoints in the `MonitoringTarget` custom resource:

  * **Static endpoints** : You explicitly declare the endpoint (port, path, scheme) in the `MonitoringTarget` configuration.
  * **Annotations** : The pod metric endpoint information is retrieved from annotations within the container's `Deployment` file. This method offers more flexibility if each pod has different endpoints.




###  Static endpoints 

Follow these steps to expose metrics from your selected pods on a statically defined endpoint:

  1. Determine the Distributed Cloud project from which you want to gather metrics for monitoring.

  2. In your pod's specification, declare the port that serves metrics in the `containerPort` field. The following example shows how to declare port `2112` in the pod's specification:
         
         # ...
         spec:
           template:
             spec:
               containers:
               - name: your-container-name
                 ports:
                 - containerPort: 2112
         # ...
         

  3. In your `MonitoringTarget` configuration, specify the endpoint details (port, path, scheme) in the `podMetricsEndpoints` section to match the port you exposed in the pod's specification.

The following YAML file shows an example of a `MonitoringTarget` configuration where every selected pod has to expose metrics on the same endpoint, `http://your-container-name:2112/metrics`:
         
         apiVersion: monitoring.gdc.goog/v1
         kind: MonitoringTarget
         metadata:
           # Choose the same namespace as the workload pods.
           namespace: your-project-namespace
           name: your-container-name
         spec:
           selector:
               # Choose pod labels to consider for this job.
               # Optional: Map of key-value pairs.
               # Default: No filtering by label.
               # To consider every pod in the project namespace, remove selector fields.
             matchLabels:
               app: your-app-label
           podMetricsEndpoints:
             port:
               value: 2112
             path:
               # Choose any value for your endpoint.
               # The /metrics value is an example.
               value: /metrics
             scheme:
               value: http
         

  4. Apply the `MonitoringTarget` configuration to the Management API server within the same namespace as your target pods:
         
         kubectl --kubeconfig KUBECONFIG_PATH apply -f MONITORING_TARGET_NAME.yaml
         

Replace the following:

     * `KUBECONFIG_PATH`: the path to the kubeconfig file for the Management API server.
     * `MONITORING_TARGET_NAME`: the name of the `MonitoringTarget` definition file.



The monitoring platform begins collecting metrics.

###  Annotations 

Follow these steps to expose metrics using annotations if each pod has different endpoints:

  1. Determine the Distributed Cloud project from which you want to gather metrics for monitoring.

  2. Add the following annotations to the `annotations` section of your container's `Deployment` file:

     * `prometheus.io/path`
     * `prometheus.io/port`
     * `prometheus.io/scheme`

The following example shows annotations for metrics on port `2112`:
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: your-container-name
      namespace: your-project-namespace
      labels:
        app: your-app-label
      annotations:
        # These annotations are not required. They demonstrate selecting
        # pod metric endpoints through annotations.
        prometheus.io/path: /metrics
        prometheus.io/port: \"2112\"
        prometheus.io/scheme: http
    

  3. In your `MonitoringTarget` configuration, specify the annotations you added to the container's `Deployment` file in the `podMetricsEndpoints` section. This specification tells the custom resource to gather the metrics endpoint information from annotations on the selected pods.

The following YAML file shows an example of a `MonitoringTarget` configuration using annotations:
         
         apiVersion: monitoring.gdc.goog/v1
         kind: MonitoringTarget
         metadata:
         metadata:
           # Choose the same namespace as the workload pods.
           namespace: your-project-namespace
           name: your-container-name
         spec:
           selector:
             matchLabels:
               app: your-app-label
           podMetricsEndpoints:
             port:
               annotation: prometheus.io/port
             path:
               annotation: prometheus.io/path
             scheme:
               annotation: prometheus.io/scheme
         

  4. Apply the `MonitoringTarget` configuration to the Management API server within the same namespace as your target pods:
         
         kubectl --kubeconfig KUBECONFIG_PATH apply -f MONITORING_TARGET_NAME.yaml
         

Replace the following:

     * `KUBECONFIG_PATH`: the path to the kubeconfig file for the Management API server.
     * `MONITORING_TARGET_NAME`: the name of the `MonitoringTarget` definition file.



The monitoring platform begins collecting metrics.

Refer to the complete `MonitoringTarget` specification and the [API reference documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/monitoring/v1/monitoring-v1#monitoringtarget) for additional fields and options.

## Complete `MonitoringTarget` specification

The following YAML file shows an example for the complete specification of the `MonitoringTarget` custom resource. For more information and a complete description of fields, see the [API reference documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/monitoring/v1/monitoring-v1#monitoringtarget).
    
    
    apiVersion: monitoring.gdc.goog/v1
    kind: MonitoringTarget
    metadata:
      # Choose the same namespace as the workload pods.
      namespace: PROJECT_NAMESPACE
      name: MONITORING_TARGET_NAME
    spec:
      # Choose matching pattern that identifies pods for this job.
      # Optional
      # Relationship between different selectors: AND
      selector:
        # Choose clusters to consider for this job.
        # Optional: List
        # Default: All clusters applicable to this project.
        # Relationship between different list elements: OR
        matchClusters:
        - string
    
        # Choose pod labels to consider for this job.
        # Optional: Map of key-value pairs.
        # Default: No filtering by label.
        # Relationship between different pairs: AND
        matchLabels:
          key1: value1
    
        # Choose annotations to consider for this job.
        # Optional: Map of key-value pairs
        # Default: No filtering by annotation
        # Relationship between different pairs: AND
        matchAnnotations:
          key1: value1
    
      # Configure the endpoint exposed for this job.
      podMetricsEndpoints:
        # Choose a port either through static value or annotation.
        # Optional
        # Annotation takes priority.
        # Default: static port 80
        port:
          value: integer
          annotation: string
    
        # Choose a path either through static value or annotation.
        # Optional
        # Annotation takes priority
        # Default: static path /metrics
        path:
          value: string
          annotation: string
    
        # Choose a scheme either through a static value (http or https) or annotation.
        # Optional
        # Annotation takes priority
        # Default: static scheme http
        scheme:
          value: string
          annotation: string
    
        # Choose the frequency to scrape the metrics endpoint defined in podMetricsEndpoints
        # Optional
        # Default: 60s
        scrapeInterval: string
    
        # Dynamically rewrite the label set of a target before it gets scraped.
        # https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config
        # Optional
        # Default: No filtering by label
        metricsRelabelings:
        - sourceLabels:
          - string
          separator: string
          regex: string
          action: string
          targetLabel: string
          replacement: string
    

Replace the following:

  * `PROJECT_NAMESPACE`: your project namespace.
  * `MONITORING_TARGET_NAME`: the name of the `MonitoringTarget` definition file.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
