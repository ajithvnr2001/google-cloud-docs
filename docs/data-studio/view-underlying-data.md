---
url: https://docs.cloud.google.com/data-studio/view-underlying-data/
title: View underlying data \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:51.904055+00:00
---

# View underlying data  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/view-underlying-data/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  View underlying data Stay organized with collections  Save and categorize content based on your preferences. 

Viewing the data that underlies a chart can help you understand what data is available and how it's structured so that you can make the best decisions about what to include in the chart. Viewing the underlying data can also help you troubleshoot problems with your reports.

## How to view a chart's underlying data

To view a chart's underlying data, perform these steps;

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select a chart, and then right click.
  3. Select **Show underlying data**.



## How viewing underlying data works

Viewing the underlying data displays all the data for the primary dimensions, breakdown dimensions, and metrics that appear in the chart. For chart types that don't have breakdown dimensions, Data Studio displays the data in a simple table. For charts that have breakdowns (for example, time series or area charts), and for pivot tables, the data is displayed in a pivot table format. If the dataset contains more than 25 rows, you'll see additional pages in the display.

> **Note** : Viewing a chart's underlying data is subject to the same principles of [data freshness](https://docs.cloud.google.com/data-studio/manage-data-freshness) as interacting with the chart itself. You may incur query costs, if applicable, by viewing the underlying data.

## Limitation of viewing the underlying data

Drill-down dimensions are not included when you view underlying data.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
