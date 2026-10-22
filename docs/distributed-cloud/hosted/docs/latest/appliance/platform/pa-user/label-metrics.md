---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/label-metrics/
title: Label metrics \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:04.469312+00:00
---

# Label metrics  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/label-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Label metrics Stay organized with collections  Save and categorize content based on your preferences. 

Labels let you differentiate the characteristics of a metric. In addition to [collecting metrics](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/collect-metrics), the `MonitoringTarget` custom resource lets you label metrics for optional observability features:

  * Send metrics to another project.
  * Add new labels to metrics.
  * Rename a metric.

**Important:** Each unique combination of key-value label pairs creates a new time series, which can significantly increase data storage. Avoid using labels for high-cardinality dimensions (many possible values), like user IDs or email addresses.

For more information on metrics relabeling, see <https://grafana.com/blog/2022/03/21/how-relabeling-in-prometheus-works/>.

## Before you begin

To manage `MonitoringTarget` custom resources, request the necessary permissions from your administrator.

### Required IAM roles

Contact your Project IAM Admin to request the following roles:

  * **MonitoringTarget Creator** (`monitoringtarget-creator`): create `MonitoringTarget` custom resources in the project namespace.
  * **MonitoringTarget Editor** (`monitoringtarget-editor`): edit or modify `MonitoringTarget` custom resources in the project namespace.
  * **MonitoringTarget Viewer** (`monitoringtarget-viewer`): view `MonitoringTarget` custom resources in the project namespace.



## Send metrics to another project

Container authors can code specific metrics to be sent to a different project, even to projects they don't own. To send a metric to a specific project, add the `_gdch_project` label to the metric in your code, setting its value to the destination project name.

Alternatively, use the `MonitoringTarget` custom resource to send _all_ collected metric data to another project. Set the `_gdch_project` label as a target label in the `metricsRelabelings` field, with the new project name as the replacement value.

The following code sample shows how to set the `_gdch_project` target label in the `MonitoringTarget` custom resource to send metrics to the project named `another-project-name`:
    
    
    apiVersion: monitoring.gdc.goog/v1
    kind: MonitoringTarget
    metadata:
      # Choose the same namespace as the workload pods.
      namespace: PROJECT_NAMESPACE
      name: MONITORING_TARGET_NAME
    spec:
      [...]
      podMetricsEndpoints:
        [...]
        metricsRelabelings:
          - action: replace
            targetLabel: _gdch_project
            replacement: another-project-name
          [...]
    

Replace the following:

  * `PROJECT_NAMESPACE`: your project namespace.
  * `MONITORING_TARGET_NAME`: the name of the `MonitoringTarget` definition file.



## Add new labels to metrics

Labels help with observability and monitoring by identifying metric characteristics. You can add labels that the scraped containers don't initially expose. In the `MonitoringTarget` custom resource, set the new label as a target label and provide a replacement value. This key-value pair is added to all metrics the resource collects.

The following code sample shows how to set the `my_new_label` target label and configure its value to `my_label_value` in the `MonitoringTarget` custom resource:
    
    
    apiVersion: monitoring.gdc.goog/v1
    kind: MonitoringTarget
    metadata:
      # Choose the same namespace as the workload pods.
      namespace: PROJECT_NAMESPACE
      name: MONITORING_TARGET_NAME
    spec:
      [...]
      podMetricsEndpoints:
        [...]
        metricsRelabelings:
          - action: replace
            targetLabel: my_new_label
            replacement: my_label_value
          [...]
    

Replace the following:

  * `PROJECT_NAMESPACE`: your project namespace.
  * `MONITORING_TARGET_NAME`: the name of the `MonitoringTarget` definition file.



## Rename a metric

You can rename a container's metric using the `MonitoringTarget` resource. Set the original metric name and its replacement in the `metricsRelabelings` field. The original name is treated as a regular expression (regex) and is replaced by the new name.

The following code sample shows how to replace the `cpu_usage` metric name (regex) with `cpu_usage_new_name` in the `MonitoringTarget` custom resource:
    
    
    apiVersion: monitoring.gdc.goog/v1
    kind: MonitoringTarget
    metadata:
      # Choose the same namespace as the workload pods.
      namespace: PROJECT_NAMESPACE
      name: MONITORING_TARGET_NAME
    spec:
      [...]
      podMetricsEndpoints:
        [...]
        metricsRelabelings:
          - action: replace
            regex: cpu_usage
            replacement: cpu_usage_new_name
            sourceLabels: [__name__]
            targetLabel: __name__
          [...]
    

Replace the following:

  * `PROJECT_NAMESPACE`: your project namespace.
  * `MONITORING_TARGET_NAME`: the name of the `MonitoringTarget` definition file.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
