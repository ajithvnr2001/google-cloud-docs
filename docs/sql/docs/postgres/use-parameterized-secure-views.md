---
url: https://docs.cloud.google.com/sql/docs/postgres/use-parameterized-secure-views/
title: Use parameterized secure views \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:50.627504+00:00
---

# Use parameterized secure views  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/use-parameterized-secure-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Use parameterized secure views Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/use-parameterized-secure-views "View this page for the MySQL database engine") | PostgreSQL | SQL Server

**Preview — Parameterized secure views**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to use parameterized secure views in Cloud SQL for PostgreSQL, which let you limit data access based on application-specific named parameters, like application user credentials. Parameterized secure views improve security and access control by extending the functionality of PostgreSQL views. These views also mitigate the risks of running untrusted queries from applications by enforcing a number of restrictions automatically on any query that is executed.

For more information, see the [parameterized secure views in Cloud SQL](https://docs.cloud.google.com/sql/docs/PostgreSQL/parameterized-secure-views) and [secure and control access to application data using parameterized secure views](https://docs.cloud.google.com/sql/docs/PostgreSQL/secure-app-data-parameterized-secure-views).

## Before you begin

This document assumes that you've already created a Cloud SQL for PostgreSQL instance.

Before you can use parameterized secure views, you must do the following:

  1. Enable the `cloudsql.enable_parameterized_views` database flag for your Cloud SQL instance. This flag change requires a database restart. For more information, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).

  2. Use [Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/postgres/manage-data-using-studio) or [psql](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip) to create the `parameterized_views` extension in any database where a parameterized view is created:
         
         -- Requires cloudsql.enable_parameterized_views set to on
         CREATE EXTENSION parameterized_views;
         

When the extension is created, a schema named `parameterized_views` is also created by the system so that the APIs are contained in that schema's namespace, and so that the APIs don't conflict with existing APIs.




## Create a parameterized secure view

To create a parameterized secure view, follow these steps:

  1. Run the `CREATE VIEW` DDL command using the `security_barrier` option:
         
         CREATE VIEW VIEW_NAME WITH (security_barrier) AS
         SELECT COLUMN_NAME, COLUMN_NAME__N_
         FROM TABLE_NAME ALIAS
         WHERE CONDITION;

Replace the following:

     * `VIEW_NAME`: the name of the parameterized secure view
     * `TABLE_NAME`: the name of the table to use in the parameterized secure view
     * `ALIAS`: the alias for the table name to use in the parameterized secure view
     * `COLUMN _NAME_` or `COLUMN_NAME _N_`: the name of the table column or columns to use in the parameterized secure view
     * `CONDITION`: the condition statement used to restrict application users so that they can only view the rows they're allowed to access. Add required parameters using the `$@PARAMETER_NAME` syntax in the `WHERE` clause. A common use case is checking the value of a column using `WHERE COLUMN = $@PARAMETER_NAME`.

`$@PARAMETER_NAME` indicates a named view parameter. Its value is provided when you use the `execute_parameterized_query` API. Named view parameters have the following requirements:

       * Named view parameters must begin with a letter (a-z) or an underscore (`_`).
       * Subsequent characters can be letters, underscores, or digits (`0`-`9`).
       * Named view parameters are case sensitive. For example, `$@PARAMETER_NAME` is interpreted differently than `$@parameter_name`.

The following is an example of creating a parameterized secure view that uses a named view parameter:
    
    CREATE VIEW user_specific_items WITH (security_barrier) AS
    SELECT item_id, item_name, description, owner_id
    FROM items t
    WHERE owner_id = $@app_user_id;
    

  2. Grant `SELECT` on the view to any database user that is allowed to query the view.

  3. Grant `USAGE` on the schema that contains the tables defined in the view to any database user that is allowed to query the view.




