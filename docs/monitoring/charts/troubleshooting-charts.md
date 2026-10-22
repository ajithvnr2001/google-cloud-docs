---
url: https://docs.cloud.google.com/monitoring/charts/troubleshooting-charts/
title: Troubleshoot charts \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:42.900947+00:00
---

# Troubleshoot charts  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/charts/troubleshooting-charts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Troubleshoot charts Stay organized with collections  Save and categorize content based on your preferences. 

To resolve error messages or unexpected results on charts and dashboard widgets in Cloud Monitoring, you can adjust your queries, alignment periods, and permissions so that your telemetry renders accurately. This document helps you diagnose common issues in Metrics Explorer and custom dashboards, including data gaps, time-series display limits, mismatched Y-axis units, and widget configuration errors.

## Chart errors

This section describes errors that you might see when you configure a chart. You can configure charts by using Metrics Explorer or by adding them to a dashboard.

### Gaps in chart data

Charts occasionally exhibit gaps in the data. For example, the following screenshot illustrates this behavior for the metric [`loadbalancing.googleapis.com/https/total_latencies`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#loadbalancing/https/total_latencies):

![Example of chart with gaps in values.](https://docs.cloud.google.com/static/monitoring/images/troubleshooting-gap-in-data.png)

Gaps in the data can occur when data is written very infrequently. Cloud Monitoring collects metrics by sampling, and with very sparse data, there might not be any data available when a sample is collected. For example, gaps in load-balancer metrics might occur when the request count is 0.05 queries per second (QPS) or less. When the query rate increases, the gaps disappear.

You can remove visual gaps by increasing the alignment interval. When the system generates a new time series with regularly spaced data points, it uses the alignment interval to determine the time window over which raw data points are combined. For more information, see [Alignment: within-series regularization](https://docs.cloud.google.com/monitoring/api/v3/aggregation#alignment-intro).

To set a minimum alignment interval, edit the query of your chart. For example, when using Metrics Explorer, go to the query pane and select _add_ **Add query element**. In the menu, select **Min Interval** , and then select a time interval.

### Alignment period changes when the time range is modified

You add a chart to a dashboard. When you change the dashboard's time range or the chart's time range, sometimes the alignment period changes. For example, if you change the time range from one hour to two hours, the alignment period is listed as `1 minute interval`. However, if you change the time range from one hour to one day, then the alignment period is listed as `5 minute interval`.

This behavior is expected.

Charts are limited in the number of data points that they can display. Therefore, when the number of data points available for the selected time range is larger than the display limit, Monitoring automatically modifies the alignment settings to reduce the number of data points to display.

### Chart doesn't display all time series

You configure a chart, but it doesn't display all time series.

For performance reasons, charts are configured to display at most 50 time series.

When you configure a chart and more than 50 time series are available, then the chart limits the number of displayed time series and adds to the toolbar an icon with a red dot. The tooltip for the icon displays the following message:
    
    
    To improve performance, we've limited the time series displayed in this chart.
    

To display all time series, expand the tooltip and select the button labeled **Show All Time Series**.

### Chart doesn't display any data

You configure a chart, but the chart displays an error message instead of data:

  * When there isn't data available for the time range specified for your chart, the following message is shown:
        
        No data is available for the selected time frame.
        

To resolve the problem, try the following:

    * Increase the time range for the chart. Some metric types, such as those that report quota usage, provide only one sample per day.

    * Change the selected metric type for your chart. It is possible that the metric type specified by your chart is inactive. A metric type is inactive when there aren't any time series for the type.

  * When the metric type or resource type specified by the query isn't recognized, the following message is shown:
        
        An error occurred requested data. One or more resources could not be found.
        

To resolve this problem, try the following:

    * Verify that the metric type and resource type specified in the query are defined. You can use the menu-driven interface for charts to search for the metric type.

    * Verify the spelling of the metric type and resource type in the query.




### Chart displays a warning about sensitive metadata

You open a custom dashboard and expect all widgets to display data. However, one or more widgets that contain SQL queries display messages similar to the following:
    
    
    This SQL query is configured to run on the BigQuery engine using [PROJECT_ID],
    and references resources from [RESOURCE, ...]. Sensitive metadata,
    including table contents, may be written to [PROJECT_ID].
    

The warning message indicates that the query crosses ownership boundaries and it provides you an opportunity to verify the query before it is executed. Ownership boundaries are determined by several factors, one of which is the hierarchy of the resources the query uses.

The system performs boundary checks each time a dashboard is opened. You can't prevent or dismiss these warnings.

**Note:** If you determine that a query isn't safe to execute, then close the dashboard. You should also consider deleting the dashboard. Don't run the query.

If a widget displays the warning message, then you can do any of the following:

  * If you know the query is safe to run and if you want to view the query results, then click **Confirm and Run**.

  * Ignore the error message. This widget won't show data for your current session.

  * Analyze the query and, if necessary, disable it. For example, you might do the following:

    1. Inspect the query and evaluate what data is queried.
    2. Review the history of the dashboard to determine who added the widget and when.
    3. If you were sent a dashboard link, then verify that the sender is a trusted source.
    4. For future reference, save your analysis to the dashboard by adding a **Text** widget.



Google Cloud provides some features that can help prevent data exfiltration through phishing, insider attacks, or external entities. To learn more, see [Data security with Observability Analytics](https://docs.cloud.google.com/logging/docs/analyze/data-security-with-analytics).

### Chart with multiple metrics displays an error message

You are configuring a chart to display multiple metrics, and the chart displays the following error message:
    
    
        The units for queries using the same Y-axis must be the same for the chart
        to render correctly.
    

Charts can display multiple metric types, and you can map a metric type to either the left Y-axis or the right Y-axis. The units of all metric types mapped to the left Y-axis must be the same; otherwise, the previous error message is shown. Similarly, the units of all metric types mapped to the right Y-axis must be the same, or the previous error message is shown.

To resolve this error, do the following:

  1. If your chart contains metrics with more than two unit types, then remove metrics until you have only two unit types.

  2. Assign all metrics with one unit type to the left Y-axis and all metrics with the other unit type to the right Y-axis.




### Chart with multiple metrics displays unexpected data

A chart is configured to display multiple metrics, and filters were added to show only specific time series. However, the chart shows time series that don't satisfy the filters.

To resolve this situation, ensure that you apply filters to each metric that is charted.

For example, the following screenshot shows the configuration pane of Metrics Explorer for a chart that displays the number of bytes read and written by virtual machine (VM) instances:

![Example of Metrics Explorer with two metric types.](https://docs.cloud.google.com/static/monitoring/images/eqb-two-metrics.png)

In the screenshot, there is one heading for each metric type that is displayed by the chart.

For example, if you want the chart to display time series only for VMs that are in the `us-central1-a` zone, then add the filter `zone = us-central1-a` to each query.

### Unable to select filter values for PromQL-defined charts

You create charts on a custom dashboard and configure those charts with PromQL. You then create [permanent dashboard filters](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent). When you view the dashboard, you attempt to change the default value of the filter, but the menu of label values isn't displayed or the menu of label values isn't correct:

![Values for a dashboard-wide filter aren't loaded.](https://docs.cloud.google.com/static/monitoring/images/dashboard-filter-no-menu-values.png)

To resolve this issue, enter the filter value, and then select **Apply**. For example, if the filter key is `zone`, then you might enter `us-central1-a`.

## Dashboard errors

This section describes errors that you might see when you create or edit dashboards.

### Dashboard creation fails

You create a dashboard by using a JSON or YAML description of the dashboard, and that description includes a `name` field. You change the display name and try to create a second dashboard, but you get an error. For example, if you use the Google Cloud CLI, then you get the following error:
    
    
    ERROR: (gcloud.alpha.monitoring.dashboards.create) Resource in projects [xxxxxxx] is the subject of a conflict: Requested entity already exists.
    

The cause of the failure is that the dashboard ID, which identifies this dashboard in the value of the `name` field, already exists. Therefore, the dashboard can't be created.

If you specify the `name` field when you create a dashboard, then the value that you specify must be globally unique. The `name` field has the following syntax:
    
    
    "name": "projects/PROJECT_ID_OR_NUMBER/dashboards/DASHBOARD_ID"
    

The display name doesn't have to be unique.

### Dashboard isn't displaying all events

You configure a [dashboard to display events](https://docs.cloud.google.com/monitoring/dashboards/show-events); however, only recent events are displayed. Older events aren't shown.

To resolve this problem, do one of the following:

  * Use a shorter time range. For example, display data for the most recent hour instead of for the most recent day or select a custom time range.

  * Add filters.




For performance reasons, dashboards are limited in the number of events that they can display. When these limits are reached, the dashboards display only the most recent events.

### Terraform-created dashboard is rescaled

You created a dashboard by using Terraform and then edited the dashboard by using the Google Cloud console. You expected that the dashboard would be unchanged except for your edits. Instead, the dashboard is rescaled. For example, your dashboard had 12 columns and now has 48 columns.

Don't use the Google Cloud console to edit dashboards that were created by using Terraform. When the dashboard is edited, the size is scaled by a factor of four.

### Alerting policy widget doesn't display any data

A dashboard contains a chart for an alerting policy, but the chart doesn't display any data.

To resolve this situation, try the following:

  * View the configuration of the chart and ensure an alerting policy is selected. If no alerting policy is displayed, then associate the chart with an alerting policy or delete the chart from the dashboard.

Charts on dashboards that display data for an alerting policy stop displaying data when the referenced alerting policy is deleted. Deleting an alerting policy doesn't delete charts that reference that policy.

  * View the details of the alerting policy and verify that it contains a single condition.

Charts on dashboards that display data for an alerting policy stop displaying data if the alerting policy is modified to contain multiple conditions. To resolve this issue, associate the chart with a single-condition alerting policy or delete the chart from the dashboard.

  * Increase the time range. The time-range selector must be set to a value longer than the sampling period of the data. While most metrics are sampled every 60 seconds, some metrics are sampled infrequently. For example, the [serviceruntime.googleapis.com/quota/limit](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#serviceruntime/quota/limit) metric is sampled every 86,400 seconds (1 day).




### Logs panel reports invalid query

You see an error message "Error: Invalid query", and the logs panel doesn't show any log entries.

To resolve this issue, reduce the number of projects whose logs the logs panel is configured to display.

For more information about this failure condition, see [Query returns an error](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#invalid-query).

### Logs panel reports no entries found

You see the error message "No entries found matching current filter" in a logs panel. There are multiple reasons why you might see this message. Check the following:

  * For each project whose log entries you want to view, ensure that one of the following is true:

    * You have the [Logs Viewer](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) (`roles/logging.viewer`) role.
    * For custom roles, you have the following permissions:

      * `logging.logs.list`
      * `logging.logServiceIndexes.list`
      * `logging.logServices.list`
  * Ensure that the clauses in the query editor don't conflict with the settings shown in the logs panel.

For example, when the **Query Editor** field contains `severity=NOTICE`, the logs panel retrieves all logs that have a severity level of exactly `NOTICE`. If the logs panel **Severity** menu is set to "Warning", then the logs panel displays "No entries found matching current filter". The message is shown because none of the retrieved log entries have a severity level of at least "Warning".

In contrast, when the **Query Editor** field contains `severity=WARNING` and the logs panel **Severity** menu is set to "Notice", you might see log entries. With this configuration, the logs panel retrieves logs whose severity level is `WARNING`. Next, that list of logs is filtered to display only those whose severity is at least "Notice", and all of the retrieved logs have at least that severity level.




### Logs panel indicates it displays partial data

You see a warning indicator and the message "Showing partial results" on a logs panel.

When you don't have permission to view logs for a Google Cloud project whose logs you've selected to display, this indicator is shown. To remove the warning indicator, do one of the following:

  * Contact your system administrator and ask them to do one of the following for each Google Cloud project whose logs you want to view:

    * Grant you the role of [Logs Viewer](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) (`roles/logging.viewer`).
    * For custom roles, grant the following permissions:

      * `logging.logs.list`
      * `logging.logServiceIndexes.list`
      * `logging.logServices.list`
  * Change the configuration of the logs panel to show logs only for Google Cloud projects where you have permission to view log entries.




### Logs panel displays permission denied message

The logs panel widget on a dashboard displays the following permission-denied message:
    
    
    Error: Permission 'logging.views.access' denied on resource (or it may not exist).
    

To resolve this problem, do the following:

  1. Edit the logs panel widget.
  2. Do one of the following:

     * Set the **Scope by** menu to **Project** and then use the **Projects** menu to select **Current project**.

     * Remove from the **Storage views** menu the log views that you don't have permission to view. For information about IAM roles required to access log views, see [Grant access to a log view](https://docs.cloud.google.com/logging/docs/logs-views#add_users).

When the logs panel widget searches log views, you must have permission to read log entries in all log views that are listed. Otherwise, an error message is displayed.

  3. Click **Apply**.




### Table doesn't display all time series

You configure a table, but it doesn't display all time series.

For performance reasons, tables are configured to display at most 300 rows.

### API call to create a dashboard with a logs panel fails

There are multiple reasons why you might see an error message when you create a dashboard with a logs panel:

  * When the logs panel doesn't meet the minimum height or width requirements, the following error is shown:
        
        Unable to save dashboard: Field mosaicLayout.tiles[0] has an invalid value: LogsPanel must have a minimum width of 3 and height of 3.
        

To resolve this condition, in the dashboard JSON representation, ensure the `height` and `width` fields of the logs panel widget meet the minimum requirements.

  * When the `logsPanel.filter` field exceeds 2,000 characters, the following error is shown:
        
        Unable to save dashboard: filter cannot be greater than 2000 characters.
        

To resolve this condition, shorten the filter.

  * When the `resourceNames` field is missing, you see the following error message:
        
        Unable to save dashboard: Dashboard is missing required field mosaicLayout.tiles[0].widget.logsPanel.resourceNames.
        

To resolve this condition, add a `resourceNames` field to the dashboard JSON.

  * When the syntax for the `resourceNames` field is incorrect, you see an error similar to the following:
        
        Unable to save dashboard: Field mosaicLayout.tiles[0].widget.logsPanelWidget.resourceNames has an invalid value of "a-project": resource name must have the format `projects/{project}`.
        

To resolve this condition, replace `a-project` with `projects/a-project` in the dashboard JSON.

  * For information about how to resolve syntax errors in the `filter` field, see [Troubleshooting: syntax issues](https://docs.cloud.google.com/logging/docs/view/advanced-queries#troubleshooting).




For an example of a correctly formatted JSON file, see [Dashboard with a `LogsPanel` widget](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_logs_panel).

## Importing Grafana dashboards

For information about using and troubleshooting the dashboard importer, see [Import Grafana dashboards into Cloud Monitoring](https://docs.cloud.google.com/monitoring/dashboards/import-grafana-dashboards).

For information about problems with the conversion of the dashboard contents, see the importer's [`README`](https://github.com/GoogleCloudPlatform/monitoring-dashboard-samples/tree/master/scripts/dashboard-importer/README.md#troubleshooting) file.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
