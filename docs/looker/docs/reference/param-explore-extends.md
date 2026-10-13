---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-extends/
title: extends (for Explores) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:21.839515+00:00
---

# extends (for Explores)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-extends/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  extends (for Explores) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `extends` parameter that is part of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore).
> 
> `extends` can also be used as part of a view, as described on the [`extends` (for views)](https://docs.cloud.google.com/looker/docs/reference/param-view-extends) parameter documentation page.
> 
> `extends` can also be used as part of a LookML dashboard, as described on the [Dashboard parameters](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#extends) documentation page.

## Usage
    
    
    
    explore: explore_name {
      extends: [explore_name, explore_name, ...]
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `extends` |  Default Value None Accepts Square brackets containing a comma-separated list of Explore names  
---|---  
  
## Definition

The `extends` parameter lets you build upon the content and settings from another Explore, using the other Explore as a starting point. If there are any conflicts, the extending Explore will use its own settings, overriding the settings of the Explore being extended. See the [Reusing code with `extends`](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends) documentation page for the details of how Looker does this.

> **Check out LookML refinements.**
> 
> Extending a view or an Explore is ideal for scenarios where you want to have multiple versions of the view or Explore. But if your goal is simply to modify a view or an Explore without editing the LookML file that contains it, you may want to use a refinement instead. You can also use an [`extends` parameter inside a refinement](https://docs.cloud.google.com/looker/docs/lookml-refinements#refinements_can_contain_extends). See the [LookML refinements](https://docs.cloud.google.com/looker/docs/lookml-refinements) documentation page for more information and use cases. 

When you're extending an Explore, it's important to have the [`view_name`](https://docs.cloud.google.com/looker/docs/reference/param-explore-view-name) parameter in the Explore that is going to be extended. The `view_name` parameter defines the view on which an Explore is based. Its default value is the name of the Explore. If the base Explore doesn't have a `view_name` specified, it defaults to the Explore name. But this doesn't work for other Explores that are extending the base Explore, so we would get the "unknown view" error. In order for Looker to use the correct view file, we need to specify it using the `view_name` parameter. And since this will be needed in any extended version of the Explore, the best practice is to add it to the base Explore so it is consistently referenced any time the Explore is extended.

If your base Explore doesn't already have a [`view_name`](https://docs.cloud.google.com/looker/docs/reference/param-explore-view-name) parameter, you can just add the `view_name` parameter and specify the same value as your Explore's name.

You may also want to use the [`view_label`](https://docs.cloud.google.com/looker/docs/reference/param-explore-view-label) parameter in your base and extending Explores. The `view_label` parameter determines the label under which the view's fields are grouped in the field picker (see the [`view_label` (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-view-label#definition) parameter documentation page for an example). If you don't specify a `view_label` for your base and extending Explores, they both will use the Explore name from the base Explore.

## Example

Here's an example Explore that's defined in our model file:
    
    
    explore: orders {
      view_name: orders
      view_label: "Orders"
      # The normal contents of the Explore follow
    }
    

And here we add a new Explore that extends the `orders` Explore that we defined previously:
    
    
    explore: name_of_the_new_explore {
      extends: [orders]
      view_label: "Order Information"
      # The additional things you want to add or change
      # in the new Explore
    }
    

If you are extending an Explore that is based on an extended view, you will also need to use the [`from`](https://docs.cloud.google.com/looker/docs/reference/param-explore-from) parameter. Add `from` to the extend _ing_ Explore and assign it the name of the extend _ed_ view.
    
    
    explore: new_explore {
      extends: [orders]
      from: extended_orders_view
      #The normal contents of the Explore follow
    }
    

## Using `extends` to limit fields for different users

A very handy use case of extending an Explore is to display only a subset of an Explore's fields to certain users. For example, suppose you have a `products` Explore with all the available fields from the joined tables:
    
    
    explore: products {
      view_name: products
      from: products
      join: inventory_items {
        type: left_outer
        sql_on: ${products.id}=${inventory_items.product_id} ;;
        relationship: many_to_one
      }
    
      join: order_items {
        type: left_outer
        sql_on: ${order_items.inventory_item_id}=${inventory_items.id} ;;
        relationship: one_to_one
      }
    }
    

If you have a team who only needs to see product category and returns, you can extend the `products` Explore and use the [`fields`](https://docs.cloud.google.com/looker/docs/reference/param-explore-fields) parameter to specify that only the product category and returns fields are to be included:
    
    
    explore: products_extended {
      extends: [products]
      fields: [products.category,order_items.returned_date]
    }
    
    

The `products_extended` Explore will display only these two fields: `products.category` and `order_items.returned_date`.

## Extending an Explore across models

Explores are usually defined within a model file. If you want to extend an Explore, you can just define the extending Explore in the same model file, as in the preceding examples.

However, if you want to extend an Explore across multiple models, you must [create a separate Explore file](https://docs.cloud.google.com/looker/docs/other-project-files#creating_an_explore_file) to use as a base file. Once you have defined the base Explore in its own file, you can [include the Explore file in your model file](https://docs.cloud.google.com/looker/docs/reference/param-model-include#including_explores_in_a_model) and extend the Explore in your model file.

Since you can [include an Explore file in another Explore file](https://docs.cloud.google.com/looker/docs/reference/param-model-include#including_explores_in_an_explore), you can also share your base Explore file across multiple other Explore files, if need be.

> Explore files will listen to the connection of the model in which they are [included](https://docs.cloud.google.com/looker/docs/reference/param-model-include#including_explores_in_a_model). Keep this in mind when you include Explore files in models that are configured with a connection that is different from the Explore file's parent model. If the schema for the including model's connection differs from the schema for the parent model's connection, it can cause query errors.

## Using metadata to see extensions for an object

You can click on an `explore` or a `view` parameter in the Looker IDE and use the metadata panel to see any extensions on the object, or to see what object it extends. See the [Metadata for LookML objects](https://docs.cloud.google.com/looker/docs/lookml-metadata) documentation page for information.

## Things to consider

### Some parameters are additive

In many cases, if the extending object contains the same parameter as the object that is being extended, the [extending object's values will override the parameter values of the extended object](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends#step_3:_resolve_conflicts). But extensions can be _additive_ for some parameters, meaning that the values from the extending object are used in conjunction with the values from the extended object.

The following Explore parameters are _additive_ :

  * [`access_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter)
  * [`aggregate_table`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table)
  * `extends` (you can [chain together multiple `extends`](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends#chaining_together_multiple_extends))
  * [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join)
  * [`query`](https://docs.cloud.google.com/looker/docs/reference/param-explore-query)



In the following example, the `aircraft_base` Explore uses the `join` parameter to join the `aircraft` view with the `aircraft_types` view:
    
    
    explore: aircraft_base {
      view_name: aircraft
      label: "Aircraft"
    
      join: aircraft_types {
        type: left_outer
        sql_on: ${aircraft.aircraft_type_id} = ${aircraft_types.aircraft_type_id} ;;
        relationship: many_to_one
      }
    }
    
    

And the `aircraft_extended` Explore extends the `aircraft_base` Explore. In addition, the `aircraft_extended` Explore has a `join` parameter that joins in the `aircraft_engine_types` view:
    
    
    explore: aircraft_extended {
      extends: [aircraft_base]
      label: "Aircraft Extended"
    
      join: aircraft_engine_types {
        type: left_outer
        sql_on: ${aircraft.aircraft_engine_type_id} = ${aircraft_engine_types.aircraft_engine_type_id} ;;
        relationship: many_to_one
      }
    }
    
    

The `join` parameter is additive, so the resultant Explore will display the views joined in the base Explore, plus the views joined into the extending Explore. In this case, the `aircraft_extended` Explore contains the `aircraft` view, the `aircraft_types` view, and the `aircraft_engine_types` view.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-extends-additive-joins-2410.png)

### Projects with localization

When extending an object, be aware that localization rules apply to your extensions as well. If you are extending an object and then defining new labels or descriptions, you should provide localization definitions in your project's locale strings files. See the [Localizing your LookML model](https://docs.cloud.google.com/looker/docs/model-localization#understanding_how_localization_rules_apply_to_extended_objects) documentation page for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-19 UTC."],[],[]] 
