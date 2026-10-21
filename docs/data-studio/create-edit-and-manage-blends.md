---
url: https://docs.cloud.google.com/data-studio/create-edit-and-manage-blends/
title: Create, edit, and manage blends \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:24.764379+00:00
---

# Create, edit, and manage blends  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/create-edit-and-manage-blends/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Create, edit, and manage blends Stay organized with collections  Save and categorize content based on your preferences. 

You can create blends automatically or manually:

## Automatically blend selected charts

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Add charts based on the data sources you want to blend. For each chart, include the fields you want to include in the blend.
  3. Select the charts you want to include in the blend. 
     1. You can blend up to 5 charts.
     2. Right-click on the selected charts, then click **Blend data**.



Data Studio generates a new chart that combines the fields from the selected charts. You can use that blended chart in your reports just like any other chart.

### Example: create a ratio metric

Blending 2 scorecards automatically creates a ratio metric, using the first chart you select as the numerator and the second chart as the denominator. For example, blending **Costs** and **Clicks** metrics automatically calculates your cost-per-click ratio:

![A user creates a blended Cost/Clicks scorecard by selecting the Cost and Clicks scorecards on a report and right-clicking to select the Blend data option.](https://docs.cloud.google.com/static/data-studio/images/cost-click-2019-09-11.png)

  1. **Cost** scorecard. Select this chart first.
  2. **Clicks** scorecard. Select this chart second, then right-click and select **Blend data**.
  3. Blended **Cost** / **Clicks** scorecard. Change the **Type** to **Currency** and adjust the **Decimal precision** to 4 places.



[See a more complete example in the **Create a ratio field based on filtered metrics** tutorial.](https://docs.cloud.google.com/data-studio/tutorial-create-a-ratio-field-based-on-filtered-metrics)

## Create blends manually

The two ways to create blends manually are:

  * Select a component on the page, then in the properties panel on the right, under **Data source** , click **+BLEND DATA**.
  * Open the **Resources > Manage blends** menu, and in the bottom left, click **Add blend**.



## Edit blends you've already created

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select a chart based on a blend.
  3. Click the ![](https://docs.cloud.google.com/static/data-studio/images/edit-pencil.png)**Edit** icon for that chart's data source.



You can also edit blends by clicking the **Resource > Manage blended data** menu option. Locate the blend in the list and click **EDIT**.

## Add a table to the blend

  1. To the right of the rightmost table in the blend, click **Join another table**.
  2. Select a data source.
  3. Add fields to the table by clicking **Add dimension** or **Add metric** , or by dragging the field from the fields drawer. If the drawer is closed, open it by clicking the ![](https://docs.cloud.google.com/static/data-studio/images/gmchevronrightgmgrey50048dp-2022-02-16.png) right arrow icon.
  4. To create a calculated field in the table, click **Add dimension** or **Add metric** , then click **+Create field**.

**Tip:** You can join tables based on calculated fields. This can be useful if the data you want to join on isn't perfectly aligned between the tables (for example, different capitalization or formatting used in a customer ID).
  5. Click the join configuration between the new table and the table to the left to set up the join between those tables.




## Move and remove tables

Tables you add to the blend always appear on the right. To reorder the tables in the blend:

**Important:** Moving tables could break your join conditions, requiring you to reconfigure the join. To restore the previous join condition, move the table back to its original position.

  1. Click the ![](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--more-vertical.png)**More** icon for the table you want to move.
  2. Select **Shift left/right**.



To remove a table from the blend:

**Tip:** Removing a table has no effect on the data sources or on other blends in the report.

  1. Click the ![](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--more-vertical.png)**More** icon for the table you want to remove.
  2. Select **Remove**.



## Add and edit join configurations

Each table in the blend is joined by a set of matching fields (the join conditions) and a join operator. To add or edit this configuration:

  1. Click the join configuration box between 2 tables.
  2. Select a join operator.
  3. Define the join condition by adding the dimensions that contain the data you want to join on. Note that the cross join operator doesn't use a join condition.
  4. Click **Save**.



### Missing fields in join conditions

A red box around the join configuration, or a pink **Missing** field in the join condition indicates that Data Studio can't join your data with the selected dimensions:

![Join configuration icon highlighted in red on the Blend Data panel indicates that a join configuration is not specified.](https://docs.cloud.google.com/static/data-studio/images/broken-join-config-2022-02-16.png)

To fix this, add the missing field to the table before configuring the join condition, or remove the missing field.

## Set a date range for a table in the blend

You have two options when setting a date range on a table in the blend:

  * **Auto** : Use the date range of the chart that gets its data from this blend.
  * **Custom** : Override the chart's date range with the range you select.



## Apply a filter to a table in the blend

Limit the data contained in a table by applying a filter. You can create a new filter, or apply an existing filter to a table in the blend as long as that filter is based on fields that exist in the table.

Get more in-depth information about [filters and date ranges in blends](https://docs.cloud.google.com/data-studio/blending-tips-and-advanced-concepts).

## Create calculated fields in a blend

Tables in a blend can include calculated fields. This can be particularly useful as a way of creating join conditions when the data isn't perfectly compatible between tables (for example, when the join fields contain differently formatted dates or capitalized strings).

####  Show me how to add a calculated field 

  1. Choose a table in the blend. 
  2. Click **Add dimension** or **Add metric**. 
  3. Click **CREATE FIELD**. 
  4. Type in the formula in the editor window, then click **APPLY**. 



**Note:** When you're creating calculated fields in a table in the blend, the formula can only reference fields found in that table. For example, a calculated field in Table 1 can't reference fields in Table 2.

To create a calculated field based on fields from different data sources, add those fields to their respective tables in the blend, then [create a chart-specific calculated field](https://docs.cloud.google.com/data-studio/add-edit-and-troubleshoot-calculated-fields#create-a-chart-specific-calculated-field).

## Rename a table

Click a current table name, then type a new name.

If you have fields in the blend with duplicate names, you'll see the table name from which those fields are derived in the lists of available dimensions and metrics.

## Rename a blend

To rename a blend, click the current blend name, then type a new name.

## Reconnect a table

Underneath the table name, click the drop-down menu and select a new data source for this table.

**Important:** Selecting a data source whose fields don't match the current data source for the table may break the blend configuration. You'll need to remove or replace any invalid fields. 

## Manage blended data

Use the **Resource > Manage blended data** menu to access all the blends contained in the current report. You can create new blends and edit, copy, or remove existing blends from this page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
