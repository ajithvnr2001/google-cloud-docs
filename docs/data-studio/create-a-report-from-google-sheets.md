---
url: https://docs.cloud.google.com/data-studio/create-a-report-from-google-sheets/
title: Create a report from Google Sheets \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:28.534101+00:00
---

# Create a report from Google Sheets  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/create-a-report-from-google-sheets/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Create a report from Google Sheets Stay organized with collections  Save and categorize content based on your preferences. 

Google Sheets is part of the Google Docs suite of productivity apps. Google Sheets lets you create and format online spreadsheets and work on them simultaneously with others. You can create a Data Studio report directly from Google Sheets.

## Create a report

To create a new report from Google Sheets, follow these steps:

  1. Navigate to the Google Sheet from which you would like to create a report.
  2. In the Google Sheets toolbar, click **Extensions**.
  3. In the **Data Studio** section of the **Extensions** menu, select **Create a new report**. Google Sheets displays the **Data Studio report creation** panel.
  4. Optionally, configure report options in Google Sheets.
  5. Click **Create**. Data Studio opens in a new tab and creates a report from the sheet.
  6. If you don't have a Data Studio account, you will be prompted to create an account. Enter your country and your company name.
  7. To save the report, click **Save and share**. 
     * If you don't click **Save and share** , the report will be deleted after 24 hours.



After you save the report, you can [edit the report](https://docs.cloud.google.com/data-studio/edit-a-report) and [share the report](https://docs.cloud.google.com/data-studio/ways-to-share-your-reports).

### Options

  * **Use first row as headers** causes the data source to use the contents of the first row in your worksheet as the field names in the data source. If this option is not selected, the field names will use the column index (A, B, C, etc.).
  * **Include hidden and filtered cells** lets you include or exclude this data from the data source. The default value is to include them. This option applies only to filters, not to filtered views. Learn more about filters in the [Sheets Help Center](https://support.google.com/docs/answer/3540681).
  * **Include selected range** lets you define a range of cells in the selected worksheet. Use standard column-row syntax to define the range: for example, A1:Z26.



## Update the data source

When you create a report from Google Sheets, Data Studio creates a new data source for the Sheet.

To update the data source, follow these steps:

  * If the data in the Sheet has changed, [manually refresh your report data](https://docs.cloud.google.com/data-studio/manage-data-freshness).
  * If columns have been added or edited in the Sheet, [refresh the data source fields](https://docs.cloud.google.com/data-studio/refresh-data-source-fields).



## Things to consider

While creating reports from Google Sheets, keep the following considerations in mind:

  * By default, the name of the report will be `Data Studio Reporting - <timestamp>`, where `<timestamp>` is the date and time that the Data Studio report was created.
  * Your data must be in a tabular format. Learn more about [how to prepare your Google Sheets to work with Data Studio](https://docs.cloud.google.com/data-studio/tutorial-create-a-google-sheets-data-source).
  * Merged cells are not supported. Unmerge all cells before creating a report.
  * The header row must be a single row.
  * All cells within a column should be of the same type.
  * Make sure that your date fields are formatted using the `Date` data type, so that Data Studio can correctly interpret them as dates for the report.



## Related resources

  * [About Google Sheets](https://www.google.com/sheets/about/)
  * [Connect to Google Sheets](https://docs.cloud.google.com/data-studio/connect-to-google-sheets)
  * [Tutorial: Create a Google Sheets data source](https://docs.cloud.google.com/data-studio/tutorial-create-a-google-sheets-data-source)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
