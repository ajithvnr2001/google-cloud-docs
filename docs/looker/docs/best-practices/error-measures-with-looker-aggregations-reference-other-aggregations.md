---
url: https://docs.cloud.google.com/looker/docs/best-practices/error-measures-with-looker-aggregations-reference-other-aggregations/
title: Error: Measures with Looker aggregations (sum, average, min, max, list types) may not reference other measures \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:52.548642+00:00
---

# Error: Measures with Looker aggregations (sum, average, min, max, list types) may not reference other measures  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/error-measures-with-looker-aggregations-reference-other-aggregations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Error: Measures with Looker aggregations (sum, average, min, max, list types) may not reference other measures Stay organized with collections  Save and categorize content based on your preferences. 

While developing in a project, you might see an error like the following in an [Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) or in the [LookML Validator](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_your_lookml): 
    
    
      Measures with Looker aggregations (sum, average, min, max, list types) may not reference other measures.
    

This error is caused by an [aggregate measure](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#measure_type_categories) referencing another aggregation or [measure](https://docs.cloud.google.com/looker/docs/reference/param-field-measure) of any type in its LookML definition, such as: 
    
    
        SELECT AVG((COUNT(*)) ) AS users.average_count FROM demo_db.users  AS users
    

SQL statements such as this generate a double or nested aggregation in SQL — most SQL dialects are unable to double aggregate, or nest aggregations, so such an attempt triggers the error. 

## Solutions

There are two possible solutions: 

  1. Use non-aggregate measures to perform non-aggregating SQL statements between measures.
  2. Use a derived table to nest aggregations or double aggregate.



### Using non-aggregate measures 

[Non-aggregate measures](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#measure_type_categories) — such as [`type: yesno`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#yesno) and [`type: number`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#number) — are the only measures that can reference other measures or aggregations. Non-aggregate measures do not perform any aggregation and thus will not perform a double or nested aggregation. Measures of `type: number` or `type: yesno` act as placeholders so other measures or combinations of measures can be referenced within them. 

For example, measures of `type: number` are used to perform calculations between measures and take any valid SQL expression that results in a number or an integer. 

The following example uses a `type: number` to calculate the percentage of all orders that are cancelled: 
    
    
    measure: order_count { # Base measure #1
        type: count
        sql: ${order_id} ;;
    }
    
    measure: cancelled_orders { # Base measure #2
        type: count
        filters: [status: "Cancelled"]
    }
    
    measure: percent_cancelled_orders { # New measure
        type: number
        sql: (1.0*${cancelled_orders})/ISNULL(${order_count},0) ;;
    }
    

### Using a derived table for double or nested aggregations

But what if a nested aggregation is necessary for performing an analysis? For example, what if you need to know the average amount that customers spend in their customer lifetime ("average customer lifetime value")? This requires two levels — a doubling or nesting — of aggregations, including: 

  1. A sum of sales, grouped by customer

  2. An average of that sum




To achieve this with LookML, you might try: 
    
    
    measure: total_revenue {
        type: sum
        sql: ${sale_price} ;;
    }
    
    measure: avg_customer_lifetime_value {
        type: average
        sql: ${total_revenue} ;;
    }
    

However, this will trigger the error because the `avg_customer_lifetime_value` measure is performing an aggregation on the `total_revenue` measure, which is already an aggregation. As previously discussed, most SQL dialects will trigger an error when double or nested aggregates are used in a query. 

To achieve an average of the `total_revenue` sum in SQL, a subquery such as the following is needed: 
    
    
      SELECT AVG(s.sum) FROM (SELECT SUM(x) as sum FROM ...) AS s
    

The equivalent solution in Looker is to create a [derived table](https://docs.cloud.google.com/looker/docs/derived-tables) to "flatten" the `total_lifetime_value` measure into a field that can be aggregated — in Looker, this is called [_dimensionalizing a measure_](https://docs.cloud.google.com/looker/docs/best-practices/how-to-dimensionalize-a-measure). With a derived table, the `total_lifetime_value` measure becomes a [dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension). You can then create a measure of [`type: average`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#average) that references the `customer_lifetime_value` dimension: 
    
    
    view: customer_facts {
        derived_table: {
            sql:
            SELECT
                user_id,
                COALESCE(SUM(sale_price), 0) AS customer_lifetime_value
            FROM orders
            GROUP BY user_id;;
        }
    
        dimension: customer_lifetime_value {
            type: number
            sql: ${TABLE}."customer_lifetime_value" ;;
        }
    
        measure: average_customer_lifetime_value {
            type: average
            sql: ${customer_lifetime_value} ;;
        }
    }
    

Once the `customer_facts` derived table is [joined](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) into an Explore, the `average_customer_lifetime_value` measure can be used to perform the desired analysis in an Explore without triggering any error. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
