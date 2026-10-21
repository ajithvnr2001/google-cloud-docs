---
url: https://docs.cloud.google.com/data-studio/preset-filter-control/
title: Preset filter control \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:06:28.526295+00:00
---

# Preset filter control  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/preset-filter-control/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Preset filter control Stay organized with collections  Save and categorize content based on your preferences. 

You can add preset filters to your Data Studio reports to let users quickly apply preset filter logic to a chart or report with the click of a button.

You can also create a [**Reset filters** button](https://docs.cloud.google.com/data-studio/add-buttons), which lets users quickly reset all filters.

## Requirements

To add a preset filter button to a report, you can use any existing **boolean** type dimension or [create a calculated field](https://docs.cloud.google.com/data-studio/add-edit-and-troubleshoot-calculated-fields) that returns a boolean value.

You must use a boolean type field because a filter button has only two states: selected or unselected.

## Add preset filters to a report

  1. Create or [edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).

  2. Select the **Preset filter** option from the **Add a control** drop-down menu.

  3. Drag the button to position it on your report.

  4. Next, configure the filter using the options on the **Setup** tab in the **Button properties** panel. See the Configure preset filters section on this page for more information about configuring a preset filter.

  5. Add a label to your filter button by clicking in the button and adding text to the text field on the report.

  6. Customize your button appearance with the options in the **Style** tab in the **Button properties** panel. Read more about button style options in the [Button style options](https://docs.cloud.google.com/data-studio/add-buttons) section of the Adding buttons page.




## Configure preset filters

Once you have added your preset filter button to your report, you can configure the following filter options in the **Setup** tab of the **Button properties** panel.

### Data source

[View, edit, or replace](https://docs.cloud.google.com/data-studio/replace-the-data-source-for-a-component-page-or-report) the data source that is specified for the button.

### Button action type

To create a preset filter, select the **Filter** option.

### Control field

Select a boolean type dimension or [create a calculated field](https://docs.cloud.google.com/data-studio/add-edit-and-troubleshoot-calculated-fields) that returns a boolean value.

To add a **Control field** , follow these steps:

  1. To access the field options for your data, select **Add control field**.
  2. Select a field. You can search for a boolean field from your data, or you can select the **ADD FIELD** option to create a calculated field.

For example, you can use the `CONTAINS_TEXT` function to create a calculated field with an expression that returns data for "United States" in a table that displays the population data for many countries:

`CONTAINS_TEXT(Country,"United States")`




This function lets users quickly filter a chart for "United States" data by clicking the filter button.

### Default selection (true or false)

When enabled, the **Default selection (true or false)** option automatically applies the filter to charts and reports without requiring user input.

To disable the filter, a user has to click the button.

This setting is optional.

### Button filter group

You can use the **Button filter group** drop-down to control how many filter options can be applied to a chart or report at one time. The number in the drop-down menu corresponds to a filter's group assignment. When one filter button is enabled in a group, the other filter buttons that are assigned to the same group will be disabled.

For example, if you have a table chart that displays population data for many different countries **,** you may want to configure several filter options for users to choose from.

You can create several filter buttons that let users filter by different countries, such as buttons for **United States** , **Japan** , or **United Kingdom**. You can use the **Button filter group** drop-down to assign the different country filter buttons to the same group. For example, assigning the **United States** , **Japan** , and **United Kingdom** filter buttons to **Button filter group** drop-down option **1** ensures that only one country filter can be applied to the chart at once.

You can specify up to five button filter groups per report page.

This setting is optional.

## Related resources

  * [About controls](https://docs.cloud.google.com/data-studio/about-controls)
  * [About calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Add buttons](https://docs.cloud.google.com/data-studio/add-buttons)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
