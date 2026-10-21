---
url: https://docs.cloud.google.com/looker/docs/best-practices/best-practices-lookml-dos-and-donts/
title: Best practice: What to do and what not to do with LookML \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:31:03.885761+00:00
---

# Best practice: What to do and what not to do with LookML  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/best-practices-lookml-dos-and-donts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Best practice: What to do and what not to do with LookML Stay organized with collections  Save and categorize content based on your preferences. 

These best practices reflect recommendations that were shared by a cross-functional team of seasoned Lookers. These insights come from years of experience working with Looker customers from implementation to long-term success. The practices are written to work for most users and situations, but — as always — use your best judgment when implementing any of the recommendations that are shared on this page. 

## Do this with LookML

  * **Do** : Define the [`relationship`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-relationship) parameter for all joins. 

This will ensure that metrics aggregate properly within Looker. By default, Looker will use a `many_to_one` join relationship for any joins in which a relationship is not defined. For additional information on defining the `relationship` parameter correctly, see the Best Practices page on [getting the `relationship` parameter right](https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-the-relationship-parameter-correctly). 
  * **Do** : Define a [primary key](https://docs.cloud.google.com/looker/docs/reference/param-field-primary-key) within each and every view, including derived tables. 

All views, whether they are derived or coming directly from the database, should contain a primary key. This primary key should be a _unique value_ to enable Looker to uniquely identify any given record. This primary key can be a single column or a concatenation of columns — it simply needs to be a unique identifier for the table or derived table. 
  * **Do** : Name [dimensions](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension), [measures](https://docs.cloud.google.com/looker/docs/reference/param-field-measure), and other LookML objects, using all lowercase letters and underscores for spaces. 

The [`label` parameter](https://docs.cloud.google.com/looker/docs/reference/param-field-label) can be used for additional formatting of a name field, and can also be used to customize the appearance of [view names](https://docs.cloud.google.com/looker/docs/reference/param-view-label), [Explore names](https://docs.cloud.google.com/looker/docs/reference/param-explore-label), and [model names](https://docs.cloud.google.com/looker/docs/reference/param-model-label). For example, in the following LookML, the `label` parameter is used to assign the label **Number of Customers** to the `customer_count_distinct` measure. 
        
        measure: customer_count_distinct {
                label: "Number of Customers"
                type: count_distinct
                sql: ${customer.id} ;;
              }

  * **Do** : Use [datagroups](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup) to align generation of [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/caching-and-datagroups) and Explore caching with underlying ETL processes. Datagroups can also be used to trigger deliveries of [dashboards](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#schedules_triggered_by_datagroup_updates) or [Looks](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#specifying_the_datagroup_trigger) to ensure that up-to-date data is sent to recipients. 



## Don't do this with LookML

  * **Don't** : Use the `from` parameter for renaming views within an Explore. 

Use the [`view_label`](https://docs.cloud.google.com/looker/docs/reference/param-explore-view-label) parameter instead. For more on the difference between `from` and `view_label`, check out the [`from` (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-from) parameter documentation page. The `from` parameter should primarily be used in the following situations: 
    * Polymorphic joins (joining the same table multiple times) 
    * [Self-joins](https://docs.cloud.google.com/looker/docs/working-with-joins#joining_a_view_more_than_once) (joining a table to itself) 
    * Re-scoping an extended view back to its original view name 
  * **Don't** : Use the word "date" or "time" in a [dimension group](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) name. 

Looker appends each timeframe to the end of the dimension group name, which means that a dimension group that is named `created_date` results in fields called, for example, `created_date_date` and `created_date_month`. Simply use `created` as the dimension group name, because this results in fields that are named, for example, `created_date` and `created_month`. 
  * **Don't** : Use formatted timestamps within joins. 

Instead, use the [raw timeframe](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#timeframes) option for joining on any date or time fields. This will avoid the inclusion of casting and timezone conversion in join predicates. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
