---
url: https://docs.cloud.google.com/data-studio/add-drill-actions-to-charts/
title: Add drill actions to charts \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:31:48.840258+00:00
---

# Add drill actions to charts  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/add-drill-actions-to-charts/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Add drill actions to charts Stay organized with collections  Save and categorize content based on your preferences. 

Drill actions can make charts more interactive, reduce the number of charts in a report, and make it easier for users to find additional context about data.

For example, suppose you want to view session data by both country and city. Rather than include two charts in your report, you can include a single chart with drill actions enabled.

This page provides an overview of the different types of drill actions in Data Studio and how to implement them in charts.

For more information about how to use drill actions when viewing reports, view the [Drill into your data](https://docs.cloud.google.com/data-studio/drill-into-your-data) tutorial page.

## Drill actions in Data Studio

Drill actions let you view levels of detail and more context about the data in a chart.

There are several types of drill actions:

  * The **Drill Down** drill action lets users drill from a higher level of detail to a lower one (for example, drill down from **Country** to **City** ) and from a lower level of detail to a higher one (for example, drill up from **City** to **Country**).

The **Drill Down** setting also lets users change or swap the dimensions that are on a report. For example, if **Country** , **State** , and **City** are available drill fields, a user can swap between them on a chart to break down metrics for a different granularity without drilling up or drilling down.

  * The **Drill Through** drill action lets users navigate to related content with a preset URL.


**Important:** The **Drill Through** drill action is available only for dimensions on [table charts](https://docs.cloud.google.com/data-studio/table-reference).

### Table chart drill actions example

In table charts, drill actions are presented to users in the tooltip that appears when they put their cursor over a data point in a chart.

For example, if a user puts their cursor over the state **California** in table chart that displays FAA flight count by destination, they can click the **Drill actions** option to see the options that are available for drilling into the data.

![Drill actions in the tooltip for California include a switch to Filter on California, drill fields DestStateName, DestCityName, and Dest, and a drill through link for a Google search by State.](https://docs.cloud.google.com/static/data-studio/images/looker-studio-drill-actions-tooltip-example.png)

The user can then take one of several actions. For example:

  * The user can swap the **DestStateName** dimension for either the **DestCityName** or **Dest** dimensions to display the **Record Count** aggregations for cities or airports instead of states.

  * The user can turn on the **Filter on "California"** switch to limit the chart results to **California**.

  * The user can click the up and down arrows in the **Drill Actions** menu header to switch the level of granularity on a chart.

  * The user can turn on the **Filter on "California"** switch to display more granular record counts for **DestCityName** or **Dest** that are in **California**.

  * The user can click **State Google search** to drill through to a Google search for more context about a state.




### Column chart drill actions example

In other chart types, such as [column charts](https://docs.cloud.google.com/data-studio/bar-chart-and-column-chart-reference), users can drill up or drill down by using one of these options:

![](https://docs.cloud.google.com/static/data-studio/images/looker-studio-chart-hover-options-drill.png)

  1. The **Drill** **up** and **Drill down** arrows that appear in a chart's header when a user puts their cursor over a chart
  2. The **Drill up** or **Drill down** options in the three-dot **More** menu that appears in a chart's header when a user puts their cursor over a chart



Alternatively, **Drill up** or **Drill down** options are available when a user right-clicks on a chart.

For example, if a user clicks the **Drill down** arrow in a column chart that displays FAA flight count by destination state, the chart will display the chart data for the next dimension that is defined in the drill hierarchy, which is **DestCityName**.

![The Drill down arrow displays the text Drill down from DestStateName to DestCityName.](https://docs.cloud.google.com/static/data-studio/images/looker-studio-column-chart-drill-example.png)

## Requirements for the Drill Down drill action

To add drill down capability to a chart, you need to define a dimension hierarchy. The hierarchy specifies the levels of detail that a chart can display when users drill down or up. Example hierarchies include the following:

  * Date (Year, Month, Day)
  * Geography (Country, Region, City)
  * Product (Department, Category, SKU)
  * Google Analytics events (Event Category, Event Action, Event Label)

**Important:** The order in which you list dimensions within a hierarchy matters. As a best practice, you should define hierarchies from the most general granularity to the most specific granularity. For example, the geographic hierarchy **Country, City, Region** can produce undesirable results because it flows from a general level to a more detailed level and then back to a more general level.

## Add drill actions to table charts

Adding drill actions is different for table charts than for other types of charts.

### Add a Drill Down action to table charts

To add the **Drill Down** drill action to table charts, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. [Add a new chart](https://docs.cloud.google.com/data-studio/add-charts-and-controls-to-your-report) or select an existing chart.
  3. In the **Properties** panel, click the **Setup** tab.
  4. In the **Dimension** section, click the field's data type icon to [edit the field](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports).
  5. Click **Add Drill Action** to open the **Add Drill Action** menu.
  6. In the **Drill Down** section, click and place dimensions from the **Data** panel or click **\+ Add Field** to add dimensions. Each dimension that you add becomes another level of detail that users can drill into or swap on a chart. You can change the order of dimensions by dragging and dropping the dimensions that are listed in the **Drill Down** section to set the drill hierarchy.
  7. Click the **Apply** button at the bottom of the **Add Drill Action** menu.

**Tip:** You can add **Drill Down** drill actions to multiple dimensions on a table chart.

### Edit or remove Drill Down fields from table charts

To edit or remove drill down fields from a table chart, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).

  2. Select the chart that you want to edit.

  3. In the **Properties** panel, click the **Setup** tab.

  4. In the **Dimension** section, click the field's data type icon to [edit the field](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports).

  5. Click **Add Drill Action** to open the **Add Drill Action** menu.

  6. In the **Drill Down** section, you can edit or remove drill fields.

     1. To **edit** fields, click and place dimensions from the **Data** panel or click **\+ Add Field** to add additional dimensions. You can also change the order of dimensions by dragging and dropping the dimensions that are listed in the **Drill Down** section.

     2. To **remove** a field, put your cursor over a field name, and click the inline **X** icon that appears.

  7. Click the **Apply** button at the bottom of the **Add Drill Action** menu.




### Add Drill Through links to table charts

To enable the **Drill Through** drill action for table charts, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).

  2. [Add a new chart](https://docs.cloud.google.com/data-studio/add-charts-and-controls-to-your-report) or select an existing chart.

  3. In the **Properties** panel, click the **Setup** tab.

  4. In the **Dimension** section, click the field's data type icon to [edit the field](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports).

  5. Click **Add Drill Action** to open the **Add Drill Action** menu.

  6. In the **Drill Through** section next to **Drill Through Link** , click **\+ Add URL** to expand the drill through link customization options.

  7. In the **Display Name** text field, enter the descriptive text that you would like users to see in the **Drill actions** menu of a chart tooltip. For example, if you link to a related Salesforce page, you can set the display text to **"Navigate to Salesforce"**.

  8. In the **URL** text field, enter the webpage URL.

  9. Click the **Save** button to save your settings. Alternatively, you can click **Cancel** to close the customization options for the drill through link.

  10. To add additional drill through links, repeat steps 6 through 9.

  11. Click the **Apply** button at the bottom of the **Add Drill Action** menu.


**Tip:** You can add multiple **Drill Through** links to a dimension.

### Edit or remove Drill Through links from table charts

To edit or remove drill through links from a table chart, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).

  2. Select the chart that you want to edit.

  3. In the **Properties** panel, click the **Setup** tab.

  4. In the **Dimension** section, click the field's data type icon to [edit the field](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports).

  5. Click **Add Drill Action** to open the **Add Drill Action** menu.

  6. In the **Drill Through** section, you can edit or remove links.

     1. To **edit a** link, select the link name to expand the drill through link customization options. Make any changes to the **Display Name** or **URL** fields.

     2. To **remove** a URL, select the link name to expand the drill through link customization options and click the trash can icon.

  7. At the bottom of the **Add Drill Action** menu, click the **Apply** button.




## Add drill actions to other chart types

To add drill actions to other charts, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).

  2. [Add a new chart](https://docs.cloud.google.com/data-studio/add-charts-and-controls-to-your-report) or select an existing chart.

  3. In the **Properties** panel, click the **Setup** tab.

  4. In the **Dimension** section, turn on the **Drill down** switch to expand the drill options section.

  5. Click and place dimensions from the **Data** panel or click **\+ Add Field** to add dimensions to the **Dimension** section. Each dimension that you add becomes another level of detail that you can drill into.

You can change the order of dimensions by dragging and dropping the dimensions that are listed in the **Dimension** section to set the drill hierarchy.

  6. Select a dimension from the **Default drill down level** drop-down menu to set a default dimension for the chart.


**Important:** Drill actions are not available for dimensionless charts such as scorecards and bullet charts.

### Edit or remove drill actions from other chart types

To turn off drill actions for other charts, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).

  2. Select the chart that you want to edit.

  3. Click the **Setup** tab in the **Properties** panel.

  4. In the **Dimension** section, you can edit or remove drill fields or turn off drill actions.

     1. To **edit** drill fields, click and place dimensions from the **Data** panel or click **\+ Add Field** to add additional dimensions. You can also change the order of dimensions by dragging and dropping the dimensions that are listed in the **Dimension** section.

Additionally, you can select a different dimension from the **Default drill down level** drop-down menu to change the default dimension for the chart.

     2. To **remove** a field, put your cursor over a field name, and click the inline **X** icon that appears.

     3. To **turn off** drill actions, turn off the **Drill down** switch.




## Drill action limitations and considerations

  * Drill actions are not available for community visualizations.

  * Drill actions are not available for dimensionless charts such as scorecards and bullet charts.

  * Drill fields and links that are [imported from Looker data sources](https://docs.cloud.google.com/data-studio/connect-to-looker) are **read-only**. To make changes to imported drill actions, [edit the underlying LookML model](https://docs.cloud.google.com/looker/docs/lookml-validation) in Looker.

  * You can see additional levels of detail in pivot tables by turning on expand-collapse. You can then show or hide the data from the dimension hierarchy in the pivot table by clicking **+** and **–** in the column header. [Learn more about pivot tables](https://data-studio/ivot-table-reference).

  * Geo charts don't support all geographic field types within all zoom areas. See the [Geo chart reference](https://docs.cloud.google.com/data-studio/geo-chart-reference) for more details.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
