---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-where/
title: sql_where \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:26.337033+00:00
---

# sql_where  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-where/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  sql_where Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    explore: view_name_1 {
      join: view_name_2 {
        sql_where: ${view_name_1.id} < 100 ;;
      }
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) `sql_where` |  Default Value None Accepts A SQL `WHERE` clause  
---|---  
  
## Definition

`sql_where` lets you apply a query restriction that users cannot change. The restriction will be inserted into the `WHERE` clause of the underlying SQL that Looker generates if and only if the join is used in the query. In addition to queries run by human users, the restriction will apply to dashboards, scheduled Looks, and embedded information that relies on that Explore.

The condition can be written in pure SQL, using your database's actual table and column names. It can also use Looker field references like `${view_name.field_name}`, which is the preferred method, because Looker can be smarter about automatically including necessary joins. A `sql_where` condition is not displayed to the user, unless they look at the underlying SQL of any queries that they create.

## Example

For example, you can specify that if the join to users is used, that only users younger than 50 should be included:
    
    
    explore: orders_users_under_50 {
      view_name: orders
    
      join: users {
        sql_on: ${users.id} = ${orders.user_id} ;;
        sql_where: ${users.age} < 50 ;;
        type: left_outer
      }
    }
    

If the user selects `Orders.Count` and `Users.Count`, the SQL that Looker would generate from this LookML is:
    
    
    SELECT
      COUNT(orders.id) AS orders_count,
      COUNT(DISTINCT users.id, 1000) AS users_count
    FROM thelook2.orders AS orders
    LEFT JOIN thelook2.users AS users ON users.id = orders.user_id
    
    WHERE users.age < 50
    LIMIT 500
    

## Things to consider

### Parentheses are required if you are using `OR` logic

If you use OR logic with `sql_where`, it's very important to place parentheses around the SQL condition. For example, instead of writing this:
    
    
    sql_where: region = 'Northeast' OR company = 'Altostrat' ;;
    

You would write this:
    
    
    sql_where: (region = 'Northeast' OR company = 'Altostrat') ;;
    

If you forgot to add the parentheses in this example, and a user added their own filter, the generated `WHERE` clause could have the form:
    
    
    WHERE
      user_filter = 'something' AND
      region = 'Northeast' OR
      company = 'Altostrat'
    

In this situation, the filter that the user applied may not work. No matter what, rows with `company = 'Altostrat'` will show up, because the AND condition is evaluated first. Without parentheses, only part of the `sql_where` condition combines with the user's filter. If parentheses were added, the `WHERE` clause would look like this instead:
    
    
    WHERE
      user_filter = 'something' AND
      (region = 'Northeast' OR company = 'Altostrat')
    

Now the user's filter will be applied for every row.

### Join order is important for `sql_where` dependencies

In general, Looker implements joins in the correct order, regardless of the order in which the joins are defined in the LookML. The exception to this is with `sql_where`. If you reference a field from another join in your `sql_where` statement, the join you are referencing must be defined before your `sql_where` statement in the LookML.

For example, here is a `sql_where` statement that references the `inventory_items.id` field before `inventory_items` has been joined in:
    
    
    explore: orders {
      hidden: yes
      join: order_items {
        sql_on: ${order_items.order_id} = ${orders.id} ;;
        sql_where: ${inventory_items.id} IS NOT NULL ;;
      }
      join: inventory_items {
        sql_on: ${inventory_items.id}=${order_items.inventory_item_id} ;;
      }
    }
    

If you run a query in this Explore, Looker will return an error that the `inventory_items.id` field cannot be found.

However, you can solve this problem by reordering your joins so that the join referenced in the `sql_where` statement is defined before the `sql_where` statement, like this:
    
    
    explore: orders {
      hidden: yes
      join: inventory_items {
        sql_on: ${inventory_items.id}=${order_items.inventory_item_id} ;;
      }
    join: order_items {
        sql_on: ${order_items.order_id} = ${orders.id} ;;
        sql_where: ${inventory_items.id} IS NOT NULL ;;
      }
    }
    

This will prevent the error because the `inventory_items` join is defined before the `inventory_items.id` field is referenced in the `sql_where` statement of the `order_items` join.

### The `sql_where` query restriction is applied only if the join is used

The query restriction specified in `sql_where` will be inserted into the `WHERE` clause of the underlying SQL that Looker generates if and only if the join is used in the query. If you want to have a where clause applied even if the join wouldn't have been used, use [`sql_always_where`](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-where) instead.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
