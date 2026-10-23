---
url: https://docs.cloud.google.com/looker/docs/editing-visualizations-new-explore-experience/
title: Configuring and editing visualizations in the new Explore experience \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:49.245754+00:00
---

# Configuring and editing visualizations in the new Explore experience  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/editing-visualizations-new-explore-experience/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Configuring and editing visualizations in the new Explore experience Stay organized with collections  Save and categorize content based on your preferences. 

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This page is part of the [new Explore experience preview feature](https://docs.cloud.google.com/looker/docs/new-explore-experience-overview) series.

This page guides you through the visualization components of the new Explore experience and describes how to edit and configure visualizations in the new Explore experience. Read the following sections to learn about these concepts:

  * Required roles
  * Accessing the new Explore experience
  * Visualization limitations in the new Explore experience
  * Changing the visualization type
  * Navigating visualization settings in the **Style** tab
  * Related resources



## Required roles

To view and interact with Explores and visualizations, you must have the **User** [Looker role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) or another role that contains the [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permission.

## Accessing the new Explore experience

To access the new Explore experience, the [**New Looker Explore and Merge Query Experience**](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#new-looker-explore-and-merge-query-experience) preview feature must be enabled for your instance. The preview feature is enabled by default. If it is disabled, and you aren't a Looker admin, ask an admin to enable the feature.

From an Explore page, click **Try the new Explore** to turn on the new Explore experience for all Explores that you interact with. To switch back to the classic experience, click **Switch to classic Explore**.

## Visualization limitations in the new Explore experience

Although there are many charts listed in the **All chart types** menu, the new Explore experience supports only the following visualization types:

  * Area charts
  * Bar charts
  * Boxplot charts
  * Column charts
  * Donut multiples charts
  * Funnel charts
  * Google maps charts
  * Line charts
  * Pie charts
  * Scatterplot charts
  * Single record charts
  * Single value charts
  * Table charts
  * Timeline charts
  * Waterfall charts
  * Word cloud charts



If you select an unsupported chart type, the visualization will render the Explore data, but there will be no configuration options available in the **Style** tab.

**Tip:** If you would like to edit or configure an unsupported visualization type, you must switch to the classic Explore experience to access the chart settings. The configuration will carry over when you switch back to the new Explore experience.

## Changing the visualization type

Visualizations are displayed in the [**Visualization** pane](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-new-explore-experience#navigating-the-new-explore-experience) in the new Explore experience. When you [open an Explore](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-new-explore-experience#finding-explores-in-looker), you can [make changes to the query](https://docs.cloud.google.com/looker/docs/creating-and-editing-new-explore-experience) and make changes to the visualization that appears.

To change the visualization type in the new Explore experience, follow these steps:

  1. Click the add_chart **Change chart** button to open the **All chart types** menu.
  2. Choose a chart type from the menu. Alternatively, you can click **Auto visualize** to let Looker choose the best chart option for displaying the results.



The new chart type will display in the **Visualization** pane.

**Note:** When a query is running, the visualization pane displays the three phases of the query in the [Explore query tracker](https://docs.cloud.google.com/looker/docs/query-tracker#explore_query_tracker).

## Navigating visualization settings in the Style tab

Once you have chosen a visualization type, you can use the [**Style** tab in the **Configure** panel](https://docs.cloud.google.com/looker/docs/creating-and-editing-new-explore-experience#navigating-the-configure-panel) to edit or configure the chart settings.

In the **Style** tab, the configuration options are organized into expandable sections that have the same names as the tabs in the classic Explore experience. Each section in the new Explore experience also includes the same configuration options as the classic Explore experience.

To view the options in each section, click the section name. To collapse the section, click the section name again.

### Style options for area charts, bar charts, boxplot charts, column charts, line charts, and scatterplot charts

For area charts, bar charts, boxplot charts, column charts, line charts, and scatterplot charts, the sections include the following:

  * **Plot** : Options to control the overall layout, spacing, and organization of a chart.
  * **Series** : Options to manage color schemes, field naming conventions, and granular per-series customizations.
  * **Values** : Options to customize the appearance, formatting, and behavior of data labels within a chart.
  * **X** : Options to configure the horizontal axis, including its scale, labels, and interactive features.
  * **Y** : Options to configure the vertical axes for precise control over scaling, labeling, and analytical overlay.

**Important:** The new Explore experience supports configuring only one Y axis. Switch to the classic Explore experience to configure multiple Y axes. The configuration will carry over when you switch back to the new Explore experience.



To earn more about configuration options for charts, see the following topics:

  * [area chart configuration options](https://docs.cloud.google.com/looker/docs/area-options)
  * [bar chart configuration options](https://docs.cloud.google.com/looker/docs/bar-options)
  * [boxplot chart configuration options](https://docs.cloud.google.com/looker/docs/boxplot-options)
  * [column chart configuration options](https://docs.cloud.google.com/looker/docs/column-options)
  * [line chart configuration options](https://docs.cloud.google.com/looker/docs/line-options)
  * [scatterplot chart configuration options](https://docs.cloud.google.com/looker/docs/scatter-options).



### Style options for donut multiples charts and pie charts

For donut multiples charts and pie charts, the sections include the following:

  * **Plot** : Options to control the overall layout and size of the chart.
  * **Series** : Options to manage color schemes.



Learn more about [donut multiples chart configuration options](https://docs.cloud.google.com/looker/docs/donut-multiples-options) and [pie chart configuration options](https://docs.cloud.google.com/looker/docs/pie-options).

### Style options for funnel charts

For funnel charts, the sections include the following:

  * **Bars** : Options to control the colors, orientation, and label scale of the chart.
  * **Labels** : Options to manage the position and appearance of bar labels.
  * **Axes** : Options to display axis labels.



[Learn more about funnel chart configuration options](https://docs.cloud.google.com/looker/docs/funnel-options).

### Style options for Google maps charts

For Google maps charts, the sections include the following:

  * **Plot** : Options to control the type and appearance of the chart.
  * **Map** : Options to map style, position, and interactive features.



[Learn more about Google maps charts configuration options](https://docs.cloud.google.com/looker/docs/google-map-options).

### Style options for single record charts

For single record charts, the sections include the following:

  * **Style** : Option to customize the appearance of the field name.



[Learn more about single record chart configuration options](https://docs.cloud.google.com/looker/docs/single-record-options).

### Style options for single value charts

For single value charts, the sections include the following:

  * **Style** : Options to customize the appearance of the primary value and its title.
  * **Comparison** : Options to incorporate a second data field for providing context or performance metrics relative to the primary value.
  * **Formatting** : Options to apply conditional formatting to color-code a visualization based on specific data values.



[Learn more about single value chart configuration options](https://docs.cloud.google.com/looker/docs/single-value-options).

### Style options for table charts

For table charts, the sections include the following:

  * **Plot** : Options to customize the layout and theme of a chart.
  * **Series** : Options to customize the layout and formatting of individual columns.
  * **Formatting** : Options to customize the visual style and apply data-driven coloring to the chart.



[Learn more about table chart configuration options](https://docs.cloud.google.com/looker/docs/table-options).

### Style options for timeline charts and word cloud charts

For timeline charts and word cloud charts, the sections include the following:

  * **Style** : Option to customize the colors and appearance of the chart.



Learn more about [timeline chart configuration options](https://docs.cloud.google.com/looker/docs/timeline-options) and [word cloud chart configuration options](https://docs.cloud.google.com/looker/docs/word-cloud-options).

### Style options for waterfall charts

For waterfall charts, the sections include the following:

  * **Series** : Options to customize the colors and appearance of the chart.
  * **Values** : Option to customize the chart labels.
  * **X** : Options to configure the horizontal axis, including its scale, labels, and interactive features.
  * **Y** : Options to configure the vertical axes for precise control over scaling, labeling, and analytical overlay.



[Learn more about waterfall chart configuration options](https://docs.cloud.google.com/looker/docs/waterfall-options).

### Using the Visualization Assistant in the new Explore experience

The [Visualization Assistant](https://docs.cloud.google.com/looker/docs/custom-looker-visualization-gemini), which lets you customize a Looker visualization by using Gemini in Looker, is available in the new Explore experience. The Visualization Assistant in the new Explore experience includes an updated conversational panel that supports multi-turn chats, displaying compact visualization renderings at each turn, letting you iterate your visualization customizations.

To customize a visualization with the **Visualization Assistant** , follow these steps:

  1. When viewing a visualization in an Explore, click the **Style** tab.

  2. Click pen_spark **Visualization Assistant** to open the prompt window.

![A Looker visualization with the Visualization Assistant prompt menu open.](https://docs.cloud.google.com/static/looker/docs/images/vis-asst-new-explore-2610.png)

  3. In the Visualization Assistant prompt field, describe any changes that you want to make to the visualization.




For more information about using the Visualization Assistant, see the [Create visualizations with Gemini assistance](https://docs.cloud.google.com/looker/docs/custom-looker-visualization-gemini) documentation page.

## Related resources

Now that you know how to edit and configure visualizations in the new Explore experience, you might want to learn how to do the following:

  * Learn how to [view and interact with Explores in the new Explore experience](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-new-explore-experience).
  * Learn how to [create or edit Explores in the new Explore experience](https://docs.cloud.google.com/looker/docs/creating-and-editing-new-explore-experience).
  * Learn about [creating visualizations and graphs](https://docs.cloud.google.com/looker/docs/creating-visualizations).
  * Learn about [selecting an effective data visualization](https://docs.cloud.google.com/looker/docs/visualization-guide).
  * Learn about [using color collections](https://docs.cloud.google.com/looker/docs/color-collections).
  * Learn how to [create custom tooltips](https://docs.cloud.google.com/looker/docs/custom-tooltips).
  * Learn how to [save Explore queries as Looks](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks).
  * Learn how to [add Explore queries to dashboards](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#creating_a_dashboard_from_a_look_or_an_explore).
  * Learn how to [share data](https://docs.cloud.google.com/looker/docs/sharing-data) with other users.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
