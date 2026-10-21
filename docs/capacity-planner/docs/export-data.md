---
url: https://docs.cloud.google.com/capacity-planner/docs/export-data/
title: Export data to your local workstation \u00a0|\u00a0 Capacity Planner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:38:52.791555+00:00
---

# Export data to your local workstation  |  Capacity Planner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/capacity-planner/docs/export-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Capacity Planner ](https://docs.cloud.google.com/capacity-planner/docs)
  * [ Guides ](https://docs.cloud.google.com/capacity-planner/docs/overview)



Send feedback 

#  Export data to your local workstation Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to export a CSV file containing the usage and forecast data of your resources in your project, folder, or organization. To export this data to a different Google Cloud product, see instead [Export data to a Cloud Storage bucket or BigQuery table](https://docs.cloud.google.com/capacity-planner/docs/export-data-api).

You can export data from Capacity Planner as a CSV file for the following resources:

  * Compute Engine instances

  * Persistent Disk and Hyperdisk volumes

  * GPUs

  * TPUs

  * Reservations

  * Cloud Storage buckets




To learn more about the data that's available from Capacity Planner, data limitations, and how you can use this data, see [View usage and forecast data](https://docs.cloud.google.com/capacity-planner/docs/view-data).

## Before you begin

If you haven't used Capacity Planner before, review [Capacity Planner overview](https://docs.cloud.google.com/capacity-planner/docs/overview) and enable Capacity Planner by completing the [prerequisites for projects and users](https://docs.cloud.google.com/capacity-planner/docs/overview#prerequisites).

### Required roles

To get the permissions that you need to export usage and forecast data of your resources, ask your administrator to grant you the following IAM roles on your project, folder, or organization: 

  * To access and view Capacity Planner: [Capacity Planner Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/capacityplanner#capacityplanner.viewer) (`roles/capacityplanner.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to export usage and forecast data of your resources. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to export usage and forecast data of your resources:

  * To view forecasted usage data: `capacityplanner.forecasts.list` on the project, folder, or organization 
  * To view historical usage data: `capacityplanner.usageHistories.list` on the project, folder, or organization 
  * To summarize the usage of your resources: `capacityplanner.usageHistories.summarize` on the project, folder, or organization 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Export usage and forecast data

Based on the usage and forecast data of the resources within your project, folder, or organization that you want to export, use one of the following methods:

  * To export usage and forecast data of your compute instances, Persistent Disk volumes, GPUs, or TPUs for the past two years and for up to six months in the future, export data by resource type.

  * To export usage and forecast data of your machine types for a specific usage period, export data filtered by machine family or GPU type.




### Export data by resource type

You can export usage and forecast data about your compute instances, Persistent Disk volumes, GPUs, or TPUs from the [**Usage and forecast by resource type** graph](https://docs.cloud.google.com/capacity-planner/docs/view-data#usage-forecast). You can export usage data from within two years in the past, and forecast data for up to six months in the future. To export data, first select the page for the resource that you want to export, and then filter the data by the following:

  * Resource type

  * Region or zone

  * Usage percentile




To export usage and forecast data about your instances, Persistent Disk volumes, GPUs, or TPUs, do the following:

  1. In the Google Cloud console, open Capacity Planner.

[Go to Capacity Planner](https://console.cloud.google.com/capacity/overview)

The **Overview** page appears.

  2. Optional: To change the scope (project, folder, or organization) that you want to export data for, do the following:

     1. On the Google Cloud console toolbar, click the resource selector.
     2. In the **Select a resource** dialog that appears, select a project, folder, or organization.
  3. To export a specific resource, select one of the following options:

###  Compute instances 

     1. In the **Usage & forecast** section of the Capacity Planner navigation menu, click to open the **Virtual machine** page.

     2. For **Machine family** , choose the machine family to export. To export all, select **All**.

     3. For **Machine type** , choose the machine type to export. To export all machine types within a machine family, select **Select**.

     4. For **Location** , select the region or zone of the instances to export.

     5. For **Usage percentile** , select a usage percentile.

     6. In the **Usage and forecast by machine family** or **Usage and forecast by machine types** graph, click file_download **Export**.

A CSV file downloads to your workstation.

###  Persistent Disks 

     1. In the **Usage & forecast** section of the Capacity Planner navigation menu, click to open the **Disk** page.

     2. For **Disk type** , choose the type of Persistent Disk to export.

     3. For **Location** , select a region or zone.

     4. For **Usage percentile** , select a usage percentile.

     5. In the **Usage and forecast by disk type** graph, click file_download **Export**.

A CSV file downloads to your workstation.

###  GPUs 

     1. In the **Usage & forecast** section of the Capacity Planner navigation menu, click to open the **GPU** page.

     2. For **GPU type** , choose the type of GPU to export. To export all, select **All**.

     3. For **Machine type** , choose the machine type that have your chosen GPU attached to export. To export all machine types that have a specific GPU type attached, select **Select**.

     4. For **Usage percentile** , select a usage percentile.

     5. In the **Usage and forecast by GPU type** or **Usage and forecast by machine types** graph, click file_download **Export**.

A CSV file downloads to your workstation.

###  TPUs 

     1. In the **Usage & forecast** section of the Capacity Planner navigation menu, click to open the **TPU** page.

     2. For **TPU type** , choose the type of TPU to export. To export all, select **All**.

     3. For **Usage percentile** , select a usage percentile.

     4. In the **Usage and forecast by TPU type** or **Usage and forecast by machine types** graph, click file_download **Export**.

A CSV file downloads to your workstation.




### Export data filtered by machine family or GPU type

You can export usage and forecast data of your instances from the [**Usage and forecast by machine types** table](https://docs.cloud.google.com/capacity-planner/docs/view-data#usage-machine-type). To export data, first select the resource that you want to export, and filter the data by the following:

  * Compute instances, CPU cores, or GPUs

  * Region or zone

  * Usage percentile




To export usage and forecast data of your instances filtered by machine family or GPU type, do the following:

  1. In the Google Cloud console, open Capacity Planner.

[Go to Capacity Planner](https://console.cloud.google.com/capacity/overview)

The **Overview** page appears.

  2. Optional: To change the scope (project, folder, or organization) that you want to export data for, do the following:

     1. On the Google Cloud console toolbar, click the resource selector.
     2. In the **Select a resource** dialog that appears, select a project, folder, or organization.
  3. To filter the usage data of your instances by machine family or GPU type, select one of the following options:

###  Compute instances 

     1. In the **Usage & forecast** section of the Capacity Planner navigation menu, click to open the **Virtual machine** page.

     2. For **Machine family** , select one of the following options:

        * To select a single machine family only, select one of the available machine families.

        * To select all machine families, select **All**.

     3. For **Location** , select a region or zone.

     4. For **Usage percentile** , select a usage percentile.

     5. In the **Usage and forecast by machine types** table, for **View data for** , select one of the following options:

        * To view usage and forecast by instances, select **VM**.

        * To view usage and forecast by CPU cores, select **Cores**.

     6. For **History start date** , select the start date of the usage period.

     7. For **History end date** , select the end date of the usage period.

     8. Click file_download **Export**.

A CSV file downloads to your workstation.

###  GPUs 

     1. In the **Usage & forecast** section of the Capacity Planner navigation menu, click to open the **GPU** page.

     2. For **GPU type** , select one of the following options:

        * To select a single GPU type only, select one of the available GPU types.

        * To select all GPU types, select **All**.

     3. For **Location** , select a region or zone.

     4. For **Usage percentile** , select a usage percentile.

     5. In the **Usage and forecast by machine types** table, for **View data for** , select one of the following options:

        * To view usage and forecast by instances, select **VM**.

        * To view usage and forecast by GPUs, select **GPU**.

     6. For **History start date** , select the start date of the usage period.

     7. For **History end date** , select the end date of the usage period.

     8. Click file_download **Export**.

A CSV file downloads to your workstation.




## What's next

  * [Audit logging information for Capacity Planner](https://docs.cloud.google.com/capacity-planner/docs/audit-logging)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
