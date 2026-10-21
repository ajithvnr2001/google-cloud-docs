---
url: https://docs.cloud.google.com/sql/docs/mysql/parameterized-secure-views/
title: Overview of parameterized secure views in Cloud SQL \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:23.305008+00:00
---

# Overview of parameterized secure views in Cloud SQL  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/parameterized-secure-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Overview of parameterized secure views in Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/parameterized-secure-views "View this page for the PostgreSQL database engine") | SQL Server

**Preview — Parameterized secure views**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Parameterized secure views in Cloud SQL for MySQL provide data security and row access control to applications while supporting SQL. These views support _data value extraction_ —the process of retrieving specific data pieces from columns—and they help protect against [prompt injection attacks](https://en.wikipedia.org/wiki/Prompt_injection). Parameterized secure views help ensure that end users can view only the data that they are supposed to access.

Parameterized secure views are an extension of [MySQL views](https://dev.mysql.com/doc/refman/8.4/en/views.html), which let you use application-specific named view parameters in view definitions. This capability provides an interface that takes a query and values for the named parameters. The views execute the query with those values, which are used throughout the execution of that query. 

## Parameterized secure view example

The following example shows how to create a parameterized secure view on a table by adding a session variable to the `WHERE` clause. 
    
    
    -- Create a view with a parameter
    
    CREATE VIEW v_orders AS
    SELECT * FROM orders
    WHERE customer_id = @local_customer_id AND year >= @earliest_year;
    

Then you can set the parameter for the view and run a query.
    
    
    -- Set the parameter and query
    
    SELECT /*+ SET_VIEW_VARS(local_customer_id=5, earliest_year=2021) */ * FROM v_orders;
    
    -- Or query through a stored procedure
    
    CALL mysql.execute_parameterized_query(
        'SELECT * FROM db.v_orders',
        'local_customer_id = 5, earliest_year = 2021');
    

### Use cases

Large language models (LLMs) might generate SQL queries that expose sensitive data.

Parameterized secure views manage data security at the database level, especially ad hoc queries from untrusted sources, such as those translated from natural language. For example, you can use parameterized secure views to provide data security for applications where users can issue queries in natural language, like, "Show my orders".

You can use parameterized secure views to apply the following requirements to how Cloud SQL for MySQL executes this query:

  * The query reads only the database objects and columns that you listed in your database parameterized secure views.
  * The query reads only the database rows that are associated with the user who submitted the query. The returned rows have a data relationship with the user's table row.



For more information about configuring security and access control, see [Use parameterized secure views](https://docs.cloud.google.com/sql/docs/mysql/use-parameterized-secure-views).

Parameterized secure views help to mitigate security risks that occur when end users are allowed to run untrusted queries, like natural language queries, on the database table. Security risks include the following:

  * Users can submit prompt injection attacks and try to manipulate the underlying model to reveal all the data that the application has access to.
  * The Natural Language to SQL (NL2SQL) model might generate SQL queries that are broader in scope than is appropriate for data security reasons. This security risk can expose sensitive data in response to even well-intentioned user queries.



Using parameterized secure views, you can define the tables and columns that untrusted queries can pull data from. These views let you restrict the range of rows available to an individual application user. These restrictions also let you tightly control the data that application users can view through natural language queries, regardless of how users phrase those queries.

For example, you might have an application that tracks customer orders. A support agent asks in the application, "What is the status of the order for customer 12345?" In this scenario, the application can use a parameterized secure view with a session variable that's based on a customer ID. The parameterized secure view uses a query that only returns rows that are linked to and accessible to the customer ID 12345.

By using parameterized secure views, you can restrict the range of rows available to individual application users. This control ensures data security, regardless of how users phrase their queries.

### Data security

Parameterized secure views give application developers data security and row access control using the following methods:

  * MySQL parameterized secure views provide row-level security by preventing maliciously-chosen functions and operators from being passed values from rows until after the view has done its work.


  * Named view parameters allows a restricted view of the database parameterized by values. The values are provided by the application based on application-level security such as end user authentication.

  * Enforcement of additional restrictions on queries accessing parameterized views that prevents attacks against escaping the checks in the views based on the given parameter values. For more information, see [Restrictions on queries](https://docs.cloud.google.com/sql/docs/mysql/use-parameterized-secure-views#restrictions).




### Simplify user management

With parameterized secure views, you can use a single database role to serve all end users, instead of using methods that might require you to create a separate database user or role for each end user. This helps simplify user and connection management for applications where each end user needs access only to their data.

For example, in an application where a user should only see the orders for a specific customer, you can define a single parameterized secure view that is parameterized by the end user identifier. This view allows a single database role –with access to the view, not the underlying table– to serve all users, which simplifies user management and database connections.

## Limitations

  * Parameterized secure views are supported only in Cloud SQL for MySQL version 8.0.43 and later. If you try to create a parameterized secure view in an earlier version of MySQL, then Cloud SQL returns an error.

  * You can't specify variables outside of `WHERE`, `HAVING` or `ON` clauses.

  * You can't use `EXPLAIN` on a parameterized secure view.



  * There are restrictions when you query parameterized secure views. For more information, see [Restrictions on queries](https://docs.cloud.google.com/sql/docs/mysql/use-parameterized-secure-views#restrictions).



## What's next

  * [Use parameterized secure views](https://docs.cloud.google.com/sql/docs/mysql/use-parameterized-secure-views)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
