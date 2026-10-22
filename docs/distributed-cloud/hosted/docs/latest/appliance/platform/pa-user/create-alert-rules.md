---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-alert-rules/
title: Create alert rules \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:02.984831+00:00
---

# Create alert rules  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-alert-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Create alert rules Stay organized with collections  Save and categorize content based on your preferences. 

This page outlines the process for creating alert rules based on logs and metrics from Google Distributed Cloud (GDC) air-gapped appliance environments to facilitate proactive monitoring and faster incident response.

GDC lets you define alert rules based on your project's metrics or logs. These rules automatically trigger alerts when specific conditions are met. The following are the alert rule types you can define:

  * **Metric-based rules** : Trigger alerts based on numerical data collected from your applications or infrastructure. For example, you could create a rule to trigger an alert if CPU usage exceeds 80%. Create metric-based rules using the GDC console or a `MonitoringRule` custom resource definition.
  * **Log-based rules** : Trigger alerts based on the analysis of log data. These alerts let you identify and respond to specific events or patterns within your logs, such as error messages or unusual activity. Create log-based rules using the GDC console or a `LoggingRule` custom resource definition.

**Important:** Before creating alert rules, ensure you have a deployed project with active workloads and configured logging and monitoring targets. In this way, the rules have data to operate on. For more information, see [Collect metrics](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/collect-metrics) or [Collect logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/collect-logs).

Both metric-based and log-based rules rely on a query language expression to define the condition that triggers an alert. This expression filters and analyzes the incoming data, evaluating whether the defined criteria are met.

The first time a condition is met, the alert transitions to the _pending_ state. If the conditions are true over the following duration period you define, the alert moves to the _open_ state. At that moment, the system sends the alert.

To provide further context and facilitate efficient alert management, you can add labels and annotations to your alert rules:

  * **Labels** : Key-value pairs that categorize and identify alerts. Use labels for information like the following:

    * Severity level (error, critical, warning)
    * Alert code
    * Resource name
  * **Annotations** : Provide additional non-identifying information to enrich the alert. Annotations can include the following information:

    * Detailed error messages
    * Relevant expressions
    * Links to runbooks or troubleshooting guides



## Before you begin

To manage _metric-based_ or _log-based_ rules, you must have the necessary permissions.

### Request IAM organization roles for _metric-based_ rules 

Contact your Organization IAM Admin to request the following roles:

  * **MonitoringRule PA Creator** (`monitoringrule-pa-creator`): create `MonitoringRule` custom resources.
  * **MonitoringRule PA Editor** (`monitoringrule-pa-editor`): edit or delete `MonitoringRule` custom resources.
  * **MonitoringRule PA Viewer** (`monitoringrule-pa-viewer`): view `MonitoringRule` custom resources.

### Request IAM project roles for _metric-based_ rules




Contact your Project IAM Admin to request the following roles:

  * **MonitoringRule Editor** (`monitoringrule-editor`): edit or delete `MonitoringRule` custom resources in the project namespace.
  * **MonitoringRule Viewer** (`monitoringrule-viewer`): view `MonitoringRule` custom resources in the project namespace.



### Request IAM organization roles for _log-based_ rules

Contact your Organization IAM Admin to request the following roles:

  * **LoggingRule PA Creator** (`loggingrule-pa-creator`): create `LoggingRule` custom resources.
  * **LoggingRule PA Editor** (`loggingrule-pa-editor`): edit or delete `LoggingRule` custom resources.
  * **LoggingRule PA Viewer** (`loggingrule-pa-viewer`): view `LoggingRule` custom resources.



### Request IAM project roles for _log-based_ rules

Contact your Project IAM Admin to request the following roles:

  * **LoggingRule Editor** (`loggingrule-editor`): edit or delete `LoggingRule` custom resources in the project namespace.
  * **LoggingRule Viewer** (`loggingrule-viewer`): view `LoggingRule` custom resources in the project namespace.



## Define alert rules

You can define alert rules in your project namespace using either the GDC console (preferred) or the monitoring and logging APIs to apply custom resources.

Select one of the following methods to define alert rules based on metrics or logs:

###  Console 

Create alert rules in rule groups from the GDC console:

  1. In the GDC console, select a project.
  2. In the navigation menu, select **Operations** > **Alerting**.
  3. Click the **Alerting Policy** tab.
  4. Click add **Create Rule Group**.
  5. Choose the alert rule type:

     * Select **Metrics** for alert rules based on metrics.
     * Select **Logs** for alert rules based on logs.
  6. Configure the alert rule group:

     * In the **Alert rule group name** field, enter a name for the rule group.
     * In the **Rule evaluation interval** field, enter the number of seconds for each interval.
     * In the **Limit** field, enter the maximum number of alerts.

