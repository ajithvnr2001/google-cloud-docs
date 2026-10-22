---
url: https://docs.cloud.google.com/gemini/data-agents/querydata/sql-mysql/secure-app-data-parameterized-secure-views-qd/
title: Secure and control access to application data \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:18.051426+00:00
---

# Secure and control access to application data  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/querydata/sql-mysql/secure-app-data-parameterized-secure-views-qd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Secure and control access to application data Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Parameterized secure views provide data security and row access control to applications. They filter query results based on the application user's identity.

This tutorial describes how to set up parameterized secure views in Cloud SQL, configure database roles and privileges to restrict access to base tables, and verify data security. The examples provided in this document are for demonstration purposes only.

## What are parameterized secure views?

As a general best practice, your application should run using a service account with the minimal required access to your database. For example, if your application shouldn't write to your database, it should use a role with read-only access. You should configure these access controls at the database level.

When your application needs more granular security than standard database-level access permits, you can use parameterized secure views to make sure that users view only their authorized data. Parameterized secure views provide dynamic data security and row access control suitable for multi-tenant SaaS applications without requiring separate database roles for each application end user.

Using parameterized secure views provides three main benefits:

  * Dynamic data security and row access control: Filters queries using end-user identifiers so users access only their authorized data regardless of query phrasing.
  * Easier role management: Uses a single shared database role for all application users instead of managing separate database roles for each individual.



## Objectives

  * Create parameterized secure views with named view parameters.
  * Create the database role that is used by the application to connect to the database and access parameterized secure views.
  * Grant the new role permissions to the parameterized secure views and revoke access to the base tables.
  * Connect using the new role and verify that the restricted tables can't be accessed. 
  * Run queries on the parameterized view using the `mysql.execute_parameterized_query` stored procedure or using the QueryData API. 



## Costs

