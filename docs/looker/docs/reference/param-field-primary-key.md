---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-primary-key/
title: primary_key \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:37.650269+00:00
---

# primary_key  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-primary-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  primary_key Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: field_name {
        primary_key: yes 
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `primary_key` |  Possible Field Types Dimension Accepts A Boolean (yes or no)  
---|---  
  
## Definition

The `primary_key` parameter specifies that a dimension is the primary key for its view. The default value is `false`. For example:
    
    
    dimension: id {
      primary_key: yes
      sql: ${TABLE}.id ;;
    }
    

The `primary_key` parameter has the following qualities:

  * Helps Looker to avoid unnecessary `GROUP BY` clauses.
  * Is necessary to make the [`foreign_key`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-foreign-key) parameter work properly.
  * Is required for the proper functioning of [symmetric aggregates](https://docs.cloud.google.com/looker/docs/best-practices/understanding-symmetric-aggregates). When you join views with measures (aggregates), a `primary_key` must be defined on each side of the join to [properly calculate the aggregations](https://docs.cloud.google.com/looker/docs/working-with-joins#primary_keys_required).



The `primary_key` parameter has the following limitations:

  * You cannot add this parameter to more than one field in each view.
  * You cannot add this parameter to a [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#time) that specifies more than one `timeframe`.



### Creating a compound primary key

If you have a primary key that is comprised of multiple columns, you can create a dimension that concatenates those columns, then declare that as your primary key. For example:
    
    
    dimension: primary_key {
      primary_key: yes
      sql: CONCAT(${TABLE}.promotion_id, ${TABLE}.sku) ;;
    }
    

> `CONCAT` works in some databases, such as MySQL, but other databases might have a different equivalent. Redshift, for example, uses `||` as its concatenation operator.

### Using a persistent derived table (PDT) to create a primary key

In cases where there is no reasonable way to identify a unique row as a primary key, you can create a [persistent derived table (PDT)](https://docs.cloud.google.com/looker/docs/derived-tables#creating_persistent_derived_tables) to generate a unique ID. For example, the following derived table uses the table's row number to serve as a primary key:
    
    
    view: transaction {
      # sql_table_name: warehouse.transaction
      derived_table: {
        sql: SELECT ROW_NUMBER as transaction_pk, * FROM warehouse.transaction ;;
        sql_trigger_value: SELECT CURRENT_DATE ;;
        indexes: [customer_id, product_id, salesperson_id, transaction_date]
      }
    
      dimension: transaction_pk {
        type: number
        primary_key: yes
        hidden: yes
        sql: ${TABLE}.transaction_pk ;;
        ...
      }
    }
    

### Defining a new primary key in an extended view

If you use the `extends` parameter to extend a view, the primary key from the base view will be extended to the new view.

To change the primary key to a new dimension, add `primary_key: no` to the original dimension definition in the new view, and add `primary_key: yes` to the new dimension definition in the new view.
    
    
    view: base {
      dimension: old_primary_key {
        primary_key: yes
        sql: ${TABLE}.id ;;
      }
    }
    
    view: new {
      extends: base
    
      dimension: old_primary_key {
        primary_key: no
      }
    
      dimension: new_primary_key {
        primary_key: yes
        sql: ${TABLE}.new_id ;;
      }
    }
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
