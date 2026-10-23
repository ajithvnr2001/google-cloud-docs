---
url: https://docs.cloud.google.com/monitoring/dashboards/slos/
title: Display SLOs on a custom dashboard \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:44.276671+00:00
---

# Display SLOs on a custom dashboard  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/dashboards/slos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Display SLOs on a custom dashboard Stay organized with collections  Save and categorize content based on your preferences. 

Service-level objective (SLO) charts on a custom dashboard in Cloud Monitoring let you monitor the health, compliance, and remaining error budget of your services in a single view. Each chart summarizes how a service performs against a configured target so you can track SLO status across a set of services.

You can add SLO charts in the Google Cloud console by following the steps in this document. To configure them with the Cloud Monitoring API instead, see [Create and manage dashboards by API](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard) and [Dashboard with an SLO widget](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_slo).

## Before you begin

Complete the following in the Google Cloud project where you want to create and modify dashboards:

  * To get the permissions that you need to create and modify custom dashboards by using the Google Cloud console, ask your administrator to grant you the [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).

  * You can put up to 100 widgets on a dashboard.

  * Configure your services and SLOs; for more information, see [SLO monitoring](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring).




## Display SLOs on a dashboard

The following screenshot illustrates a chart that displays the remaining error budget for an SLO:

![Example of an SLO chart that shows the remaining error budget for an SLO.](https://docs.cloud.google.com/static/monitoring/images/slo-chart-errbudget.png)

To add an SLO chart to a dashboard, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select a dashboard or click **Create dashboard**.
  4. In the toolbar, click _add_ **Add widget**.
  5. In the **Add widget** dialog, select ![](https://docs.cloud.google.com/static/monitoring/images/slo_button.png) **SLO**.
  6. In the **Choose an SLO to show data** pane, click _arrow_drop_down_ **Service** , and then select a service.
  7. Select an existing SLO for the service from the **Service-level Objectives** menu.

If the chosen service has no SLOs, then a message tells you that you must create one. To add an SLO, click **Create SLO**. For more information about creating SLOs, see [Creating an SLO](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-slo). After you create an SLO, select it and proceed to the next step.

  8. Select an SLO metric from the **Service Level Objective Chart Type** menu. You can select health, compliance, and absolute or fractional error budget. For more information about SLO metrics, see [Retrieving SLO data](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/timeseries-selectors).

  9. Optional: Update the chart title.

  10. To apply your changes to the dashboard, in the toolbar, click **Apply**. To discard your changes, click **Cancel**.




## What's next

You can also add widgets to your custom dashboards that display the following:

  * [Metric data](https://docs.cloud.google.com/monitoring/charts)
  * [Log entries](https://docs.cloud.google.com/monitoring/charts/view-logs)
  * [Trace data](https://docs.cloud.google.com/monitoring/dashboards/display-traces-on-dashboards)
  * [Descriptive text](https://docs.cloud.google.com/monitoring/dashboards/text-and-grouping)
  * [Display alerts and charts for alerting policies](https://docs.cloud.google.com/monitoring/dashboards/alerts-and-incidents)



For information about exploring charted data and filtering your dashboards, see the following documents:

  * [Explore charted data](https://docs.cloud.google.com/monitoring/charts/working-with-charts)
  * [Add temporary dashboard filters](https://docs.cloud.google.com/monitoring/charts/filter-dashboard)
  * [Create and manage variables and pinned filters](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
