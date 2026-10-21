---
url: https://docs.cloud.google.com/monitoring/mql/troubleshooting/
title: Troubleshoot MQL alerting policies \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:18:39.709196+00:00
---

# Troubleshoot MQL alerting policies  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/mql/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Troubleshoot MQL alerting policies Stay organized with collections  Save and categorize content based on your preferences. 

**Announcement:** On July 22, 2025, Google Cloud customer support for MQL ended, and MQL is no longer available in the Google Cloud console when you create charts, dashboards, and alerting policies. Existing MQL charts, dashboards, and alerting policies continue to work, and you can still create them by using the Cloud Monitoring API. For more information, see the [deprecation notice for MQL](https://docs.cloud.google.com/stackdriver/docs/deprecations/mql). 

This page explains why some alerting policies with Monitoring Query Language (MQL)-based conditions might behave differently than intended, and offers possible remedies for those situations.

## Data gaps

You created an alerting policy with an MQL-based condition, and the MQL query results show an unexpected gap in the reported data.

Gaps appear in aligned data when a calculation results in a null value at a given timestamp. For example, the following data table is related to a query with a 30 second period:

**Table A1**

Timestamp | Value  
---|---  
00:00:00 | 1  
00:00:30 | 2  
00:01:30 | 3  
00:02:00 | 4  
  
Since you have a 30-second period, you would expect to see a timestamp at 00:01:00. Gaps like this can occur for many reasons.

### Gaps due to alignment

Overly-narrow aligner windows can cause data gaps. For example, the following table of unaligned raw metric data is written approximately every 30 seconds.

**Table B1**

Timestamp | Value  
---|---  
00:00:01 | 1  
00:00:28 | 2  
00:01:01 | 3  
00:01:32 | 4  
  
If you run a query at 00:02:00 that aligns your data using a `next_older(30s)` operation, then you receive the following output, which has a data gap at 00:01:00:

**Table B2**

Timestamp | Value  
---|---  
00:00:30 | 2  
00:00:28 | 3  
00:01:01 | 4  
  
This data gap occurs because no point in the raw data falls in the 30-second window that ends at 00:01:00. To avoid a gap like this, use a larger window. For example, a `next_older(1m)` operation produces a table without data gaps:

**Table B3**

Timestamp | Value  
---|---  
00:00:01 | 1  
00:00:28 | 2  
00:01:01 | 3  
00:01:32 | 4  
  
In general, if your data is written every S seconds, then use an alignment window that is larger than S. This way, you can account for uneven distribution of data points over time.

### Gaps due to table operations

Some table operations can produce unexpected gaps. For example, the `join` operation produces output only at timestamps that have a value in all of the input tables.

Table operations such as `join` can produce gaps. For example, you join the following two aligned tables:

**Table C1**

Timestamp | Value  
---|---  
00:00:30 | 2  
00:01:30 | 3  
00:02:00 | 4  
  
**Table C2**

Timestamp | Value  
---|---  
00:00:30 | 4  
00:01:00 | 3  
00:01:30 | 2  
00:02:00 | 1  
  
You then receive the following output:

**Table C3**

Timestamp | Value A | Value B  
---|---|---  
00:00:30 | 1 | 4  
00:01:30 | 2 | 2  
00:02:00 | 3 | 1  
  
This table has no value at `00:01:00` due to the absence of a value at `00:01:00` in Table C1.

### Gaps due to missing values

Some functions produce gaps when their output can't be converted or is undefined. For example, you apply `value.string_to_int64` to the following table of string values:

**Table D1**

Timestamp | Value  
---|---  
00:00:30 | '4'  
00:01:00 | '3'  
00:01:30 | 'init'  
00:02:00 | '1'  
  
Your resulting table contains a gap at 00:01:30 because MQL can't convert `'init'` to an integer:

**Table D2**

Timestamp | Value  
---|---  
00:00:30 | 4  
00:01:00 | 3  
00:01:30 | null  
00:02:00 | 1  
  
To avoid gaps in data due to bad or missing values, use the [`has_value`](https://docs.cloud.google.com/monitoring/mql/reference#has_value-func) or [`or_else`](https://docs.cloud.google.com/monitoring/mql/reference#or_else-func) functions to handle those values.

`has_value` returns `false` if its argument evaluates to null. Otherwise, it returns `true`. For example, if you apply `value has_value(1 / val())` to Table D2, then your results don't have gaps:

**Table D3**

Timestamp | Value  
---|---  
00:00:30 | true  
00:01:00 | true  
00:01:30 | false  
00:02:00 | true  
  
## Threshold alert fires when MQL chart shows threshold hasn't been crossed

**Note:** The examples in this section use `delta_gauge` instead of `delta` due to `delta` causing alerts to trigger at incorrect times when used an alerting policy query. For more information, see [Recommended operations for MQL alerting policy queries](https://docs.cloud.google.com/monitoring/mql/best-practices-alerts#recommended-operations).

You want to be notified if a virtual machine (VM) has large fluctuations in its CPU utilization, so you create an alerting policy that monitors the metric `compute.googleapis.com/instance/cpu/utilization`. You create and configure the condition to generate an alert when CPU utilization every six hours is greater than a threshold of 50%. Your condition uses the following query:
    
    
    fetch gce_instance
    | metric 'compute.googleapis.com/instance/cpu/utilization'
    | group_by 5m, [value_utilization_mean: mean(value.utilization)]
    | align delta_gauge(6h)
    | condition val() > 0.5
    

You receive an alert after 30 seconds. However, your MQL chart shows that the utilization delta hasn't become greater than the threshold.

Alerting policies have a 30-second output window. This period can't be overwritten by leaving the period undefined or defining a different period in your query. For example, the following queries still use a 30-second output window:
    
    
    fetch gce_instance
    | metric 'compute.googleapis.com/instance/cpu/utilization'
    | group_by 5m, [value_utilization_mean: mean(value.utilization)]
    | align delta_gauge(6h) # period not 30 seconds
    | condition val() > 0.5
    
    
    
    fetch gce_instance
    | metric 'compute.googleapis.com/instance/cpu/utilization'
    | group_by 5m, [value_utilization_mean: mean(value.utilization)]
    | align delta_gauge() # undefined period
    | condition val() > 0.5
    

Your metric threshold was crossed in the first 30 seconds of evaluation, so Cloud Monitoring sent an alert. To avoid this problem, add `| every 30s` to the end of your query to verify that your output window produces the intended results. For example:
    
    
    fetch gce_instance
    | metric 'compute.googleapis.com/instance/cpu/utilization'
    | group_by 5m, [value_utilization_mean: mean(value.utilization)]
    | align delta_gauge()
    | every 30s # explicit 30 second output window
    | condition val() > 0.5
    

## Error: Unable to save alerting policy. Request contains an invalid argument.

You created an alerting policy with an MQL-based condition. When you save the alerting policy, you receive the following error message:

` Error: Unable to save alerting policy. Request contains an invalid argument. `

Some MQL table operations, such as `group_by`, require their inputs to be aligned. If your query doesn't align its inputs, then MQL automatically aligns the data. However, this automatic alignment sometimes results in invalid arguments.

To avoid this problem, if your query uses a table operation, then ensure that your query includes data alignment. For a list of data alignment functions, see the [aligning](https://docs.cloud.google.com/monitoring/mql/reference#aligner-group) section in the MQL reference documentation.

**Note:** Unaligned queries run correctly in the Metrics Explorer. However, they may cause errors when included in the MQL condition of an alerting policy.

## Threshold line doesn't appear on MQL chart

You created a metric-threshold alerting policy with an MQL-based condition. However, the threshold line doesn't appear on the MQL chart.

Cloud Monitoring draws the threshold line only when your query contains a boolean expression that compares two values, where one value is a column and one value is a literal. For example, the following expression charts a threshold line:
    
    
    val() > 5'GBy'
    

However, the following expressions don't chart a threshold line:
    
    
    val(0) > val(1) #one of the values must be a literal
    
    
    
    5 > 4 #one of the values must be a column
    
    
    
    val() #the expression must be a comparison
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
