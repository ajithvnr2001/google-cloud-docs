---
url: https://docs.cloud.google.com/data-studio/optional-metrics/
title: Optional metrics \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:16:57.990758+00:00
---

# Optional metrics  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/optional-metrics/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Optional metrics Stay organized with collections  Save and categorize content based on your preferences. 

You can make your charts and tables more flexible by adding optional metrics. You can change the columns or fields that you want to see in the chart without having to edit the chart configuration each time.

## Add optional metrics

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select or [add a chart](https://docs.cloud.google.com/data-studio/add-charts-and-controls-to-your-report).
  3. In the **Properties** panel, select the **SETUP** tab.
  4. Under **Metric** , turn on **Optional metrics**.
  5. Click **+Add metric** or drag the metric from the **Available fields** panel.



## Select optional metrics in a chart

  1. View or edit your report.
  2. Hover over a chart with optional metrics; then, in the header, click the **Optional metrics** icon.
  3. Select the optional metrics from the list.

**Tip:** Be sure to set the chart's **Chart header** option to **Always show** or **Show on hover**. Otherwise, you won't be able to access the optional metrics when viewing the chart.

## Restore the default fields

To revert the chart to its default field set, hover over the chart and click the **Reset** icon ![Undo](https://docs.cloud.google.com/static/data-studio/images/icundogrey6002xweb48dp-2019-09-11-.png).

## Limits of optional metrics

  * The number of optional metrics that you can select depends on the number of required metrics that are already present in the chart and the chart type: 
    * **Table and pivot table:** The maximum is determined by the maximum number of metrics that are allowed by the chart, which depends on the data source. The maximum typically ranges from 20-100.
    * **Bar/Line/Combo:** 20.
    * **All other chart types** : 100.
  * Optional metrics are not available for scatter charts or Google Maps.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-14 UTC."],[],[]] 
