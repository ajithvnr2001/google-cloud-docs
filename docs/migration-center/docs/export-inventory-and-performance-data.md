---
url: https://docs.cloud.google.com/migration-center/docs/export-inventory-and-performance-data/
title: Export asset and performance data \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:00.806353+00:00
---

# Export asset and performance data  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/export-inventory-and-performance-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Export asset and performance data Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to export your inventory of assets, and how to export the performance data collected for the assets.

## Export your asset details

Migration Center lets you generate a report of your inventory of assets. You can download the report as a CSV file or a Microsoft Excel spreadsheet, or export it to a Google Sheets file in your Google Drive, which you can then share with your colleagues or customers.

### Export details for all in-scope assets

To export your asset details, follow these steps:

  1. In the Google Cloud console, go to the **Create reports** page.

[Go to Create reports](https://console.cloud.google.com/migration/all-reports?gtm_source=documentation&gtm_source_id=export_reports)

  2. In the **Assets** section, click **Asset details export**.

  3. To view a list of all assets in your asset inventory, click **All**. By default, the **In scope** tab is selected.

  4. To export to CSV or Google Sheets, click **Export to CSV/Google Sheets**. After the export is complete, a dialog appears.

     * To download the files in CSV format, click **Download**.
     * To export your report to Google Sheets, click **Export to Google Sheets**. Then, when the export finishes, to view your report, click **Open in Google Sheets**.
  5. To export to Microsoft Excel format, click **Export to Microsoft Excel**. After the export is complete, a dialog appears where you can download the file.




### Filter and export assets

If you only want to export assets that satisfy certain conditions, first filter the assets, and then export them. You must filter servers and databases separately.

  1. In the Google Cloud console, go to the **Create reports** page.

[Go to Create reports](https://console.cloud.google.com/migration/all-reports?gtm_source=documentation&gtm_source_id=export_reports)

  2. In the **Assets** section, click **Asset details export**.

  3. To view a list of assets belonging to a specific group or asset type, click **Groups** or an asset type such as **Servers** or **S3**.

  4. To export to CSV or Google Sheets, click **Export to CSV/Google Sheets**. After the export is complete, a dialog appears.

     * To download the files in CSV format, click **Download**.
     * To export your report to Google Sheets, click **Export to Google Sheets**. Then, when the export finishes, to view your report, click **Open in Google Sheets**.
  5. To export to Microsoft Excel format, click **Export to Microsoft Excel**. After the export is complete, a dialog appears where you can download the file.




### Export groups of assets

To export groups of assets, follow these steps:

  1. In the Google Cloud console, go to the **Create reports** page.

[Go to Create reports](https://console.cloud.google.com/migration/all-reports?gtm_source=documentation&gtm_source_id=export_reports)

  2. In the **Assets** section, click **Asset details export**.

  3. To view groups of assets, click **Group**.

  4. Select the groups that you want to export.

  5. To export to CSV or Google Sheets, click **Export to CSV/Google Sheets**. After the export is complete, a dialog appears with a list of files containing your asset details:

     * To download the files in CSV format, click **Download**.
     * To export your report to Google Sheets, click **Export to Google Sheets**. Then, when the export finishes, to view your report, click **Open in Google Sheets**.
  6. To export to Microsoft Excel format, click **Export to Microsoft Excel**. After the export is complete, a dialog appears where you can download the file.




### Export details for all out-of-scope assets

To export your out-of-scope assets, follow these steps:

  1. In the Google Cloud console, go to the **Create reports** page.

[Go to Create reports](https://console.cloud.google.com/migration/all-reports?gtm_source=documentation&gtm_source_id=export_reports)

  2. In the **Assets** section, click **Asset details export**.

  3. Click the **All** tab, then click the **Out of scope** tab. The page shows the total number of out of scope assets to export.

  4. To export to CSV or Google Sheets, click **Export to CSV/Google Sheets**. After the export is complete, a dialog appears.

     * To download the files in CSV format, click **Download**.
     * To export your report to Google Sheets, click **Export to Google Sheets**. Then, when the export finishes, to view your report, click **Open in Google Sheets**.
  5. To export to Microsoft Excel format, click **Export to Microsoft Excel**. After the export is complete, a dialog appears where you can download the file.




## Export performance data

Migration Center lets you generate a report with the performance data collected from your assets with the discovery client or the `mcdc` CLI. A performance data export contains daily aggregated metrics from your assets. You can export metrics for the past available days, from a minimum of 10 up to a maximum of 420 days.

You can download the report as a CSV file or a Microsoft Excel spreadsheet, or export it to a Google Sheets file in your Google Drive.

### Export performance data for all assets

To export the performance data for all the assets in your inventory, including servers and databases, follow these steps:

  1. In the Google Cloud console, go to the **Create reports** page.

[Go to Create reports](https://console.cloud.google.com/migration/all-reports?gtm_source=documentation&gtm_source_id=export_reports)

  2. In the **Assets** section, click **Performance data export**.

  3. Click the **All assets** tab. The page shows the total number of in scope assets to export. Choose if you want to export servers, databases, or both.

  4. To export to CSV format or Google Sheets, click **Export to CSV/Google Sheets**. To export to Microsoft Excel format, click **Export to Microsoft Excel**.

  5. In the dialog that appears, select the number of days of performance data that you want to export for each asset, then click **Export**.

  6. After the export is complete, a dialog appears with one or two files to download, depending on the format you chose.

     * To download the files, click **Download**.
     * To export your report to Google Sheets, click **Export to Google Sheets**. Then, when the export finishes, to view your report, click **Open in Google Sheets**.



This export doesn't include assets that you [marked as out of scope](https://docs.cloud.google.com/migration-center/docs/view-assets#out-of-scope).

### Filter assets and export performance data

To limit the performance data export to selected assets, filter them first by specifying the conditions that you want to apply to your export.

  1. In the Google Cloud console, go to the **Create reports** page.

[Go to Create reports](https://console.cloud.google.com/migration/all-reports?gtm_source=documentation&gtm_source_id=export_reports)

  2. In the **Assets** section, click **Performance data export**.

  3. Depending on the asset type you want to export, click either the **Export servers** or **Export databases** tab.

  4. Use the **Filter** tab to select assets based on properties and values. For example, filter assets based on the OS or fit level. You can apply multiple filters at the same time.

  5. To export to CSV format or Google Sheets, click **Export to CSV/Google Sheets**. To export to Microsoft Excel format, click **Export to Microsoft Excel**.

  6. In the dialog that appears, select the number of days of performance data that you want to export for each asset, then click **Export**.

  7. After the export is complete, a dialog appears with one file to download, depending on the format you chose.

     * To download the file, click **Download**.
     * To export your report to Google Sheets, click **Export to Google Sheets**. Then, when the export finishes, to view your report, click **Open in Google Sheets**.



### Export performance data for groups of assets

To export the performance data for groups of assets, follow these steps:

  1. In the Google Cloud console, go to the **Create reports** page.

[Go to Create reports](https://console.cloud.google.com/migration/all-reports?gtm_source=documentation&gtm_source_id=export_reports)

  2. In the **Assets** section, click **Performance data export**.

  3. Click the **Export groups** tab. The page shows all the groups in your Migration Center project.

  4. Select the groups that you want to export, either manually, or with the **Filter** tab.

  5. To export to CSV format or Google Sheets, click **Export to CSV/Google Sheets**. To export to Microsoft Excel format, click **Export to Microsoft Excel**.

  6. In the dialog that appears, select the number of days of performance data that you want to export for each asset, then click **Export**.

  7. After the export is complete, a dialog appears with one or two files to download, depending on the format you chose.

     * To download the files, click **Download**.
     * To export your report to Google Sheets, click **Export to Google Sheets**. Then, when the export finishes, to view your report, click **Open in Google Sheets**.



## View recent exported reports

Migration Center lets you view the last 100 reports that you've generated. You can't see reports generated by other users, nor reports generated in other Google Cloud projects.

  * To view your recent reports, go to the **Recent exports** page.

[Go to Recent exports](https://console.cloud.google.com/migration/exports?gtm_source=documentation&gtm_source_id=export_reports)




## What's next

  * Learn how to [generate a total cost of ownership (TCO) report for your infrastructure](https://docs.cloud.google.com/migration-center/docs/generate-tco-report).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
