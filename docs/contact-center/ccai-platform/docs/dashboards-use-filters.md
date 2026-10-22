---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-use-filters/
title: Filters: Retrieving data using filters \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:10.364714+00:00
---

# Filters: Retrieving data using filters  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-use-filters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)



Send feedback 

#  Filters: Retrieving data using filters Stay organized with collections  Save and categorize content based on your preferences. 

While you can still create the filter, you cannot apply multiple filters that use the same field to the same dashboard tile.

If you want to create a filter on a field from an Explore that is not used in the dashboard, see the Advanced filters section on this page.

If you have already selected a field in the filter by dialog box of the **Add Filter** window, clicking the **Advanced** switch results in no changes to the Add Filter window and an advanced filter is not initiated.

Once you've selected the field you want to filter by, click **Add**.

**Note:** A 45-day limit has been applied to the date range filter to optimize performance. If a date range exceeds this limit, a **Date range has been exceeded** error message will appear, and no data will be displayed as a result.

## Adding dashboard filters

To get started, make sure the dashboard is in edit mode and that you have at least one query tile or Look-linked tile.

  1. Click **Filters** in the top toolbar, and then click **Add Filter**. An Add Filter window appears next.

  2. The **Add Filter** window appears pre-populated with fields (dimensions or measures) from any Explores that were used in the creation of this dashboard's tiles. For example, the following **Add Filter** window shows the Explores that are presently used in the dashboard's tiles: the Flights Explore from the E Faa model and the Order Items Explore from the MB ecommerce_demo model




![Write in a field name to filter by.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/dashboards-add-filter.png)

  1. Clicking the arrow to the left of an Explore expands the Explore to show the Explore's views.



Each view can then be expanded to reveal the view's fields. To filter on a field from one of these Explores, you can use the **Filter by dialog** box to search for fields or manually enter a field name.

You can also click a field name, such as Order ID, to add it to the Filter by dialog box: If you select a field that is already being used by another filter, you will receive an alert message.

## Advanced filters

Advanced filters let you create dashboard filters using fields that are outside of the Explores used to create tiles on the dashboard.

Click the **Advanced** switch to use advanced filters. This updates the **Add Filter** window with options to select a model, an Explore, and a field with which to create the filter.

![Write in or select a field name to filter by.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/advanced-toggle.png)

First, select a model name from the drop-down Model menu.

The drop-down menu contains all models that you have access to.

Once a model is selected, the Explore dialog box populates with a drop-down menu of all the Explores that are present in the selected model.

Once the model and the Explore are selected, the fields that are available in that Explore will populate the Add Filter window.

You can use the search bar to find the field that you want to filter by, or you can click a field name to select it. Once you've selected the field you want to filter by, click **Add**.

### Customizing filter configuration

Once you select a filter field and click **Add** , the Add Filter window shows a variety of customizable settings:

![Choose a name, default value, and control setting for your custom filter.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/dashboards-customize-filter.png)

  * **Title** : enter the title of the filter as you want it to appear on the dashboard. The title option pre-populates with the name of the filter-by field.

  * **Control** : select from a list of control types, which vary depending on the type of data you are filtering. See the Dashboard filter controls section on this page to learn more about the different types of controls.

  * **Display** : for controls that can be displayed as either inline or popover, select how the filter will be displayed. See the Displaying dashboard filters section on this page to learn more about the different ways to display filters. If a control can be displayed only in one way, this option will not appear.

  * **Values** : to set specific value options for the filter, choose from the drop-down or enter the value options in this field. Leave blank to allow value options from the database to be surfaced, up to the maximum number of values available for that control. For numeric data, this field is replaced by the Min and Max fields.

  * **Configure Default Value** : optional, use to set the default value for the filter

  * **Require a filter value** : select the checkbox to require a value for the filter. See the Requiring a filter value section on this page to learn more about requiring filter values.

  * **Select filters to update when this filter changes** : select the checkbox to link other filters to this filter. See the Setting up linked filters section on this page to learn more about linked filters. If there are no other filters on the dashboard, this option will be disabled.

  * **Add and Cancel** : click one of these buttons to save or cancel the new filter




