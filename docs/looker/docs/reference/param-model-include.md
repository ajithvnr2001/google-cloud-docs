---
url: https://docs.cloud.google.com/looker/docs/reference/param-model-include/
title: include \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:18.985957+00:00
---

# include  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-model-include/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  include Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    
    include: "/views/airports.view"
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) `include` \- or - [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) `include` \- or - [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `include` |  Default Value None Accepts A string containing a filename or pattern   
---|---  
  
## Definition

The `include` parameter specifies the LookML files that will be available to a model, a view, or an Explore. If you want to use or reference a LookML file within another file, you must add it with the `include` parameter.

You can use the `include` parameter in model files, view files, and Explore files. The `include` parameter can reference different types of LookML files, depending on the context.

In a model file, you can use `include` to reference these file types:

  * View files
  * Dashboard files
  * Explore files
  * Data test files



In a view file, you can use `include` to reference these file types:

  * View files
  * Explore files
  * Data test files



In an Explore file, you can use `include` to reference these file types:

  * View files
  * Explore files



You can also use `include` to bring in files from other projects. See the [Importing files from other projects](https://docs.cloud.google.com/looker/docs/importing-projects#include_files_from_an_imported_project) documentation page for information on including files from another project. 

Note the following when using `include`:

  * You don't need to use `include` for non-LookML file types, such as [documentation files](https://docs.cloud.google.com/looker/docs/other-project-files#document_files) or [data files](https://docs.cloud.google.com/looker/docs/other-project-files#data_files).
  * Including files is all-or-nothing, so all the includ _ed_ file's information is added to the includ _ing_ file.
  * You can use multiple `include` parameters in a file.
  * You can use the `*` wildcard character to indicate files with strategic naming conventions or with the same extension. For example, you can use `"*base.dashboard"` to match and include both `"database.dashboard"` and `"crunchbase.dashboard"`. You can use `"*.dashboard"` to indicate all files with the extension `.dashboard`.
  * You can use the `*` wildcard character to include all files in a directory. For example, you can include all view files in the `views/users/` directory by specifying `include: "/views/users/*.view"`. See the documentation page on [IDE folders](https://docs.cloud.google.com/looker/docs/ide-folders#using_include_with_ide_folders) for more information on using wildcards with IDE folders.

**Tip:** When you're using wildcards, you can check which files are included by hovering over the information icon by the line number in the file or by selecting the `include` statement and looking in the quick help.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-include-tips-2206.png)

**Tip:** You can copy the path for a file by selecting **Copy File Path** from the file's three-dot **File options** menu in the file browser section of the Looker IDE.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-copy-path-name-2208.png)

## Using `include` in a model file

You can use the `include` parameter in a model file to include views and dashboards or Explores.

### Including views and dashboards in a model

Use the `include` parameter in a model file to specify the dashboard and view files that will be available to that model. If you want to use or reference a LookML file within a model, you must add it with the `include` parameter.

In the `include` parameter, use the extension `.view` for view files and the extension `.dashboard` for dashboards. You can leave out the `.lkml` and `.lookml` part of these extensions.

You can use the `*` wildcard character to indicate files with strategic naming conventions or with the same extension. You can also use the `*` wildcard in combination with directory paths to specify multiple files, as described in the [Wildcard examples](https://docs.cloud.google.com/looker/docs/reference/param-model-include#wildcard_examples) section of the `include` parameter page.

For example, you could use these `include` parameters in a model file:
    
    
    include: "/**/*.dashboard"
    include: "/*/*base.view.lkml"
    include: "//e_commerce/views/*.view.lkml"
    

These parameters would include the following files:

  * All dashboard files in any directory in your project
  * Any view files that end with `base.view.lkml` in any immediate child directory of the project, such as `/views/database.view.lkml` or `/public/crunchbase.view.lkml`
  * All view files in the `/views/` directory of the [imported project](https://docs.cloud.google.com/looker/docs/importing-projects) named `e_commerce`



If your project has a large number of view files or if your project uses persistent derived tables (PDTs), you should avoid including all view files in your model. Instead, include individual view files like this. Here's an example of including individual view files and all dashboards in a project:
    
    
    include: "/views/order.view"
    include: "/views/user.view"
    include: "/**/*.dashboard"
    

### Including models in a model

You cannot include a model file from another project. Instead, to reuse, [refine](https://docs.cloud.google.com/looker/docs/lookml-refinements), or [extend](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends) Explores across projects, in the imported project you can [create a separate Explore file](https://docs.cloud.google.com/looker/docs/other-project-files#creating_an_explore_file), then include that Explore file in other projects. See Including Explores in a Model for more information.

### Including Explores in a model

**Note:** Explore files will listen to the connection of the model that they are included in. Consider this fact when you include Explore files in models that are configured with a connection that is different from the Explore file's parent model. If the schema for the including model's connection differs from the schema for the parent model's connection, it can cause query errors.

Explores are usually defined within a model file. However, sometimes you need a separate Explore file [for a derived table](https://docs.cloud.google.com/looker/docs/creating-ndts#using_includes_to_enable_referencing_fields), or to [extend](https://docs.cloud.google.com/looker/docs/reference/param-explore-extends#extending_an_explore_across_models) or [refine](https://docs.cloud.google.com/looker/docs/lookml-refinements) an Explore across models.

If you do have a separate Explore file, you need to use the `include` parameter in the model file to include it. In the `include` parameter, use the extension `.explore.lkml` for Explore files.

The following example is a model file that has two Explores:

  * The `aircraft_new` Explore, which is defined in its own file called `aircraft_new.explore.lkml` in the `explores` folder. Because that Explore is defined in its own file, you must specify the Explore file's path in an `include` parameter.
  * The `accidents` Explore, which is defined within the model file. Because it is defined in the model file itself, you don't need to use an `include` parameter for it in the model. However, you do need an `include` for the view on which the `accidents` Explore is based.


    
    
    connection: "faa"
    
    include: "/explores/aircraft_new.explore.lkml"
    include: "/views/accidents.view"
    
    explore: accidents {
      view_name: accidents
      from: accidents
    }
    

### Including data tests in a model

[Data tests](https://docs.cloud.google.com/looker/docs/reference/param-model-test) can be defined directly in a model file or a view file. However, you can also create a separate [data test file](https://docs.cloud.google.com/looker/docs/other-project-files#data_test_files) if you want to reuse your data tests in multiple places in your project.

If you do have a separate data test file, you need to use the `include` parameter in your model file or view file so that you can run the data tests. In the `include` parameter, use the extension `.lkml` for data test files.

For example, here is an excerpt from a model file that includes a data test file:
    
    
    connection: "faa"
    
    include: "/explores/aircraft_new.explore.lkml"
    include: "/views/accidents.view"
    include: "/tests/data_tests.lkml"
    
    . . .
    
    

Once you include the data test file in a model file, you can [run the data test](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#running_data_tests) to verify that your data test works properly and to see if your model's logic passes the test.

You can also include the data test file in a view file, as described on theIncluding data tests in a view section on this page.

## Using `include` in a view file

For the most part, you don't need to use `include` in a view file. However, there are some cases in which you do want to include files in your view file:

  * If you are extending or refining a view
  * If you have an Explore file for a derived table



### Including views in a view (to extend or refine)

You can also include a view file in another view file to [extend](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends) or to [refine](https://docs.cloud.google.com/looker/docs/lookml-refinements) the included view.

For example, here is the `marketing_order_fields` view file that includes the `basic_order_fields` view file and then extends it:
    
    
    include: "/views/basic_order_fields.view"
    view: marketing_order_fields {
      extends: [basic_order_fields]  # The file that contains the basic_order_fields
    }                                # view should be included
    

### Including Explores in a view

**Note:** Explore files will listen to the connection of the model that they are included in. Consider this fact when you include Explore files in models that are configured with a connection that is different from the Explore file's parent model. If the schema for the including model's connection differs from the schema for the parent model's connection, it can cause query errors.

In most cases, you don't need to include an Explore in a view. However, [native derived tables](https://docs.cloud.google.com/looker/docs/creating-ndts) are a special case because they are defined in their own view file that has an [`explore_source`](https://docs.cloud.google.com/looker/docs/reference/param-view-explore-source) parameter. You use the `explore_source` parameter to specify an Explore and define the desired columns and other desired characteristics for the native derived table. Explores are usually defined within a model file, but in the case of native derived tables it may be cleaner to [create a separate file for the Explore](https://docs.cloud.google.com/looker/docs/creating-ndts#creating_an_explore_file) using the `.explore.lkml` file extension. If you create a separate Explore file, you must include the Explore file in the native derived table view file.

Here is an example of using `include` in a native derived table view file to point to an Explore file:
    
    
    include: "/explores/order_items.explore.lkml"
    
    view: user_order_facts {
      derived_table: {
        explore_source: order_items {
          column: user_id {field: order_items.user_id}
          column: lifetime_number_of_orders {field: order_items.order_count}
          column: lifetime_customer_value {field: order_items.total_revenue}
          derived_column: average_customer_order {
            sql:  lifetime_customer_value / lifetime_number_of_orders ;;
          }
        }
      }
      dimension: user_id {hidden: yes}
      dimension: lifetime_number_of_orders {type: number}
      dimension: lifetime_customer_value {type: number}
      dimension: average_customer_order {type: number}
    }
    
    

See our documentation on [using `include` statements to enable referencing fields](https://docs.cloud.google.com/looker/docs/creating-ndts#using_includes_to_enable_referencing_fields) for more information on Explore files for native derived tables.

### Including data tests in a view

[Data tests](https://docs.cloud.google.com/looker/docs/reference/param-model-test) can be defined directly in a model file or a view file. However, you can also create a separate [data test file](https://docs.cloud.google.com/looker/docs/other-project-files#data_test_files) if you want to reuse your data tests in multiple places in your project.

If you do have a separate data test file, you need to use the `include` parameter in your model file or view file so that you can run the data tests. In the `include` parameter, use the extension `.lkml` for data test files.

For example, here is an excerpt from a view file that includes a data test file:
    
    
    include: "/tests/data_tests.lkml"
    
    view: orders {
      sql_table_name: looker.orders ;;
    
      dimension: id {
        primary_key: yes
        type: number
        sql: ${TABLE}.id ;;
      }
    
    . . .
    
    

Once you include the data test file in a view file, you can [run the data test](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#running_data_tests) to verify that your data test works properly and to see if your view's logic passes the test.

You can also include the data test file in a model file, as described on the Including data tests in a model section on this page.

## Using `include` in an Explore file

Explores are usually defined within a model file. However, sometimes you need a separate Explore file [for a derived table](https://docs.cloud.google.com/looker/docs/creating-ndts#using_includes_to_enable_referencing_fields), or to [extend](https://docs.cloud.google.com/looker/docs/reference/param-explore-extends#extending_an_explore_across_models) or [refine](https://docs.cloud.google.com/looker/docs/lookml-refinements) an Explore across models.

If you do have a separate Explore file, you can use the `include` parameter to include views or other Explores.

### Including views in an Explore

If you have a separate Explore file, you need to include any views that are used by the Explore. Use the file extension `.view` for view files. You can leave out the `.lkml` part of the file extension. Here is an example Explore file that includes the two views it's using:
    
    
    include: "/views/aircraft.view"
    include: "/views/aircraft_types.view"
    
    explore: aircraft {
      join: aircraft_types {
        type: left_outer
        sql_on: ${aircraft.aircraft_type_id} = ${aircraft_types.aircraft_type_id} ;;
        relationship: many_to_one
      }
    }
    
    

### Including Explores in an Explore

**Note:** Explore files will listen to the connection of the model that they are included in. Consider this fact when you include Explore files in models that are configured with a connection that is different from the Explore file's parent model. If the schema for the including model's connection differs from the schema for the parent model's connection, it can cause query errors.

You can include one Explore file in another Explore file, such as when you are [extending](https://docs.cloud.google.com/looker/docs/reference/param-explore-extends#extending_an_explore_across_models) or [refining](https://docs.cloud.google.com/looker/docs/lookml-refinements) an Explore. Use the `include` parameter and add the file extension `.explore.lkml`.

Here is an example Explore file that includes another Explore file and then extends the Explore:
    
    
    include: "/explores/base.explore.lkml"
    
    explore: aircraft_information {
      extends: [aircraft]
    

## Using `include` with IDE folders

When you [organize your LookML project files into folders](https://docs.cloud.google.com/looker/docs/ide-folders#organizing_an_existing_project_with_ide_folders), you need to provide the paths for files within the `include` statement.

**Note:** When you use `include`, keep in mind that LookML is case sensitive. When you specify a file's path, you must match the case of the file and of the folders in the path. Generally, it's a good idea to stick with lowercase when naming LookML objects and folders.

You can use absolute or relative paths in the `include` statement (see the Path syntax section on this page for examples), and you can use the wildcards `*` and `**` to include multiple files at once (see the Wildcard examples section on this page for examples).

For example, suppose you have this directory structure in your project, with the following top-level contents of the `views` folder:

  * The `orders` folder, which contains the view files `order_facts` and `order_items`
  * The `users` folder, which contains the view files `user_with_age_extension`, `users`, and `users_extended`
  * The individual view files `distribution_centers`, `events`, `inventory_items`, and `products`



![Sample directory structure with folders for Explores, models, and views.](https://docs.cloud.google.com/static/looker/docs/images/dev-include-example-2104.png)

The following statements will include the `products` view, the `order_facts` view, and all views in the `/views/users/` directory:
    
    
    include: "/views/products.view"
    include: "/views/orders/order_facts.view"
    include: "/views/users/*.view"
    

When you change a file's path, be sure to update any `include` statements in your project to match the file's new path. You may see LookML validation warnings on your old `include` statements if they no longer refer to existing files or file paths. In addition, you may see LookML validation errors for referenced objects that can no longer be found because their file paths have changed.

### Path syntax

Here are some example syntaxes you can use for including files:

Syntax | Description  
---|---  
`PATH` | Relative path starting from current file's location.  
`./PATH` | Relative path starting from current file's location. This example points to the same file as the previous example: `PATH`.  
`../PATH` | Relative path starting from current file's parent directory.  
`/PATH` | Absolute path starting from current project's root.  
`//PROJECT_NAME/PATH` | Absolute path starting from the root of an [imported project](https://docs.cloud.google.com/looker/docs/importing-projects) called `PROJECT_NAME`.  
  
## Using wildcards

For projects where only a few files need to be managed, you can list each file in its own `include` parameter, like this:
    
    
    include: "/dashboards/user_info.dashboard"
    include: "/views/users.view"
    

For projects with many files to include, you can reduce the number of `include` parameters that you need to write by using [wildcards](https://docs.cloud.google.com/looker/docs/reference/param-model-include#wildcard_examples) to include several files at once:

  * Use wildcards with IDE folders to include files in a specific directory of your project.
  * Use wildcards with file extensions to include files of a specific file type.
  * Use wildcards with strategic filenames to include files with specific prefixes or suffixes in their filenames.



Using wildcards may be especially helpful during development when you need to create a temporary fix for LookML validation warnings, especially when [organizing an existing project into IDE folders](https://docs.cloud.google.com/looker/docs/ide-folders#organizing_an_existing_project_with_ide_folders). But take the following into consideration when using wildcards in your `include` statements:

  * Looker does not recommend the use of wildcards to include all view files in a project, since including all view files can affect the performance of LookML validation and can clutter your database schema.
  * Looker does not support the use of wildcards to include all files in a project if the project has multiple model files, since model files cannot be included in other model files.



### Using wildcards with IDE folders

You can use wildcards in combination with [IDE folders](https://docs.cloud.google.com/looker/docs/ide-folders) to include files in a specific directory in your LookML project.

For example, this `include` statement references all the files in the `/explores/` directory of a LookML project:
    
    
    include: "/explores/*"
    

### Using wildcards for specific file types

You can use wildcards to reference all files of a specific type. For example, this `include` statement references all Explore files in a LookML project:
    
    
    include: "/**/*.explore.lkml"
    

See the [Types of files in a LookML project](https://docs.cloud.google.com/looker/docs/lookml-project-files#project_file_types) section of the [Understanding LookML project files](https://docs.cloud.google.com/looker/docs/lookml-project-files) documentation page for a list of the types of LookML files and their file extensions.

**Note:** Looker does not recommend the use of wildcards to include all view files in a project, since including all view files can affect the performance of LookML validation and can clutter your database schema.

### Using wildcards with strategic naming patterns

You can also use wildcards with strategic file naming to further optimize your `include` statements. For example, instead of naming files like this:
    
    
    /views/apple.view
    /views/banana.view
    /views/cherry.view
    /views/orange.view
    /views/celery.view
    

You can add a strategic prefix or suffix to your filenames, like this:
    
    
    /views/apple.fruit.view
    /views/banana.fruit.view
    /views/cherry.fruit.view
    /views/orange.fruit.view
    /views/celery.vegetable.view
    

Then use wildcards to reference only the `.fruit` suffix by using this `include`:
    
    
    include: "/views/*.fruit.view"
    

### Wildcard examples

**Note:** If you are using [LookML refinements](https://docs.cloud.google.com/looker/docs/lookml-refinements), do not use wildcards in your includes. LookML refinements leverage the order of includes, and using wildcards in your includes does not allow you to control the order in which each file is included. See the [LookML refinements](https://docs.cloud.google.com/looker/docs/lookml-refinements) documentation page for more information about refinements.

Here are some examples using wildcards (note that you can replace `PATH` with the path syntaxes in the previous table):

Syntax | Description  
---|---  
`PATH/*.view` | Wildcard matching files ending with `.view` at `PATH`.  
`PATH/*.view.lkml` | Wildcard matching files ending with `.view.lkml` at `PATH`. Because view files have the extension `.view.lkml`, this example specifies the same file as the previous example, `PATH/*.view`. The `.lkml` part is not displayed in the IDE, nor is the `.lkml` part required for `include` statements. However, you can use wildcards to leverage this common part of the file extension. See the [LookML project files](https://docs.cloud.google.com/looker/docs/lookml-project-files#project_file_extensions) documentation page for a list of project file extensions.  
`PATH/*.lkml` | Wildcard matching files ending with `.lkml` at `PATH`. Note that several file types share `.lkml` as the final part of the file extension, such as `.view.lkml` and `.model.lkml`. The `.lkml` part is not displayed in the IDE, nor is the `.lkml` part required for `include` statements. However, you can use wildcards to leverage this common part of the file extension. See the [LookML project files](https://docs.cloud.google.com/looker/docs/lookml-project-files#project_file_extensions) documentation page for a list of project file extensions.  
`PATH/myfile.*` | Wildcard matching files called `myfile` with any extension type at `PATH`.  
`PATH/myfile.*.lkml` | Wildcard matching files called myfile with any `.lkml` extension type at `PATH`.  
`PATH/my*file.view` | Wildcard matching files starting with `my` and ending with `file.view` at `PATH`.  
`PATH/my*fi*le.view` | Wildcards matching files starting with `my`, followed by some characters, then `fi`, some additional characters, and ending with `le.view` at `PATH`.  
`PATH/*/myfile.lkml` | Folder name wildcard (match only a single level of nesting). Matches all `myfile.lkml` files in any direct child directories of `PATH`.  
`PATH/**/my_file.view` | Recursive wildcard matching (match any amount of nesting) for all files called `my_file.view.lkml` at `PATH` and all subdirectories.  
`PATH/**/*.view` | Recursive wildcard matching all files ending with `.view.lkml` at `PATH`'s subdirectories.  
`PATH/**/my_folder/myfile.view` | Recursive wildcard matching the subpath `/my_folder/myfile.view` at any depth under `PATH`.  
  
## Examples

See the previous sections for examples of using `include` in model files, view files, and Explore files.

## Things to consider

### Including all view files can affect performance of LookML validation

If your project has a large number of view files and you include them all in your model file, this may affect the performance of the [LookML Validator](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_your_changes). Since the LookML Validator checks all the view files included in the model, you should include only the needed view files in the model file's `include` parameter.

Consider using strategic naming conventions for view files to enable easy inclusion of groups of views within a model (see the example in Using wildcards with strategic naming patterns on this page). Or, you can use [IDE folders](https://docs.cloud.google.com/looker/docs/ide-folders) to organize your views into folders. Then you can use the `*` wildcard to include all views in a single folder, instead of including all views in your project. See the section on using `include` with IDE folders for information.

### Including all view files can clutter your database schema

For projects that use [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table), you can include the PDT's view file in your model file. However, each model file that includes the PDT's view file will create a copy of the PDT in the scratch schema on your database. If you have multiple model files and you include all view files in your model files, you may add unnecessary clutter to your database scratch schema. For this reason, be sure that you include a PDT's view file only in the model files where the PDT is needed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
