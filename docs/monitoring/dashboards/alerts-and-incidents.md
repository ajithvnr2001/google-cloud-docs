---
url: https://docs.cloud.google.com/monitoring/dashboards/alerts-and-incidents/
title: Display alerts and charts for alerting policies \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:57.677087+00:00
---

# Display alerts and charts for alerting policies  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/dashboards/alerts-and-incidents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Display alerts and charts for alerting policies Stay organized with collections  Save and categorize content based on your preferences. 

Alerting policy charts and **Alerts** widgets on a custom dashboard in Cloud Monitoring let you monitor policy thresholds and track open alerts alongside your telemetry data. Policy charts plot the monitored time series against condition thresholds, while **Alerts** widgets list alerts in a table so you can inspect policy conditions and alert details.

This document describes how to add these widgets by using the Google Cloud console. To configure them programmatically by using the Cloud Monitoring API, see [Create and manage dashboards by API](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard), [Dashboard with an `AlertChart` widget](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_an_alert), and [Dashboard with an `IncidentList` widget](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_incident_list).

## Before you begin

Complete the following in the Google Cloud project where you want to create and manage dashboards:

  * To get the permissions that you need to create and modify custom dashboards by using the Google Cloud console, ask your administrator to grant you the [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).

  * You can put up to 100 widgets on a dashboard.




## Add alerting policies to a dashboard

To view the data that an alerting policy monitors alongside log, metric, and trace data, add the alerting policy's chart to your dashboard. The chart displays the monitored time series, the associated threshold, the number of open alerts, and whether the policy is disabled. You can also use options on the chart to get more information about the alerting policy.

The following screenshot illustrates a chart for an alerting policy:

![Example of a chart for an alerting policy.](https://docs.cloud.google.com/static/monitoring/images/chartdef-style-alert.png)

To display the chart for an alerting policy on a dashboard, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select a dashboard or click **Create dashboard**.
  4. In the toolbar, click _add_ **Add widget**.
  5. In the **Add widget** dialog, select ![](https://docs.cloud.google.com/static/stackdriver/images/alerting-widget-icon.svg)**Alerting Policy**.
  6. Click _arrow_drop_down_ **Alerting policy** , and then select an alerting policy.
  7. To apply your changes to the dashboard, in the toolbar, click **Apply**. To discard your changes, click **Cancel**.



### Inspect an alerting policy or explore chart metrics

When you are viewing a chart for an alerting policy, you might want more information about the alerting policy. For example, you might want to review the selected notification channels or what custom documentation is included with a notification. To get information about the alerting policy, try the following:

  * To access the alerting policy, click the alerts chip on the chart, and then select **View alert policy**.

  * To view details of the chart, place your pointer on the chart, click _more_vert_ **More chart options** , and then select **View in Metrics Explorer**.

Metrics Explorer displays a copy of the chart that is on your dashboard.




### Charts for deleted alerting policies

If you delete an alerting policy, any charts associated with that policy stop displaying data. For more information, see [Alerting policy widget doesn't display any data](https://docs.cloud.google.com/monitoring/charts/troubleshooting-charts#no-data-alert-chart).

## Display alerts on a dashboard

To view a table of alerts in the same context as your metric data, add an **Alerts** widget, which lists information about alerts using a tabular format. For each alert, the widget displays the names of the alerting policy and condition, and when the alert opened. The widget includes options that let you view the associated alerting policy and the alert details.

The following screenshot illustrates an **Alerts** widget:

Alerts widget." class="screenshot">

The remaining information in this section is for the Google Cloud console. For information about using the Cloud Monitoring API, see [Dashboard with an **Alerts** widget](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_incident_list).

An **Alerts** widget can list at most 20 alerting policies or at most 20 resources. An **Alerts** widget can't list both alerting policies and resources.

To display alerts on a dashboard, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select a dashboard or click **Create dashboard**.
  4. In the toolbar, click _add_ **Add widget**.
  5. In the **Add widget** dialog, select ![](https://docs.cloud.google.com/static/monitoring/images/incident_button.png) **Alerts**.
  6. Optional: Add a title.
  7. Optional: Select the criteria that define which alerts are shown. By default, all alerts in the Google Cloud project are listed. However, you can restrict the widget to display alerts for specific alerting policies or resource types:

     * To display all alerts, use the default settings.

     * To display only alerts for specific alerting policies, select **Alert policy** and then make selections from the **Alert policies** menu.

There is a limit of 20 alerting policies per **Alerts** widget. If you exceed this limit, the Google Cloud console displays the error message `"You must choose no more than 20 policies"`.

     * To display only alerts for specific resource types, select **Resource type** and then make selections from the **Resource types** menu.

There is a limit of 20 resources per **Alerts** widget. If you exceed this limit, then saving your dashboard fails.

You can't select specific alerting policies and specific resource types.

  8. To apply your changes to the dashboard, in the toolbar, click **Apply**. To discard your changes, click **Cancel**.




By default, only open alerts are shown. To show all alerts, including those that have closed within the time interval specified by the time-range selector, place your pointer on the **Alerts** widget to enable the toolbar, and then enable the ![](https://docs.cloud.google.com/static/monitoring/images/toggle-on.png)**Show closed alerts** toggle.

You can sort the list of alerts by the date opened or closed. You can also search the list by using the _filter_list_ **Filter** field.

### Inspect an alert or explore alerting policy details

When you are viewing an **Alerts** widget, you might want information about the alert or the alerting policy:

  * To view the details of an alert, find that alert in the **Alerts** widget and click **View**.

  * To view the details of the alerting policy associated with the alert, find that alert in the **Alerts** widget and then select the policy name.




## What's next

You can also add widgets to your custom dashboards that display the following:

  * [Metric data](https://docs.cloud.google.com/monitoring/charts)
  * [Log entries](https://docs.cloud.google.com/monitoring/charts/view-logs)
  * [Trace data](https://docs.cloud.google.com/monitoring/dashboards/display-traces-on-dashboards)
  * [Descriptive text](https://docs.cloud.google.com/monitoring/dashboards/text-and-grouping)
  * [Service-level objectives (SLOs) for a set of services](https://docs.cloud.google.com/monitoring/dashboards/slos)



For information about exploring charted data and filtering your dashboards, see the following documents:

  * [Explore charted data](https://docs.cloud.google.com/monitoring/charts/working-with-charts)
  * [Add temporary dashboard filters](https://docs.cloud.google.com/monitoring/charts/filter-dashboard)
  * [Create and manage variables and pinned filters](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
