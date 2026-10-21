---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-lookerstudio/
title: View Data Studio prebuilt reports in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:46.057552+00:00
---

# View Data Studio prebuilt reports in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-lookerstudio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  View Data Studio prebuilt reports in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view Backup and DR reports in Data Studio.

After you [set up prebuilt reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#script) in BigQuery, you can view them in Data Studio. Data Studio is a cloud-based business intelligence and data visualization tool that lets you view, modify, and create reports and dashboards.

You can use the Data Studio template to connect to your BigQuery dataset and view the prebuilt Backup and DR reports. The Data Studio template is a pre-designed report or dashboard that gives you a head start for visualizing your data.

## Prerequisite

  * [Set up prebuilt reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#script)



## View Backup and DR reports in Data Studio

To view reports in Data Studio, you must use the same dataset name and project ID where logs are routed to BigQuery.

Use the following instructions to view Backup and DR reports in Data Studio.

  1. Copy and paste the following URL based on your backup/recovery appliance version in the address bar of a web browser after replacing the project ID and dataset.
         
         https://lookerstudio.google.com/reporting/create
             ?c.reportId=a00296dc-1687-41b5-be52-ab55cd805744
             &r.reportName=Backup%20and%20DR%20-%20Report%20&%20Insights
             &ds.ds1.datasourceName=Job%20Details
             &ds.ds1.connector=bigQuery
             &ds.ds1.projectId=PROJECT_ID
             &ds.ds1.type=TABLE
             &ds.ds1.datasetId=DATASET
             &ds.ds1.tableId=Job%20Details
             &ds.ds2.datasourceName=Protected%20Data%20Resource
             &ds.ds2.connector=bigQuery
             &ds.ds2.projectId=PROJECT_ID
             &ds.ds2.type=TABLE
             &ds.ds2.datasetId=DATASET
             &ds.ds2.tableId=Protected%20Data%20Resource
             &ds.ds3.datasourceName=Recovery%20Jobs%20Summary
             &ds.ds3.connector=bigQuery
             &ds.ds3.projectId=PROJECT_ID
             &ds.ds3.type=TABLE
             &ds.ds3.datasetId=DATASET
             &ds.ds3.tableId=Recovery%20Jobs%20Summary
             &ds.ds4.datasourceName=Daily%20Schedule%20Compliance
             &ds.ds4.connector=bigQuery
             &ds.ds4.projectId=PROJECT_ID
             &ds.ds4.type=TABLE
             &ds.ds4.datasetId=DATASET
             &ds.ds4.tableId=Daily%20Schedule%20Compliance
             &ds.ds5.datasourceName=Backup%20Jobs%20Summary
             &ds.ds5.connector=bigQuery
             &ds.ds5.projectId=PROJECT_ID
             &ds.ds5.type=TABLE
             &ds.ds5.datasetId=DATASET
             &ds.ds5.tableId=Backup%20Jobs%20Summary
             &ds.ds6.datasourceName=Failed%20Jobs
             &ds.ds6.connector=bigQuery
             &ds.ds6.projectId=PROJECT_ID
             &ds.ds6.type=TABLE
             &ds.ds6.datasetId=DATASET
             &ds.ds6.tableId=Failed%20Jobs
             &ds.ds7.datasourceName=Unresolved%20Failures
             &ds.ds7.connector=bigQuery
             &ds.ds7.projectId=PROJECT_ID
             &ds.ds7.type=TABLE
             &ds.ds7.datasetId=DATASET
             &ds.ds7.tableId=Unresolved%20Failures
         

Replace the following:

     * `PROJECT_ID`: the name of your project.
     * `DATASET`: the name of your BigQuery dataset. The default BigQuery dataset name for Backup and DR reports is `BackupandDR_reports`. In case you have set a different name for your BigQuery dataset for Backup and DR reports, modify the dataset name to match your BigQuery dataset.
  2. Click **Authorize**.

  3. Sign in with your Google Cloud account.

You are directed to Data Studio, where you can view [Job reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backup-recovery-reports), [Daily Schedule Compliance reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/compliance-reports-bigquery), and [Protected Resource reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/protected-resource-reports). These reports are available with view-only access. You can [export reports](https://support.google.com/looker-studio/answer/7398375?hl=en#zippy=%2Cin-this-article) to a CSV file or as individual sheets. You can save this URL for quick access to Backup and DR prebuilt reports.

**Note:** In Data Studio, you can view up to 2 million rows and export up to 750,000 rows of data from a chart.

Data Studio automatically refreshes your report at certain intervals. To change the default data refresh rate, see [Manage data freshness](https://support.google.com/looker-studio/answer/7020039?hl=en#zippy=%2Cin-this-article).




For advanced use cases, such as scheduling, emailing, customizing, and sharing, you can make your own copy of the report using the **Edit and share** button.

## Pricing

Data Studio is available at no charge for viewing and creating reports. However, BigQuery is a paid product and you will incur charges for using it when you access BigQuery datasets through the Data Studio. There are no charges for the first 1 TiB BigQuery data processed per month. For detailed pricing information, see [BigQuery pricing](https://cloud.google.com/bigquery/pricing#free) and [Data Studio pricing](https://cloud.google.com/looker-studio#pricing).

## What's next

  * Learn how to [Add data to a report](https://support.google.com/looker-studio/answer/6300774)
  * Learn how to [Share reports](https://support.google.com/looker-studio/answer/6287179)
  * Learn how to [Export reports](https://support.google.com/looker-studio/answer/7398375?hl=en#zippy=%2Cin-this-article)
  * Learn how to [Download reports](https://support.google.com/looker-studio/answer/9125317?hl=en&sjid=8370556453844609296-AP)
  * Learn how to [Schedule automatic report delivery over email](https://support.google.com/looker-studio/answer/9263641?hl=en&sjid=8370556453844609296-AP#zippy=%2Cin-this-article)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
