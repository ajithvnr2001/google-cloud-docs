---
url: https://docs.cloud.google.com/capacity-planner/docs/release-notes/
title: Capacity Planner release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:13:13.166664+00:00
---

# Capacity Planner release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/capacity-planner/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Capacity Planner ](https://docs.cloud.google.com/capacity-planner/docs)
  * [ Resources ](https://docs.cloud.google.com/capacity-planner/docs/resources)



Send feedback 

#  Capacity Planner release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Capacity Planner. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

## September 30, 2026

Feature

**Preview** : You can use Capacity Assist, which provides AI-powered assistance through Gemini in Capacity Planner, to help you understand and manage your resource usage and plan capacity ([Preview](https://cloud.google.com/products#product-launch-stages)). You can use natural-language prompts in Capacity Assist to do the following:

  * Analyze historical usage patterns across regions and resources.
  * Forecast capacity needs and identify quota risks early.
  * Simulate growth events to plan future capacity.
  * Get answers to your Capacity Planner questions.



For more information, see [Plan capacity with Capacity Assist](https://docs.cloud.google.com/capacity-planner/docs/capacity-assist).

## March 05, 2026

Feature

**Preview** : You can use Capacity Planner to view historical forecast snapshots from any day over the last one year for your Compute Engine instances, Google Cloud Hyperdisk and Persistent Disk volumes, GPUs, and TPUs. This feature lets you compare how past predictions have changed over time and contrast them with actual usage or current forecasts. You can use this data to evaluate forecast accuracy and better understand how usage trends have evolved.

For more information, see [View usage and forecast data](https://docs.cloud.google.com/capacity-planner/docs/view-data).

## February 06, 2026

Feature

**Preview** : Capacity Planner supports the following:

  * Usage data for the egress bandwidth of Cloud Storage buckets, which can help you monitor when to request more bandwidth.
  * Usage data for GPUs attached to Spot VMs, which can help you optimize your resource usage and plan for future capacity and quota needs.



For more information, see [View usage and forecast data](https://docs.cloud.google.com/capacity-planner/docs/view-data).

## January 05, 2026

Feature

**Preview** : You can use client libraries to access the Capacity Planner API using C#, Go, Java, Node.js, PHP, Python, or Ruby. For more information, see [Capacity Planner client libraries](https://docs.cloud.google.com/capacity-planner/docs/reference/libraries).

## December 09, 2025

Change

The Google Cloud console has been changed as follows:

  * An **Overview** page for Capacity Planner has been added. You can use the **Overview** page to view data that summarizes the overall resource usage for a project, folder, or organization, including potential action items and the regional distribution of your resources.

  * The data for the region distribution of your resources has been relocated: the doughnut charts have been replaced with a bar chart on the **Overview** page for Capacity Planner.




For more information, see [View usage and forecast data](https://docs.cloud.google.com/capacity-planner/docs/view-data).

## October 03, 2025

Feature

**Preview:** Capacity Planner supports the following:

  * Usage and forecast data for Hyperdisk volumes
  * Usage and forecast data for Persistent Disk and Hyperdisk volume IOPS and throughput
  * Usage data for Spot VMs and TPUs that are attached to Spot VMs



For more information, see [View usage and forecast data](https://docs.cloud.google.com/capacity-planner/docs/view-data).

## August 29, 2025

Announcement

[Capacity Planner](https://cloud.google.com/capacity-planner/docs/overview) is available in [Preview](https://cloud.google.com/products#product-launch-stages)!

Feature

Reference documentation has been added for the REST Capacity Planner API. For more information, see [Authenticate to Capacity Planner](https://cloud.google.com/capacity-planner/docs/authentication) and the [REST API reference overview](https://cloud.google.com/capacity-planner/docs/reference/rest).

## August 25, 2025

Feature

**Preview** : You can use capacity requests to request a large number of resources for a future date and time, and across multiple regions or zones. When you use capacity requests, you get best-effort assurance for the capacity that Google Cloud provisions, and you only pay for resources when you use them. This approach helps ensure that your Google Cloud project has sufficient capacity to prevent resource availability errors during unexpected growth, without committing to pay for resources that you might not use.

For more information, see [About capacity requests](https://cloud.google.com/capacity-planner/docs/about-capacity-requests).

## May 23, 2025

Feature

**Preview** : You can view and export usage and forecast data of the machine types and TPUs in your project, folder, or organization. This information helps you analyze usage trends and plan for future capacity needs. For more information, see the following:

  * [Capacity Planner overview](https://cloud.google.com/capacity-planner/docs/overview)

  * [View usage and forecast data in Capacity Planner](https://cloud.google.com/capacity-planner/docs/view-data)

  * [Export usage and forecast with the Google Cloud console](https://cloud.google.com/capacity-planner/docs/export-data)

  * [Export usage and forecast with the Capacity Planner API](https://cloud.google.com/capacity-planner/docs/export-data-api)

  * [Reserve capacity in Capacity Planner](https://cloud.google.com/capacity-planner/docs/reserve-capacity)




## December 19, 2024

Feature

**Preview** : You can create future reservation requests for VMs of a single machine type using the Google Cloud console. Reserving capacity based on your predicted VM or GPU usage helps ensure that your projects have the capacity needed to support increases in usage. For more information, see [Reserve capacity in Capacity Planner](https://cloud.google.com/capacity-planner/docs/reserve-capacity).

## November 15, 2024

Feature

**Preview** : You can view and export historical utilization of on-demand and future reservations in your project, folder, or organization. This data helps you analyze usage trends for your VMs or GPUs, as well as plan for future capacity needs. For more information, see the following: 

  * [Export usage and forecast with the Google Cloud console](https://docs.cloud.google.com/capacity-planner/docs/export-data)

  * [Export usage and forecast with the Capacity Planner API](https://docs.cloud.google.com/capacity-planner/docs/export-data-api)

  * [View usage and forecast data in Capacity Planner](https://docs.cloud.google.com/capacity-planner/docs/view-data)




## September 05, 2024

Feature

**Preview** : You can use the Capacity Planner API to export usage and forecast data of the VMs, Persistent Disk volumes, or GPUs in your project, folder, or organization. This lets you export usage and forecast data in a Cloud Storage bucket or BigQuery table. For more information, see [Export usage and forecast data using the Capacity Planner API](https://docs.cloud.google.com/capacity-planner/docs/export-data-api).

Feature

**Preview** : You can view the on-demand reservations and future reservation requests available for consumption in your project, folder, or organization. This helps you plan for future capacity assurance, as well as view the reserved resources that cover your projected growth or peak usage. For more information, see [View usage and forecast data in Capacity Planner](https://cloud.google.com/capacity-planner/docs/view-data).

## July 29, 2024

Feature

**Preview** : Capacity planner supports the following for data aggregated by folder ID:

  * View and export the actual and forecasted usage data of the VMs, Persistent Disk volumes, and GPUs in your folder.

  * Generate gcloud CLI commands to create future reservation requests based on the actual or forecasted usage data of your VMs or GPUs by folder.




For more information, see the following pages:

  * [About Capacity Planner](https://docs.cloud.google.com/capacity-planner/docs/about)

  * [Export usage and forecast data in Capacity Planner](https://docs.cloud.google.com/capacity-planner/docs/export-data)

  * [Reserve capacity from actual or forecasted usage](https://docs.cloud.google.com/capacity-planner/docs/reserve-capacity)

  * [View actual and forecasted usage in Capacity Planner](https://docs.cloud.google.com/capacity-planner/docs/view-data)




## July 01, 2024

Feature

**Preview** : Capacity Planner displays GPU usage and forecasts of the GPUs in your Google Cloud project or organization. This is useful to plan and optimize your GPU consumption.

For more information, see the following pages:

  * [About Capacity Planner](https://cloud.google.com/capacity-planner/docs/about)

  * [Export usage and forecast data in Capacity Planner](https://cloud.google.com/capacity-planner/docs/export-data)

  * [View actual and forecasted usage in Capacity Planner](https://cloud.google.com/capacity-planner/docs/view-data)




## March 28, 2024

Feature

**Preview** : Capacity planner supports the following for data aggregated by organization ID:

  * View and export the actual and forecasted usage data of the VMs and persistent disks in your organization.

  * Generate gcloud CLI commands to create future reservation requests based on the actual or forecasted usage data of your VMs by organization.




For more information, see the following pages:

  * [About Capacity Planner](https://cloud.google.com/capacity-planner/docs/about)

  * [Export usage and forecast data in Capacity Planner](https://cloud.google.com/capacity-planner/docs/export-data)

  * [Reserve capacity from actual or forecasted usage](https://cloud.google.com/capacity-planner/docs/reserve-capacity)

  * [View actual and forecasted usage in Capacity Planner](https://cloud.google.com/capacity-planner/docs/view-data)




## December 15, 2023

Feature

**Preview** : When using Capacity Planner, you can enable quota adjuster for the Compute Engine resources in your project. This allows Google Cloud to automatically submit quota increase requests on your behalf when your quota nears a limit. 

Enabling quota adjuster is helpful to proactively respond to planned or unplanned growths in consumption, or prevent outages when reaching a quota limit. For more information, see [Enable quota adjuster](https://cloud.google.com/capacity-planner/docs/enable-quota-adjuster).

Feature

**Preview** : You can view the following when using Capacity Planner:

  * The historical or forecasted usage of your persistent disks.

  * Your quota in relation to the usage of your Compute Engine resources. 




Viewing your persistent disks' forecasted usage and your quota is useful when reserving resources or adjusting your quota limits for planned or unplanned spikes in consumption. For more information, see [About Capacity Planner](https://cloud.google.com/capacity-planner/docs/about).

## September 07, 2023

Feature

**Preview** : You can view the following when using Capacity Planner:

  * The 50th and 75th percentile usage and forecast of your VMs.

  * The historical usage of your VMs up to 2 years in the past.

  * The usage and forecast of all machine families in a project.




For more information, see [About Capacity Planner](https://cloud.google.com/capacity-planner/docs/about).

Feature

**Preview** : You can generate gcloud CLI commands to create future reservation requests of Compute Engine zonal resources based on the actual or forecasted usage of your VMs. Future reservations are useful to secure capacity up to 1 year in advance for forecasted spikes.

For more information, see [Reserve capacity from actual or forecasted usage](https://cloud.google.com/capacity-planner/docs/reserve-capacity).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
