---
url: https://docs.cloud.google.com/monitoring/charts/predefined-dashboards/
title: View and copy Google Cloud dashboards \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:58.279618+00:00
---

# View and copy Google Cloud dashboards  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/charts/predefined-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  View and copy Google Cloud dashboards Stay organized with collections  Save and categorize content based on your preferences. 

Preconfigured dashboards in Cloud Monitoring let you monitor the health and performance of your Google Cloud resources—such as Compute Engine virtual machine (VM) instances or Google Kubernetes Engine clusters—without manual setup. Monitoring installs these service-specific dashboards automatically when you add resources to your Google Cloud project. Although you can't edit or delete preconfigured dashboards directly, you can copy supported dashboards or individual charts to [create a custom dashboard](https://docs.cloud.google.com/monitoring/charts/dashboards) for further customization.

## Before you begin

Complete the following in the Google Cloud project that stores the dashboards that you want to view:

  * To get the permissions that you need to view dashboards by using the Google Cloud console, ask your administrator to grant you the [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).




## View dashboards for Google Cloud services

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. In the **My Dashboards** pane, go to **Type** , and then select **Google Services**.
  4. To view the dashboard for a specific service, select that service in the list of dashboards.

To find a dashboard, you can add filters to the filter bar. For example, to find all Google Kubernetes Engine dashboards, you might add the filter **Name: GKE**. The **My Dashboards** pane only lists dashboards whose name contains **GKE**. When you add multiple filters, an implicit **AND** is applied between filters unless you include an **OR** operator.

     * To view Google Kubernetes Engine performance data, examine the dashboards whose names begin with **GKE**.

For example, the **GKE** dashboard reports data in a tabular format about your clusters, namespaces, nodes, workloads, and services. In contrast, the **GKE Compute Resources** dashboard displays charts that show information about memory and CPU utilization.

     * To view metrics and logs for an individual VM, click **VM Instances** , and then select the VM whose data you want to view.

Compute Engine also provides a dashboard for each VM instance, and the **Observability** tab of that dashboard displays the same metrics and logs that you can view from the dashboard provided by Cloud Monitoring. For more information about the Compute Engine dashboard, see [Observe and monitor VMs](https://docs.cloud.google.com/compute/docs/instances/observe-monitor-vms).

     * To view the metrics for all of your VMs, click **GCE VM Instance Monitoring**.




## Create a custom dashboard by copying a Google Cloud service dashboard

You can't delete or modify the automatically created dashboards; however, in some cases, you can copy these dashboards. You can modify the content of the copy, and you can delete the copy. For example, you might add widgets that display log data and delete uninteresting charts. You might also add labels, which can help you manage your dashboards, or configure which events the dashboard displays.

To create a copy of a dashboard for a Google Cloud service, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. In the **My Dashboards** pane, go to **Type** , and then select **Google Services**.
  4. Locate the dashboard that you want to copy, and then click _content_copy_ **Copy dashboard**.

Not all dashboards for Google Cloud services can be copied. If the copy icon isn't displayed, then the dashboard can't be copied.

  5. In the copy dialog, enter the name for the dashboard, and then click **Copy**.




The new dashboard that you created is listed in the **Custom** category. You can add and remove widgets, reposition widgets, and resize widgets. You can also delete the dashboard. For more information about adding widgets, see the following pages:

  * [Add charts and tables](https://docs.cloud.google.com/monitoring/charts#add_chart).
  * [Display alerts and charts for alerting policies](https://docs.cloud.google.com/monitoring/dashboards/alerts-and-incidents).
  * [Display logs](https://docs.cloud.google.com/monitoring/charts/view-logs).
  * [Add text and groupings](https://docs.cloud.google.com/monitoring/dashboards/text-and-grouping).
  * [Show events on a dashboard](https://docs.cloud.google.com/monitoring/dashboards/show-events).
  * [Add and remove labels](https://docs.cloud.google.com/monitoring/charts/dashboards#add-remove-labels).



## Copy a chart to a custom dashboard

A Google Cloud dashboard might only display some metric data that you want to view. While you can't add widgets to a Google Cloud dashboard, you can copy some widgets from these dashboards to custom dashboards. Not all widgets support the copy operation.

To copy a widget on a Google Cloud dashboard to a custom dashboard, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select the Google Cloud dashboard and then identify the chart that you want to copy.
  4. In the chart toolbar, select _more_vert_ **More chart options**.
  5. If **Clone widget** is a menu option, then select **Clone widget** , select the dashboard where the clone is to be saved, and then click **Clone**.
  6. Otherwise, select **View in Metrics Explorer** , select **Save as** , select **Dashboard chart** , and complete the dialog.



## Configure data refresh

When you open a dashboard, it is configured with auto refresh disabled. The toolbar displays a toggle, sync_disabled, which indicates this state.

For your current session, to enable auto refresh, go to the toolbar and select sync_disabled **Enable auto refresh**.

To disable auto refresh after you've enabled it, go to the toolbar and select sync **Disable auto refresh**.

**Note:** You can't configure a dashboard to open with auto refresh enabled. You can enable auto refresh for your current session only. When you reload the dashboard, auto refresh is disabled.

## What's next

  * [Create and manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards)
  * [Explore charted data](https://docs.cloud.google.com/monitoring/charts/working-with-charts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
