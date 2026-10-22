---
url: https://docs.cloud.google.com/monitoring/charts/filter-dashboard/
title: Add temporary filters to a custom dashboard \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:58.089093+00:00
---

# Add temporary filters to a custom dashboard  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/charts/filter-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Add temporary filters to a custom dashboard Stay organized with collections  Save and categorize content based on your preferences. 

Temporary filters and groupings in Cloud Monitoring let you dynamically narrow or aggregate the data displayed across a custom dashboard without editing individual widgets. For example, when investigating an alert, you can apply a temporary filter from the dashboard toolbar to view metrics and logs for only a specific virtual machine (VM) or region.

Reloading the page clears these settings automatically, or you can remove them manually. To save filters for future sessions or apply them to specific widgets, see [Create and manage variables and pinned filters](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent).

## How dashboard filters work

A dashboard filter specifies a label and a value. The time series that the dashboard displays determine the labels available for filtering. How a widget supports a dashboard-wide filter depends on the type of data the widget displays, and the configuration of the widget:

  * For widgets that display time-series data, such as line charts, the following rules apply:

    * If the time series displayed by the widget doesn't support the label in a filter, then the dashboard-wide filter doesn't change the displayed data.

For example, if you add a filter on the label `instance_id`, but a chart on the dashboard doesn't display data with an `instance_id` label, then the filter doesn't change the displayed data.

    * If the widget specifies a value for a label, then the dashboard-wide filter doesn't change the displayed data.

For example, if you add a filter on the label `instance_id`, but a chart on the dashboard includes a filter based on the `instance_id` label, then the dashboard-wide filter doesn't change the displayed data.

    * Otherwise, the chart filters the data it displays to only those time series that satisfy the dashboard-wide filter.

  * For logs panel widgets, dashboard-wide filters that are based on a resource label update the query. For example, if you add the dashboard-wide filter **cluster_name: mycluster** , then the query is updated to include **resource.labels."cluster_name"="mycluster"**.




You can add multiple dashboard-wide filters. These filters are joined with a logical AND.

## Before you begin

Complete the following in the Google Cloud project where you want to view your dashboards:

  * To get the permissions that you need to add or modify temporary filters by using the Google Cloud console, ask your administrator to grant you the [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).




## Create or modify temporary groupings

When you add dashboard-wide groupings, the widgets on the dashboard display one time series for each set of time series that have the same values for the grouping labels. By default, the average of each set is shown. However, when the widget defines a grouping function, then that function is used.

For example, assume your dashboard contains a chart that displays the CPU utilization of your VM instances. To determine whether you need to deploy more VMs to a particular zone, you could edit the dashboard and that chart to change its grouping options. An alternative is to temporarily group the dashboard by zone, and then view the CPU utilization chart.

To create or modify the temporary groupings, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Expand the _arrow_drop_down_ **Group By** menu and then select the labels for grouping.
  4. Click **OK**.



When you navigate away from the dashboard, any groupings that you created are discarded.

## Create a temporary filter

When you are investigating an alert, you might want to look at data in specific ways. For example, you might want to view only time series for a specific virtual machine or for resources in a specific region. When you create a temporary filter, all dashboard widgets are modified to show data that matches that filter. For example, to configure all charts to show only time series for a specific VM instance, create a filter based on the label `instance_id`. Similarly, to configure the dashboard to only show time series for a specific zone, create a filter based on the label `zone`.

To create a temporary filter, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. In the dashboard's _filter_list_ filter bar, click **Add filter** , and then select a label from the menu.

The menu lists the labels for every time series shown on the dashboard.

After you select a label, a filter is added to the dashboard toolbar. The filter's name has the same name as your selection, and its value is set to `*`, which matches all values. For example, if you select `zone`, then the toolbar displays `zone: *`.

  4. To select a specific value to match, click the filter (for example, click `zone: *`), and then select a value from the menu. To reduce the number of menu options, enter part of the value into the _filter_list_ **Filter** area.


**Note:** For tables that display time-series data, some table cells contain a _filter_list_ **Filter dashboard to this value** button, which becomes visible when you place your pointer in the cell. If you select this button, then either a new filter is applied or the value for an existing permanent filter or variable is updated. Existing filters and variables are updated when the label key for the table column matches the label key for a filter or variable.

When you navigate away from the dashboard, any filters that you created are discarded.

## Modify a temporary filter

To modify the value of a temporary filter, on that filter, click _arrow_drop_down_ **Menu** , and then make a selection.

After you make a selection, charts and tables are refreshed.

## Delete a temporary filter

Temporary filters are deleted automatically when you navigate away from the dashboard. To manually remove a temporary filter, on that filter, click _cancel_ **Delete**.

## What's next

  * [Explore charted data](https://docs.cloud.google.com/monitoring/charts/working-with-charts)
  * [Access resource-specific dashboards](https://docs.cloud.google.com/monitoring/charts/working-with-legends#resource-dashboards)
  * [Create and manage variables and pinned filters](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
