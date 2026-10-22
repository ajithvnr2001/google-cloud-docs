---
url: https://docs.cloud.google.com/looker/docs/best-practices/flows/error-unknown-or-inaccessible-field/
title: Error: Unknown or inaccessible field \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:39.596092+00:00
---

# Error: Unknown or inaccessible field  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/flows/error-unknown-or-inaccessible-field/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Error: Unknown or inaccessible field Stay organized with collections  Save and categorize content based on your preferences. 

When you are working on your LookML files and are satisfied with your updates, the next step to deploy your LookML changes is to run the [LookML Validator](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_your_changes) to perform a full model validation. 

Occasionally, you might see an error like the following: 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-error-unknown-inaccessible-field-2210.png)
    
    
     Unknown or inaccessible field "user_order_facts.lifetime_orders" referenced in "users.lifetime_orders". Check for typos and missing joins.
    

In this example, the error refers to the `lifetime_orders` field in the `users` view. The error indicates that `users.lifetime_orders` cannot access the `user_order_facts.lifetime_orders` field that it references. 

## Debugging tree

Use the following decision tree to troubleshoot common Liquid issues:

The following sections describe the scenarios in the tree in further detail.

## Why does this error occur?

There are a few reasons this error can occur: 

  1. The field that you're referencing does not exist. 
  2. The field that you're referencing is an entire dimension group — for example, a dimension group is referenced without an appended`timeframe`. 
  3. The field is inaccessible by some Explores because there is a missing join. 



### The field does not exist

If the field `user_order_facts.lifetime_orders` is referenced in LookML fields but does not exist as a field itself, you will receive the `unknown or inaccessible field` error. 

You can resolve the error by adding the field that is triggering the error — in this example, `user_order_facts.lifetime_orders` — to the view that contains the field in question. In this case, you can make sure the field is defined in the `user_order_facts` view; if it doesn't exist, you can add it. 

### The field references an entire dimension group

Dimension groups represent a group of dimensions. [`type: time`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#time_type) dimension groups represent a group of time-period dimensions that are defined in the [`timeframe`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#timeframe_options) parameter. When you reference dimension groups in LookML, you _must_ append the appropriate dimension — `timeframe`, in this case — to the dimension group name. 

For example, consider the following dimension group: 
    
    
      dimension_group: created {
        type: time
        timeframes: [date, week, month]
        sql: ${TABLE}.created_at ;;
      }
    

If you want to reference the `created` dimension group in another LookML field, you must reference a specific _timeframe_ dimension within the group, such as one of the following: 

  * **`date`** : `${created_date}`
  * **`week`** : `${created_week}`
  * **`month`** : `${created_month}`



If you try to use just the name of the dimension group — `${created}` — Looker won't know which timeframe you are referring to and will generate the error. 

### There is a missing join

The following is the LookML definition of `users.lifetime_orders`: 
    
    
      dimension: lifetime_orders {
        type: number
        sql: ${user_order_facts.lifetime_orders};;
      }
    

> Note the use of the [substitution operators](https://docs.cloud.google.com/looker/docs/sql-and-referring-to-lookml)` ${}` to reference the LookML field `user_order_facts.lifetime_orders`. 

The `lifetime_orders` dimension in the `users` view references the `lifetime_orders` field from the `user_order_facts` view. In this case, the error is triggered because there are instances in the model file where the `users` view is joined to an Explore _without_ the `user_order_facts` having been joined as well. 

To see which Explores are causing the problem, you can expand the occurrences that are highlighted in the error message: 

![Expanded error message displaying the views, view code lines, and Explores of two causes: users:79 \(ecommerce:order_items\) and users:79 \(ecommerce:orders\).](https://docs.cloud.google.com/static/looker/docs/images/hc-error-unknown-inaccessible-field-expanded-2210.png)

These occurrences show that the `order_items` and `orders` Explores in the `ecommerce` model are causing the error. These Explores have many [joins](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) and are defined as the following in the model file: 
    
    
      explore: orders {
        join: users { # users joined without user_order_facts
          relationship: many_to_one
          sql_on: ${orders.user_id} = ${users.id}
        }
      }
    
      explore: order_items {
        join: inventory_items {
          relationship: many_to_one
          sql_on: ${order_items.inventory_item_id} = ${inventory_items.id}
        }
        join: orders {
          relationship: many_to_one
          sql_on: ${order_items.order_id} = ${orders.id}
        }
        join: users { # users joined without user_order_facts
          relationship: many_to_one
          sql_on: ${orders.user_id} = ${users.id}
        }
      }
    

In both of these Explores, the `users` view is joined _without_ also joining the `user_order_facts` view; as such, neither Explore can access the `user_order_facts.lifetime_orders` field. If you tried to query the `users.lifetime_orders` field — which references `user_order_facts.lifetime_orders` — in either Explore, you would trigger the error. 

The LookML validator is warning you that users will receive the error when they query `users_order_facts.lifetime_orders`. The `users.lifetime_orders` field won't trigger the error in an Explore to which `user_order_facts` is also joined. 

For example, consider the `users` Explore: 
    
    
      explore: users {
        join: user_order_facts {
          sql_on: ${users.id} = ${user_order_facts.users_id}
        }
      }
    

Here `user_order_facts` _is_ joined, so querying `users.lifetime_orders` won't trigger an error. 

## How can I fix the error when it is caused by a missing join?

If the error is caused by a missing join, you can fix this error in a couple of ways: 

  1. Join the missing view in **all cases**. For the example used throughout this page, make sure the `user_order_facts` view is joined wherever the `users` view is joined in an Explore. 
  2. [Exclude](https://docs.cloud.google.com/looker/docs/reference/param-explore-fields) the field causing the error from Explores if you don't want to join the missing view. 



### Join the missing view

In the preceding example the error can be solved by joining `user_order_facts` to all the Explores where `users` is also joined. This will ensure that Explores can access `user_order_facts.lifetime_orders` when `users.lifetime_orders` is used in a query. 

> You can use the [metadata panel in the IDE](https://docs.cloud.google.com/looker/docs/lookml-metadata#metadata_for_views) to see all Explores that use the `users` view. 

The following example joins the missing views: 
    
    
      explore: order_items {
        join: inventory_items {
          relationship: many_to_one
          sql_on: ${inventory_items.id} = ${order_items.inventory_item_id}
        }
        join: orders {
          relationship: many_to_one
          sql_on: ${order_items.order_id} = ${orders.id}
        }
        join: users {
          relationship: many_to_one
          sql_on: ${orders.user_id} = ${users.id}
        }
        join: user_order_facts { # join user_order_facts through users
          relationship: many_to_one
          sql_on: ${users.id} = ${user_order_facts.users_id}
        }
      }
    

Now, if you rerun the LookML validator, this error shouldn't appear. 

### Exclude the field that is causing the error from Explores

You may not want to join the `user_order_facts` view to all Explores where `users` is joined. For example, maybe you don't want users to access the fields from the `user_order_facts` view in the `orders` Explore, but you _do_ want users to access the fields from the `users` view without error. You can do this by excluding the field causing the error — `users.lifetime_orders` — from the `orders` Explore, using the [`fields`](https://docs.cloud.google.com/looker/docs/reference/param-explore-fields) parameter. 

The `fields` parameter for Explores lets you include or exclude specific fields from an Explore. In this case, you can exclude the `users.lifetime_orders` field from the `orders` Explore like this: 
    
    
      explore: orders {
        fields: [-users.lifetime_orders] # exclude users.lifetime_orders
        join: users {
          relationship: many_to_one
          sql_on: ${orders.user_id} = ${users.id}
        }
      }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
