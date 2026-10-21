---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/server/http/
title: HTTP server \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:59.630263+00:00
---

# HTTP server  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/server/http/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  HTTP server Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from the HTTP requests served by your application. This document describes how to do the following: 

  * Set up your application to export HTTP metrics in a predefined format.
  * Configure a PodMonitoring resource for Managed Service for Prometheus to collect the exported metrics.
  * View the **Application** dashboard for your GKE Deployment.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus.

## Set up

To collect metrics from your HTTP server that can be displayed on the **Application** dashboard, you must export the following metrics as described: 

  * `http_requests_total` of type `counter`, with the labels `code` and `method`.
  * `http_request_duration_seconds_bucket` of type `histogram`, with the label `method`.



For an example that collects these metrics by using the Prometheus Go client, see [prometheus-example-app](https://github.com/brancz/prometheus-example-app).

To verify that your HTTP server is emitting metrics on the expected endpoints, do the following: 

  1. Set up port forwarding by using the following command: 
         
         kubectl -n NAMESPACE_NAME port-forward deploy/HTTP_SERVER_DEPLOYMENT_NAME PROMETHEUS_PORT_NUMBER
           

  2. Access `localhost:PROMETHEUS_PORT_NUMBER` by using the browser or the `curl` utility in another terminal session.



## Define a PodMonitoring resource

For target discovery, the Managed Service for Prometheus Operator requires a PodMonitoring resource that corresponds to the HTTP server in the same namespace.

You can use the following PodMonitoring configuration:
    
    
    apiVersion: monitoring.googleapis.com/v1
    kind: PodMonitoring
    metadata:
      name: my-prometheus-http-app
      labels:
        app.kubernetes.io/name: my-prometheus-http-app
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      endpoints:
      - port: web
        scheme: http
        interval: 30s
        path: /metrics
      selector:
        matchLabels:
          app.kubernetes.io/name: prometheus-example-app
    

Ensure that the values of the `port` and `MatchLabels` fields match those of the HTTP application that you want to monitor.

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## View application metrics

To view request, error-rate, and latency metrics from your HTTP application, do the following: 

  1. In the Google Cloud console, go to the **Workloads** page: 

[Go to **Workloads**](https://console.cloud.google.com/kubernetes/workload/overview)

If you use the search bar to find this page, then select the result whose subheading is **Kubernetes Engine**.

  2. Click a Deployment in the list of workloads. The **Type** column in the list indicates the type of the workload.
  3. On the **Deployment details** page, click the **Observability** tab.
  4. Select **Application** in the dashboard selector.



For more information, see [Use application performance metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/app-performance-metrics). 

## Troubleshooting

For information about troubleshooting metric ingestion problems in Managed Service for Prometheus, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