In this document, you use the following billable components of Google Cloud:

  * [ Cloud SQL for MySQL](https://cloud.google.com/sql/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

New Google Cloud users might be eligible for a [free trial](https://cloud.google.com/free).

To avoid continued billing, delete the resources you created when you finish the tasks in this document. For more information, see Clean up.

## Before you begin

Before you create parameterized secure views, complete the following prerequisites.

### Enable billing and required APIs

  1. In the Google Cloud console, select a project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Make sure that billing is enabled for your Google Cloud project.](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project)

  3. Enable the Cloud APIs necessary to create and connect to Cloud SQL.

     1. [Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin.googleapis.com,dataplex.googleapis.com)

     2. In the **Confirm project** step, click **Next** to confirm the name of the project you are going to make changes to.

     3. In the **Enable APIs** step, click **Enable** to enable the following:

        * Cloud SQL for MySQL API
        * Knowledge Catalog API



### Create and connect to a database

  1. [Create an instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance#create-instance).
  2. [Connect to your instance and create a database](https://docs.cloud.google.com/sql/docs/mysql/create-manage-databases).



## Prepare your environment

To prepare for running queries on a parameterized secure view, set up the database, database roles, and the application schema.

### Enable the database flag

  * Make sure that your Cloud SQL for MySQL instance is running Cloud SQL for MySQL 8.0.43 or later. If your Cloud SQL for MySQL 8.0 instance is running an earlier minor version, then you can perform a minor version upgrade.
  * Enable the `cloudsql_parameterized_secure_view` database flag for your instance. This flag change doesn't require a database restart. For more information, see [Configure an instance's database flags](https://docs.cloud.google.com/sql/docs/mysql/flags).



### Set up the database and roles

  1. In the Google Cloud console, go to the Cloud SQL page.

[Go to Cloud SQL](https://console.cloud.google.com/sql)

  2. Select an instance from the list.

  3. In the navigation menu, click **Cloud SQL Studio**.

  4. Sign in to **Studio** using administrative user account.

  5. Click **Authenticate**. The Explorer pane displays a list of the objects in your database.

  6. Click **New SQL editor tab** or **New tab** to open a new tab.

  7. Create a database named `store_db` for the application data and views:
         
         CREATE DATABASE IF NOT EXISTS store_db;
         USE store_db;
         

  8. Create a new database role for running queries against parameterized views. The application uses this role to connect to the database and run queries with access restricted strictly to authorized views:
         
         CREATE ROLE 'psv_user';
         




### Create the table and insert data

  1. In the Google Cloud console, go to the Cloud SQL page.

[Go to Cloud SQL](https://console.cloud.google.com/sql)

  2. Select a Cloud SQL for MySQL instance from the list.

  3. In the navigation menu, click **Cloud SQL Studio**.

  4. Sign in to **Studio** using database authentication.

  5. Click **New tab** to open a new SQL editor tab.

  6. Create the tables and insert data:
         
         CREATE TABLE store_db.checked_items (
         bag_id INT,
         timestamp TIMESTAMP,
         loc_code CHAR(3),
         scan_type CHAR(1),
         location TEXT,
         customer_id INT
         );
         
         INSERT INTO store_db.checked_items (bag_id, timestamp, loc_code, scan_type, location, customer_id) VALUES
         (101, '2023-10-26 10:00:00', 'ABC', 'I', 'Warehouse A', 123),
         (102, '2023-10-26 10:15:30', 'DEF', 'O', 'Loading Dock B', 456),
         (103, '2023-10-26 10:30:45', 'GHI', 'I', 'Conveyor Belt 1', 789),
         (104, '2023-10-26 11:00:00', 'JKL', 'O', 'Shipping Area C', 101),
         (105, '2023-10-26 11:45:15', 'MNO', 'I', 'Sorting Station D', 202),
         (106, '2023-10-26 12:00:00', 'PQR', 'O', 'Truck Bay E', 303);
         




## Create parameterized secure views and set up access privileges

To create parameterized secure views, follow these steps:

  1. In the Google Cloud console, go to the Cloud SQL page.

[Go to Cloud SQL](https://console.cloud.google.com/sql)

  2. Select an instance from the list.

  3. In the navigation menu, click **Cloud SQL Studio**. 

  4. Sign in to **Studio** and connect to the `database` as the `store_db` user account you used in the previous section. 

  5. Click **Authenticate**. The Explorer pane displays a list of the objects in your database. 

  6. Click **New SQL editor tab** or **New tab** to open a new tab.

  7. To provide limited access to the view, create a parameterized view:
         
         CREATE VIEW store_db.secure_checked_items AS
         SELECT bag_id, timestamp, location
         FROM store_db.checked_items t
         WHERE customer_id = @app_end_userid;
         

**Note:** Make sure that you use unique parameter names, such as `@app_end_userid`, when creating parameterized secure views.
  8. Grant SELECT access on the parameterized view to the `psv_user` role:
         
         GRANT SELECT ON store_db.secure_checked_items TO 'psv_user';
         

  9. Grant execution permission on the built-in system stored procedure used to execute parameterized queries safely:
         
         GRANT EXECUTE ON PROCEDURE mysql.execute_parameterized_query TO 'psv_user';
         

  10. Optional. Explicitly revoke any direct privileges on the base table from `psv_user` to ensure users cannot bypass the secure view:
         
         REVOKE ALL PRIVILEGES ON store_db.checked_items FROM 'psv_user';
         

**Note:** If a `Error 1147: There is no such grant defined for user` occurs, you can safely ignore it. This error appears if you try to revoke a privilege that was never granted. A new role has no privileges by default. Only run this command if you are modifying an existing role that already had access to the base table.
  11. Grant the `psv_user` role to the IAM-authenticated database user or application login account:
         
         GRANT 'psv_user' TO 'IAM_USER_EMAIL'@'%';
         
         SET DEFAULT ROLE 'psv_user' TO 'IAM_USER_EMAIL'@'%';
         

Replace `IAM_USER_EMAIL` with your IAM user email address or application login account.




## Verify data security

To verify that you can query the parameterized secure views, follow these steps:

  1. Sign in to **Cloud SQL Studio** using the restricted IAM email address or application login.

  2. Click **New tab** to open a new SQL editor tab.

  3. Query the base table and verify that access is denied.
         
         SELECT * FROM store_db.checked_items;
         

The database returns the `ERROR 1142 (42000): SELECT command denied to user 'IAM_USER_EMAIL'@'%' for table 'checked_items'` error.

  4. Query the parameterized secure view using the built-in `mysql.execute_parameterized_query` stored procedure.
         
         CALL mysql.execute_parameterized_query(
           'SELECT * FROM store_db.secure_checked_items',
           'app_end_userid=303'
         );
         

  5. Query the parameterized secure views using SQL syntax and the `QueryData` request with PSV parameters.
         
         curl -X POST \
            "https://geminidataanalytics.googleapis.com/v1beta/projects/PROJECT_ID/locations/REGION:queryData" \
            -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            -H "Content-Type: application/json; charset=utf-8" \
            -d '{
              "prompt": "Show me the checked items.",
              "context": {
                "datasource_references": {
                  "cloud_sql_reference": {
                    "database_reference": {
                      "engine": "MYSQL",
                      "project_id": "PROJECT_ID",
                      "region": "REGION",
                      "instance_id": "INSTANCE_ID",
                      "database_id": "DATABASE_ID"
                    }
                  }
                },
                "parameterized_secure_view_parameters": {
                  "parameters": {
                    "key": "app_end_userid"
                    "app_end_userid": "303"
                  }
                }
              },
              "generation_options": {
                "generate_query_result": true,
                "generate_natural_language_answer": true,
                "generate_explanation": true
              }
            }'

Replace the following values:

     * `PROJECT_ID`: Your Google Cloud project ID.
     * `REGION`: The region where your Cloud SQL for MySQL instance is located.
     * `INSTANCE_ID`: The ID of your Cloud SQL for MySQL instance.
     * `DATABASE_ID`: The ID of your Cloud SQL for MySQL database.



## Clean up

### Delete the cluster

When you delete the cluster that you created in the before you begin section, you also delete all of the objects you created.

  1. In the Google Cloud console, go to the Cloud SQL page.

[Go to Cloud SQL](https://console.cloud.google.com/sql)

  2. Select an instance from the list.

  3. Click **Delete**.

  4. Confirm that you want to delete the instance by entering the instance name and clicking **Delete**.




## What's next

* Learn about [parameterized secure views](https://docs.cloud.google.com/sql/docs/mysql/parameterized-secure-views).

* Learn how to [use parameterized secure views](https://docs.cloud.google.com/sql/docs/mysql/use-parameterized-secure-views). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
