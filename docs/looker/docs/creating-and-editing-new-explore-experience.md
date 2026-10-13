---
url: https://docs.cloud.google.com/looker/docs/creating-and-editing-new-explore-experience/
title: Creating and editing Explores in the new Explore experience \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:30.221907+00:00
---

# Creating and editing Explores in the new Explore experience  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/creating-and-editing-new-explore-experience/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Creating and editing Explores in the new Explore experience Stay organized with collections  Save and categorize content based on your preferences. 

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This page is part of the [new Explore experience preview feature](https://docs.cloud.google.com/looker/docs/new-explore-experience-overview) series.

This page introduces you to creating and editing Explores in the new Explore experience. Read the following sections to learn how to create and edit Explore queries for presenting data to your users:

  * Required roles
  * Accessing the new Explore experience
  * Starting with a blank Explore
  * Using starter questions
  * Navigating the Configure panel
  * Adding fields
  * Removing fields
  * Sorting data
  * Pivoting data
  * Reordering columns
  * Displaying totals
  * Features for developers
  * Related resources



For more information about the components of the new Explore experience, see the [Viewing and interacting with Explores in the new Explore experience](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-new-explore-experience) documentation page.

## Required roles

You must have specific roles and permissions to perform the following functions in Explores:

  * To view and interact with Explores, you must have the **User** [Looker role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) or another role that contains the [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permission.

  * To access features for developers, which includes the ability to see LookML information about fields, you must have the **User** [Looker role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#user) or another role that contains either the [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) permission or the [`see_lookml`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_lookml) permission.

  * To create and edit table calculations, you must have either the **Developer** Looker role or another role that contains the [`create_table_calculations`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_table_calculations) permission.

  * To create and edit custom fields, you must have either the **Developer** Looker role or another role that contains the [`create_custom_fields`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_fields) permission.




## Accessing the new Explore experience

To access the new Explore experience, the [**New Looker Explore and Merge Query Experience**](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#new-looker-explore-and-merge-query-experience) preview feature must be enabled for your instance. The preview feature is enabled by default. If it is disabled, and you aren't a Looker admin, ask an admin to enable the feature.

From an Explore page, click **Try the new Explore** to turn on the new Explore experience for all Explores that you interact with. To switch back to the classic experience, click **Switch to classic Explore**.

## Starting with a blank Explore

When you [open a blank Explore in Looker](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-new-explore-experience#finding-explores-in-looker) or clear an existing Explore, you have several options for getting started:

  * Use a starter question to load an Explore.
  * [Ask Insight Assistant](https://docs.cloud.google.com/looker/docs/gemini-insight-asst) to get answers to your data questions and starting points for your analysis (when available).
  * Explore from scratch by adding fields from the **Configure** panel.



## Using starter questions

Once you have [opened an Explore in the new Explore experience](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-new-explore-experience#finding-explores-in-looker), if your Looker admin has [enabled starter questions](https://docs.cloud.google.com/looker/docs/gemini-quick-starts), you can use starter questions to create a starting point for quickly running and building analyses. Starter questions can be [modeled queries](https://docs.cloud.google.com/looker/docs/reference/param-explore-query) or can be [generated by Gemini](https://docs.cloud.google.com/looker/docs/gemini-quick-starts).

You can open **starter questions** in one of two ways:

  * By clicking the **Starter Questions** drop-down field in a blank Explore.
  * By clicking the dynamic_form [**Show starter questions** button](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-new-explore-experience#navigating-the-new-explore-experience).



Each starter question card displays the name of the analysis and, when available, a [description](https://docs.cloud.google.com/looker/docs/reference/param-explore-query#description).

If [starter questions](https://docs.cloud.google.com/looker/docs/gemini-quick-starts#generating_quick_start_analyses_for_an_explore) are enabled for your instance, when you select an Explore from the Explore menu that doesn't already have defined starter questions, Gemini in Looker will give you an option for **Starter Questions**. Click the **Starter Questions** drop-down field, and Gemini will analyze the Explore and generate starter question Explores.

**Tip:** More information on how developers can model prebuilt analyses for users is available on the [`query`](https://docs.cloud.google.com/looker/docs/reference/param-explore-query) parameter documentation page.

You can open a starter question analysis from a blank Explore in the new Explore experience or once an Explore has already been run in the new Explore experience.

**Important:** See Starter question filter behavior in this section for things to know about resolving starter question filter conflicts.

#### Choosing a starter question from a blank Explore in the new Explore experience

To run a starter question analysis, click the **Starter Questions** drop-down field and choose the analysis that you want to explore. The query will automatically run and display results, including the visualization.

You can modify a starter question analysis once it has run by adding fields or removing fields from the **All Fields** tab, from **Search** results, or from the **Fields in use** tab in the **Configure** panel.

#### Choosing a starter question once an Explore has run in the new Explore experience

Once an Explore has finished running in the new Explore experience, you can select a new starter question analysis by clicking the dynamic_form [**Show starter questions** button](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-new-explore-experience#navigating-the-new-explore-experience) to open the **Starter Question** panel to view the available analysis cards.

Clicking a starter question analysis card from the panel runs the analysis and replaces all the previous Explore results, except for any existing filters.

#### Starter question filter behavior

Filters are additive. This means that, when run, starter question analyses will include any existing Explore filters. If a selected starter question analysis has a filter that conflicts with an existing Explore filter, you will be prompted to select which filter value to use in the Explore query.

When you choose a starter question analysis with a conflicting filter configuration, the **Choose filter set** dialog will open and prompt you to resolve the conflict by selecting either the **Keep current filters** option, which lists the existing filter configuration, or the **Replace with new filters** option, which lists the configured filter values of the starter question analysis.

To resolve the conflict in the **Choose filter set** dialog, follow these steps:

  1. Choose an option. 
     * Choose **Keep current filters** to run the new analysis with the existing filter configuration.
     * Choose **Replace with new filters** to run the new analysis with its configured filter condition.
  2. Click **Apply** to confirm the filter selection and run the analysis.



The Explore will run with the selected filter configuration.

## Navigating the Configure panel

Once you have [opened an Explore in the new Explore experience](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-new-explore-experience#finding-explores-in-looker), you can use the **Configure** panel to create, edit, and configure Explore queries and visualizations. The **Configure** panel includes the following elements:

![](https://docs.cloud.google.com/static/looker/docs/images/nextgen-explore-configure-panel-264.png)

  1. The close **Close** button: When clicked, closes the **Configure** panel. Alternatively, use the build **Configure** button to display or hide the **Configure** panel.
  2. The **All Fields** tab: Displays all available fields for an Explore.
  3. The **Fields in use** tab: Displays all the Explore fields that are selected in the query.
  4. The **Style** tab: Displays the options for configuring the query visualization. Learn more about [using the **Style** tab](https://docs.cloud.google.com/looker/docs/editing-visualizations-new-explore-experience) to configure visualizations.
  5. The name of the Explore.
  6. The number of fields that are selected in the Explore query.
  7. The info **Explore Summary** info button: When clicked, displays a description of the Explore that was either added by a developer, or [generated by Gemini in Looker](https://docs.cloud.google.com/looker/docs/explore-summary-gemini).
  8. The search bar: Lets users search for fields that match specific terms and criteria.
  9. The Explore views: Displays the views that are included in the Explore, and the number of fields from that view that are in the Explore query. Click the name of the view to expand or collapse the view details. When expanded, each view lists the fields that are available to use in the Explore, organized under field type headers: **Dimensions** , **Measures** , and **Filter-Only Fields**. [Custom fields](https://docs.cloud.google.com/looker/docs/custom-fields) and [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) will appear under the **Custom Fields** view label. The base view is indicated with the **Base view** label.
  10. The field-specific information and actions icons: Display a field's current and potential functions in an Explore query, as well as more details about a field.
  11. The **Clear all** and **Clear fields keep filters** options: When clicked, **Clear all** clears all of the Explore fields, and **Clear fields keep filters** clears the Explore fields but keeps any filters that are applied.
  12. The join_left **Merge queries (join data)** button: Opens the **Join data** page. Learn more about [joining data in the new Explore experience](https://docs.cloud.google.com/looker/docs/merge-queries-new-explore).
  13. The Explore summary: Displays the total number of fields in an Explore (including custom fields and table calculations when [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_table_calculations) allow), and the **Go to LookML** link. The **Go to LookML** link directs users to the `explore` definition in its LookML project. This link is visible only to users with the [`see_lookml`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_lookml) permission.



### Using the field-specific information and actions icons

The icons next to each field provide more information about the field and indicate the available options for that field. The icons are visible when you hold your cursor over a field.

You can click an icon to make changes to a query by using a field, depending on the field's data type, including filtering or pivoting by a field. You can also use icons to view information about a field, or — when [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_fields) allow — to create a custom field that is based on the field.

These icons appear on the **All Fields** and **Fields in use** tabs.

**Tip:** You can also use field-specific actions in the data column more_vert **More** menu to edit the Explore query and visualization around a specific column. See Using the data column **More** menu on this page for more details.

The available icons and functions include the following:

  1. The pivot_table_chart **Pivot data** icon: Click this icon to pivot or unpivot a field in an Explore. This icon will persist next to a field name when a field is pivoted. Click the persisted icon to remove the pivot. Learn more about pivoting data.
  2. The filter_alt **Filter by field** icon: Click this icon to [filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting-new-explore-experience) the query results by a field. This icon will persist next to a field name when a field is filtered. Click the persisted icon to remove the filter.

  3. The info **Info** icon: Click this icon to display more information about a field:

     * The information includes the field's data type, [description](https://docs.cloud.google.com/looker/docs/reference/param-field-description) (when available), and LookML field name (in `view_name.field_name` syntax) for all users.
     * For users with the [`see_lookml`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_lookml) permission, the information will include the definition of the LookML field's [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameter, as well as a link to navigate to that field in the LookML project.

  4. The more_vert **More** menu: Click this icon to create a custom field or to switch a timeframe for a [dimension group](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group). This icon is available only to users in certain cases:

     * When a user has the [`create_custom_fields`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_fields) permission. Users with the `create_custom_fields` permission can use the more_vert **More** menu to quickly create [custom fields](https://docs.cloud.google.com/looker/docs/custom-fields), depending on a field's type.
     * When a dimension group is selected in the Explore query. The more_vert **Switch to** option will appear for dimension groups on the **Fields in use** tab, in addition to custom fields options.



### Using the data column More menu

In addition to the field-specific information and action icons, you can edit a query and visualization in the new Explore experience with the options in the data column more_vert **More** menu.

The options that are displayed depend on the field type and a user's [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permissions_list).

For dimensions and measures, the data column **More** menu options can include the following:

  * delete_outline **Remove** : Removes the column field from the Explore query.
  * filter_alt **Filter** : Filters the Explore query by the column field. Learn more about [filtering data in the new Explore experience](https://docs.cloud.google.com/looker/docs/filtering-and-limiting-new-explore-experience).
  * filter_alt_off **Remove Filter** : Removes a filter field. This option is available when an Explore is filtered by the field.
  * pivot_table_chart **Pivot** : Pivots a field in an Explore query. Learn more about pivoting data.
  * pivot_table_chart **Unpivot** : Unpivots a field in an Explore query. This option is available when a field is pivoted, and in the pivot row more_vert **More** menu.
  * compare_arrows **Switch to** : Displays a list of timeframes for dimension groups that users can switch between in a query.
  * visibility_off **Hide from visualization** : Hides the column field from the visualization. If a field is hidden from the visualization, this option appears as remove_red_eye **Show in visualization**. Learn more about [hiding fields from visualizations](https://docs.cloud.google.com/looker/docs/creating-visualizations#temporary_hide).
  * visibility_off **Hide "No"s from visualization** : For `yesno` type fields, hides the rows that correspond to "No"s from the visualization. If "No"s are hidden from the visualization, this option appears as remove_red_eye **Show "No"s in visualization**. Learn more about [`yesno` type fields](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#yesno).
  * function **Calculations** : Displays a list of [shortcut calculations](https://docs.cloud.google.com/looker/docs/table-calculations#using_a_fields_data_table_gear_menu_to_use_shortcuts_for_common_calculations) to let users who have the [`create_table_calculations` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_table_calculations) create a table calculation that is based on the column field. This option is available only for non-string-based data types.
  * content_copy **Copy values** : Copies all the values from a table column to paste into a document or a tool like Excel or Google Sheets.
  * bar_chart **Bin** : Opens the [**Bin**](https://docs.cloud.google.com/looker/docs/custom-fields#custom_binning) dialog to let users who have the [`create_custom_fields` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_field) create custom bins that are based on the column field. Custom bins are available only for certain [field types](https://docs.cloud.google.com/looker/docs/custom-fields#bin).
  * rule **Group** : Opens the [**Group By**](https://docs.cloud.google.com/looker/docs/custom-fields#custom_grouping) dialog to let users who have the [`create_custom_fields` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_field) create a custom group that is based on the column field. Custom groups are available only for certain [field types](https://docs.cloud.google.com/looker/docs/custom-fields#group).
  * sort_by_alpha **Sort** : Sorts the query by the column field in either **Ascending** or **Descending** order. Learn more about sorting data.
  * sort_by_alpha **Add additional sort** : Sorts the query by a secondary column field in either **Ascending** or **Descending** order. Learn more about sorting data. This option is only available if an Explore is already sorted by a different field.



In addition to the previous options, table calculations and custom fields data column **More** menu options can include the following:

  * content_copy **Duplicate** : Duplicates the table calculation or the custom field in the query.
  * edit **Edit** or **Edit Calculation** : Opens a dialog for [editing a table calculation](https://docs.cloud.google.com/looker/docs/table-calculations#editing_table_calculations) or [editing a custom field](https://docs.cloud.google.com/looker/docs/custom-fields#editing_a_custom_field).
  * delete_forever **Delete** : Permanently deletes a custom field or table calculation from an Explore query _and_ the **Configure** panel. To remove a custom field or a table calculation from the Explore query, but _not_ from the **Configure** panel, use the delete_outline **Remove** option.



### Using the All Fields tab

When you open an existing Explore in the new Explore experience, the **All Fields** tab is displayed by default. This tab is the starting place for building an Explore and displays all the available fields that you can select for a query. Fields are organized alphanumerically by type (dimensions, followed by measures) under the name of the [view](https://docs.cloud.google.com/looker/docs/reference/param-view-view) or [view label](https://docs.cloud.google.com/looker/docs/reference/param-field-view-label) in which they are defined. Each field will show field-specific information and actions, such as a field's current and potential functions in an Explore query.

Click the name of the view to expand or collapse the view details. When expanded, each view lists the fields that are available to use in the Explore, organized under field type headers: **Dimensions** , **Measures** , and **Filter-Only Fields**. [Custom fields](https://docs.cloud.google.com/looker/docs/custom-fields) and [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) will appear under the **Custom Fields** view label. The base view is indicated with the **Base view** label. Users with the [`create_table_calculations`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_table_calculations) permission can create and edit table calculations, and users with the [`create_custom_fields`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_fields) permission can create and edit custom fields by clicking **\+ Add** , or by choosing a custom field option from a field's more_vert **More** menu.

**Caution:** Users _must have_ the `create_custom_fields` permission to see the more_vert **More** menu. The only exception is for [dimension groups](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) in the **Fields in use** tab.

Fields that are selected in a query will appear highlighted by a background, and any corresponding field action icons (pivot, filter) will appear in bold without you needing to hold the pointer over a field when it is active.

You can click **Clear all** to remove all of the fields from the Explore, or click **Clear fields keep filters** to clear the Explore fields but keep any filters that are applied.

### Using the Fields in use tab

The **Fields in use** tab provides a snapshot of the Explore, including the chart type that is selected in the **Visualization** pane, and all of the fields that are active in an Explore, organized alphanumerically by [view](https://docs.cloud.google.com/looker/docs/reference/param-view-view) or [view label](https://docs.cloud.google.com/looker/docs/reference/param-field-view-label), and under the corresponding field type headers (**Dimensions** , **Measures** , and **Filter-Only Fields**).

The **Fields in use** tab also displays the total number of active fields in an Explore in the Explore summary. A **Go to LookML** link is also available to users with the [`see_lookml`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_lookml) permission. **Go to LookML** directs users to the `explore` definition in its LookML project.

You can click fields to remove them from an Explore, click **Clear all** to remove all of the fields from the Explore, or click **Clear fields keep filters** to clear the Explore fields but keep any filters that are applied.

### Using the search bar

The search bar lets you quickly find the specific fields that you need to build Explores in the new Explore experience. To perform a search, enter a term into the search bar.

To refine the scope of your search, click tune **Search Options**. You can limit your search to [field labels](https://docs.cloud.google.com/looker/docs/reference/param-field-label), [field descriptions](https://docs.cloud.google.com/looker/docs/reference/param-field-description), [group labels](https://docs.cloud.google.com/looker/docs/reference/param-field-group-label), or [view labels](https://docs.cloud.google.com/looker/docs/reference/param-field-view-label).

**Tip:** For exact searches, wrap your search term in quotes.

## Adding fields

You can add fields to queries in the new Explore experience in one of several ways:

  * By choosing a starter question
  * By dragging a field from the **All Fields** tab and dropping it into the [**Data** pane](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-new-explore-experience#navigating-the-new-explore-experience)
  * By clicking on a field from the **All Fields** tab



Once you have added all of the fields that you want in the Explore query, click **Run to update**.

See the sections for Adding table calculations and Adding custom fields on this page for information about performing advanced analyses in the new Explore experience.

### Adding table calculations

Users with the [`create_table_calculations`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_table_calculations) permission can create calculations in the following ways:

  * By clicking **\+ Add** in the **Custom Fields** view and choosing **Table Calculation** to open the [**Create table calculation**](https://docs.cloud.google.com/looker/docs/table-calculations#using_the_add_button_in_the_custom_fields_section_of_the_field_picker_to_create_table_calculations) dialog.

**Tip:** Creating a table calculation with the **\+ Add** button lets you create a table calculation using a [Looker expression](https://docs.cloud.google.com/looker/docs/creating-looker-expressions). Looker expressions let you include other dimensions, and, when available, use [Gemini assistance for assistance in creating a Looker expression](https://docs.cloud.google.com/looker/docs/gemini-expression-asst#using)
  * By clicking a field's data column more_vert **More** menu and choosing a [shortcut calculation](https://docs.cloud.google.com/looker/docs/table-calculations#types_of_common_calculation_shortcuts) from the function **Calculations** option menu.




#### Editing and duplicating table calculations

You can [edit](https://docs.cloud.google.com/looker/docs/table-calculations#editing_table_calculations) or [duplicate](https://docs.cloud.google.com/looker/docs/table-calculations#editing_table_calculations) table calculations in the following ways:

  * By choosing the appropriate option in the calculation's more_vert **More** menu in the **Custom Fields** view in the **All Fields** or **Fields in use** tabs
  * By choosing the appropriate option in the calculation's data column more_vert **More** menu



See Removing fields on this page to learn how to delete or remove table calculations from queries in the new Explore experience.

### Adding custom fields

Users with the [`create_custom_fields`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_fields) permission can create custom fields in the following ways:

  * By clicking **\+ Add** in the **Custom Fields** view and choosing either the **Custom Dimension** or **Custom Measure** option. Choosing one of these options opens the [**Create Custom measure** dialog](https://docs.cloud.google.com/looker/docs/custom-fields#using_the_custom_fields_section) for custom measures, or the [**Create Custom dimension** dialog](https://docs.cloud.google.com/looker/docs/custom-fields#creating_a_custom_dimension_using_a_looker_expression) for custom dimensions.

**Tip:** Creating a custom dimension with the **\+ Add** button lets you create a custom dimension using a [Looker expression](https://docs.cloud.google.com/looker/docs/creating-looker-expressions). Looker expressions let you include other dimensions, and, when available, use [Gemini assistance for guidance in creating a Looker expression](https://docs.cloud.google.com/looker/docs/gemini-expression-asst#using). To create a [custom bin](https://docs.cloud.google.com/looker/docs/custom-fields#custom_binning) or a [custom group](https://docs.cloud.google.com/looker/docs/custom-fields#custom_grouping) on an existing dimension, use the dimension's more_vert **More** menu in the **All Fields** tab or **Fields in use** tab, or a field's data column more_vert **More** menu.
  * By clicking a field's more_vert **More** menu in the **All Fields** tab or **Fields in use** tab in the **Configure** panel and choosing [**Aggregate**](https://docs.cloud.google.com/looker/docs/custom-fields#using_the_dimensions_three-dot_more_menu), [**Bin**](https://docs.cloud.google.com/looker/docs/custom-fields#custom_binning), [**Group**](https://docs.cloud.google.com/looker/docs/custom-fields#custom_grouping), or [**Create filtered measure**](https://docs.cloud.google.com/looker/docs/custom-fields#creating_a_filtered_measure_from_another_measure), depending on the field's type.

  * By clicking a field's data column more_vert **More** menu and choosing bar_chart **Bin** or rule **Group** to open the [**Bin**](https://docs.cloud.google.com/looker/docs/custom-fields#custom_binning) dialog or [**Group By**](https://docs.cloud.google.com/looker/docs/custom-fields#custom_grouping) dialog.




#### Editing and duplicating custom fields

You can [edit](https://docs.cloud.google.com/looker/docs/custom-fields#editing_a_custom_field) or [duplicate](https://docs.cloud.google.com/looker/docs/custom-fields#duplicating_a_custom_field) custom fields in the following ways:

  * By choosing the appropriate option in the custom field's more_vert **More** menu in the **Custom Fields** view in the **All Fields** or **Fields in use** tabs
  * By choosing the appropriate option in the custom field's data column more_vert **More** menu



See Removing fields on this page to learn how to delete or remove custom fields from queries in the new Explore experience.

## Removing fields

You can remove fields from queries in the new Explore experience in several ways:

  * By clicking an individual field name in the **All Fields** tab, or in the **Fields in use** tab.
  * By clicking **Clear all** in the **Fields in use** tab to remove all of the fields in an Explore query.
  * By clicking **Clear fields keep filters** in the **Fields in use** tab to remove all of the fields in the Explore query, but keep any filters that are applied to the Explore query.
  * By clicking delete_outline **Remove** from the data column more_vert **More** menu.
  * By clicking delete_forever **Delete** from the data column more_vert **More** menu. The **Delete** option permanently deletes a custom field or table calculation from an Explore query _and_ the **Configure** panel. To remove a custom field or a table calculation from the Explore query, but _not_ the **Configure** panel, use the delete_outline **Remove** option.



Once you have removed all of the fields that you want to remove from the Explore query, click **Run to update**.

## Sorting data

Unpivoted data in the new Explore experience is sorted by default according to the following prioritization:

  1. By the first date dimension, descending
  2. If no date dimension exists, by the first measure, descending
  3. If no measure exists, by the first added dimension, ascending



For information on sorting pivoted data, see the Pivots and sorting section.

A field's sort order is indicated in the [data table](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-new-explore-experience#navigating-the-new-explore-experience) in several ways:

  * With a number and an **^** upward-facing or **⌄** downward-facing arrow next to the field name that distinguishes its sort-by order and sort direction, as compared to other fields
  * With an arrow next to the field name that indicates the sorting direction (**^** pointed up for ascending or **⌄** down for descending)
  * With a tooltip that appears when you hold the pointer over a field name



You may want to sort data differently than the default order. You can sort by clicking a field's column header in the data table to sort the query by that field:

  * Click a field's column header once to sort by that field in descending order.
  * Click a field's column header twice to sort that field in ascending order.



Alternatively, you can click the sort_by_alpha **Sort** option in the field's data column more_vert **More** menu.

To sort _multiple_ fields, hold down the **Shift** key and then click the column headers in the order that you want them sorted. Alternatively, you can click the sort_by_alpha **Add additional sort** option in the field's data column more_vert **More** menu.

### Things to know about sorting

  * Some sorting in Explores is performed on the client side (in the user's browser) to reduce the number of round-trip calls to databases, which can be both costly and time consuming. However, this behavior can lead to inconsistencies between Explore results and other Looker content, as sorting between client and database can produce different results — especially if system locales differ.
  * If you reach a [row limit](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#limiting_data), you won't be able to sort row totals or [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations#cannot-sort).
  * Any sorting that is applied in the **Visualization** pane (and not in the **Data** pane) is a temporary client-side operation and won't persist when an Explore is [saved as a Look](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks#saving_looks_from_an_explore) or [as a dashboard tile](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#creating_a_dashboard_from_a_look_or_an_explore).



## Pivoting data

Multiple dimensions are often easier to look at when you pivot one of the dimensions horizontally. Each value in the dimension will become a column in your query. This makes the information easier to consume visually and reduces the need to scroll to find data. Looker supports up to 200 pivoted values.

To pivot results by a dimension in the new Explore experience, follow these steps:

  1. In the **All Fields** or **Fields in use** tab, position your cursor over the dimension name and click the pivot_table_chart **Pivot data** icon.

Alternatively, click the pivot_table_chart **Pivot** option in a field's data row more_vert **More** menu.

  2. Click **Run to update** to re-run the query.




You can add an additional field to the pivot table by dragging the field from the **All Fields** tab and dropping it into the [**Data** pane](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-new-explore-experience#navigating-the-new-explore-experience), and then specifying if the new field should be a column or row (for dimensions), or a value (for measures and table calculations).

You can unpivot a field by clicking the dimension's pivot_table_chart **Pivot data** icon from either the **All Fields** tab or the **Fields in use** tab. Alternatively, you can click the pivot_table_chart **Unpivot** option from a field's data row more_vert **More** menu.

**Important:** A row of data whose value does not appear in a column is indicated with the **∅** null value symbol.

### Pivots and sorting

You can also sort pivoted dimensions by clicking the field name header of the dimension in the data table, or by clicking the sort_by_alpha **Sort** option in the field's data row more_vert **More** menu menu.

To sort by _multiple_ pivoted dimensions, hold down the **Shift** key and then click the row headers in the order that you want them sorted. Alternatively, you can click the sort_by_alpha **Add additional sort** option in the field's data row more_vert **More** menu. When you're sorting a pivoted measure, any rows with values in that column are sorted first, followed by rows without data in that column (indicated by the **∅** null value symbol).

**Tip:** You can also create custom sorting using the [`case`](https://docs.cloud.google.com/looker/docs/reference/param-field-case) parameter.

## Reordering columns

You can reorder columns in the **Data** pane data table by clicking a column header and dragging and dropping the column to its new position. The visualization will reflect the new column order after you click the **Run to update** button.

The order of columns in the data table is based on field type:

  1. Dimensions (including [custom fields](https://docs.cloud.google.com/looker/docs/custom-fields))
  2. Dimension [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations)
  3. Measures (including custom fields)
  4. Measure table calculations
  5. Row totals



For the most part, columns can be reordered within each field type but cannot be moved out of their field type section.

For example, dimension table calculations can be rearranged among themselves, but you cannot place a dimension table calculation in between two measures.

Columns under a pivoted dimension can be reordered, but the order of pivoted dimensions can be changed only by changing the sort order, not by manual reordering.

## Displaying totals

Sometimes a summary of your data is useful. You can add column or row totals to a query in the new Explore experience by clicking the **Totals** switch [in the data table](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-new-explore-experience#navigating-the-new-explore-experience) and then rerunning the query.

If you've added row totals, and your query exceeds any [row limit](https://docs.cloud.google.com/looker/docs/filtering-and-limiting-new-explore-experience#row-limits) that you've set, you won't be able to sort the **Row Totals** column (although you can sort dimension and measure columns as normal). This is because you might be missing rows in your data that should be included in your totals. If you run into this issue, you can try increasing the query's row limit to 5,000 rows (or up to 50,000 rows [if a higher limit is specified by your admin](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails#visualization-limits)).

### When totals aren't available

There are some cases when totals won't be available:

  * Column totals are available only for measures and table calculations that exclusively reference measures, not for dimensions or table calculations that reference dimensions.
  * Row totals are available only for measures, not for dimensions or table calculations that are based on dimensions.
  * Certain types of columns won't be totaled, because of database limitations or because the value wouldn't make sense as a total. For example, you can't add together a list of words.



### Things to consider with totals

Additionally, there are some things to keep in mind about how totals work in certain situations:

  * Columns that count unique items might not add up as you expect, since the same item might show up in several categories but be counted as only one unique item in the totals. See the [Why don't my totals match the values in my table?](https://docs.cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-looker-totals) Best Practices page for more details.
  * The **Row Totals** feature creates an additional query, and this query has a limit of 30,000 rows. If your Explore query has more than 30,000 rows, row totals will be shown for the first 30,000 rows only. Furthermore, if the data is pivoted, the row totals limit is further reduced by the number of options in your pivot.
  * Some [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) that perform aggregations, such as calculations that use `percentile` or `median`, might not add up as you expect. This is because table calculations calculate totals by using the values in the **Total** row, not the values in the data column. See the [Display potentially confusing table calculation totals as nulls](https://docs.cloud.google.com/looker/docs/best-practices/how-to-display-confusing-table-calculation-totals-as-nulls) Best Practices page for troubleshooting tips.
  * If you've [filtered](https://docs.cloud.google.com/looker/docs/filtering-and-limiting-new-explore-experience#filtering_data) your query by a measure, totals may appear to be too high. However, in actuality, what you're seeing is a total for your data _before_ the measure filter is applied. In other words, the measure filter may be hiding some data from your query results, even though that data is included in the total.
  * If you've used totals with [merged results](https://docs.cloud.google.com/looker/docs/new-explore-experience-merge-queries), Looker calculates totals on each of the component queries and uses those totals in the merged result. Therefore, totals may appear too high, because what you are seeing are totals calculated before the [results were merged](https://docs.cloud.google.com/looker/docs/merged-results#what_if_one_query_doesnt_have_a_matching_data_value). One way to avoid this is to align the filters on each query.
  * Similarly, if you've placed [row](https://docs.cloud.google.com/looker/docs/filtering-and-limiting-new-explore-experience#row-limits) or [column](https://docs.cloud.google.com/looker/docs/filtering-and-limiting-new-explore-experience#column-limits) limits on your query, and your query results exceed that limit, totals may also appear to be too high. However, what you're seeing is a total for your data _before_ the limits are applied. In other words, the limits may be hiding some data from your query results, even though that data is included in the total.



In the situations involving merged results, it is possible to calculate totals _only_ for the data that you can see. To do so, you'll need to use a table calculation. For a column total, use `sum(${view_name.field_name})`. For a row total, use `sum(pivot_row(${view_name.field_name}))`.

**Note:** For information about displaying subtotals in table visualizations, see the [Table chart options](https://docs.cloud.google.com/looker/docs/table-options#subtotals) documentation page.

## Features for developers

Depending on your [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permissions_list), you may see several features that are designed for Looker developers in the **Configure** panel:

  * The **Go to LookML** option on the **All Fields** and **Fields in use** tabs lets developers navigate to the Explore LookML.
  * The **Go to LookML** option in a field's settings **Filter actions** menu in the **Filters** pane lets developers navigate to the field's LookML.
  * The `sql` parameter definition in a field's info **Info** icon menu lets developers see a field's `sql` definition without needing to navigate to the field's LookML.
  * The **Go to LookML** option in a field's info **Info** icon menu lets developers see the field's LookML.
  * The [**SQL query** button](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-new-explore-experience#navigating-the-new-explore-experience) in the new Explore experience **Data** pane lets Looker developers see [the SQL query](https://docs.cloud.google.com/looker/docs/how-looker-generates-sql#viewing_the_query) that Looker sends to the database to retrieve the data.
  * The [Explore query tracker](https://docs.cloud.google.com/looker/docs/query-tracker#explore_query_tracker) lets Looker developers track the performance and execution of the Explore query.



## Related resources

  * Learn how to [filter and limit queries in the new Explore experience](https://docs.cloud.google.com/looker/docs/filtering-and-limiting-new-explore-experience).
  * Learn how to [perform ad hoc analyses with table calculations](https://docs.cloud.google.com/looker/docs/table-calculations).
  * Learn how to [create custom fields and measures](https://docs.cloud.google.com/looker/docs/custom-fields).
  * Learn how to [edit visualization configurations in the new Explore experience](https://docs.cloud.google.com/looker/docs/editing-visualizations-new-explore-experience).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
