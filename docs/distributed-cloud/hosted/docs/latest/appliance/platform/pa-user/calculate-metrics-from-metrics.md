---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/calculate-metrics-from-metrics/
title: Create new metrics from existing metrics \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:46.460215+00:00
---

# Create new metrics from existing metrics  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/calculate-metrics-from-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Create new metrics from existing metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to generate new metrics from existing metrics by deploying a `MonitoringRule` custom resource in Google Distributed Cloud (GDC) air-gapped appliance.

Recording rules allow you to precompute frequently used or computationally expensive expressions, improving performance for dashboards and alerts. Defined within `MonitoringRule` custom resources, these rules generate new time series metrics from existing metrics, enhancing data observability.

By storing precomputed results, recording rules eliminate redundant calculations each time an expression is needed. This method significantly speeds up query times, particularly for complex dashboards and alerts that require repeated evaluations of the same expression. Essentially, `MonitoringRule` resources let you derive new metrics from existing ones by specifying the necessary calculations within their recording rules.

## Before you begin

To manage `MonitoringRule` custom resources, request the necessary permissions from your administrator.

### Required IAM roles

Contact your Project IAM Admin to request the following roles:

  * **MonitoringRule Creator** (`monitoringrule-creator`): create `MonitoringRule` custom resources in the project namespace.
  * **MonitoringRule Editor** (`monitoringrule-editor`): edit or modify `MonitoringRule` custom resources in the project namespace.
  * **MonitoringRule Viewer** (`monitoringrule-viewer`): view `MonitoringRule` custom resources in the project namespace.



## Create recording rules

To create a recording rule, define a name for the recorded metric and a valid expression that produces a numeric value. This expression, when evaluated, generates the new metric. Deploy the custom resource in your project namespace on the Management API server to create the recording rules.

For more information about recording rules, see <https://grafana.com/docs/loki/latest/rules/>.

**Important:** Before creating recording rules, ensure you have a deployed project with active workloads and configured metric scraping. In this way, the rules have data to operate on. For more information, see [Collect metrics](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/collect-metrics).

Follow these steps to create recording rules in your project namespace:

  1. Determine the GDC project from which you want to create recording rules.
  2. Create a YAML file defining the `MonitoringRule` custom resource.

The complete `MonitoringRule` specification shows an example for metric-based recording rules. For more information, see the [API reference documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/monitoring/v1/monitoring-v1#monitoringrule).

  3. Replace the following values in the YAML file according to your needs:

Field name | Description  
---|---  
`namespace` | The project namespace.  
`name` | The name for the rule configuration.  
`interval` | The duration of the rule evaluation interval in seconds.  
`limit` | _Optional._ The maximum number of alerts. Set to `0` for unlimited alerts.  
`recordRules` | The definitions for calculating new metrics.  
`recordRules.record` | The record name for the new metric. The value must be a valid metric name that defines the time series where the results are stored.  
`recordRules.expr` | A [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/) expression for the metric rule, which must evaluate to a numeric value.  
`recordRules.labels` | _Optional._ The key-value pairs of labels to add to or overwrite the new metric.  
  4. Save the YAML file.

  5. Apply the `MonitoringRule` configuration to the Management API server within the same namespace as your recording rules:
         
         kubectl --kubeconfig KUBECONFIG_PATH apply -f MONITORING_RULE_NAME.yaml
         

Replace the following:

     * `KUBECONFIG_PATH`: the path to the kubeconfig file for the Management API server.
     * `MONITORING_RULE_NAME`: the name of the `MonitoringRule` definition file.



## Complete `MonitoringRule` specification

A `MonitoringRule` custom resource contains recording rules that describe the conditions to create new metrics based on existing metrics for observability.

The following YAML file shows a template for the `MonitoringRule` custom resource. For more information, see the [API reference documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/monitoring/v1/monitoring-v1#monitoringrule).
    
    
    # Configures either an alert or a target record for precomputation.
    apiVersion: monitoring.gdc.goog/v1
    kind: MonitoringRule
    metadata:
      # Choose a namespace that matches the project namespace.
      # The alert or record is produced in the same namespace.
      namespace: PROJECT_NAMESPACE
      name: MONITORING_RULE_NAME
    spec:
      # Rule evaluation interval.
      interval: 60s
    
      # Configure the limit for the number of alerts.
      # A value of '0' means no limit.
      # Optional.
      # Default value: '0'
      limit: 0
    
      # Configure recording rules to generate new metrics based on existing metrics.
      # Recording rules precompute expressions that are frequently needed or computationally expensive.
      # Results are saved as a new set of time series.
      recordRules:
        # Define the time series where you want to write the recording rule.
        # The value must be a valid metric name.
      - record: MyMetricsName
    
        # Define the PromQL expression to evaluate for this rule.
        expr: rate({service_name="bob-service"} [1m])
    
        # Define labels to add or overwrite.
        # Map of key-value pairs.
        # Optional.
        labels:
          verb: read
    

Replace the following:

  * `PROJECT_NAMESPACE`: your project namespace.
  * `MONITORING_RULE_NAME`: the name of the `MonitoringRule` definition file.



## The `LoggingRule` record rules

A `LoggingRule` CR contains record rules that describe the conditions to calculate new metrics based on pre-existing logs.

The following YAML file shows a template for the `recordRules` field of the `LoggingRule` CR.
    
    
    # Configures either an alert or a target record for precomputation
    apiVersion: logging.gdc.goog/v1alpha1
    kind: LoggingRule
    metadata:
      # Choose namespace that matches the project's namespace
      # Note: The alert or record will be produced in the same namespace
      namespace: g-fleetns-a
      name: alerting-config
    spec:
      # Choose which log source to base alerts on (Operational/Audit/Security Logs)
      # Optional, Default: Operational
      source: <string>
    
      # Rule evaluation interval
      interval: <duration>
    
      # Configure limit for number of alerts (0: no limit)
      # Optional, Default: 0 (no limit)
      limit: <int>
    
      # Configure record rules to generate new metrics based on pre-existing logs.
      # Record rules generate metrics based on logs.
      # Use record rules for complex alerts, which query the same expression repeatedly every time they are evaluated.
      recordRules:
        # Define which timeseries to write to (must be a valid metric name)
      - record: <string>
    
        # Define LogQL expression to evaluate for this rule
        # https://grafana.com/docs/loki/latest/rules/
        expr: <string>
    
        # Define labels to add or overwrite
        # Optional, Map of {key, value} pairs
        labels:
          <labelname>: <labelvalue>
    ...
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
