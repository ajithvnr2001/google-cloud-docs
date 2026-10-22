---
url: https://docs.cloud.google.com/data-studio/add-charts-and-controls-to-your-report/
title: Add charts and controls to your report \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:49.437951+00:00
---

# Add charts and controls to your report  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/add-charts-and-controls-to-your-report/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Add charts and controls to your report Stay organized with collections  Save and categorize content based on your preferences. 

You can add charts and controls to your Data Studio report to visualize data and create interactive user experiences. Charts transform data into visual graphics, while controls let viewers filter data, select date ranges, or enter parameter values. You can combine and customize these components to build clear, engaging reports for your team.

Before you begin, you should be familiar with the following topics:

  * [How to create a report](https://docs.cloud.google.com/data-studio/tutorial-create-a-new-report)
  * [How to edit a report](https://docs.cloud.google.com/data-studio/edit-a-report)

**Important:** Some of the features described on this page are not supported for responsive reports. Check the [Limitations of responsive reports](https://docs.cloud.google.com/data-studio/create-a-responsive-report#limitations) section of the **Create a responsive report** article for a list of unsupported features.

## Add a chart to a report

Data Studio comes with a number of preconfigured charts that you can add to your report and then customize as needed. To learn more about specific charts, see the [chart references](https://docs.cloud.google.com/data-studio/types-of-charts).

To add a chart to the report, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Navigate to the page that will contain the chart.
  3. In the tool bar, click **Add a chart.** Important: You cannot add more than 50 charts to a [page of a report](https://docs.cloud.google.com/data-studio/add-pages-and-report-navigation).
  4. Select the chart you want to add.
  5. Click the canvas to add the chart to the report.
  6. On the right, configure the chart using the [properties panel](https://docs.cloud.google.com/data-studio/properties-panel).



> You can also add visualizations created by the [Data Studio developer community](https://docs.cloud.google.com/data-studio/community-visualizations-developer-preview).

## Add a control to a report

Controls, such as dimensions filters, date range controls, and the data control, make reports interactive by letting viewers customize the data displayed in your reports.

To add a control to the report, follow these steps:

  1. Edit your report.
  2. In the toolbar, select ![Control icon.](https://docs.cloud.google.com/static/data-studio/images/filterlistgrey6002x48dp-2020-09-09.png)**Add a control**.
  3. Select the control type, and then position it on your chart.
  4. On the right, configure the chart with the settings in the [**Properties** panel](https://docs.cloud.google.com/data-studio/properties-panel).

     1. To filter the report by selected dimension values, use a dimension for the **Control field**.
     2. To set the value of a parameter, use that parameter as the **Control field**.
     3. To change the appearance of the data control, use the options in the **Style** tab of the properties panel.

Learn more [about controls](https://docs.cloud.google.com/data-studio/about-controls).




## Switch chart types

![](https://docs.cloud.google.com/static/data-studio/images/viz-switcher-gray-55-2022-06-06.png)

You can switch between chart types without having to create a new chart. This lets you see how your data looks when you use different visualization techniques. To switch between chart types, follow these steps:

  1. Select a chart.
  2. In the properties panel, expand expand_more **Chart types**.
  3. Select the new chart type.



Data Studio adjusts the default dimensions and metrics to best suit the selected chart type. Any customizations that you've made to the chart, including adding or changing dimensions and metrics, style options, filters, or segments, are preserved so that you can switch back to the chart that was selected originally.

You can also switch between control types in a similar fashion.

## Add other components to a report

Use the toolbar icons or the **Insert** menu to add other components to the current page. Besides adding charts and controls, you can add the following kinds of components to your reports by following these steps:

  * **Images, text boxes, rectangles, lines,** and **circles** add stylistic elements, letting you brand your reports and make them visually appealing. Learn more about [adding design components](https://docs.cloud.google.com/data-studio/add-text-images-lines-and-shapes-to-your-reports).
  * **Embedded external content** , such videos, Google Docs, and external websites, lets you create reports that integrate a wide variety of content. Learn more about [embedding external content](https://docs.cloud.google.com/data-studio/embed-external-content-in-reports).



## Change report arrangement and layout

Use the options in the **View** and **Arrange** menus to control where components appear on the report canvas.

For example, when you place new objects on the canvas or move them with the mouse or keyboard, you can choose whether or not they snap to the report grid. Options in the **Arrange** menu let you align components and distribute them on the report page.

Learn more about [report layout options](https://docs.cloud.google.com/data-studio/report-and-page-layout) and [arranging and grouping components on the page](https://docs.cloud.google.com/data-studio/arrange-group-and-distribute-components).

## Arrange, move, or resize multiple components at once

You can move, resize, and arrange multiple components at once. Hold down the Ctrl key (PC) or the command key (Mac), and click the components that you want to work with (this action is known as _multi-selecting_ ). Then, perform an action to apply it to all the selected items.

For example, you can resize several charts at once, as demonstrated in the following video:

Other multi-select actions include editing shared properties, grouping, aligning, copying, and deleting.

## Related resources

  * [Troubleshoot chart and report errors](https://docs.cloud.google.com/data-studio/troubleshooting-guide)
  * [Make reports interactive](https://docs.cloud.google.com/data-studio/about-controls)
  * [Chart references](https://docs.cloud.google.com/data-studio/types-of-charts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
