---
url: https://docs.cloud.google.com/monitoring/charts/breakdown-chart-by-labels/
title: Break down a chart by labels \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:23.321002+00:00
---

# Break down a chart by labels  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/charts/breakdown-chart-by-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Break down a chart by labels Stay organized with collections  Save and categorize content based on your preferences. 

The breakdown feature in Metrics Explorer lets you divide a chart into a grid of tiles, where each tile displays time-series data for a specific label key or value. You can use these views to find spikes, dips, or trends that aggregation might hide and determine whether specific resource types or locations are causing an issue.

## Why you should break down your chart

Breaking down a chart by labels helps you identify root causes by isolating data for specific resource types or locations.

Metrics Explorer supports a two-phased breakdown. In the initial phase, it displays the chart and a grid of tiles, where each tile displays a chart and is for a specific label key. If you select a tile, then Metrics Explorer breaks down the data by label value.

In both modes, the tiles can show spikes, dips, and trends that are typically hidden by aggregation. This breakdown helps you identify which factors are contributing to an issue and refine your analysis by applying filters directly from the tiles.

The following chart illustrates this:

![Chart displaying aggregated time-series data as a single, relatively flat line.](https://docs.cloud.google.com/static/monitoring/images/breakdown-aggregated-data.png)

This chart shows a single time series where the values are not changing significantly. However, this chart hides underlying data. How many time series are combined? Are there any time series with significant spikes, dips, or trends?

In contrast, the following image shows the same chart, but the data is broken down by key:

![Breakdown view with multiple time-series tiles, including one that shows a significant data spike.](https://docs.cloud.google.com/static/monitoring/images/breakdown-broke-down-data.png)

The breakdown shows multiple time series with data collected from various regions and different machine types. It also shows a data spike that might be related to resources in a specific region or to an application.

## Before you begin

  * To get the permissions that you need to break down a chart by labels, ask your administrator to grant you the [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * This page assumes that you are viewing a chart by using Metrics Explorer and that you want to investigate the data you are viewing.

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)




## Break down a chart

To break down your chart by labels:

  1. In the toolbar of Metrics Explorer, select **Show breakdown**.

The display updates to show a split screen with the following panes:

     * Your chart.
     * A menu with the text **Breakdown by label**.
     * A collection of tiles. Each tile displays a chart, a label key, and a **Breakdown** button. Each tile corresponds to a key associated with your metric and resource labels.

The two earlier images in this document illustrate a chart and the tiles that show the data grouped by key.

  2. When you display a breakdown by label key, you have two options:

     * Select **Close breakdown** to return to Metrics Explorer.

     * On a tile, select **Breakdown**. This applies a breakdown for a specific label key and updates the tiles pane. The updated pane displays each tile with the label value and an **Add Filter** button.

**Note:** This action helps identify when a tile displays spikes, dips, trends, or unexpected values.

For example, if you select **Breakdown** on the `zone` tile, you see a tile for each zone with metric data:

![Display one tile for each zone.](https://docs.cloud.google.com/static/monitoring/images/breakdown-filter-zone-tile.png)

  3. When you display a breakdown by a specific label, you have two options:

     * Select _arrow_back_ **Back** on the toolbar that displays that button and text similar to **Select a value for some-key**.

You return to the split screen that shows a breakdown by label key.

     * On a tile, select **Add Filter**.

**Note:** If you add or remove a filter, you change the chart's query. Changes to filters are retained when you return to Metrics Explorer.

For example, if you select **Add Filter** on the `us-east1-b` tile, your query includes the filter `zone=us-east1-b`. Your chart and the tiles show only time series that match the filter. The tiles pane also doesn't display a tile for the `zone` key.

  4. Optional: Break down your chart by additional label keys.

  5. To return to Metrics Explorer, select **Close breakdown**.




You can perform these actions at any time:

  * Remove filters. To remove a filter, select _close_ **Close** on the filter.
  * Use the menu and search fields to find a specific label.
  * Save your chart to a custom dashboard.



## Limitations

  * You can only break down line charts. This feature isn't available for other types of charts, such as heatmaps.

  * You can't save the split screen, which shows your chart and a breakdown by key.




## What's next

  * [Explore charted data](https://docs.cloud.google.com/monitoring/charts/working-with-charts): Describes how to use chart controls to highlight time series, change the chart resolution, show outliers, and compare current to past data.

  * [Set chart display options](https://docs.cloud.google.com/monitoring/charts/chart-view-options): Describes how to change the visual display of your chart.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
