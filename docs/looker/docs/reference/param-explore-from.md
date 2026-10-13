---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-from/
title: from (for Explores) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:21.891058+00:00
---

# from (for Explores)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-from/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  from (for Explores) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `from` parameter that is part of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore).
> 
> `from` can also be used as part of a join, described on the [`from` (for joins)](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-from) parameter documentation page.

## Usage
    
    
    
    explore: explore_name {
      from: view_name
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `from` |  Default Value A view whose name matches the Explore's name Accepts The name of an existing view  
---|---  
  
## Definition

`from` determines the view that will define the fields of an Explore. If `from` is omitted, Looker will assume that the underlying view name is the same as the Explore name. Typically `from` is only used if you want the Explore _and its fields_ to have a different name than the underlying view.

To make this more clear, consider an example where a dimension called `order_value` has been created in a view called `underlying_view`:

  * This field would typically appear as **UNDERLYING VIEW Order Value** in the Explore UI, and would be referenced in LookML with `${underlying_view.order_value}`.
  * In the usage example given, the field would appear instead as **NEW ALIAS NAME Order Value** and be referenced as `${new_alias_name.order_value}`.



## Examples

Add an option to the Explore menu called **Customer** based on the view called `user`:
    
    
    explore: customer {
      from: user
    }
    

## Common challenges

### `from`, `view_name`, and `label` are often confused but have different behaviors

As seen in the preceding examples, `from` has many effects on the way that an Explore is labeled and the way that fields are referenced. There is also a [`view_name`](https://docs.cloud.google.com/looker/docs/reference/param-explore-view-name) parameter and a [`label`](https://docs.cloud.google.com/looker/docs/reference/param-explore-label) parameter that have similar, but different, effects.

#### Using `from`

You should use this option if you want to create multiple Explores from the same view and also want to reference fields _differently_ for each Explore:
    
    
    explore: customer {
      from: user
    }
    # Would appear in the Explore menu as 'Customer'
    # Fields would appear like 'Customer Name'
    # You would reference fields like ${customer.name}
    
    explore: buyer {
      from: user
    }
    # Would appear in the Explore menu as 'Buyer'
    # Fields would appear like 'Buyer Name'
    # You would reference fields like ${buyer.name}
    

The underlying reason for this behavior is that with `from: user`, the generated SQL _aliases_ the original table name, like this: `FROM schema.users AS customer`.

#### Using `view_name`

You should use this option if you want to create multiple Explores from the same view, and you want to reference fields the _same_ way for each Explore:
    
    
    explore: customer {
      view_name: user
    }
    # Would appear in the Explore menu as 'Customer'
    # Fields would appear like 'User Name'
    # You would reference fields like ${user.name}
    
    explore: buyer {
      view_name: user
    }
    # Would appear in the Explore menu as 'Buyer'
    # Fields would appear like 'User Name'
    # You would reference fields like ${user.name}
    

The underlying reason for this behavior is that with `view_name: user`, the generated SQL uses the original table name, like this: `FROM schema.users AS users`.

#### Using `label`

You should use this option if you _don't_ need to create multiple Explores from the same view, but want the Explore's name to appear _differently_ in the Explore menu:
    
    
    explore: user {
      label: "Customer"
    }
    # Would appear in the Explore menu as 'Customer'
    # Fields would appear like 'User Name'
    # You would reference fields like ${user.name}
    

## Things to know

### `from` is rarely used with `explore`

It's not very common to use `from` to re-name an Explore. Although there are legitimate use cases, if you find yourself wanting to use this parameter, consider if you can simply rename the underlying view instead. It's much more common to rename joins using the join-level [`from`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-from) parameter.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
