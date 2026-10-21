---
url: https://docs.cloud.google.com/data-studio/metric-slider/
title: Metric slider \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:09:44.895027+00:00
---

# Metric slider  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/metric-slider/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Metric slider Stay organized with collections  Save and categorize content based on your preferences. 

You can use a metric slider to filter a chart by metric value. For example, you can limit the chart to only show Orders where the total value is between $100 and $200, or where Levels Completed (in a game) is less than 5.

## Add metric sliders to a chart

**Note:** A chart can have metric sliders or [optional metrics](https://docs.cloud.google.com/data-studio/optional-metrics), but not both.

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).

  2. Select a chart.

     1. You can add sliders to tables, time series, line charts, bar charts, pie charts, area charts, treemaps, scatter charts, and geo maps.
  3. In the **Properties** panel, select the **SETUP** tab.

  4. Under _Metric_ , turn on **Metric sliders**.

  5. If necessary, add one or more metrics to the chart.




## Use metric sliders

  1. View or edit your report.
  2. Hover over a chart that has metric sliders turned on.
  3. Click the ![](https://docs.cloud.google.com/static/data-studio/images/instantmixgrey6001x48dp-2020-06-09.png)**Metric sliders** icon.
  4. Each metric in your chart has a slider: if necessary, scroll the list to see more of your metrics.
  5. Drag the left and right ends of the slider to adjust the lower and upper boundaries of the range for a selected metric. Or type in the numbers directly using the entry fields on the left and right.

![For a table chart that has metric sliders for Cost and Clicks, a user slides the Cost metric to adjust the value range from 27 through 55, and leaves the Clicks metric slider range set from 1 through 193.](https://docs.cloud.google.com/static/data-studio/images/metric-slider-2020-06-09.png)

  6. To reset an individual slider to its default values, click **Clear**.

  7. To reset the entire chart, hover over the chart and click ![](https://docs.cloud.google.com/static/data-studio/images/chart-reset-2020-06-09.png)**Reset**.

     1. This resets all chart options, including metric sliders, optional metrics, drill down, and sorting.

**Note:** Filtering by one metric doesn't affect the other metrics in the chart.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
