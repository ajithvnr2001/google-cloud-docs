---
url: https://docs.cloud.google.com/data-studio/create-rename-copy-hide-and-remove-fields/
title: Create, rename, copy, hide, and remove fields \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:26.084059+00:00
---

# Create, rename, copy, hide, and remove fields  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/create-rename-copy-hide-and-remove-fields/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Create, rename, copy, hide, and remove fields Stay organized with collections  Save and categorize content based on your preferences. 

Once you've created a data source, you can add, remove, and change the fields.

**Tip:** To apply changes that were made in the underlying dataset to the data source, see [Refresh data source fields](https://docs.cloud.google.com/data-studio/refresh-data-source-fields).

## Create a new field

You can create new fields in a data source in two ways:

  * Create a new count or count distinct metric from an existing dimension.
  * Use [calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields) to create more complex metrics or new dimensions.



### Create count and count distinct metrics

To count values in a dimension, follow these steps:

  1. [Edit the data source](https://docs.cloud.google.com/data-studio/edit-a-data-source).
  2. Next to field you want to count, click ![](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png)**More**.
  3. Click **Count** or **Count distinct**. The new field is added to the field list and is named "Count (or Count Distinct) of [original field name]." If the data source has a lot of fields, you might have to scroll to see the new field.



#### Example: Count the number of sales representatives per sales region

Suppose you have a spreadsheet that tracks sales people and the regions they cover:

Employee ID  |  Sales Region   
---|---  
120134  |  West   
949304  |  East   
039443  |  South   
393930  |  Central   
...  | ...   
  
A Google Sheets data source based on this data would look like this:

![A data source displays the Text type fields Employee ID and Sales Region.](https://docs.cloud.google.com/static/data-studio/images/sales-region-example-ds-2016-06-08.png)

To find out how many sales people you have in each region, you can create a new metric to count them by following these steps:

  1. Next to **Employee ID** , click ![](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png)**More**.
  2. Select **Count Distinct** from the menu.



This creates a new metric, **Count Distinct Employee ID**. (You can change this name by clicking the new field.) The new metric can be used in visualizations just as you would any other field.

![A data source displays the Text type fields Employee ID and Sales Region, and the Number type calculated field Count Distinct Employee ID with Auto aggregation.](https://docs.cloud.google.com/static/data-studio/images/sales-region-example-ds-3-2016-06-08.png)

To edit the formula, at the end of the metric field, click **fx.**

## Rename a field

To rename a field, follow these steps:

  1. [Edit the data source](https://docs.cloud.google.com/data-studio/edit-a-data-source).
  2. Click the name of the field you want to change.
  3. Enter a new name.

**Tip:** You can also [rename fields and manage](https://docs.cloud.google.com/data-studio/manage-field-ids) their IDs at the report level.

### Effects of renaming a field

When you rename a data source field, the new name is used in the following places:

  * Calculated fields that use this field (renaming a field won't break calculated fields)
  * The **Data** panel in reports
  * Charts that use this field 
    * **Exception** : if you've renamed this field in a chart, the chart continues to use the name you gave it there. (The field name in the chart overrides the field name in the data source.)



## Copy a field

To create a copy of a field, follow these steps:

  1. [Edit the data source](https://docs.cloud.google.com/data-studio/edit-a-data-source).
  2. Next to the field that you want to copy, click ![](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png)**More**.
  3. Click **Duplicate**.



## Hide a field

Hiding a field disables it.

**Caution:** Hiding a field in a reusable data source affects every report that uses that data source. Charts in other reports that use the hidden field break and display an error. 

To hide a field, follow these steps:

  1. [Edit the data source](https://docs.cloud.google.com/data-studio/edit-a-data-source).
  2. Next to the field that you want to hide, click ![](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png)**More**.
  3. Click **Hide**. To unhide the field, follow the same steps and then click **Show**.



### Effects of hiding a field

Hiding a data source field has the following effects:

  * The field appears grayed out in the data source field list.
  * The field won't appear in the **Properties** panel in reports.
  * The field won't appear in report metadata or data requests.
  * Charts, filters and calculated fields that use this field display an error.

**Tip:** To fix errors in charts, calculated fields, filters, or other components, remove the hidden field from the broken component.

## Remove a field

Removing a field deletes it from the data source.

**Caution:** Removing a field from a reusable data source affects every report that uses that data source. Charts in other reports that use the removed field break and display an error. 

To remove a field, follow these steps:

  1. [Edit the data source](https://docs.cloud.google.com/data-studio/edit-a-data-source).
  2. Next to the field that you want to remove, click ![](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png)**More**.
  3. Click **Remove**.



### Effects of removing a field

**Important:** Removing a calculated field permanently deletes the field. Once a field is removed, you can't get the calculated field back except by recreating it.

Removing a data source field has the following effects:

  * The field is removed from the data source field list.
  * The field is removed from the **Properties** panel in reports.
  * The field won't appear in report metadata or data requests.
  * Charts, filters and calculated fields that use this field display an error.

**Tip:** To fix errors in charts, calculated fields, filters, or other components, remove the deleted field from the broken component.

## Restore a removed field

To add removed fields back to the data source [reconnect the data source](https://docs.cloud.google.com/data-studio/edit-the-data-source-connection) or [refresh the data source fields](https://docs.cloud.google.com/data-studio/refresh-data-source-fields).

## Related resources

  * [Model your data](https://docs.cloud.google.com/data-studio/model-your-data)
  * [About calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Manage field names and IDs](https://docs.cloud.google.com/data-studio/manage-field-ids)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
