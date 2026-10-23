---
url: https://docs.cloud.google.com/sql/docs/mysql/use-parameterized-secure-views/
title: Use parameterized secure views \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:37.756849+00:00
---

# Use parameterized secure views  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/use-parameterized-secure-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Use parameterized secure views Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/use-parameterized-secure-views "View this page for the PostgreSQL database engine") | SQL Server

**Preview — Parameterized secure views**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to use parameterized secure views in Cloud SQL for MySQL, which let you limit data access based on application-specific named parameters, like application user credentials. Parameterized secure views improve security and access control by extending the functionality of MySQL views. These views also mitigate the risks of running untrusted queries from applications by enforcing a number of restrictions automatically on any query that is executed.

For more information, see [Parameterized secure views in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/parameterized-secure-views).

## Before you begin

This document assumes that you've already created a Cloud SQL for MySQL instance.

  1. Make sure that your Cloud SQL instance is running MySQL 8.0.43 or later. If your MySQL 8.0 instance is running an earlier minor version, then you can perform a [minor version upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-versio).

  2. Enable the `cloudsql_parameterized_secure_view` database flag for your instance.

This flag change doesn't require a database restart. For more information, see [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags).




## Create a parameterized secure view

To create a parameterized secure view, run the `CREATE VIEW` DDL command. For example:
    
    
    CREATE VIEW v_orders
    AS SELECT * FROM orders
    WHERE customer_id = @local_customer_id;
    

Use the following syntax:
    
    
    -- Create a view with a parameter using the WHERE clause
    CREATE VIEW VIEW_NAME AS
    SELECT * FROM TABLE_NAME
    WHERE CONDITION;
    
    
    -- Create a view with a parameter using the HAVING clause
    CREATE VIEW VIEW_NAME AS
    SELECT * FROM TABLE_NAME
    WHERE CONDITION_1      -- row level security
    GROUP BY COLUMN_NAME
    HAVING CONDITION_2;    -- grouping
    
    
    -- Create a view with a parameter using the ON clause
    CREATE VIEW VIEW_NAME AS
    SELECT * FROM TABLE_NAME_1
    JOIN TABLE_NAME_2
    ON CONDITION_1       --  join criteria
    WHERE CONDITION_2;   --  row level security

Replace the following:

  * `VIEW_NAME`: the name of the parameterized secure view
  * `TABLE_NAME` or `TABLE_NAME__N_`: the name of the table or tables to use in the parameterized view
  * `COLUMN_NAME` or `COLUMN_NAME__N_`: the name of the table column or columns to use in the parameterized view
  * `CONDITION` or `CONDITION__N_`: the condition statement or statements to evaluate as part of a `WHERE`, `ON`, or `HAVING` clause. You can specify the session variable that is used as the parameter when you later perform a query on the view. A condition resembles the following:
        
        WHERE customer_id = @local_customer_id

Session variables, `@variable_name`, are permitted only within the `WHERE`, `ON`, or `HAVING` clauses of a `CREATE VIEW` statement.




## Query a parameterized secure view

To query a parameterized secure view in Cloud SQL for MySQL, you have two options:

  * Assign values to variables by using the `SET_VIEW_VARS` hint while querying the parameterized secure view. If any of the variables that are referenced by the view aren't set, or if any unrelated variables appear in the `SET_VIEW_VARS` hint, then the query against the parameterized secure view fails.

  * Call the `mysql.execute_parameterized_query` procedure to query the parameterized secure view. If you use the `mysql.execute_parameterized_query` procedure, then you provide two arguments to the procedure. The first argument is a query against the parameterized secure view without any hints about the session variable. The second argument provides all the needed session variables and the values that you want to provide.




### Use hint values

To query the parameterized secure view by using the `SET_VIEW_VARS` hint, do the following:
    
    
    -- Set the parameter and query
    SELECT /*+ SET_VIEW_VARS(SESSION_VARIABLE = VALUE) */ *
    FROM VIEW_NAME;

Replace the following:

  * `SESSION_VARIABLE`: the named parameter of the parameterized secure view that you can provide different values for. You define the session variable name when you create the view by using the `@variable_name` notation in the view condition clause.
  * `VALUE`: a value for this named parameter
  * `VIEW_NAME`: name of the parameterized secure view



For example:
    
    
    SELECT /*+ SET_VIEW_VARS(local_customer_id = 12345) */ *
    FROM v_orders;
    

### Use the parameterized query procedure

To query the parameterized secure view by using the `mysql.execute_parameterized_query` procedure, use the following syntax:
    
    
    CALL mysql.execute_parameterized_query(
      'SELECT * FROM DATABASE_NAME.VIEW_NAME',
      'SESSION_VARIABLE=VALUE');

Replace the following:

  * `SESSION_VARIABLE`: the named parameter of the parameterized secure view that you can provide different values for. You define the session variable name when you create the view by using the `@variable_name` notation in the view condition clause.
  * `VALUE`: a value for this named parameter
  * `DATABASE_NAME`: name of the database of the view
  * `VIEW_NAME`: name of the parameterized secure view



For example:
    
    
       CALL mysql.execute_parameterized_query(
        'SELECT * FROM db.v_orders',
        'local_customer_id = 5, earliest_year = 2021');
    

### Restrictions on queries

The following lists the set of restricted operations for queries that you run using the options described in Query a parameterized secure view:

  * The query can only be a `SELECT` statement.
  * The query can't include invocations to user-defined functions or stored procedures.
  * The query can't assign variables.
  * If you use the `CALL mysql.execute_parameterized_query` method, then the query can't be multiple statements concatenated into a single statement. For example, the query statement `SELECT * FROM a; DROP TABLE a;` isn't valid.



## View parameterized secure views in logs

When Cloud SQL for MySQL database users try to create a parameterized secure view, an information-level message is logged in the MySQL error log similar to the following:
    
    
     User variables permitted in %s.%s through Parameterized
     Secure View feature
    

## Troubleshoot parameterized secure views

Issue | Troubleshooting |  `cloud_parameterized_secure_view` flag isn't set for the instance  |  If the `cloudsql_parameterized_secure_view` flag is set to `OFF`, then any attempt to query an existing parameterized secure view will result in the following error: `Cannot operate on a Parameterized Secure View without `cloudsql_parameterized_secure_view` being set. Please turn the flag on first before querying Parameterized Secure Views` If you attempt to create a parameterized secure view without the flag set, then you receive the following error: `View's SELECT contains a variable or parameter` You can verify whether the parameterized secure views is enabled for a Cloud SQL instance by checking the global variable:
    
    
    SHOW VARIABLES LIKE 'cloudsql_parameterized_secure_view';  
  
---|---  
Query fails with the error `View's SELECT contains a variable or parameter`. | Variables aren't allowed outside of `WHERE`, `HAVING`, or `ON` clauses. Using a variable outside of these clauses results in an error.  
Query fails with `User variable `%s` used in Parameterized Secure View %s must be set in the query before using SET_VIEW_VARS hint` error  | Set the session variable before you run the query.  
Query fails with a MySQL version error  | If you try to query an existing parameterized secure view from a MySQL version earlier than 8.0.43, then you can encounter the following error: `Variable %s found in view %s. Please upgrade to 8.0.43 or above to use Parameterized Secure Views`  
  
## What's next

  * [Parameterized secure views overview](https://docs.cloud.google.com/sql/docs/mysql/parameterized-secure-views)


  * [Context sets overview](https://docs.cloud.google.com/sql/docs/mysql/data-agent-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
