---
url: https://docs.cloud.google.com/monitoring/charts/manage-widgets/
title: Manage dashboard widgets \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:03.457047+00:00
---

# Manage dashboard widgets  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/charts/manage-widgets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Manage dashboard widgets Stay organized with collections  Save and categorize content based on your preferences. 

To refine how your custom dashboards in Cloud Monitoring present telemetry, you can modify, convert, or delete existing dashboard widgets by using the Google Cloud console. For example, you can change a line chart into a stacked-area chart to see how each time series contributes to the total, update which time series a widget displays, or edit a widget's JSON representation.

To manage dashboard widgets programmatically, see [Create and manage dashboards by API](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard). To add new widgets to a dashboard, see the documents for [charts, tables, and indicators](https://docs.cloud.google.com/monitoring/charts), [alerts](https://docs.cloud.google.com/monitoring/dashboards/alerts-and-incidents), [log entries](https://docs.cloud.google.com/monitoring/charts/view-logs), [text and group widgets](https://docs.cloud.google.com/monitoring/dashboards/text-and-grouping), and [service-level objectives (SLOs)](https://docs.cloud.google.com/monitoring/dashboards/slos).

## Before you begin

Complete the following in the Google Cloud project where you want to manage your dashboards:

  * To get the permissions that you need to create and modify custom dashboards by using the Google Cloud console, ask your administrator to grant you the [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).




## View JSON representation

The JSON representation of a dashboard or a widget can be helpful when you prefer to manage your dashboards by using the Cloud Monitoring API but you prototype your dashboards by using the Google Cloud console.

To view or modify the JSON representation for the dashboard, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select a dashboard or click **Create dashboard**.
  4. Do one of the following:

     * To view or modify the JSON representation for the dashboard, in the dashboard toolbar, click _settings_ **Settings** , click **JSON** , and then click **JSON Editor**.

You can now view or modify the JSON representation. If you make modifications, then ensure that you click **Apply changes**.

     * To view or modify the JSON representation for a specific widget, place your pointer on the widget to activate the toolbar, click _edit_ **Edit widget** , and then click _code_ **JSON Editor**.

You can now view or modify the JSON. If you make modifications, then ensure that you click **Apply changes**.




## Change a widget's type

When a widget is displaying the correct data but not presenting it in the most useful way, consider changing the widget's type. For example, suppose you have a line chart on your dashboard. To view how each time series contributes to the sum, change that line chart to a stacked-area chart.

You can change a widget's type only if the destination widget can represent the data shown by the source widget. For example, you can always change a line chart into a stacked-area or stacked-bar chart. Similarly, you can always convert a gauge, which shows a single time series, into a line chart. However, you might not be able to convert a line chart, which can show multiple time series, into a gauge.

You can't change the type of a chart that displays data for an alerting policy, a logs panel, or a collapsible group. You can't convert any widget to a logs panel or to a collapsible group widget.

### Create an alerting policy from a line chart

To convert a line chart that displays a single metric type to a chart that displays data for an alerting policy, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select a dashboard or click **Create dashboard**.
  4. Place your pointer on the widget to activate the toolbar, click _more_vert_ **More options** , and then select **Convert to alert chart**.

When you make this selection, the **Create alert policy** dialog opens and the metric, filter, and grouping selections from your chart are applied to the alerting condition. Complete the specification of the alerting policy and then click **Create**. For information about those steps, see [Create an alerting policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).

  5. To apply your changes to the dashboard, in the toolbar, click **Apply**. To discard your changes, click **Cancel**.




### Set the widget type

To perform any conversions other than converting a line chart to a chart that displays data for an alerting policy, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select a dashboard or click **Create dashboard**.
  4. On the widget whose type you want to change, place your pointer on the widget to activate the toolbar, and then click _edit_ **Edit widget**.
  5. In the **Display** pane, expand the **Widget type** menu, and then make a selection.

The **Widget type** menu lists all widget types that can display the same type of data; however, some widgets might not be enabled.

For example, consider a chart that displays multiple time series, where each measurement is a double:

     * The logs panel isn't listed because it can't display time-series data.
     * The **Scorecard** and **Gauge** widgets are listed under the heading **Compatible with adjustments** because these two widgets can only display a single time series and the chart is displaying multiple time series. Before you can convert to one of these types, you must modify the grouping configuration.
     * The **Heatmap** widget is disabled because these widgets only display distribution-valued data.
     * The **Stacked area** , **Stacked bar** , and **Table** widgets are listed under the heading **Compatible**. You can select one of these values.
  6. To apply your changes to the dashboard, in the toolbar, click **Apply**. To discard your changes, click **Cancel**.




## Modify a widget's configuration

To change which time series a widget displays or to change how those time series are combined, modify the widget's configuration. For example, when a chart displays many time series, you can improve the chart's performance and visual clarity by grouping time series by one or more labels.

To modify a widget's configuration, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select a dashboard or click **Create dashboard**.
  4. Edit the widget:

     * For all widgets other than the single-view widget and the collapsible group widget, place your pointer on the widget to activate the toolbar, and then click _edit_ **Edit widget**.

The configuration page for the widget opens.

     * For the collapsible group widget, do any of the following:

       * To edit the group name, click _edit_ **Edit group** , and then complete the dialog.
       * To add widgets to the group, drag the widgets from the dashboard to the group.
       * To remove widgets from the group, delete the widgets or drag them to unused space on the dashboard.
     * For the single-view widget, expand the **Widget** menu, click _edit_ **Edit group** , and then do any of the following:

       * To add a widget to the group, click **Add widget** and then complete the dialog.
       * To remove a widget from the group, do one of the following:

         1. To delete a widget, click delete **Delete widget**.
         2. To remove a widget from the group and move it to the dashboard, click _cancel_ **Remove from group**.
  5. To apply your changes to the dashboard, in the toolbar, click **Apply**. To discard your changes, click **Cancel**.




## Delete a widget

How quickly a dashboard displays data depends on the number of widgets the dashboard displays and on the number of time series each widget displays. To improve the performance of a dashboard, one option is to place rarely used widgets in a collapsible group widget and collapse the group. Data for widgets in a collapsed group is loaded at a lower priority than for other dashboard widgets. An alternative to using the collapsible group widget is to delete those widgets that you don't use.

Deleting a chart associated with an alerting policy doesn't delete the alerting policy whose data was displayed on the chart. To delete an alerting policy, go to the **Alerting** page in the Google Cloud console. For information about how to delete a policy, see [Manage alerting policies](https://docs.cloud.google.com/monitoring/alerts/manage-alerts). You can't delete an alerting policy from a custom dashboard.

To delete a widget on a dashboard, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select a dashboard or click **Create dashboard**.
  4. Delete the widget:

     * For all widgets other than the single-view widget and the collapsible group widget, place your pointer on the widget to activate the toolbar, click _more_vert_ **More options** , and then select **Delete widget**.

     * For the collapsible group widget, place your pointer on the widget to activate the toolbar, and then do one of the following:

       * To delete the collapsible group widget and the widgets it contains, click delete **Remove group and its children**.
       * To delete a collapsible group widget and move the widgets to the dashboard, click _cancel_ **Remove the group but keep its children**.
     * For the single-view widget, expand the **Widget** menu, click _edit_ **Edit group** , and then do one of the following:

       * To delete the single-view group widget and the widgets it contains, click delete **Delete group**.
       * To delete the single-view group and move the widgets it contains to the dashboard, click _cancel_ **Ungroup**.
  5. To apply your changes to the dashboard, in the toolbar, click **Apply**. To discard your changes, click **Cancel**.




## What's next

  * [Explore charted data](https://docs.cloud.google.com/monitoring/charts/working-with-charts)
  * [Configure legends](https://docs.cloud.google.com/monitoring/charts/working-with-legends)
  * Filter a dashboard: 
    * [Add temporary filters to a custom dashboard](https://docs.cloud.google.com/monitoring/charts/filter-dashboard)
    * [Add permanent filters to a custom dashboard](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
