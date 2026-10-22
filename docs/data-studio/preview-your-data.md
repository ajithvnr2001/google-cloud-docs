---
url: https://docs.cloud.google.com/data-studio/preview-your-data/
title: Preview your data \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:59.424401+00:00
---

# Preview your data  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/preview-your-data/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Preview your data Stay organized with collections  Save and categorize content based on your preferences. 

To better understand the shape of your data, you can preview it in Data Studio. This page explains how to preview your data by using the data source editor.

## Open the Data Preview pane

To preview your data for a data source, follow these steps:

  1. Navigate to the list of fields for a data source. 
     * When you [create a new data source](https://docs.cloud.google.com/data-studio/add-data-to-a-report), Data Studio automatically takes you to the list of fields after you connect your data.
     * For an existing data source, [edit the data source](https://docs.cloud.google.com/data-studio/edit-a-data-source). You can edit a data source from within a report or from the Data Studio home page.
  2. In the bottom left corner of the page, click **Data Preview**.



## Preview different sets of fields

To preview data for a set of fields, follow these steps:

  1. In the left-hand panel, select the fields that you'd like to preview in the **Dimensions** and **Metrics** sections. 
     * You can also search for fields using the search bar.
     * You cannot select more than the maximum number of fields. Data Studio displays the maximum number of fields at the bottom of the **Data Preview** pane.
  2. To select or deselect all fields, click the **Select All** checkbox next to the search bar. 
     * If the number of fields in the data source is greater than the maximum number of fields that can be selected, the **Select All** checkbox will be disabled. Data Studio displays the maximum number of fields at the bottom of the **Data Preview** pane.
  3. In the bottom left corner of the window, click **Refresh preview** to generate a data preview for the selected set of fields.



![](https://docs.cloud.google.com/static/data-studio/images/data-preview.png)

## Notes

Note the following considerations while previewing your data:

  * If [filtering by email address](https://docs.cloud.google.com/data-studio/filter-by-email-address) is enabled for a data source, then the results in the **Data Preview** pane will also be filtered by your email address.

  * You cannot manually set the widths of columns.

  * The **Data Preview** pane doesn't include [parameters](https://docs.cloud.google.com/data-studio/parameters).

  * Depending on your data source, the number of fields that you can preview may be limited. Data Studio displays this limit at the bottom of the **Data Preview** pane. For example, you can only preview 100 dimensions and 100 metrics for Google Sheets data sources.

  * The **Data Preview** pane can display a maximum of 1,000 rows.

  * The **Data Preview** pane is only available for the following data sources:

    * [Google BigQuery](https://docs.cloud.google.com/data-studio/connect-to-google-bigquery)
    * [Google Sheets](https://docs.cloud.google.com/data-studio/connect-to-google-sheets)
    * [Looker](https://docs.cloud.google.com/data-studio/connect-to-looker)
    * [Microsoft Excel](https://docs.cloud.google.com/data-studio/connect-to-microsoft-excel)
    * [CSV upload](https://docs.cloud.google.com/data-studio/upload-csv-files)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
