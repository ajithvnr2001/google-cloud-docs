---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/manage-application-data-security-parameterized-secure-views/
title: Manage application data security using AlloyDB Omni parameterized secure views \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.13.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:12:09.436412+00:00
---

# Manage application data security using AlloyDB Omni parameterized secure views  |  AlloyDB Omni for Kubernetes: 15.13.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/manage-application-data-security-parameterized-secure-views/

This page documents AlloyDB Omni version **15.13.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/overview)



Send feedback 

#  Manage application data security using AlloyDB Omni parameterized secure views Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.13.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/manage-application-data-security-parameterized-secure-views)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/manage-application-data-security-parameterized-secure-views)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/manage-application-data-security-parameterized-secure-views)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/manage-application-data-security-parameterized-secure-views)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/manage-application-data-security-parameterized-secure-views)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/manage-application-data-security-parameterized-secure-views)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/manage-application-data-security-parameterized-secure-views)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/manage-application-data-security-parameterized-secure-views)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/manage-application-data-security-parameterized-secure-views)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/manage-application-data-security-parameterized-secure-views)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/manage-application-data-security-parameterized-secure-views)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/manage-application-data-security-parameterized-secure-views)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/manage-application-data-security-parameterized-secure-views)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/manage-application-data-security-parameterized-secure-views)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/manage-application-data-security-parameterized-secure-views)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/manage-application-data-security-parameterized-secure-views)



**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use parameterized secure views in AlloyDB Omni to limit data access based on application-specific named parameters, like application user credentials. Parameterized secure views improve security and access control by extending the functionality of PostgreSQL views. These views also mitigate the risks of running untrusted queries from applications by automatically enforcing restrictions on any query that is executed.

For more information, see [Parameterized secure views overview](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/parameterized-secure-views-overview) and [Secure and control access to application data using parameterized secure views](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/secure-app-data-parameterized-secure-views).

## Before you begin

AlloyDB AI parameterized views support is provided through `parameterized_views`, which is an AlloyDB for PostgreSQL extension.

This page assumes that you installed AlloyDB Omni. See Install AlloyDB Omni ([for containers](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/deploy-vm), [for Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/deploy-kubernetes)).

