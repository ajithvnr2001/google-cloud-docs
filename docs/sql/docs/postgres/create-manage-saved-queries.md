---
url: https://docs.cloud.google.com/sql/docs/postgres/create-manage-saved-queries/
title: Create and manage saved queries \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:34.458086+00:00
---

# Create and manage saved queries  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/create-manage-saved-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Create and manage saved queries Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/create-manage-saved-queries "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-saved-queries "View this page for the SQL Server database engine")

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To reuse and share common database operations across sessions, you can create, organize, and manage saved SQL scripts in Cloud SQL Studio . For more information, see [Saved queries overview](https://docs.cloud.google.com/sql/docs/postgres/saved-queries) .

The saved queries capability is available only in the console, and not using APIs.

## Required roles

To get the permissions that you need to use saved queries, ask your administrator to grant you the following Identity and Access Management (IAM) roles on the project:

  * To view saved queries: Cloud SQL Studio User (`roles/cloudsql.studiouser`)
  * To create, edit, view, and delete saved queries in a project, including access to the **Saved queries** page: Cloud SQL Admin (`roles/cloudsql.admin`) or [Studio Query User](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole) (`roles/databasesconsole.studioQueryUser`)
  * To manage all saved queries in a project, including access to the **Saved queries** page: [Studio Query Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole) (`roles/databasesconsole.studioQueryAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

These predefined roles contain the permissions required to use saved queries. To learn more about required permissions, see Required permissions.

### Required permissions

To create, view, modify, and delete saved queries, you need the following IAM permissions at the project level:

**Action** | **Required IAM permissions**  
---|---  
Create saved queries | 

  * `databasesconsole.studioQueries.create`

  
View saved queries | 

  * `databasesconsole.studioQueries.search`
  * `databasesconsole.locations.get`
  * `databasesconsole.locations.list`

  
Modify saved queries | 

  * `databasesconsole.studioQueries.update`

  
Delete saved queries | 

  * `databasesconsole.studioQueries.delete`

  
Administer saved queries  
(Only for use by administrators) | 

  * `databasesConsole.studioQueries.list`


  * `databasesconsole.locations.list`

**Note:** Having access to saved queries doesn't automatically mean that you have permissions to run the query.You can also get these permissions using [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). The [Studio Query User](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole) (`roles/databasesconsole.studioQueryUser`) role provides create, view, and write saved queries access. This role meets the needs of most users. Grant the [Studio Query Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole) (`roles/databasesconsole.studioQueryAdmin`) role only to administrators. For more information about Cloud SQL for PostgreSQL IAM, see [Roles and permissions](https://docs.cloud.google.com/sql/docs/postgres/roles-and-permissions) .

## Create a saved query

To create a saved query, follow these steps:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page. [Go to Cloud SQL Instances](https://console.cloud.google.com/sql)
  2. Select the instance in which you want to create a saved query.
  3. In the navigation menu, click **Cloud SQL Studio**.
  4. On the **Cloud SQL Studio** page, click add **New tab** or use the empty editor tab.
  5. In the query editor, enter a SQL query.
  6. Click **Save**.
  7. In the **Save query** dialog, enter a name for the saved query.
  8. Click **Save**.



## Open and run a saved query

To open a saved query as a new query, follow these steps:

  1. In the **Explorer** pane on the **Cloud SQL Studio** page, navigate to the **Queries** section.
  2. Click a saved query to open it in a new editor tab. Optionally, you can click more_vert **View actions** next to a saved query. Then, click **Open query** to open it in a new editor tab.
  3. Click **Run**.



## Update a saved query

To update an existing saved query, follow these steps:

  1. In the **Explorer** pane on the **Cloud SQL Studio** page, navigate to the **Queries** section.
  2. Click a saved query to open it in a new editor tab. Optionally, you can click more_vert **View actions** next to a saved query. Then, click **Open query** to open it in a new editor tab.
  3. Modify the query.
  4. To save the modified query, click **Save**.



## View and manage a list of all saved queries

To view a list of all saved queries in your project, follow these steps:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page. [Go to Cloud SQL Instances](https://console.cloud.google.com/sql)
  2. Select any instance. Because a saved query is a child of a project, as long as you have the required role, you can view all saved queries in the project from any instance or database.
  3. In the navigation menu, click **Cloud SQL Studio** and [authenticate](https://docs.cloud.google.com/sql/docs/postgres/manage-data-using-studio#authentication).


  3. Select any database.
  4. In the **Explorer** pane on the **Cloud SQL Studio** page, navigate to the **Queries** section.
  5. Click more_vert **View actions** next to a saved query. Then, click **Manage queries**. The **Saved queries** page opens. This page lists all the saved queries in this project, including saved queries for other Google Cloud products.

You can search, filter, view, and delete queries on the **Saved queries** page. You can't edit an existing query on the **Saved queries** page.

## Delete a saved query

You can delete a saved query from the **Cloud SQL Studio** page or on the **Saved queries** page in the Google Cloud console.

  1. In the **Explorer** pane on the **Cloud SQL Studio** page, navigate to the **Queries** section.
  2. Click more_vert **View actions** next to the saved query that you want to delete. Then, to delete the saved query, click **Delete query**.
  3. In the **Delete query** dialog, click **Delete**.

You can also delete a saved query on the **Saved queries** page. To delete a saved query on the **Saved queries** page, follow these steps:

  1. Navigate to the **Saved queries** page.
  2. Click more_vert **View actions** next to the saved query that you want to delete.
  3. Click **Delete query** to delete the saved query.
  4. In the **Delete query** dialog, click **Delete**.



## What's next

  * Learn about [saved queries](https://docs.cloud.google.com/sql/docs/postgres/saved-queries).

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-10-23 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
