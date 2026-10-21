---
url: https://docs.cloud.google.com/data-studio/chart-cross-filtering/
title: Chart cross-filtering \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:03:31.494137+00:00
---

# Chart cross-filtering  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/chart-cross-filtering/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Chart cross-filtering Stay organized with collections  Save and categorize content based on your preferences. 

Cross-filtering lets you interact with one chart and apply that interaction as a filter to other charts in the report. These cross-filters, along with other filter controls and quick filters, are displayed in the filter bar. When cross-filtering is turned on for a chart, you can filter the report by interacting with that chart in two ways:

  * Click one or more dimension values in the chart.
  * Select an area by clicking and dragging your mouse across a time series, line chart, or area chart.

**Note:** You can also [let people drill down into your data](https://docs.cloud.google.com/data-studio/add-drill-actions-to-charts).

## How cross-filtering works

Cross-filtering works in the same way as other controls. For example, a pie chart based on the _Country_ dimension lets you filter your report in the same way as a drop-down list control based on the **Country** dimension. Brushing a time series acts in the same way as a date range control.

Cross-filtering can be restricted to groups, just like other controls.

## Enable cross-filtering

Cross-filtering is turned on for most connector types by default. However, to improve performance, Ads-related connectors have cross-filtering turned off.

### Turn cross-filtering on or off

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select a chart.
  3. On the right, scroll to the bottom of the DATA properties panel.
  4. In the **Chart** **interactions** section, click **Cross-filtering**.
  5. Repeat these steps for each chart you want to use as a filter.



## Reset chart filters

You can reset a chart filter to the default in several ways:

  * Right-click the chart, then select **Reset Action**.
  * Deselect the selected dimensions by clicking them.
  * Click somewhere on the border of chart you are filtering by.
  * [Clear or reset the filter bar](https://docs.cloud.google.com/data-studio/add-a-quick-filter#clear), which also resets any applied chart cross-filters.



## Limits of chart interactions

  * Cross-filtering isn't available in scorecards or bullet charts.
  * You can't cross filter by the "Others" category.
  * Cross-filtering is subject to the same limits as other controls in terms of [filtering across data sources](https://docs.cloud.google.com/data-studio/use-controls-across-data-sources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-14 UTC."],[],[]] 
