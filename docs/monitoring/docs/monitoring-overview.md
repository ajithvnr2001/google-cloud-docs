---
url: https://docs.cloud.google.com/monitoring/docs/monitoring-overview/
title: Cloud Monitoring overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:52.284486+00:00
---

# Cloud Monitoring overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/monitoring-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Cloud Monitoring overview Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Monitoring collects, stores, and analyzes metric data to help you understand the behavior, health, and performance of your applications and Google Cloud services. Cloud Monitoring automatically collects performance metrics for most Google Cloud services. You can also collect [Prometheus](https://prometheus.io) metrics by using [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus), or install the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent) on your Compute Engine virtual machines (VMs) to collect metrics and logs from your applications and third-party software.

With Cloud Monitoring alerting, testing, and visualization services, you can track service load and performance, verify website responsiveness, and monitor the health of your [App Hub applications](https://docs.cloud.google.com/app-hub/docs/overview). You can access and manage most Cloud Monitoring services by using the Google Cloud console, the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/list), the Google Cloud CLI, or Terraform.

## Cloud Monitoring services

Cloud Monitoring provides different services that you can use to understand the health and performance of your applications and of the other Google Cloud services that you use.

### Alerts and notifications in Cloud Monitoring

To be notified when the value of a performance metric meets criteria that you define, create an [alerting policy](https://docs.cloud.google.com/monitoring/alerts). The alerting policy includes the list of people or groups who are to receive notifications. Monitoring supports [common notification channels](https://docs.cloud.google.com/monitoring/support/notification-options), including email, Cloud Mobile App, and services such as PagerDuty or Slack. For example, you might create an alerting policy so that you are notified when the CPU utilization of a VM exceeds 80%.

Each notification includes relevant information about a failure, and it includes a link to an alert. An _alert_ is a persistent record that stores information that you can use to troubleshoot the failure. Typically, a record lists the status of the alert, links to logs, a chart of the recorded metric data, labels, and duration.

The alerting service is integrated with many Google Cloud services. When these integrations exist, you might see a panel that lists recommended alerts, or you might see a button on a chart that lets you create an alerting policy. In both cases, the alerting policies are preconfigured; you only specify the list of people or groups to be notified.

You can create and manage alerting policies by using the Google Cloud console, the Cloud Monitoring API, the Google Cloud CLI, or Terraform.

### Proactive monitoring and validation

To test the availability, consistency, and performance of your services, applications, web pages, and APIs, create [synthetic monitors](https://docs.cloud.google.com/monitoring/uptime-checks/introduction). For example, you can probe HTTP, HTTPS, and TCP endpoints for responsiveness with [uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks), and then get notified when an endpoint fails to respond. You can also create a [broken-link checker](https://docs.cloud.google.com/monitoring/synthetic-monitors/broken-links) to crawl a web page and then notify you when broken links are detected.

You can create and manage synthetic monitors by using the Google Cloud console, the Cloud Monitoring API, the Google Cloud CLI, or Terraform.

### Data visualization

As you instantiate Google Cloud resources or register applications with [App Hub](https://docs.cloud.google.com/app-hub/docs/overview), the dashboard service automatically creates [Google Cloud-managed dashboards](https://docs.cloud.google.com/monitoring/charts/predefined-dashboards). These dashboards show curated information that helps you understand the health of your resources and applications. For example, for an App Hub application, dashboards are created for the application and for each of its services and workloads. These dashboards show information like an application's log or metric data, and the number of open alerts.

The dashboards created by Google Cloud might provide you enough information to complete an investigation. However, they might not provide the exact data you need to see trends, identify outliers, or view other details about your data. To complete these tasks, you can use the [dashboard](https://docs.cloud.google.com/monitoring/dashboards) and [charting](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) services:

  * To control what data you view and the display format for that data, [create a custom dashboard](https://docs.cloud.google.com/monitoring/charts/dashboards). For example, you might [import a Grafana dashboard](https://docs.cloud.google.com/monitoring/dashboards/import-grafana-dashboards) or [install a dashboard from a template](https://docs.cloud.google.com/monitoring/dashboards/dashboard-templates).

Your custom dashboards can display the following:

    * Charts and tables that show metric data
    * Log data and error groups
    * Charts for alerting policies
    * Information about alerts
    * Text
    * [Events](https://docs.cloud.google.com/monitoring/dashboards/event-types), such as a reboot or a crash, that affect the operation of a system.

You can create and manage dashboards by using the [Google Cloud console](https://docs.cloud.google.com/monitoring/charts/dashboards) or the [API](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard).

  * The chart service, [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer), lets you quickly visualize and explore time-series data. The chart settings let you compare current data to previous data, display outliers and percentiles, and display multiple metrics. You can also [save charts](https://docs.cloud.google.com/monitoring/charts/metrics-explorer#save_a_chart) to a custom dashboard.




### Data collection and storage

Cloud Monitoring collects and stores the following types of metric data:

  * [System metrics generated by Google Cloud services](https://docs.cloud.google.com/monitoring/api/metrics_gcp). These metrics provide information about how a service is operating.


  * [System and application metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent) that the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent) collects about system resources and applications running on Compute Engine instances. You can configure the Ops Agent to collect metrics from [third-party plugins](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party) such as Apache or Nginx web servers, or MongoDB or PostgreSQL databases.


  * [User-defined metrics](https://docs.cloud.google.com/monitoring/custom-metrics) that are created by using the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/docs/apis) or by using a library such as [OpenTelemetry](https://opentelemetry.io).

  * [External metrics](https://docs.cloud.google.com/monitoring/api/metrics_other) that are defined by some open source libraries or third-party providers.

  * Prometheus metrics that are collected by [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus), or by using the Ops Agent and the [Prometheus receiver](https://docs.cloud.google.com/monitoring/agent/ops-agent/prometheus) or the [OTLP receiver](https://docs.cloud.google.com/monitoring/agent/ops-agent/otlp).



  * [Log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) that record numeric information about the logs written to [Cloud Logging](https://docs.cloud.google.com/logging/docs). Google-defined log-based metrics include counts of the errors that your service detects and the total number of log entries received by your Google Cloud project. You can also define log-based metrics.



## Query languages for Cloud Monitoring

When you create an alerting policy or a chart, you must provide a query that describes the data that you want to monitor or chart:

  * Google Cloud console: You can build your query by making selections from menus, or you can write a query. Query editors are available for the [Prometheus Query Language (PromQL)](https://docs.cloud.google.com/monitoring/promql). The query editor provides syntax checks and suggestions. You can also write a [Monitoring filter](https://docs.cloud.google.com/monitoring/api/v3/filters) expression.

  * Cloud Monitoring API: The API supports Prometheus Query Language (PromQL) and Monitoring filter expressions.




## Monitor metrics for multiple Google Cloud projects

To view and monitor the time-series data for multiple Google Cloud projects and AWS accounts through a single interface, configure a multi-project [metrics scope](https://docs.cloud.google.com/monitoring/settings).

By default, Cloud Monitoring pages in the Google Cloud console provide access only to the time series stored in the _scoping project_. The scoping project is the project that you selected with the Google Cloud console project picker. The scoping project stores the [alerts](https://docs.cloud.google.com/monitoring/alerts), [synthetic monitors](https://docs.cloud.google.com/monitoring/uptime-checks/introduction), and [dashboards](https://docs.cloud.google.com/monitoring/dashboards) that you configure.

The scoping project also hosts a metrics scope. The _metrics scope_ defines the projects and accounts whose metrics are visible to the scoping project. You can configure the metrics scope to include time-series data from other Google Cloud projects and from AWS accounts. For information about how to modify a metrics scope, see [Configure a metrics scope for multiple projects](https://docs.cloud.google.com/monitoring/settings/multiple-projects).

## Cloud Monitoring data model

This section introduces the Cloud Monitoring data model:

  * A _metric type_ describes something that is measured. Examples of metric types include a VM's CPU utilization and the percentage of a disk that is used.

  * A _time series_ is a data structure that contains time-stamped measurements of a metric and information about the source and meaning of those measurements.




Here are some details about what a time series contains:

  * The `points` array contains the time-stamped measurements.

The following is an example of a `points` array with two values:
        
        "points": [
            {
              "interval": {
                "startTime": "2020-07-27T20:20:21.597143Z",
                "endTime": "2020-07-27T20:20:21.597143Z"
              },
              "value": {
                "doubleValue": 0.473005
              }
            },
            {
              "interval": {
                "startTime": "2020-07-27T20:19:21.597239Z",
                "endTime": "2020-07-27T20:19:21.597239Z"
              },
              "value": {
                "doubleValue": 0.473025
              }
            },
          ],
        

To understand the meaning of a value, you need to refer to the other data included in the time series and to the definitions of that data.

  * The `resource` field describes the hardware or software component that is being monitored. In Cloud Monitoring, the hardware or software component is referred to as the _monitored resource_. Examples of monitored resources include Compute Engine instances and App Engine applications. For a list of monitored resources, see the [Monitored resource list](https://docs.cloud.google.com/monitoring/api/resources).

The following is an example of a `resource` field:
        
        "resource": {
            "type": "gce_instance",
            "labels": {
              "instance_id": "2708613220420473591",
              "zone": "us-east1-b",
              "project_id": "sampleproject"
            }
          }
        

    * The `type` field lists the monitored resource as a [`gce_instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance), which indicates that these measurements are taken on a Compute Engine VM instance.

    * The `labels` field contains key-value pairs that provide additional information about the monitored resource. For a `gce_instance` type, the labels identify the VM instance that is being monitored.

  * The `metric` field describes what is being measured.

The following is an example of a `metric` field:
        
        "metric": {
            "labels": {
              "instance_name": "test"
            },
            "type": "compute.googleapis.com/instance/cpu/utilization"
          },
        

    * For Google Cloud services, the `type` field specifies the service and what is being monitored. In this example, the Compute Engine service is measuring the CPU utilization. When the `type` field begins with `custom` or `external`, the metric is either a custom metric or one defined by a third party.
    * The `labels` field contains key-value pairs that provide additional information about the measurement. These labels are defined as part of the [`MetricDescriptor`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor), which is a data structure that defines the attributes of the measured data. The `MetricDescriptor` for the metric [`compute.googleapis.com/instance/cpu/utilization`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#compute/instance/cpu/utilization) includes the label `instance_name`.
  * The [`metricKind`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind) field describes the relationship between adjacent measurements within a time series:

    * `GAUGE` metrics store the value of the thing being measured at a given moment in time—for example, an hourly temperature record.

    * `CUMULATIVE` metrics store the accumulated value of the thing being measured at a given moment in time—for example, an odometer in a vehicle.

    * `DELTA` metrics store the change in the value of the thing being measured over a specified period—for example, a stock summary that shows the stock's gains or losses.

  * The [`valueType`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#ValueType) field describes the data type for the measurement: `INT64`, `DOUBLE`, `BOOL`, `STRING`, or [`DISTRIBUTION`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Distribution).


Cloud Monitoring writes one time series for each combination of resource and metric label values. You can use these labels to group and to filter time series. For example, when a Google Cloud project contains multiple Compute Engine VM instances, the CPU utilization for each VM instance is a unique time series. Here are a few of the ways that you can display this data: 
  * You can show the CPU utilization of every VM instance.
  * You can show the CPU utilization for a specific VM instance by filtering the time series for a single value of the `instance_id` label.
  * You can group the VM instances by the `machine_type` label, and then display the average CPU utilization. The following screenshot illustrates a chart with this configuration:

![Average CPU utilization grouped by machine type.](https://docs.cloud.google.com/static/monitoring/images/percent-used-by-state.png)




## Pricing

To learn about pricing for Cloud Monitoring, see the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page.

## What's next

  * To explore Cloud Monitoring, try the [Quickstart for monitoring a Compute Engine instance](https://docs.cloud.google.com/monitoring/monitor-compute-engine-virtual-machine).


  * For information about how to configure your Google Cloud project to view metrics for multiple Google Cloud projects and AWS accounts, see [Metrics scopes overview](https://docs.cloud.google.com/monitoring/settings).


  * For information about the Cloud Monitoring data model, see [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics).

  * For information about the Cloud Monitoring API, see [APIs and reference](https://docs.cloud.google.com/monitoring/docs/apis).

  * For lists of metrics and monitored resources, see [Metrics list](https://docs.cloud.google.com/monitoring/api/metrics) and [Monitored resource list](https://docs.cloud.google.com/monitoring/api/resources).

  * [Quotas and limits](https://docs.cloud.google.com/monitoring/quotas).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
