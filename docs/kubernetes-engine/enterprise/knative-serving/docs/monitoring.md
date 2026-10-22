---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/monitoring/
title: Monitoring health and performance \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:42.649396+00:00
---

# Monitoring health and performance  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Monitoring health and performance Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Knative serving uses [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs), which provides performance monitoring, [metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-run), [uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks), and threshold based [alerts](https://docs.cloud.google.com/monitoring/alerts). You can also set up and use [Cloud Monitoring custom metrics](https://docs.cloud.google.com/monitoring/custom-metrics). [Google Cloud Observability pricing](https://cloud.google.com/stackdriver/pricing) applies.

For clusters on Google Cloud, Knative serving is automatically integrated with Cloud Monitoring without additional configuration. This means that the metrics for your Knative serving services are captured automatically when they are running.

For other clusters, you must first enable metrics by [configuring your `CloudRun` custom resource](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/outside-gcp#configure_your_cloudrun_custom_resource).

You can view metrics either in Cloud Monitoring or in the Knative serving page in the console. Cloud Monitoring provides more charting and filtering options.

## Resource types

The monitoring resource name for Knative serving is _Knative serving Revision_ (`knative_revision`) .

## Viewing metrics in Knative serving

To view metrics in Knative serving:

  1. Go to Knative serving in the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Locate the service in the services list, and click on it.

  3. Click the _Metrics_ tab to show the metrics for that revision.




## Viewing metrics in Cloud Monitoring

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `Knative serving Revision` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **Knative serving Revision**.
     2. To select a metric, use the **Active metric categories** and **Active metrics** menus. For a full description of the available metrics, see: 
        * [Monitoring Knative metrics](https://docs.cloud.google.com/monitoring/api/metrics_knative)
        * [Monitoring Kubernetes metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes) pages.
     3. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. To combine time series, use the menus on the [**Aggregation** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#select_display). For example, to display the CPU utilization for your VMs, based on their zone, set the first menu to **Mean** and the second menu to **zone**.

All time series are displayed when the first menu of the **Aggregation** element is set to **Unaggregated**. The default settings for the **Aggregation** element are determined by the metric type you selected.

  6. For quota and other metrics that report one sample per day, do the following: 
     1. In the **Display** pane, set the **Widget type** to **Stacked bar chart**.
     2. Set the time period to at least one week.

**Note:** Some of the metrics listed show a sample interval of only once every 60 seconds. This means that if the underlying value of the metric changes more than once in 60 seconds, only one of the underlying values will be reported to Monitoring.

## Adding Uptime checks

You can use Cloud Monitoring to keep track of your services' performance. For more information, see [Verify availability of your service](https://docs.cloud.google.com/monitoring/uptime-checks)(uptime checks).

## Adding Alerts

You can use Cloud Monitoring to send notification about certain events, such as uptime check failures. For more information, see [Create and manage alerting policies](https://docs.cloud.google.com/monitoring/alerts) for your service. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
