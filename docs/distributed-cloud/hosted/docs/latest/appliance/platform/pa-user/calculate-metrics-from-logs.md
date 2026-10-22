---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/calculate-metrics-from-logs/
title: Create metrics from logs \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:54.446158+00:00
---

# Create metrics from logs  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/calculate-metrics-from-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Create metrics from logs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to generate new metrics from existing logs by deploying a `LoggingRule` custom resource in Google Distributed Cloud (GDC) air-gapped appliance.

Recording rules allow you to precompute frequently used or computationally expensive expressions, improving performance for dashboards and alerts. Defined within `LoggingRule` custom resources, these rules generate new time series metrics from existing logs, enhancing data observability.

By storing precomputed results, recording rules eliminate redundant calculations each time an expression is needed. This method significantly speeds up query times, particularly for complex dashboards and alerts that require repeated evaluations of the same expression. Essentially, `LoggingRule` resources let you derive new metrics from existing logging data by specifying the necessary calculations within their recording rules.

## Before you begin

To get the permissions that you need to manage `LoggingRule` custom resources, ask your Organization IAM Admin or Project IAM Admin to grant you one of the associated `LoggingRule` roles.

Depending on the level of access and permissions you need, you might obtain creator, editor, or viewer roles for this resource in an organization or a project. For more information, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/obs-iam-permissions).

## Create recording rules

To create a recording rule, define a name for the recorded log and a valid expression that produces a numeric value. This expression, when evaluated, generates the new metric. Deploy the `LoggingRule` custom resource in your project namespace on the Management API server to activate the recording rule.

For more information about recording rules, see <https://grafana.com/docs/loki/latest/rules/>.

**Important:** Before creating recording rules, ensure you have a deployed project with active workloads and configured logging targets. In this way, the rules have data to operate on. For more information, see [Collect logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/collect-logs).

Follow these steps to create recording rules in your project namespace:

  1. Determine the GDC project from which you want to create recording rules.
  2. Create a YAML file defining the `LoggingRule` custom resource.

The complete `LoggingRule` specification shows an example for log-based recording rules. For more information, see the [API reference documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/logging/v1/logging-v1#loggingrule).

  3. Replace the following values in the YAML file according to your needs:

Field name | Description  
---|---  
`namespace` | The project namespace.  
`name` | The name for the rule configuration.  
`source` | The log source for the recording rule. Valid options are `operational` and `audit`.  
`interval` | The duration of the rule evaluation interval in seconds.  
`limit` | _Optional._ The maximum number of alerts. Set to `0` for unlimited alerts.  
`recordRules` | The definitions for calculating new metrics.  
`recordRules.record` | The record name for the new metric. The value must be a valid metric name that defines the time series where the results are stored.  
`recordRules.expr` | A [LogQL](https://grafana.com/docs/loki/latest/logql/) expression for the log rule, which must evaluate to a numeric value.  
`recordRules.labels` | _Optional._ The key-value pairs of labels to add to or overwrite the new metric.  
  4. Save the YAML file.

  5. Apply the `LoggingRule` configuration to the Management API server within the same namespace as your recording rules:
         
         kubectl --kubeconfig KUBECONFIG_PATH apply -f LOGGING_RULE_NAME.yaml
         

Replace the following:

     * `KUBECONFIG_PATH`: the path to the kubeconfig file for the Management API server.
     * `LOGGING_RULE_NAME`: the name of the `LoggingRule` definition file.



## Complete `LoggingRule` specification

A `LoggingRule` custom resource contains recording rules that describe the conditions to create new metrics based on existing logs for observability.

The following YAML file shows a template for the `LoggingRule` custom resource. For more information, see the [API reference documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/logging/v1/logging-v1#loggingrule).
    
    
    # Configures either an alert or a target record for precomputation.
    apiVersion: logging.gdc.goog/v1
    kind: LoggingRule
    metadata:
      # Choose a namespace that matches the project namespace.
      # The alert or record is produced in the same namespace.
      namespace: PROJECT_NAMESPACE
      name: LOGGING_RULE_NAME
    spec:
      # Choose the log source to base alerts on (operational or audit logs).
      # Optional.
      # Valid options: 'operational' and 'audit'
      # Default value: 'operational'
      source: operational
    
      # Rule evaluation interval.
      interval: 60s
    
      # Configure the limit for the number of alerts.
      # A value of '0' means no limit.
      # Optional.
      # Default value: '0'
      limit: 0
    
      # Configure recording rules to generate new metrics based on existing logs.
      # Recording rules precompute expressions that are frequently needed or computationally expensive.
      # Results are saved as a new set of time series.
      recordRules:
        # Define the time series where you want to write the recording rule.
        # The value must be a valid metric name.
      - record: MyMetricsName
    
        # Define the LogQL expression to evaluate for this rule.
        expr: rate({service_name="bob-service"} [1m])
    
        # Define labels to add or overwrite.
        # Map of key-value pairs.
        # Optional.
        labels:
          verb: read
    

Replace the following:

  * `PROJECT_NAMESPACE`: your project namespace.
  * `LOGGING_RULE_NAME`: the name of the `LoggingRule` definition file.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
