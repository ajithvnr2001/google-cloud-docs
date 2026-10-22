---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-a-positive-experience-for-looker-users/
title: Best practice: Create a positive experience for Looker users \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:15.761544+00:00
---

# Best practice: Create a positive experience for Looker users  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-a-positive-experience-for-looker-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Best practice: Create a positive experience for Looker users Stay organized with collections  Save and categorize content based on your preferences. 

_These best practices reflect recommendations shared by a cross-functional team of seasoned Lookers. These insights come from years of experience working with Looker customers, from implementation to long-term success. The practices are written to work for most users and situations, but you should use your best judgment when implementing._

LookML developers can consider following these tips to improve their users' experience with Looker: 

  * Provide users with meaningful field names
  * Group similar fields together for easier navigation
  * Avoid exposing too much to users initially
  * Add descriptions so users know which fields and Explores to use
  * Build common workflows into Looker



These recommendations are explained in further detail in the sections that follow. 

## Provide users with meaningful field names

  * Use the [`label`](https://docs.cloud.google.com/looker/docs/reference/param-field-label) parameter to apply user-friendly names to dimensions or measures while maintaining database-friendly names within the view and model files. You might consider renaming a couple of common terms, like **Count** to **Number of** and **Sum** to **Total**. If you aren't sure which words are meaningful to users, work with a business user to build some common queries, and see what words the query results use to describe what users are looking for. As an example, suppose the **Inventory Items** , **Order Items** , **Orders** , and **Products** views each have a measure called **Count**. You can use the `label` parameter to give each of these measures a unique and meaningful name, such as **Number of Inventory Items** , **Number of Order Items** , **Number of Orders** , and **Number of Products**. 
  * Avoid exposing multiple fields with the same name. For example, measures of `type: count` are automatically created within Looker with the name **Count**. This results in most view files containing a count measure with the same name. Multiple fields with the same name can confuse users. Adding labels or renaming count measures to indicate the object that is being counted will prevent confusion. Other fields to keep in mind include **Created Date** and **Updated Date** , such as in [dimension groups](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group). 
  * Provide clear names for fields of [`type: yesno`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#yesno). For example, use **Was the Item Returned?** instead of **Returned** to name a field that indicates whether an item has been returned. 
  * Name ratios descriptively. For example, **Orders Per Purchasing Customers** is clearer than **Orders Percent**. 
  * Name fields and represent values consistently across the model. Using the [`value_format`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format) or [`value_format_name`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format-name) parameter to apply formatting such as currency symbols, percentages, and decimal precision to numerical fields will help make everything clearer to your users. 



## Group similar fields together for easier navigation

  * Use the [`group_label`](https://docs.cloud.google.com/looker/docs/reference/param-field-group-label) parameter to consolidate dimensions and measures from individual or multiple joined views that are related. For example, group all geographic information into a **Geography** group to pull all address and location information together within the field picker, rather than having it all listed alphabetically: 
        
        dimension: city {
              group_label: "Geography"
              type: string
              sql: ${TABLE}.city ;;
            }
        
            dimension: country {
              group_label: "Geography"
              type: string
              map_layer_name: countries
              sql: ${TABLE}.country ;;
            }
            

![The City and Country dimensions are grouped under the label Geography in the field picker.](https://docs.cloud.google.com/static/looker/docs/images/hc-positive-experience-group-label-2210.png)

  * Break up large, denormalized tables using the [`view_label`](https://docs.cloud.google.com/looker/docs/reference/param-field-view-label) parameter. Utilize the `view_label` parameter within fields to group fields together logically into separate headings within the field picker. Large, denormalized tables with a lot of fields can be difficult to navigate, so this gives the illusion of multiple views in the left-hand Explore field picker. 



## Avoid exposing too much to users initially

  * Avoid exposing too much to users upon an initial Looker roll-out. Start small, and then expand the options. You don't have to expose all the tables or dimensions and measures at once. You can expose the most important fields at first and then continue to build in more functionality as business users become more confident with data exploration. 
  * Hide dimensions that are not relevant to users from the user interface. Use the [`hidden`](https://docs.cloud.google.com/looker/docs/reference/param-field-hidden) parameter on dimensions that will never be used through the user interface (such as ID fields or database update dates). 
  * Use the [`fields`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-fields) parameter within Explores and joins to limit the number of fields that are available to users. Included fields should be only those relevant to the Explore. This reduces bloat and provides a better experience for users. Unlike the `hidden` parameter, the `field` parameter enables fields to be included or excluded on an Explore-by-Explore basis. 
  * Hide any Explores that exist solely for populating specific Looks, dashboard tiles, or filters using the [`hidden` parameter for Explores](https://docs.cloud.google.com/looker/docs/reference/param-explore-hidden). Explores that are not meant for exploration by users should be hidden from the user interface. 
  * Use the fewest number of Explores possible while still allowing users to easily get access to the answers they need. Consider splitting out Explores into different models for different audiences to [limit the options available for each user group](https://docs.cloud.google.com/looker/docs/access-control-and-permission-management#controlling_feature_and_data_access). The optimal number of Explores is different for every business, but having too many Explores tends to confuse users. Consider using the [`group_label`](https://docs.cloud.google.com/looker/docs/reference/param-explore-group-label) parameter for Explores within a model, which will let you group them in a sensible way within the **Explore** drop-down menu. 



## Add descriptions so users know which fields and Explores to use

  * Use the [`description`](https://docs.cloud.google.com/looker/docs/reference/param-field-description) parameter on dimensions and measures to provide additional information to users about the logic or calculations that are used within the model. This is particularly important for dimensions and measures that leverage complex logic or calculations. That being said, it's a good idea to also consider descriptions for simpler fields to be sure that users understand the definitions behind them. 
  * Define [Explore descriptions](https://docs.cloud.google.com/looker/docs/reference/param-explore-description) for users. Add a short description to each Explore to specify the purpose of the Explore and the audience who will use it. 



## Build common workflows into Looker

  * Add [`drill_fields`](https://docs.cloud.google.com/looker/docs/reference/param-field-drill-fields) to all relevant measures. Drill fields enable users to click into aggregate values in order to access detailed data. Use the [`set`](https://docs.cloud.google.com/looker/docs/reference/param-view-set) parameter to create reusable sets of fields that can then be applied to any number of measures within a view. 
  * Add [`drill_fields`](https://docs.cloud.google.com/looker/docs/reference/param-field-drill-fields) to all hierarchical dimensions. For example, adding a `drill_field` for **City** into a **State** dimension will let users select a state and then drill deeper into the cities within that state. Note that this hierarchical drilling will automatically be applied within time dimension groups. 
  * Set up links that enable users to easily navigate and pass filters to other Looker dashboards or to systems or platforms that are external to Looker. See our [ documentation on the `link` parameter](https://docs.looker.com/reference/field-params/link?lookml=new#passing_a_querys_filter_values_into_a_link) for examples of passing filters through drills. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
