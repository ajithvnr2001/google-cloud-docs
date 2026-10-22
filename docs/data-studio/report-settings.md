---
url: https://docs.cloud.google.com/data-studio/report-settings/
title: Report settings \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:41.185024+00:00
---

# Report settings  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/report-settings/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Report settings Stay organized with collections  Save and categorize content based on your preferences. 

The report settings panel lets you configure a number of general properties for the report.

To access the report settings panel, follow these steps:

  1. Edit the report.
  2. Select **File > Report settings**, or right-click the canvas, then click **Report settings**.



## Data source

Configuring a data source in the report settings panel is no different than adding a data source to any other component. That data source will be the default until you add a different one to any other component in the report.

**Note:** Report-level data sources are a legacy feature that remains as a convenience for supporting older reports.

## Date Range Dimension

Configuring a date range dimension in the report settings panel sets it as the default for the entire report. You can override this by setting a different date range dimension for a selected component.

[Learn more about changing the default date range](https://docs.cloud.google.com/data-studio/set-report-date-ranges).

## Report filter

Configuring a filter in the report settings panel sets it as the default for the entire report. All components that share the same (or similar) data source are affected by the filter. You can override this by turning off filter inheritance for a selected component.

[Learn more about filters](https://docs.cloud.google.com/data-studio/about-filter-properties).

## Viewer data refresh

By default, only report editors can [manually refresh report data](https://docs.cloud.google.com/data-studio/manage-data-freshness#refresh-report-data-manually).

The **Viewer data refresh** toggle lets report viewers refresh the data in a report. When this setting is enabled, viewers can refresh data for individual components or for all data sources in the report.

If you use Data Studio Pro, organization administrators can prevent report editors from enabling the **Viewer data refresh** option in report settings. This setting is managed in the Google Admin console and is not available in the Data Studio report settings UI.

## Google Analytics measurement ID

You can measure traffic to a report by entering a Google Analytics 4 measurement ID.

Learn more about [measuring report usage with Google Analytics](https://docs.cloud.google.com/data-studio/measure-report-usage).

**Important:** If the report is copied, the measurement ID does NOT get copied to the new report. This is to protect the privacy of the Google Analytics account owner.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
