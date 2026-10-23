---
url: https://docs.cloud.google.com/data-studio/export-data-from-a-chart/
title: Export data from a chart \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:26.047671+00:00
---

# Export data from a chart  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/export-data-from-a-chart/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Export data from a chart Stay organized with collections  Save and categorize content based on your preferences. 

You can export data or copy chart images from a Data Studio report to use in other applications. Exporting data from a chart lets you perform advanced analysis, integrate with custom systems, or share data with external collaborators.

## To export data from a chart

  1. View the report.
  2. Hover over the chart that you want to export.
  3. Right-click on the chart or select more_vert **More options** , and then select **Export data**.
  4. In the **Export data** window, enter a name for your export and select an **Export As** option: 
     * **CSV** creates a comma-separated text file.
     * **CSV (Microsoft Excel)** creates a comma-separated text file where non-ASCII characters are encoded properly for use in Excel™.
     * **Google Sheets** sends your data directly to Sheets.
  5. Select the **Keep value formatting** option if you want to retain the number and date formats that are applied in Data Studio in the exported data.



## To export or copy an image of a chart

You can add an image of a chart to another document by downloading the image as a file or by copying the chart image to your clipboard by following these steps:

  1. View the report.
  2. Hold your pointer over the chart that you want to export or copy.
  3. Right-click on the chart or select more_vert **More options** , and then select **Export as PNG** to download an image file or **Copy image to clipboard**.



If you can't see the more_vert **More options** menu and you can edit the report, try increasing the space around your charts. Sometimes other components on the page can obscure the menu. It's also possible that the owner of the report has configured the report so that the data cannot be exported.

## How exporting works

You can export a chart's data or an image of the chart.

**Exporting data** saves the information from a chart to the file format that you select. Data export is available in view mode. You can export data from only one chart at a time. Only the data available to you in that chart is exported. Any filters and date range controls are also applied to the exported data.

**Exporting an image** saves a PNG image of the chart or copies it to your clipboard. This option is not available for Google Maps, Sankey, or Timeline charts.

### Export from tables

You can control how much data to export from a table using the [**Show pagination** option](https://docs.cloud.google.com/data-studio/table-reference), located in the table's **Style** tab, and the **Rows per page** option, located in the **Setup** tab of the properties panel.

  * When **Show pagination** is enabled, all data in the table is exported. The number of rows per page has no effect on the amount of data exported.
  * When **Show pagination** is disabled, only the number of rows shown in the table are exported.



## Prevent others from exporting data

You can prevent other people from exporting data from your report as part of the report's sharing options. [Learn how to stop sharing your reports and data sources](https://docs.cloud.google.com/data-studio/stop-sharing-your-reports-and-data-sources).

## Limits of exporting data from a chart

You can export up to 750,000 rows of data from a chart.

If your data source is a [Looker Explore](https://docs.cloud.google.com/data-studio/connect-to-looker), then the limits depend on your Looker permissions. If your chart uses a [blended data source](https://docs.cloud.google.com/data-studio/blending-data), and one of the data sources is a [Looker Explore](https://docs.cloud.google.com/data-studio/connect-to-looker), the number of rows in the exported data may differ from the number of rows that are displayed in the chart.

## Related resources

[Embed a report](https://docs.cloud.google.com/data-studio/embed-a-report)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
