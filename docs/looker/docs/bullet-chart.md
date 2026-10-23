---
url: https://docs.cloud.google.com/looker/docs/bullet-chart/
title: Creating a bullet chart with the Chart Config Editor \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:14.695917+00:00
---

# Creating a bullet chart with the Chart Config Editor  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/bullet-chart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Creating a bullet chart with the Chart Config Editor Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Starting in Looker 24.4, the Chart Config Editor supports the creation of bullet charts.

Bullet charts are useful for showing performance against a target, or progress on a goal.

Using the [Chart Config Editor](https://docs.cloud.google.com/looker/docs/chart-config-editor), you can create bullet charts by starting from a bar chart in Looker.

For example, the following bullet chart compares the **New Customers Count** measure, represented by a blue progress bar, to a target value of 40, represented by a blue vertical line. The chart also indicates progress buckets between 0 and 20, between 20 and 40, and between 40 and 80, each represented by a different shade of grey.

![](https://docs.cloud.google.com/static/looker/docs/images/bullet-chart-244.png)

## Prerequisites

To access the Chart Config Editor, you must have the [`can_override_vis_config` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#can_override_vis_config).

### Writing the JSON snippet

To create a bullet chart, start from the following JSON snippet:
    
    
    {
      chart: {
        type: 'bullet'
      },
      xAxis: {
        categories: ['New Customers']
      },
      yAxis: {
        plotBands: [{
          from: 0,
          to: 20,
          color: '#666666'
        }, {
          from: 20,
          to: 40,
          color: '#999999'
        }, {
          from: 40,
          to: 80,
          color: '#bbbbbb'
        }],
      },
      series: [{
        data: [{
          target: 40
        }]
      }],
    }
    

Change the following values to fit your use case:

  * The `xAxis.categories` attribute overwrites the label of the X-axis. In this example, the X-axis label should be the measure name **New Customers**.
  * The `yAxis.plotBands` attribute specifies the background color of the chart for certain values. In this example, the background color is dark grey (`#666666`) between 0 and 20, medium grey (`#999999`) between 20 and 40, and light grey (`#bbbbbb`) between 40 and 80.
  * The `series.data.target` attribute specifies the target value for the bullet chart, which will appear as a vertical line. In this example, the target is 40.



### Creating a bullet chart

To create a bullet chart, follow these steps:

  1. View a [bar chart](https://docs.cloud.google.com/looker/docs/bar-options) in an Explore, or edit a bar chart in a Look or dashboard.

For this example, we recommend starting from a bar chart with one dimension and one measure, with a limit of one row. Your starting chart might look something like this example:

![Sample bar chart with a single bar that extends across the X-axis.](https://docs.cloud.google.com/static/looker/docs/images/bullet-chart-base-244.png)

  2. Open the **Edit** menu in the visualization.

  3. In the **Plot** tab, click the **Edit Chart Config** button. Looker displays the **Edit Chart Config** dialog.

  4. Select the **Chart Config (Override)** section, and enter the HighCharts JSON from the Writing the JSON snippet section of this page.

  5. To allow Looker to properly format your JSON, click **< > (Format code)**.

  6. To test your changes, click **Preview**.

  7. To apply your changes, click **Apply**. The visualization will be displayed using the custom JSON values.




![](https://docs.cloud.google.com/static/looker/docs/images/bullet-chart-editor-244.png)

Once you've customized your visualization, you can save it. If you viewed the visualization in an Explore, [save the Explore](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#the_explore_actions_gear_menu). If you edited a Look or a dashboard, click **Save**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
