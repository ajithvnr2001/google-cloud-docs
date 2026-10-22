---
url: https://docs.cloud.google.com/config-connector/docs/how-to/monitoring-prometheus/
title: Monitoring Config Connector with Prometheus \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:37.266622+00:00
---

# Monitoring Config Connector with Prometheus  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/how-to/monitoring-prometheus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitoring Config Connector with Prometheus

You can use [Prometheus](https://prometheus.io/) to collect and show metrics from Config Connector.

## Before you begin

To complete the steps in this page, you need to install Prometheus on your cluster. You can do this by:

  * Using the [Prometheus Operator provided by CoreOS](https://coreos.com/operators/prometheus/docs/latest/), or

  * Following the [Prometheus documentation](https://prometheus.io/docs/prometheus/latest/getting_started/) to configure your cluster for scraping.




## Scraping metrics

Prometheus gathers metrics by _scraping_ an HTTP endpoint. This section describes the Config Connector scrape endpoints and configuring Prometheus.

### Config Connector scrape endpoints

For Config Connector, service endpoints are on port 8888 at `cnrm-controller-manager-service` and `cnrm-resource-stats-recorder-service`. These services have the `prometheus.io/scrape: "true"` and `prometheus.io/port: "8888"` annotations. The services also include the labels `cnrm.cloud.google.com/monitored: "true"` and `cnrm.cloud.google.com/system: "true"`. You configure Prometheus to scrape Config Connector components from these annotations and labels.

### Configuring Prometheus

Before you can scrape metrics, you might need to configure Prometheus for [Kubernetes Service Discovery (SD)](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#kubernetes_sd_config) to discover scrape targets from the Kubernetes REST API.

How you configure Prometheus to scrape metrics from Config Connector depends on how you installed Prometheus. Check the documentation for your Prometheus installation for how to update configuration.

For example, If you are using the Prometheus Operator and configure it with [ServiceMonitor](https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/user-guides/basic-auth.md), you can apply the following configuration to scrape metrics from Config Connector.
    
    
      spec:
        endpoints:
        - interval: 10s
          port: metrics
        namespaceSelector:
          matchNames:
          - cnrm-system
        selector:
          matchLabels:
            cnrm.cloud.google.com/monitored: "true"
            cnrm.cloud.google.com/system: "true"
    

## Example queries

Prometheus uses a query language called [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/). This section contains example PromQL queries for Config Connector's metrics. You can configure Prometheus to generate [alerts](https://prometheus.io/docs/alerting/overview/) from any valid PromQL query.

### Query reconcile requests by resource kind and status

You can see the count of failed reconcile requests by resource kind and status.

For example, to check the total count of errors for `PubSubTopic` resources, use the following query.
    
    
    configconnector_reconcile_requests_total{group_version_kind="PubSubTopic.pubsub.cnrm.cloud.google.com", status="ERROR"}
    

### Check the aggregate status of resources by kind and Namespace

You can see the count of resources that are in a Namespace.

For example, to check the total count of `PubSubTopic` resources in the `default` Namespace, use the following query.
    
    
    configconnector_applied_resources_total{group_version_kind="PubSubTopic.pubsub.cnrm.cloud.google.com", Namespace="default"}
    

### Query the utilization of reconcile workers per resource kind
    
    
    (configconnector_reconcile_occupied_workers_total / configconnector_reconcile_workers_total)
    

## Available metrics

Config Connector collects the following metrics and makes them available.

**Note:** Additional metrics might be available. You can see the complete list in the Prometheus user interface by searching for the prefix `configconnector_`.Name | Type | Labels | Description  
---|---|---|---  
configconnector_reconcile_requests_total | Counter | Namespace  
group_version_kind  
status | The total number of reconcile requests.  
configconnector_reconcile_request_duration_seconds | Histogram | Namespace  
group_version_kind  
status | Distributions of the time to complete reconcile requests.  
configconnector_applied_resources_total | Gauge | Namespace  
group_version_kind  
status | The total number of resources under management.  
configconnector_build_info | Gauge | version | Current version of Config Connector.  
configconnector_reconcile_workers_total | Gauge | group_version_kind | The total number of reconcile workers aggregated by resource kind.  
configconnector_reconcile_occupied_workers_total | Gauge | group_version_kind | The total number of occupied reconcile workers aggregated by resource kind.  
  
## Enabling resource name labels

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

By default, metrics are aggregated on resource kind (for example, PubSubTopic). You can enable metrics to be aggregated by individual resources.

**Note:** Enabling this option can dramatically increase the amount of data stored in Prometheus. Be sure you have enough storage space, or configure [retention](https://prometheus.io/docs/prometheus/latest/storage/#compaction).

To enable aggregation by resource name, perform the following steps.

  1. Edit the `cnrm-controller-manager` StatefulSet object
         
         kubectl edit statefulset cnrm-controller-manager -n cnrm-system

If you are using [Namespaced mode](https://docs.cloud.google.com/config-connector/docs/concepts/installation-types), replace `NAMESPACE_NAME` with your Namespace.
         
         kubectl edit statefulset cnrm-controller-manager -n NAMESPACE_NAME

  2. Find the array `spec.args` and add `--resource-name-label=true`.
         
         apiVersion: apps/v1
         kind: StatefulSet
           name: cnrm-controller-manager
         spec:
           template:
             spec:
               containers:
               - name: manager
           args:
                 - --resource-name-label=true
         




## What's next

For more information on writing queries, see the Prometheus [Query language documentation](https://prometheus.io/docs/prometheus/latest/querying/basics/) and [Examples](https://prometheus.io/docs/prometheus/latest/querying/examples/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
