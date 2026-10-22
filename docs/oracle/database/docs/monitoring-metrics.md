---
url: https://docs.cloud.google.com/oracle/database/docs/monitoring-metrics/
title: Monitor resources using Cloud Monitoring \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:44.305667+00:00
---

# Monitor resources using Cloud Monitoring  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/monitoring-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Monitor resources using Cloud Monitoring Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view and use the monitoring metrics available for your Oracle Database@Google Cloud resources using Cloud Monitoring.

You can use Cloud Monitoring to monitor your Oracle Database@Google Cloud resources using _custom dashboards_ , and _metrics charts and alerts_.

## Monitor using Cloud Monitoring dashboards

Cloud Monitoring lets you monitor your Oracle Database@Google Cloud resources using custom dashboards. You can create custom dashboards using Cloud Monitoring and the available Oracle Database@Google Cloud metrics and logs.

For more information on how to create a custom dashboard, see [Create a new dashboard](https://docs.cloud.google.com/monitoring/charts/dashboards#create_a_new_dashboard).

## Monitor using Cloud Monitoring metrics

You can use the Metrics explorer in Cloud Monitoring to _view metrics_ , _create charts_ , or _set up alerts_ for your Oracle Database@Google Cloud resources.

### View metrics

You can view available Oracle Database@Google Cloud metrics using Cloud Monitoring in the Google Cloud console.

To view an available metric:

  1. Go to the Cloud Monitoring metrics explorer page in the Google Cloud console.

[Go to Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer/)

  2. In the **Queries** section, click **Select a metric** , and choose one of the following resource names to view metrics for that resource: **Exadata Infrastructure** , **Cloud VM Cluster** , **Autonomous Database** , **Container Database** , or **Pluggable Database**.

Click **Apply**. The metric is displayed. You can view your metric as a _chart_ , _table_ , or _both_ by selecting the option in the results pane.




### Create custom charts for metrics

You can create custom charts for Oracle Database@Google Cloud metrics using Cloud Monitoring. You can use two or more metrics to view and understand the correlation between the metrics. For example, you can use the _CPU utilization_ and _latency_ metrics to create a chart that might indicate that your instance needs more capacity, or if your instance or cluster is experiencing high utilization.

To create a custom chart:

  1. Go to Cloud Monitoring Metrics explorer page in Google Cloud console.

[Go to Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer/)

  2. In the **Queries** section, add the metrics to your chart:

     1. Click **Select a metric** to open the drop-down, select the first metric, then press **Apply** to add it to the chart.

For each additional metric, click **Add query** to add a new metric line and select the metrics.

     2. _Optional_ \- You can modify the following for each metric:

        * _Filter_ : click **Add Filter** next to your metric name to filter your metric values.
        * _Aggregation_ : click **Aggregation** next to your metric name to apply an aggregation, such as sum, min, max ..., to your metric values.

Click `+` to view and select additional options available to modify your metric values.

  3. In the **Display** pane, modify the following as necessary:

     * **Widget type** : select the type of chart you want to use to display your metrics.
     * **Analysis mode** : select _standard_ , _x-ray_ , or _stats_ mode for your analysis type.
     * **Compare to past** : check the box to **enable compare to past++ then select the **timeshift duration**.
     * **Threshold line** : click **Add threshold** to add a threshold line to your chart, then input the **Threshold** percentage and select the **Y-axis** line. You can add multiple threshold lines to your chart.
     * **Y-axis assignment** : select the y-axis alignment for each of the metrics in your chart by using the drop-down in the **Y-axis** column.
     * **Y-axis labels** : add labels for the left and right Y-axis of your chart. These labels will be displayed to identify the axises in the chart.
     * **Legend alias** : customize the description of the time series legend in your chart using this option.
  4. Click **Save Chart** and in the dialog, add a name for your chart in the **Chart title** field, and add your chart to an existing or new dashboard.

Click **Save chart** in the dialog to confirm.




### Create metric alerts

You can use Cloud Monitoring to create alerts for available Oracle Database@Google Cloud metrics.

You can create metric alerts for the following:

  * [Metric-threshold alerting policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui): creates an altering policy that sends notifications when the values of a metric are more than, or less than, the specific threshold.
  * [Metric-absence alerting policy](https://docs.cloud.google.com/monitoring/alerts/metric-absence): creates an alerting policy that sends notifications when a monitored metric has no data for a specific period of time.



## What's next

  * Learn more about [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).
  * [View audit logs](https://docs.cloud.google.com/oracle/database/docs/view-audit-logs).
  * [View resource logs](https://docs.cloud.google.com/oracle/database/docs/view-resource-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