Before you use parameterized secure views, you must do the following once in every new postgres container. Each setting can be applied using `ALTER SYSTEM` or by editing the `postgresql.conf` directly.

  1. Add `parameterized_views` to `shared_preload_libraries`.
  2. Enable the feature by setting `parameterized_views.enabled=on`.
  3. Restart the PostgreSQL server for the changes to take effect.
         
         -- See the current shared_preload_libraries
         SHOW shared_preload_libraries;
         ALTER SYSTEM SET shared_preload_libraries="...,parameterized_views";
         ALTER SYSTEM SET parameterized_views.enabled=on;
         

  4. Use [psql](https://docs.cloud.google.com/alloydb/docs/connect-psql) to create the `parameterized_views` extension in any database where you want to create a parameterized view:
         
         -- Requires parameterized_views.enabled set to true
         CREATE EXTENSION parameterized_views;
         

When the extension is created, a schema named `parameterized_views` is also created by the system so that the APIs are contained in that schema's namespace, and so that the APIs don't conflict with existing APIs.




## Create a parameterized secure view

To create a parameterized secure view, follow these steps:

  1. Run the [`CREATE VIEW`](https://www.postgresql.org/docs/current/sql-createview.html) DDL command, as shown in the following example:
         
         CREATE VIEW secure_checked_items WITH (security_barrier) AS
         SELECT bag_id, timestamp, location
         FROM checked_items t
         WHERE customer_id = $@app_end_userid;
         

In the preceding example, the parameterized secure view allows access to three columns from a table named `checked_items`. The view limits the results to rows where `checked_items.customer_id` matches a required parameter. Use the following attributes:

     * Create the view using the `security_barrier` option.
     * To restrict application users so that they can only view the rows they're allowed to access, add required parameters in the view definition using the `$@PARAMETER_NAME` syntax. A common use case is checking the value of a column in the `WHERE` clause using `COLUMN = $@PARAMETER_NAME`.
     * `$@PARAMETER_NAME` indicates a named view parameter. Its value is provided when you use the `execute_parameterized_query` API. Named view parameters have the following requirements: 
       * Named view parameters must begin with a letter (a-z).
       * You can use letters with diacritical marks and non-Latin letters, and you can use an underscore (`_`).
       * Subsequent characters can be letters, underscores, or digits (`0-9`).
       * Named view parameters can't contain `$`.
       * Named view parameters are case sensitive. For example, `$@PARAMETER_NAME` is interpreted differently than `$@parameter_name`.
  2. Grant `SELECT` on the view to any database user that is allowed to query the view.

  3. Grant `USAGE` on the schema that contains the tables defined in the view to any database user that is allowed to query the view.




For more information, see [Secure and control access to application data using parameterized secure views](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/secure-app-data-parameterized-secure-views).

## Configure security for your application

To configure security for your applications using parameterized secure views, follow these steps:

  1. Create the secure parameterized views as an administrative user. This user is an AlloyDB Omni database user that performs administrative operations for the application, including database setup and security administration.
  2. Create a new database role for executing queries against parameterized secure views. This is an AlloyDB Omni database role that the application uses to connect and sign into the database, and to execute queries against parameterized views.
  3. Grant the new role permissions to the secure views, which typically includes `SELECT` privileges to the views and `USAGE` on the schemas.
  4. Limit the objects that this role can access to the minimum required set of public functions and objects that the application needs. Avoid providing access to schemas and tables that aren't public.
  5. When you query the views, the application provides the values of the required view parameters, which are tied to the application user identity.



## Query a parameterized secure view

To query a parameterized secure view, use one of the following options that best supports your use case:

  * JSON-based: Use this API to run the query in one-shot and return JSON rows.
  * CURSOR-based: Use this API when you have longer running queries or when you have large queries and you want to fetch the result in batches. The `execute_parameterized_query` function provided by the `parameterized_views` extension accepts a cursor name.
  * `PREPARE EXECUTE` statement: Use this for prepared statements that can be executed multiple times with different parameters values.



To query parameterized secure views, you use the `execute_parameterized_query()` function provided by the `parameterized_views` extension.

### JSON API

This API has limitations because it declares a cursor for the given query. As a result, the query must be compatible with [PostgreSQL cursors](https://www.postgresql.org/docs/16/plpgsql-cursors.html). For example, the CURSOR API doesn't support `DO` or `SHOW` statements.

This API also doesn't restrict the results by size or by the number of rows returned.

Run the `execute_parameterized_query()` function, which has the following syntax:
    
    
    SELECT * FROM
    parameterized_views.execute_parameterized_query(
        query => SQL_QUERY,
        param_names => ARRAY [PARAMETER_NAMES],
        param_values => ARRAY [PARAMETER_VALUES]
    )
    

Replace the following:

  * `SQL_QUERY`: a SQL query whose `FROM` clause refers to one or more parameterized secure views.
  * `PARAMETER_NAMES`: a list of parameter names to pass in as strings.
  * `PARAMETER_VALUES`: a list of parameter values to pass in. 
    * This list must be the same size as the `param_names` list, where the order of the values matches the order of the names.
    * The exact type of the values is inferred from the query and parameterized view definition. Type conversions are performed when needed and when possible for the given parameter value. In case of a type-mismatch, an error is thrown.



The function returns a table of JSON objects. Each row in the table is equivalent to the `ROW_TO_JSON()` value of the original query result row.

Use the following example to query a parameterized secure view:
    
    
    SELECT * FROM
    parameterized_views.execute_parameterized_query(
        query => 'SELECT * FROM secure_checked_items',
        param_names => ARRAY ['app_end_userid'],
        param_values => ARRAY ['40']
    )
    

Using this API limits the size of the result set by size expressed in kilobytes (kB) of the results and by the number of rows. You can configure these limits by using `parameterized_views.json_results_max_size` and `parameterized_views.json_results_max_rows`.

This API has limitations because it declares a cursor for the given query. As a result, the query must be compatible with [PostgreSQL cursors](https://www.postgresql.org/docs/16/plpgsql-cursors.html). For example, the CURSOR API doesn't support `DO` or `SHOW` statements.

This API also doesn't restrict the results by size or by the number of rows returned.

Run the `execute_parameterized_query()` function, which has the following syntax:
    
    
    SELECT * FROM
    parameterized_views.execute_parameterized_query(
        query => SQL_QUERY,
        param_names => ARRAY [PARAMETER_NAMES],
        param_values => ARRAY [PARAMETER_VALUES]
    )
    

Replace the following:

  * `SQL_QUERY`: a SQL query whose `FROM` clause refers to one or more parameterized secure views.
  * `PARAMETER_NAMES`: a list of parameter names to pass in as strings.
  * `PARAMETER_VALUES`: a list of parameter values to pass in.
  * This list must be the same size as the `param_names` list, where the order of the values matches the order of the names.
  * The exact type of the values is inferred from the query and parameterized view definition. Type conversions are performed when needed and when possible for the given parameter value. In case of a type-mismatch, an error is thrown.



The function returns a table of JSON objects. Each row in the table is equivalent to the `ROW_TO_JSON()` value of the original query result row.

Use the following example to query a parameterized secure view:
    
    
    SELECT * FROM
    parameterized_views.execute_parameterized_query(
        query => 'SELECT * FROM secure_checked_items',
        param_names => ARRAY ['app_end_userid'],
        param_values => ARRAY ['40']
    )
    
    

Using this API limits the size of the result set by size expressed in kilobytes (kB) of the results and by the number of rows. You can configure these limits by using `parameterized_views.json_results_max_size` and `parameterized_views.json_results_max_rows`.

### CURSOR API

This API has limitations because it declares a cursor for the given query. As a result, the query must be compatible with [PostgreSQL cursors](https://www.postgresql.org/docs/16/plpgsql-cursors.html). For example, the CURSOR API doesn't support `DO` or `SHOW` statements.

This API also doesn't restrict the results by size or by the number of rows returned.

Run the `execute_parameterized_query()` function, which has the following syntax:
    
    
    SELECT * FROM
    parameterized_views.execute_parameterized_query(
        query => SQL_QUERY,
        param_names => ARRAY [PARAMETER_NAMES],
        param_values => ARRAY [PARAMETER_VALUES]
    )
    

Replace the following:

  * `SQL_QUERY`: a SQL query whose `FROM` clause refers to one or more parameterized secure views.
  * `PARAMETER_NAMES`: a list of parameter names to pass in as strings.
  * `PARAMETER_VALUES`: a list of parameter values to pass in. 
    * This list must be the same size as the `param_names` list, where the order of the values matches the order of the names.
    * The exact type of the values is inferred from the query and parameterized view definition. Type conversions are performed when needed and when possible for the given parameter value. In case of a type-mismatch, an error is thrown.



The function returns a table of JSON objects. Each row in the table is equivalent to the `ROW_TO_JSON()` value of the original query result row.

Use the following example to query a parameterized secure view:
    
    
    SELECT * FROM
    parameterized_views.execute_parameterized_query(
        query => 'SELECT * FROM secure_checked_items',
        param_names => ARRAY ['app_end_userid'],
        param_values => ARRAY ['40']
    )
    

Using this API limits the size of the result set by size expressed in kilobytes (kB) of the results and by the number of rows. You can configure these limits by using `parameterized_views.json_results_max_size` and `parameterized_views.json_results_max_rows`.

### PREPARE statement

Use the `PREPARE .. AS RESTRICTED` command to create a prepared statement that references parameterized views. These prepared statements support positional parameters and enforce various restrictions when you execute them. For more information, see [Security mechanism](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/parameterized-secure-views-overview#security-mechanism).

This feature extends the `PREPARE` and `EXECUTE` commands to support named view parameters. Use prepared statements to avoid the overhead of parsing, analyzing, and rewriting each time the statement is executed, which can result in significant performance gains, especially for frequently executed or complex queries. A prepared statement is a server-side object that can optimize performance by pre-compiling and storing a parameterized SQL statement for later execution.

This API has limitations because the statement must be allowed in a `PREPARE` statement, which means that only `SELECT` and `VALUES` statements are supported.

This API also doesn't restrict the results by size or number of rows returned.

To create a prepared statement that references parameterized views, run the `PREPARE .. AS RESTRICTED` command:
    
    
    PREPARE pquery (/POSITIONAL_PARAM_TYPES/)
            AS RESTRICTED query % a query that may refer to parameterized views
    EXECUTE pquery (/POSITIONAL_PARAM_VALUES/)
          WITH VIEW PARAMETERS (VIEW_PARAM_NAME1 = VIEW_PARAM_VALUE1[, ...]);
    

Replace the following:

  * `POSITIONAL_PARAM_TYPES`: one or more positional parameters that are used in the `RESTRICTED` query.
  * `POSITIONAL_PARAM_VALUES`: the actual values that are substituted for the positional parameters defined in the `PREPARE` statement.
  * `VIEW_PARAM_NAME`: the name of the parameter expected by the parameterized views referenced in the `RESTRICTED` query.
  * `VIEW_PARAM_VALUE`: the actual values being passed to the corresponding `viewParamName` parameters of the parameterized views.



To include parameters in a prepared statement, you supply a list of data types in the `PREPARE` statement. In the statement that you prepare, you refer to the parameters by position using, for example, `$1` and `$2`.

**Note:** You can't use named view parameters directly in the `PREPARE` statement.

Use the `EXECUTE .. WITH VIEW PARAMETERS` command to execute a previously prepared statement that you created using the `PREPARE .. AS RESTRICTED` command. If the `PREPARE` statement that created the statement specified positional parameters, then you must pass a compatible set of parameters to the `EXECUTE` statement. You must pass any named view parameters required by parameterized views in the `WITH VIEW PARAMETERS` clause.

Use the following example to query a parameterized secure view:
    
    
      PREPARE pquery (timestamp) AS RESTRICTED SELECT * FROM secure_checked_items WHERE timestamp > $1;
    
      EXECUTE pquery (current_date - 1) WITH VIEW PARAMETERS (app_end_userid = 40);
      EXECUTE pquery (current_date - 30) WITH VIEW PARAMETERS (app_end_userid = 40);
      ```
    

## Enforced restrictions on queries

The following lists the set of restricted operations for queries that you run using the options described in [Query a parameterized secure view](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/manage-application-data-security-parameterized-secure-views#query-parameterized-secure-view):

  * Any recursive invocation of any APIs—`execute_parameterized_query` or by using `EXECUTE .. WITH VIEW PARAMETERS`— is prohibited, so that only the values specified by the application are used. This restriction also prevents the query from being used to circumvent the security envelope of the given set of parameter values.
  * Some extensions that start a new background session are disallowed, including the `dblink, pg_cron` and `pg_background` extensions.
  * The following lists the set of query constructs permitted that are restricted:

    * Read-only `SELECT` statements are allowed.
    * Read-only `SHOW` statements, `CALL` statements, and `DO` statements are allowed.
    * DML statements such as `INSERT, UPDATE`, and `DELETE` aren't allowed.
    * DDL statements such as `CREATE TABLE` and `ALTER TABLE` aren't allowed.
    * Other statement types such as `LOAD, SET, CLUSTER, LOCK, CHECKPOINT`, and `EXPLAIN` aren't allowed.
  * `EXPLAIN` statements are disallowed to avoid the possibility of covert channel attacks using query plans. For more information, see [Covert channel](https://en.wikipedia.org/wiki/Covert_channel).

  * Parameterized secure views provide settings to help you manage resources that are used by the APIs to query parameterized views, such as `parameterized_views.statement_timeout`. For more information, see [AlloyDB for PostgreSQL flags](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/alloydb-flags).




## List all parameterized views

Use the `parameterized_views` extension to list all the parameterized views in the database by using the `all_parameterized_views` view. The output of this view is the same as the [`pg_views`](https://www.postgresql.org/docs/16/view-pg-views.html) catalog view, but `all_parameterized_views` only lists views with named view parameters.

To list parameterized views, use the following example:
    
    
    postgres=# select * from parameterized_views.all_parameterized_views ;
    schemaname |      viewname      | viewowner |                       definition
    -----------+--------------------+-----------+---------------------------------------------------------
    public     | checked_items_view | postgres  |  SELECT checked_items.bag_id,                          +
               |                    |           |     checked_items."timestamp",                         +
               |                    |           |     checked_items.location                             +
               |                    |           |    FROM checked_items                                  +
               |                    |           |   WHERE (checked_items.customer_id = $@app_end_userid);
    

To list a parameterized view in `all_parameterized_views`, make sure that the parameterized view contains at least one named view parameter in its definition.

## What's next

  * Learn about [parameterized secure views](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/parameterized-secure-views-overview).

  * Learn how to [secure and control access to application data using parameterized secure views](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/secure-app-data-parameterized-secure-views).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
