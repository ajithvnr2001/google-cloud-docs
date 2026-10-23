---
url: https://docs.cloud.google.com/workload-manager/docs/observe/sap/modify-dashboards/
title: Modify observability dashboards \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:04.450488+00:00
---

# Modify observability dashboards  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/observe/sap/modify-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Modify observability dashboards Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create custom dashboards and how to add events on the observability dashboards in Workload Manager.

## Create custom dashboards

By default, Workload Manager provides a predefined dashboard that displays the observability metrics for SAP workloads. To view only specific metrics or to change the order of the widgets, you can modify the predefined dashboard and save it as a customized dashboard.

**Note:** To create custom dashboards, all widgets on the predefined dashboard must report metric values. Otherwise, you see an error message and the dashboard creation fails.

Custom dashboards carry over between different SAP systems. For example, if you create a custom dashboard for the Application dashboard on system ID ED1, you can view the same dashboard when viewing another system ID PF7.

To create a custom dashboard, do the following:

  1. In the Google Cloud console, go to the **Workload Manager** page.

[Go to Workload Manager](https://console.cloud.google.com/workload-manager/systems)

  2. Select **Observability** from the left navigation menu.

  3. To customize the predefined dashboard, on the dashboard toolbar, click edit.

Workload Manager creates a copy of the predefined dashboard, and then opens the copy in edit mode.

  4. In the editor, you can add, modify, delete, reposition, or resize the visualizations in the dashboard. The visualizations are collectively called _widgets_. For more information about the different widget types, see [Dashboards overview](https://docs.cloud.google.com/monitoring/dashboards).

  5. After you finish modifying the dashboard, click **Save**.

  6. In the dialog confirming the changes, click **View customized dashboard** to go to the customized view.

You can switch back to the predefined view by selecting **Predefined** from the **Dashboard** drop-down.




## Add events to the dashboards

You can add events directly to the charts on both the Applications and Database dashboards. This helps correlate events and the corresponding impact on metrics and values.

To configure the SAP obserbility dashboards to show events, do the following:

  1. In the Google Cloud console, go to the **Workload Manager** page.

[Go to Workload Manager](https://console.cloud.google.com/workload-manager/systems)

  2. Select **Observability** from the left navigation menu.

  3. Verify that the **Dashboard** menu is set to **Predefined**. Events can't be shown on custom dashboards.

  4. On the toolbar, click _event_available_ , and select the events that you want to add to the dashboard.

  5. Click **Ok** to return to the dashboard.




When one of the selected events occurs, it is displayed directly on all the related graphs and widgets. Hold the pointer over the event icon to view additional information or view the complete logs.

In [Preview](https://docs.cloud.google.com/workload-manager/docs/observe/sap/\(/products#product-launch-stages\)), only the following events are supported on the dashboards:

  * VM termination: Helps you identify VM terminations, including manually triggered stops, guest OS terminations, maintenance terminations, and host errors.
  * VM start failed: Tracks VM instance start failures due to stockouts, IP space exhaustion, quota exceeded errors, or Shielded VM integrity errors.
  * VM guest OS error: Tracks specific VM instance guest OS errors including disk full, file system mount failed, and boot failures that activate Linux emergency mode.



## What's next

  * [Remove workloads from dashboards](https://docs.cloud.google.com/workload-manager/docs/observe/sap/view-dashboards).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
