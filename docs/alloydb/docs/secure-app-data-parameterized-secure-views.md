---
url: https://docs.cloud.google.com/alloydb/docs/secure-app-data-parameterized-secure-views/
title: Secure and control access to application data using parameterized secure views \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:30:35.722405+00:00
---

# Secure and control access to application data using parameterized secure views  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/secure-app-data-parameterized-secure-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Secure and control access to application data using parameterized secure views Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This tutorial describes how to use parameterized secure views in AlloyDB for PostgreSQL to restrict user access to parameterized views using AlloyDB Studio or psql.

Examples are included to illustrate the capabilities of parameterized secure views. These examples are intended for demonstration purposes only.

## Objectives

  * Create secure parameterized views with named view parameters.
  * Create the database role that is used by the application to connect to the database and access parameterized secure views.
  * Grant the new role permissions to the secure views and revoke access to the base tables.
  * Connect using the new role and verify that the restricted tables can't be accessed.
  * Run queries on the parameterized secure view using the `execute_parameterized_query` function.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

### Enable billing and required APIs

  1. In the Google Cloud console, select a project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Make sure that billing is enabled for your Google Cloud project.](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project)

  3. Enable the Cloud APIs necessary to create and connect to AlloyDB for PostgreSQL.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=alloydb.googleapis.com)

     1. In the **Confirm project** step, click **Next** to confirm the name of the project you are going to make changes to.
     2. In the **Enable APIs** step, click **Enable** to enable the following:

        * AlloyDB API



### Create and connect to a database

  1. [Create a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#create-cluster).
  2. [Connect to your instance and create a database](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#run).



## Prepare your environment

To prepare for running queries on a parameterized secure view, you must first set up parameterized views, the database and database roles, the `parameterized_view` extension, and the application schema.

### Enable the required extension

Enable the `parameterized_views.enabled` database flag, which loads the required extension libraries. For more information, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

**Note:** After you enable the `parameterized_views.enabled` database flag, your database restarts to make these changes take effect.

### Set up the database

  * Create a database called `database` for the application data and parameterized views. For more information, see [Create a database](https://docs.cloud.google.com/alloydb/docs/database-create).



### Create database roles, the extension, and the application schema

  1. Using [AlloyDB Studio](https://docs.cloud.google.com/alloydb/docs/manage-data-using-studio) or [psql](https://docs.cloud.google.com/alloydb/docs/connect-psql), connect to the database as the `postgres` user or as a user with [AlloyDB superuser](https://docs.cloud.google.com/alloydb/docs/database-users/overview#alloydbsuperuser) privileges.
         
         psql database -U postgres
         

For more information, see [About database user management in AlloyDB](https://docs.cloud.google.com/alloydb/docs/database-users/overview).

  2. Create the `parameterized_views` extension in the database.
         
         -- Requires parameterized_views.enabled set to true
         CREATE EXTENSION parameterized_views;
         

When the extension is created, the system also creates a schema named `parameterized_views` so that the APIs are contained in that schema's namespace and so that those APIs don't conflict with existing APIs.

**Note:** You must create an extension in every database in which parameterized views are created.
  3. Create the AlloyDB administrative role, which owns and manages the database.
         
         CREATE ROLE admin_user WITH LOGIN PASSWORD '...';
          GRANT ALL PRIVILEGES ON DATABASE database TO admin_user;
         

For more information, see [`CREATE USER`](https://www.postgresql.org/docs/15/sql-createuser.html).

  4. Create a new database role for executing queries against parameterized secure views. This is an AlloyDB role that the application uses to connect and sign into the database to execute queries with limited access to public functions or objects to the minimal required set.
         
         CREATE ROLE psv_user WITH LOGIN PASSWORD '...';
         

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

  1. Using [AlloyDB Studio](https://docs.cloud.google.com/alloydb/docs/manage-data-using-studio) or [psql](https://docs.cloud.google.com/alloydb/docs/connect-psql), connect to the database as `admin_user`.
         
         psql database -U admin_user
         

  2. To provide limited access to the view, create a parameterized secure view:
         
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

To verify that the parameterized secure views are restricting access to the designated views, run the following commands as `psv_user`. This is a AlloyDB database role that the application uses to connect and sign into the database to execute queries.

  1. Connect as a parameterized secure views user.
         
         psql database -U psv_user
         

  2. Verify that the base table can't be accessed.
         
         SELECT * FROM schema.checked_items;
         ERROR:  permission denied for table checked_items
         

  3. Access the parameterized secure view using the `execute_parameterized_query` function:
         
         SELECT * FROM parameterized_views.execute_parameterized_query(
           query => 'SELECT * from schema.secure_checked_items',
           param_names => ARRAY ['app_end_userid'],
           param_values => ARRAY ['303']
         );
         

  4. To improve security for natural language generated queries, integrate your parameterized secure views using [AlloyDB AI natural language](https://docs.cloud.google.com/alloydb/docs/ai/generate-sql-queries-natural-language).




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click the name of your cluster, `my-cluster`, in the **Resource name** column.

  3. Click _delete_ **Delete cluster**.

  4. In **Delete cluster my-cluster** , enter `my-cluster` to confirm you want to delete your cluster.

  5. Click **Delete**.

  6. If you created a private connection when you created a cluster, go to the Google Cloud console [Networking page](https://console.cloud.google.com/networking/networks/details/default) and click **Delete VPC network**.

  7. Using [AlloyDB Studio](https://docs.cloud.google.com/alloydb/docs/manage-data-using-studio) or [psql](https://docs.cloud.google.com/alloydb/docs/connect-psql), connect to the database as `postgres`.
         
         psql database -U postgres
         

  8. Drop the objects that you created.
         
         DROP VIEW schema.secure_checked_items;
         DROP TABLE schema.checked_items;
         DROP SCHEMA schema;
         DROP ROLE psv_user;
         DROP ROLE admin_user;
         DROP EXTENSION parameterized_views;
         




## What's next

  * Learn about [parameterized secure views](https://docs.cloud.google.com/alloydb/docs/parameterized-secure-views-overview).
  * Learn how to [manage application data security using parameterized secure views](https://docs.cloud.google.com/alloydb/docs/manage-application-data-security-parameterized-secure-views).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
