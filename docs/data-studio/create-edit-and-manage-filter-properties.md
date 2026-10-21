---
url: https://docs.cloud.google.com/data-studio/create-edit-and-manage-filter-properties/
title: Create, edit, and manage filter properties \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:35:03.866911+00:00
---

# Create, edit, and manage filter properties  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/create-edit-and-manage-filter-properties/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)



Send feedback 

#  Create, edit, and manage filter properties Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to apply filters that only report editors can change. For information on filters that viewers can edit, see [About controls](https://docs.cloud.google.com/data-studio/about-controls).

## Add a filter property to a chart or control

To add a filter property to a chart or control, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).

  2. Select the chart or control that you want to filter. You can also filter a group of charts, a group of controls, or a group of both charts and controls.

  3. Select the **SETUP** tab in the **Properties** panel.

  4. Click **ADD A FILTER**.

  5. Click **CREATE A FILTER**.

**Tip:** You can also reuse an existing filter.
  6. Give the filter a **Name**.

  7. For each condition in the filter:

     1. Select **Include** or **Exclude**. Include filters include only data that matches the expression that you provide. Exclude filters remove all data that matches the expression.
     2. Select the dimension or metric by which to filter.
     3. Select the condition (for example, **Equal to (=)** , **Greater than ( >)**, **Contains** ). When defining filters on charts, pages, or reports that use **Equal to (=)** or **In** conditions, report editors can select from a list of possible filter values that are provided from the underlying data. To see filter value suggestions, enable **Show suggested values while typing** in the filter editor. Filter suggestions are supported for all data connectors.
     4. Provide a comparison value for the expression.
     5. To add more conditions to the filter clause, to the right of the condition, click the drop-down menu. Conditions within a clause can use **AND** or **OR** logic.
  8. To add more clauses to the filter, click the drop-down menu. You can combine filter conditions by using **AND** or **OR** logic.

  9. Click **SAVE**.




## Add a filter property to the entire report or to a page

To add a filter property for the entire report, in the menus, select **File > Report settings**.

To add a filter property for a page, in the menus, select **Page > Current page settings**.

Next, follow these steps:

  1. Select the **SETUP** tab in the **Properties** panel.
  2. Click **ADD A FILTER**.
  3. Set up the filter property using the previous instructions.



## Edit a filter property

To edit a filter property, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select the chart or control that has the filter property. Or, use the page settings menu as described in the previous section.
  3. Select the **SETUP** tab in the **Properties** panel.
  4. In the **Filter** section, click ![](https://docs.cloud.google.com/static/data-studio/images/icmodeeditgrey6002xweb24dp-2016-10-12.png)**Edit**.

**Note:** You can also create, edit, and duplicate filter properties using the filter manager.

## Reuse an existing filter property

Once you've added a filter property to a report, you can use it in other components or even other reports. Adding an existing filter property to a component _reuses_ that filter. Reusing a filter property does not create a copy of the filter. It's actually the same filter property, so if you later edit it in one place, that changes the filter property everywhere in the report.

**Important:** If you reuse a filter property for a chart or control with an incompatible data source, the chart or control will display an error. You can fix this by editing the filter property to use dimensions or metrics that are common to both data sources. [Learn more about filter properties and data sources](https://docs.cloud.google.com/data-studio/about-filter-properties).

## Copy components and reports with filter properties

When you make a copy of a page or component within a report, its filter properties are reused by the copy.

If you copy a filtered component into a different report, Data Studio makes a new copy of the filter property. It has no relationship to the original filter property. Note that if you copy and paste the component a second time, you will get another copy of the filter property. The two copies are not related.

If you make a copy of a report and change the data source, any filter properties in the report use the new data source.

## Manage filter properties

The filter manager lists of all the filter properties in a report. Use this list to duplicate, edit, or remove filters. You can also create a new filter using the filter manager.

**Important:** When you edit or create a filter property from the filter manager, you can select which data source is used by the filter property. If you change the data source for an existing filter property and the new schema doesn't match the original data source, the filter property may break.

### Display the filter manager

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. In the menus, select **Resource > Manage** **filters**.
  3. Use the links in the **Actions** column to manage the filter properties in your report.



#### Edit a filter property

To edit the filter property configuration, click **Edit** in the **Actions** column. This is the same as using the **Edit** icon ![](https://docs.cloud.google.com/static/data-studio/images/icmodeeditgrey6002xweb24dp-2016-10-12.png) as described in Edit a filter property.

#### Duplicate a filter property

To create a copy of the filter property, click **Duplicate** in the **Actions** column. You can then modify the filter property conditions and apply the filter property to other charts in the report.

#### Remove a filter property

To delete the filter property permanently from the report, click **Remove** in the **Actions** column.

**Important:** Be careful! You can't undo this action.

## Display filter properties to viewers

By default, [report viewers can see all the filters for which they can edit the values](https://docs.cloud.google.com/data-studio/about-filter-properties), but they cannot see any of the filters for which they cannot edit the values. To allow report viewers to see the values of filters that they cannot edit, follow these steps:

  1. Click the **Share** button.
  2. Click the **Report access settings** gear icon.
  3. Clear the **Disable viewers from viewing advanced applied filters** option.



Viewers can also share a link to the report with their filter configuration selections. For more information, see [Get a link to your report](https://docs.cloud.google.com/data-studio/get-a-link-to-your-report#include_your_current_report_view).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
