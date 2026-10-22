---
url: https://docs.cloud.google.com/looker/docs/best-practices/dry-cookbook-2/
title: Maximizing code reusability with DRY LookML: Defining reusable lists of fields with the set parameter \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:01.217006+00:00
---

# Maximizing code reusability with DRY LookML: Defining reusable lists of fields with the set parameter  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/dry-cookbook-2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Maximizing code reusability with DRY LookML: Defining reusable lists of fields with the set parameter Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page is part of the [Looker cookbook: Maximizing code reusability with DRY LookML](https://docs.cloud.google.com/looker/docs/best-practices/dry-lookml-cookbook).

One way to make your LookML projects more efficient and easier to maintain is with the LookML `set` parameter. The `set` parameter lets you group fields that may often be repeated throughout your project within the `fields` parameter or within drill fields. If you use a set to group repeated fields, you create a single place within the model where that group of fields can be maintained.

This page includes the following examples of using LookML sets to make your LookML projects more efficient and maintainable:

  * Adding the same drill fields to multiple measures: Define drill fields for details that your users commonly want to see when they drill into aggregations.
  * Including or omitting a set of fields from an Explore: Customize the Explore experience for users and simplify the list of fields that users can choose from in the field picker.

**Important:** If you use the `set` parameter in one view to reference a field that is from a second view, make sure that the second view is joined to the [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) where `set` is being used. Use the syntax `view_name.field_name` to reference fields from a joined view within a set.

## Ingredients

  * The LookML [`set` parameter](https://docs.cloud.google.com/looker/docs/reference/param-view-set)
  * The LookML [`fields` parameter (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-fields)
  * The LookML [`drill_fields` parameter (for fields)](https://docs.cloud.google.com/looker/docs/reference/param-field-drill-fields)
  * The LookML [`drill_fields` parameter (for views)](https://docs.cloud.google.com/looker/docs/reference/param-view-drill-fields)



## Prerequisites

  * [A configured LookML model](https://docs.cloud.google.com/looker/docs/generating-a-model#when_you_need_to_configure_models)
  * [Permissions to develop LookML](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permission_sets)



## Example: Adding the same drill fields to multiple measures

Suppose you want your users to be able to drill down to see more granular user details wherever they see sales metrics in Explores, Looks, or dashboards, so that selecting a value for the **Count** measure in the Explore UI opens a query on the fields **ID** , **City** , **State** , and **Country** :

![Selecting a value for the Count measure opens a query on the fields ID, City, State, and Country.](https://docs.cloud.google.com/static/looker/docs/images/drill-fields-measure-2210.png)

You can create a set called `user_details` that includes the fields `id`, `city`, `state`, and `country` and then reference them in multiple measures for your users to drill into:
    
    
    set: user_details {
      fields: [id, city, state, country]
    }
    
    

The `user_details` set can be used to define a [drill field](https://docs.cloud.google.com/looker/docs/reference/param-field-drill-fields) for the `count` measure:
    
    
    measure: count {
      type: count
      drill_fields: [user_details*]
    }
    
    

In this example, the syntax `[set_name*]` is used to specify that the fields within the `user_details` will appear in the query results when you drill into the **Count** measure.

You can then reuse this set to create additional drill fields. For example, you can add the LookML code `drill_fields: [user_details*]` to the `order_count`, `total_sale_price`, and `average_sale_price` measures:
    
    
    measure: order_count {
      view_label: "Orders"
      type: count_distinct
      description: "Number of orders"
      sql: ${order_id} ;;
      drill_fields: [user_details*]
    
    }
    
    measure: total_sale_price {
      type: sum
      value_format_name: usd
      sql: ${sale_price} ;;
      drill_fields: [user_details*]
    }
    
    measure: average_sale_price {
      type: average
      value_format_name: usd
      sql: ${sale_price} ;;
      drill_fields: [user_details*]
    }
    
    

As with the **Count** measure, when a user selects a value for **Order Count** , **Total Sale Price** , or **Average Sale Price** in the Explore UI, Looker opens a window containing a query on the fields **ID** , **City** , **State** , and **Country**.

If you want to change anything about the drill fields, such as adding or removing a field, you would only have to update the `user_details` set.

You can also reference a set within the [`drill_fields` parameter of a view](https://docs.cloud.google.com/looker/docs/reference/param-view-drill-fields) to define drill fields for all measures within that view that do not already have drill fields specified at the field level.

## Example: Including or omitting a set of fields from an Explore

Suppose you want to simplify the Explore field picker for users by excluding fields that are not crucial for those users.

For example, suppose you have a `users` view that contains information about your customers, including fields for **ID** , **First Name** , **Last Name** , **Email** , and **Age** , as well as location fields like **City** , **State** , **Country** , and **Zip**. The `users` view is joined to the `orders` Explore:

![The field picker for the Orders view includes all the fields from the Orders and Users view, including the fields that you want to omit.](https://docs.cloud.google.com/static/looker/docs/images/dry-cookbook-exclude-set-all-fields-example-2304.png)

What if you want to exclude the **First Name** , **Last Name** , **Email** , **Age** , and **Gender** fields from the Explore for your users? You can create a set called `user_info` that lists the fields you want to exclude from the **Orders** Explore:

![The Orders Without User Data Explore excludes the First Name, Last Name, Email, Age, and Gender fields from the Explore field picker.](https://docs.cloud.google.com/static/looker/docs/images/dry-cookbook-exclude-set-example-2304.png)

The LookML for the `user_info` set would look like this:
    
    
    set: user_info {
      fields: [first_name, last_name, email, age, gender]
    }
    
    

To define an **Orders** Explore with the label **Orders Without User Data** , join the `users` view to the `orders` Explore. Add the LookML code `fields: [ALL_FIELDS*, -users.user_info*]` to the `orders` Explore to include all fields except for the fields in the `user_info` set from the `users` view:
    
    
    explore: orders {
      fields: [ALL_FIELDS*, -users.user_info*]
      label: "Orders Without User Data"
      join: users {
        type: left_outer
        sql_on: ${orders.user_id} = ${users.id} ;;
        relationship: many_to_one
      }
    }
    
    

Because the `user_details` set is excluded from the Explore with the syntax `-users.user_details*` in the `fields` parameter of the `orders` Explore, the **Orders** view within the **Orders Without User Data** Explore omits the fields listed in the `users_user.info` set from the Explore field picker.

You can reuse the `user_info` set to omit these fields from the Explore UI for any other Explores to which the `users` view is joined. If you want to change anything about the `user_info` set, such as adding or removing a field, you would only have to update the `user_info` set.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