For more information, see [Secure and control access to application data using parameterized secure views](https://docs.cloud.google.com/sql/docs/postgres/secure-app-data-parameterized-secure-views).

## Configure security for your application

To configure security for your applications using parameterized secure views, follow these steps:

  1. Create the parameterized secure view as an administrative user. This is a Cloud SQL database user that performs administrative operations for the application.
  2. Create a new database role for executing queries against parameterized secure views. This is a Cloud SQL database role that the application uses to connect and sign into the database.

     1. Grant the new role permissions to the secure views, which typically includes `SELECT` privileges to the views and `USAGE` on the schemas.
     2. Limit the objects that this role can access to the minimum required set of public functions and objects that the application needs. Avoid providing access to schemas and tables that aren't public.

When you query the views, the application provides the values of the required view parameters, which are tied to the application user identity.

For more information, see [Create and manage users](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users).




## Query a parameterized secure view

To query a parameterized secure view, use one of the following options:

  * JSON-based: Use this API to run the query in one-shot and return JSON rows.
  * CURSOR-based: Use this API when you have longer running queries or when you have large queries and you want to fetch the result in batches.
  * `PREPARE .. AS RESTRICTED` statement: Use `PREPARE .. AS RESTRICTED` to define the query plan and then run `EXECUTE ... WITH VIEW PARAMETERS (...)` to execute it with specific parameters for the view.



### JSON API

Run the `execute_parameterized_query()` function, which has the following syntax:
    
    
    SELECT * FROM
    parameterized_views.execute_parameterized_query(
        query => SQL_QUERY,
        param_names => ARRAY [PARAMETER_NAMES],
        param_values => ARRAY [PARAMETER_VALUES]
    );
    

The function returns a table of JSON objects. Each row in the table is equivalent to the `row_to_json()` value of the original query result row.

Using this API limits the size of the result set by size (in KB) and by the number of rows. You can configure these limits by using `parameterized_views.json_results_max_size` and `parameterized_views.json_results_max_rows`.

### CURSOR API

Run the `execute_parameterized_query()` function with a cursor name, which creates and returns a transaction-scoped CURSOR:
    
    
    -- Must be in a transaction block
    BEGIN;
    
    SELECT * FROM
    parameterized_views.execute_parameterized_query(
        query => SQL_QUERY,
        cursor_name => CURSOR_NAME,
        param_names => ARRAY [PARAMETER_NAMES],
        param_values => ARRAY [PARAMETER_VALUES]
    );
    
    FETCH ALL FROM CURSOR_NAME;
    
    END;
    

### Prepared statements

The prepared statements method lets you prepare a query plan once and then execute it multiple times with different values for both the query's positional parameters and the view's named parameters.

To use a prepared statement, do the following:

  1. Create the prepared statement.
         
         -- Prepare the statement
         PREPARE PREPARED_STATEMENT_NAME (QUERY_PARAM_TYPE_1, QUERY_PARAM_TYPE_N)
         AS RESTRICTED SQL_QUERY;

Replace the following:

     * `PREPARED_STATEMENT_NAME`: the name of the prepared statement
     * `QUERY_PARAM_TYPE__N_`: the data type of the query parameter, such as `TEXT`
     * `SQL_QUERY`: the SQL query to execute as part of the prepared statement with the given value or values
  2. Execute the prepared statement.
         
         -- Execute the statement with query parameters and view parameters
         EXECUTE PREPARED_STATEMENT_NAME (QUERY_VALUE_1, QUERY_VALUE_N)
         WITH VIEW PARAMETERS (PARAMETER_NAME_1 := 'PARAMETER_VALUE_1', PARAMETER_NAME_N := 'PARAMETER_VALUE_N');

Replace the following:

     * `PREPARED_STATEMENT_NAME`: the name of the prepared statement.
     * `QUERY_VALUE__N_`: the value or values to provide as a parameter or parameters to the SQL query
     * `PARAMETER_NAME__N_`: the name of the named view parameter or parameters that you defined when you created the parameterized secure view. You create the named view parameter from the column of the table.
     * `PARAMETER_VALUE__N_`: the value or values for the named view parameter which restricts the parameterized secure view to the rows associated with the value.
  3. Clean up the prepared statement.
         
         -- Cleanup
         DEALLOCATE PREPARED_STATEMENT_NAME>;




The following example uses a parameterized secure view named `user_specific_items` which requires the named view parameter `$@app_user_id`.
    
    
    -- Prepare a query with a positional parameter $1 for the item_name pattern
    PREPARE get_items_by_name (TEXT) AS RESTRICTED
    SELECT item_id, item_name FROM user_specific_items
    WHERE item_name LIKE $1;
    

After you create the prepared statement, you can execute the prepared statement multiple times with and assign different values for both the query and the named view parameter.

For example, the first query execution:
    
    
    -- Execute for user 123, looking for items like '%Laptop%'
    EXECUTE get_items_by_name ('%Laptop%')
    WITH VIEW PARAMETERS (app_user_id := '123');
    

The second query execution:
    
    
    -- Execute for user 456, looking for items like '%Book%'
    EXECUTE get_items_by_name ('%Book%')
    WITH VIEW PARAMETERS (app_user_id := '456');
    

The `WITH VIEW PARAMETERS` clause is where the named view parameters (`123`, `456`) for the parameterized secure view are supplied, separate from the positional parameters for the prepared query (`%Laptop%`, `%Book%`).

Finally, clean up the prepared statement.
    
    
    -- Clean up the get_item_by_name prepared statement
    DEALLOCATE get_items_by_name;
    

### Restrictions on queries

The following lists the set of restricted operations for queries that you run using the options described in Query a parameterized secure view:

  * Read-only: Only read-only `SELECT` statements are allowed. DML (`INSERT`, `UPDATE`, `DELETE`) and DDL (`CREATE`, `ALTER`) are prohibited.
  * No Nesting: Recursive calls to `execute_parameterized_query` are prohibited.
  * Extension Limits: Certain extensions that start new background sessions (e.g., `dblink`, `pg_cron`) are disallowed.
  * `EXPLAIN` statements are disallowed to prevent potential information leakage using query plans.



## List all parameterized views

Use the `parameterized_views.all_parameterized_views` view to list all parameterized views (those containing at least one named parameter `$@...`).
    
    
    SELECT * FROM parameterized_views.all_parameterized_views;
    

## What's next

  * [Parameterized secure views overview](https://docs.cloud.google.com/sql/docs/postgres/parameterized-secure-views)


  * [Secure and control access to application data using parameterized secure views (Tutorial)](https://docs.cloud.google.com/sql/docs/postgres/secure-app-data-parameterized-secure-views)


  * [Context sets overview](https://docs.cloud.google.com/sql/docs/postgres/data-agent-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
