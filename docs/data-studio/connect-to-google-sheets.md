---
url: https://docs.cloud.google.com/data-studio/connect-to-google-sheets/
title: Connect to Google Sheets \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:22.614972+00:00
---

# Connect to Google Sheets  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-google-sheets/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect to Google Sheets Stay organized with collections  Save and categorize content based on your preferences. 

You can connect your Google Sheets data to Data Studio using the Google Sheets connector. You can turn spreadsheet rows into interactive charts, tables, and shareable dashboards for your team. Visualizing your spreadsheet data helps you uncover trends and share dynamic insights without writing code.

## How to connect to Google Sheets

A Google Sheets data source can connect to a single worksheet in a Google Sheet.

**To connect:**

  1. [Sign in to Data Studio.](https://datastudio.google.com)

  2. On the Data Studio home page, in the top left, click ![The Create icon.](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Create** , and then select **Data Source**.

  3. Select the **Google Sheets** connector.

  4. Select a **Spreadsheet** and a **Worksheet.**

> You can connect to spreadsheets that you own or that have been shared with you. You can also paste in the URL of a Google Sheet to which you have access.

  5. Configure any of the data source options.

  6. In the upper right, click **CONNECT**.

     1. The data source fields panel appears.
     2. The data source is now connected to your [dataset](https://docs.cloud.google.com/data-studio/dataset).



All the columns that you've included in the connection now appear as fields in the data source. See [Create and edit data sources](https://docs.cloud.google.com/data-studio/about-data-sources) to learn more about configuring your data source.

### Options

**Use first row as headers** causes the data source to use the first row in your worksheet as the field names in the data source. If this option is not selected, the field names will use the column index (A, B, C, etc.)

**Include hidden and filtered cells** lets you include or exclude this data from the data source. The default value is to include them. This option only applies to filters, not to filtered views. Learn more about filters in the [Sheets Help Center](https://support.google.com/docs/answer/3540681).

**Optional Range** lets you define a range of cells in the selected worksheet. Use standard column-row syntax to define the range: for example, `A1:Z26`.

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

## Notes

  * Your data must be in a **tabular format**. Learn more about [how to prepare your Google Sheets to work with Data Studio](https://docs.cloud.google.com/data-studio/tutorial-create-a-google-sheets-data-source).

  * The header row must be a **single row**.

  * All cells within a column should be of the **same type**.

  * Data Studio will automatically check for any changed data values and new rows every time a query is run on any report that uses the sheet.

  * If you change a sheet's columns after connecting it as a data source, [refresh the data source fields](https://docs.cloud.google.com/data-studio/refresh-data-source-fields) to see those changes.

  * To connect to data in Microsoft Excel, use the [Microsoft Excel connector](https://docs.cloud.google.com/data-studio/connect-to-microsoft-excel) instead.




## Troubleshooting

If you're having trouble connecting to your spreadsheets, consider the following:

  * Data Studio does not support accessing files on Team Drive. Check that your Sheets are stored in standard Drive folders.
  * Make sure that you're using the same account for both Data Studio and Google Drive. If you've accidentally connected Data Studio to a different Google Drive account, you can [remove that connection](https://docs.cloud.google.com/data-studio/remove-or-reconnect-access-to-your-google-account) and then reconnect by using a different account.
  * See the [general tips on troubleshooting issues with Drive](https://support.google.com/drive/answer/7505592) support article.
  * If you are a Google Workspace user, your organization must permit access to Drive. [Learn how to manage Drive in Google Workspace](https://support.google.com/a/topic/2490075?ref_topic=9197).



## Related resources

  * [About data sources](https://docs.cloud.google.com/data-studio/about-data-sources)
  * [About Google Sheets](https://www.google.com/sheets/about/)
  * [Google Workspace help center](https://support.google.com/docs)
  * [Connect to Microsoft Excel](https://docs.cloud.google.com/data-studio/connect-to-microsoft-excel)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
