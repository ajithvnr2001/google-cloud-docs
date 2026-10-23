---
url: https://docs.cloud.google.com/looker/docs/using-looker-data-dictionary/
title: Using the Looker Data Dictionary extension \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:37.896466+00:00
---

# Using the Looker Data Dictionary extension  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/using-looker-data-dictionary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Using the Looker Data Dictionary extension Stay organized with collections  Save and categorize content based on your preferences. 

The Looker Data Dictionary is an extension — a web application built using Looker components — developed using the Looker [extension framework](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework) and deployed through the [Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace).

The Looker Data Dictionary extension provides a dedicated, centralized interface for searching through all your Looker fields and descriptions. Use this extension to perform these tasks:

  * Provide a searchable directory for all metrics and descriptions for users to identify the appropriate dimension or measure for analysis.
  * Enable external stakeholders to identify and locate unique metrics.
  * Audit LookML models to assess whether consistent naming conventions are followed, whether there are redundant fields, or whether fields are annotated with descriptions.
  * Add and share comments about specific fields (if your Looker Data Dictionary application is on version 2.0.0 or later). You can verify that you have the most updated version of the Data Dictionary by going to the Looker Marketplace, selecting **Manage** , and selecting the **Update** button next to the extension.



## Data Dictionary workflow

For users to access and use the Looker Data Dictionary, a Looker admin must perform the following steps:

  1. Enable the appropriate features.
  2. Install the Looker Data Dictionary extension.
  3. Grant permissions to access the Looker Data Dictionary.



Once the extension is available to users, you can do the following:

  1. Navigate to the Looker Data Dictionary extension.
  2. View your model's metadata.



### Before you begin

