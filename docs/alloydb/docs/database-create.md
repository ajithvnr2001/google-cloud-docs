---
url: https://docs.cloud.google.com/alloydb/docs/database-create/
title: Create and manage a database \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:41:57.787418+00:00
---

# Create and manage a database  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/database-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Create and manage a database Stay organized with collections  Save and categorize content based on your preferences. 

To organize your schemas and isolate application data within an AlloyDB for PostgreSQL cluster, you can create additional PostgreSQL databases alongside the default `postgres` database, list existing databases on your cluster, and delete databases that you no longer need.

## Before you begin

The Google Cloud project you use must be [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect).

You must have one of the following Identity and Access Management roles in the Google Cloud project that you're using:

  * `roles/alloydb.admin`: the AlloyDB Admin predefined IAM role
  * `roles/owner`: the Owner basic IAM role
  * `roles/editor`: the Editor basic IAM role



If you don't have any of these roles, contact your Organization Administrator to request access.

## Create a database

Before you can create a database, you must [create a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create).

To create a database, complete the following steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. In the **Resource name** column, click the name of your cluster.

  3. In the navigation pane, click **Databases**.

  4. Click **Create a database**. A dialog window opens that suggests a query to use in AlloyDB Studio.

  5. Copy the query and click **Open in Studio**. The AlloyDB Studio page opens with an additional **Log in to your database** dialog window.

  6. In the **Log in to your database** window, make the following selections:

     * Select the `postgres` database.
     * Select a [database authentication method](https://docs.cloud.google.com/alloydb/docs/manage-data-using-studio#authentication) and enter a username and password.
  7. Click **Authenticate**. The **Explorer** pane displays a list of the objects in the `postgres` database.

  8. Select the **Untitled Query** tab and paste the following query that you copied:
         
         CREATE DATABASE DATABASE_NAME;
         

Replace DATABASE_NAME with the name of the database.

  9. Click **Run**.

If the **Statement executed successfully** message displays in the **Results** pane, then you know that you created your database.




## List a database

To list all databases on a cluster, complete the following steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. To open the **Overview** page of a cluster, click the cluster name in the **Resource name** column.

  3. In the navigation pane, click **Databases**. The **Databases** page lists the database names along with their collation type and character set.




## Delete a database

To delete a database in a cluster, complete the following steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. To open the **Overview** page of a cluster, click the cluster name in the **Resource name** column.

  3. In the navigation pane, click **Databases**. The **Databases** page lists the database names along with their collation type and character set.

  4. Choose a database to delete, click the three-dot menu more_vert in that row, and select **Drop**. A **Drop a database** dialog window opens.

**Note:** If there's only one database in the list, you don't have the option to drop the database.
  5. Click **Open in Studio**.

  6. In the open **Untitled Query** tab, click **Run**.

If the **Statement executed successfully** message displays in the **Results** pane, then you know that you deleted the database.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