**Note:** Enter `0` for unlimited alerts.
  7. In the **Alert rules** section, click add **Add Rule**.

  8. In the **Create alert rule** window, enter the following details:

     * A name for the alert rule.
     * An expression for the alert rule (Use [LogQL](https://grafana.com/docs/loki/latest/logql/) for log-based rules and [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/) for metric-based rules).

**Note:** This expression must evaluate to a true or false statement, which determines whether the alert must move to a pending state or not.
     * The duration in seconds before an alert transitions from _pending_ to _open_.

**Note:** If you set the duration to a value of `0`, the system sends the alert immediately after the condition is met.
     * The severity level, such as **Error** or **Warning**.

     * A short name to identify the related resource.

     * An alert code to identify the alert.

     * A runbook URL or troubleshooting information.

     * An alert message or description.

     * Optional: Add **Labels** and **Annotations** as key-value pairs.

  9. Click **Save** to create the rule.

  10. Click **Create** to create the rule group.




The rule group appears in the **Alert rule group** list. You can group more alert rules within this rule group.

###  API 

Create alert rules from the monitoring or logging APIs:

  1. Define a `MonitoringRule` (metric-based rules) or `LoggingRule` (log-based rules) custom resource in a YAML file.

The complete resource specification shows an example for metric-based and log-based rules.

  2. Replace the following values in the YAML file according to your needs:

Field | Description  
---|---  
`namespace` | The project namespace.  
`name` | The name for the alert rule configuration.  
`source` | The log source for the alert rule. Valid options are `operational` and `audit`. Only applicable for `LoggingRule` resources.  
`interval` | The duration of the rule evaluation interval in seconds.  
`limit` | _Optional_. The maximum number of alerts. Set to `0` for unlimited alerts.  
`alertRules` | The definitions for creating alert rules.  
`alertRules.alert` | The name of the alert.  
`alertRules.expr` | A [LogQL](https://grafana.com/docs/loki/latest/logql/) expression for log-based rules or a [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/) expression for metric-based rules. The expression must evaluate to a true or false value to determine if the alert transitions to a pending state.  
`alertRules.for` | _Optional_. The duration in seconds before an alert transitions from _pending_ to _open_. Defaults to `0` seconds (immediate triggering).  
`alertRules.labels` | Key-value pairs to categorize and identify the alert. It requires the following labels: `severity`, `code`, and `resource`.  
`alertRules.annotations` | _Optional_. Non-identifying metadata to the alert as key-value pairs.  
  3. Save the YAML file.

  4. Apply the resource configuration to the Management API server within the same namespace as your metric-based or log-based alert rules:
         
         kubectl --kubeconfig KUBECONFIG_PATH apply -f ALERT_RULE_NAME.yaml
         

Replace the following:

     * `KUBECONFIG_PATH`: the path to the kubeconfig file for the Management API server.
     * `ALERT_RULE_NAME`: the name of the `MonitoringRule` or `LoggingRule` definition file.



## Complete resource specification

This section contains the YAML templates you can use to create metric-based and log-based alert rules by applying custom resources. If you create alerts from the GDC console, you can skip this section.

Define alert rules in the following custom resources:

  * `MonitoringRule`: metric-based rules.
  * `LoggingRule`: log-based rules.




###  MonitoringRule 

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
    
      # Configure metric-based alert rules.
      alertRules:
        # Define an alert name.
      - alert: my-metric-based-alert
    
        # Define the PromQL expression to evaluate for this rule.
        expr: rate({service_name="bob-service"} [1m])
    
        # The duration in seconds before an alert transitions from pending to open.
        # Optional.
        # Default value: '0s'
        for: 0s
    
        # Define labels to add or overwrite.
        # Map of key-value pairs.
        # Required labels:
        #     severity: [error, critical, warning, info]
        #     code:
        #     resource: component/service/hardware related to the alert
        # Additional labels are optional.
        labels:
          severity: error
          code: 202
          resource: AIS
          another-label: another-value
    
        # Define annotations to add.
        # Map of key-value pairs.
        # Optional.
        # Recommended annotations:
        #     message: value of the Message field in the user interface.
        #     expression: value of the Rule field in the user interface.
        #     runbookurl: URL of the Actions to take field in the user interface.
        annotations:
          message: my-alert-message
    

Replace the following:

  * `PROJECT_NAMESPACE`: your project namespace.
  * `MONITORING_RULE_NAME`: the name of the `MonitoringRule` definition file.



###  LoggingRule 

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
    
      # Configure log-based alert rules.
      alertRules:
        # Define an alert name.
      - alert: my-log-based-alert
    
        # Define the LogQL expression to evaluate for this rule.
        expr: rate({service_name="bob-service"} [1m])
    
        # The duration in seconds before an alert transitions from pending to open.
        # Optional.
        # Default value: '0s'
        for: 0s
    
        # Define labels to add or overwrite.
        # Map of key-value pairs.
        # Required labels:
        #     severity: [error, critical, warning, info]
        #     code:
        #     resource: component/service/hardware related to the alert
        # Additional labels are optional.
        labels:
          severity: warning
          code: 202
          resource: AIS
          another-label: another-value
    
        # Define annotations to add.
        # Map of key-value pairs.
        # Optional.
        # Recommended annotations:
        #     message: value of the Message field in the user interface.
        #     expression: value of the Rule field in the user interface.
        #     runbookurl: URL of the Actions to take field in the user interface.
        annotations:
          message: my-alert-message
    

Replace the following:

  * `PROJECT_NAMESPACE`: your project namespace.
  * `LOGGING_RULE_NAME`: the name of the `LoggingRule` definition file.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
