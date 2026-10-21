---
url: https://docs.cloud.google.com/monitoring/mql/best-practices-alerts/
title: Best practices for MQL alerting policies \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:18:37.426626+00:00
---

# Best practices for MQL alerting policies  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/mql/best-practices-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Best practices for MQL alerting policies Stay organized with collections  Save and categorize content based on your preferences. 

**Announcement:** On July 22, 2025, Google Cloud customer support for MQL ended, and MQL is no longer available in the Google Cloud console when you create charts, dashboards, and alerting policies. Existing MQL charts, dashboards, and alerting policies continue to work, and you can still create them by using the Cloud Monitoring API. For more information, see the [deprecation notice for MQL](https://docs.cloud.google.com/stackdriver/docs/deprecations/mql). 

This page contains an index of best practices for alerting policies with a Monitoring Query Language (MQL)-based condition. You can use the information collected here as a quick reference of what to keep in mind when configuring an alerting policy with a MQL-based condition.

This page doesn't describe the basics of how to use MQL queries in your alerting policies. If you're a new user, then see [Alerting policies with MQL](https://docs.cloud.google.com/monitoring/mql/alerts).

## Recommended operations for MQL queries in alerting policies

Alerting policy evaluation involves multiple internal services. Due to the way these services interact with MQL, we strongly recommend using certain MQL operations instead of others. For example, if you use `delta` instead of `delta_gauge`, then alerts may trigger at incorrect times.

The following table shows a list of operations to avoid and recommended operations to use instead.

Avoid | Recommended  
---|---  
`adjacent_rate` | `rate`  
`adjacent_delta` | `delta_gauge`  
`delta` | `delta_gauge`  
`window` | `sliding`  
  
## Use the `every 30s` statement with alerting policies

Alerting policies evaluate their condition every 30 seconds. This range of time is called an output window. We recommend that your conditions include an explicit [`every 30s`](https://docs.cloud.google.com/monitoring/mql/reference#every-tabop) operation as a visual reminder of this period.

For example, the following alerting policy MQL query includes an explicit `every 30s` statement:
    
    
    fetch gce_instance :: compute.googleapis.com/instance/disk/write_bytes_count
    | group_by sliding(1h)
    | every 30s
    

If you save an alerting policy with an MQL query that uses a different value for the `every` operation, then Cloud Monitoring still uses a value of 30 seconds when the alerting policy is active. For example, an alerting policy with the following query still has a 30-second output window:
    
    
    fetch gce_instance :: compute.googleapis.com/instance/disk/write_bytes_count
    | group_by sliding(1h)
    | every 90s
    

## Improve query efficiency

Queries run slowly when processing large volumes of data. To improve query efficiency, you can try reducing the amount of data that the query processes. The following sections provide several options for reducing the volume of data that your query evaluates.

### Place filters earlier in your query

When you place filters earlier in your query, they can filter out unnecessary data before your query runs operations on your data. For example, consider the following query:
    
    
    fetch gce_instance :: compute.googleapis.com/instance/disk/write_bytes_count
    | group_by [resource.zone], .sum
    | filter zone = 'us-west1-b'
    | condition val() > 5'GBy'
    

The query might run faster if you move the `filter` operation before the `group_by` operation:
    
    
    fetch gce_instance :: compute.googleapis.com/instance/disk/write_bytes_count
    | filter zone = 'us-west1-b'
    | group_by [resource.zone], .sum
    | condition val() > 5'GBy'
    

### Decrease your query alignment window

When a query uses the `align` operation, a smaller alignment window represents a smaller range of time that Cloud Monitoring evaluates for each point in the time series. As a result, you can try improving your query efficiency by reducing the value of your `align` operation. For example, the following query has a two-hour alignment window:
    
    
    fetch gce_instance :: compute.googleapis.com/instance/disk/read_bytes_count
    | group_by window(1h), .sum
    | align next_older(2h)
    | every 30s
    | condition val() > 2'GBy'
    

However, if you need to see data for only a 1-hour window, then you could reduce the alignment window to 1 hour:
    
    
    fetch gce_instance :: compute.googleapis.com/instance/disk/read_bytes_count
    | group_by window(1h), .sum
    | align next_older(1h)
    | every 30s
    | condition val() > 2'GBy'
    

For more information, see [Alignment](https://docs.cloud.google.com/monitoring/mql/reference#alignment).

### Decrease your alerting policy duration window

The alerting policy duration window represents the time period in which each measure must violate the condition before an alert is sent. If you reduce the duration window of your alerting policy without increasing your query alignment window, then Cloud Monitoring has fewer points to evaluate for your alerting policy condition.

For more information, see [Duration window](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#duration-window).

## Assign default values to null metadata

If a metadata value is null, then your queries might produce unexpected results. You can avoid unexpected results by using the [`or_else`](https://docs.cloud.google.com/monitoring/mql/reference#or_else-func) function to assign a default value to metadata that would otherwise have a null value.

For example, you run a query that aggregates all of your data together:
    
    
    fetch k8s_pod :: networking.googleapis.com/pod_flow/egress_bytes_count
    | group_by [], 24h, sum(egress_bytes_count)
    | condition val() > 10'MBy'
    

The query produces a result of 10MBy. Next, you run a query to verify how the 10MBy is distributed across node zones:
    
    
    fetch k8s_pod :: networking.googleapis.com/pod_flow/egress_bytes_count
    | group_by [metadata.system.node_zone], 24h, sum(egress_bytes_count)
    | condition val() > 10'MBy'
    

The distribution query returns the following results:

`node_zone` | `egress_byte_count`  
---|---  
us-central1-f | 7.3MBy  
us-west1-b | 2.5MBy  
  
These results show a total of 9.8MBy rather than the expected 10MBy. This discrepancy can occur if one of the aggregated metadata labels has a null value, such as in the following dataset:

value | metadata value  
---|---  
7.3MBy | us-central1-f  
2.5MBy | us-west1-b  
0.2MBy |   
  
To avoid problems from null metadata, you can wrap your metadata reference in an `or_else` operation, which lets you specify a default value in case a metadata column has no value. For example, the following query uses `or_else` to set a metadata value of `no zone` for any metadata columns without a value:
    
    
    fetch k8s_pod :: networking.googleapis.com/pod_flow/egress_bytes_count
    | group_by [or_else(metadata.system.node_zone, 'no zone')], 24h, sum(egress_bytes_count)
    | condition val() > 10'MBy'
    

This new query produces the following results, which sum to 10MBy:

`node_zone` | `egress_byte_count`  
---|---  
us-central1-f | 7.3MBy  
us-west1-b | 2.5MBy  
no zone | 0.2MBy  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
