---
url: https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.AlertPolicy.Condition
title: Class Condition (2.32.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:50:42.136147+00:00
---

# Class Condition (2.32.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.AlertPolicy.Condition

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Condition (2.32.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.32.0 (latest)  2.31.0  2.30.0  2.29.1  2.28.0  2.27.2  2.26.0  2.25.0  2.24.0  2.23.1  2.22.2  2.21.0  2.20.0  2.19.4  2.18.0  2.17.0  2.16.0  2.15.1  2.14.2  2.13.0  2.12.0  2.11.3  2.10.1  2.9.2  2.8.0  2.7.0  2.6.0  2.5.2  2.4.2  2.3.0  2.2.1  2.1.0  2.0.1  1.1.2  1.0.0  0.36.2  0.35.0  0.34.0  0.33.0  0.32.0 
    
    
    Condition(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A condition is a true/false test that determines when an alerting policy should open an incident. If a condition evaluates to true, it signifies that something is wrong.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required if the condition exists. The unique resource name for this condition. Its format is: :: projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[POLICY_ID]/conditions/[CONDITION_ID] `[CONDITION_ID]` is assigned by Cloud Monitoring when the condition is created as part of a new or updated alerting policy. When calling the `alertPolicies.create][google.monitoring.v3.AlertPolicyService.CreateAlertPolicy]` method, do not include the `name` field in the conditions of the requested alerting policy. Cloud Monitoring creates the condition identifiers and includes them in the new policy. When calling the `alertPolicies.update][google.monitoring.v3.AlertPolicyService.UpdateAlertPolicy]` method to update a policy, including a condition `name` causes the existing condition to be updated. Conditions without names are added to the updated policy. Existing conditions are deleted if they are not updated. Best practice is to preserve `[CONDITION_ID]` if you make only small changes, such as those to condition thresholds, durations, or trigger values. Otherwise, treat the change as a new condition and let the existing condition be deleted.   
`display_name` |  `str`   
A short name or phrase used to identify the condition in dashboards, notifications, and incidents. To avoid confusion, don't use the same display name for multiple conditions in the same policy.   
`condition_threshold` |  `[google.cloud.monitoring_v3.types.AlertPolicy.Condition.MetricThreshold](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.AlertPolicy.Condition.MetricThreshold)`   
A condition that compares a time series against a threshold. This field is a member of `oneof`_ `condition`.   
`condition_absent` |  `[google.cloud.monitoring_v3.types.AlertPolicy.Condition.MetricAbsence](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.AlertPolicy.Condition.MetricAbsence)`   
A condition that checks that a time series continues to receive new data points. This field is a member of `oneof`_ `condition`.   
`condition_matched_log` |  `[google.cloud.monitoring_v3.types.AlertPolicy.Condition.LogMatch](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.AlertPolicy.Condition.LogMatch)`   
A condition that checks for log messages matching given constraints. If set, no other conditions can be present. This field is a member of `oneof`_ `condition`.   
`condition_monitoring_query_language` |  `[google.cloud.monitoring_v3.types.AlertPolicy.Condition.MonitoringQueryLanguageCondition](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.AlertPolicy.Condition.MonitoringQueryLanguageCondition)`   
A condition that uses the Monitoring Query Language to define alerts. This field is a member of `oneof`_ `condition`.   
`condition_prometheus_query_language` |  `[google.cloud.monitoring_v3.types.AlertPolicy.Condition.PrometheusQueryLanguageCondition](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.AlertPolicy.Condition.PrometheusQueryLanguageCondition)`   
A condition that uses the Prometheus query language to define alerts. This field is a member of `oneof`_ `condition`.   
`condition_sql` |  `[google.cloud.monitoring_v3.types.AlertPolicy.Condition.SqlCondition](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.AlertPolicy.Condition.SqlCondition)`   
A condition that periodically evaluates a SQL query result. This field is a member of `oneof`_ `condition`.   
  
## Classes 

### EvaluationMissingData
    
    
    EvaluationMissingData(value)

A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. This control doesn't affect metric-absence policies.

### LogMatch
    
    
    LogMatch(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A condition type that checks whether a log message in the `scoping project <https://cloud.google.com/monitoring/api/v3#project_name>`__ satisfies the given filter. Logs from other projects in the metrics scope are not evaluated.

### MetricAbsence
    
    
    MetricAbsence(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A condition type that checks that monitored resources are reporting data. The configuration defines a metric and a set of monitored resources. The predicate is considered in violation when a time series for the specified metric of a monitored resource does not include any data in the specified `duration`.

### MetricThreshold
    
    
    MetricThreshold(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A condition type that compares a collection of time series against a threshold.

### MonitoringQueryLanguageCondition
    
    
    MonitoringQueryLanguageCondition(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

A condition type that allows alerting policies to be defined using `Monitoring Query Language <https://cloud.google.com/monitoring/mql>`__.

### PrometheusQueryLanguageCondition
    
    
    PrometheusQueryLanguageCondition(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

A condition type that allows alerting policies to be defined using `Prometheus Query Language (PromQL) <https://prometheus.io/docs/prometheus/latest/querying/basics/>`__.

The PrometheusQueryLanguageCondition message contains information from a Prometheus alerting rule and its associated rule group.

A Prometheus alerting rule is described `here <https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/>`**. The semantics of a Prometheus alerting rule is described`here <https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/#rule>`**.

A Prometheus rule group is described `here <https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/>`**. The semantics of a Prometheus rule group is described`here <https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/#rule_group>`**.

Because Cloud Alerting has no representation of a Prometheus rule group resource, we must embed the information of the parent rule group inside each of the conditions that refer to it. We must also update the contents of all Prometheus alerts in case the information of their rule group changes.

The PrometheusQueryLanguageCondition protocol buffer combines the information of the corresponding rule group and alerting rule. The structure of the PrometheusQueryLanguageCondition protocol buffer does NOT mimic the structure of the Prometheus rule group and alerting rule YAML declarations. The PrometheusQueryLanguageCondition protocol buffer may change in the future to support future rule group and/or alerting rule features. There are no new such features at the present time (2023-06-26).

### SqlCondition
    
    
    SqlCondition(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A condition that allows alerting policies to be defined using GoogleSQL. SQL conditions examine a sliding window of logs using GoogleSQL. Alert policies with SQL conditions may incur additional billing.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### Trigger
    
    
    Trigger(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Specifies how many time series must fail a predicate to trigger a condition. If not specified, then a `{count: 1}` trigger is used.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
