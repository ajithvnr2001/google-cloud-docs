---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-group-label/
title: group_label (for Explores) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:22.090781+00:00
---

# group_label (for Explores)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-group-label/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  group_label (for Explores) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `group_label` parameter that is part of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore).
> 
> `group_label` can also be used as part of a field, as described on the [`group_label` (for fields)](https://docs.cloud.google.com/looker/docs/reference/param-field-group-label) parameter documentation page.

## Usage
    
    
    explore: explore_name {
      group_label: "Label to Use as a Heading in the Explore Menu"
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `group_label` |  Default Value With no `group_label` defined, Explores are grouped by model, with each word capitalized and underscores replaced by spaces Accepts A string   
---|---  
  
## Definition

Use `group_label` to change the default organization of the [Explore menu](https://docs.cloud.google.com/looker/docs/changing-explore-menu-and-field-picker). The `group_label` parameter specifies the label to use as a heading in the Explore menu for this [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore).

Instead of each Explore being listed under its model's name, you can list an Explore under a new group label or under another model's name. Adding the same `group_label` to multiple Explores will list all of those Explores under the same heading in the Explore menu. You can use `group_label` to group Explores together even if they are defined in different projects.

If you use the name of another model as the value for an Explore's `group_label` parameter, then the Explore will be listed with any Explores that are part of that model. If you specify a value for the `group_label` parameter that does not correspond to a model name, Looker adds that new label as a heading in the Explore menu.

## Example

Create a group heading in the Explore menu called **Online Store Queries** and list the **Customers** Explore under that heading in the Explore menu:
    
    
    explore: customers {
      group_label: "Online Store Queries"
    }
    

By adding the group label to two different Explores, you can group them together under the **Online Store Queries** label. In the following sample LookML, the `group_label` parameter is used with the `order_items` Explore and the `inventory` Explore:
    
    
    explore: order_items {
      label: "Order Items"
      description: "Based on the individual items that compose customer orders"
      group_label: "Online Store Queries"
      ...
    }
    
    explore: inventory {
      group_label: "Online Store Queries"
      ...
    }
    

The **Order Items** and **Inventory** Explores will then be listed under the **Online Store Queries** label in the Explore menu.

## Things to know

### `group_label` has no effect other than changing the Explore menu appearance

When you change the `group_label` of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore), this only affects the Explore's heading in the Explore menu. To change the display name of the Explore itself, use the [`label`](https://docs.cloud.google.com/looker/docs/reference/param-explore-label) parameter.

The way that fields should be referenced in the LookML goes unchanged. The way that fields appear within the Explore UI is also unchanged.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
