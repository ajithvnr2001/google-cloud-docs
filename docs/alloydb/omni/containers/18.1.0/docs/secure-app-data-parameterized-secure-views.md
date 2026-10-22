---
url: https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/secure-app-data-parameterized-secure-views/
title: Secure and control access to application data using parameterized secure views \u00a0|\u00a0 AlloyDB Omni using containers: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:37:27.155795+00:00
---

# Secure and control access to application data using parameterized secure views  |  AlloyDB Omni using containers: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/secure-app-data-parameterized-secure-views/

This page documents AlloyDB Omni version **18.1.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/overview)



Send feedback 

#  Secure and control access to application data using parameterized secure views Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/secure-app-data-parameterized-secure-views)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/secure-app-data-parameterized-secure-views)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/secure-app-data-parameterized-secure-views)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/secure-app-data-parameterized-secure-views)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/secure-app-data-parameterized-secure-views)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/secure-app-data-parameterized-secure-views)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/secure-app-data-parameterized-secure-views)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/secure-app-data-parameterized-secure-views)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/secure-app-data-parameterized-secure-views)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/secure-app-data-parameterized-secure-views)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/secure-app-data-parameterized-secure-views)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/secure-app-data-parameterized-secure-views)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/secure-app-data-parameterized-secure-views)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/secure-app-data-parameterized-secure-views)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/secure-app-data-parameterized-secure-views)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/secure-app-data-parameterized-secure-views)

This tutorial describes how to use parameterized secure views in AlloyDB Omni to restrict user access to parameterized views using AlloyDB Omni Studio or psql. 

Examples are included to illustrate the capabilities of parameterized secure views. These examples are intended for demonstration purposes only.

## Objectives

  * Create secure parameterized views with named view parameters.
  * Create the database role that is used by the application to connect to the database and access parameterized secure views.
  * Grant the new role permissions to the secure views and revoke access to the base tables.
  * Connect using the new role and verify that the restricted tables can't be accessed.
  * Run queries on the parameterized secure view using the `execute_parameterized_query` function.



## Install and connect to a database

  1. Install AlloyDB Omni [using containers](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/quickstart).

  2. [Create a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#create-cluster).

  3. Connect to your instance [using containers](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/run-connect#connect).




## Prepare your environment

To prepare for running queries on a parameterized secure view, you must first set up parameterized views, the database and database roles, the `parameterized_view` extension, and the application schema.

Before you use parameterized secure views, you must do the following once in every new postgres container. Each setting can be applied using `ALTER SYSTEM` or by editing the `postgresql.conf` directly.:

  1. Add "parameterized_views" to `shared_preload_libraries`.
  2. Enable the feature by setting `parameterized_views.enabled=on`.
  3. Restart postgres for the changes to take effect.



### Set up the database

  * Create a database called `database` for the application data and parameterized views.



### Create database roles, the extension, and the application schema

  1. Using psql, connect to the database as the `postgres` user or as a user with AlloyDB Omni [superuser](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/database-users/overview) privileges.
         
         psql database -U postgres
         

  2. Create the `parameterized_views` extension in the database.
         
         -- Requires parameterized_views.enabled set to true
         CREATE EXTENSION parameterized_views;
         

When the extension is created, the system also creates a schema named `parameterized_views` so that the APIs are contained in that schema's namespace and so that those APIs don't conflict with existing APIs.

**Note:** You must create an extension in every database in which parameterized views are created.
  3. Create the AlloyDB Omni administrative role, which owns and manages the database.
         
         CREATE ROLE admin_user WITH LOGIN PASSWORD '...';
         GRANT ALL PRIVILEGES ON DATABASE database TO admin_user;
         

For more information, see [`CREATE USER`](https://www.postgresql.org/docs/15/sql-createuser.html).

  4. Create a new database role for executing queries against parameterized secure views. This is an AlloyDB Omni role that the application uses to connect and sign into the database to execute queries with limited access to public functions or objects to the minimal required set.

For more information, see [`CREATE USER`](https://www.postgresql.org/docs/15/sql-createuser.html).

  5. Connect as the administrative user.
         
         SET role TO admin_user;
         

  6. Create the schema that contains the tables.
         
         CREATE SCHEMA schema;
         

  7. Create the tables and insert data.
         
         CREATE TABLE schema.checked_items(bag_id INT,timestamp TIMESTAMP, loc_code CHAR(3), scan_type CHAR(1), location TEXT, customer_id INT);
         
         INSERT INTO schema.checked_items (bag_id, timestamp, loc_code, scan_type, location, customer_id) VALUES
         (101, '2023-10-26 10:00:00', 'ABC', 'I', 'Warehouse A', 123),
         (102, '2023-10-26 10:15:30', 'DEF', 'O', 'Loading Dock B', 456),
         (103, '2023-10-26 10:30:45', 'GHI', 'I', 'Conveyor Belt 1', 789),
         (104, '2023-10-26 11:00:00', 'JKL', 'O', 'Shipping Area C', 101),
         (105, '2023-10-26 11:45:15', 'MNO', 'I', 'Sorting Station D', 202),
         (106, '2023-10-26 12:00:00', 'PQR', 'O', 'Truck Bay E', 303);
         




## Create secure parameterized views and set up access privileges

To create secure parameterized views and to set up appropriate access privileges for the base table and views, follow these steps:

  1. Using psql, connect to the database as `admin_user`.
         
         psql database -U admin_user
         

  2. To provide limited access to the view, create a parameterized secure view.
         
         CREATE VIEW schema.secure_checked_items WITH (security_barrier) AS
         SELECT bag_id, timestamp, location
         FROM schema.checked_items t
         WHERE customer_id = $@app_end_userid;
         

  3. Grant access to the view.
         
         GRANT SELECT ON schema.secure_checked_items TO psv_user;
         

  4. To access the view, grant access to the schema.
         
         GRANT USAGE ON SCHEMA schema TO psv_user;
         

  5. Revoke direct access to the base table.
         
         REVOKE ALL PRIVILEGES ON schema.checked_items FROM psv_user;
         




## Verify data security

To verify that the parameterized secure views are restricting access to the designated views, run the following commands as `psv_user`. This is an AlloyDB Omni database role that the application uses to connect and sign into the database to execute queries.

  1. Connect as a parameterized secure views user.

`sql psql database -U psv_user`
  2. Verify that the base table can't be accessed.
         
         SELECT * FROM schema.checked_items;
         ERROR:  permission denied for table checked_items
         

  3. Access the parameterized secure view using the `execute_parameterized_query` function.
         
         SELECT * FROM parameterized_views.execute_parameterized_query(
           query => 'SELECT * from schema.secure_checked_items',
           param_names => ARRAY ['app_end_userid'],
           param_values => ARRAY ['303']
         );
         

  4. To improve security for natural language generated queries, integrate your parameterized secure views using natural language.




## Clean up

To clean up, you can either uninstall the AlloyDB Omni instance or keep the instance and delete the individual objects.

## What's next

  * Learn about [parameterized secure views](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/parameterized-secure-views-overview).
  * Learn how to [manage application data security using parameterized secure views](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/manage-application-data-security-parameterized-secure-views).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
