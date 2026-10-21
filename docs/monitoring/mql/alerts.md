---
url: https://docs.cloud.google.com/monitoring/mql/alerts/
title: Alerting policies with MQL \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:18:37.361396+00:00
---

# Alerting policies with MQL  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/mql/alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Alerting policies with MQL Stay organized with collections  Save and categorize content based on your preferences. 

**Announcement:** On July 22, 2025, Google Cloud customer support for MQL ended, and MQL is no longer available in the Google Cloud console when you create charts, dashboards, and alerting policies. Existing MQL charts, dashboards, and alerting policies continue to work, and you can still create them by using the Cloud Monitoring API. For more information, see the [deprecation notice for MQL](https://docs.cloud.google.com/stackdriver/docs/deprecations/mql). 

By using the Cloud Monitoring API, you can create Monitoring alerting policies whose condition includes a Monitoring Query Language (MQL) query. MQL queries for alerting policy conditions are like other MQL queries, except that they also include a MQL alerting operation. If you use MQL in a condition, then that condition must be the only condition in the policy.

This page introduces MQL alerting operations and describes how to create an alerting policy that uses them. For general information on Monitoring alerting policies, see [Behavior of metric-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth).

## Get started

All MQL queries start with the following components:

  * A `fetch` operation, which retrieves time series from Cloud Monitoring.
  * An argument, consisting of a monitored resource and a metric type, that identifies the time series to fetch.



For example, the following query retrieves the time series written by Compute Engine instances for the metric type `compute.googleapis.com/instance/cpu/utilization`, which records the CPU utilization of those instances:
    
    
    fetch gce_instance::compute.googleapis.com/instance/cpu/utilization
    

The argument of the `fetch` command consists of a monitored-resource type `gce_instance`, a pair of colon characters, `::`, and a metric type, `compute.googleapis.com/instance/cpu/utilization`.

**Note:** Your query must not include an explicit time-range specification, that is, a [`within`](https://docs.cloud.google.com/monitoring/mql/reference#within-tabop) operation.

To use your query in an alerting policy with an MQL-based condition, your query must end with an operation that defines the parameters under which Cloud Monitoring triggers an alert. The operation varies depending on whether you're building a metric-threshold alerting policy or a metric-absence alerting policy.

### MQL queries for metric-threshold alerting policies

Metric-threshold MQL queries require the [`condition`](https://docs.cloud.google.com/monitoring/mql/reference#condition-tabop) operation, which evaluates a boolean expression at each point within the query execution time. If the expression evaluates to `true` for all points in the duration window, then Cloud Monitoring triggers an alert.

For example, the following query evaluates Compute Engine VM instances and triggers an alert if any instance wrote more than 5 gigabytes to disk over the last 24 hours:
    
    
    fetch gce_instance :: compute.googleapis.com/instance/disk/write_bytes_count
    | group_by 24h, .sum
    | every 30s
    | condition val() > 5'GBy'
    

You can use complex conditions to evaluate specific ranges of data. For example, the following condition triggers an alert if a VM instance over the last 24 hours wrote greater than five gigabytes and less than six gigabytes of data, or greater than 8 gigabytes of data:
    
    
    fetch gce_instance :: compute.googleapis.com/instance/disk/write_bytes_count
    | group_by 24h, .sum
    | every 30s
    | condition (val() > 5'GBy' && val() < 6'GBy') || val() > 8'GBy'
    

The following example uses `filter`, a sliding `group_by` operation, and a complex condition to evaluate each data point in an aligned input table and determine whether the utilization value exceeds the threshold value of 15%:
    
    
    fetch gce_instance::compute.googleapis.com/instance/cpu/utilization
    | filter zone =~ 'us-central.*'
    | group_by sliding(5m), mean(val())
    | every 30s
    | condition val() > .15 '10^2.%'
    

In the previous query, the table resulting from the `condition` operator has two value columns, a boolean column recording the result of the threshold evaluation, and a second containing a copy of the `utilization` value column from the input table. Because the default `group_by` window setting is sliding, the `group_by` expression is identical to `group_by 5m, mean(val())`.

The CPU-utilization value is stored as fractional utilization; the values range from 0.0 to 1.0. The metric descriptor specifies the unit for these value as `10^2.%`, which the chart displays as a percentage. The units for the threshold have to be compatible, so we express the threshold as `.15 '10^2.%`.

### MQL queries for metric-absence alerting policies

Metric-absence MQL queries use the [`absent_for`](https://docs.cloud.google.com/monitoring/mql/reference#absent_for-tabop) operation, which takes a duration for which data must be missing. For example, the following query tests to see if data has been missing from the US central zones for eight hours:
    
    
    fetch gce_instance::compute.googleapis.com/instance/cpu/utilization
    | filter zone =~ 'us-central.*'
    | every 30s
    | **absent_for 8h**
    

The `absent_for` operation takes only a duration argument, which indicates for how long data must be absent to satisfy the condition.

Data is considered absent if data has appeared in the last 24-hour period but not within the duration, in this example, the most recent eight hours.

An `absent_for` query creates an output table with aligned values, using either the default alignment or by using an `every` operation following the `absent_for` operation.

The output table has two columns.

  * The first is the `active` column, which records the boolean results for data absence. A `true` value means there was an input point within the last 24 hours and none within the duration period.

  * The second column is the `signal` column. If the input table has value columns, then the `signal` column contains the value from the first value column of the most recent input point. If the input table has no value columns, then the `signal` column contains the number of minutes since the last input point was recorded. You can force this case, as shown in the following example:
        
        fetch gce_instance::compute.googleapis.com/instance/cpu/utilization
        | filter zone =~ 'us-central.*'
        | value []
        | every 30s
        | **absent_for 8h**
        

In the preceding example, the `value []` operation removes the value columns from its input table, so the `signal` column in the table created by the `absent_for` operation contain the number of minutes since the last input point was recorded.




### Alerting policy configuration

In addition to the MQL query, an alerting-policy condition includes two other values:

  * The number of input time series that must satisfy the condition. The value can be any of the following: 
    * A single time series.
    * A specific number of time series.
    * A percentage of time series.
    * All time series.
  * Duration of the alert state, that is, how long the alert condition must continuously evaluate to `true`.



If the query continuously evaluates to `true` for the specified duration for a particular time series, then that time series is considered _active_. When the specified number of time series are active, the alerting policy is triggered and an alert is generated for each active time series. For more information about how alerting policies are evaluated, see [Behavior of metric-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth).

When time series data stops arriving or when data is delayed, Monitoring classifies the data as _missing_. For information about how to configure Monitoring to evaluate metric-threshold conditions when data stops arriving, see [Partial metric data](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#partial-metric-data).

If you use MQL in a condition, that condition must be the only condition in the policy. You can't use multiple conditions in MQL-based alerting policies.

## Guidelines

MQL lets you create user-defined labels and attach them to alerts. For examples, see [Add severity levels to an alerting policy](https://docs.cloud.google.com/monitoring/alerts/labels).

Units for metric types are listed in the relevant table of metric types; for the metric type `compute.googleapis.com/instance/cpu/utilization`, see the [`compute`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute) table.

## What's next

For information about how to use the Cloud Monitoring API to create an alerting policy, see [Creating conditions for alerting policies](https://docs.cloud.google.com/monitoring/mql/qn-from-api#ql-alert-condition).

For a list of guidelines and recommendations for configuring effective alerting policies with an MQL-based condition, see [Best practices for MQL alerts](https://docs.cloud.google.com/monitoring/mql/best-practices-alerts).

For information about how to troubleshoot common issues for alerting policies with an MQL-based condition, see [Troubleshoot MQL alerts](https://docs.cloud.google.com/monitoring/mql/troubleshooting).

For examples of alerting policies with an MQL-based condition, see [Use cases for MQL alerts](https://docs.cloud.google.com/monitoring/mql/use-cases).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
