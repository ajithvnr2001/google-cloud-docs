---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-view-name/
title: view_name \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:24.257922+00:00
---

# view_name  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-view-name/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  view_name Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    explore: explore_name {
      view_name: view_name
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `view_name` |  Default Value A view whose name matches the Explore's name Accepts The name of an existing view  
---|---  
  
## Definition

`view_name` determines the view that will define the fields of an Explore. If `view_name` is omitted, Looker assumes that the underlying view name is the same as the Explore name. Typically `view_name` is only used to create multiple Explores from the same view.

## Examples

Add an option to the Explore menu called **Customer** based on the view called `users`:
    
    
    explore: customer {
      view_name: users
    }
    

## Common challenges

### `view_name`, `from`, and `label` are often confused but have different behaviors

`view_name`, [`from`](https://docs.cloud.google.com/looker/docs/reference/param-explore-from) and [`label`](https://docs.cloud.google.com/looker/docs/reference/param-explore-label) parameters have similar, but different effects.

#### Using `view_name`

Use `view_name` to create multiple Explores from the same view, and reference fields the same way for each Explore:
    
    
    explore: customer {
      view_name: users
    }
    # Would appear in the Explore menu as 'Customer'
    # Fields would appear like 'User Name'
    # You would reference fields like ${users.name}
    
    explore: buyer {
      view_name: users
    }
    # Would appear in the Explore menu as 'Buyer'
    # Fields would appear like 'Users Name'
    # You would reference fields like ${users.name}
    

With `view_name: users`, the generated SQL uses the original table name, like this: `FROM schema.users AS users`.

#### Using `from`

Use `from` to create multiple Explores from the same view, and reference fields differently for each Explore:
    
    
    explore: customer {
      from: users
    }
    # Would appear in the Explore menu as 'Customer'
    # Fields would appear like 'Customer Name'
    # You would reference fields like ${customer.name}
    
    explore: buyer {
      from: users
    }
    # Would appear in the Explore menu as 'Buyer'
    # Fields would appear like 'Buyer Name'
    # You would reference fields like ${buyer.name}
    

With `from: users`, the generated SQL _aliases_ the original table name, like this: `FROM schema.users AS customer`.

#### Using `label`

Use `label` if you don't need to create multiple Explores from the same view, and you want the Explore's name to appear differently in the Explore menu:
    
    
    explore: users {
      label: "Customer"
    }
    # Would appear in the Explore menu as 'Customer'
    # Fields would appear like 'Users Name'
    # You would reference fields like ${users.name}
    

## Things to know

### `view_name` is rarely used to rename an Explore

It is uncommon to use `view_name` to rename an Explore, unless you are creating an extended model and need to create multiple Explores from the same view.

Consider renaming the underlying view or using [`label`](https://docs.cloud.google.com/looker/docs/reference/param-explore-label) to change how the Explore appears in the field picker.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
