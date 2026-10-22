---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-slo/
title: Creating an SLO \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:45.207682+00:00
---

# Creating an SLO  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-slo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Creating an SLO Stay organized with collections  Save and categorize content based on your preferences. 

To monitor a service, you need at least one service-level objective (SLO). The SLOs encapsulate your performance goals for the service. Every SLO is based on a performance metric, called a service-level indicator (SLI). For background information on SLIs and SLOs, see [Concepts in service monitoring](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring).

You can create up to 500 SLOs for a service.

## Before you begin

To get the permissions that you need to view and create SLOs, ask your administrator to grant you the Monitoring Editor (`roles/monitoring.editor`). IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Getting started

To define an SLO, navigate to the **Create a Service Level Objective (SLO)** pane.

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/services-icon.png) **SLOs** page: 

[Go to **SLOs**](https://console.cloud.google.com/monitoring/services)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Open the **Create a Service Level Objective (SLO)** pane:

For a new service:

     1. Click **Define service** , and then [define your service](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/define-svc).
     2. After you click **Submit** in the **Define service** pane, click **Create SLO**.

For an existing service:

     1. In the **Services** list, click the name of the service in the **Services** list.
     2. On the **Service details** page, click **Create SLO**.



The SLO-creation pane leads you through the steps to create an SLO. The remainder of this document describes each of the following steps in the SLO-creation process:

  1. Set the SLI.
  2. Define SLI details.
  3. Set the SLO.
  4. Review and save the SLO.



To advance to the next step, click **Continue**. You can click a previous step to make changes before you save the SLO. To exit the SLO-creation process, click **Cancel**.

## Setting your SLI

The **Set your SLI** pane has the following sub-panes:

  * **Service details** , which reports identifying information about your service. This is the same as the **Service details** pane on the dashboard for the service.

  * **Choose a metric** , where you choose a metric for the performance you want to monitor.

  * **Request-based or windows-based?** , where you choose how the metric is to be evaluated.




The following screenshot shows the SLI pane:

![Use the **Set your SLI** pane to choose a performance metric](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-slo-sli.png)

For more information about metrics used in SLIs and the evaluation methods, see the conceptual topic [Service-level indicators](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring#defn-sli).

### Choosing a metric

The SLI metric specifies the type of performance you want to measure. In the SLI, you build a ratio from the metric to measure good performance over time. You have the following options for SLIs:

  * Availability, which measures how available your service is to users.
  * Latency, which measures how responsive your service is to users.
  * Other, which lets you indicate that you want to use a specific metric. You specify the metric and describe how to build the SLI on the **Set SLI details** pane.



The valid choices depend on the type of service you are configuring.

  * For services on Cloud Service Mesh, Istio on Google Kubernetes Engine, and App Engine, you can choose any of the options. The availability and latency metrics are already known for these services, or you choose **Other** to use a custom SLI.

  * For GKE-based services, and for custom services, the only choice is **Other**. Prometheus metrics are not included in default availability and latency SLOs, and other meaningful availability or latency metrics aren't known in advance for these services.

If you configured collection of Prometheus metrics using [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus), you can set a collected Prometheus metric as a custom SLI.




### Choosing the evaluation method

After you select the metric for your SLI, you specify how the metric should be evaluated.

  * Request-based evaluation measures the number of requests that meet the evaluation criterion against the total number of requests in a given period.

  * Windows-based evaluation measures the number of evaluation periods that meet a goodness criterion against the total number of evaluation periods.




For both evaluation methods, you specify the evaluation criteria on the **Set SLI details** page.

For more information on these evaluation types, see [Compliance in request- and windows-based SLOs](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring#slo-types).

## Setting SLI details

The contents of the **Define SLI details** pane depends on the metric and evaluation method you chose in the previous step.

If you chose the availability metric and request-based evaluation, there are no other details needed.

### Windows-based evaluation

If you selected window-based evaluation, you set the additional criteria for the window on this pane: a goodness criterion and a duration.

![Set the SLI window by choosing a goodness criterion and evaluation period.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-slo-sli-window.png)

The goodness criterion indicates the percentage of windows that must evaluate to “good” over the compliance period. The duration specifies the length of the window.

### Latency metric

If you chose the latency metric, you specify the threshold value that determines acceptable performance on this pane:

![Set the latency threshold for the SLI.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-slo-sli-latency.png)

Anything above the latency threshold is considered “bad” performance in evaluating the SLI.

### Custom SLI

If you selected **Other** as the SLI metric, you specify the metric you want to use on this pane. You can select a metric by typing in the **Performance Metric** field or select one from the list.

The metrics in the list are divided into two types:

  * Distribution-cut indicators
  * Time-series ratio indicators



If you are collecting Prometheus metrics with Google Cloud Managed Service for Prometheus, the metric name starts with `prometheus.googleapis.com/`.

The following screenshot shows a partial list:

![Metrics in the menu are classified by indicator type.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-slo-sli-custom-metric.png)

If you select a distribution-cut indicator, you configure the SLI by providing a range—above, below, or between—and a filter to specify the monitored resource and any labels you want to include. The configuration pane looks like the following:

![Set a range and filter for a distribution-cut indicator.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-slo-sli-custom-distcut.png)

If you select a time-series ratio indicator, you configure the ratio by building numerator and denominator filters to classify the metric data, typically by selecting the values of labels in the metric or resource type. The configuration pane looks like the following:

![Set numerator and denominator filters for a time-series ratio.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-slo-sli-custom-ratio.png)

For more information about these SLI types, see the Monitoring API reference pages for [`DistributionCut`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut) and [`TimeSeriesRatio`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio).

#### GKE control plane metrics

GKE control plane metrics are useful indicators of system health that you can use for custom SLIs. You must [enable collection](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#control-plane-metrics) of these metrics before you can use them. These metrics are collected by Google Cloud Managed Service for Prometheus.

  * Use [API server metrics][gke-api-metrics] to track API server load, the fraction of API server requests that return errors, and the response latency for requests received by the API server.
  * Use [scheduler metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/control-plane-metrics#scheduler-metrics) to help you to proactively respond to scheduling issues when there aren't enough resources for pending Pods.



For more information about control plane metrics and using them to monitor system health, see [Use control plane metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/control-plane-metrics).

### Preview chart

After you have configured the SLI, the **Define SLI details** pane includes a preview chart to show you how the historical performance of this service is measured by the SLI. For example:

![The completed SLI shows a chart based on historical data.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-slo-sli-done.png)

If you have just created or deployed a service, there may not be any data yet. You can still create the SLI, but you won't get the historical perspective.

## Setting your SLO

The **Set your SLO** pane has the following regions:

  * **Compliance period** , where you set the time period over which you want to evaluate the SLI.

  * **Performance goal** , where you specify the threshold for performance over the compliance period.

  * **Preview** , which displays a chart that shows the performance-goal threshold and graph that shows the results of evaluating the SLI over the compliance period.




![Set the SLO by choosing a compliance period and a performance
goal.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-slo-slo.png)

### Compliance period

There are two types of compliance period, which you select from the menu:

  * Calendar period
  * Rolling window



A calendar period measures compliance over a fixed period of time, the period length. When the period ends, the error budget is reset and a new compliance period starts.

A rolling window is a sliding period. It also has a length, but the compliance is computed over the last _n_ days. When a new day starts, the compliance and remaining error budget are recomputed over the previous _n_ days.

For more on calendar and rolling-window compliance periods, see [Compliance periods](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring#compliance-period).

### Preview chart

After you have configured the SLO, the **Set your SLO** pane includes a preview chart to show you how the historical performance of this service is measured by the SLO. For example:

![The completed SLO shows a chart based on historical data.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-slo-slo-done.png)

If you have just created or deployed a service, there may not be any data yet. You can still create the SLO, but you won't get the historical perspective.

## Saving your SLO

The **Review and save** pane has a single field, a display name for the SLO. The field has a default value based on the selections you made while defining the SLO, but you can change it to make the display name more descriptive.

The pane also provides a preview of your SLO in JSON format. The JSON block summarizes your SLO and can be copied for use with the [`serviceLevelObjectives.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/create) method. If you change any of the SLO values, the JSON preview is updated automatically.

The following screenshot shows the field with a default name:

![Monitoring generates a default name for your SLO.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/svcmon-save-slo.png)

When you are satisfied with the display name, click **Create SLO**.

## What's next

After you create an SLO, you can do the following:

  * Monitor the performance of your service relative to the SLO by creating an alerting policy. For more information, see [Alerting on your burn rate](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate) and [Creating an alerting policy](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-alert).

  * View the status of all the SLOs for a set of services by creating a custom dashboard in Cloud Monitoring that displays SLO charts. For more information, see [Create a custom dashboard](https://docs.cloud.google.com/monitoring/charts/dashboards#create-custom-dashboard) and [Display SLOs on a dashboard](https://docs.cloud.google.com/monitoring/dashboards/slos).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
