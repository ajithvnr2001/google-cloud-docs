---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-sheets/
title: View prebuilt reports in Google connected sheets \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:41.605458+00:00
---

# View prebuilt reports in Google connected sheets  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-sheets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  View prebuilt reports in Google connected sheets Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view view reports in Google connected sheets. It also explains how to download reports to a local file.

After you [set up prebuilt reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#script), if you have access to Google Workspace, you can view the results in Google connected sheets. For more information, see [Using Connected Sheets](https://docs.cloud.google.com/bigquery/docs/connected-sheets).

If you don't have access to Google Workspace, you can [view the reports in Data Studio](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-lookerstudio) or download prebuilt reports in a CSV file. For instructions, see Download prebuilt reports.

To view prebuilt reports in Google connected sheets, do the following:

  1. In the Google Cloud console, go to the **BigQuery Studio** page: 

[Go to BigQuery Studio page](https://console.cloud.google.com/)

  2. In the **Explorer** panel, click the arrow_rightexpander arrow to expand a dataset.
  3. Select a prebuilt report. For example, `Backup Jobs Summary`.
  4. From **Export** , click **Explore with sheets**.

A new tab opens in connected sheet with the report data.




## Download prebuilt reports

After you set up the prebuilt reports, you can download them to a local file. For more information, see [Downloading and saving query results from the Google Cloud console](https://docs.cloud.google.com/bigquery/docs/writing-results#downloading-saving-results-console).

To download prebuilt reports in BigQuery, do the following:

  1. In the Google Cloud console, go to the **BigQuery Studio** page: 

[Go to BigQuery Studio page](https://console.cloud.google.com/)

  2. In the **Explorer** panel, click the arrow_rightexpander arrow to expand a dataset.
  3. Select a prebuilt report. For example, `Backup Jobs Summary`.
  4. Click **Query** and select either **In new tab** or **In split tab**.

A new tab opens with a sample query.

  5. Write a query based on the field names that are populated in the **Schema** tab. For example, you can use the following query to download the entire report.
         
         SELECT * FROM `PROJECT_ID.BackupandDR_reports.Backup Jobs Summary`.
         

  6. Click **Run** to display the preview of the query results.

  7. From **Save results** , select **CSV (local file)** to download report to a local file.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
