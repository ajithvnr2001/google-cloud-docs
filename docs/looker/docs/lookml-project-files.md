---
url: https://docs.cloud.google.com/looker/docs/lookml-project-files/
title: Types of files in a LookML project \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:37.584625+00:00
---

# Types of files in a LookML project  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/lookml-project-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Types of files in a LookML project Stay organized with collections  Save and categorize content based on your preferences. 

A LookML [project](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#lookml_project) is a collection of [LookML](https://docs.cloud.google.com/looker/docs/what-is-lookml) files that tell Looker how to connect to your database, how to query your data, and how to control the user interface's behavior. You can access LookML project files either from the **Develop** section in Looker or from the UI, as described on the [Accessing LookML project files](https://docs.cloud.google.com/looker/docs/accessing-project-files) documentation page.

Project files are organized by your Looker developers using [folders in the IDE](https://docs.cloud.google.com/looker/docs/ide-folders).

A LookML project consists of at least one model file and at least one view file, and possibly some of the other types of files described on this page. All project files have extensions, although the extensions are hidden in the IDE list if your project isn't enabled for [folders in the IDE](https://docs.cloud.google.com/looker/docs/ide-folders).

Select the following links to get more information about each of the types of files that can be used in a LookML project:

  * Model files with extension `.model.lkml`
  * View files with extension `.view.lkml`
  * Dashboard files with extension `.dashboard.lookml`
  * Data files with extension `.topojson` or `.geojson` or `.json`
  * Document files with extension `.md`
  * Project manifest files that are always named `manifest.lkml`
  * Manifest lock files with extension `.lkml`
  * Locale strings files with extension `.strings.json`
  * Explore files with extension `.explore.lkml`
  * Data test files with extension `.lkml`
  * Refinements files with extension `.lkml`
  * Other files with any file extension not previously listed

**Note:** If you are not an advanced LookML developer, we recommend that you follow the standard LookML file types at first. There are some LookML elements that must be housed in specific file types, such as [project manifest LookML parameters](https://docs.cloud.google.com/looker/docs/reference/param-project-manifest), which must be in a project's `manifest.lkml` file, and the [`connection`](https://docs.cloud.google.com/looker/docs/reference/param-model-connection) parameter, which must be housed in a `.model.lkml` file. However, LookML is quite flexible and many LookML elements can be housed in any `.lkml` file. Very advanced LookML developers can get creative with LookML files, using the [`include`](https://docs.cloud.google.com/looker/docs/reference/param-model-include) parameter to reference elements from one LookML file in another LookML file, such as by [using refinements to add analysis layers](https://docs.cloud.google.com/looker/docs/lookml-refinements#using_refinements_to_add_analysis), [creating dedicated files for data tests](https://docs.cloud.google.com/looker/docs/lookml-project-files#data_test_files), etc.

Once you have [created a LookML project](https://docs.cloud.google.com/looker/docs/generating-a-model), you can [access the project files](https://docs.cloud.google.com/looker/docs/accessing-project-files) and [add new files and folders to the project](https://docs.cloud.google.com/looker/docs/creating-project-files) using the Looker IDE.

## Model files

A model file specifies a database connection and the set of [Explores](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#explore) that use that connection. A model file also defines the Explores themselves and their relationships to other views. An Explore is a starting point for querying your data. In SQL terms, an Explore is the `FROM` clause of a query. The Explores that you define in the model are seen by your users when they look at the Looker **Explore** menu.

In other words, the model file is where you define which data tables should be used (as included views) and how they should be joined together, if necessary.

Note the following about model files: 

  * Explores are usually defined within a model file. However, sometimes you need a [separate Explore file for a derived table](https://docs.cloud.google.com/looker/docs/creating-ndts#creating_an_explore_file), or to [extend an Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-extends#extending_an_explore_across_models) or to [refine an Explore](https://docs.cloud.google.com/looker/docs/lookml-refinements) across models.
  * A [model file](https://docs.cloud.google.com/looker/docs/lookml-project-files#model_files) must have a unique name across all projects on your instance. If your instance contains two `.model.lkml` files with the same name, it is likely that you will encounter errors, such as model configuration errors on the [**LookML Projects** page](https://docs.cloud.google.com/looker/docs/manage-projects#viewing_the_listing_for_a_project) and rendering errors for LookML dashboard errors, since LookML dashboards use the model name in their URL format (`<hostname>/dashboard/model_name::<dashboard_name>`). You can use the [LookML Validator](https://docs.cloud.google.com/looker/docs/lookml-validation) to verify if model names are duplicated across your instance. However, even if the LookML Validator detects duplicate model names on your instance, you can still push your code to production. Therefore, be sure to fix any duplicate model name errors before you deploy your LookML project to production.



See the [Managing LookML files and folders](https://docs.cloud.google.com/looker/docs/creating-project-files#creating_files) documentation page for instructions for creating LookML project files, including model files.

### Structure and general syntax

Within an Explore's curly braces, `{ }`, you define parameters for the Explore. You can use `join` parameters to join other views to an Explore in a model file.

In the following example, the LookML in a sample model file defines an Explore called `inventory_items`, along with its joined views:
    
    
    connection: "thelook_events"
    
    explore: inventory_items {
      join: products {
        type: left_outer
        sql_on: ${inventory_items.product_id} = ${products.id} ;;
        relationship: many_to_one
      }
    
      join: distribution_centers {
        type: left_outer
        sql_on: ${products.distribution_center_id} = ${distribution_center.id} ;;
        relationship: many_to_one
      }
    }
    
    

This LookML definition causes **Inventory Items** to appear in the **Explore** section of the [Looker navigation](https://docs.cloud.google.com/looker/docs/finding-content) and joins data from the `products` and `distribution_centers` views to the `inventory_items` view.

![The Distribution Centers, Inventory Items, and Products views can be accessed from the field picker for the Inventory Items Explore.](https://docs.cloud.google.com/static/looker/docs/images/model-lookml-ui-example-2214.png)

For more specific information on the LookML structures in a model file, see the [LookML terms and concepts](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#model) documentation page.

Read the [Model parameters](https://docs.cloud.google.com/looker/docs/reference/param-model), [Explore parameters](https://docs.cloud.google.com/looker/docs/reference/param-explore), and [Join parameters](https://docs.cloud.google.com/looker/docs/reference/param-join) documentation pages to learn more about LookML parameters in the model file.

## View files

A view file generally defines a single "view" within Looker. A view corresponds to either a single table in your database or a single [derived table](https://docs.cloud.google.com/looker/docs/derived-tables). The view file specifies a table to query and the fields (dimensions and measures) to include from that table so that users can create queries with those fields in the Looker UI.

See the [Managing LookML files and folders](https://docs.cloud.google.com/looker/docs/creating-project-files#creating_files) documentation page for instructions for creating LookML project files, including view files.

### Structure and general syntax

Within each view's curly braces, `{ }`, are field definitions, which usually correspond to a column in the underlying table or a calculation in Looker. Looker categorizes most of these definitions as either **dimensions** or **measures**.

In the following example of a view file, the `orders.view` file includes definitions for the `id`, `status`, and `user_id` dimensions, the `created` dimension group, and the `count` measure:
    
    
    view: orders {
      sql_table_name: demo_db.orders ;;
      drill_fields: [id]
    
      dimension: id {
        primary_key: yes
        type: number
        sql: ${TABLE}.id ;;
      }
    
      dimension: status {
        type: string
        sql: ${TABLE}.status ;;
      }
    
      dimension: user_id {
        type: number
        # hidden: yes
        sql: ${TABLE}.user_id ;;
      }
    
        dimension_group: created {
        type: time
        timeframes: [
          raw,
          time,
          date,
          week,
          month,
          quarter,
          year
        ]
        sql: ${TABLE}.created_at ;;
      }
    
      measure: count {
        type: count
        drill_fields: [id, users.id, users.first_name, users.last_name, order_items.count]
      }
    }
    

The definition of these fields in the `orders` view exposes the **Created Date** , **ID** , **Status** , **User ID** , and **Count** fields in the field picker for the **Orders** Explore.

![](https://docs.cloud.google.com/static/looker/docs/images/view-structure-ui-example-2308.png)

Users who have access to the **Orders** Explore can query the **Orders** Explore by selecting and filtering on these fields.

In addition to dimensions and measures, you can also create several time-based dimensions at once using [dimension groups](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) or specify a filter for your users with [filter fields](https://docs.cloud.google.com/looker/docs/reference/param-field-filter). Visit the [View parameters](https://docs.cloud.google.com/looker/docs/reference/param-view) documentation page to learn more about LookML parameters in view files, and visit the [Field parameters](https://docs.cloud.google.com/looker/docs/reference/param-field) documentation page for information about the LookML parameters used to define dimensions, measures, dimension groups, and filter fields in LookML.

## Dashboard files

Looker supports two types of dashboards:

  * **User-defined dashboards** , which can be created by non-developer users without using LookML. For details, see the [Creating user-defined dashboards](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards) documentation page.
  * **LookML dashboards** , which are stored as version-controlled files that are associated with the project.



If your project contains LookML dashboards, they will be defined in dedicated dashboard files in the IDE, with the extension `.dashboard.lookml`.

For more information on LookML dashboards, see the [Creating LookML dashboards](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards) documentation page.

## Document files

Looker document files let you write documentation or other notes about your Looker data model using [GitHub-flavored Markdown](https://help.github.com/categories/writing-on-github/). This can be helpful for your users to become acquainted with how your organization uses Looker.

See the [Managing LookML files and folders](https://docs.cloud.google.com/looker/docs/creating-project-files#creating_files) documentation page for instructions for creating LookML project files, including document files.

### Viewing the document outside the IDE

To see a document outside the IDE, which you will need to do to take advantage of the navigation features described on this page, choose the **View Document** option from the **See file actions** menu for the document file:

![](https://docs.cloud.google.com/static/looker/docs/images/dev-doc-view-doc-2500.png)

You can distribute the URL of the resulting page to other users so that they can directly access the document without having to navigate through the Looker **Develop** menu to reach it. 

### Adding a navigation structure to your document

You can add a sidebar to your document files so that users can see the structure of the information and navigate between documents.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-doc-navigation-2300.png)

To add sidebar navigation for a document, create a navigation section starting on the first line of the document. Mark the start and end of your navigation section with three dashes (`---`).

You can use the following parameters in the navigation section:

  * `navigation`
  * `title`
  * `section`
  * `label`



#### `navigation`

You can use `navigation: true` in a document file to add the navigation sidebar to that document. For example, you can add the following code to the top of a Markdown file:
    
    
    ---
    navigation: true
    ---
    

![](https://docs.cloud.google.com/static/looker/docs/images/dev-doc-navigation-file-2206.png)

This code adds to the document a navigation sidebar with links to all the project's documents. If you include only `navigation: true` in a document, the sidebar of that document lists all the project's documents in alphabetical order by filename.

Also, you might find that organizing by alphabetical filename is not ideal, or you may have some documents that you don't want to appear in the navigation:

![The sidebar lists Document Four, Document One, Document Three, and Document Two in alphabetical order, along with a document titled Do Not Display.](https://docs.cloud.google.com/static/looker/docs/images/dev-doc-navigation-no-2220.png)

In this example, you might want to list the documents **Document One** , **Document Two** , **Document Three** , and **Document Four** in numerical order rather than alphabetical order as well as to hide the document **Do Not Display** from the navigation sidebar.

To change the order of the documents in the navigation sidebar, or to show only a subset of your documents in the sidebar, you can use this format:
    
    
    ---
    navigation:
      - document_one
      - document_two
      - document_three
      - document_four
    ---
    

Now the navigation will show only the document files that you want to be shown, and they will appear in a more logical order:

![The sidebar lists the documents in numerical order, and the document Do Not Display is no longer shown.](https://docs.cloud.google.com/static/looker/docs/images/dev-doc-navigation-yes-2300.png)

#### `title`

By default, the sidebar displays the document's heading (if the document begins with a heading), or the document's filename if there is no heading in the file. You can add a `title` parameter at the top of a document to change how the document is displayed in navigation sidebars:
    
    
    ---
    title: New Title for Users
    ---
    

This title will be used as the link text in the navigation sidebars of all documents unless you specify a different `label` in the navigation section of a document.

#### `label`

If you want to change the way a document is listed in the navigation sidebar, you can use the `document` and `label` parameters like this:
    
    
    ---
    navigation:
      - document_one
      - document: document_two
        label: Customized Label for Document Two
      - document_three
      - document_four
    ---
    

**Note:** To use the `label` parameter, you must add the `document:` before the document filename as shown in the preceding example. If you are not using a `label` for a document, do _not_ include `document:` before the filename.

The `label` value defines how a document is shown in the document's sidebar navigation, even if the document to which it refers has its own `title` parameter.

The preceding example looks like this in the document's sidebar:

![The page document_two is listed as Customized Label for Document Two in the sidebar.](https://docs.cloud.google.com/static/looker/docs/images/dev-doc-navigation-label-2300.png)

#### `section`

If you want to break the navigation sidebar into sections, you can use the `section` parameter like this:
    
    
    ---
    navigation:
      - document_one
      - document_two
      - section: My Section Name
      - document_three
      - document_four
    ---
    

In this example, the `section` parameter adds a section break and the text heading **My Section Name** to the sidebar.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-doc-navigation-section-2206.png)

The text heading is not a link itself; it does not refer to any of your document files.

## Data files

Data files are [JSON](https://en.wikipedia.org/wiki/JSON) files with file extension `.json`, `.topojson`, or `.geojson`.

The [`map_layer`](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer) parameter lets you use a JSON file as a custom map that can then be used to plot your data in Looker.

![](https://docs.cloud.google.com/static/looker/docs/images/data-lookml-ui-612-v2.png)

You then use the [map_layer_name](https://docs.cloud.google.com/looker/docs/reference/param-field-map-layer-name) parameter with a dimension so that you can associate a data value (like "Paris") with a geographic region on your custom map.

You can edit a JSON file in the LookML IDE and then select **Save**.

For debugging, you can choose **View Raw** by selecting the **See file actions** menu next to the name of the file to view the file in raw format. If you have the proper extension to view JSON in your browser, you will also have the option to view the file in a **Parsed** format.

See the [Managing LookML files and folders](https://docs.cloud.google.com/looker/docs/creating-project-files#uploading_files) documentation page for instructions on uploading a JSON file to a LookML project.

## Project manifest files

Your project may contain a project manifest file, which is used for the following tasks:

  * Specifying other projects to [import into the current project](https://docs.cloud.google.com/looker/docs/importing-projects)
  * Specifying [model localization settings](https://docs.cloud.google.com/looker/docs/model-localization)
  * Defining [LookML constants](https://docs.cloud.google.com/looker/docs/sql-and-referring-to-lookml#lookml_constants)
  * Adding an [extension](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework#adding_an_extension_to_looker) to your project
  * Adding a [custom visualization](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization) to your project

**Note:** [Model localization](https://docs.cloud.google.com/looker/docs/model-localization) is not compatible with [project import](https://docs.cloud.google.com/looker/docs/importing-projects).

See the [Project manifest parameters](https://docs.cloud.google.com/looker/docs/reference/param-project-manifest) documentation page to see an example manifest file and the possible parameters for manifest files. See the [Managing LookML files and folders](https://docs.cloud.google.com/looker/docs/creating-project-files#creating_files) documentation page for instructions for creating LookML project files, including project manifest files.

Note the following about project manifest files:

  * Each project can only have one manifest file, and it must be named `manifest.lkml` and located at the root level of your project's directory structure and in your Git repository.
  * Looker does not support an empty project manifest file. If your manifest file is empty, [delete the file](https://docs.cloud.google.com/looker/docs/creating-project-files#deleting_files_and_folders).
  * Each project can have only one manifest file. 
  * The project manifest file must be named `manifest.lkml` and be located at the root level of your project's [directory structure](https://docs.cloud.google.com/looker/docs/ide-folders).



## Manifest lock files

Manifest lock files are created automatically when a [remote dependency](https://docs.cloud.google.com/looker/docs/reference/param-manifest-remote-dependency) is added to the project manifest file. Looker uses the manifest lock file to track the version of the remote projects that are specified in the manifest file. The manifest lock file is listed in the file browser panel of the Looker IDE and has the filename `manifest_lock.lkml`.

Looker developers don't need to create or edit a manifest lock file, since lock files are managed automatically by Looker.

For more information, see the [Importing files from other projects](https://docs.cloud.google.com/looker/docs/importing-projects#manifest_lock_file) documentation page.

## Locale strings files

If you are [localizing your data model](https://docs.cloud.google.com/looker/docs/model-localization) you will need to create locale strings files for each locale you want to localize to, including your default locale (for example, often English in the USA).

Locale strings files list key-value pairs for each label and description that you are localizing in your model. The strings file for each locale should provide that locale's translation for each label or description. More information about creating locale strings files appears on the [Localizing your LookML model](https://docs.cloud.google.com/looker/docs/model-localization#creating_locale_strings_files) documentation page.

See the [Managing LookML files and folders](https://docs.cloud.google.com/looker/docs/creating-project-files#creating_files) documentation page for instructions for creating LookML project files, including locale strings files.

## Explore files

An [Explore](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#explore) is a [view](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#view) that users can query. An Explore is the starting point for a query or, in SQL terms, the `FROM` in a SQL statement. See the [Viewing and interacting with Explores in Looker](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores) documentation page for information on how users interact with Explores to query your data.

Explores are usually defined within a model file. However, sometimes you need a separate Explore file [for a derived table](https://docs.cloud.google.com/looker/docs/creating-ndts#using_includes_to_enable_referencing_fields), or to [extend](https://docs.cloud.google.com/looker/docs/reference/param-explore-extends#extending_an_explore_across_models) or [refine](https://docs.cloud.google.com/looker/docs/lookml-refinements) an Explore across models.

See the [Managing LookML files and folders](https://docs.cloud.google.com/looker/docs/creating-project-files#creating_files) documentation page for instructions for creating LookML project files, including Explore files.

## Data test files

Your project may have [data test](https://docs.cloud.google.com/looker/docs/reference/param-model-test) files used for verifying the logic of your LookML model. Data tests can be contained in model files or in view files, but if your developers want to use the same data tests across several different models, it may be helpful to keep the data tests in their own, dedicated file.

See the [Managing LookML files and folders](https://docs.cloud.google.com/looker/docs/creating-project-files#creating_files) documentation page for instructions for creating LookML project files, including data test files.

## Refinements files

Your project may have files used for [LookML refinements](https://docs.cloud.google.com/looker/docs/lookml-refinements). With LookML refinements, you can adapt an existing [view](https://docs.cloud.google.com/looker/docs/reference/param-view-view) or [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) without editing the LookML file that contains it. LookML refinements can be contained in model, view, or Explore files, or in their own, dedicated file.

See the [Managing LookML files and folders](https://docs.cloud.google.com/looker/docs/creating-project-files#creating_files) documentation page for instructions for creating LookML project files, including refinements files.

## Other files

Many LookML elements can be housed in different files in your project, or in their own dedicated files. For example, [data tests](https://docs.cloud.google.com/looker/docs/reference/param-model-test) can be housed in model files, view files, or their own dedicated `.lkml` files.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
