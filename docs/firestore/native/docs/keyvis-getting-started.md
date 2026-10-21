---
url: https://docs.cloud.google.com/firestore/native/docs/keyvis-getting-started/
title: Get started with Key Visualizer \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:25:38.501369+00:00
---

# Get started with Key Visualizer  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/keyvis-getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Get started with Key Visualizer

This page describes how to use Key Visualizer to check for performance issues that are related to your Firestore usage patterns.

### Edition and mode requirements

This document applies to Firestore Standard edition in Firestore in Native mode. 

## Before you begin

To use Key Visualizer for Firestore, you must enable the Firestore Key Visualizer API.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=firestorekeyvisualizer.googleapis.com&redirect=https%3A//console.cloud.google.com)

### Required roles

Make sure that your account is granted one of the following IAM roles:

  * Cloud Datastore Owner
  * Cloud Datastore Key Visualizer Viewer
  * Editor
  * Owner



These roles include the following IAM permissions which are required to access Key Visualizer:

  * `datastore.keyVisualizerScans.get`
  * `datastore.keyVisualizerScans.list`
  * `datastore.databases.getMetadata`
  * `resourcemanager.projects.get`



You can also define a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) with the required permissions.

## Viewing a scan for a time period

Each Key Visualizer scan covers a two hour period. A scan for a given period is available for databases with traffic that exceeds 3000 document operations in any given minute in that period. 

To launch Key Visualizer:

  1. In the Google Cloud console, go to the **Databases** page.

[Go to Databases](https://console.cloud.google.com/firestore/databases)

  2. Select the required database from the list of databases.

  3. In the navigation menu, click **Key Visualizer**.

  4. Select a time span and a metric from the available Key Visualizer scans:

     1. Click the **Pencil icon** in the upper right. Select a **Date** and a **Time Span**.

Scans are available based on [scan eligibility](https://docs.cloud.google.com/firestore/native/docs/key-visualizer#scan_eligibility). You can't select time spans that did not meet scan eligibility or that are still processing. The two most recent scans of the day will take some time to process before they are available.

     2. Select **All document data** or **All index data** as the source.

     3. Click **Update**.

  5. Select a metric to analyze:

Click the metrics dropdown in the upper left and select a metric to view. Key Visualizer opens in the **Ops/s** metric for document keys and **Index Write Ops/s** metric for index keys by default.




To compare metrics or look for data correlations, you can display multiple Key Visualizer metrics together. See [Finding connections between different metrics](https://docs.cloud.google.com/firestore/native/docs/keyvis-exploring-heatmaps#finding-connections).

## Viewing an activity overview

To get an overview of activity during the selected two-hour time period, review the heatmap for the default metric.

The following example shows a heatmap where there are major differences in the usage pattern for different key ranges:

  * Ranges shown in dark colors have little or no activity.
  * Ranges in bright colors have significantly more activity.
  * The glowing white range in the middle has very high activity.



![Example of a Key Visualizer scan](https://docs.cloud.google.com/static/firestore/native/docs/images/keyvis-scan-example.png)

### Document keys scan

The **Ops/s** metric measures the number of requests per second for each key range. This metric is a sum of write, lookup, and query requests. Key Visualizer shows this metric by default when you open a heatmap.

After getting an idea of the overall activity in your database, you can continue your investigation by looking at other metrics and focusing on key ranges that might be causing problems. [Learn more](https://docs.cloud.google.com/firestore/native/docs/keyvis-exploring-heatmaps).

### Index keys scan

The **Index Write Ops/s** metric at a given cell measures the average index writes per second within the corresponding 10-second time interval and key range.

## What's next

  * Learn to recognize [common patterns in heatmaps for document keys](https://docs.cloud.google.com/firestore/native/docs/keyvis-patterns).
  * Learn to recognize [common patterns in heatmaps for index keys](https://docs.cloud.google.com/firestore/native/docs/keyvis-patterns-index).
  * Find out how to [explore a heatmap in depth](https://docs.cloud.google.com/firestore/native/docs/keyvis-exploring-heatmaps).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
