---
url: https://docs.cloud.google.com/compute/docs/disks/monitor-pool-performance/
title: Monitor Hyperdisk pools \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:20.952023+00:00
---

# Monitor Hyperdisk pools  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/monitor-pool-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Monitor Hyperdisk pools Stay organized with collections  Save and categorize content based on your preferences. 

To monitor a Hyperdisk pool's usage, review the metrics that Compute Engine provides. This document discusses how to view metrics for pools, including Hyperdisk Exapools and Hyperdisk Storage Pools.

Metrics provide information to help you perform tasks like the following:

  * Understand how much of the pool's capacity and performance has been allocated to the disks in the pool.
  * Understand how much of the allocated capacity and performance is being used by the disks (available if your pool uses advanced provisioning).
  * Determine if you need to increase or decrease the pool's provisioned IOPS, throughput, or capacity.
  * Enable notifications when certain conditions are met. For example, if the pool's utilized capacity reaches a specific value, you can use metrics to create alerts.



## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles and permissions

To get the permissions that you need to view metrics for a pool, ask your administrator to grant you the following IAM roles on the project: 

  * [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`)
  * To modify a metric's scope, you need the following role for the scoping project and each resource container that you want to add: [Monitoring Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.admin) (`roles/monitoring.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Retrieve and visualize metrics

You can view prebuilt charts and create custom charts of your pool metrics in the Google Cloud console, or in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).

You can programmatically retrieve and calculate pool metrics using any of the following methods:

  * [REST](https://docs.cloud.google.com/monitoring/api)
  * [Client libraries](https://docs.cloud.google.com/monitoring/docs/reference/libraries)
  * [Promethus Query Language (PromQL)](https://docs.cloud.google.com/monitoring/promql)



For a full list of pool metrics, see [Available metrics for Hyperdisk pools](https://docs.cloud.google.com/compute/docs/disks/pool-metrics).

## Prebuilt charts

You can view prebuilt charts of a pool's characteristics and performance from the pool's **Details** page in the Google Cloud console. The available charts depend on the type of pool.

To visualize a metric that isn't listed in the table, follow the steps in Create custom charts of pool metrics.

Prebuilt charts for Hyperdisk pools  
---  
Chart | Storage Pools | Exapools  
Provisioned capacity |  |   
Capacity utilization |  |   
Total disk provisioned capacity |  |   
Overprovisioning for capacity |  |   
Used capacity |  | **—**  
Provisioned IOPS and throughput |  |   
IOPS utilization and throughput utilization |  |   
Total disk provisioned IOPS and throughput |  |   
Overprovisioning for IOPS and throughput (%) |  |   
Used IOPS and throughput |  | **—**  
Used read IOPS and used read throughput | **—** |   
Used write IOPS and used write throughput | **—** |   
  
For descriptions of each metric, see [Available metrics for Hyperdisk pools](https://docs.cloud.google.com/compute/docs/disks/pool-metrics).

To visualize a metric that isn't listed, follow the steps in Create custom charts of pool metrics.

### View prebuilt charts in the Google Cloud console

To view the prebuilt charts for pool metrics in the Google Cloud console, complete the following steps.

  1. In the Google Cloud console, go to the **Storage pools** page.

[Go to the Storage pools page](https://console.cloud.google.com/compute/storagePools)

  2. Select the tab for **Exapools** or **Storage Pools**.

  3. Click the name of the pool to open the **Details** page.

  4. To view the prebuilt graphs for a pool, click the **Monitoring tab**.

  5. Optional: Reset the one hour default period to the period you want to monitor, by choosing one of the following options:

     * 6 hours
     * 1 day
     * 1 week
     * 1 month
     * 6 weeks
     * Custom date or time range



## Customize the monitoring dashboard

Use the following instructions to modify the graphs shown on the dashboard for a Hyperdisk pools.

  1. In the Google Cloud console, go to the **Storage pools** page.

[Go to the Storage pools page](https://console.cloud.google.com/compute/storagePools)

  2. Select the tab for **Exapools** or **Storage Pools**.

  3. Click the name of a storage pool to open the **Details** page.

  4. Click the **Monitoring tab** of the **Manage storage pool** page for a specific pool.

  5. In the list of charts that appear, find the chart with the metric that you want to review.

     * To change a prebuilt chart, click query_stats **Explore data**.

This opens an **Explore** page, where you can create a customized monitoring chart or table. For information about how to create a chart for a specific metric, see [Chart a single metric type](https://docs.cloud.google.com/monitoring/charts/metrics-explorer#find-me). After you create a custom graph or table, you can save the result to a new or existing custom dashboard.

For more information about custom dashboards, see [View and customize Google Cloud dashboards](https://docs.cloud.google.com/monitoring/charts/predefined-dashboards).

     * To add a prebuilt chart to a custom dashboard, click more_vert**More chart options** , then click **Add to custom dashboard**.

  6. To learn how to further customize your dashboard, see [View and customize Google Cloud dashboards](https://docs.cloud.google.com/monitoring/charts/predefined-dashboards).




## Create custom charts of pool metrics

If there is no prebuilt chart for a metric or for more complex analysis, you can create your own charts in Metrics Explorer. Metrics Explorer lets you visualize and analyze any of the pool metrics listed in [List of available metrics](https://docs.cloud.google.com/compute/docs/disks/pool-metrics). You can create graphs in the Google Cloud console or using PromQL.

### Example: Visualize Hyperdisk Storage Pools capacity utilization

To visualize a Storage Pools's used capacity with a chart, complete the following steps. You can follow the same procedure for any other metric. 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `Storage pool` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **Storage pool**.
     2. In the **Active metric categories** menu, select **Storage_pool**.
     3. In the **Active metrics** menu, select **Used Capacity**. 
     4. Click **Apply**.
The fully qualified name for this metric is `compute.googleapis.com/storage_pool/used_capacity`. 
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. Configure how the data is viewed. To display only the metrics for a specific pool, follow these steps: 
     * In the **Filter** element, click **Add filter** , and then select **storage_pool_id**. For the value, enter a specific pool ID.
     * In the **Aggregation** entry, set the first menu to **Unaggregated** and the second menu to **storage_pool_id**.

For more information about configuring a chart, see [Select metrics when using Metrics Explorer.](https://docs.cloud.google.com/monitoring/charts/metrics-selector)




## Set up alerts for metrics

Use the following instructions to create an alert for the metric data shown on the Storage Pool dashboard.

  1. In the Google Cloud console, go to the **Storage pools** page.

[Go to the Storage pools page](https://console.cloud.google.com/compute/storagePools)

  2. Select the tab for **Exapools** or **Storage Pools**.

  3. Click the name of a storage pool to open the **Details** page.

  4. Click the **Monitoring tab** of the **Manage storage pool** page for a specific pool.

  5. Click **Create alerting policy**.

The **Create alerting policy** page appears. Configure the parameters for the alerting policy. For information about how to configure an alerting policy, see [Create alerting policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#create-policy).




## What's next

  * Monitor performance for individual disks by [reviewing disk performance metrics](https://docs.cloud.google.com/compute/docs/disks/review-disk-metrics) and [monitoring disk health](https://docs.cloud.google.com/compute/docs/disks/disk-health).
  * Learn more about [creating charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
