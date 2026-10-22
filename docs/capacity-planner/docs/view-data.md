---
url: https://docs.cloud.google.com/capacity-planner/docs/view-data/
title: View usage and forecast data \u00a0|\u00a0 Capacity Planner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:58.416408+00:00
---

# View usage and forecast data  |  Capacity Planner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/capacity-planner/docs/view-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Capacity Planner ](https://docs.cloud.google.com/capacity-planner/docs)
  * [ Guides ](https://docs.cloud.google.com/capacity-planner/docs/overview)



Send feedback 

#  View usage and forecast data Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to view usage and forecast data for your resources in Capacity Planner. To learn more about Capacity Planner, see [Capacity Planner overview](https://docs.cloud.google.com/capacity-planner/docs/overview).

  * You can view the usage and forecast data for the following compute resources:

    * Compute Engine instances including vCPUs, memory, and Local SSD disks attached to the instances.

    * Google Cloud Hyperdisk and Persistent Disk volumes for storage, IOPS, and throughput, whether they are attached to instances or not.

    * GPUs, whether they are attached to instances or not.

    * TPUs.

You can also view your reservations, including current on-demand reservations as well as past and current future reservation requests, of compute resources.

You can use data about compute resources to help optimize your resource usage and plan for future capacity and quota needs in your project, folder, or organization.

  * You can view the usage data for Cloud Storage buckets for egress bandwidth. You can use this data to monitor when to request more bandwidth. For more information about egress bandwidth and how to request more bandwidth, see [Overview of bandwidth usage in Cloud Storage](https://docs.cloud.google.com/storage/docs/bandwidth-usage). If your requests for increasing egress bandwidth are rejected, then [contact Technical Account Management](https://cloud.google.com/tam).




In addition, you can view the forecasts made on any day during the last year. This data lets you compare how predictions for your resources have changed over time, analyze the usage trends of the resources across various percentiles, and evaluate past prediction accuracy against actual historical usage. For more information, see the View historical forecast snapshots section.

## Limitations

Before you view usage and forecast data in Capacity Planner, consider the following:

  * Forecast data isn't supported for the following resources:

    * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot) (including the instances and any attached resources, such as GPUs and TPUs)
    * Cloud Storage buckets
  * Usage data for Spot VMs and preemptible quota is only available for instances, GPUs, and TPUs. To view this data, use one of the following methods: 

    * In the Google Cloud console, open one of the following graphs:

      * **Usage and forecast by machine family**
      * **Usage and forecast by GPU type**
      * **Usage and forecast by TPU type**

Click tune **More options** , and then click the **Spot usage** toggle to the on position.

    * In the Capacity Planner API, set the `isSpot` field to `true`.

  * The **Usage and forecast by resource type** graph has the following limitations:

    * You can only view quota for your compute instances, GPUs, or TPUs when you do all of the following:

      * You view usage and forecast data in your project.

      * You filter the graph by a single machine family, GPU type, or TPU type.

      * For instances and GPUs, you filter the graph by region. For TPUs, to view quota for Google Kubernetes Engine, filter the graph by region; to view quota for Cloud TPU, filter by zone.

    * You can only view reservations and future reservation requests when you do both of the following:

      * You view usage and forecast data for instances or GPUs.

      * You view usage and forecast data in the project where you created the reservations, the folder containing this project, or your organization.

  * You can only view the **Usage and forecast by machine types** table when you view usage and forecast data for instances or GPUs.

  * Historical forecast snapshots are available for only Compute Engine instances, Hyperdisk and Persistent Disk volumes, GPUs, and TPUs. To view this data for a resource, use one of the following methods:

    * In the Google Cloud console, follow the steps mentioned in the View historical forecast snapshots section.

    * In the Capacity Planner API, use the `startDate`, `endDate`, and `generationDate` fields to specify the required date and time in `ISO 8601` format (`YYYY-MM-DDTHH:MM:SS.sssZ`). These fields let you filter and view specific historical forecast data.

For example, consider that you specify the `startDate` as `2025-06-03T00:00:00.000Z`, the `endDate` as `2025-10-02T00:00:00.000Z`, and the `generationDate` as `2025-05-04T00:00:00.000Z`. The API retrieves the forecast snapshot that was calculated on May 4, 2025 and shows the past forecast data starting from June 3, 2025 until October 2, 2025.

**Note** : If you don't specify a date for the `generationDate` field, then the API retrieves the most recently generated forecast snapshot.




For more information, see the Data availability and updates section.

## Before you begin

If you haven't used Capacity Planner before, review [Capacity Planner overview](https://docs.cloud.google.com/capacity-planner/docs/overview) and enable Capacity Planner by completing the [prerequisites for projects and users](https://docs.cloud.google.com/capacity-planner/docs/overview#prerequisites).

### Required roles

To get the permissions that you need to view the usage and forecast data of your resources, ask your administrator to grant you the [Capacity Planner Usage Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.viewer) (`roles/capacityplanner.viewer`) IAM role on your project, folder, or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view the usage and forecast data of your resources. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view the usage and forecast data of your resources:

  * To view forecast data: `capacityplanner.forecasts.list` on the project, folder, or organization 
  * To view historical usage data: `capacityplanner.usageHistories.list` on the project, folder, or organization 
  * To summarize the historical usage data: `capacityplanner.usageHistories.summarize` on the project, folder, or organization 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Data availability and updates

When you view usage and forecast data in Capacity Planner, consider the following:

  * Capacity Planner data is available as follows:

    * **Historical usage data** : historical usage data is available for up to the past two years with the following exceptions:

      * For future reservation requests, usage data is only available for up to one year after the start of its reservation period.

      * For Cloud Storage buckets, historical usage data isn't available before December 1, 2025.

    * **Forecast data** : you can view forecast data up to six months in the future.

    * **Historical forecast snapshot data** : you can view historical forecast snapshot data for up to one year in the past.

  * Capacity Planner data is updated as follows:

    * Capacity Planner samples historical usage data every five minutes and displays the data within 24 hours after usage.

    * On the **Overview** Google Cloud console page, data in the **Insights** section updates at least once every 48 hours.




## View the forecast and usage of your resources

View the usage and forecast data about the compute instances, Persistent Disk volumes, GPUs, and TPUs in your project, folder, or organization by using the following methods:

  * View the forecast and usage of your resources using the Google Cloud console (Recommended)
  * View the forecast and usage of your resources using the Capacity Planner API



### View the forecast and usage of your resources using the Google Cloud console

To view the forecast and usage of your resources using the Google Cloud console, complete the following steps.

  1. In the Google Cloud console, open Capacity Planner.

[Go to Capacity Planner](https://console.cloud.google.com/capacity/overview)

The **Overview** page appears.

  2. Optional: To change the scope (project, folder, or organization) that you want to view data for, do the following:

     1. On the Google Cloud console toolbar, click the resource selector.
     2. In the **Select a resource** dialog that appears, select a project, folder, or organization.
  3. On the **Overview** page, you can view data that summarizes overall resource usage, including potential action items and the regional distribution of your resources as follows:

     * The **Insights** section summarizes overall resource usage and highlights data that indicates potential action items.

For example, the **Active regions** metric shows the total number of regions that your project, folder, or organization has resources in; this metric might help you understand the overall size and growth of your workloads. Additionally, the **Fastest growing resource** metric shows the resource with the largest positive [percent change](https://en.wikipedia.org/wiki/Relative_change#Percentage_change) in usage in the last 30 days compared to the 30 days before that. 

     * The **Region and resource distribution** chart shows the number of resources that you have in each region for each resource type in the last 30 days. To filter the chart, use the **Resource** list and then the **Resource type** list to select a resource metric. 

Notably, this chart doesn't include Spot VMs usage. Additionally, if there are more than 5 regions for the selected resource metric in the last 30 days, then only the top 5 regions for the metric are listed, and the remaining regions specified as **Other**.

  4. To view usage and forecast data for specific types of resources in specific regions and zones, review the pages in the **Usage & forecast** section as follows: 

     1. In the **Usage & forecast** section of the Capacity Planner navigation menu, select a page based on the type of resource that you want to view data for:

        * To view data for instances, open the **Virtual machine** page.

        * To view data for Hyperdisk and Persistent Disk volumes, open the **Disk** page.

        * To view data for GPUs, open the **GPU** page.

        * To view data for TPUs, open the **TPU** page.

        * To view data for Cloud Storage buckets, open the **Cloud Storage** page.

     2. To learn about the tables and graphs on the **Usage & forecast** pages, see the following sections:

        * Usage and forecast by resource type
        * Usage and forecast by machine types (**Virtual machine** and **GPU** pages only)



#### Usage and forecast by resource type

When you view the **Usage & forecast** pages, the graph that you see depends on which resource you're viewing. For all of the following graphs, you can also show or hide data in the graph.

  * **Usage and forecast by machine family** or **Usage and forecast by machine type** : on the **Virtual machine** page, this graph shows the usage, forecast, reservations (if any), and quota of the Local SSD disks, memory, or vCPUs of your instances, filtered by the following:

    * Machine family or machine type
    * Location

By default, the graph shows the machine family and region with the highest usage in the last 30 days. You can also show or hide data for reservations and Spot VMs.

  * **Usage and forecast by disk type** : on the **Disk** page, this graph shows the history, forecast, and quota for your Hyperdisk and Persistent Disk volumes, filtered by the following:

    * Disk type
    * Confidentiality mode, which only appears if you use confidential mode for Hyperdisk balanced
    * Location
    * Resource type, which is one of the following: 
      * Storage
      * IOPS
      * Throughput
  * **Usage and forecast by GPU type** : on the **GPU** page, this graph shows the usage, forecast, reservations (if any), and quota for your GPUs, filtered by the following:

    * GPU type or machine type
    * Location

You can also show or hide data for reservations and Spot VMs.

  * **Usage and forecast by TPU type** : on the **TPU** page, this graph shows the usage, forecast, and quota for your TPUs, filtered by TPU type and location.

  * **Egress bandwidth usage by bucket traffic attributes** : on the **Cloud Storage** page, this graph shows the egress bandwidth, filtered by the following:

    * Traffic path, which is one of the following: 
      * Google
      * Internet
    * Bucket location type, which is one of the following: 
      * Single-region
      * Dual-region
      * Multi-region
    * Bucket location
    * Serving location



If you are viewing usage and forecast data of a resource in your project, and your project has sufficient usage data, the **Enable quota adjuster** button appears in a graph. You can click it to [enable the quota adjuster in your project](https://docs.cloud.google.com/capacity-planner/docs/enable-quota-adjuster).

##### Show or hide data in a graph

To show or hide options in a graph, click tune **More options** , and then click the respective toggles to the on or off position. Capacity Planner updates the calculated future reservations data every 60 minutes.

For example, for instructions on how to view Spot VMs usage and preemptible quota, see the limitation for Spot VMs.

##### View historical forecast snapshots

You can view historical forecast snapshots to compare the past predictions of your resources with their actual usage or current forecasts. This data lets you evaluate forecast accuracy and understand how usage trends have evolved over time.

To view the historical forecast snapshot of a resource, do the following:

  1. In the Google Cloud console, go to the **Capacity Planner Overview** page.

[Go to Capacity Planner](https://console.cloud.google.com/capacity/overview)

  2. In the **Usage & forecast** section of the Capacity Planner navigation menu, select one of the following resource types:

     * **Virtual Machines**
     * **Disk**
     * **GPU**
     * **TPU**
  3. On the **Usage and forecast** chart of the resource, click **Forecast Options** and then follow these steps:

     1. Click the **Show Historical Forecast on chart** toggle to the on position.

     2. Select a date from the past, up to one year before the current date.

     3. Select a percentile, or a combination of percentiles, for which you want to view the forecast snapshot data.

     4. Click **Apply**.




The chart shows the past forecast data that was generated from the selected date until the next six months, overlaid against the actual historical usage. For example, if you select the date as `June 3, 2025`, the chart shows the historical forecast data from June 3, 2025 until December 2, 2025.

#### Usage and forecast by machine types

When you view the **Virtual Machines** page or **GPUs** page, the **Usage and forecast by machine types** table shows historical and forecasted usage for the following resources:

  * When you view the usage data of your compute instances, the table shows the forecasted usage for a selected machine family and location. This table doesn't include Spot VMs usage.

  * When you view the usage data of your GPUs, the table shows the forecasted usage for a selected GPU type and location.




Capacity Planner presents data as follows:

  * At the 50th, 75th, or 99th percentile.

  * Broken down by individual machine type and zone.

  * Filtered by instances, CPU cores (if applicable), or GPUs (if applicable).




The table includes the following columns:

  * **Machine type** : the details of each machine type in the selected machine family, including vCPUs, memory, attached Local SSD disks (if any), and GPU type (if any).

  * **Zone** : the zone where each machine type is located.

  * **Max of NTH percentile RESOURCE usage**: the maximum number of instances that used each machine type, calculated using your selected percentile.

  * **Max of NTH forecast MONTH**: the maximum number of instances that are expected to use each machine type in a specific month, calculated using your selected percentile. The table contains a separate column for up to six months in the future.

  * **Reservations** : the existing reservations, as well as past and existing future reservation requests. The table shows the data broken down by machine type and zone, and calculated using your selected percentile. If there are reservations or future reservation requests for a specific machine type and zone, click **the Details button**. A pane appears showing the following:

    * In the **Usage by CPU platform** section, the percentage breakdown of minimum CPU platforms for that machine type and zone.

    * In the **VM forecast for date range** section, the forecast number of instances over your selected date range for the selected percentile usage.

    * In the **Reservations by CPU platform** section, the existing reservations and future reservation requests grouped by CPU platform.




Except for the percentage breakdown by machine type, Capacity Planner rounds all values to the nearest whole number.

By default, the table shows the 99th percentile usage and a prediction interval of 50% for the most used machine type in the most active location over the past 30 days. To view the future reservation requests during your chosen forecast dates, click **Future reservations in forecast range**.

### View the forecast and usage of your resources using the Capacity Planner API

To view the forecast and usage of your resources using the Capacity Planner API, make a request to one or more of the REST methods in the following table. These methods are helpful when you want to query data programmatically. For more information about the available data, also see View the forecast and usage of your resources using the Google Cloud console.

REST methods  
---  
Query historical usage timeseries | 

  * project-level query: [v1beta `projects.locations.usageHistories.query` method](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/projects.locations.usageHistories/query)
  * folder-level query: [v1beta `folders.locations.usageHistories.query` method](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/folders.locations.usageHistories/query)
  * organization-level query: [v1beta `organizations.locations.usageHistories.query` method](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/organizations.locations.usageHistories/query)

  
Query forecast timeseries | 

  * project-level query: [v1beta `projects.locations.forecasts.query` method](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/projects.locations.forecasts/query)
  * folder-level query: [v1beta `folders.locations.forecasts.query` method](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/folders.locations.forecasts/query)
  * organization-level query: [v1beta `organizations.locations.forecasts.query` method](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/organizations.locations.forecasts/query)

  
Query reservations timeseries | 

  * project-level query: [v1beta `projects.locations.reservations.query` method](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/projects.locations.reservations/query)
  * folder-level query: [v1beta `folders.locations.reservations.query` method](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/folders.locations.reservations/query)
  * organization-level query: [v1beta `organizations.locations.reservations.query` method](https://docs.cloud.google.com/capacity-planner/docs/reference/rest/v1beta/organizations.locations.reservations/query)

  
  
## What's next

  * [Export usage and forecast data](https://docs.cloud.google.com/capacity-planner/docs/export-data)

  * [Enable the quota adjuster](https://docs.cloud.google.com/capacity-planner/docs/enable-quota-adjuster)

  * [Request capacity from actual or forecasted usage](https://docs.cloud.google.com/capacity-planner/docs/choose-request-method)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
