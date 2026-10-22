---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-liquid-in-labels/
title: Interesting ways to use Liquid in labels \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:09.991505+00:00
---

# Interesting ways to use Liquid in labels  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-liquid-in-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Interesting ways to use Liquid in labels Stay organized with collections  Save and categorize content based on your preferences. 

This page highlights useful ways to use Looker's [`parameter` field](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter) with some of the `label` subparameters that accept Liquid variables.

The examples on this page require an understanding of Liquid. To learn about using Liquid in Looker, visit our [Liquid variable reference](https://docs.cloud.google.com/looker/docs/liquid-variable-reference) documentation page.

##  Using `view_label` for dynamic view names 

Looker's `view_label` parameter is used for grouping dimensions together under a more contextual, user-friendly name in the Explore field picker. To learn more about view labels, visit the [`view_label` (for fields)](https://docs.cloud.google.com/looker/docs/reference/param-field-view-label) documentation page. 

Assigning the same `view_label` to dimensions simplifies Explores for users. Clear, descriptive groups of fields ensure that users can find the data that they need. 

###  Example: Writing DRY (don't repeat yourself) code with a Liquid `view_label`

For example, say you have fields that are organized under the `view_label` "Finance & Accounting" in an Explore called **Inventory Items** : 
    
    
    dimension: cost {
      view_label: "Finance & Accounting"
      type: number
      sql: ${TABLE}.COST ;;
    }
    
    
    
    dimension: cost_ex_vat {
      view_label: "Finance & Accounting"
      type: number
      sql: ${TABLE}.COST_EX_VAT ;;
    }
    
    
    
    dimension: cost_eur {
      view_label: "Finance & Accounting"
      type: number
      sql: ${TABLE}.COST_EUR ;;
    }
    

What if you wanted to change the `view_label` "Finance & Accounting" to "The Money Zone" for users? Using Liquid can prevent repetitive rewriting of code. 

You can create a type of pseudo-variable of the desired view name, using Looker's `parameter` field. Once you change the view name in the `parameter`, all the fields will update. 
    
    
    parameter: view_label {
      type: string
      default_value: "The Money Zone"
    }
    
    dimension: cost {
      view_label: "{% parameter view_label %}"
      type: number
      sql: ${TABLE}.COST ;;
    }
    
    
    
    dimension: cost_ex_vat {
      view_label: "{% parameter view_label %}"
      type: number
      sql: ${TABLE}.COST_EX_VAT ;;
      }
    
    
    
    dimension: cost_eur {
      view_label: "{% parameter view_label %}"
      type: number
      sql: ${TABLE}.COST_EUR ;;
    }
    

![Inventory Items Explore field picker showing Cost, Cost Eur, and Cost Ex Vat organized under the view label 'The Money Zone'.](https://docs.cloud.google.com/static/looker/docs/images/hc-liquid-view-label-2214.png)

**Note:** If you don't want the quotation marks to appear in the menu, `parameter` must be set as `type:unquoted`, and the `default_value` _must_ be a string without spaces, for example, `The_Money_Zone`. If the parameter is `type:string`, the quotation marks will appear. 

##  Dynamic field labels 

You may have multiple groups of users who might interpret a field's name differently. For example, some users could refer to a gross margin an _operating margin_ , and other users could refer to a gross margin as a _standard margin_ , depending on their use case. 

The name of a field can look different for different users according to how you combine [user attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) and [Liquid variables](https://docs.cloud.google.com/looker/docs/liquid-variable-reference). 

###  Example: Different labels for different user attributes 

Extrapolating on the previous example, you can accommodate differences in business logic by making the **Gross Margin** field appear as **Standard Margin** for some users and **Operating Margin** for other users. The following LookML leverages user attributes and Liquid variables. 
    
    
    dimension: gross_margin {
      label: "{% if _user_attributes['customer'] == 'A' %} Standard Margin
        {% elsif _user_attributes['customer'] == 'B' %} Operating Margin
        {% else %} Gross Margin
        {% endif %}"
      type: number
      value_format_name: usd
      sql: ${sale_price} - ${inventory_items.cost} ;;
    }
    

Based on the LookML, the field **Gross Margin** appears as **Operating Margin** in an Explore field picker for **User A**.

![](https://docs.cloud.google.com/static/looker/docs/images/hc-liquid-label-a-2214.png)

Based on the LookML, the field **Gross Margin** appears as **Standard Margin** in an Explore field picker for **User B**. 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-liquid-label-b-2214.png)

This pattern can also be used to create low-level localization on a user-by-user basis, as demonstrated in the next example. 

###  Example: Customized field names for multiple Explores 

This example combines the techniques from the previous examples to create an Explore with field labels that vary depending on a user's region. 

In this example, there are two regional teams — Finance East and Finance West — that use an Explore called **Company Sales**. Both teams need to use the **Total Profit** and **Total Revenue** measures in their queries: 
    
    
    measure: total_profit {
      label: "{{ _explore._name}}: Profit"
      type: sum
      sql: ${profit} ;;
    }
    
    
    
    measure: total_revenue {
      label: "{{ _explore._name}}: Revenue"
      type: sum
      sql: ${sale_price} ;;
      value_format_name: usd
    }
    

However, each team would like the field name to reflect their team's region. 

Developers can make the field names look one way to users on Finance East and another way to users on Finance West. They can do this with DRY LookML by using the following Liquid parameters: 

* The [`from`](https://docs.cloud.google.com/looker/docs/reference/param-explore-from) parameter specifies the underlying view for the Explores. 
* The[`explore_label`](https://docs.cloud.google.com/looker/docs/reference/param-explore-label) is used to display the same name for the two aliased Explores ("Company Sales") to create an otherwise identical exploring experience for both teams. 
* The labels of the measures can be changed according to a team's region by leveraging the [`{{ _explore._name}}`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#liquid_variable_definitions) Liquid variable, which will capture and display the Explore name. 

**The Explores:**
    
    
    explore: Finance_East{
      from: order_items
      label: "Company Sales"
      view_label: "The Money Zone"
    }
    
    
    
    explore: Finance_West{
      from: order_items
      label: "Company Sales"
      view_label: "The Money Zone"
    }
    

When exploring, the Finance East team will see the field **Total profit** as **Finance_East: Profit** and the field **Total Revenue** as **Finance_East: Revenue**. 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-liquid-label-east-2214.png)

When exploring, the Finance West team will see the field **Total profit** as **Finance_West: Profit** and the field **Total Revenue** as **Finance_West: Revenue**. 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-liquid-label-west-2214.png)

For additional ways to customize how fields appear to users, visit the [Changing the Explore menu and field picker](https://docs.cloud.google.com/looker/docs/changing-explore-menu-and-field-picker) documentation page. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
