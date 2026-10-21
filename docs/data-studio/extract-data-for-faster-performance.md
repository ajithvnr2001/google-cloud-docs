---
url: https://docs.cloud.google.com/data-studio/extract-data-for-faster-performance/
title: Extract data for faster performance \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:22.687576+00:00
---

# Extract data for faster performance  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/extract-data-for-faster-performance/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Extract data for faster performance Stay organized with collections  Save and categorize content based on your preferences. 

Data extract lets you explore a subset of your data. This can make your reports and explorations load faster and be more responsive when applying filters and date ranges than when working with a live connection to your data.

## How extracting data works

When you extract data, you select an existing data source of any type, then select the specific fields you want to include in the _extracted data source_. You can apply filters and date ranges to reduce the amount of data even further. You can then use the extracted data source in your reports and explorations, just as you would a standard, live connection data source.

### Extracted data and aggregation

Extracting data from an already aggregated dataset, such as Google Ads or Analytics, creates a new, disaggregated dataset. This makes performing your own aggregation in extracted data sources more flexible than standard data sources. For example, in a standard Analytics data source, the _Users_ metric is set to Auto aggregation, meaning you can't change it. In an extracted Analytics data source, you are free to apply any of the available aggregation types. This can help you explore different interpretations of your data than is possible in reports using a standard (already aggregated) data source.

## Create an extracted data source

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. On the Data Studio home page, in the top left, click ![](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Create** , and then select **Data Source**.
  3. In the connectors list, select **Extract Data.**
  4. Select an existing data source to extract from.
  5. Select the dimensions and metrics to extract by dragging them from the Available Fields list onto the targets, or by clicking **Add**. All the fields you add appear in the list on the far right.
  6. (Optional) If the data is unaggregated, consider applying an aggregation, such as `Sum`, or `Average`, to reduce the amount of data extracted.
  7. (Optional) Apply filters to the data in order to reduce the number of rows.
  8. Apply a date range. Date ranges are required by some connectors, such as Analytics, but are optional for other connector types.
  9. Give your data source a name by clicking **Untitled Data Source** in the upper left.
  10. (Optional) To automatically refresh your data, in the lower right, turn on **Auto update** and set an update schedule.
  11. In the lower right, click **SAVE AND EXTRACT**.



You can now add this data source to a report or exploration by clicking one of the buttons in the upper right.

## Update extracted data

To update the information contained in a data extract, turn on "Auto update" or edit the data source connection and extract the data again:

  1. [Sign in to Data Studio.](https://datastudio.google.com)

  2. Navigate to the [DATA SOURCES Home](https://datastudio.google.com/navigation/datasources) page.

  3. Locate the extracted data source.

  4. Click the data source to edit it.

  5. In the upper left, click **EDIT CONNECTION**. You must be the data source owner to see this option.

  6. (Optional) To automatically refresh your data, in the lower right, turn on **Auto update** and set an update schedule.

  7. In the lower right, click **SAVE AND EXTRACT**.




## Delete your extracted data

Deleting an extracted data source also deletes its data from Google servers.

## Limits of data extract

  * Extracted data sources can contain up to 100 MB of data. If your extract contains more than 100 MB of data, Data Studio will fail to extract and will display an error message.
  * Extracted data sources can contain up to 750,000 rows. If your extract contains more than 750,000 rows, Data Studio will truncate the extract.
  * Extracted data sources contain static information: to refresh or update the data, turn on Auto update and set an update schedule.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
