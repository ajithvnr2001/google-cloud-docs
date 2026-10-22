---
url: https://docs.cloud.google.com/looker/docs/sunburst/
title: Creating a sunburst chart with the Chart Config Editor \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:52.904288+00:00
---

# Creating a sunburst chart with the Chart Config Editor  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/sunburst/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Creating a sunburst chart with the Chart Config Editor Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Starting in Looker 24.16, the Chart Config Editor supports the creation of sunburst charts.

A sunburst chart displays hierarchical data as a set of concentric rings, where the size of each ring slice is determined by a numeric measure.

Using the [Chart Config Editor](https://docs.cloud.google.com/looker/docs/chart-config-editor), you can create sunburst charts by starting from a [column chart](https://docs.cloud.google.com/looker/docs/column-options) in Looker. For best results, use at least two unpivoted dimensions and exactly one numeric measure to create a sunburst chart.

For example, you can create a sunburst chart that shows the **Orders Count** measure, broken down by the **Users Country** , **Users State** , and **Users City** dimensions. The size of each ring slice corresponds to the **Orders Count** .

![](https://docs.cloud.google.com/static/looker/docs/images/sunburst-2414.png)

## Prerequisites

To access the Chart Config Editor, you must have the [`can_override_vis_config` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#can_override_vis_config).

## Writing the JSON snippet

To create a sunburst chart, start from the following JSON snippet:
    
    
    {
      chart: {
        type: 'sunburst',
      }
    }
    

## Creating a sunburst chart

To create a sunburst chart, follow these steps:

  1. View a [column chart](https://docs.cloud.google.com/looker/docs/column-options) in an Explore, or edit a column chart in a Look or dashboard.

Start from a column chart with two or more unpivoted dimensions and exactly one numeric measure. Make sure to order the dimensions from least granular to most granular. Your starting chart might look like a column chart plotting a single measure, with a concatenation of dimension values for each x-axis value.

![Sample column chart with a country, state, and city concatenation on the x-axis and Orders Count on the y-axis](https://docs.cloud.google.com/static/looker/docs/images/sunburst-base-2414.png)

**Note:** Even though this example is sorted by each dimension for clarity, sorting is not required and does not affect the sunburst chart.
  2. Open the **Edit** menu in the visualization.

  3. In the **Plot** tab, click the **Edit Chart Config** button. Looker displays the **Edit Chart Config** dialog.

  4. Select the **Chart Config (Override)** section, and enter the HighCharts JSON from the Writing the JSON snippet section of this page.

  5. To let Looker properly format your JSON, click **< > (Format code)**.

  6. To test your changes, click **Preview**.

  7. To apply your changes, click **Apply**. The visualization will be displayed using the custom JSON values.




![](https://docs.cloud.google.com/static/looker/docs/images/sunburst-2414.png)

Once you've customized your visualization, you can save it.

## Drilling into the data

Sunburst charts support the following drill actions:

  * To drill into one dimension value, click the corresponding ring slice.
  * To go back one level, click the center of the sunburst chart.
  * To go back one or more levels, use the breadcrumb navigation at the top left of the chart.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
