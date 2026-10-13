---
url: https://docs.cloud.google.com/data-studio/connect-to-microsoft-excel/
title: Connect to Microsoft Excel \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:13:14.787632+00:00
---

# Connect to Microsoft Excel  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-microsoft-excel/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect to Microsoft Excel Stay organized with collections  Save and categorize content based on your preferences. 

You can connect your local Microsoft Excel worksheets to Data Studio using the Microsoft Excel connector. Uploading your spreadsheets lets you build interactive visual reports and combine Excel data with other sources. You can then share dynamic dashboards across your organization for collaborative analysis.

## How to connect Data Studio to Excel

An Excel data source can connect to a single worksheet in an Excel workbook.

To connect to Excel, follow these steps:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. On the Data Studio home page, in the top left, click add **Create** , and then select **Data Source**.
  3. Select the **Microsoft Excel** connector.
  4. In the **Available Files** section, click **\+ New** to upload an Excel spreadsheet, or select a previously uploaded Excel spreadsheet.
  5. In the **Worksheets** section, select the worksheet to use for the data source.
  6. Configure any of the data source options (see the **General options** section for more details).
  7. In the upper right, click **CONNECT**. 
     1. The worksheet is added to your Available Files list.
     2. The data source fields panel appears.
     3. The data source is now connected to your [dataset](https://docs.cloud.google.com/data-studio/dataset).



All the columns you've included in the connection now appear as fields in the data source. See [Create and edit data sources](https://docs.cloud.google.com/data-studio/about-data-sources) to learn more about configuring your data source.

### General options

When you're setting up the Excel Connector, you can configure the following options:

  * **Use first row as headers** causes the data source to use the first row in your worksheet as the field names in the data source. If this option is not selected, the field names will use the column index (A, B, C, etc.).
  * **Include hidden and filtered cells** lets you include or exclude this data from the data source. The default value is to include them. This option applies only to filters, not to filtered views.
  * **Include specific range** lets you define a range of cells in the selected worksheet. Use standard column-row syntax to define the range: for example, `A1:Z26`.
  * **Select rows to skip** lets you specify certain rows that Data Studio should ignore when it creates the data source.
  * **Select columns to skip** lets you specify certain columns that Data Studio should ignore when it creates the data source.



You can also configure these options later by [editing the data source connection](https://docs.cloud.google.com/data-studio/edit-the-data-source-connection).

### Field editing in reports

The **Field Editing in Reports** data source option lets report editors change field definitions at the chart level. Editing field definitions in the report makes customizing your reports faster and easier. Learn more about [editing fields in reports](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports).

## Configure the data source

The data source fields panel is where you configure the data source by renaming fields and adding descriptions, adding calculated fields, and changing data types and aggregations. Learn more about [working with data source fields](https://docs.cloud.google.com/data-studio/model-your-data).

## Control who sees the data

At the top of the fields panel, you can change the data credentials. Credentials control who can see the data that this data source provides.

**OWNER'S CREDENTIALS** let other people view or create reports that use this data without requiring them to have their own access to the dataset.

**VIEWER'S CREDENTIALS** , on the other hand, require each user of the data source to provide their own credentials to access the dataset.

**SERVICE ACCOUNT CREDENTIALS** rely on a special type of Google Account that represents a non-human user that can authenticate and be authorized to access data.

[Learn more about data credentials](https://docs.cloud.google.com/data-studio/data-credentials-article).

## Create a new report from the data source

To create a new report from the data source, follow these steps:

  1. In the upper right, click **CREATE REPORT**. The report editor appears.
  2. Click **ADD TO REPORT**. 
     1. This action adds the data source to the report.
     2. You can now create charts and controls that get their data from this data source.



### New to Data Studio?

Take the [Create a report tutorial](https://docs.cloud.google.com/data-studio/tutorial-create-a-new-report).

## Delete or download Excel spreadsheets

The **Available Files** section lists the Excel spreadsheets that you have previously uploaded. You can delete spreadsheets to free up space and download spreadsheets to your device.

When you're using the Excel connector in Data Studio, the following storage limits apply:

  * If you don't have Data Studio Pro, you can store up to 2 GB in Excel data sources.
  * If you have Data Studio Pro, you can store up to 5 GB in Excel data sources.



To delete or download spreadsheets, follow these steps:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. On the Data Studio home page, in the top left, click add **Create** , and then select **Data Source**.
  3. Select the **Microsoft Excel** connector.
  4. The **Available Files** section lists the Excel spreadsheets that you have previously uploaded. Click the three-dot menu next to the spreadsheet that you'd like to delete or download, and then choose one of the following options:


  * To delete the spreadsheet, click **Delete**. Important: Deleting an Excel file will also delete any data sources that use the file, potentially impacting charts and reports.



## Data Studio Pro features

If you have Data Studio Pro, you can store up to 5 GB in Excel data sources instead of 2 GB.

If you store more than 2 GB in Excel data sources and then downgrade from Data Studio Pro, spreadsheets that you have already uploaded won't be affected. However, you won't be able to upload new spreadsheets until your total storage is less than 2 GB.

## Notes

Note the following requirements and limitations for sheets that are uploaded with the Excel Connector:

  * If you don't have Data Studio Pro, you can store up to 2 GB in Excel data sources.
  * If you have Data Studio Pro, you can store up to 5 GB in Excel data sources.
  * You can only upload Excel files up to 100 MB.
  * The header row must be a **single row**.
  * All cells within a column should be of the **same type**.
  * Excel Online spreadsheets are not supported.
  * Password-protected files are not supported.
  * Macros are not supported.
  * Pivot tables are not supported.
  * An Excel spreadsheet can be used by one or more data sources.
  * The **Available Files** section lists only the Excel spreadsheets that you have previously uploaded, not spreadsheets uploaded by other members of your organization.



## Related resources

  * [About data sources](https://docs.cloud.google.com/data-studio/about-data-sources)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
