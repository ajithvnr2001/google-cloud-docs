---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/monitoring/
title: Monitor your usage of Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:34.861997+00:00
---

# Monitor your usage of Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/monitoring/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Monitor your usage of Sensitive Data Protection Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Cloud Monitoring to view and graph metrics data about your Sensitive Data Protection usage.

Sensitive Data Protection sends detailed telemetry about your Sensitive Data Protection usage to Monitoring. This can be useful to monitor for unexpected findings, amount of data scanned or transformed, errors in [job triggers or jobs](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-job-triggers), and [expenses](https://cloud.google.com/sensitive-data-protection/pricing).

## View Sensitive Data Protection metrics in Monitoring

Using [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) in Cloud Monitoring, you can dig into available metrics data to give you insight into your Sensitive Data Protection usage. Monitoring supports a wide variety of metrics, which you can combine with filters and aggregations for new and insightful views.

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the **Metric** element, expand the **Select a metric** menu, and then select a resource type and metric type. For example, to chart the CPU utilization of a virtual machine, do the following: 
     1. (Optional) To reduce the menu's options, enter part of the metric name in the **Filter bar**. For this example, enter `utilization`.
     2. In the **Active resources** menu, select **VM instance**.
     3. In the **Active metric categories** menu, select **Instance**.
     4. In the **Active metrics** menu, select **CPU utilization** and then click **Apply**.
  3. To filter which time series are displayed, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  4. To combine time series, use the menus on the [**Aggregation** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#select_display). For example, to display the CPU utilization for your VMs, based on their zone, set the first menu to **Mean** and the second menu to **zone**.

All time series are displayed when the first menu of the **Aggregation** element is set to **Unaggregated**. The default settings for the **Aggregation** element are determined by the metric type you selected.




To see Sensitive Data Protection-specific metrics in Metrics Explorer, search with `dlp.googleapis.com` to refine your search results.

To see API metrics in Metrics Explorer, select **Consumed API** as the resource type, and then use the filter and aggregation options to refine your data.

After you've found the metrics you want, you can use Monitoring to create custom dashboards and alerts that will help you continue to monitor and maintain a robust application.

## Graph the metrics

You can graph metrics by aggregating them using Advanced Aggregation. Use the following settings:

  * Aligner: SUM
  * Alignment Period: 1440

[ ![Cloud Monitoring metric configuration.](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/stackdriver-metric.png)](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/stackdriver-metric.png) Cloud Monitoring metric configuration (click to enlarge).

You get a chart showing the results per day.

[ ![Cloud Monitoring metric configuration.](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/stackdriver-chart.png)](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/stackdriver-chart.png) Cloud Monitoring metric configuration (click to enlarge).

Cloud Monitoring supports alerting on all metrics. Using the Sensitive Data Protection metrics, you can alert on use cases that include:

  * Monitor `content_bytes_inspected_count` or `content_bytes_transformed_count` to alert when spend has exceeded budget for a day.
  * Alert when the number of total findings or findings for a specific infoType exceed a threshold. For example, you can build an alert if `CREDIT_CARD_NUMBER` findings exceed 0 in a given project where no PII should exist.



## Available metrics

The following metric type names must be prefixed with `dlp.googleapis.com/`. That prefix has been omitted from the entries in the table.

Metric type  
Display name  
---  
Kind, Type, Unit  
Launch stage | _Description_  
Labels  
`finding_count`  
Number of findings   
`DELTA`, `INT64`, `By` |  _Number of findings per second. Only populated for jobs where the action`PublishToStackdriver` is included._  
`content_bytes_inspected_count`  
Content bytes inspected   
`DELTA`, `INT64`, `By` |  _Number of bytes inspected in content methods per second._  
`content_bytes_transformed_count`  
Content bytes transformed   
`DELTA`, `INT64`, `By` |  _Number of bytes transformed in content methods per second._  
`storage_bytes_inspected_count`  
Storage bytes inspected   
`DELTA`, `INT64`, `By` |  _Number of bytes inspected in Sensitive Data Protection jobs._  
`storage_bytes_transformed_count`  
Storage bytes transformed   
`DELTA`, `INT64`, `By` |  _Number of bytes transformed in Sensitive Data Protection jobs._  
`job_result_count`  
Job results   
`DELTA`, `INT64`, `1` |  _Results of Sensitive Data Protection jobs. True if the job was success and false otherwise._  
`job_trigger_run_count`  
Job trigger runs   
`DELTA`, `INT64`, `1` |  _Results of job trigger runs._  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
