---
url: https://docs.cloud.google.com/data-studio/tutorial-add-charts-to-your-report/
title: Tutorial: Add charts to your report \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:51.673894+00:00
---

# Tutorial: Add charts to your report  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/tutorial-add-charts-to-your-report/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Tutorial: Add charts to your report Stay organized with collections  Save and categorize content based on your preferences. 

Use charts to visualize and explore your data. In this lesson, you'll add a pie chart, a bar chart and a Geo chart to this report.

**Important:** This page assumes you are using the `[Sample] Google Analytics Data` [data source](https://docs.cloud.google.com/data-studio/data-source), as described in the [Create a new report](https://docs.cloud.google.com/data-studio/tutorial-create-a-new-report) tutorial. If you are using a different data source, you may need to select the appropriate dimensions and metrics for each chart.

## How to add a chart

To add a chart to the current page:

  1. Edit your report.
  2. Navigate to the page that will contain the chart.
  3. In the toolbar, click **Add a chart**.
  4. Select the chart you want to add.
  5. Click the canvas to add the chart to the report.
  6. Select one or more charts to move or resize them as needed.



## Step 1: Add a pie chart

![School icon.](https://docs.cloud.google.com/static/data-studio/images/icschoolgrey60024dp-2014-12-01-image.png) Use a pie chart to give a general comparison of a small number of metrics or variables.

[Learn more about pie charts](https://docs.cloud.google.com/data-studio/pie-chart-reference).

![](https://docs.cloud.google.com/static/data-studio/images/pie-chart-example-2015-09-17.png)

  1. Following the steps in [How to add a chart](#how-to-add-a-chart), add a **Pie Chart** to the report.
  2. In the **Properties** panel, select the **SETUP** tab.
  3. Click the **Source** dimension chip to access the **Dimension Picker**.
  4. Click the **User Type** dimension.
  5. Click the **STYLE** tab.
  6. Use the donut slider to change the solid shape to a ring shape. ![](https://docs.cloud.google.com/static/data-studio/images/piechart-donut-slider-2015-11-05.png)
  7. Use the **Legend** property to position the metric labels under the pie: ![Label position.](https://docs.cloud.google.com/static/data-studio/images/label-position-2015-09-17.png)

**Tip:** Use the **Dimension Picker's** search box to find dimensions and metrics quickly: ![Search icon.](https://docs.cloud.google.com/static/data-studio/images/search-icon-2015-09-18.png)

## Step 2: Add a bar chart

![School icon.](https://docs.cloud.google.com/static/data-studio/images/icschoolgrey60024dp-2014-12-01-image.png) Bar charts are great for showing and comparing the magnitude of multiple variables.

[Learn more about bar charts](https://docs.cloud.google.com/data-studio/bar-chart-and-column-chart-reference).

![Bar chart displays web browser data.](https://docs.cloud.google.com/static/data-studio/images/bar-chart-example-2015-09-18.png)

  1. Following the steps in How to add a chart, add a **Bar Chart** to the report.
  2. In the **Properties** panel, select the **SETUP** tab.
  3. Click the **Source** dimension and change it to **Browser**.
  4. Click the return arrow: ![Return arrow icon.](https://docs.cloud.google.com/static/data-studio/images/return-arrow-icon-2015-09-18.png)
  5. Click the **Sessions** metric and change it to **Users**.
  6. Click the **STYLE** tab.
  7. Change the orientation to **Horizontal** : ![Horizontal orientation icon.](https://docs.cloud.google.com/static/data-studio/images/bar-chart-horizontal-icon-2015-09-18.png)
  8. Scroll to the **Background and Border** section of the **STYLE** tab.
  9. Set the **Border color** to gray: ![Border color icon.](https://docs.cloud.google.com/static/data-studio/images/border-color-icon-2015-09-01.png)



## Step 3: Add a Google Map

![School icon.](https://docs.cloud.google.com/static/data-studio/images/icschoolgrey60024dp-2014-12-01-image.png) Use a Google Map to see the distribution of sessions (or other metrics) across the world.

**Note:** For Google Analyticss data, Data Studio automatically selects the geographic dimension. If you are using a different data source, be sure it contains a valid geo dimension.

[Learn more about Google Maps](https://docs.cloud.google.com/data-studio/google-maps-reference).

![A bubble map chart of the world displays countries in various shades of red with the United States in dark red, and a red gradient scale ranging from 1 to 35.556 underneath.](https://docs.cloud.google.com/static/data-studio/images/geomap-example-2015-09-18.png)

  1. Following the steps in How to add a chart, add a **Google Map** to the report. Choose the bubble map style.
  2. In the **Properties** panel, select the **SETUP** tab.
  3. Click the default **Location** field and replace it with the **City** dimension.
  4. Add metrics for bubble color and bubble size. For example, select **Sessions** for **Size** , and **Average time on Page** for **Color**.
  5. Select the **Style** tab.
  6. Use the sliders to adjust the background details, such as roads, landmarks, and labels.
  7. In the **Colors** section, select colors for the range of metric values.
  8. In the **Map Controls** section, turn on or off the map controls you want to let your viewers use.
  9. View your report. Pan, zoom, and scroll. You can also use [Street View](https://www.google.com/streetview/)!



## Next step

Congratulations! You've created your first Data Studio report!

If you'd like, add titles, change colors and styles, add more visualizations. When you're ready to move on, begin the next lesson: [View and share your report](https://docs.cloud.google.com/data-studio/tutorial-view-and-share-your-report).

## Related resources

[Types of charts in Data Studio](https://docs.cloud.google.com/data-studio/types-of-charts)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
