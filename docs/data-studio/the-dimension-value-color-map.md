---
url: https://docs.cloud.google.com/data-studio/the-dimension-value-color-map/
title: The dimension value color map \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:05:11.912793+00:00
---

# The dimension value color map  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/the-dimension-value-color-map/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  The dimension value color map Stay organized with collections  Save and categorize content based on your preferences. 

The _dimension value color map_ is a table of the dimension values that appear in your report, with an associated color for each value. Charts that use the [color by dimension values](https://docs.cloud.google.com/data-studio/color-your-data) option get their colors from this map. The dimension value color map is created automatically from the data in your report. You can also edit the map directly to add values and change colors.

## How the dimension value color map works

### For editors

Whenever you add or edit a chart, any new dimension values that are displayed by that chart are added to the map. The colors in the map come from the report-level color theme that is currently in effect when the values are added.

#### Example

In a new blank report, the dimension value color map is empty. If you add a pie chart with the **Country** dimension and limit it to three slices, the dimension value color map now contains three values: one for each of the countries that appears in the chart.

![Three countries are represented on a pie chart: DE \(Germany\), FR \(France\), and IN \(India\) are assigned colors on the dimension value color map.](https://docs.cloud.google.com/static/data-studio/images/dimension-value-color-map-2017-09-21.png)

If you then edit the chart and increase the number of slices to 10, the new country values are added to the dimension value color map.

Next, you add a time series that is broken down by the **Source** dimension. The new dimension values are added to the map, so it now includes items like "  google ," "(  direct  )", "  youtube.com ," etc., along with colors for each value.

![The dimension value color map displays the Source dimension fields that were added to the report.](https://docs.cloud.google.com/static/data-studio/images/dimension-value-color-map-2-2017-09-21.png)

As you edit the report, only the dimension values that are actually displayed in the charts are added to the dimension value color map. Paginated charts, or charts that contain data only for certain date ranges, won't be added to the map until those values are actually displayed.

> The dimension value color map can contain a maximum of 1,000 entries. If the map exceeds this limit, you'll be prompted restore the default colors. Currently, there is no way to selectively remove values from the map.

### For viewers

When someone views dimension values that haven't been added to the dimension value color map, Looker Studio will select colors automatically. These colors might be different for different viewers, and they won't be added to the map.

## Manage dimension value colors

To edit the dimension value color map, follow either of these methods:

  * From the **Theme and Layout** panel, on the **THEME** tab, in the **Primary styles** section, click **Manage dimension value colors**.
  * From the **Resource** menu, click **Manage dimension value colors**.



####  Add a new value to the map 

To add an individual value to the dimension value color map, follow these steps: 

  1. Edit the dimension value color map by using one of the methods  that was described previously . 
  2. Click **Add a value**. 
  3. Click the color swatch to select a new color, if desired. 
  4. Enter the new dimension value. 
  5. Click **CREATE VALUE**. 



![A new purple color for the value Fred is added to the Dimension value colors menu.](https://docs.cloud.google.com/static/l/data-studio/ages/add-dim-color-2017-09-21.png) /><>

####  Change the color of an existing value 

To change a dimension value's color, follow these steps: 

  1. Edit the dimension value color map by using one of the methods  that was described previously . 
  2. Locate the dimension value to be changed (use the **Search** box on the right if you have a lot of values). 
  3. Click the color swatch for that dimension value. 
  4. Select the new color. 



####  Restore default colors 

To reset the dimension value color map, follow these steps: 

  1. Edit the dimension value color map by using one of the methods  that was described previously . 
  2. Click **RESTORE DEFAULT COLORS**. 



![](https://data-studio/mages/restore-default-colors-2017-09-21.png)

Important: Restoring the dimension value color map will discard any values that you've added manually. In addition, the new map will only contain values for the charts that are currently displayed on the report page. **Restoring the colors cannot be undone** , so proceed with caution. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-14 UTC."],[],[]] 
