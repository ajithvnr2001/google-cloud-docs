---
url: https://docs.cloud.google.com/logging/docs/view/dashboard/
title: Visualize log severity and error metrics \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:51.321999+00:00
---

# Visualize log severity and error metrics  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/view/dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Visualize log severity and error metrics Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use the Logs Dashboard page to detect trends in the behavior of your systems, monitor your workloads, and diagnose and resolve problems by using the predefined dashboard or by creating a custom dashboard.

## Types of dashboards

The **Logs Dashboard** page has two options for visualizing the performance of the resources in your Google Cloud project: the predefined dashboard and a custom dashboard. The predefined dashboard is always available and is managed by Monitoring, but you can also customize this predefined dashboard.

### Predefined dashboard

The predefined dashboard is automatically configured and only provides information for resources in your Google Cloud project that are producing logs data.

The predefined dashboard is organized into a pair of charts for each of the following resource types:

  * Google Kubernetes Engine

  * Compute Engine

  * App Engine

  * Cloud Load Balancing

  * Cloud SQL

  * BigQuery




One chart displays the number of logs and their severity types, such as `WARNING`. The other chart displays logs that contain errors. To get more information about severity types or error logs, hold your pointer over the chart.

The following screenshot is an example of the predefined dashboard:

![Example of a dashboard that displays Google Kubernetes Engine severity and errors.](https://docs.cloud.google.com/static/logging/docs/images/resource-severity-errors.png)

### Custom dashboard

If the content in the predefined dashboard doesn't contain the information you need to help you troubleshoot, then consider creating a custom dashboard. [Custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards) let you display information that is of interest to you, organized in a way that's useful to you. For example, you might create a dashboard that displays the logs, metrics, and alerting policies for virtual machines (VM) in your production environment.

Custom dashboards are managed by Cloud Monitoring, but you must create a new custom dashboard to use in the **Logs Dashboard** page. The custom dashboard you create in the **Logs Dashboard** page is only accessible in Cloud Logging. When you create a custom dashboard, the predefined dashboard is copied into the custom dashboard, so that you can delete unnecessary widgets and add missing content.

## View the predefined dashboard

To view the predefined dashboard, do the following:

  1. In the Google Cloud console, go to the **Logs Dashboard** page: 

[Go to **Logs Dashboard**](https://console.cloud.google.com/monitoring/dashboards/resourceList/logs)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

**Note:** Ensure that a project is selected. When a project isn't selected, the dashboard displays a loading-data spinner.

  2. If the **Dashboard** menu is enabled, then select **Predefined**.




## Customize the predefined dashboard

You can't modify the predefined dashboard. However, you can make a copy of this dashboard, and then modify the copy.

To create a copy of the predefined dashboard, do the following:

  1. In the Google Cloud console, go to the **Logs Dashboard** page: 

[Go to **Logs Dashboard**](https://console.cloud.google.com/monitoring/dashboards/resourceList/logs)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

**Note:** Ensure that a project is selected. When a project isn't selected, the dashboard displays a loading-data spinner.

  2. In the toolbar of the dashboard, select _edit_**Customize Dashboard**. 

A dashboard is created and displayed. The name of the dashboard is listed in the **Custom view name** text box. The toolbar also displays three buttons: **Add widget** , **Exit Edit Mode** , and **Save**.

  3. Modify the dashboard by adding or removing widgets, by editing existing widgets, or by moving widgets.

For example, to add a widget, click **Add widget** , complete the dialog, and then select **Apply**. For more information about adding widgets, see the following pages:

     * [Add charts and tables](https://docs.cloud.google.com/monitoring/charts#add_chart).
     * [Display alerts and charts for alerting policies](https://docs.cloud.google.com/monitoring/dashboards/alerts-and-incidents).
     * [Display logs](https://docs.cloud.google.com/monitoring/charts/view-logs).
     * [Add text and groupings](https://docs.cloud.google.com/monitoring/dashboards/text-and-grouping).
  4. After you complete your modifications, go to the toobar and click **Save**.

To toggle between the predefined dashboard and your custom dashboard, use the menu in the toolbar.




## What's next

  * For information about dashboards and how to select what information to display on a dashboard, see [Dashboards overview](https://docs.cloud.google.com/monitoring/dashboards).

  * For information about displaying project-scoped logs on your dashboards, see [Display logs on a custom dashboard](https://docs.cloud.google.com/monitoring/charts/view-logs).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
