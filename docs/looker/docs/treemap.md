---
url: https://docs.cloud.google.com/looker/docs/treemap/
title: Creating a treemap chart with the Chart Config Editor \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:36.046401+00:00
---

# Creating a treemap chart with the Chart Config Editor  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/treemap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Creating a treemap chart with the Chart Config Editor Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Starting in Looker 24.10, the Chart Config Editor supports the creation of treemap charts.

A treemap chart displays categorical and hierarchical data as a set of rectangles, where the size of each rectangle is determined by a numeric measure.

Using the [Chart Config Editor](https://docs.cloud.google.com/looker/docs/chart-config-editor), you can create treemap charts by starting from a [column chart](https://docs.cloud.google.com/looker/docs/column-options) in Looker. For best results, use a pivoted dimension, an unpivoted dimension, and a measure to create a treemap chart.

For example, you can create a treemap chart that shows the **Order Item Count** over several different **Category** values, pivoted by **Seasonal Collection**. Each season is represented by a color-coded rectangle, which contains smaller rectangles that represent the category. The size of each rectangle corresponds to the **Order Item Count** .

![](https://docs.cloud.google.com/static/looker/docs/images/treemap-2410.png)

## Prerequisites

To access the Chart Config Editor, you must have the [`can_override_vis_config` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#can_override_vis_config).

### Writing the JSON snippet

To create a treemap chart, start from the following JSON snippet:
    
    
    {
      chart: {
        type: 'treemap',
      }
    }
    

### Creating a treemap chart

To create a treemap chart, follow these steps:

  1. View a [column chart](https://docs.cloud.google.com/looker/docs/column-options) in an Explore, or edit a column chart in a Look or dashboard.

For this example, we recommend starting from a column chart with two dimensions and one measure. One dimension should be pivoted. The pivoted values define the top level categories used to render the treemap. Your starting chart might look something like this example:

![Sample column chart with Category Name on the x-axis and Order Items grouped by Seasonal Collection on the y-axis](https://docs.cloud.google.com/static/looker/docs/images/treemap-base-2410.png)

  2. Open the **Edit** menu in the visualization.

  3. In the **Plot** tab, click the **Edit Chart Config** button. Looker displays the **Edit Chart Config** dialog.

  4. Select the **Chart Config (Override)** section, and enter the HighCharts JSON from the Writing the JSON snippet section of this page.

  5. To let Looker properly format your JSON, click **< > (Format code)**.

  6. To test your changes, click **Preview**.

  7. To apply your changes, click **Apply**. The visualization will be displayed using the custom JSON values.




![](https://docs.cloud.google.com/static/looker/docs/images/treemap-editor-2410.png)

Once you've customized your visualization, you can save it.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
