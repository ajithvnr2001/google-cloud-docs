---
url: https://docs.cloud.google.com/monitoring/promql/promql-migrate/
title: Migrate alerting rules and receivers from Prometheus \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:21.870930+00:00
---

# Migrate alerting rules and receivers from Prometheus  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/promql/promql-migrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Migrate alerting rules and receivers from Prometheus Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to migrate Prometheus alerting rules to PromQL-based alerting policies in Cloud Monitoring. The migration process is useful if you use PromQL in environments outside Google Cloud. By migrating your Prometheus alerting rules to Cloud Monitoring, you can manage all of your alerting policies in one environment.

For general information about PromQL-based alerting policies, see [PromQL alerting overview](https://docs.cloud.google.com/monitoring/promql/promql-in-alerting).

You can also import Grafana dashboards. For more information, see [Import Grafana dashboards into Cloud Monitoring](https://docs.cloud.google.com/monitoring/dashboards/import-grafana-dashboards).

## How migration works

In the gcloud CLI, you can migrate your existing alerting rules and receivers to create Cloud Monitoring alerting policies and notification channels. The gcloud CLI can perform the following types of migration:

  * If you provide a Prometheus [configuration file](https://prometheus.io/docs/alerting/latest/configuration/) with an alerting rule, then the gcloud CLI creates a PromQL-based alerting policy.

You can provide multiple Prometheus configuration files at the same time to create multiple PromQL-based alerting policies.

  * If you provide a Prometheus [Alertmanager](https://prometheus.io/docs/alerting/latest/Alertmanager/) file with at least one receiver, then the gcloud CLI converts each receiver to an equivalent notification channel in Monitoring.

**Note:** You can migrate an AlertManager receiver only when Cloud Monitoring supports the same type of notification channel. For example, Cloud Monitoring doesn't support Jira receivers, so they can't be migrated from a Prometheus AlertManager file. If you try to migrate an incompatible receiver, then the gcloud CLI ignores the receiver. If you want to use a receiver that Cloud Monitoring doesn't support, then [create a notification channel](https://docs.cloud.google.com/monitoring/support/notification-options) that uses Webhook for public endpoints or Pub/Sub for private endpoints.
  * If you provide a Prometheus Alertmanager file and a Prometheus configuration file at the same time, then the gcloud CLI creates the alerting policy and notification channels, and then associates each new notification channel with the new alerting policy.

If you provide multiple configuration files with alerting rules, then gcloud CLI assigns every notification channel from the Alertmanager file to each new alerting policy.




If your Prometheus alerting rule references a custom metric, then the gcloud CLI requires an equivalent metric descriptor to create the alerting policy.

Prometheus configuration files and Prometheus Alertmanager files must be formatted as valid Prometheus [rule files](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/#configuring-rules) in either YAML or JSON.

### Field Mapping

The gcloud CLI maps fields between a Prometheus alerting rule and a Cloud Monitoring alerting policy as follows:

Prometheus alerting rule | Cloud Monitoring alerting policy  
---|---  
`alert` | `conditionPrometheusQueryLanguage.alertRule`  
`expr` | `conditionPrometheusQueryLanguage.query`  
`for` | `conditionPrometheusQueryLanguage.duration`  
`labels` | `conditionPrometheusQueryLanguage.labels`  
`annotations: "summary"` | `documentation.subject`  
`annotations: "description"` | `documentation.content`  
  
### Google Cloud documentation variables in migrated Prometheus alerting rules

Prometheus uses [alert field templates](https://prometheus.io/docs/prometheus/latest/configuration/template_examples/) to configure variables in alerting rule annotations and labels. When you migrate Prometheus alerting rules that have alert field templates, Cloud Monitoring converts the templates to Cloud Monitoring [documentation variables](https://docs.cloud.google.com/monitoring/alerts/doc-variables) as follows:

Prometheus alert field template | Cloud Monitoring documentation variable  
---|---  
`{{$value}}` |  `${metric.label.value}` This variable is an implementation of `${metric.label.KEY}`, where `value` holds the value of the PromQL query.  
`{{humanize $value}}` |  `${metric.label.value}` This variable is an implementation of `${metric.label.KEY}`, where `value` holds the value of the PromQL query.  
`{{$labels}}` | `${metric_or_resource.labels}`  
`{{humanize $labels}}` | `${metric_or_resource.labels}`  
`{{$labels.key}}` |  Appears as `${metric_or_resource.label.KEY}` in the alerting policy documentation configuration.

  * If KEY is a valid label, then this variable renders in the notification as the value of `${metric.label.KEY}`.
  * If KEY is a valid resource, then this variable renders in the notification as the value of `${resource.label.KEY}`.
  * If KEY is neither a valid label nor a valid resource, then this variable renders in the notification as an empty string.

  
`{{humanize $labels.<key>}}` |  Appears as `${metric_or_resource.label.KEY}` in the alerting policy documentation configuration.

  * If KEY is a valid label, then this variable renders in the notification as the value of `${metric.label.KEY}`.
  * If KEY is a valid resource, then this variable renders in the notification as the value of `${resource.label.KEY}`.
  * If KEY is neither a valid label nor a valid resource, then this variable renders in the notification as an empty string.

  
  
## Migrate alerting rules and receivers from Prometheus

To migrate your Prometheus alerting rules to Cloud Monitoring PromQL-based alerting policies, use the [`gcloud monitoring policies migrate`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies/migrate) command. This command also lets you migrate your Prometheus receivers to Cloud Monitoring notification channels.

  * To migrate an alerting rule, you must have a YAML or JSON Prometheus [rule file](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/#configuring-rules) file that contains the alerting rule.
  * To migrate a receiver, you must a YAML or JSON Prometheus [Alertmanager](https://prometheus.io/docs/alerting/latest/Alertmanager/) file that contains the receiver.

**Note:** You can migrate an AlertManager receiver only when Cloud Monitoring supports the same type of notification channel. For example, Cloud Monitoring doesn't support Jira receivers, so they can't be migrated from a Prometheus AlertManager file. If you try to migrate an incompatible receiver, then the gcloud CLI ignores the receiver. If you want to use a receiver that Cloud Monitoring doesn't support, then [create a notification channel](https://docs.cloud.google.com/monitoring/support/notification-options) that uses Webhook for public endpoints or Pub/Sub for private endpoints.



Google Cloud doesn't support migrating Prometheus [recording rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/). To use recording rules, we recommend using a [self-deployed rule evaluator](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-unmanaged).

### Create an alerting policy from a Prometheus configuration file

To create an alerting policy from a Prometheus configuration file, run the following command. You can create multiple alerting policies by providing multiple file paths:
    
    
    gcloud monitoring policies migrate \
    --policies-from-prometheus-alert-rules-yaml=PATH_TO_FILE_1,PATH_TO_FILE_2
    

### Create notification channels from a Prometheus Alertmanager configuration file

To create notification channels from a Prometheus Alertmanager configuration file, run the following command:
    
    
    gcloud monitoring policies migrate \
    --channels-from-prometheus-alertmanager-yaml=PATH_TO_FILE
    

### Create alerting policies and notification channels at the same time

To create alerting policies from Prometheus configuration files and to create notification channels from a Prometheus Alertmanager configuration file at the same time, run the following command:
    
    
    gcloud monitoring policies migrate \
    --policies-from-prometheus-alert-rules-yaml=PATH_TO_FILE_1,PATH_TO_FILE_2 \
    --channels-from-prometheus-alertmanager-yaml=PATH_TO_FILE
    

#### Example

You have a Prometheus configuration file with an alerting rule that sends out an alert when CPU utilization stays greater than 75% for one minute. The alerting rule is configured as follows:
    
    
    groups:
    - name: Utilization_Alerts
      interval: 30s
      rules:
      - alert: CPU_Utilization_Over_75
        expr: compute_googleapis_com:instance_cpu_utilization > 75
        for: 60s
        labels:
          severity: page
        annotations:
          subject: "Subject: ${metric.label.value}"
          description: "CPU utilization is over 75%"
    

You also have a Prometheus AlertManager file that contains email, PagerDuty, and webhook receivers.
    
    
    receivers:
    - name: 'team-emails'
      email_configs:
      - to: EMAIL_ADDRESS
    - name: 'team-pager'
      pagerduty_configs:
      - service_key: SERVICE_KEY
    - name: 'team-webhook'
      webhook_configs:
      - url: WEBHOOK_ADDRESS
    

To create the alerting policy and notification channel, run the following command:
    
    
    gcloud monitoring policies migrate \
    --policies-from-prometheus-alert-rules-yaml=PATH_TO_CONFIG_FILE \
    --channels-from-prometheus-alertmanager-yaml=PATH_TO_ALERTMANAGER_FILE
    

The gcloud CLI then creates an alerting policy like the following example:
    
    
      {
      "name": "projects/PROJECT_ID/alertPolicies/POLICY_ID",
      "displayName": "Utilization_Alerts/CPU_Utilization_Over_75",
      "documentation": {
        "content": "CPU utilization is over 75%",
        "mimeType": "text/markdown",
        "subject": "Subject: ${metric.label.value}"
      },
      "userLabels": {},
      "conditions": [
        {
          "name": "projects/PROJECT_ID/alertPolicies/POLICY_ID/conditions/CONDITION_ID",
          "displayName": "CPU_Utilization_Over_75"
          "conditionPrometheusQueryLanguage": {
            "alertRule": "CPU_Utilization_Over_75",
            "duration": "60s",
            "evaluationInterval": "30s",
            "labels": {
              "severity": "page"
            },
            "query": "compute_googleapis_com:instance_cpu_utilization > 75",
            "ruleGroup": "Utilization_Alerts"
          }
        }
      ],
      "alertStrategy": {},
      "combiner": "OR",
      "enabled": true,
      "notificationChannels": [
        "projects/google.com:PROJECT_ID/notificationChannels/CHANNEL_ID_1",
        "projects/google.com:PROJECT_ID/notificationChannels/CHANNEL_ID_2",
        "projects/google.com:PROJECT_ID/notificationChannels/CHANNEL_ID_3"
      ]
    }
    

## Migrate alerting rules from Managed Service for Prometheus

Google Cloud configures [managed rule evaluation](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed) for Managed Service for Prometheus by using the [Rules](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#rules), [ClusterRules](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#clusterrules), and [GlobalRules](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.17.2/doc/api.md#globalrules) custom resources.

To migrate these resources to a Google Cloud PromQL-based alerting policy, do the following:

  1. Copy the `groups` section of the custom resource into a new Prometheus [rule file](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/#configuring-rules).

  2. Migrate the rule file by [using the gcloud CLI](https://docs.cloud.google.com/monitoring/promql/promql-migrate#create-policy-from-prom).




For example, you have the following Rules custom resource:
    
    
    apiVersion: monitoring.googleapis.com/v1
    kind: Rules
    metadata:
      namespace: NAMESPACE_NAME
      name: example-rules
    spec:
      groups:
      - name: example
        interval: 30s
        rules:
        - alert: FewerThanTenInstancesUp
          expr: sum(up) < 10
    

The Prometheus rules file created by copying `groups` from the previous Rules custom resource would look like the following:
    
    
      groups:
      - name: example
        interval: 30s
        rules:
        - alert: FewerThanTenInstancesUp
          expr: sum(up) < 10
    

### Migrate multiple Rules custom resources

If you want to migrate multiple Rules, CustomRules, or GlobalRules, then we recommend constructing and migrating a separate rules file for each resource. For more information, see the [Prometheus documentation](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/#failed-rule-evaluations-due-to-slow-evaluation).

### Manage filter and aggregation expressions

Rules and ClusterRules automatically filter their Prometheus alert expressions based on certain labels. To preserve this behavior in the query of a migrated alerting policy, you must explicitly include these labels in a filter or aggregation expression in your Prometheus rules file before you migrate the file.

For example, [the managed rule evaluator for Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed) executes the expression `sum(up) < 10` as follows:
    
    
    sum(up{project_id="test-project", cluster="test-cluster", namespace="NAMESPACE_NAME"}) < 10
    

However, if an alerting policy has the PromQL query `sum(up) < 10`, then Cloud Monitoring executes the query as only `sum(up) < 10`. This query is applied to every Google Cloud project, cluster, and namespace in your metrics scope. To avoid this behavior, we recommend aggregating by labels in your query to ensure that Cloud Monitoring executes your query as intended. For example, when you create your rules file from the Rules custom resource, you could change `sum(up) < 10` to the following expression:
    
    
    sum (up) by (project_id, cluster, namespace) < 10
    

The previous expression generates a separate time series for each Google Cloud project, cluster, and namespace, and then compares each time series to the alert threshold of `<10`.

The following table shows the order of evaluation of alert-expression filters for Rules and ClusterRules:

Rule resource type | Filter labels  
---|---  
Rule | 

  1. `project_id`
  2. `cluster`
  3. `namespace`

  
ClusterRule | 

  1. `project_id`
  2. `cluster`

  
  
For more information about filtering behavior in Prometheus expressions, see [Instant vector selectors](https://prometheus.io/docs/prometheus/latest/querying/basics/#instant-vector-selectors).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
