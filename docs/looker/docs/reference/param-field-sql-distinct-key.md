---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-sql-distinct-key/
title: sql_distinct_key \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:38.982669+00:00
---

# sql_distinct_key  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-sql-distinct-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  sql_distinct_key Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      measure: field_name {
        type: sum_distinct
        sql_distinct_key: ${my_field_name} ;;
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [measure](https://docs.cloud.google.com/looker/docs/reference/param-field-measure) `sql_distinct_key` |  Possible Field Types Measure Accepts A SQL expression  
---|---  
  
## Definition

The `sql_distinct_key` parameter is used with measure types that perform aggregations on non-repeated values, specifically measures of type [`average_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#average_distinct), [`median_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#median_distinct), [`percentile_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percentile_distinct), and [`sum_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum_distinct). `sql_distinct_key` tells Looker which field to use as a basis for determining unique values, thereby avoiding miscalculations in the case of a [fanout](https://discuss.google.dev/t/the-problem-of-sql-fanouts/119220).

For example, `type: sum_distinct` adds up the nonrepeated values in a given field, based on the unique values defined by the [`sql_distinct_key`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql-distinct-key) parameter.

Consider a table like this:

Order Item ID | Order ID | Order Shipping  
---|---|---  
1 | 1 | 10.00  
2 | 1 | 10.00  
3 | 2 | 20.00  
4 | 2 | 20.00  
5 | 2 | 20.00  
  
In this situation, there are multiple rows for each order. If you added a basic measure of `type: sum` for the `order_shipping` column, you get a total of 80.00, even though the total shipping collected is actually 30.00.
    
    
     # Will NOT calculate the correct shipping amount
    measure: total_shipping {
      type: sum
      sql: ${order_shipping} ;;
    }
    

To get an accurate result, you can explain to Looker how it should identify each unique entity (in this case, each unique order) by using the `sql_distinct_key` parameter. This _will_ calculate the correct 30.00 amount:
    
    
     # Will calculate the correct shipping amount
    measure: total_shipping {
      type: sum_distinct
      sql_distinct_key: ${order_id} ;;
      sql: ${order_shipping} ;;
    }
    

Every unique value of `sql_distinct_key` must have just one corresponding value in [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql). This example works because _every_ row with an `order_id` of 1 has the same `order_shipping` of 10.00, _every_ row with an `order_id` of 2 has the same `order_shipping` of 20.00, etc.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
