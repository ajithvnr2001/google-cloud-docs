---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-required-joins/
title: required_joins \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:25.677886+00:00
---

# required_joins  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-required-joins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  required_joins Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    explore: view_name_1 {
      join: view_name_2 { ... }
      join: view_name_3 {
        required_joins: [view_name_2, ...]
      }
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) `required_joins` |  Default Value None Accepts Square brackets containing a comma-separated list of joins for this Explore Special Rules A view must be joined to an Explore before it can be referenced in `required_joins`  
---|---  
  
## Definition

`required_joins` forces one or more [`joins`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) to be included in the SQL that Looker generates, even if the user has not selected a field from that joined view. This behavior is triggered whenever the user selects a field from a related view that you specify. Multiple joins can be required by using a comma-separated list like `[join_name_a, join_name_b, ...]`.

When Looker generates SQL for a query, it attempts to create the cleanest SQL possible, and will only use the joins that are necessary for the fields a user selects. In the syntax diagram example at the top of this page:

  * If a user only chose a field from `view_name_2`, that would be the only view joined to the Explore.
  * If a user selects a field from `view_name_3`, then that join's `required_joins` parameter causes `view_name_2` to be joined to the Explore.



The primary use cases for `required_joins`:

  * Old syntax style with `sql_on`
  * Need or desire to write raw SQL



### Old syntax style with `sql_on`

[`sql_on`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-on) does not need `required_joins` when it is used with `${view_name.looker_dimension_name}` syntax. However, some older models still use the `view_name.native_column_name` syntax. For example:
    
    
    explore: order_items {
      join: order {
        sql_on: order_items.order_id = order.id ;;
      }
      join: customer {
        sql_on: order.customer_id = customer.id ;;
        required_joins: [order]
      }
    }
    

In this example, whenever a user selects a field from `customer`, the `order` view must be joined in as well to maintain the proper join relationship. If you forget to require this queries _might_ still work if the user happens to choose fields from all the required views. However, other queries may silently result in bad data due to the bad join.

Instead of using `required_joins`, consider modifying the model to use the `${view_name.looker_dimension_name}` syntax.

### Need or desire to write raw SQL

There are some cases when you cannot or do not want to use the `${view_name.looker_dimension_name}` syntax with [`sql_on`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-on). Typically this is because you want to use the raw values in your database and want to avoid any casting or other manipulations that occur with the `${view_name.looker_dimension_name}` syntax. Here is an example of the usage:
    
    
    explore: order {
      join: user {
        sql_on: ${order.user_id} = ${user.id} ;;
      }
      join: pre_sign_up_events {
        from: event
        sql_on:
          ${event.user_id} = ${user.id} AND
          event.date BETWEEN user.creation_date AND user.sign_up_date ;;
        required_joins: [user]
        relationship: one_to_many
      }
    }
    

In this example, the `pre_sign_up_events` join relies on dates from `user`. Consequently, it's important to make sure that `user` is joined in by using `required_joins`.

Instead of using `required_joins` to avoid casting with time or date fields, consider using the [`date_raw` type](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#individual_time_and_date_types) and avoid using `required_joins`.

## Common challenges

### A view must be joined to an Explore before it can be referenced in `required_joins`

To place a view into `required_joins`, you need to make sure it is joined to the [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) where the `required_joins` is being used. For example, this will not work:
    
    
    explore: order_items {
      join: customer {
        sql_on: order.customer_id = customer.id ;;
        required_joins: [order]
      }
    }
    

Here `order` hasn't been joined to `order_items`, so it isn't available for use in `required_joins`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
