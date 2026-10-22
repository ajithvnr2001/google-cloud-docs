---
url: https://docs.cloud.google.com/compute/docs/disks/monitor-disks/
title: Monitor disk IOPS and throughput rates \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:15.465603+00:00
---

# Monitor disk IOPS and throughput rates  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/monitor-disks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Monitor disk IOPS and throughput rates Stay organized with collections  Save and categorize content based on your preferences. 

Monitoring disk performance rates provides useful information to help you find the right size and configuration of your disks. Compute Engine lets you view the average and peak IOPS and throughput rates for your disks by using the **Observability** tab in the Google Cloud console. This tab provides a predefined dashboard using [metric data](https://docs.cloud.google.com/compute/docs/disks/pool-metrics) so you can monitor your disk performance and configuration.

The **Observability** tab shows the following graphs for IOPS and throughput by default:

  * Mean Throughput (MB/s): the average throughput rate, in MB per second, for a disk over a period of time
  * Mean Operations (IOPS): the average number of I/O operations per second (IOPS) for a disk over a period of time
  * Peak Throughput (MB/s): the peak throughput rates, in MB per second, for a disk over a period of time
  * Peak Operations (IOPS): the peak number of I/O operations per second (IOPS) for a disk over a period of time



You can select the time period for the graphs on this page, using predefined values of one hour, six hours, one day, one week, one month, or six weeks. You can also specify a custom time period for the graph data. 

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




## Access the disk monitoring page for a single disk

You can view the disk monitoring page in the Google Cloud console.

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Click the name of a disk to open the **Manage disk** page.

  3. Click the **Observability** tab to display the monitoring dashboard for the disk.

  4. Optional: Reset the one hour default timeframe to the timeframe you want to monitor, by choosing one of the following options:

     * 6 hours
     * 1 day
     * 1 week
     * 1 month
     * 6 weeks
     * Custom date or time range



## Customize the disk monitoring dashboard

Use the following instructions to modify the graphs shown on the disk monitoring dashboard.

  1. Access the disk **Observability** tab.
  2. Click query_stats **Explore data**.

This opens an **Explore** page, where you can create a customized monitoring chart or table. For information about how to create a chart for a specific metric, see [Chart a single metric type](https://docs.cloud.google.com/monitoring/charts/metrics-explorer#find-me).

  3. After creating a custom graph or table, you can save the result to a new or existing custom dashboard.

For more information about custom dashboards, see [View and customize Google Cloud dashboards](https://docs.cloud.google.com/monitoring/charts/predefined-dashboards).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
