---
url: https://docs.cloud.google.com/looker/docs/changing-explore-menu-and-field-picker/
title: Changing the Explore menu and field picker \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:39.149407+00:00
---

# Changing the Explore menu and field picker  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/changing-explore-menu-and-field-picker/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Changing the Explore menu and field picker Stay organized with collections  Save and categorize content based on your preferences. 

You can use a number of LookML parameters to make your Explores more user-friendly by changing how fields appear in the user interface without altering your underlying LookML. This page provides an overview of LookML parameters that modify the appearance of the Looker Explore menu and field picker.

In Looker, your users can see Explores listed in the **Explore** menu.  |  Within an Explore, your users can use the **field picker** to select the fields ([dimensions](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension) and [measures](https://docs.cloud.google.com/looker/docs/reference/param-field-measure)) to use to query their data.  
---|---  
![Explores are listed in the Explore menu below the name of the model they belong to.](https://docs.cloud.google.com/static/looker/docs/images/develop-explore-menu-list-2120.png) |  ![The field picker in an Explore shows an expandable list of views containing fields that you can add to your query.](https://docs.cloud.google.com/static/looker/docs/images/develop-field-picker-2410.png)  
  
This page lists each commonly used parameter with a link to its full reference page, a short description of its function, and an image of what it does.

For tips and suggestions about making a user-friendly Explore, see the [Best practice: Create a positive experience for Looker users](https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-a-positive-experience-for-looker-users) Best Practices page.

## Explore name and menu

This section describes the default behavior for an Explore's name and appearance on the **Explore** menu, then describes the LookML parameters that let you change that behavior:

  * `label` (model)
  * `label` (Explore)
  * `group_label` (Explore)
  * `description` (Explore)
  * `hidden` (Explore)



### Explore menu default behavior

#### Model names

By default, the **Explore** menu is organized by model names, which are determined by the name of each model file. The **Explore** menu shows a formatted version of the model name, with underscores changed to spaces and each word capitalized. Under each model name is a list of the Explores defined in that model file.

#### Explore names

The name of each Explore in the menu is based on the corresponding `explore` parameter in the model file. As with the model names, Explore names are formatted in the menu so that underscores are changed to spaces and each word is capitalized. The Explore name is also shown as the Explore title in the field picker panel.

In the following example, the `order_items` Explore is defined in the model file `e_commerce_model.model`:
    
    
    explore: order_items {
      join: orders {
        type: left_outer
        sql_on: ${order_items.order_id} = ${orders.id} ;;
        relationship: many_to_one
      }
    }
    
    

The `order_items` Explore shows up as **Order Items** in the Explore menu and field picker.

Explore menu: |  Field picker:  
---|---  
![Order Items appears in the list of Explores in the Explore menu.](https://docs.cloud.google.com/static/looker/docs/images/develop-function-explore-menu-2112.png) | ![The Order Items label appears at the top left of the field picker panel.](https://docs.cloud.google.com/static/looker/docs/images/develop-function-explore-field-picker-2112.png)  
  
For more information about model files, see the [Understanding model and view files](https://docs.cloud.google.com/looker/docs/model-and-view-files#model_files) documentation page. For more information about defining Explores, see the [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) parameter documentation page.

### `label` (model)

A model's [`label`](https://docs.cloud.google.com/looker/docs/reference/param-model-label) parameter renames a model in the **Explore** menu without changing how it's referenced in LookML. Explore URLs, the Looker IDE, and SQL Runner still reflect the actual model name; the way the model should be referenced in LookML and Admin settings remains unchanged.

By default, the model `market_research.model` appears as **Market Research** in the Explore menu.

![](https://docs.cloud.google.com/static/looker/docs/images/develop-label-model-default-2120.png)

You can use the `label` parameter to rename the model in the Explore menu. For example, you add the code `label: "Marketing R&D"` to the `market_research.model` model file:
    
    
    label: "Marketing R&D"
    
    

In this example, Looker displays the model name as follows in the Explore menu:

![The Market Research model has the label Marketing R&D in the Explore menu.](https://docs.cloud.google.com/static/looker/docs/images/develop-label-model-with-label-2120.png)

### `label` (Explore)

An Explore's [`label`](https://docs.cloud.google.com/looker/docs/reference/param-explore-label) parameter renames an Explore in the **Explore** menu and on the Explore page without changing how it's referenced in LookML.

If the `label` parameter is not used, the Explore name displays according to its default behavior.

![An Explore with the label Order Item Information in the Explore menu and field picker.](https://docs.cloud.google.com/static/looker/docs/images/dev-explore-params-label-2412.png)

### `group_label` (Explore)

An Explore's [`group_label`](https://docs.cloud.google.com/looker/docs/reference/param-explore-group-label) parameter changes the default organization of the **Explore** menu. Instead of listing each Explore under its model's name, `group_label` lets you define a custom heading under which to list one or more Explores.

In this example, the Explores **Customers** , **Inventory** , **Order Items** , and **User Data** are listed under the group label **Online Store Queries** :

![Explores listed under the Online Store Queries group label in the Explore menu.](https://docs.cloud.google.com/static/looker/docs/images/reference-group-label-2112.png)

### `description` (Explore)

An Explore's [`description`](https://docs.cloud.google.com/looker/docs/reference/param-explore-description) parameter lets you add a description of an Explore to the UI, so users can get additional information while creating Explore queries.

Users can see the description by hovering over the information icon, next to the Explore name at the top of the field picker. The information icon also appears in the drop-down list of Explores. If you do not explicitly add a description to an Explore, no description displays.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-description-explore-menu-2216.png)

### `hidden` (Explore)

An Explore's [`hidden`](https://docs.cloud.google.com/looker/docs/reference/param-explore-hidden) parameter hides the Explore from the **Explore** menu. By default, `hidden` is off and the Explore will be displayed. `hidden` does not hide LookML or prevent access to an Explore via the URL. `hidden` is not meant as a security feature, but rather as a presentation feature.

As an example, adding the LookML code `hidden: yes` to the LookML for the `inventory` Explore in the following example hides the **Inventory** Explore from the Explore menu:
    
    
    explore: inventory {
      hidden: yes
    
      join: order_facts {
        view_label: "Orders"
        relationship: many_to_one
        sql_on: ${order_facts.order_id} = ${order_items.order_id} ;;
      }
    }
    
    

## Field picker

This section describes the default behavior of the field picker, then describes the LookML parameters that let you change that behavior.

Change how view names appear in the field picker with:

  * `view_label` (Explore)
  * `view_label` (join)
  * `label` (view)



Change how names of individual fields appear in the field picker with:

  * `description` (field)
  * `hidden` (field)
  * `label` (field)
  * `fields` (field)



Change how fields are organized within the field picker with:

  * `view_label` (field)
  * `group_label` (field)



### Field picker default behavior

By default, the field picker is organized by headings that correspond to the views specified by the LookML `view` parameter. Each view's fields are grouped in the field picker. The type of field (dimension, dimension group, measure, filter field, and parameter field) determines where the field is shown within the view. Unless the `label` parameter is used to alter the display name, the field picker will show a formatted version of the LookML view or field name, with underscores changed to spaces and each word capitalized.

In the following example, Looker displays the `accounts` [view](https://docs.cloud.google.com/looker/docs/reference/param-view-view) as **Accounts** in the field picker, which is the default behavior:
    
    
    view: accounts {
      sql_table_name: accounts ;;
    }
    
    

![](https://docs.cloud.google.com/static/looker/docs/images/develop-view-default-behavior-2112.png)

The following example shows how the names of a [dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension), [dimension group](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group), and [measure](https://docs.cloud.google.com/looker/docs/reference/param-field-measure) show by default. The same formatting will apply to the names of any filter fields and parameter fields.
    
    
    dimension: account_number {
      primary_key: yes
      type: number
      sql: ${TABLE}.account_number ;;
    }
    
    dimension: name {
      type: string
      sql: ${TABLE}.name ;;
    }
    
    dimension_group: created {
      type: time
      timeframes: [raw, time, date, week, month, quarter, year]
      sql: ${TABLE}.created_date ;;
    }
    
    measure: average_annual_revenue {
      type: average
      sql: ${annual_revenue} ;;
      value_format_name: custom_amount_value_format
    }
    
    

In this example, the field picker shows the default field names **Account Number** , **Name** , **Created Date** , and **Average Annual Revenue** for the `account_number` and `name` dimensions, the `created` dimension group, and the `average_annual_revenue` measure, respectively.

![](https://docs.cloud.google.com/static/looker/docs/images/develop-fields-default-behavior-2112.png)

If you change the name of a field, then the field picker adapts to the new name but you might want to add an [`alias`](https://docs.cloud.google.com/looker/docs/reference/param-field-alias) parameter with the field's old name. That parameter provides alternative names for a field that might appear in the URL for a query. It can be useful in cases when field names in a model change, but some people have [shared links to data](https://docs.cloud.google.com/looker/docs/sharing-urls#share_the_url) and you want to keep those pre-existing URLs functioning.

### `view_label` (Explore)

An Explore's [`view_label`](https://docs.cloud.google.com/looker/docs/reference/param-explore-view-label) parameter changes how the group of fields from an Explore's base view is labeled in the field picker without changing how the Explore and its fields are referenced in LookML.

As an example, if you join a view `order_facts` to an Explore called `order_items`, you can use the `view_label` parameter to set the label that Looker displays for the `order_facts` view in the field picker as follows:
    
    
    explore: order_items {
      label: "Order Items"
      join: order_facts {
        view_label: "Orders and more"
        relationship: many_to_one
        sql_on: ${order_facts.order_id} = ${order_items.order_id} ;;
      }
    }
    
    

In this example, the `order_facts` view appears as **Orders and more** in the field picker of the **Order Items** Explore.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-explore-view-label-2112.png)

### `view_label` (join)

A join's [`view_label`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-view-label) parameter lets you group fields from one view under another view's name in the field picker. If you do not explicitly add a `view_label` to a join, the `view_label` defaults to the name of the join.

For example, you join the `products` view to the `product_facts` Explore:
    
    
    explore: product_facts {
      join: products {
        type: left_outer
        sql_on: ${product_facts.product_id} = ${products.id} ;;
        relationship: many_to_one
      }
    }
    
    

In this example, since a view label is not specified, the fields from the `products` view are grouped under the **Products** view label in the field picker, separate from the **Product Facts** view:

![The fields from the Product view are grouped under the Product view label by default.](https://docs.cloud.google.com/static/looker/docs/images/develop-view_label-separate-2112.png)

You can use the `view_label` parameter to add a view label to the joined `products` view, as in the following example:
    
    
    explore: product_facts {
      join: products {
        view_label: "Product Facts"
        type: left_outer
        sql_on: ${product_facts.product_id} = ${products.id} ;;
        relationship: many_to_one
      }
    }
    
    

This groups the fields from the `products` view under the view label **Product Facts** in the field picker:

![The fields from the Product view are grouped under the Product Facts view label.](https://docs.cloud.google.com/static/looker/docs/images/develop-view_label-grouped-2112.png)

### `label` (view)

A view's [`label`](https://docs.cloud.google.com/looker/docs/reference/param-view-label) parameter changes how the view is labeled in the field picker without changing how it is referenced in LookML. If not specified, the label defaults to the name of the view. Unlike `view_label` (Explore) and `view_label` (Join), this parameter affects all Explores that use the view.

As an example, you can use the `label` parameter to specify a label for the `inventory_items` view as follows:
    
    
    view: inventory_items {
      label: "Items in Inventory"
      sql_table_name: inventory_items ;;
    }
    
    

In this example, the field picker displays the label **Items in Inventory** for the `inventory_items` view, rather than the default label **Inventory Items**.

![](https://docs.cloud.google.com/static/looker/docs/images/develop-funct-display-label-view-2112.png)

### `description` (field)

You can add a [`description`](https://docs.cloud.google.com/looker/docs/reference/param-field-description) to any field. For BigQuery connections, if you [generate a LookML project from your database](https://docs.cloud.google.com/looker/docs/generating-a-model), Looker will autopopulate field descriptions with the descriptions from your BigQuery column metadata, if any.

The user can see this description in multiple places. Looker displays the description when the user selects the information icon to the right of the field name in the field picker.

![](https://docs.cloud.google.com/static/looker/docs/images/field-desc-info-icon-2112.png)

In addition, Looker also displays the description when the user hovers over the column name in a table or table chart visualization in an Explore, a dashboard, or a Look.

![](https://docs.cloud.google.com/static/looker/docs/images/table-desc-hover-2104.png)

### `hidden` (field)

By default, fields specified in a view will be displayed in the field picker. The field's [`hidden`](https://docs.cloud.google.com/looker/docs/reference/param-field-hidden) parameter hides a field in the field picker.

Hidden fields can still be accessed in the UI if they are manually added to the URL and will show up in some Looker windows. Therefore, think of `hidden` as a way to keep the field picker clean, and not as a security feature.

As an example, adding the LookML code `hidden: yes` to the LookML for the `product_id` dimension in the following example hides the **Product ID** dimension from the field picker:
    
    
    dimension: product_id {
      hidden: yes
      type: number
      sql: ${TABLE}.product_id ;;
    }
    
    

### `fields` (field)

The [`fields`](https://docs.cloud.google.com/looker/docs/reference/param-explore-fields) parameter lets you specify which fields from an Explore's base view and joins are exposed in the field picker. If you do not use the `fields` parameter, Looker exposes all fields.

To specify the fields you want to display in the field picker, use a comma-separated list of fields or sets. To specify the fields you want to hide from the field picker, use the set `ALL_FIELDS*` with a comma-separated list of the fields or sets to be excluded, with a hyphen (-) preceding each.

As an example, you can use the following LookML code to display only a selection of fields from the `aircraft` Explore in the field picker:
    
    
    explore: aircraft {
      fields: [
        aircraft.aircraft_model_code,
        aircraft.aircraft_engine_code,
        aircraft.count,
        aircraft.city,
        aircraft.country,
        aircraft.zip,
       ]
    }
    
    

In this example, the **Aircraft** Explore displays only the **Aircraft Model Code** , **Aircraft Engine Code** , **City** , **Country** , and **Zip** dimensions and the **Count** measure in the field picker.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-fields-field-2112.png)

### `label` (field)

A field's [`label`](https://docs.cloud.google.com/looker/docs/reference/param-field-label) parameter lets you change how a field name will appear in the field picker without changing how it is referenced in LookML. If no label is specified, the label defaults to the name of the field.

As an example, you can use the `label` parameter to set a label for the `cost` dimension as follows:
    
    
    dimension: cost {
      label: "price"
      type: number
      sql: ${TABLE}.cost ;;
    }
    
    

In this example, the **Cost** dimension has the label **price** in the field picker.

![](https://docs.cloud.google.com/static/looker/docs/images/develop-funct-display-label-field-2112.png)

### `view_label` (field)

A field's [`view_label`](https://docs.cloud.google.com/looker/docs/reference/param-field-view-label) parameter lets you change the name of the view under which the field is listed in the field picker without changing how it is referenced in LookML. If no label is specified, the field appears under the label for the view in which it is defined.

As an example, you can use the `view_label` parameter as follows to specify a view label for the `cost` dimension:
    
    
    dimension: cost {
      view_label: "Cost Information"
      type: number
      sql: ${TABLE}.cost ;;
    }
    
    

In this example, Looker displays the **Cost** dimension under the **Cost Information** view label in the field picker.

![](https://docs.cloud.google.com/static/looker/docs/images/develop-funct-display-view_label-field-2112.png)

### `group_label` (field)

The [`group_label`](https://docs.cloud.google.com/looker/docs/reference/param-field-group-label) parameter lets you combine fields together in a common drop-down list within a view in the field picker.

In this example, the **Shipping Info** group includes the fields **Shipping City** , **Shipping Country** , and **Shipping State** :

![The Shipping Info group in the field picker of an Explore.](https://docs.cloud.google.com/static/looker/docs/images/dev-group-label-2112.png)

### `group_item_label` (field)

When fields are shown under a group label, they might not need to have their full field names or labels displayed in the field picker. In the example shown previously for `group_label` (field), the group label already indicates that the fields pertain to shipping. In cases like this, you can add the [`group_item_label`](https://docs.cloud.google.com/looker/docs/reference/param-field-group-item-label) parameter to each of these grouped fields to change how they look under the group label.

In this example, the **Shipping Info** group includes the fields **City** , **Country** , and **State** :

![The Shipping Info group in the field picker of an Explore.](https://docs.cloud.google.com/static/looker/docs/images/dev-group-item-label-2112.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
