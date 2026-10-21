---
url: https://docs.cloud.google.com/data-studio/add-edit-and-troubleshoot-calculated-fields/
title: Add, edit, and troubleshoot calculated fields \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:29.000757+00:00
---

# Add, edit, and troubleshoot calculated fields  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/add-edit-and-troubleshoot-calculated-fields/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Add, edit, and troubleshoot calculated fields Stay organized with collections  Save and categorize content based on your preferences. 

You can use calculated fields to extend your data's capabilities by creating new metrics or dimensions. Adding calculated fields to your report lets you perform advanced analysis and customize your Data Studio reports. This document shows you how to create, edit, reuse, and troubleshoot calculated fields in data sources and charts.

## Create a calculated field in your data source

**Note:** You must have edit rights to the data source to create and edit calculated fields.

Calculated fields in data sources are available in any report that uses that data source. To create a calculated field, follow these steps:

  1. [Edit the data source](https://docs.cloud.google.com/data-studio/edit-a-data-source).
  2. Click ![](https://docs.cloud.google.com/static/data-studio/images/icaddcirclegoogblue2xweb48dp-2017-11-03.png)**ADD A FIELD**.
  3. Select **Add calculated field.**
  4. Enter a **Name** value for this field: 
     1. This is the default name that appears in your reports. You can change this for individual charts by editing the name in the dimension and metric picker.
     2. The field name must be unique.
     3. You can't use a reserved keyword as the field name.
  5. Enter a value for **Formula** :

     1. To select a dimension, metric, or function, start typing its name. 
        1. If you have multiple fields with similar names, or fields that duplicate part of a function name, for example, **Date** and **Date2** , type part of the name, and then scroll through the list and select the field that you want.
        2. You can also click a field in the **Available Fields** list to add it to the formula editor.
     2. On the bottom right, click **SAVE** (or **UPDATE** if you are editing an existing field).
     3. Adjust the **Type** , **Aggregation** , and **Show As** options, as appropriate.

Alternatively, you can create a calculated field in your data source from a report by following these steps:

  6. Create or [edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).

  7. Click ![](https://docs.cloud.google.com/static/data-studio/images/icaddcirclegoogblue2xweb48dp-2017-11-03.png)**Add a field**.

  8. Select **Add calculated field.**

  9. Enter a **Name** value for this field:

     1. This is the default name that appears in your reports. You can change this for individual charts by editing the name in the dimension and metric picker.
     2. The field name must be unique.
     3. You can't use a reserved keyword as the field name.
  10. Enter a value for **Formula** :

     1. To select a dimension, metric, or function, start typing its name. 
        1. If you have multiple fields with similar names, or fields that duplicate part of a function name, for example, **Date** and **Date2** , type part of the name, and then scroll through the list and select the field that you want.
        2. You can also click a field in the **Available Fields** list to add it to the formula editor.
     2. On the bottom right, click **SAVE** (or **UPDATE** if you are editing an existing field).
     3. Adjust the **Type** , **Aggregation** , and **Show As** options, as appropriate.



> Learn more about [what you can do with calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields) and the difference between calculated fields that are [created in a data source versus chart-specific calculated fields](https://support-con/looker-studio/answer/6299685#data-source-vs-chart-specific-calculated-fields).

## Edit a calculated field in your data source

Calculated fields appear in the data source with an **fx** symbol. To edit the formula, click **fx** next to the field name. This opens the formula editor, where you can adjust the field as needed.

![On the Edit Connection menu field list, a user selects the fx icon to open the formula editor for the calculated field called My Calculated Field.](https://docs.cloud.google.com/static/data-studio/images/edit-calculated-field-2016-04-11.png)

## Create a chart-specific calculated field

Chart-specific calculated fields exist only in the chart in which you create them.

To create a chart-specific calculated field, follow these steps:

  1. Create or [edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).

  2. [Add a new chart](https://docs.cloud.google.com/data-studio/add-charts-and-controls-to-your-report) or select an existing chart.

  3. In the **Setup** tab of the **Properties** panel, click **\+ Add dimension** or **+** **Add metric** , depending on the kind of calculated field that you want to create.

  4. Click **+** **ADD FIELD**.

  5. Enter a field name.

  6. Enter your formula.

> You can use the same operators and functions as data source calculated fields. However, you can't reference other chart-specific calculated fields. You can use chart-specific calculated fields with [blended data](https://docs.cloud.google.com/data-studio/how-blends-work).

  7. Click **APPLY**.

  8. Adjust the **Type** , **Aggregation** , [**Display Format,**](https://docs.cloud.google.com/data-studio/format-fields-in-reports) and **Show As** options, as appropriate.


**Important:** Custom value formatting is chart-specific and cannot be applied when creating or editing calculated fields in your data source. 

## Edit a chart-specific calculated field

Chart-specific calculated fields appear in the **Setup** tab of the chart's **Properties** panel.

When you hover your cursor over the field type next to the field name, an **fx** symbol will appear. To edit the formula, click **fx.** This brings up the formula editor, where you can adjust the field as needed.

## Reuse a chart-specific calculated field

Chart-specific calculated fields only exist in the chart in which you create them. You can't directly reuse chart-specific calculated field, or reference it in other calculated fields.

However, you can copy a chart containing chart-specific calculated fields. The copy will contain any calculated fields defined in the original. You can then edit them as needed in the new chart.

## Troubleshoot calculated fields

If there is an error in a calculated field formula, you'll see a warning message, and you won't be able to save the field. Here are a few reasons why a formula might be rejected:

Error message or reason  |  **Possible Solutions**  
---|---  
**Invalid field name.** A valid field name automatically appears as a green or blue chip in the formula editor.  |  Check the spelling and any special characters in the field name.   
**Invalid function name.** A valid function automatically appears in uppercase green letters in the formula editor.  |  [ Check the spelling ](https://docs.cloud.google.com/data-studio/function-list) of the function name.   
**Missing quotes.** Literal strings must be quoted with matched pairs of single or double quotes.  |  Make sure all string literals are properly quoted.   
**Mismatched parentheses.** When nesting functions, a closing parentheses may have been missed.  |  Make sure that you have the same number of opening parentheses as closing parentheses, and that they are in the right spots.   
**Function argument type mismatch.** Functions expect arguments to be of a particular type. If there's a mismatch, it can cause an error. For example, trying to use a Date function on a Text dimension will create a function argument type mismatch.  |  Choose the correct input values. You can possibly use [ CAST() ](https://docs.cloud.google.com/data-studio/cast) to change the input value type.   
**Re-aggregating metrics is not supported.** Aggregation functions can't be applied to already aggregated data. This includes most metrics that are found in Google Analytics and Google Ads. For example, _ Sessions  _ is already aggregated as a sum in your data set, so the formula SUM( _ Sessions  _ ) will produce an error.  |  This limitation comes from the underlying data set. Any solution will involve changing how the data appears there, if possible.   
**An expression can have either metrics or dimensions, but not both.** You can't mix dimensions and metrics in function arguments.  |  Make sure you are using the appropriate function for your data. For example, use [ CONCAT() ](https://docs.cloud.google.com/data-studio/concat) to append text to a Text field, instead of using +.   
**Metric expressions and aggregations are not allowed in this expression.** You're creating a new chart-specific calculated dimension, but the result of the formula you've provided would create a metric.  |  Try creating the new field as a metric instead.   
  
## Related resources

  * [Dimensions and metrics](https://docs.cloud.google.com/data-studio/model-your-data)
  * [Format fields in reports](https://docs.cloud.google.com/data-studio/format-fields-in-reports)
  * [Create a data source](https://docs.cloud.google.com/data-studio/add-data-to-a-report)
  * [About calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Create a custom group](https://docs.cloud.google.com/data-studio/create-a-custom-group)
  * [Create a custom bin](https://docs.cloud.google.com/data-studio/create-a-custom-bin)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
