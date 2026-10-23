---
url: https://docs.cloud.google.com/bigtable/docs/create-manage-saved-queries/
title: Create and manage saved queries \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:38.463059+00:00
---

# Create and manage saved queries  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/create-manage-saved-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and manage saved queries

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To reuse and share common database operations across sessions, you can create, organize, and manage saved SQL scripts in Bigtable Studio. For more information, see [Saved queries overview](https://docs.cloud.google.com/bigtable/docs/saved-queries).

The saved queries capability is available only in the console, and not using APIs.

## Required roles

To get the permissions that you need to use saved queries, ask your administrator to grant you the following Identity and Access Management (IAM) roles on the project:

  * To view saved queries: [Bigtable Reader](https://docs.cloud.google.com/bigtable/docs/access-control#bigtable.reader) (`roles/bigtable.reader`)
  * To view, create, modify, and delete saved queries: [Bigtable User](https://docs.cloud.google.com/bigtable/docs/access-control#bigtable.user) (`roles/bigtable.user`)
  * To administer, view, create, modify, and delete saved queries: [Bigtable Admin](https://docs.cloud.google.com/bigtable/docs/access-control#bigtable.admin) (`roles/bigtable.admin`). This role has broad permissions and provides full access to Bigtable, only for use by administrators.



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

**Note:** Having access to saved queries doesn't automatically mean that you have permissions to run the query.You can also get these permissions using [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). The [Studio Query User](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole) (`roles/databasesconsole.studioQueryUser`) role provides create, view, and write saved queries access. This role meets the needs of most users. Grant the [Studio Query Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/databasesconsole) (`roles/databasesconsole.studioQueryAdmin`) role only to administrators. For more information about Bigtable IAM, see [Bigtable access control with IAM](https://docs.cloud.google.com/bigtable/docs/access-control).

## Create a saved query

To create a saved query, follow these steps:

  1. In the Google Cloud console, go to the Bigtable **Instances** page.  
[Instances](https://console.cloud.google.com/bigtable/instances)
  2. Select the instance in which you want to create a saved query.
  3. In the navigation menu, click **Bigtable Studio**. The **Explorer** pane displays a list of tables, views, and queries in the instance.
  4. From the **Editor** tab, run your query. The results appear in the **Results** table.
  5. If you aren't satisfied with the results, then modify the query and run it again. When you're satisfied with the query, click **Save**.
  6. In the **Save query** dialog, enter a name for the saved query.
  7. Click **Save**.

Optional:

  * To save the query with a different name, click the **Save as** expander arrow, choose **Save as query** , and then enter a new name in the dialog.
  * To change the region used by this saved query, select **Show advanced options**. Then, from the **Region** list, select a region.

You can also save the query as a [logical](https://docs.cloud.google.com/bigtable/docs/create-manage-logical-views) or a [continuous materialized](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views) view.

## Open and run a saved query

To open a saved query as a new query, follow these steps:

  1. In the **Explorer** pane on the **Bigtable Studio** page, navigate to the **Queries** section.
  2. Click a saved query to open it in a new editor tab. Optionally, you can click more_vert **View actions** next to a saved query. Then, click **Open query** to open it in a new editor tab.
  3. Click **Run**.



## Update a saved query

To update an existing saved query, follow these steps:

  1. In the **Explorer** pane on the **Bigtable Studio** page, navigate to the **Queries** section.
  2. Click a saved query to open it in a new editor tab. Optionally, you can click more_vert **View actions** next to a saved query. Then, click **Open query** to open it in a new editor tab.
  3. Modify the query.
  4. To save the modified query, click **Save**.



## View and manage a list of all saved queries

To view a list of all saved queries in your project, follow these steps:

  1. In the Google Cloud console, go to the Bigtable **Instances** page.  
[Instances](https://console.cloud.google.com/bigtable/instances)
  2. Select an instance. Because a saved query is a child of a project, as long as you have the required role, you can view all saved queries in the project from any instance or database.


  3. In the **Explorer** pane on the **Bigtable Studio** page, navigate to the **Queries** section.
  4. Click more_vert **View actions** next to a saved query. Then, click **Manage queries**. The **Saved queries** page opens. This page lists all the saved queries in this project, including saved queries for other Google Cloud products.

You can search, filter, view, and delete queries on the **Saved queries** page. You can't edit an existing query on the **Saved queries** page.

## Delete a saved query

You can delete a saved query from the **Bigtable Studio** page or on the **Saved queries** page in the Google Cloud console.

  1. In the **Explorer** pane on the **Bigtable Studio** page, navigate to the **Queries** section.
  2. Click more_vert **View actions** next to the saved query that you want to delete. Then, to delete the saved query, click **Delete query**.
  3. In the **Delete query** dialog, click **Delete**.

You can also delete a saved query on the **Saved queries** page. To delete a saved query on the **Saved queries** page, follow these steps:

  1. Navigate to the **Saved queries** page.
  2. Click more_vert **View actions** next to the saved query that you want to delete.
  3. Click **Delete query** to delete the saved query.
  4. In the **Delete query** dialog, click **Delete**.



## What's next

  * Learn about [saved queries](https://docs.cloud.google.com/bigtable/docs/saved-queries).

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-10-23 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
