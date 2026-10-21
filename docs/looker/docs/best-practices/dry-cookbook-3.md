---
url: https://docs.cloud.google.com/looker/docs/best-practices/dry-cookbook-3/
title: Maximizing code reusability with DRY LookML: Defining reusable measures for complex calculations \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:34.234880+00:00
---

# Maximizing code reusability with DRY LookML: Defining reusable measures for complex calculations  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/dry-cookbook-3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Maximizing code reusability with DRY LookML: Defining reusable measures for complex calculations Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page is part of the [Looker cookbook: Maximizing code reusability with DRY LookML](https://docs.cloud.google.com/looker/docs/best-practices/dry-lookml-cookbook).

When you're defining complex calculations in LookML, it can be helpful to break them down into intermediate steps that involve simpler calculations. By creating intermediate measures, you make your calculations more readable, easier to maintain, and less error-prone, since you only need to ensure that each intermediate calculation is correct in one place.

This page provides an example of how you can make your calculations in LookML more readable and maintainable by defining intermediate measures to break complex calculations into smaller, more manageable steps.

## Ingredients

  * The LookML [`measure`](https://docs.cloud.google.com/looker/docs/reference/param-field-measure) parameter
  * The [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameter of a measure
  * A measure of [`type: sum`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum)
  * A measure of [`type: number`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#number)
  * The LookML [`hidden`](https://docs.cloud.google.com/looker/docs/reference/param-field-hidden) parameter (for fields)



## Prerequisites

  * [A configured LookML model](https://docs.cloud.google.com/looker/docs/generating-a-model#when_you_need_to_configure_models)
  * [Permissions to develop LookML](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permission_sets)



## Example: Breaking a complex calculation into intermediate measures

Suppose you have a company that sells products online, and you want to define measures to calculate total profit and shareholder dividends. One way to do this would be to define two measures: a `total_profit` measure and a `shareholder_dividends` measure, as follows:
    
    
    measure: total_profit {
      type: number
      sql: SUM(${orders.sale_price}) - SUM(${employees.salary}) - SUM(${products.cost}) ;;
    }
    
    measure: shareholder_dividends
      description: "We give shareholders 60% of our total profits."
      type: number
      sql: 0.6 * (SUM(${orders.sale_price}) - SUM(${employees.salary}) - SUM(${products.cost})) ;;
    
    

In this example, the calculation `SUM(${orders.sale_price}) - SUM(${employees.salary}) - SUM(${products.cost})` is reused in the `sql` parameter for both measures. If you need to update the definition of this calculation, such as to correct an error, you would have to update the calculation manually for both measures.

You can make these measure definitions easier to maintain by reusing the `total_profit` measure within the calculation in the `shareholder_dividends` measure:
    
    
    measure: total_profit {
      type: number
      sql: SUM(${orders.sale_price}) - SUM(${employees.salary}) - SUM(${products.cost}) ;;
    }
    
    measure: shareholder_dividends
      description: "We give shareholders 60% of our total profits."
      type: number
      sql: 0.6 * ${total_profit} ;;
    
    

You may want to break the calculation in `total_profit` into even simpler measures that can be reused in other calculations. For example, you can create measures of `type: sum` called `total_sales`, `total_revenue`, `total_cost`, and `total_salary`:
    
    
    measure: total_sales {
      hidden: yes
      type: sum
      sql: ${orders.sale_price} ;;
    }
    
    measure: total_revenue {
      hidden: yes
      type: number
      sql: ${total_sales} ;;
    }
    
    measure: total_cost {
      hidden: yes
      type: sum
      sql: ${products.cost} ;;
    }
    
    measure: total_salary {
      hidden: yes
      type: sum
      sql: ${employees.salary} ;;
    }
    
    

**Note:** You can set the `hidden` parameter to `yes` to hide intermediate fields that you don't want to surface in the Explore UI for users.

You can then reuse the intermediate fields you have defined as follows:
    
    
    measure: total_expenses {
      type: number
      sql: ${total_cost} + ${total_salary} ;;
    }
    
    measure: total_profit {
      type: number
      sql: ${total_revenue} - ${total_expenses} ;;
    }
    
    measure: shareholder_dividends {
      description: "We give shareholders 60% of our total profits."
      type: number
      sql: 0.6 * ${total_profit} ;;
    }
    
    

Although you have defined more measures, these intermediate measures can be reused within other calculations, and it will be easier correct a mistake or make any changes to calculations that are used in multiple measures.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
