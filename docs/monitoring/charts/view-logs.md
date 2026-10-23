---
url: https://docs.cloud.google.com/monitoring/charts/view-logs/
title: Display logs and errors on a custom dashboard \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:18.608087+00:00
---

# Display logs and errors on a custom dashboard  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/charts/view-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Display logs and errors on a custom dashboard Stay organized with collections  Save and categorize content based on your preferences. 

Adding log and error widgets to a custom dashboard in Cloud Monitoring lets you correlate log entries and application errors with your performance metrics. You can use the logs panel widget to inspect individual log entries, the error-reporting panel widget to track recent [error groups](https://docs.cloud.google.com/error-reporting/docs/grouping-errors), and a Observability Analytics chart widget to visualize trends from SQL queries.

## Logs Explorer and the logs panel widget

The [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) is the standard way to investigate logs. Adding a logs panel widget to a dashboard won't change how you use the Logs Explorer. Because logs panel widgets can be added to custom dashboards, they provide a way to view your log entries in the same context as your metrics.

The Logs Explorer and the logs panel widget support the same [query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language), and they both display only those log entries that you have permission to view. Your Identity and Access Management (IAM) roles on the resources that store the log entries determine whether you can view the stored log entries.

The Logs Explorer and the logs panel widget are both preconfigured to search the resources listed in the default [log scope](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage) for log entries. If that scope isn't accessible, then they search for the log entries that originate in your selected project. When a project is selected, the search results include the log entries that are routed to the project by a sink in another project and then stored in a log bucket. You can configure which resources are searched for log entries. For example, you can search for log entries by [log view](https://docs.cloud.google.com/logging/docs/logs-views).

Logs panel widgets display one log entry per row, with columns for severity, the timestamp, and a summary of the log entry. To view the JSON-formatted representation of a log entry, click the **View log details** button. The structure of each entry summary varies based on the log type. For example, the following picture shows two log entries:

![A picture of two log entries in the logs panel widget.](https://docs.cloud.google.com/static/monitoring/images/dash-logs-panel-example.png)

In the previous picture, the first log entry displays information about a service request. The summary shows information about the service, an email address, and a string-formatted version of the JSON structure for the entry. The second entry displays the results of a request, and shows only a sentence summarizing the action that occurred.

For general information about Cloud Logging, see the following resources:

  * [Basic concepts](https://docs.cloud.google.com/logging/docs/overview)
  * [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language)
  * [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface)



## Before you begin

To get the permissions that you need to add a logs panel widget to a custom dashboard by using the Google Cloud console, and configure it to display log entries in projects or in log views, ask your administrator to grant you the following IAM roles: 

  * [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) on on your project.
  * [Logging Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on on each project whose log entries you want to view. This role doesn't grant you access to every log entry. For more information about the roles, see [Cloud Logging Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles).
  * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`) on on each project that stores the log bucket for a log view that you want to access. The Logs View Accessor role grants access to all log views stored by the project. For information about how to get access to specific log views, see [Control access to a log view](https://docs.cloud.google.com/logging/docs/logs-views#about-iam-policies).



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** The logs panel widget queries the projects and log views listed in the default [log scope](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage) and displays only the log entries that you have permission to view. To ensure that the widget can display all available entries, you might need the Logs Viewer role on multiple projects and the Logs View Accessor role on multiple log views.

## Display log entries on a dashboard

This section describes how to add and configure a logs panel widget by using the Google Cloud console. For information about using the Cloud Monitoring API, see [Dashboard with a `LogsPanel` widget](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_logs_panel).

You can put up to 100 widgets on a dashboard.

To add a logs panel widget to the dashboard by using the console, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select a dashboard or click **Create dashboard**.
  4. In the toolbar, click _add_ **Add widget**.
  5. In the **Add widget** dialog, select ![](https://docs.cloud.google.com/static/monitoring/images/logs_button.png) **Logs**.
  6. Optional: To update the title, enter the new title in the **Widget title** field.
  7. Configure which resources are searched for log entries:

     * To search by project, set the **Scope by** entry to **Project** , and then expand the **Projects** entry and complete the dialog.

**Note:** You must expand the **Projects** menu and select at least one project. No projects are automatically selected.

The **Projects** menu lists all Google Cloud projects in the current metrics scope. If an entry in the menu includes the text "You don't have project-level permission to view logs in this project", then you don't have the permissions required to view the log entries available in that Google Cloud project.

The displayed log entries include those that originate in your Google Cloud project and those that are routed to your Google Cloud project by a sink in another project.

     * To search for log entries by [log views](https://docs.cloud.google.com/logging/docs/logs-views) on log buckets, set the **Scope by** entry to **Storage** , and then expand the **Storage views** entry and complete the dialog.

**Note:** You must expand the **Storage views** menu and select at least one log view. No log views are automatically selected.

The **Storage views** menu lists log views on log buckets in your selected Google Cloud project.

To select log views on log buckets in other Google Cloud projects, in the menu, click _add_circle_ **Import project** , select a project, and then select one or more log views. You can only import projects that are included in the current metrics scope.

**Note:** When the current user doesn't have permission to access all log views that a logs panel widget searches for log entries, the widget displays an error. For more information, see [Logs panel displays permission denied message](https://docs.cloud.google.com/monitoring/charts/troubleshooting-charts#trouble-permission-denied).
     * To search the resources included in a [log scope](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage), which can include projects and log views, set the **Scope by** entry to **Logs Scope** , and then expand the **Log Scopes** entry and select a log scope.

  8. Optional: To restrict which logs the logs panel widget displays, enter a query in the **Query Editor** field, and if you've disabled queries from being automatically run, then click **Run query**. For a brief introduction to queries, see Query examples.

A query can have at most 2,000 characters.

  9. Optional: Update the widget's query or configuration to depend on variables. When you change the value of the variable, the widget is also updated. For syntax and other information, see Add variables to your query.

  10. To apply your changes to the dashboard, in the toolbar, click **Apply**. To discard your changes, click **Cancel**.

  11. To save your modified dashboard, in the toolbar, click **Save**.

The logs panel widget displays a table of log entries. You can also use the widget's filter bar to temporarily change the log entries that the widget displays. For more information, see the section titled Filter the log entries.




### Query examples

To populate the **Query Editor** field, you can enter text into the field or you can make selections from menus. The **Query Editor** field uses the same [query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language) as [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface). For troubleshooting information, see [Syntax issues](https://docs.cloud.google.com/logging/docs/view/advanced-queries#troubleshooting).

The **Severity** and **Log name** menus let you select multiple options. The following is an example of a query statement that matches multiple severity levels:
    
    
    severity=(WARNING OR ERROR OR CRITICAL OR ALERT OR EMERGENCY)
    

The **Resource** menu lets you filter by resource. You can select a resource type, such as **Audited Resource** , or you can navigate through the menus to select a specific method.

For example, to add a query for **Audited Resource** , do the following:

  1. Expand the **Resource** menu.
  2. Search for and select **Audited Resource**.
  3. Click **Apply**.

These steps add the following clause to the **Query Editor** field:
         
         resource.type="audited_resource"
         




Similarly, to add a query for Cloud Run functions audit logs, do the following:

  1. Expand the **Resource** menu.
  2. Search for and select **Audited Resource**.
  3. In the services menu, select **Cloud Functions**.
  4. Click **Apply**.

These steps add the following clause to the **Query Editor** field:
         
         resource.type="audited_resource" resource.labels.service="cloudfunctions.googleapis.com"
         




### Add variables to your query

You can use [variables](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent) in your query or in other fields in the logs panel widget. When you change the value of the variable, the data shown by the widget also changes.

To add a variable to your query, do the following:

  1. [Create a variable](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent#create-variable). In the Google Cloud console, you can use a dashboard's _settings_ **Settings** option to create, edit, and view variables. You can also use the Cloud Monitoring API.

  2. To apply a variable to your query, use one of the following forms:

     * For label-based variables, use `${label_based_variable.value}`.
     * For value-based variables, use `${value_based_variable}`.

For example, suppose you create the value-only variable `value_only_severity_variable` and configure it to have one of three values: `ERROR`, `INFO`, and `NOTICE`. You also add the following statement to your query:
    
    severity =~ "${value_only_severity_variable}"
    

The following illustrates the rendered form:
    
    severity =~ "^(ERROR|INFO|NOTICE)$"
    

For more information about variables and how to apply them to the logs panel widget or to other widgets, see [Update the query of a widget](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent#apply-permanent-filter).




For information about how to use a variable to show or hide a widget, see [Set the visibility of a widget](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent#set-visibility).

### Filter the log entries

**Note:** A query can have at most 2,000 characters.

You can modify which log entries a logs panel widget displays by modifying the values of the following fields or menus:

  * Dashboard time selector: By default, the logs panel widget only retrieves log entries that are written in the interval specified by this field. If you want a different interval, then apply a filter that includes a `timestamp` clause. The logs panel widget doesn't support a time-range override.

  * **Filter** field on the logs panel widget: The filter you specify is applied after the query completes. The value of this field is retained only for the current session.

  * **Severity** menu on the logs panel widget: The filter by severity level is applied after the query completes. The value of this field is retained only for the current session.

  * Query on the logs panel widget: The logs panel widget displays only those log entries that match the query. If you don't specify a query, then all logs in the selected time interval are displayed. If you do specify a query, then the logs panel widget displays a **Show query** icon, which displays the current query as a tooltip.

To modify the query, edit the logs panel widget.

  * Google Cloud project on the logs panel widget: To modify this setting, edit the logs panel widget.

  * Dashboard filters: When dashboard filters exist, the filter setting is applied to the query of the logs panel widget. For example, if you add the dashboard filter **cluster_name: mycluster** , then the query is updated to include **resource.labels."cluster_name"="mycluster"**. For more information about dashboard filters, see [Add temporary filters](https://docs.cloud.google.com/monitoring/charts/filter-dashboard) and [Add permanent filters](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent).




The remainder of this section provides additional information about how to filter your log entries.

#### Example: filter log entries by date

To display the most recent logs in a logs panel widget, use the time fields in the dashboard toolbar. For example, you might set the toolbar's time-range selector to **1H**. Provided you don't select a custom time range, the widget always displays the most recent logs, even when they are older than the selected time window.

When you are investigating an alert, you might want to restrict the log entries to those entries that are in a specific time interval. To configure the log entries to only show logs that are in a fixed time interval, do one or both of the following:

  * Select a time range by using the time-range selector.
  * Enter a `timestamp` clause in the **Query Editor** field of the configuration pane, and then select **Apply filter**.



When you specify a time interval, the logs panel widget isn't automatically refreshed.

#### Example: filter log entries by severity

When you are debugging a failure, you might want to view only error messages and hide all other log entries from the display. To configure a logs panel widget to display only those log entries that satisfy specific severity levels, do one or both of the following:

  * To apply a temporary filter, select a value for the **Severity** menu in the logs panel widget. This menu specifies a minimum severity level. For example, a value of "Warning" results in log entries with a severity of "Error" being retrieved, but those log entries with a severity of "Notice" aren't retrieved. By default, the value for this field is set to `Default`, which includes all log entries.

The setting for the **Severity** menu is discarded when you navigate away from the dashboard.

  * To apply a permanent filter, enter a `severity` clause in the **Query Editor** field of the configuration pane, and then select **Apply filter**.




#### Example: filter log entries by a string or phrase

Filtering log entries by a specific string or phrase lets you hide log entries that aren't of interest. For example, to view log entries that include a specific email address, you can filter by that address.

  * To apply a temporary filter so that you view only those log entries that contain a specific word or phrase, use the _filter_list_ **Filter** field. The contains test is case-insensitive.

If you add multiple filters, then only logs that match all filters are shown because an implicit `AND` is inserted between adjacent filters. However, you can explicitly insert an `OR` operator:

    * For example, when you add the filters `Get` and `Compute`, log entries that contain both words are shown.

    * For example, when you add the filters `Get`, `OR`, and `Compute`, log entries that contain `Get` or `Compute` are shown.

The value of the _filter_list_ **Filter** field isn't persistent.

  * To apply a permanent filter, modify the query stored in the **Query Editor** field, and then select **Apply filter**. For information about the query syntax, see [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language).

For example, to display only those log entries with a `MESSAGE` field whose value contains the string "lamp", add the clause `jsonPayload.MESSAGE:"lamp"` to the **Query Editor** field.




### View log entries in the Logs Explorer

Logs panel widgets display key fields of log entries; they don't display the complete log entry. To examine all fields of a log entry, do the following:

  1. In the logs panel widget, select **View in Logs Explorer**.
  2. In the dialog, select the Google Cloud project in which to open Logs Explorer.

Logs Explorer opens in a new browser tab, and the filters you've selected in the logs panel widget are automatically applied.

  3. Select the log entry that you want to view.




## Display charts generated from a Observability Analytics query

This section describes how to configure and save a chart generated from a Observability Analytics query to a custom dashboard. Observability Analytics lets you search and aggregate logs to generate useful insights by using SQL queries.

In addition to using the Observability Analytics page to configure and [save charts to a dashboard](https://docs.cloud.google.com/logging/docs/analyze/charts#save-chart-dashboard), you can save a Observability Analytics chart directly in **Monitoring** by doing the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select a dashboard or click **Create dashboard**.
  4. In the toolbar, click _add_ **Add widget**.
  5. In the **Add widget** dialog, go to the **Data** section, and then select **Observability Analytics**.
  6. In the **Configure widget** dialog, configure the data to display, and then click **Run Query**.

To select the data to display, you can build a SQL query or you can select a saved or recent query. The [log views](https://docs.cloud.google.com/logging/docs/logs-views) and [analytics views](https://docs.cloud.google.com/logging/docs/analyze/about-analytics-views) that you can query are listed in the **Views & Schema** section. Clicking a data source shows a list of fields for that data source under the **Schema** header.

  7. Optional: In the **Results** tab, customize the chart configuration by using the **Display** panel.

In the **Display** panel, you can change the chart type and customize which rows and columns are charted by changing the dimension, measure, and breakdown:

     * **Dimension** : The dimension must be a timestamp, numeric, or string column. By default, the dimension is set to the first timestamp-based column in the schema. If no timestamp is present in the query, then the first string column is selected as the dimension. You can also customize what the dimension is in the **Chart display** panel. When a timestamp column is selected as the dimension, then the chart shows how data changes over time. When a string column is selected as the dimension for a bar chart, you can sort the data by ascending or descending, which sorts the dimension by lexical order. You can also keep the `default` sort order, which sorts the dimension based on the values of the corresponding measure in descending order. 

     * **Measure** : You can select multiple measures in the **Chart display** panel. When you select a measure, you must also select the aggregation function to perform on its grouped values, such as `count`, `sum`, `average`, and `percentile-99`. For example, `count-distinct` returns the number of unique values in a given column. 

     * **Breakdown** : To split a single data series into multiple data series based on another column, add a breakdown. 

For more information about customizing the chart configuration, see [Customize chart configuration](https://docs.cloud.google.com/logging/docs/analyze/charts#chart-config).

  8. To save your modified dashboard, in the toolbar, click **Save**.




Observability Analytics charts can also be edited after they are saved to a dashboard. For more information, see [Modify a widget's configuration](https://docs.cloud.google.com/monitoring/charts/manage-widgets#editing).

## Display errors on a dashboard

This section describes how to add and configure an error-reporting panel by using the Google Cloud console. For information about adding an error-reporting panel to a dashboard by using the Cloud Monitoring API, see [Dashboard with an `ErrorReportingPanel` widget](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_er_panel).

To add an error-reporting panel to the dashboard by using the console, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select a dashboard or click **Create dashboard**.
  4. In the toolbar, click _add_ **Add widget**.
  5. In the **Add widget** dialog, go to the **Visualization** section, and then select **Error Reporting panel**.
  6. Expand _arrow_drop_down_ **Projects** , and then select a project.
  7. Optional: Update the title.
  8. Optional: To restrict the resources for which errors are displayed, do the following:

     1. Expand _arrow_drop_down_ **All Resources** and select a resource.
     2. After you select a resource, you can select **Apply** , or you can use the additional menus to refine the filter criteria:

        * To show errors for App Engine resources, select **GAE Services** , and then click **Apply**.

        * To show errors for a specific App Engine service, select **GAE Services** , select the service, and then click **Apply**.

  9. To apply your changes to the dashboard, in the toolbar, click **Apply**. To discard your changes, click **Cancel**.

The following example shows an error-reporting panel:

![Example of an error-reporting panel configuration pane.](https://docs.cloud.google.com/static/monitoring/images/dash-tex-er-widget.png)

  10. To save your modified dashboard, in the toolbar, click **Save**.




## Troubleshoot

  * [Logs panel indicates it displays partial data](https://docs.cloud.google.com/monitoring/charts/troubleshooting-charts#trouble-partial-logs)
  * [Logs panel reports an invalid query](https://docs.cloud.google.com/monitoring/charts/troubleshooting-charts#trouble-invalid-query)
  * [Logs panel displays a "No entries found" message](https://docs.cloud.google.com/monitoring/charts/troubleshooting-charts#trouble-no-entries)



## What's next

  * [Metrics scope overview](https://docs.cloud.google.com/monitoring/settings) describes how Cloud Monitoring provides visibility into metrics and logs stored in multiple Google Cloud projects.

  * [Error Reporting overview](https://docs.cloud.google.com/error-reporting/docs/grouping-errors) describes error groups.

  * For information about how to configure a dashboard to show logs or errors by using the API, see the following:

    * [Dashboard with a `LogsPanel` widget](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_logs_panel).
    * [Dashboard with an `ErrorReportingPanel` widget](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_er_panel).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