Before installing the Looker Data Dictionary from the [Marketplace](https://docs.cloud.google.com/looker/docs/marketplace), a Looker admin must enable these features:

  * [**Marketplace**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-marketplace): To access the Looker Marketplace (enabled by default)
  * [**Extension Framework**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-extension-framework): To deploy extensions that are developed using the Looker extension framework (enabled by default)



Installing applications and tools — such as extensions — from the Looker Marketplace requires that you have the `develop`, `manage_models`, and `deploy` [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permissions_list).

## Installing the Looker Data Dictionary

See the [Using the Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace#installing_a_tool_from_the_marketplace) documentation for instructions on installing a tool from the Looker Marketplace. After the Data Dictionary is installed, a Looker admin must grant users permissions to perform the following tasks:

  * Access the Looker Data Dictionary extension
  * Interact with field comments



### Granting permissions to access the Looker Data Dictionary extension

After the Looker Data Dictionary is installed, a model called `data-dictionary` is automatically added to the list of available models on the [**New Model Set**](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#creating_a_model_set) and [**Edit Model Set**](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#editing_a_model_set) pages, accessible from the **Roles** page in the **Admin** panel.

A Looker admin must grant users `explore` or `develop` [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permissions_list) to access the `data-dictionary` model and any models they need to explore in the Data Dictionary. See the [Setting permissions for Looker extensions](https://docs.cloud.google.com/looker/docs/setting-permissions-for-extensions) documentation page for information on granting users permissions to access and use extensions.

### Granting permissions to interact with field comments

Field comments provide users with the ability to add context to field definitions without having to update any LookML. By default, all users who have access to the data dictionary extension will be able to see all comments, and add, edit, and delete their own comments.

A Looker admin can manage how users interact with the field comment functionality by creating specific user groups on the **Groups** page of the **Admin** panel and assigning users to those groups. See the [Groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups) documentation page for more information about how to assign users to groups.

The user groups must be created with the predefined names that are shown in the Group Name column of the following table. The table also shows the predefined privileges that users assigned to each group will have.

Group Name | Privileges  
---|---  
`marketplace_data_dictionary_comments_disabled` | Users cannot see or otherwise interact with any comments; all comment capabilities are disabled. This group's privileges always take precedence over those of other groups — any user included in the `disabled` group won't be able to see or make comments, even if they also belong to another group that has more elevated privileges.  
`marketplace_data_dictionary_comments_reader` | User can see existing comments, but cannot add any.  
`marketplace_data_dictionary_comments_writer` | Users can see all comments, add new comments, and edit/delete their own. **This is the default privilege.**  
`marketplace_data_dictionary_comments_manager` | Users can see all comments, add new comments, and edit/delete all comments.   
  
If a user doesn't belong to any of these groups, they will default to `writer`. If a user is assigned to multiple groups (not including `marketplace_data_dictionary_comments_disabled`), their more elevated privilege takes precedence.

**Note:** Changes to a comments group, such as adding or removing a user, that are made on the [**Groups**](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups) page in the **Admin** panel will take effect after a hard refresh of the Data Dictionary page or after the user selects another option and then returns to the Data Dictionary page.

## Navigating to the Looker Data Dictionary extension

You can navigate to the Data Dictionary from the list of installed applications and extensions in the left sidebar.

![](https://docs.cloud.google.com/static/looker/docs/images/marketplace-extensions-data-dictionary-access-2416.png)

## Viewing model metadata with the Looker Data Dictionary

In the Looker Data Dictionary, users with `explore` permissions on a model can select this [model](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#model) and view its metadata, including its [Explores](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#explore) and each Explore's list of [fields](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#field), grouped by [view](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#view). The Looker Data Dictionary displays the selected model's Explores in the left sidebar and the selected Explore's views and fields on the main part of the page.

Users can collapse the sidebar by selecting the **<** icon.

The Looker Data Dictionary shows the following information:

![](https://docs.cloud.google.com/static/looker/docs/images/develop-data-dictionary-ui-2402.png)

  1. The name of the selected model
  2. The list of Explores contained in the selected model
  3. The selected Explore
  4. A text field to filter the fields in an Explore
  5. Quick filters to narrow displayed fields based on selected characteristics
  6. The name of the view
  7. Metadata about each field. Select what metadata is displayed by selecting the **View Options** button. See the field's entire set of metadata in the field profiler.
  8. Rows containing metadata for each field in a given view
  9. Navigation to the Explore in the Looker UI



## Selecting a model and an Explore

The **Select a Model** drop-down lists all the models for which a user has `explore` permissions. When choosing a model from the **Select a Model** drop-down menu, the left sidebar will populate with a list of that model's Explores.

You can also search the selected model for a specific Explore by typing in the **Search Model** search box. The list of Explores will filter to display only the results that match your search terms.

Select the name of an Explore to see its fields, grouped by view, displayed on the main part of the page.

You can also select the **Explore** button in the upper right corner to go straight to the [Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) page in Looker.

## Filtering fields in an Explore

You can filter the displayed fields by typing text into the **Filter fields in this Explore** box to match against the list of fields' **Field Label** or **Description**.

You can also select specific metadata attributes to filter on, such as whether the field:

  * Has a [description](https://docs.cloud.google.com/looker/docs/reference/param-field-description)
  * Is a [dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension) or a [measure](https://docs.cloud.google.com/looker/docs/reference/param-field-measure)
  * Has [tags](https://docs.cloud.google.com/looker/docs/reference/param-field-tags)
  * Has type [string](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#string), [number](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#number), [date](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#date_types), [zipcode](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#zipcode), [count](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count), [sum](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum), [average](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#average), [list](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#list), or [unquoted](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter#parameters_of_type:_unquoted)



## Viewing field metadata

The Looker Data Dictionary displays the metadata for an Explore's fields, grouped by view:

  * **Field Label** : The field name according to the field's [`label` parameter](https://docs.cloud.google.com/looker/docs/reference/param-field-label)
  * **Category** : The field category as a [dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension) or a [measure](https://docs.cloud.google.com/looker/docs/reference/param-field-measure)
  * **Description** : The field's description according to the field's [`description` parameter](https://docs.cloud.google.com/looker/docs/reference/param-field-description)
  * **LookML Name** : The field name in `view_name.field_name` syntax
  * **Type** : The field type as [string](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#string), [number](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#number), [date](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#date_types), [zipcode](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#zipcode), [count](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count), [sum](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum), [average](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#average), [list](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#list), or [unquoted](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter#parameters_of_type:_unquoted) according to the field's `type` parameter
  * **SQL** : The [SQL expression](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) that references that field
  * **Tags** : The [LookML tags](https://docs.cloud.google.com/looker/docs/reference/param-field-tags) associated with that field



### Customizing displayed metadata

You can specify what metadata is displayed for each field by selecting the **View Options** button in the upper right corner and checking or unchecking the boxes for metadata you want to view.

![](https://docs.cloud.google.com/static/looker/docs/images/develop-data-dictionary-view-options-2310.png)

## Using field comments

**Note:** If an instance already has the Data Dictionary installed, a Looker admin should [verify](https://docs.cloud.google.com/looker/docs/marketplace#managing_installed_tools) that the Data Dictionary extension is on version 2.0.0 or later to use field-level comments.

LookML developers often include additional information or explanations about a model's fields in the field-level [`description`](https://docs.cloud.google.com/looker/docs/reference/param-field-description) parameter. However, these descriptions are not always meaningful or useful to all users. With field-level comments, users can add context to a specific field. These comments are viewable by other users but will not affect the model's underlying LookML.

A Looker admin must grant users the ability to interact with comments by adding them to specific groups on the **Groups** page of the **Admin** panel. By default, all users with access to the data dictionary extension can view all comments and add, edit, and delete their own comments.

### Adding a field comment

To add a comment to a field:

![](https://docs.cloud.google.com/static/looker/docs/images/marketplace-extensions-data-dictionary-add-comment-1-2310.png)

  1. Hover over the field row to reveal a **+** icon (if there are no existing field comments) or a notepad icon (if a field has existing comments). Click the icon to open the **Comments** tab of the field profiler panel.
  2. Click the **Add Comment** button.
  3. Type your comment and select the **Comment** button to save your entry. Click **Cancel** to close the field profiler. You can expand the comment box by selecting and dragging the bottom right corner.



Once a comment has been added, it appears on the **Comments** tab of the field profiler and is viewable to other users.

### Viewing field comments

When a field includes comments, a notepad icon appears with the number of comments that exist on that field. Click the notepad icon to view the field's comments listed in the **Comments** tab of the field profiler.

The number of comments on that field is also indicated in parentheses on the **Comments** tab. Each comment entry shows the following information:

  * The commenter's name
  * The timestamp showing when the comment was added
  * A preview of the comment



### Editing or deleting a field comment

To edit or delete your own field comments:

![](https://docs.cloud.google.com/static/looker/docs/images/marketplace-extensions-data-dictionary-edit-delete-comment-1-2310.png)

  1. Select the field's notepad icon.
  2. On the **Comments** tab, locate and hover over the comment that you would like to edit or delete.
  3. Click the three-dot menu, and select **Edit Comment** to edit the comment or **Delete Comment** to delete the comment. If you're deleting the comment, confirm your intention.
  4. If you're editing your comment, select **Save** once you've made your changes.



### Sharing a field comment

The URL of the **Comments** tab for each field is unique and can be copied and shared with other users who have access to that model in the Looker Data Dictionary.

## Using the field profiler

Click a specific field row to open a field profiler panel that displays the field's entire set of metadata, options to preview numeric dimension values, and buttons to navigate to the [Looker IDE](https://docs.cloud.google.com/looker/docs/looker-ide) or the [Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) page.

![](https://docs.cloud.google.com/static/looker/docs/images/develop-data-dictionary-field-profiler-2310.png)

> If you're using version 2.0.0 or later of the Looker Data Dictionary extension, the field profiler opens by default to the **Details** tab.

In the **Distribution** section, select **Calculate** to show a preview of a column chart depicting the distribution of the count values for numeric dimensions on a view with a measure that has `type: count`. The **Distribution** section will also display the minimum, maximum, and average values of the numeric dimension series.

Under **Values** , select **Calculate** to show a preview of count values for numeric dimensions on a view with a measure that has `type: count`. Select the **Explore More** button to open the Explore UI with the numeric dimension and count measure pre-selected from the field picker.

Select **Go to LookML** to open the view file from the LookML project that is associated with the selected model in the Looker IDE.

Select the **Explore with Field** button to open the [Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) page with that field automatically selected from the field picker.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
