---
url: https://docs.cloud.google.com/data-studio/query-result-variables/
title: Query result variables \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:14.842367+00:00
---

# Query result variables  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/query-result-variables/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Query result variables Stay organized with collections  Save and categorize content based on your preferences. 

Query result variables let you insert data directly into text elements. For example, you could add text that describes a data point to your report, and then include that data point in the text as a chip. A query result chip updates its value when fresh data is available.

## Create a query result variable

To create a query result variable, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. [Add text to your report](https://docs.cloud.google.com/data-studio/add-text-images-lines-and-shapes-to-your-reports), or edit an existing text element.
  3. Enter `@` to open the variable insert menu.
  4. Click **Add a variable** to open the **Create variable** dialog.
  5. Give your variable a unique name.
  6. In the **Data Source** section, select the data source that the query should start from.
  7. Create a query that returns the data point you'd like to display. 
     * You can add or remove dimensions in the **Dimension** section.
     * You can change or remove the selected metric in the **Metric** section. You can select up to one metric.
     * You can add or remove filters in the **Filters** section.
     * You can change the sorting of the table in the **Sort** section.
  8. In the **Column** and **Row** fields, enter the column and row that contain the data point that you'd like to return. You can also click directly on a cell in the data table to select it.
  9. Optionally, edit the **Font color** and **Background color** settings of the query result chip. The **Preview** section displays how the chip will look. You can also apply conditional formatting to the chip.
  10. Click **Save**.



Data Studio inserts the query result chip into the text element. Whenever a user views this text element, the data value is updated.

## Apply conditional formatting to a query result variable

To make it easier to visualize and interpret key insights, you can apply conditional formatting that is based on specified rules to highlight data in your query result variables.

To apply conditional formatting, click **Conditional formatting** when you create or edit a variable. Then select one of the following options in the **Color type** section:

  * Select **Single color** to apply color rules to the query results variable when specific criteria are met.
  * Select **Color scale** to color the query results variable by using a gradient of colors that is based on the chip's value.



Note that you can't apply conditional formatting from the **Text Properties** panel while editing text.

### Single color conditional formatting

To apply single color formatting to a query result variable, follow these steps:

  1. In the **Format rules** section, define a format rule. 
     * Select the **field** whose value you want to check.
     * Choose a **condition** (for example, GREATER THAN, LESS THAN, EQUAL TO).
     * Enter an **Input value**. This value can also be another field.
     * You can add more `OR` or `AND` conditions to the format rule as needed.
  2. In the **Color and style** section, set the font color and background color that Data Studio should apply to the query results variable when it meets the format rules.



You can create multiple format rules with distinct color and style settings.

### Color scale conditional formatting

To apply a color scale to a query result variable, follow these steps:

  1. In the **Format based on** section, select the metric to which you want to apply the color scale.
  2. In the **Color and style** section, select a color scale. You can also click **Reverse color scale** to reverse the color scale.
  3. Select some **Point** values to define the colors at the start and end of your color scale. You can add and delete points to define midpoints along your color scale. 
     * You must define at least two points, but you can define up to five points.
  4. Click **Save** to apply your conditional formatting rules.



### Edit and manage conditional formatting rules

To see all format rules that are applied to a query result variable, click **X rules applied**. Data Studio displays a list of all format rules that are being applied in a numerical list.

You can edit, delete, or reorder format rules.

A format rule with a greater numerical list value takes precedent over previous format rules in the list. For example, if your first format rule applies a blue background color if a value is greater than 0, and your second format rule applies a red background color if a value is greater than 1, and the value is greater than both 0 and 1, then Data Studio will apply a red background color.

## Edit and manage query result variables

To edit a query result variable directly from a report page, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select the text field containing the variable, then click the variable.
  3. Click the **Edit variable** icon.
  4. Make any changes to the query or format of the query result variable.
  5. Click **Save**.



To edit a query result variable from a list of all variables, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Click the **Resource** menu, and then select **Manage variables (parameters)**.
  3. Next to the query result variable that you'd like to edit, click **Edit**.
  4. Make any changes to the query or format of the variable.
  5. Click **Save**.



## Duplicate a query result variable

To duplicate a query result variable, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Click the **Resource** menu, and then select **Manage variables (parameters)**.
  3. Next to the query result variable that you'd like to duplicate, click **Duplicate**.
  4. Make any changes to the query or format of the variable.
  5. Click **Save**.



## Delete a query result variable

To delete a query result variable directly from a report page, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Click or hold the pointer over the query result chip, and then click the **Delete** icon.



To delete a query result variable from a list of all variables, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Click the **Resource** menu, and then select **Manage variables (parameters)**.
  3. Next to the query result variable that you'd like to delete, click **Delete**.
  4. In the confirmation dialog, click **Remove variable**.



## Related resources

  * [Parameters](https://docs.cloud.google.com/data-studio/parameters)
  * [Add text, images, lines, and shapes to your reports](https://docs.cloud.google.com/data-studio/add-text-images-lines-and-shapes-to-your-reports)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
