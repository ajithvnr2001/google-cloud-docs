---
url: https://docs.cloud.google.com/spanner/docs/graph/graph-with-views-overview/
title: Overview of graphs created from SQL views \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:24.204424+00:00
---

# Overview of graphs created from SQL views  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/graph/graph-with-views-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Overview of graphs created from SQL views Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This feature is available with the Spanner Enterprise edition and Enterprise Plus edition. For more information, see the [Spanner editions overview](https://docs.cloud.google.com/spanner/docs/editions-overview). 

Use this document to learn about the benefits of using SQL views to create a graph. This document includes benefits of creating graphs with views, requirements, and considerations to help you decide if you should use [tables](https://docs.cloud.google.com/spanner/docs/graph/create-update-drop-schema) or views to create a graph.

For details about how to create a graph from views, see [Create a property graph from SQL views](https://docs.cloud.google.com/spanner/docs/graph/graph-with-views-how-to).

## Benefits of creating graphs with views instead of tables

A SQL _view_ is a virtual table defined by a SQL query. In Spanner, the query defining a view executes every time a query that refers to the view executes. Spanner views aren't materialized views because they don't store the results of the query defining the view as an actual table in data storage. For more information, see [Views overview](https://docs.cloud.google.com/spanner/docs/views). You can create graph elements from SQL views, but you can't create a view that queries a graph.

Views provide several advantages as an abstraction layer between tables and a graph schema that aren't available when you use tables to create a graph.

  * [**Row-level access control**](https://docs.cloud.google.com/spanner/docs/graph/graph-with-views-how-to#fine-grained-graph-access). Apply [fine-grained access control](https://docs.cloud.google.com/spanner/docs/fgac-about) at the row-level to graph data using the security privileges of [definer's rights views](https://docs.cloud.google.com/spanner/docs/views#definer). This ensures users can query only nodes and edges they are permitted to see.

  * **[Flexible data modeling](https://docs.cloud.google.com/spanner/docs/graph/graph-with-views-how-to#model-derived-graph)**. Use a view with a query to shape and transform relational data before creating a graph element. The view's query lets you filter rows, combine columns, or unnest repeated fields such as in an `ARRAY`.

  * **[Transition from schemaless data to formalized data](https://docs.cloud.google.com/spanner/docs/graph/graph-with-views-how-to#schemaless-transition)**. Create views from [schemaless data](https://docs.cloud.google.com/spanner/docs/graph/manage-schemaless-data) to define node and edge types explicitly. This helps formalize the relationships in the data.




## Requirements for using views to create graphs

You must follow these requirements when you use views to create graph elements:

  * Use the `KEY` clause when you specify a graph element.

  * Ensure node and edge key uniqueness.




### Use the `KEY` clause when you specify a graph element

You must explicitly define the columns that uniquely identify the graph element when you use views to create a node or an edge element. To do this, use the `KEY` clause in the node or edge element definition. To learn how to use the `KEY` clause when creating a graph element, see the code examples in this document and in [Create a Spanner Graph from a SQL view](https://docs.cloud.google.com/spanner/docs/graph/graph-with-views-how-to).

### Ensure node and edge key uniqueness

Every node and edge in a property graph must have a unique key. When you define graph elements using views, you can choose how element key uniqueness is verified:

  * Strict key validation (default): Spanner verifies that views follow supported query patterns to ensure key uniqueness.
  * Disabled key validation (any SQL query): You can use any SQL query if you set the `validate_element_key_uniqueness = false` graph option. In this mode, you are responsible for ensuring that element keys are unique.



#### Strict key validation (default)

By default, Spanner verifies that views defining node or edge tables follow one of the following patterns to ensure that each node or edge is unique:

  * Pattern 1: The view uses a single table's primary key.

  * Pattern 2: The view uses a `GROUP BY` or a `SELECT DISTINCT` clause.




You can use other SQL operators such as `WHERE`, `HAVING`, `ORDER BY`,`LIMIT`, and `TABLESAMPLE` in combination with these patterns. These operators filter or order the results, but they don't change the underlying uniqueness guarantee that the patterns provide.

**Pattern 1: Use a single table's primary key**

In this pattern, the view selects from a single table, and the `KEY` clause in the graph definition matches the base table's primary key columns. Because of this, each node or edge row produced by the view is unique.

For example, the following selects a subset of rows from the `Account` table. The graph `KEY(account_id)` matches the `Account` table's primary key, which ensures that each row produced by the view is unique.
    
    
    -- Table has PRIMARY KEY(account_id).
    CREATE TABLE Account (
      account_id INT64 NOT NULL,
      customer_id INT64 NOT NULL,
      account_type STRING(MAX),
      balance INT64
    ) PRIMARY KEY(account_id);
    
    -- Pattern 1: View uses the primary key from a single table.
    CREATE VIEW SavingAccount
      SQL SECURITY INVOKER AS
        SELECT accnt.account_id, accnt.customer_id, accnt.balance
        FROM Account accnt
        WHERE accnt.account_type = 'saving';
    
    CREATE PROPERTY GRAPH SavingAccountGraph
      NODE TABLES (
        -- The element KEY(account_id) matches the table's primary key.
        SavingAccount KEY(account_id)
      );
    

**Pattern 2: Use`GROUP BY` or `SELECT DISTINCT` clause**

In this pattern, the view's query uses a `GROUP BY` or a `SELECT DISTINCT` clause. The columns in the `KEY` clause must match the columns that these clauses use to define uniqueness:

  * For `GROUP BY`: The `KEY` clause columns must match all columns in the `GROUP BY` clause.

  * For `SELECT DISTINCT`: The `KEY` clause columns must match the columns in the `SELECT DISTINCT` list.




Example with `GROUP BY`:
    
    
    CREATE TABLE Customer (
      customer_id INT64,
      name STRING(MAX)
    ) PRIMARY KEY (customer_id);
    
    CREATE TABLE SaleOrder (
      order_id INT64,
      customer_id INT64,
      amount INT64
    ) PRIMARY KEY (order_id);
    
    CREATE VIEW CustomerOrder
      SQL SECURITY INVOKER AS
        SELECT
          s.order_id,
          ANY_VALUE(c.customer_id) AS customer_id,
          ANY_VALUE(c.name) AS customer_name
        FROM Customer c JOIN SaleOrder s ON c.customer_id = s.customer_id
        GROUP BY s.order_id;
    
    CREATE PROPERTY GRAPH OrderGraph
      NODE TABLES (
        -- The KEY(order_id) matches the GROUP BY column in view definition.
        CustomerOrder KEY(order_id)
      );
    

Example with `SELECT DISTINCT`:
    
    
    CREATE TABLE SaleOrder (
      order_id INT64,
      customer_id INT64,
      amount INT64
    ) PRIMARY KEY (order_id);
    
    CREATE VIEW KeyCustomer SQL SECURITY INVOKER AS
      SELECT DISTINCT s.customer_id, s.amount
      FROM SaleOrder s
      WHERE s.amount > 1000;
    
    CREATE PROPERTY GRAPH KeyCustomersGraph
      NODE TABLES (
        -- The KEY(customer_id, amount) matches the DISTINCT columns.
        KeyCustomer KEY(customer_id, amount)
      );
    

#### Disabled key validation (any SQL query)

If your view uses a query that doesn't follow Pattern 1 or Pattern 2—such as a query that joins tables without a `GROUP BY` or `SELECT DISTINCT` clause—you can disable element key validation by setting the graph option `validate_element_key_uniqueness = false`.

By default, `validate_element_key_uniqueness` is `true`. When set to `false`, Spanner does not validate the view's query definition at schema creation time. You can use any SQL query in the view, but you must ensure that the columns specified in the `KEY` clause contain unique values for every node or edge row.

**Caution:** If you set `validate_element_key_uniqueness = false` and the view's data contains duplicate keys, graph pattern matching might return duplicate elements or unexpected query results.

The following example defines a view named `CustomerOrderTrusted` that joins the `Customer` and `SaleOrder` tables without a `GROUP BY` clause. Because each sale order is unique, joining `SaleOrder` with `Customer` preserves the uniqueness of `order_id` in the view results. However, because the query uses a `JOIN` and does not follow Pattern 1 or Pattern 2, Spanner cannot verify uniqueness syntactically.

By specifying `KEY(order_id)` and setting `validate_element_key_uniqueness = false` in the `OPTIONS` clause, you can define the property graph without modifying the view query:
    
    
    -- View uses a JOIN without GROUP BY or DISTINCT.
    CREATE VIEW CustomerOrderTrusted
      SQL SECURITY INVOKER AS
        SELECT
          s.order_id,
          c.customer_id,
          c.name AS customer_name
        FROM Customer c JOIN SaleOrder s ON c.customer_id = s.customer_id;
    
    -- Property graph disables element key uniqueness validation.
    CREATE PROPERTY GRAPH OrderGraphTrusted
      NODE TABLES (
        CustomerOrderTrusted
          KEY(order_id)
          LABEL CustomerOrder PROPERTIES(
            order_id,
            customer_id,
            customer_name)
      ) OPTIONS (validate_element_key_uniqueness = false);
    

## Considerations when using views

When you use views to define graph elements, the following can help you design and implement an effective graph:

  * Query performance evaluation.

  * Schema optimization.

  * Error handling to enforce data integrity.




### Property graph query performance

When you define graph elements on views that perform data transformations (for example, `GROUP BY`, `UNNEST`, or `JOIN` operations), carefully evaluate query performance for your use case. Remember that Spanner executes a view's query definition every time a query performs [element pattern matching](https://docs.cloud.google.com/spanner/docs/graph/queries-overview#graph-pattern-matching).

### Graph schema optimization

When you use views to define graph elements, some [graph schema optimizations](https://docs.cloud.google.com/spanner/docs/graph/best-practices-designing-schema) might be less effective than when you use tables to define graph elements.

#### Views that project a single table's primary key

If a view is a projection from a single base table, any optimizations on that underlying table remain effective for graph queries. For example, applying the following techniques to base tables provides similar performance benefits for graph elements defined on such views:

  * [Optimize forward edge traversal](https://docs.cloud.google.com/spanner/docs/graph/best-practices-designing-schema#optimize-forward-edge-traversal).

  * [Use referential constraints](https://docs.cloud.google.com/spanner/docs/graph/best-practices-designing-schema#use-ref-constraints).

  * [Use secondary indexes to filter properties](https://docs.cloud.google.com/spanner/docs/graph/best-practices-designing-schema#use-secondary-indexes).




#### Views defined with `GROUP BY` or `DISTINCT` clause

Views that perform aggregations, such as `GROUP BY`, `SELECT DISTINCT`, or other complex transformations, lose the direct relationship to the underlying table structure. Because of this, schema optimizations on the base tables might not provide the same performance benefits for graph queries that operate on the views. Carefully evaluate query performance for your use case when your views perform complex aggregations.

### Data modification with view-based graphs

Views are not materialized, which means they don't store the results of the query that defines the view as a table in data storage, and they are read-only. Because of this, to insert, update, or drop nodes or edges in a graph created from views, you modify data in the tables used to create the views.

### Graph error handling to enforce data integrity

When you use views to define graph elements, enforce data integrity (for example, enforce data types) on the underlying base tables. Otherwise, the data in the base tables might be invalid and cause queries on your view-based graph to fail at runtime.

For example, when you [transition from schemaless to a formalized graph](https://docs.cloud.google.com/spanner/docs/graph/graph-with-views-how-to#schemaless-transition), use `CHECK` constraints to validate data in your base tables (`GraphNode` and `GraphEdge`). The following code applies these constraints within the JSON properties to ensure data integrity at the source and prevent runtime query errors.
    
    
    -- Enforce that the 'name' property exists for nodes with the 'person' label.
    ALTER TABLE GraphNode
    ADD CONSTRAINT NameMustExistForPersonConstraint
    CHECK (IF(label = 'person', properties.name IS NOT NULL, TRUE));
    
    -- Enforce that the 'name' property is a string for nodes with the 'person' label.
    ALTER TABLE GraphNode
    ADD CONSTRAINT PersonNameMustBeStringTypeConstraint
    CHECK (IF(label = 'person', JSON_TYPE(properties.name) = 'string', TRUE));
    

## What's next

  * Learn how to [create a property graph from SQL views](https://docs.cloud.google.com/spanner/docs/graph/graph-with-views-how-to).

  * Learn about the [Spanner Graph schema](https://docs.cloud.google.com/spanner/docs/graph/schema-overview).

  * Learn about [best practices for designing a Spanner Graph schema](https://docs.cloud.google.com/spanner/docs/graph/best-practices-designing-schema).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
