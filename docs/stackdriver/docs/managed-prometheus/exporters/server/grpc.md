---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/server/grpc/
title: gRPC server \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:52.929667+00:00
---

# gRPC server  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/server/grpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  gRPC server Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from the gRPC requests served by your application. This document describes how to do the following: 

  * Set up the gRPC Prometheus middleware for Go and Java.
  * Configure a PodMonitoring resource for Managed Service for Prometheus to collect the exported metrics.
  * View the **Application** dashboard for your GKE Deployment.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus.

For more information about gRPC, see [grpc.io](https://grpc.io).

## Set up

To collect metrics from your gRPC server, you must configure the appropriate gRPC middleware. 

  * If you are using Go, then see [go-grpc-middleware](https://github.com/grpc-ecosystem/go-grpc-middleware).
  * If you are using Java, then see [java-grpc-prometheus](https://github.com/grpc-ecosystem/java-grpc-prometheus).



To verify that your gRPC server is emitting metrics on the expected endpoints, do the following: 

  1. Set up port forwarding by using the following command: 
         
         kubectl -n NAMESPACE_NAME port-forward deploy/GRPC_SERVER_DEPLOYMENT_NAME PROMETHEUS_PORT_NUMBER
           

  2. Access `localhost:PROMETHEUS_PORT_NUMBER` by using the browser or the `curl` utility in another terminal session.



## Define a PodMonitoring resource

For target discovery, the Managed Service for Prometheus Operator requires a PodMonitoring resource that corresponds to the gRPC server in the same namespace.

You can use the following PodMonitoring configuration:
    
    
    apiVersion: monitoring.googleapis.com/v1
    kind: PodMonitoring
    metadata:
      name: my-prometheus-grpc-app
      labels:
        app.kubernetes.io/name: my-prometheus-grpc-app
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      endpoints:
      - port: prometheus
        scheme: http
        interval: 30s
        path: /metrics
      selector:
        matchLabels:
          app.kubernetes.io/name: my-prometheus-grpc-app
    

Ensure that the values of the `port` and `MatchLabels` fields match those of the gRPC application that you want to monitor.

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## View application metrics

To view request, error-rate, and latency metrics from your gRPC application, do the following: 

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

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
