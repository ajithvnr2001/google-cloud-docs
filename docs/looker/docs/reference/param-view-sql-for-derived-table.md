---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-sql-for-derived-table/
title: sql (for derived tables) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:32.199082+00:00
---

# sql (for derived tables)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-sql-for-derived-table/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  sql (for derived tables) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `sql` parameter that is part of a [derived table](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table).
> 
> You can also use `sql` as part of a field, as described on the [`sql` (for fields)](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameter documentation page.

## Usage
    
    
    view: my_derived_table {
      derived_table: {
        sql: 
          SELECT *
          FROM events
          WHERE type NOT IN ('test', 'staff')
     ;;
        ...
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [`derived_table`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table) `sql` |  Default Value None Accepts A SQL block   
---|---  
  
## Definition

`sql` lets you specify the SQL that will be used to generate a derived table. You can use any legal SQL query in the `sql` parameter, as long as the SQL query is written in raw SQL and does not reference Looker fields. For a more complete understanding of derived tables, see the [Derived tables in Looker](https://docs.cloud.google.com/looker/docs/derived-tables) documentation page.

In addition to referencing normal database tables, you can also reference LookML views or derived tables in `sql`. To do so, use:

`${view_or_derived_table_name.SQL_TABLE_NAME} AS view_or_derived_table_name`

The `SQL_TABLE_NAME` in this reference is a literal string; you do not need to replace it with anything. For example, if you wanted to reference a derived table named `key_customer` in your `key_customer_order_facts` derived table, you might have something like this:
    
    
    view: key_customer_order_facts {
      derived_table: {
        sql:
          SELECT
            customer_id,
            COUNT( * ) AS lifetime_orders
          FROM
            order
          INNER JOIN
            ${key_customer.SQL_TABLE_NAME} AS key_customer
          ON
            order.customer_id = key_customer.id
          GROUP BY 1
          ;;
      }
    }
    

### Liquid variables with `sql`

You can also use [Liquid variables](https://docs.cloud.google.com/looker/docs/liquid-variable-reference) with the `sql` parameter. Liquid variables let you access data such as the values in a field, data about the field, and filters applied to the field.

The [`date_start`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#date_start) and [`date_end`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#date_end) Liquid variables are very useful for database dialects that partition data into multiple tables by date, such as BigQuery. See the [Using `date_start` and `date_end` with date filters](https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-date_start-and-date_end-with-date-filters) Best Practices page for an in-depth explanation.

The `_in_query`, `_is_selected`, and `_is_filtered` [Liquid variables](https://docs.cloud.google.com/looker/docs/liquid-variable-reference) in particular can add some interesting functionality to derived tables. They return true or false based on whether a field or filter has been included in a query. There are some intricacies that should be considered to properly use these true/false values; see the [Liquid variable page](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#in-query-variables) for more information.

For example, this derived table changes the database table that it queries based on which fields the user has selected:
    
    
    view: dynamic_order_counts {
      derived_table: {
        sql:
          SELECT
            period, number_of_orders
          FROM
            {% if dates.reporting_date._in_query %}
              daily_orders
            {% elsif dates.reporting_week._in_query %}
              weekly_orders
            {% else %}
              monthly_orders
            {% endif %}
          GROUP BY 1
          ;;
      }
    }
    

## Examples

Create a `customer_order_facts` derived table:
    
    
    view: customer_order_facts {
      derived_table: {
        sql:
          SELECT
            customer_id,
            COUNT( * ) AS lifetime_orders
          FROM
            order
          GROUP BY 1
          ;;
      }
    }
    

## Things to consider

### Tables referenced by `sql` must be accessible from the current connection

`views` that contain a derived table are referenced by an [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) or [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) parameter, which in turn is referenced by a [model](https://docs.cloud.google.com/looker/docs/reference/param-model). The model determines which database connection is used (see the [`connection`](https://docs.cloud.google.com/looker/docs/reference/param-model-connection) parameter documentation page). Database connections themselves are defined in the **Admin** section of Looker. When you reference a table in the `sql` parameter, the table needs to be accessible within the associated connection.

### Use raw SQL with `sql`, not Looker field references

The SQL that you write into a derived table `sql` parameter should be raw SQL, referencing the underlying columns and tables from your database. It should not reference Looker field names or view names.

### Using `_filters['view_name.field_name']` in a derived table requires `sql_quote`

When you are defining a [SQL-based derived table](https://docs.cloud.google.com/looker/docs/derived-tables#sql-based_derived_tables), if you use the [`_filters['view_name.field_name']`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#_filters) Liquid variable where the value is rendered in SQL and the filter returns a string value, you need to add single quotation marks around the output. You can do this by including the `sql_quote` Liquid filter.

Otherwise, you will get the following LookML warning if you do not append the Liquid variable with `| sql_quote`:

`Using "_filters[]" in Derived Table SQL without "sql_quote" is discouraged.`

See the [Liquid variable reference](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#require_sql_quote) documentation page for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
