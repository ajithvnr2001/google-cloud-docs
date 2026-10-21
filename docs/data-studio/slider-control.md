---
url: https://docs.cloud.google.com/data-studio/slider-control/
title: Slider control \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:11:26.749034+00:00
---

# Slider control  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/slider-control/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Slider control Stay organized with collections  Save and categorize content based on your preferences. 

Slider controls let you filter by a range of values in a numeric dimension, or select a single value from a numeric parameter.

## Slider DATA options

Most of the DATA options only apply to controls as filters. To configure parameter data options, edit the parameter in the data source.

### Data Source

Provides the dimensions and parameters you can use in the control.

#### Date range dimension

This option appears if your data source has a valid date dimension. For Google Ads and Analytics data sources, this option is automatically set to the **Date** dimension.

The Date Range Dimension is used as the basis for limiting the date range of the chart. For example, this is the dimension used if you set a date range property for the chart, or if you use a date range control to limit the time frame.

### Dimension

Provides the list of values that appear in the control.

#### Control field

The dimension to filter by or the parameter whose value is set by this control.

#### Default selection

Specify default values, separated by commas. Be sure to enter the values exactly as they appear in your data.

### Order

#### Show top N

Limits the number of items displayed in the control to the top N values.

### Default Date Range

This option limits the values displayed in the control to the range you specify.

### Filter

Restrict the data displayed in the control by including or excluding the values you specify.

## Slider STYLE options

### Drop-down

Displays the control in a drop-down box.

### Fixed-size

Displays the control as a fixed-size box.

### Label position

Sets the appearance of the control's label.

### Slider mode

Available for controls as filters.

  * **Range** : Makes the minimum and maximum values adjustable.
  * **Single value** : Lets you use the slider to select a single value.
  * **Locked min** : Makes only the maximum value in the range adjustable.
  * **Locked max** : Makes only the minimum value in the range adjustable.



### Min value / Max value

Available for controls as filters. Sets the minimum and maximum values in the slider.

### Snapping

#### Step size

Sets the size of each movement of the slider thumb. For example, to have each move of the slider thumb increase or decrease by 10, set **Step size** to 10.

#### Show tick marks / Tick interval

Shows marks on the slider bar at the specified interval.

### Text

Shows a text label for the current minimum and maximum slider values.

## Related resources

[About parameters](https://docs.cloud.google.com/data-studio/parameters)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-14 UTC."],[],[]] 