The **Tiles To Update** tab lets you determine which tiles listen to the filter. Advanced Reporting begins by automatically applying the filter to any tiles that were created from the same Explore as the filter and sets the value of Field to Filter to the same field as the field chosen for the filter:

![Add a filter criteria and select tiles to update.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/dashboards-tiles-to-update.png)

  1. Select All or None to turn the filter on or off for all tiles.

  2. In the Field to Filter section, for each tile, choose which field will be affected by the filter, or choose not to apply the filter to an individual tile.

  3. If you select a field that is already used in an existing filter, any tiles filtered by the existing filter are unavailable to the new filter.

  4. Select Add or Cancel to save or cancel the new filter.




If any new tiles are added to the dashboard after the filter is created, if they were created from the same Explore as the filter, the dashboard filter is automatically applied to that tile.

For further information see the Looker documentation for: [Dashboard filter controls](https://cloud.google.com/looker/docs/filters-user-defined-dashboards#dashboard_filter_controls).

### Displaying Dashboard filters

You have several options for altering the way dashboard filters are displayed. You can adjust the appearance of individual filter controls or of the entire filter bar.

#### Appearance of individual filters

To set the way a filter appears, first make sure your dashboard is in edit mode and then select the style of display in the **Display** field of the filter configuration window that appears when you select **Edit** from the filter menu. Most dashboard filters can be displayed in the following ways:

  * Inline: The filter is displayed directly in the top bar of the dashboard.

  * Popover: A summary value appears in the top bar of the dashboard; click the value to see the full filter.

  * Filters can also be placed behind a More button: A More button will appear in the filter bar with an indicator that shows the number of filters the bar contains; viewers can click the button to see the filters and their values.




Some filter controls can be displayed only in inline orientation; when you edit a dashboard with these filter controls, you won't see a Display field in the filter configuration window. These filter controls can be displayed only in inline orientation:

  * Drop-down Menu

  * Single Day

  * Timeframes

  * Date Range




Additionally, some filter controls can be displayed only in popover orientation; when you edit a dashboard with these filter controls, you won't see a Display field in the filter configuration window. These filter controls can be displayed only in popover orientation:

  * Tag List

  * Advanced




Generally, we recommend that important or frequently used filters be displayed as inline or popover, and less frequently used filters be displayed as overflow.

#### Appearance of the filter bar

To set the way a filter bar appears, follow these steps:

  1. Make sure your dashboard is in **edit** mode.

  2. Open the dashboard's **Settings** window.

  3. Click the **Filters** tab of the **Settings** window.

  4. You can set the Default filters view option to Expanded or Collapsed. (The default is Expanded.)

  5. The Filters location option allows you to place the filter bar at the top or the right of the dashboard. (The default is at the top.)




## Editing dashboard filters

In edit mode, a three-dot Filter Menu icon appears next to every filter.

To edit a filter:

  1. Click the icon. This opens the filter menu, which displays options to edit or delete a filter.

  2. Select the **Edit** menu option to open a filter configuration window, similar to the one used to add a filter, populated with the existing configuration for the filter. From there, you can update the filter-by field, the filter's settings, or the tiles to update.

  3. Select **Update** or **Cancel** in the filter configuration window to save or cancel your changes.

  4. Once you've edited filters, click the dashboard's **Update** button to apply the new filter settings to the tiles.

  5. Click **Save** to save your changes and exit edit mode.




## Deleting dashboard filters

In edit mode, three-dot Filter Menu icon appears next to every filter.

To delete a filter:

  1. Click the three-dot **Filter Menu** icon. \ This menu displays options to edit or delete a filter.

  2. Select the **Delete** menu option to delete the filter.

  3. Click **Save** to save your changes and exit edit mode.

  4. Once you've deleted the filters, click the dashboard's **Update** button to apply the new filter settings to the tiles.




Alternatively, you can select the **Edit** menu option, which opens the filter configuration window. Click the Delete button within the filter configuration window to delete your filter.

**Caution:** Deleting a filter cannot be undone.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
