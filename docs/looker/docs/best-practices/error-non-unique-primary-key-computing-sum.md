---
url: https://docs.cloud.google.com/looker/docs/best-practices/error-non-unique-primary-key-computing-sum/
title: Error: Non-Unique value/primary key (or sql_distinct_key), value overflow or collision when computing sum \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:44:02.862037+00:00
---

# Error: Non-Unique value/primary key (or sql_distinct_key), value overflow or collision when computing sum  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/error-non-unique-primary-key-computing-sum/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Error: Non-Unique value/primary key (or sql_distinct_key), value overflow or collision when computing sum Stay organized with collections  Save and categorize content based on your preferences. 

This page will help you troubleshoot this Looker error: 
    
    
      Non-unique value/primary key (or sql_distinct_key), value overflow or collision when computing sum
    

One of several issues can cause this error: 

  * A non-unique primary key (most common)
  * Incorrect usage of `sql_distinct_key`
  * Referencing a field across views when fanouts are involved



## Non-unique primary key

The most common cause of this error is that your query involves a non-unique primary key. You specify a primary key by using `primary_key: yes` on a dimension, and it must be a dimension without any repeated values. 

### Quick fix

Once you identify the primary key dimensions in your query, you can test them for uniqueness in Looker's [SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-basics) with this query: 
    
    
    SELECT
      COUNT(*),
      COUNT(DISTINCT your_primary_key)
    FROM
      your_table_name
    

If the counts in this query match, the primary key is unique. If the counts do _not_ match, the primary key is not unique and appears in multiple rows. You will need to choose or create a new dimension as your primary key. If no single dimension contains entirely unique values, you may need to concatenate fields to [create your own primary key dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-primary-key#compound_primary_key). 

### Using `row_number` to generate a primary key for a derived table

If you receive this error with a [derived table](https://docs.cloud.google.com/looker/docs/derived-tables), you can use the `row_number()` window function in Postgres and Redshift databases to make a unique field. This field can then be used as a primary key: 
    
    
      view: derived_table_name {
        derived_table {
          sql:
          SELECT
          row_number() OVER(ORDER BY created_at) AS prim_key,
          *
          FROM orders ;;
        }
    
        dimension: prim_key {
          type: number
          primary_key: yes
          sql: ${TABLE}.prim_key ;;
        }
      }
      

In MySQL, you can use a variable that iterates every row to achieve the same effect: 
    
    
      view: derived_table_name {
        derived_table {
         sql:
          SELECT
          CAST(@rownum := @rownum + 1 AS UNSIGNED) AS prim_key, t.*
          FROM orders t,
          (SELECT @rownum := 0) r ;;
        }
    
        dimension: prim_key {
          type: number
          primary_key: yes
          sql: ${TABLE}.prim_key ;;
        }
      }
      

## Incorrect usage of `sql_distinct_key`

If any of the measures in your query are of the type `sum_distinct`, there may be a uniqueness mismatch between the `sql_distinct_key` and `sql` parameters of that measure. 

### Quick fix

Check out our [`sum_distinct` documentation page](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum_distinct) for these parameters' requirements. 

## Referencing fields across views with fanouts

Your query may use a measure from view A, but the measure references a field from view B. In this situation Looker will use the primary key from view A to calculate that measure. If your query involves a fanout, that may not be the correct primary key to use. (To become familiar with fanouts, check out our [related Community post](https://www.googlecloudcommunity.com/gc/Technical-Tips-Tricks/Aggregate-functions-gone-bad-and-the-joins-who-made-them-that/ta-p/588767).) 

### Quick fix

To resolve this problem, add the primary key from view B to the problem measure with the `sql_distinct_key` parameter. 

## What if none of the listed causes apply, but the error still occurs?

There is a very specific situation in which your primary key can be unique, and the other causes of this problem don't apply to your query but this error still occurs. First, your query will involve multiple joins of `relationship: one_to_many`. Second, one of the measures in your query will reference a dimension that combines values from multiple joined views. 

To fix this problem, make a note of that measure, and then follow these steps: 

  1. Find the dimension within the measure that combines values from multiple joined views.
  2. Find the views that are referenced by that dimension.
  3. Concatenate the primary keys from those views using your SQL dialect's concatenation function.
  4. Place that concatenated key into a `sql_distinct_key` parameter on the measure that caused the problem.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
