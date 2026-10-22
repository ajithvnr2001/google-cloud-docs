---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-when-measures-dont-come-through-a-join/
title: Why aren't my measures coming through a join? \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:16.784714+00:00
---

# Why aren't my measures coming through a join?  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-when-measures-dont-come-through-a-join/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Why aren't my measures coming through a join? Stay organized with collections  Save and categorize content based on your preferences. 

You have defined some measures in a view — but when you join that view to another view you no longer see the measures in an Explore. Where did the measures go? 

## Possible causes and solutions

The possible underlying causes can depend on whether you have [symmetric aggregates](https://docs.cloud.google.com/looker/docs/best-practices/understanding-symmetric-aggregates) enabled. Symmetric aggregates are automatically enabled unless your developer has disabled them with the [`symmetric_aggregates: no`](https://docs.cloud.google.com/looker/docs/reference/param-explore-symmetric-aggregates) LookML setting or if your database dialect [does not support symmetric aggregates](https://docs.cloud.google.com/looker/docs/reference/param-explore-symmetric-aggregates#dialect_support_for_symmetric_aggregates). 

### When symmetric aggregates are enabled

Symmetric aggregates let measures of all types carry through joins. However, this is only possible if there are primary keys defined in the views on both sides of a join. To enable measures to carry through joins, you need to define a primary key in all involved views. 

You can define a primary key in each view by adding `primary_key: yes` to the [primary key field](https://docs.cloud.google.com/looker/docs/reference/param-field-primary-key) definition, like so: 
    
    
    dimension: id {
     type: number
     primary_key: yes
    }
    

Primary keys must have completely unique, non-`NULL` values for measure types [`sum`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum) and [`average`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#average) to carry through joins. If your primary key is not unique, you might receive an error like the following: 
    
    
    Non-Unique value/primary key (or sql_distinct_key), value overflow or collision when computing sum.

Additionally, if you are in a situation where there is not a single unique field in your view, you can make a compound primary key by concatenating together two or more fields in SQL to create a unique combination of values. Read more about how to resolve this error in the [Non-unique primary key section](https://docs.cloud.google.com/looker/docs/best-practices/error-non-unique-primary-key-computing-sum#non-unique-primary-key) of the [`Error: Non-Unique value/primary key (or sql_distinct_key), value overflow or collision when computing sum`](https://docs.cloud.google.com/looker/docs/best-practices/error-non-unique-primary-key-computing-sum) Best Practices page. 

### When symmetric aggregates are not enabled

Some dialects don't support symmetric aggregates, or your Looker developer has disabled symmetric aggregates with the [`symmetric_aggregates: no`](https://docs.cloud.google.com/looker/docs/reference/param-explore-symmetric-aggregates) LookML setting. When symmetric aggregates cannot be used, Looker will only carry [`count`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count) type measures (which become count distinct measures) through a join by default. This approach also requires a primary key, because the count distinct will use the primary key. This prevents inaccurate results and fanouts. Check out the Community post about [aggregate functions gone bad](https://www.googlecloudcommunity.com/gc/Technical-Tips-Tricks/Aggregate-functions-gone-bad-and-the-joins-who-made-them-that/ta-p/588767). 

There is a list that shows [which dialects support symmetric aggregates](https://docs.cloud.google.com/looker/docs/reference/param-explore-symmetric-aggregates#dialect_support_for_symmetric_aggregates) in the most recent Looker release. 

### Additional solutions to consider

  * The use of [`fields` (for joins)](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-fields) at the join level. `fields` lets you specify which fields (measures, dimensions) from a joined view appear in an Explore. 
  * Choosing the correct [ `relationship` parameter](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-relationship). The `relationship` parameter tells Looker whether to apply symmetric aggregates when the join is used in a SQL query. It's important to properly define the type of relationship to allow Looker to calculate accurate measure values. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
