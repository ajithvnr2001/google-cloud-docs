---
url: https://docs.cloud.google.com/looker/docs/best-practices/dry-cookbook-5/
title: Maximizing code reusability with DRY LookML: Customizing a single base view for multiple use cases \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:34.291816+00:00
---

# Maximizing code reusability with DRY LookML: Customizing a single base view for multiple use cases  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/dry-cookbook-5/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Maximizing code reusability with DRY LookML: Customizing a single base view for multiple use cases Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page is part of the [Looker cookbook: Maximizing code reusability with DRY LookML](https://docs.cloud.google.com/looker/docs/best-practices/dry-lookml-cookbook). 

This is an advanced topic that assumes that the reader has a solid knowledge of LookML. 

Imagine that you have many users who share one Explore but who have different use cases depending on their team or region. Each user wants to see only the fields that apply to their unique use cases. To cater to the diverse needs of your users, you can use [LookML refinements](https://docs.cloud.google.com/looker/docs/lookml-refinements) to customize existing views and Explores without having to modify the original LookML. You can then include these refined views and Explores in separate, dedicated model files that are customized to your users' different needs.

This page provides an example of using LookML refinements to customize a single base view and create distinct Explores for two different teams within your company. It also includes examples of hiding and adding fields in refined content.

## Ingredients

  * LookML [views](https://docs.cloud.google.com/looker/docs/reference/param-view)
  * LookML [Explores](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore)
  * LookML [model files](https://docs.cloud.google.com/looker/docs/lookml-project-files#model_files)
  * [LookML refinements](https://docs.cloud.google.com/looker/docs/lookml-refinements)
  * [Generic LookML files](https://docs.cloud.google.com/looker/docs/lookml-project-files#refinements_files) for housing refinements
  * The LookML [`include`](https://docs.cloud.google.com/looker/docs/reference/param-model-include) parameter
  * The LookML [`hidden`](https://docs.cloud.google.com/looker/docs/reference/param-field-hidden) parameter (for fields)
  * Optionally, [model access](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets) to specific models for viewers, configured by a Looker admin



## Prerequisites

  * [A configured LookML model](https://docs.cloud.google.com/looker/docs/generating-a-model#when_you_need_to_configure_models)
  * [Permissions to develop LookML](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permission_sets)
  * Experiencing developing models in LookML, including familiarity with more advanced LookML concepts like [refinements](https://docs.cloud.google.com/looker/docs/lookml-refinements) and [extends](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends)



## Example: Creating multiple customized Explores from the same base view

Suppose you have a **Sales** Explore that contains data about customers, purchases, shipping, and location. Your company's Marketing and Logistics teams both need to explore this data, but they each focus on different fields within the **Sales** Explore.

You want to display only the fields that are useful to each team in the Explore field picker to make exploring easier. To do this, you can define two different refinements of the **Sales** Explore and the `sales` view that it is based on. The Marketing team's Explore can show fields that are related to customers and purchasing trends, while the Logistics team's Explore can show fields that are related to shipping and location. You can also add new fields to each refined view that are specific to each team's needs.

Currently, the field picker for the **Sales** Explore displays all the fields from the **Sales** view:

![The Sales view includes fields for created, delivered, returned, and shipped date, as well as ID, profit, status, average and total sale price, and count.](https://docs.cloud.google.com/static/looker/docs/images/dry-cookbook-refinement-field-picker-example-sales-2304.png)

The field picker also displays all the fields from the joined **Users** view:

![The Users view includes fields for age, city, country, created date, email, first and last name, ID, state, zip, and count.](https://docs.cloud.google.com/static/looker/docs/images/dry-cookbook-refinement-field-picker-example-users-2304.png)

You can refine the `sales` view to create two separate Explores that contain only the fields that are of interest to the Marketing and Logistics teams by following these steps:

  1. Create a new LookML file, in this example a file called `base_analysis.lkml`, that contains the LookML for the **Sales** Explore, which is based on the `sales` view and the joined `users` view. Since you want to use the base `sales` Explore and its corresponding views to create a customized Explore for each team, you can define all the shared fields and properties in a single location, such as within a single file.

**Note:** Since you can't include a model file within another model file, you can add the `sales` Explore declaration in a generic LookML file with the file extension `.lkml` and then include that file in multiple models, as well as in any files where refinements of the `sales` Explore are defined.
         
         # base_analysis.lkml
         
         include: "views/sales.view.lkml"
         include: "views/inventory_items.view.lkml"
         include: "views/users.view.lkml"
         
         explore: sales {
           join: inventory_items {
             type: left_outer
             sql_on: ${sales.inventory_item_id} = ${inventory_items.id} ;;
             relationship: many_to_one
           }
         
           join: users {
             type: left_outer
             sql_on: ${sales.user_id} = ${users.id} ;;
             relationship: many_to_one
           }
         }
         

  2. Create two separate files to house the refinements of the **Sales** Explore that you will define for each team. You can name the files `marketing_analysis.lkml` and `logistics_analysis.lkml`. The LookML code, shown next, refines the base `sales` Explore as defined in the `base_analysis.lkml` file, shown previously, to add the label **Sales Analysis for Marketing Team** within a new file called `marketing_analysis.lkml`. The statement `include: "/base/base_analysis.lkml"` makes the contents of the `base_analysis.lkml` file available to reference within the `marketing_analysis.lkml` file.
         
         # marketing_analysis.lkml
         
         include: "/base/base_analysis.lkml"
         
         explore: +sales {
           label: "Sales Analysis for Marketing Team"
         }
         
         

**Note:** Refinements can be placed within any LookML file in a project, such as a model file or a view file, or in its own dedicated LookML file. See the Using refinements in your LookML project section for how it works.
  3. Create a separate model file for each team, such as `ecommerce_marketing.model` and `ecommerce_logistics.model`. By housing the different refinements in separate dedicated models for each team, you can refine the same set of views and Explores multiple times without overwriting the customizations you have made for one team's use case. See the [LookML refinements](https://docs.cloud.google.com/looker/docs/lookml-refinements#refinements_override_parameters) documentation page for more information.

  4. With the [`include`](https://docs.cloud.google.com/looker/docs/reference/param-model-include) parameter, include `marketing_analysis.lkml` in the `ecommerce_marketing.model` model, and include `logistics_analysis.lkml` within the `ecommerce_logistics.model` model.

  5. Add any additional refinements to the `marketing_analysis.lkml` and `logistics_analysis.lkml` files as desired. For example, you can hide unnecessary fields  and add new fields to the refined Explores for each team.




You can optionally have a Looker admin configure [model access](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets) for each dedicated model to provide specific teams with Explore-level access.

### Hiding unnecessary fields from the refined Explores

You can refine the `sales` view as follows in the `marketing_analysis.lkml` file to hide the **Returned** , **Shipped** , **Delivered** , and **Created** dimension groups, as well as the **Status** dimension, since those fields are not used by the Marketing team:
    
    
    # marketing_analysis.lkml
    
    include: "/base/base_analysis.lkml"
    
    explore: +sales {
      label: "Sales Analysis for Marketing Team"
    }
    
    view: +sales
      dimension_group: returned {
        hidden: yes
      }
    
      dimension_group: shipped {
        hidden: yes
      }
    
      dimension_group: delivered {
        hidden: yes
      }
    
      dimension_group: created {
        hidden: yes
      }
    
      dimension: status {
        hidden: yes
      }
    }
    
    

Similarly, you can use the following LookML in the `logistics_analysis.lkml` file to hide fields that the Logistics team doesn't need (like **Profit** , **Sale Price** , and **Average Sale Price**):
    
    
    # logistics_analysis.lkml
    
    include: "/base/base_analysis.lkml"
    
    explore: +sales {
      label: "Sales Analysis for Logistics Team"
    }
    
    view: +sales {
      dimension: profit {
        hidden: yes
      }
    
      dimension: sale_price {
        hidden: yes
      }
    
      measure: average_sale_price {
        hidden: yes
      }
    }
    

Since the Logistics team has no need to see personal information about customers, such as their names, ages, or email addresses, you can also add a refinement for the joined `users` view within the `logistics_analysis.lkml` file to hide these fields from the Explore:
    
    
      view: +users {
        dimension: age {
        hidden: yes
      }
    
      dimension: email {
        hidden: yes
      }
    
      dimension: first_name {
        hidden: yes
      }
    
      dimension: last_name {
        hidden: yes
      }
    
      dimension_group: created {
        hidden: yes
      }
    }
    

### Adding new fields to the refined Explores

You can also create new fields that are of interest to the Marketing team within the refined `sales` view. For example, you can add fields for **Average Sale Price** , **Total Sale Price** , and **Average Spend per User** within the refined `sales` view:

![The Sales view lists ID, Profit, Sale Price, and Count, plus the new Average Sale Price, Average Spend per User, and Total Sale Price fields.](https://docs.cloud.google.com/static/looker/docs/images/dry-cookbook-refinement-field-picker-refined-marketing-2304.png)

You can use the following LookML to add these fields to the refined `sales` view in the `marketing_analysis.lkml` file:
    
    
    # marketing_analysis.lkml
    
    view: +sales {
      measure: average_sale_price {
        type: average
        value_format_name: usd
        sql: ${sale_price} ;;
        drill_fields: [detail*]
      }
    
      measure: total_sale_price {
        type: sum
        value_format_name: usd
        sql: ${sale_price} ;;
        drill_fields: [detail*]
      }
    
      measure: average_spend_per_user {
        type: number
        value_format_name: usd
        sql: 1.0 * ${total_sale_price} / NULLIF(${users.count},0) ;;
        drill_fields: [detail*]
      }
    }
    
    

The Marketing Explore you created will contain the new fields under the **Sales** view in addition to the fields in the joined **Users** view. The **Returned** , **Shipped** , **Delivered** , and **Created** dimension groups and the **Status** dimension are hidden since the Marketing team doesn't need them.

Similarly, for the Logistics team, you can create new fields that will be useful to the Logistics team, such as **Shipping Time Buckets** and **Average Shipping Time** :

![The Logistics team Explore now lists the new Shipping Time Buckets and Average Shipping Time fields, along with other shipping and user location fields.](https://docs.cloud.google.com/static/looker/docs/images/dry-cookbook-refinement-field-picker-refined-logistics-2304.png)

You can use the following LookML to add these fields to the refined `sales` view in the `logistics_analysis.lkml` file:
    
    
    # logistics_analysis.lkml
    
    view: +sales {
      dimension: shipping_time_buckets {
        case: {
          when: {
            sql: ${shipping_time} <= 7 ;;
            label: "One Week"
          }
          when: {
            sql: ${shipping_time} > 7 AND ${shipping_time} <= 14 ;;
            label: "Two Weeks"
          }
          when: {
            sql:  ${shipping_time} > 14 ;;
            label: "Over Two Weeks"
          }
          else: "Note Shipped"
        }
      }
    
      measure: average_shipping_time {
        type: average
        value_format_name: decimal_4
        sql: ${shipping_time} ;;
      }
    }
    

The Logistics Explore you created will contain the new fields under the **Sales** view in addition to the fields in the joined **Users** view. The **Profit** , **Sale Price** , and **Average Sale Price** fields from the **Sales** view and the **Age** , **Email** , **First Name** , **Last Name** , and **Created** fields from the **Users** Explore are hidden since the Logistics team doesn't need them.

Each team now has an Explore that is more tailored to their specific needs. While this approach involves a bit more setup upfront, by keeping the core data in one place, you can make it easier to find and use.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
