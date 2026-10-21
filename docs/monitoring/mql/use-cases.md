---
url: https://docs.cloud.google.com/monitoring/mql/use-cases/
title: Use cases for MQL alerts \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:18:37.506630+00:00
---

# Use cases for MQL alerts  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/mql/use-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Use cases for MQL alerts Stay organized with collections  Save and categorize content based on your preferences. 

**Announcement:** On July 22, 2025, Google Cloud customer support for MQL ended, and MQL is no longer available in the Google Cloud console when you create charts, dashboards, and alerting policies. Existing MQL charts, dashboards, and alerting policies continue to work, and you can still create them by using the Cloud Monitoring API. For more information, see the [deprecation notice for MQL](https://docs.cloud.google.com/stackdriver/docs/deprecations/mql). 

Alerting policies with a Monitoring Query Language (MQL)-based condition let you configure your alerting environment for many possible use cases. Certain configurations are available only through the use of MQL queries.

This document describes several uses cases and sample queries for deploying alerting policies with an MQL-based condition in a production environment.

## Alert on dynamic thresholds

You can use an MQL query to configure an alerting policy that triggers alerts based on a threshold that varies over time, such as days of the week. This configuration isn't supported in alerting policy conditions without MQL queries.

For example, you have an MQL query that sends an alert if the CPU utilization of a Compute Engine instance exceeds 95%:
    
    
    fetch gce_instance :: compute.googleapis.com/instance/cpu/utilization
    | align
    | every 30s
    | condition utilization > 95'%'
    

However, you want to set a lower utilization threshold, such as 85%, for weekends, to account for longer response times from your support team. In this case, you could configure your query with a value column that contains the alerting threshold:
    
    
    fetch gce_instance :: compute.googleapis.com/instance/cpu/utilization
    | align
    | every 30s
    | value add [day_of_week: end().timestamp_to_string('%w').string_to_int64]
    | value [utilization, is_weekend: day_of_week = 0 || day_of_week = 6]
    | value [utilization, max_allowed_utilization: if(is_weekend, 85'%', 95'%')]
    | condition utilization > scale(max_allowed_utilization)
    

The [value](https://docs.cloud.google.com/monitoring/mql/reference#value-tabop) operations do the following:

  * `value add [day_of_week: end().timestamp_to_string('%w').string_to_int64]` adds a value column whose value is a number between 0 and 6, where `0` is Sunday and `6` is Saturday.
  * `value [utilization, is_weekend: day_of_week = 0 || day_of_week = 6]` replaces your day number with a boolean that indicates whether the data point was on a weekend or a weekday.
  * `value [utilization, max_allowed_utilization: if(is_weekend, 85'%', 95'%')]` replaces the boolean with a threshold that varies depending on the value of `is_weekend`.



The condition, `condition utilization > scale(max_allowed_utilization)`, compares the two value columns.

For an example of an alerting policy with an MQL-based condition that configures alert severity levels based on dynamic criteria, see [Create dynamic severity levels using MQL](https://docs.cloud.google.com/monitoring/alerts/labels#example-dynamic-label).

## Alert on thresholds based on rate of change

You can configure alerting policy MQL queries to evaluate thresholds based on the rate of change for a metric. For example, you want to evaluate the rate of `5xx` errors per instance of `resource.method` in your API requests, where your rate is equivalent to requests per second. If the rate is greater than 5 error responses per second, then Cloud Monitoring sends an alert:
    
    
    fetch consumed_api
    | metric 'serviceruntime.googleapis.com/api/request_count'
    | filter (metric.response_code_class == '5xx')
    | align rate(10m)
    | every 30s
    | group_by [resource.method],
        [value_request_count_mean: mean(value.request_count)]
    | condition val() > 0.05'1/s'
    

You can create rate-of-change alerting policies without using MQL:

  * For an example that uses the Google Cloud console, see [Monitor a rate of change](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#rate-of-change).
  * For an example that uses the Cloud Monitoring API, see [Rate of change policy](https://docs.cloud.google.com/monitoring/alerts/policies-in-json#json-rate-of-change).



## Alert on ratio-based thresholds

Your alerting policy can use an MQL query to evaluate ratios derived by joining two metrics and then dividing the value columns. For example, you want to query the ratio of `read` bytes compared to `write` bytes for each of your Compute Engine instances. If the ratio is greater than `3/5`, or 60%, then Cloud Monitoring sends an alert:
    
    
    {
      fetch gce_instance :: compute.googleapis.com/instance/disk/read_bytes_count;
      fetch gce_instance :: compute.googleapis.com/instance/disk/write_bytes_count
    }
    | every 30s
    | join
    | value val(0) / val(1)
    | condition val() > 0.6
    

**Note:** The `ratio` table operation is also equivalent to `value val(0) / val(1)`.

You can also query the ratio of aggregated values. For example, you want to compute the average CPU usage time per core across your Compute Engine instances. If the ratio is greater than than `3/5`, or 60%, then Cloud Monitoring sends an alert. In this example, you must also include a [`cast_units`](https://docs.cloud.google.com/monitoring/mql/reference#cast_units-func) function to align the units of measurement.
    
    
    {
      fetch gce_instance :: compute.googleapis.com/instance/cpu/usage_time
      | group_by [], .sum;
      fetch gce_instance :: compute.googleapis.com/instance/cpu/reserved_cores
      | group_by [], .sum | cast_units('s{CPU}')
    }
    | every 30s
    | ratio
    | condition val() > 0.6
    

You can create ratio-based alerting policies without using MQL:

  * For an example that uses the Google Cloud console, see [Compute ratios](https://docs.cloud.google.com/monitoring/mql/examples#qlx-ratios).
  * For an example that uses the Cloud Monitoring API, see [Metric ratio](https://docs.cloud.google.com/monitoring/alerts/policies-in-json#json-ratio).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
