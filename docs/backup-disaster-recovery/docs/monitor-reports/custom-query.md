---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/custom-query/
title: Custom queries in BigQuery \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:14.053171+00:00
---

# Custom queries in BigQuery  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/custom-query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Custom queries in BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to set up and view prebuilt reports in BigQuery.

In Google Cloud console, you can write your custom query based on the table name or prebuilt report and save it as a query or as a view.

## Write custom queries in BigQuery as a query

To write custom queries in BigQuery as a query, do the following:

  1. In the Google Cloud console, go to the **BigQuery Studio** page: 

[Go to BigQuery Studio page](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** panel, expand your project and select a dataset.
  3. Click the dataset name to expand it.

The tables and views in the dataset appear.

  4. Click the table name or a prebuilt report.

The **Details** tab displays the table's description and the **Schema** tab displays the table's schema definition.

  5. Click **Query** and select either **In new tab** or **In split tab**.

A new tab opens with a sample query.

  6. Write a query based on the field names that are populated in the **Schema** tab.

  7. Click **Run**. This displays the preview of the query results.

  8. Click **Save query**.

  9. In the **Save query** dialog, type a name for the saved query.




You can download and save queries to the selected location. For more information, see [Downloading and saving query results from the Google Cloud console](https://docs.cloud.google.com/bigquery/docs/writing-results#downloading-saving-results-console).

## Write custom queries in BigQuery as a view

To write custom queries in BigQuery as a view, do the following:

  1. In the Google Cloud console, go to the **BigQuery Studio** page: 

[Go to BigQuery Studio page](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** panel, expand your project and select a dataset.
  3. Click the dataset name to expand it.

The tables and views in the dataset appear.

  4. Click the table name or a prebuilt report.

The **Details** tab displays the table's description and the **Schema** tab displays the table's schema definition.

  5. Click **Query** and select either **In new tab** or **In split tab**.

A new tab opens with a sample query.

  6. Write a query based on the field names that are populated in the **Schema** tab.

  7. Click **Run**. This displays the preview of the query results.

  8. Click **Save view**.

  9. In the **Save view** dialog, do the following:

     1. In the **Project** list, click **Browse** and select a project.
     2. In the **Dataset** list, select a dataset to store the view. The dataset that contains your view and the dataset that contains the tables referenced by the view must be in the same [location](https://docs.cloud.google.com/bigquery/docs/dataset-locations).
     3. In **Table name** , enter a name for the view.
     4. Click **Save**.



You can download and save queries to the selected location. For more information, see [Downloading and saving query results from the Google Cloud console](https://docs.cloud.google.com/bigquery/docs/writing-results#downloading-saving-results-console).

## What's next

  * Learn how to [View prebuilt reports in Google connected sheets](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-sheets)
  * Learn how to [View prebuilt reports in Looker](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-lookerstudio)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
