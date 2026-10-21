---
url: https://docs.cloud.google.com/dataflow/docs/guides/project-monitoring/
title: Dataflow project monitoring dashboard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:47.570706+00:00
---

# Dataflow project monitoring dashboard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/project-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Dataflow project monitoring dashboard Stay organized with collections  Save and categorize content based on your preferences. 

The Dataflow web-based monitoring interface includes a dashboard that monitors your Dataflow jobs at the project level. The charts show data for all of the jobs in one project.

[Go to dashboard](https://console.cloud.google.com/dataflow/monitoring)

The dashboard can help you with the following tasks:

  * Detect and identify the source of quota errors.
  * Detect anomalous horizontal autoscaling in a job.
  * Identify slow or stuck streaming jobs.



The dashboard uses [Cloud Monitoring](https://docs.cloud.google.com/dataflow/docs/guides/using-cloud-monitoring) to access Dataflow job metrics. To customize the information displayed in the charts, use [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-selector).

## Features

The dashboard includes the following features:

  * Choose which jobs appear in the dashboard by using regular expressions.
  * Access the job details page from individual charts.
  * Customize the dashboard widgets and charts.



## Required roles

To get the permission that you need to see the graph data, ask your administrator to grant you the [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) IAM role. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `monitoring.timeSeries.list` permission, which is required to see the graph data. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Access the dashboard

To access the dashboard, follow these steps:

  1. [Sign in](https://console.cloud.google.com/) to the Google Cloud console.
  2. Select your Google Cloud project.
  3. Open the navigation menu.
  4. In **Analytics** , click **Dataflow**.
  5. In the Dataflow navigation menu, click **Monitoring**.

[Go to dashboard](https://console.cloud.google.com/dataflow/monitoring)




## Dashboard metrics

By default, the following time-series charts appear in the dashboard. For more information about the metrics displayed, see [Job metrics](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf).

The following charts apply to batch and streaming jobs:

  * **Running jobs**. Shows the number of active jobs running in the project. This chart indicates the overall Dataflow activity in the project over time.
  * **Workers per job (top 25)**. Shows the current worker counts for the 25 most parallelized jobs. This chart is useful for understanding resource allocation and identifying high-workload jobs. You can also see if jobs have unexpected scaling behavior.
  * **Total count of vCPUs**. Shows the total number of virtual CPUs (vCPUs) in use across all jobs in the project. The total number of vCPUs affects Compute Engine quotas.
  * **vCPUs per job (top 25)**. Show the 25 jobs that consume the most vCPU resources. This chart highlights potentially expensive jobs.
  * **Total count of vCPUs**. Shows a project-wide aggregate of vCPUs in use. This chart gives a high-level view of the Compute Engine resources that your jobs consume.
  * **Quota exceeded errors**. Reports any instances where [Dataflow quotas](https://docs.cloud.google.com/dataflow/quotas) or [Compute Engine quotas](https://docs.cloud.google.com/compute/quotas-limits) have been reached. This chart can help you to find potential job failures or scaling slowdowns.



The following charts apply to streaming jobs:

  * **Average system latency**. Shows the average [system latency](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf#system_latency_streaming), which reflects the typical delay experienced by data as it passes through source stages. This chart can indicate potential input bottlenecks. Use this chart to identify streaming jobs that have an unusual delay between when data appears in a source and when the data is written to all sinks.
  * **System lag (top 25)**. Shows the 25 streaming pipelines with the highest system lag, which is the longest amount of time that data spends being processed or awaiting processing. This chart can indicate potential real-time processing bottlenecks.
  * **Data watermark lag per stage (top 25)**. Shows the 25 streaming jobs with the largest watermark lag. The _watermark lag_ for a stage is the difference between the latest event time received by the stage and the watermark. This chart can indicate potential bottlenecks at per-stage granularity. Use this chart to find streaming jobs that might be slow or stuck. For more information, see [Troubleshoot slow or stuck streaming-jobs](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-slow-streaming-jobs).
  * **SECU usage (top 25)**. Shows the 25 streaming jobs that consume the most [Streaming Engine Compute Units](https://cloud.google.com/dataflow/pricing#streaming-compute-units). Use this chart to measure the cost and intensity of your streaming jobs that use [resource-based billing](https://docs.cloud.google.com/dataflow/docs/streaming-engine#compute-unit-pricing).
  * **User processing latencies (top 25)**. Shows the 25 streaming jobs where user-defined code in processing stages takes the longest. Use this chart to find potential performance bottlenecks in your application logic.
  * **Max backlog bytes (top 25)**. Shows the 25 streaming jobs with the largest volume of unprocessed data waiting at any stage. This chart can indicate potential input overload or slow processing.
  * **Backlogged keys (top 25)**. Shows backlogged streaming jobs by the largest number of backlogged keys in a bottleneck stage. For more information, see [Troubleshoot bottlenecks](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-bottlenecks).
  * **Bottleneck likely causes (top 10)**. Shows the top 10 likely causes of bottlenecked stages in backlogged jobs. For more information, see [Troubleshoot bottlenecks](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-bottlenecks).



For more information about working with charts, see [Explore charted data](https://docs.cloud.google.com/monitoring/charts/working-with-charts).

## Customize the dashboard

You can customize the dashboard contents and the information displayed in the charts. When you edit the dashboard, a new, customized dashboard is created.

The dashboard uses Cloud Monitoring to access Dataflow job metrics. Use the Cloud Monitoring tools to customize the charts.

  1. Open the dashboard and click **Customize Dashboard**.
  2. Modify your dashboard. 
     * To filter the jobs that display on the dashboard, see [Add temporary filters to a custom dashboard](https://docs.cloud.google.com/monitoring/charts/filter-dashboard) and [Add permanent filters to a custom dashboard](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent).
     * To edit or remove widgets, see [Manage dashboard widgets](https://docs.cloud.google.com/monitoring/charts/manage-widgets).
     * To edit the contents of the charts, see [Select metrics for charts on dashboards](https://docs.cloud.google.com/monitoring/charts/metrics-selector).
     * To add charts to the dashboard, see [Add charts and tables to a custom dashboard](https://docs.cloud.google.com/monitoring/charts).
  3. Click **Save** , and then click **View customized dashboard**.



After you create a customized dashboard, to return to the default dashboard, in the **Dashboard** menu, select **Predefined**.

For an example of adding a custom metrics chart to the dashboard, see [Customize the Dataflow monitoring dashboard](https://docs.cloud.google.com/dataflow/docs/guides/customize-monitoring-dashboard).

## Troubleshooting

This section provides instructions for troubleshooting common issues

### No data is available

When you open your dashboard, one or more charts shows the following message:
    
    
    No data is available for the selected time frame.
    

This message appears when the time period covered in the charts doesn't have any data. To resolve this issue, change or expand the time range.

To change the displayed time range, on the chart, click **Explore data** , and then use the time-range selector.

### Unable to restore deleted widgets

When you remove a widget from the dashboard, you create a customized dashboard. After you create a customized dashboard, to return to the default dashboard, in the **Dashboard** menu, select **Predefined**.

### Unable to view charts

To see the graph data, you need the `monitoring.timeSeries.list` permission. For more information, see Required roles.

## What's next

  * Learn more about individual [job metrics](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf).
  * Explore metrics with [Cloud Monitoring](https://docs.cloud.google.com/dataflow/docs/guides/using-cloud-monitoring).
  * Learn how to [troubleshoot Dataflow pipelines](https://docs.cloud.google.com/dataflow/docs/guides/troubleshooting-your-pipeline).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
