---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-dimensionalize-a-measure/
title: How to dimensionalize a measure in Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:35.399186+00:00
---

# How to dimensionalize a measure in Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-dimensionalize-a-measure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  How to dimensionalize a measure in Looker Stay organized with collections  Save and categorize content based on your preferences. 

As a general rule in SQL — and, by extension, Looker — you cannot group a query by the results of an aggregate function (represented in Looker as [measures](https://docs.cloud.google.com/looker/docs/reference/param-field-measure)). You can only group by unaggregated fields (represented in Looker as [dimensions](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension)). If you try to aggregate a measure in Looker, you will see the following [error](https://docs.cloud.google.com/looker/docs/best-practices/error-measures-with-looker-aggregations-reference-other-aggregations): 
    
    
    Measures with Looker aggregations (sum, average, min, max, list types) may not reference other measures.
    

What if you need a way to change a measure (COUNT, SUM, AVG, MAX, etc.) into a dimension, so that you can group by it to aggregate it (like a SUM of a COUNT or an AVG of a SUM), [filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting) by it (in the WHERE clause rather than a [HAVING](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#filtering_measures:_calculates_first,_then_restricts_the_results) clause), or [pivot](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#pivoting_dimensions) on it in an Explore? 

## Using derived tables to dimensionalize a measure

Internally at Looker the solution is called _dimensionalizing a measure_. This is because you redefine a measure as a _dimension_. This is accomplished by creating a [derived table](https://docs.cloud.google.com/looker/docs/derived-tables) that includes the measure you want to dimensionalize in its SQL definition. 

### The process

The following example is based on a sample e-commerce dataset. The goal for this example is to create an [`type: average`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#average) measure that is based on an existing **Total Revenue** [`type: sum`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum) measure. 

> _The following steps outline how to generate a SQL-based derived table. You can elect to create a LookML-based derived table, also known as a[native derived table (NDT)](https://docs.cloud.google.com/looker/docs/creating-ndts), as an alternative to SQL. _

  1. Start by setting up an [Explore query](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores). Choose the appropriate fields, including the measure you want to dimensionalize. 

In the example use case, the Explore **Data** table features **Total Revenue** grouped by **Users State** and **Users ID** :

![](https://docs.cloud.google.com/static/looker/docs/images/hc-dimensionalize-measure-base-explore-2212.png)
  2. Choose **Open in SQL Runner** from the **SQL** tab in the **Data** table to open the query in [SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-basics): 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-dimensionalize-measure-open-sql-runner-2212.png)
  3. After running the query in SQL Runner (by clicking the **Run** button) and confirming the results, choose the [**Add to Project**](https://docs.cloud.google.com/looker/docs/sql-runner-create-derived-tables#adding_to_a_lookml_project) option from the SQL Runner gear menu to open the **Add to Project** pop-up. _At this point you need to remove any row limit clause in the derived table SQL to ensure that all desired results are included in the query._

> _You can also choose[**Get Derived Table LookML**](https://docs.cloud.google.com/looker/docs/sql-runner-create-derived-tables#getting_the_lookml_for_a_derived_table) from the menu to copy and paste the generated LookML into your project manually._

  4. From the **Add to Project** pop-up, select a project name from the **Project** drop-down, enter a name for your derived table view file, and select **Add**. 
  5. Now that the derived table is in a view file, you can create a measure that aggregates the dimensionalized measure. For example, you can now create a `type: average` measure for the new total revenue dimension, `order_items_total_revenue`: 
         
         dimension: order_items_total_revenue {
                 type:  number
                 sql: ${TABLE}.order_items.total_revenue ;;
                 value_format_name: usd
               }
         
               measure: average_revenue {
                 type:  average
                 sql:  ${order_items_total_revenue} ;;
                 value_format_name: usd
               }
             

  6. Double-check that a [primary key](https://docs.cloud.google.com/looker/docs/reference/param-field-primary-key) is defined in the derived table. 
  7. [Join](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) the new view into the original Explore (or create a new Explore) to be able to create queries and content with the new fields. 



## Conclusion

Dimensionalizing measures with Looker derived tables unlocks new capabilities and provides the power to make further insights with your data. With the ability to **group by** a dimensionalized measure, filter by it in a WHERE clause (instead of HAVING), pivot on it, and create other dimensions based on it, you can take your Explore queries, and content, to the next dimension. 

Visit the [Derived tables](https://docs.cloud.google.com/looker/docs/derived-tables) documentation page for more information about creating and using derived tables, along with considerations and performance optimization tips. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
