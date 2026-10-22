---
url: https://docs.cloud.google.com/looker/docs/streamgraph/
title: Creating a streamgraph chart with the Chart Config Editor \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:44.684898+00:00
---

# Creating a streamgraph chart with the Chart Config Editor  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/streamgraph/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Creating a streamgraph chart with the Chart Config Editor Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Starting in Looker 24.8, the Chart Config Editor supports the creation of streamgraph charts.

A streamgraph chart is a type of stacked area chart that is useful for displaying compound volume across different categories or over time.

Using the [Chart Config Editor](https://docs.cloud.google.com/looker/docs/chart-config-editor), you can create streamgraph charts by starting from an [area chart](https://docs.cloud.google.com/looker/docs/area-options) in Looker. Streamgraph charts require two dimensions and one measure.

For example, the following streamgraph chart shows the **Total Sale Price** over several different **Category** values, plotted over **Order Created Month**. Categories are stacked on top of one another to show how much each category contributes to the total, as well as how the total changes over time.

![](https://docs.cloud.google.com/static/looker/docs/images/streamgraph-248.png)

## Prerequisites

To access the Chart Config Editor, you must have the [`can_override_vis_config` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#can_override_vis_config).

### Writing the JSON snippet

To create a streamgraph chart, start from the following JSON snippet:
    
    
    {
      chart: {
        type: 'streamgraph',
      }
    }
    

### Creating a streamgraph chart

To create a streamgraph chart, follow these steps:

  1. View an [area chart](https://docs.cloud.google.com/looker/docs/area-options) in an Explore, or edit an area chart in a Look or dashboard.

For this example, we recommend starting from an area chart with two dimensions and one measure. One dimension should be pivoted. Your starting chart might look something like this example:

![Sample stacked area chart.](https://docs.cloud.google.com/static/looker/docs/images/streamgraph-base-248.png)

  2. Open the **Edit** menu in the visualization.

  3. In the **Plot** tab, click the **Edit Chart Config** button. Looker displays the **Edit Chart Config** dialog.

  4. Select the **Chart Config (Override)** section, and enter the HighCharts JSON from the Writing the JSON snippet section of this page.

  5. To let Looker properly format your JSON, click **< > (Format code)**.

  6. To test your changes, click **Preview**.

  7. To apply your changes, click **Apply**. The visualization will be displayed using the custom JSON values.




![](https://docs.cloud.google.com/static/looker/docs/images/streamgraph-editor-248.png)

Once you've customized your visualization, you can save it.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
