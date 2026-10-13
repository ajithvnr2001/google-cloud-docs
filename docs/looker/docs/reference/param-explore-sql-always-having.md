---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-having/
title: sql_always_having \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:23.381482+00:00
---

# sql_always_having  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-having/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  sql_always_having Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    explore: explore_name {
      sql_always_having: ${count} >= 100 ;;
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `sql_always_having` |  Default Value None Accepts A SQL `HAVING` condition using measure name(s) and/or SQL column name(s) Special Rules If you are referencing a SQL column name in `sql_always_having` that is part of a joined view, rather than part of the Explore, it's important to use the [`always_join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-join) parameter -- or reference a field name instead   
---|---  
  
## Definition

`sql_always_having` lets you apply a query restriction that users cannot change. The restriction will be inserted into the `HAVING` clause of the underlying SQL that Looker generates, for all queries on the [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) where `sql_always_having` is used. In addition to queries run by human users, the restriction will apply to dashboards, scheduled Looks, and embedded information that relies on that Explore.

The condition can be written in pure SQL, using your database's actual table and column names. It can also use Looker references like:

  * `${view_name.SQL_TABLE_NAME}`, which references a different Looker view or a [derived table](https://docs.cloud.google.com/looker/docs/derived-tables). Note that `SQL_TABLE_NAME` in this reference is a literal string; you do not need to replace it with anything.
  * `${view_name.field_name}`, which references a Looker field. Using this method is better than referring to SQL columns directly because Looker can automatically include any necessary joins.



A `sql_always_having` condition is not displayed to the user, unless they look at the underlying SQL of any queries that they create.

## Examples

Prevent users from looking at groups with fewer than 100 orders:
    
    
    # Using Looker references
    explore: order {
      sql_always_having: ${count} >= 100 ;;
    }
    
    # Using raw SQL
    explore: order {
      sql_always_having: COUNT(*) >= 100 ;;
    }
    

Prevent users from looking at groups with less than $1,000 in revenue:
    
    
    explore: customer {
      sql_always_having: ${total_revenue} >= 1000 ;;
    }
    

Prevent users from looking at groups with fewer than 100 customers:
    
    
    explore: order {
      sql_always_having: ${customer.count} >= 100 ;;
      join: customer {
        sql_on: ${order.customer_id} = ${customer.id} ;;
      }
    }
    

## Common challenges

### If you use raw SQL, you might need to use `always_join`

If you are referencing a SQL column name in `sql_always_having` that is part of a joined view rather than part of the Explore, it's important to use the [`always_join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-join) parameter. Consider this example:
    
    
    explore: order {
      sql_always_having: SUM(customer.visits) >= 100 ;;
      join: customer {
        sql_on: ${order.customer_id} = ${customer.id} ;;
      }
    }
    

In this case `sql_always_having` is referencing a column from the joined `customer` view, instead of the `order` Explore. Since `sql_always_having` will be applied to every query, it's important that `customer` is also joined in every query.

When Looker generates SQL for a query, it attempts to create the cleanest SQL possible, and will only use the joins that are necessary for the fields a user selects. In this case, Looker would only join `customer` if a user selected a customer field. By using [`always_join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-join), you can force the join to occur no matter what.

If, instead of `sql_always_having: SUM(customer.visits) >= 100` you used `sql_always_having: ${customer.total_visits} >= 100`, Looker would be smart enough to make the `customer` join without requiring you to use [`always_join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-join). For this reason, we encourage you to use Looker field references instead of raw SQL references when possible.

### Only use one `sql_always_having` per Explore

You should only have one `sql_always_having` in an `explore` definition. Put all the desired behavior into a single `sql_always_having` by using `AND` and `OR` as needed.

## Things to know

### There is a similar parameter for the SQL WHERE clause

There is a very similar parameter to `sql_always_having` called [`sql_always_where`](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-where) that works in the same way, but applies conditions to the `WHERE` clause instead of the `HAVING` clause.

### If you want filters a user can change, but not remove, consider `always_filter`

If you want to force users to use a specific set of filters, but where the default value can be changed, try [`always_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-filter) instead.

### If you want user-specific filters that can't be changed, consider `access_filter`

If you want an Explore to have filters that are specific to each user, and cannot be changed in any way, you can use [`access_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
