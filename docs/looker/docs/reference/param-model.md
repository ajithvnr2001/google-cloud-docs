---
url: https://docs.cloud.google.com/looker/docs/reference/param-model/
title: Model parameters \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:18.305445+00:00
---

# Model parameters  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  Model parameters Stay organized with collections  Save and categorize content based on your preferences. 

A [model file](https://docs.cloud.google.com/looker/docs/model-and-view-files#model_files) specifies a database connection, defines the set of [Explores](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#explore) that use that connection, and defines the Explores' relationships to other views. Unlike other LookML elements, a model is not declared with a specific "model" parameter. Instead, a LookML developer defines a model by creating a LookML project file that has the `.model.lkml` file extension. The model name is taken from the filename.

A model name must be unique across all projects on your instance. If your instance contains two `.model.lkml` files with the same name, it is likely that you will encounter errors, such as model configuration errors on the [**LookML Projects** page](https://docs.cloud.google.com/looker/docs/manage-projects#viewing_the_listing_for_a_project) and rendering errors for LookML dashboard errors, since LookML dashboards use the model name in their URL format (`<hostname>/dashboard/model_name::<dashboard_name>`).

You can use the [LookML Validator](https://docs.cloud.google.com/looker/docs/lookml-validation) to verify if model names are duplicated across your instance. However, even if the LookML Validator detects duplicate model names on your instance, you can still push your code to production. Therefore, be sure to fix any duplicate model name errors before you deploy your LookML project to production.

A model file typically contains any [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore) declarations, along with a number of model-level settings.

This page links to the model-level LookML parameters. They are typically written at the top of the model file and shouldn't be nested within other parameters.

## Example usage

Hold the pointer over a parameter name to see a quick description. Click a parameter to visit its reference page. When a parameter can be set to one of several specific options, the default value is listed first.
    
    
    ## STRUCTURAL PARAMETERS
    [include](https://docs.cloud.google.com/looker/docs/reference/param-model-include "Adds files to a model"):"filename_or_pattern"
    ## Possibly more include declarations
    
    [explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore "Exposes a view in the Explore menu"): explore_name {
      # Desired explore parameters (described on [Explore Parameters](https://docs.cloud.google.com/looker/docs/reference/param-explore) page)
    }
    ## Possibly more explore declarations
    
    [access_grant](https://docs.cloud.google.com/looker/docs/reference/param-model-access-grant "Defines an access grant that limits access to only users with specified user attributes"): access_grant_name{
      [user_attribute](https://docs.cloud.google.com/looker/docs/reference/param-model-access-grant "Specifies the user attribute used to grant access"): user_attribute_name
      [allowed_values](https://docs.cloud.google.com/looker/docs/reference/param-model-access-grant "Specifies the user attribute values that are required for access"): ["value_1", "value_2", ...]
    }
    ## Possibly more access_grant declarations
    
    [test](https://docs.cloud.google.com/looker/docs/reference/param-model-test "Creates a data test to verify your model's logic"): test_name{
      [explore_source](https://docs.cloud.google.com/looker/docs/reference/param-model-test "Specifies the source Explore for the test query"): explore_name {
        # Desired subparameters (described on [test](https://docs.cloud.google.com/looker/docs/reference/param-model-test) page)
      }
      [assert](https://docs.cloud.google.com/looker/docs/reference/param-model-test "Defines a yes/no Looker expression that must result in yes for the test to pass"): assert_statement {
        [expression](https://docs.cloud.google.com/looker/docs/reference/param-model-test "Specifies the yes/no Looker expression to be executed to test your model's logic"):Looker expression ;;
      }
      # Possibly more assert declarations
    }
    ## Possibly more test declarations
    
    ## DISPLAY PARAMETERS
    [label](https://docs.cloud.google.com/looker/docs/reference/param-model-label "Changes the way a model appears in the Explore menu"): "desired label"
    
    ## FILTER PARAMETERS
    [case_sensitive](https://docs.cloud.google.com/looker/docs/reference/param-model-case-sensitive "Specifies whether filters are case-sensitive for a model"): yes | no
    
    ## QUERY PARAMETERS
    [connection](https://docs.cloud.google.com/looker/docs/reference/param-model-connection "Change the database connection for a model"): "connection_name"
    [datagroup](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup "Creates a datagroup caching policy for the model"): datagroup_name{
      [label](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup "Specifies an optional label for the datagroup"): "desired label"
      [description](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup "Adds an optional description for a datagroup that can be used to explain the datagroup's purpose and mechanism"): "desired description"
      [max_cache_age](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup#max_cache_age "Specifies the maximum time period for the cached results to be used"): "N (minutes | hours | days)"
      [sql_trigger](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup#sql_trigger "Specifies the condition that invalidates the cached results"): SQL query ;;
    }
    ## Possibly more datagroup declarations
    [fiscal_month_offset](https://docs.cloud.google.com/looker/docs/reference/param-model-fiscal-month-offset "Specifies the month your fiscal year begins \(if it differs from calendar year\)"): N
    [persist_for](https://docs.cloud.google.com/looker/docs/reference/param-model-persist-for "Changes the cache settings for a model"): "N (seconds | minutes | hours)"
    [persist_with](https://docs.cloud.google.com/looker/docs/reference/param-model-persist-with "Specifies the datagroup to use for the model's caching policy"): datagroup_name
    [week_start_day](https://docs.cloud.google.com/looker/docs/reference/param-model-week-start-day "Specifies the day of week that week-related dimensions should start on"): monday | tuesday | wednesday | thursday | friday | saturday | sunday
    
    ## VISUALIZATION AND FORMATTING PARAMETERS
    [map_layer](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer "Creates custom maps to be used with map_layer_name"): map_name{
      [extents_json_url](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer "The URL to a JSON file that defines the geographic extents of each region available in the map layer "): "URL to JSON extents file"
      [feature_key](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer "Specifies the name of the TopoJSON object that the map layer references"): "Name of TopoJSON object"
      [file](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer "Specifies the name and location of the JSON map file"): "TopoJSON or GeoJSON filename" # or use the url subparameter
      [format](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer "Specifies the data format of the region information"): topojson | vector_tile_region
      [label](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer "Specifies what to call the map in the chart configuration UI"): "desired label"
      [max_zoom_level](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer "Specifies the maximum zoom level for zooming in the map layer"): number indicating max zoom
      [min_zoom_level](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer "Specifies the minimum zoom level for zooming in the map layer"): number indicating min zoom
      [projection](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer "Specifies the preferred geographic projection of the map layer"): Preferred geographic projection
      [property_key](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer "Specifies the property from the TopoJSON data to plot against"): "TopoJSON property"
      [property_label_key](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer "Specifies the property from the TopoJSON data to use to label the region"): "Label for TopoJSON property"
      [url](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer "Specifies the URL that is the location of the JSON map"): "URL that contains map file" # or use the file subparameter
    }
    ## Possibly more map layer declarations
    
    [named_value_format](https://docs.cloud.google.com/looker/docs/reference/param-model-named-value-format "Creates a custom value format to be used with value_format_name"): desired_name {
      [value_format](https://docs.cloud.google.com/looker/docs/reference/param-model-named-value-format "See named_value_format page for more detail"): "excel formatting string"
      [strict_value_format](https://docs.cloud.google.com/looker/docs/reference/param-model-named-value-format "See named_value_format page for more detail"): yes | no
     }
    ## Possibly more named value format declarations
    

## Parameter definitions

Parameter Name | Description  
---|---  
Structural Parameters  
[`access_grant`](https://docs.cloud.google.com/looker/docs/reference/param-model-access-grant) | Creates an access grant that limits access of LookML structures to only those users who are assigned an approved [user attribute](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) value. This parameter has the `user_attribute` and `allowed_values` subparameters.  
[`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) | Exposes a view in the Explore menu. For more information about Explores and their parameters, see the [Explore Parameter Reference](https://docs.cloud.google.com/looker/docs/reference/param-explore) page.  
[`include`](https://docs.cloud.google.com/looker/docs/reference/param-model-include) | Adds files to a model  
[`test`](https://docs.cloud.google.com/looker/docs/reference/param-model-test) | Creates a data test to verify your model's logic. The project settings include an option to [require data tests](https://docs.cloud.google.com/looker/docs/git-options#require-data-tests). When this is enabled for a project, developers on the project must run data tests before deploying their changes to production. This parameter has the `explore_source` and `assert` subparameters.  
Display Parameters  
[`label` (for model)](https://docs.cloud.google.com/looker/docs/reference/param-model-label) | Changes the way a model appears in the Explore menu  
Filter Parameters  
[`case_sensitive` (for model)](https://docs.cloud.google.com/looker/docs/reference/param-model-case-sensitive) | Specifies whether filters are case-sensitive for a model  
Query Parameters  
[`connection`](https://docs.cloud.google.com/looker/docs/reference/param-model-connection) | Changes the database connection for a model  
[`datagroup`](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup) | Creates a datagroup-caching policy for a model. This parameter has the `label`, `description`, `max_cache_age`, and `sql_trigger` subparameters.  
[`fiscal_month_offset`](https://docs.cloud.google.com/looker/docs/reference/param-model-fiscal-month-offset) | Specifies the month your fiscal year begins (if it differs from the calendar year)  
[`persist_for` (for model)](https://docs.cloud.google.com/looker/docs/reference/param-model-persist-for) | Changes the cache settings for a model  
[`persist_with` (for model)](https://docs.cloud.google.com/looker/docs/reference/param-model-persist-with) | Specifies the datagroup to use for the model's caching policy  
[`week_start_day`](https://docs.cloud.google.com/looker/docs/reference/param-model-week-start-day) | Specifies the day of the week on which week-related dimensions should start  
Visualization and Formatting Parameters  
[`map_layer` (for model)](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer) | Creates custom maps to be used with [`map_layer_name`](https://docs.cloud.google.com/looker/docs/reference/param-field-map-layer-name)  
[`named_value_format`](https://docs.cloud.google.com/looker/docs/reference/param-model-named-value-format) | Creates a custom value format to be used with [`value_format_name`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format-name). This parameter has the `value_format` and `strict_value_format` subparameters.  
Parameters to Avoid  
[`scoping`](https://docs.cloud.google.com/looker/docs/reference/param-model-scoping) |  Removed 3.52  No longer required  
[`template`](https://docs.cloud.google.com/looker/docs/reference/param-model-template) |  Removed 3.30  No longer required  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
