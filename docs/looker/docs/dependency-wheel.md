---
url: https://docs.cloud.google.com/looker/docs/dependency-wheel/
title: Creating a dependency wheel chart with the Chart Config Editor \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:51.423915+00:00
---

# Creating a dependency wheel chart with the Chart Config Editor  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/dependency-wheel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Creating a dependency wheel chart with the Chart Config Editor Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Starting in Looker 24.20, the Chart Config Editor supports the creation of dependency wheel charts.

A dependency wheel chart is similar to a [Sankey chart](https://docs.cloud.google.com/looker/docs/best-practices/sankey), but a dependency wheel displays flow between states around a circle rather than in a linear direction. In Looker, each dimension value is represented as a state, and the size of the flow is determined by a numeric measure value.

Using the [Chart Config Editor](https://docs.cloud.google.com/looker/docs/chart-config-editor), you can create dependency wheel charts by starting from a [column chart](https://docs.cloud.google.com/looker/docs/column-options) in Looker. 

Dependency wheel charts require at least two dimensions and exactly one measure.

For example, you can create a dependency wheel chart that shows the **Order Item Count** measure values over several **Seasonal Collection** dimension values, which flow into **Category** dimension values. Each dimension value is represented by a color-coded arc on the outside of the circle. The width of a line connecting two arcs corresponds to the values of the **Order Item Count** measure for that dimension pair. The higher the value, the wider the line. ![](https://docs.cloud.google.com/static/looker/docs/images/wheel-2420.png)

## Prerequisites

To access the Chart Config Editor, you must have the [`can_override_vis_config` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#can_override_vis_config).

### Writing the JSON snippet

To create a dependency wheel chart, start from the following JSON snippet:
    
    
    {
      chart: {
        type: 'dependencywheel'
      }
    }
    

## Creating a dependency wheel chart

To create a dependency wheel chart, follow these steps:

  1. View a [column chart](https://docs.cloud.google.com/looker/docs/column-options) in an Explore, or edit a column chart in a Look or dashboard.

Start from a column chart with at least two dimensions and exactly one measure. Your starting chart might look something like this example:

![Sample column chart with Category Name and Seasonal Collection on the x-axis and Order Items Count on the y-axis.](https://docs.cloud.google.com/static/looker/docs/images/sankey-base-2412.png)

  2. Open the **Edit** menu in the visualization.

  3. In the **Plot** tab, click the **Edit Chart Config** button. Looker displays the **Edit Chart Config** dialog.

  4. Select the **Chart Config (Override)** section, and enter the HighCharts JSON from the Writing the JSON snippet section of this page.

  5. To let Looker properly format your JSON, click **< > (Format code)**.

  6. To test your changes, click **Preview**.

  7. To apply your changes, click **Apply**. The visualization will be displayed using the custom JSON values.




![](https://docs.cloud.google.com/static/looker/docs/images/wheel-json-2420.png)

Once you've customized your visualization, you can save it.

## Limitations and requirements

When you're using dependency wheel charts, keep the following limitations and requirements in mind:

  * Dependency wheel charts require at least two dimensions and exactly one measure.
  * Dependency wheel charts can display a maximum of 50 rows of data.
  * Dependency wheel charts don't support pivoted dimensions.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
