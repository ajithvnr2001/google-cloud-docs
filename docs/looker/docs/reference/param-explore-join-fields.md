---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-fields/
title: fields (for joins) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:24.487522+00:00
---

# fields (for joins)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-fields/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  fields (for joins) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `fields` parameter that is part of a [join](https://docs.cloud.google.com/looker/docs/reference/param-explore-join).
> 
> `fields` can also be used as part of an Explore, described on the [`fields` (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-fields) parameter documentation page.
> 
> `fields` can also be used as part of a set, described on the [`set`](https://docs.cloud.google.com/looker/docs/reference/param-view-set) parameter documentation page.

## Usage
    
    
    explore: view_name_1 {
      join: view_name_2 {
        fields: [
          field-or-set-specification,
          field-or-set-specification,
          ...
        ]
      }
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) `fields` |  Default Value All fields in the joined view Accepts Square brackets containing a comma-separated list of fields or sets Special Rules

  * Set names always end with an asterisk (`*`)
  * At the join level, fields and sets can only be included, not excluded. You can, however, exclude _all_ fields by using the `fields` parameter with an empty list, like this: `fields: []`

  
---|---  
  
## Definition

`fields` at the join level lets you specify which fields from a joined view are brought into an Explore. If you do not use `fields` Looker defaults to adding all fields from the view.

A list of fields may be used, like `[field_a, field_b]`.

You can also reference a set of fields (which are created by the [`set`](https://docs.cloud.google.com/looker/docs/reference/param-view-set) parameter), like `[set_a*]`. The asterisk tells Looker that you are referencing a set name instead of a field name.

## Examples

Only add the field called `name` from the `customer` view to the `order` Explore:
    
    
    explore: order {
      join: customer {
        sql_on: ${order.customer_id} = ${customer.id} ;;
        fields: [name]
      }
    }
    

Add the fields called `name`, `address`, and `age` from the `customer` view to the `order` Explore:
    
    
    explore: order {
      join: customer {
        sql_on: ${order.customer_id} = ${customer.id} ;;
        fields: [name, address, age]
      }
    }
    

Add the set of fields called `order_fields` from the `customer` view to the `order` Explore:
    
    
    explore: order {
      join: customer {
        sql_on: ${order.customer_id} = ${customer.id} ;;
        fields: [order_fields* ]
      }
    }
    

## Common challenges

### `fields` can only reference fields from its own `join`

`fields` will be a child of a [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join), which references a view. Any dimensions or measures that are referenced in `fields` must be a part of that view. For example, suppose we have:
    
    
    explore: order {
      join: customer {
        sql_on: ${order.customer_id} = ${customer.id} ;;
        fields: [name]
      }
    }
    

To work properly, a dimension or measure called `name` must exist in the `customer` view.

## Things to know

### Use `fields: []` with an empty list to exclude all fields

You can exclude _all_ fields from a joined view by using the `fields` parameter with an empty list in your join, like this:
    
    
    explore: order {
      join: customer {
        fields: []
        sql_on: ${order.customer_id} = ${customer.id} ;;
      }
    }
    

In this example, none of the fields from the `customer` view will be displayed in the `order` Explore.

The only way to remove fields at the `join` level is to exclude them all at once with `fields: []`. You cannot use the `ALL_FIELDS*` set to exclude all fields at the `join` level.

However, at the `explore` level, you can use the `ALL_FIELDS*` set to exclude individual items, as described in the You can exclude individual items by using `fields` with `explore` section on this page.

### You can exclude individual items by using `fields` with `explore`

When `fields` is nested under a [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) parameter, you can exclude all fields at once using `fields: []` or you can include specific fields. But you cannot _exclude_ specific fields one at a time. For example, if you had 100 fields, and you only wanted to exclude one of them, you would need to list out all 99 fields that you _did_ want.

However, you can instead nest `fields` under the [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) parameter in order to take advantage of the `ALL_FIELDS*` set and then exclude fields. For example:
    
    
    explore: order {
      fields: [
        ALL_FIELDS*,
        -customer.unwanted_field_a,
        -customer.unwanted_field_b
      ]
      join: customer {
        sql_on: ${order.customer_id} = ${customer.id} ;;
      }
    }
    

Notice how we were able to reference fields from the joined view `customer` in the Explore level's `fields` parameter by using the syntax `view_name.field_name`.

### Different types of `fields` parameters are applied at different times

This page describes `fields` when it is nested under a [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) parameter. There is also a similar [`fields`](https://docs.cloud.google.com/looker/docs/reference/param-explore-fields) parameter that is nested under [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore). When both are used at the same time, they are applied in a specific order, which affects the resultant behavior:

First, all the `fields` parameters under [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) are applied. This creates the set of fields that the Explore can choose from. Consider this example:
    
    
    explore: orders {
      join: users {
        fields: [name]
        sql_on: ${orders.user_id} = ${users.id} ;;
      }
    }
    

In this case, the fields that will be available are everything from `orders`, and `name` from `users`. This is the group of fields that would be in the `ALL_FIELDS*` set (described in the section on excluding individual items).

Now, if we add a [`fields`](https://docs.cloud.google.com/looker/docs/reference/param-explore-fields) parameter under [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore), we're adding a restriction on top of that set. Suppose we did this:
    
    
    explore: orders {
      fields: [orders.price, users.address]
      join: users {
        fields: [name]
        sql_on: ${orders.user_id} = ${users.id} ;;
      }
    }
    

In this case:

  * `price` from `orders` will show up as expected, because it is in the `ALL_FIELDS*` set we created.
  * `address` from `users` _won't_ show up, because it wasn't included when `users` was joined in (only `name` was).
  * `name` from `users` won't show up either, because we didn't add it to the Explore in the row `fields: [orders.price, users.address]`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
