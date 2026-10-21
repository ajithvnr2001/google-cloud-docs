---
url: https://docs.cloud.google.com/sql/docs/postgres/secure-app-data-parameterized-secure-views/
title: Secure and control access to application data using parameterized secure views \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:26.199259+00:00
---

# Secure and control access to application data using parameterized secure views  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/secure-app-data-parameterized-secure-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Secure and control access to application data using parameterized secure views Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This tutorial describes how to use parameterized secure views in Cloud SQL for PostgreSQL to restrict user access to parameterized views using [Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/postgres/manage-data-using-studio) or psql.

## Objectives

  * Create secure parameterized views with named view parameters.
  * Create the database role that is used by the application to connect to the database and access parameterized secure views.
  * Grant the new role permissions to the secure views and revoke access to the base tables.
  * Connect using the new role and verify that the restricted tables can't be accessed.
  * Run queries on the parameterized secure view using the `execute_parameterized_query` function.



## Prepare your environment

  1. Enable the `cloudsql.enable_parameterized_views` database flag for your Cloud SQL instance. This flag change requires a database restart.

  2. Connect to your database as the `postgres` user.
         
         psql -U postgres
         

  3. Create the `parameterized_views` extension in the database.
         
         CREATE EXTENSION parameterized_views;
         

  4. Create a new database role for executing queries.
         
         CREATE ROLE psv_user WITH LOGIN PASSWORD 'PASSWORD';
         

  5. Create a schema and a table for the application data.
         
         CREATE SCHEMA app_schema;
         CREATE TABLE app_schema.items(item_id INT, item_name TEXT, description TEXT, owner_id INT);
         
         INSERT INTO app_schema.items (item_id, item_name, description, owner_id) VALUES
         (1, 'Book', 'A great read', 123),
         (2, 'Laptop', 'Work machine', 456),
         (3, 'Pencil', 'For writing', 123);
         




## Create secure parameterized views and set up access privileges

  1. Create a parameterized secure view:
         
         CREATE VIEW app_schema.user_items_view WITH (security_barrier) AS
         SELECT item_id, item_name, description
         FROM app_schema.items
         WHERE owner_id = $@current_user_id;
         

  2. Grant access to the view and schema to the application role.
         
         GRANT USAGE ON SCHEMA app_schema TO psv_user;
         GRANT SELECT ON app_schema.user_items_view TO psv_user;
         

  3. Revoke direct access to the base table.
         
         REVOKE ALL PRIVILEGES ON app_schema.items FROM psv_user;
         




## Verify data security

  1. Connect as the `psv_user`.
         
         psql -U psv_user -d postgres
         

  2. Verify that the base table can't be accessed.
         
         SELECT * FROM app_schema.items;
         -- ERROR:  permission denied for table items
         

  3. Access the parameterized secure view using the `execute_parameterized_query` function:
         
         SELECT * FROM parameterized_views.execute_parameterized_query(
           query => 'SELECT * from app_schema.user_items_view',
           param_names => ARRAY ['current_user_id'],
           param_values => ARRAY ['123']
         );
         

The result should only include items where `owner_id` is `123`.




## What's next

  * Learn about [parameterized secure views overview](https://docs.cloud.google.com/sql/docs/postgres/parameterized-secure-views).
  * Learn how to [manage application data security using parameterized secure views](https://docs.cloud.google.com/sql/docs/postgres/use-parameterized-secure-views).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
