---
url: https://docs.cloud.google.com/data-studio/zoom-and-pan-on-charts/
title: Zoom and pan on charts \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:29:40.215197+00:00
---

# Zoom and pan on charts  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/zoom-and-pan-on-charts/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Zoom and pan on charts Stay organized with collections  Save and categorize content based on your preferences. 

Zooming and panning can help you focus on specific areas of a data-dense visualization, such as when you want to highlight a portion of your data or review more granular details.

When the **Zoom** option is enabled for a Cartesian chart, you can zoom in to magnify a portion of that chart. After you zoom into a chart, you can also pan on that chart to view all the data that is present.

## Enable zoom and pan for a chart

**Important:** The **Zoom** option is not available when [chart cross-filtering](https://docs.cloud.google.com/data-studio/chart-cross-filtering) is enabled.

To enable zooming and panning on a chart, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select a chart from among the supported chart types.
  3. Scroll to the bottom of the **Setup** tab of the properties panel.
  4. In the **Chart interactions** section, select **Zoom**.
  5. Navigate to the **Style** tab of the properties panel. Under **Zoom** , select an option: 
     * **Click and drag to zoom** : Zoom by clicking and dragging to select the portion of the visualization that you want to magnify.
     * **Scroll to zoom** : Zoom by scrolling with your mouse.
  6. Optionally, for the following chart types, select the **Pan/Zoom X-axis only** checkbox to allow zooming and panning only along the X-axis: 
     * Area charts
     * Scatter and bubble charts
     * Time series charts



Repeat these steps for each chart for which you want to enable zooming and panning.

### Visualization support for zoom and pan

> Pan and zoom are only available in [view mode](https://docs.cloud.google.com/data-studio/view-mode).

When the **Zoom** option is enabled, the following Cartesian chart types support zooming and panning along the X-axis, the Y-axis, or both the X-axis and the Y-axis:

**Chart type** |  **Axis support for zoom and pan**  
---|---  
[ Area ](https://docs.cloud.google.com/data-studio/area-chart-reference) |  Support for pan and zoom along both the X-axis and the Y-axis   
[ Bar and column ](https://docs.cloud.google.com/data-studio/bar-chart-and-column-chart-reference) |  Support for pan and zoom along the X-axis for bar charts and along the Y-axis for column charts   
[ Line and combo ](https://docs.cloud.google.com/data-studio/line-chart-and-combo-chart-reference) |  Support for pan and zoom along the Y-axis   
[ Scatter and bubble ](https://docs.cloud.google.com/data-studio/scatter-chart-reference) |  Support for pan and zoom along both the X-axis and the Y-axis   
[ Time series ](https://docs.cloud.google.com/data-studio/time-series-reference) |  Support for pan and zoom along both the X-axis and the Y-axis   
  
## Zoom in and out of a section of a chart

To zoom in and out of a chart:

  1. View the chart.
  2. You can zoom in on the chart in one of the following ways:

     1. **Click and drag to zoom** : Zoom by clicking and dragging to select the portion of the visualization that you want to magnify.

     2. **Scroll to zoom** : Zoom by scrolling with your mouse. You can then pan on the chart to view more data points.

The zoom options for each chart can be configured in the **Zoom** section of the **Style** tab of the properties panel.

  3. To zoom out and reset the visualization to its default view, select the **Reset Zoom** button. If you are zooming in by scrolling, you can also use your cursor to scroll in and out of the chart without having to select **Reset Zoom**.




## Pan on a section of a chart

To pan on a section of a chart:

  1. View the chart.
  2. Hold down the shift key and drag your cursor to pan on a selection of the chart.
  3. To zoom out and reset the chart to its default view, select the **Reset Zoom** button.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-14 UTC."],[],[]] 
