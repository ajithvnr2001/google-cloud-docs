---
url: https://docs.cloud.google.com/monitoring/charts/working-with-legends/
title: Configure legends \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:59.691143+00:00
---

# Configure legends  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/charts/working-with-legends/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Configure legends Stay organized with collections  Save and categorize content based on your preferences. 

Chart legends in Cloud Monitoring let you inspect metric values at a selected point in time, view resource and metric labels in configurable columns, and sort time series. From an expanded legend on a custom dashboard, you can also apply temporary filters or open resource-specific dashboards.

## Show and hide legends

By default, the legend on a dashboard is configured to show only the colored dots that correspond to lines in the graph. The following screenshot shows a chart on a dashboard with the default legend:

![Default legend of a chart on a dashboard.](https://docs.cloud.google.com/static/monitoring/images/legends-dashboard-chart-faded.png)

For charts on dashboards, you can also expand the legend to view more details, such as configurable data columns and a **Value** column. The **Value** column displays the values for the metric being charted, and other columns display the values of chosen metric or resource labels. The dashed bar on the chart indicates the time for which values are displayed.

###  Charts on dashboards 

You can show or hide the legends of all charts on a dashboard or of each chart individually:

  * To show or hide the legends of every chart in a dashboard, in the dashboard toolbar, click _settings_ **Settings** and then select **Condensed** or **Table**.
  * To show or hide the legend of a particular chart, click _unfold_more_ **Expand legend** , or select **Expand chart legend** in the _more_vert_ **More chart options** menu.



###  Metrics Explorer 

  * To show a chart's full legend, in the toggle labeled **Chart Table Both** , select **Both**.
  * To hide a chart's full legend, in the toggle labeled **Chart Table Both** , select **Chart**.



Legends for charts that display multiple metric types might be difficult to interpret. By default, the legend columns are selected from the metric and resource labels for the charted metric type. When a chart has multiple metric types, the result is that a specific legend column might not be meaningful for a specific time series.

  * Example: A chart displays the number of bytes written to and the number of bytes read from virtual machine (VM) instances. Assume that the bytes-read data is filtered to the `us-central1-a` zone. The legend includes a `zone` column, and the values in that column might be different from `us-central1-a`. The reason is that the bytes-written metric type contains a `zone` label and that metric data wasn't filtered by zone.

  * Example: A chart displays the number of bytes written to VM instances and the CPU usage for those instances. The legend contains columns for the disk type and storage type. However, the values for those labels are empty for the CPU usage time series. The reason is that the CPU usage metric type doesn't support those labels.




## Select legend columns

To change the columns that appear in the legend, expand the legend, and then click _view_column_ **Legend columns**. Clicking the button brings up a configuration panel. This panel lists the metric and resource labels available to display as columns. Required columns have disabled checkboxes. The following screenshot shows the **Columns** button and the configuration panel for a particular legend:

![Legend showing Columns button](https://docs.cloud.google.com/static/monitoring/images/legends-icon-menu.png)

When the chart is initially created, the system heuristically chooses a set of labels to show by default. You can select or clear labeled columns. The entries for required columns, most typically **Value** , are disabled and can't be cleared. When you change the configuration, you must have at least one metric or resource label selected.

The legend displays a scrollbar when it has many columns to display and paginates the rows when there are many time series to display. The following screenshot illustrates a legend with a scrollbar, and arrows for navigating through the pages:

![Legend showing scrollbar and arrows to change pages](https://docs.cloud.google.com/static/monitoring/images/legends-scrollbars.png)

## Sort legend rows

You can sort the rows of the legend by any of the columns. Rows can be sorted into ascending or descending order. To sort a row, click the header. The most recently sorted column displays an arrow indicating the sort order. The following screenshot shows a legend that has been sorted by **zone** in descending order:

![Legend sorted on zone](https://docs.cloud.google.com/static/monitoring/images/legends-sorted-zone.png)

## Understand legends in "Compare to Past" mode

When you use [**Compare to Past** mode](https://docs.cloud.google.com/monitoring/charts/working-with-charts#comparetopast-option) on a chart, the legend is modified to include a second “values” column. The current **Value** column becomes **Today** , and the past values column is named appropriately—for example, **Last Week**. The following screenshot shows a legend for a table comparing current data to that of the last hour:

![Legend showing past data](https://docs.cloud.google.com/static/monitoring/images/legends-compare-mode.png)

## Configure the name of a legend column

The **Legend Alias** field lets you customize a description for the time series on your chart. These descriptions appear on the tooltip for the chart and on the chart legend in the **Name** column. By default, the descriptions in the legend are created for you from the values of different labels in your time series. Because the system selects the labels, the results might not be helpful to you. To build a template for descriptions, use this field.

You can enter plain text and templates in the **Legend Alias** field. When you add a template, you add an expression that is evaluated when the legend is displayed.

To add a legend template to a chart, do the following:

  1. In the **Display** pane, expand _expand_more_ **Legend Alias**.
  2. Click _add_ **Display template variable suggestions** and select an entry from the menu. For example, if you select `zone`, then the template `${resource.labels.zone}` is added.



For example, the following screenshot shows a legend template that contains plain text and the expression `${resource.labels.zone}`:

![A template for a simple description.](https://docs.cloud.google.com/static/monitoring/images/metricpicker-template-field.png)

In the chart legend, the values generated from the template appear in a column with the header **Name** and in the tooltip:

![Descriptions generated from a template.](https://docs.cloud.google.com/static/monitoring/images/metricpicker-custom-descs.png)

You can configure the legend template to include multiple text strings and templates; however, the display space available on the tooltip is limited.

## Access resource-specific dashboards

This feature is available when you are viewing charts on dashboards. It isn't available when you use Metrics Explorer.

When you are viewing a time series, you might want to view more information about the resource against which that time series is written. For some resources, you can go to the management page for that resource by using options in a chart's legend.

To go to the management page for a resource, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select a dashboard and then go to the chart or table that is displaying the time series of interest.
  4. If you are viewing a table, then scroll through the table until you find the row of interest. Next, go to the column that displays the numeric value, click _more_vert_**Actions for this timeseries** , and then select **Manage**.
  5. If you are viewing a chart, then do the following:

     1. On the chart, click _unfold_more_ **Expand legend**.
     2. Scroll through the legend until you find the specific time series of interest, click _more_vert_**Actions for this timeseries** , and then select **Manage**.



The following is a partial list of resources whose management page you can access from the legend options:

  * BigQuery datasets
  * Cloud Storage buckets
  * Compute Engine disks and instances
  * Google Kubernetes Engine clusters, containers, nodes, and pods
  * External Application Load Balancers
  * Pub/Sub subscriptions and topics
  * Spanner instances



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
