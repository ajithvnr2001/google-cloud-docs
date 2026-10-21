---
url: https://docs.cloud.google.com/data-studio/create-a-custom-bin/
title: Create a custom bin \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:43:26.654988+00:00
---

# Create a custom bin  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/create-a-custom-bin/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Create a custom bin Stay organized with collections  Save and categorize content based on your preferences. 

The **Bin** calculated field type lets you create ad hoc numeric tiers for numeric dimensions without needing to develop `CASE WHEN` expressions in calculated fields or logic in SQL.

The **Bin** calculated field type can be helpful when you want to quickly group values into specific integer ranges to adjust the granularity of your data.

This page explains how to create and edit custom bins, and includes the following sections:

  * Configure a custom bin
  * Create a custom bin in your data source
  * Edit a custom bin in your data source
  * Create a chart-specific custom bin
  * Edit a chart-specific custom bin
  * Reuse a chart-specific custom bin



## Create a custom bin in a reusable data source

**Note:** You must have edit rights to the data source to create and edit calculated fields.

You can use custom bins that exist in a reusable data source in any report that includes that data source. To create a custom bin in a data source, follow these steps:

  1. [Edit the data source](https://docs.cloud.google.com/data-studio/edit-a-data-source).

  2. Click ![](https://docs.cloud.google.com/static/data-studio/images/icaddcirclegoogblue2xweb48dp-2017-11-03.png)**ADD A FIELD**.

  3. Select **Add bin.**

  4. Configure the bin options. For more information, see Configure a custom bin.

  5. Click **Save**.




### Create a custom bin in a data source while editing a report

Alternatively, you can create a custom bin in either a reusable or an embedded data source by following these steps:

  1. Create or [edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).

  2. In the **Data** panel, click ![](https://docs.cloud.google.com/static/data-studio/images/icaddcirclegoogblue2xweb48dp-2017-11-03.png)**Add a field.**

  3. Select **Add bin**.

  4. Configure the bin options. For more information, see Configure a custom bin.

  5. Click **Save**.




## Edit a custom bin in your data source

**Note:** You must have edit rights to the data source to create and edit calculated fields.

Custom bins and calculated fields appear in the data source with an **fx** symbol. To edit the formula, click **fx** next to the field name to open the formula editor, where you can adjust the field as needed.

![On the Edit Connection menu field list, a user selects the fx icon to open the formula editor for the calculated field called My Calculated Field.](https://docs.cloud.google.com/static/data-studio/images/edit-calculated-field-2016-04-11.png)

## Create a chart-specific custom bin

**Note:** To create a chart-specific custom bin, you must meet the following requirements: 

  * You must enable [Field Editing in Reports](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports) in the data source.
  * You must have edit rights to the report to create and edit calculated fields.
  * You can't reference other chart-specific calculated fields.



Chart-specific custom bins exist only in the chart in which you create them.

To create a chart-specific custom bin, follow these steps:

  1. Create or [edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).

  2. [Add a new chart](https://docs.cloud.google.com/data-studio/add-charts-and-controls-to-your-report) or select an existing chart.

  3. In the **Setup** tab of the **Properties** panel, click **\+ Add dimension.**

  4. At the bottom of the field list, click **+** **ADD BIN**.

  5. Configure the bin options. For more information, see Configure a custom bin.

  6. Click **Save**.


**Tip:** Learn more about the difference between calculated fields that are [created in a data source versus chart-specific calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields).

## Configure a custom bin

When you create a custom bin, you can configure several options to define how Data Studio groups the data:

  * **Selected field to bin by** : Select an existing numeric field to bin by from the **Selected field to bin by** drop-down menu.
  * **Bin field format** : Select a format for the bin from the **Bin field format** drop-down menu. Options include the following: 
    * **Interval "[x,y)"** —This format displays the range that includes x and up to but not including y.
    * **Integer "x to y"** —You must use this format with discrete integer values (such as age).
    * **Relational " >=x and < y"**—This format works best with continuous numbers (such as dollars).
  * **New field name** : Specify a name in the **New field name** field. 
    * This name is the default name that appears in your reports. You can change this name for individual charts by editing the name in the dimension picker.
    * The field name must be unique.
    * You can't use a reserved keyword as the field name.
  * **New field ID** : If you are creating a custom bin in a data source, you can edit the default ID in the **New field ID** field, if needed. Data Studio uses this ID to identify a field as an alternative to the field name.
  * **Refresh field info** : As an optional starting point, click **Refresh field info** to learn more about the values for the dimension for which you're creating custom bins, including the dimension's minimum and maximum values. Having this information can be helpful in determining the way in which you specify value bins.
  * **Apply automatic values** : Click **Apply automatic values** to automatically populate the **Bin size** , **Minimum value** , and **Maximum value** fields for **Equal Sized** bins.
  * **Bin type** : Specify a **Bin type** : 
    * Select **Equal Sized** to bin numeric values into equal integer ranges. For example, tiers of values ranging from 0-10, 10-20, and 20-30.
    * Select **Custom Sized** to create custom bin sizes of varying integer ranges. For example, tiers of values ranging from 0-15, 15-75, and 75-100.
  * **Bin sizes and ranges** : Customize the bin sizes and ranges:

    * If the selected **Bin type** is **Equal Sized** , enter values in the **Bin size** , **Minimum value** , and **Maximum value** fields.
    * If the selected **Bin type** is **Custom Sized** , specify the tier breakpoints in ascending order in the **Bin breakpoints** box, separated either by commas or by pressing the **Enter** key **(PC) or Return** key **(Mac)**. You can also use the **Tab** key.
**Important:** You can create a maximum of 195 total bins for each **Bin** calculated field.
  * **Bin remaining values** : Configure how Data Studio displays values outside of the specified minimum and maximum bin values:

    * If you select the **Bin remaining values outside the min and max as separate bins** checkbox, Data Studio groups values that are less than the minimum bin value into one bin, and values that are greater than the maximum bin value into another bin. The label for these bins depends on the **Bin field format** that you select (for example, `[-inf, min)` and `(max, inf]`).
    * If you don't select this checkbox, each value outside of the minimum and maximum values appears as its own bin.

**Tip:** [See a custom bin example](https://docs.cloud.google.com/data-studio/about-calculated-fields#create_a_custom_bin).

## Edit a chart-specific custom bin

**Note:** You must have edit rights to the report to create and edit calculated fields.

Chart-specific calculated fields appear in the chart **Properties** panel on the **Setup** tab.

When you hold the pointer over the field type next to the field name, an **fx** symbol will appear. To edit the formula, click **fx** to bring up the formula editor, where you can adjust the field as needed.

## Reuse a chart-specific custom bin

Chart-specific calculated fields exist only in the chart in which you create them. You can't directly reuse a chart-specific calculated field or reference it in other calculated fields.

However, you can copy a chart that contains chart-specific calculated fields. The copy will contain any calculated fields defined in the original. You can then edit them as needed in the new chart.

## Related resources

  * [About calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Add, edit, and troubleshoot calculated fields](https://docs.cloud.google.com/data-studio/add-edit-and-troubleshoot-calculated-fields)
  * [Edit fields](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
