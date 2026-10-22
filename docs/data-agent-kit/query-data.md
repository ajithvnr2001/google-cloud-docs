---
url: https://docs.cloud.google.com/data-agent-kit/query-data/
title: Query your data \u00a0|\u00a0 Google Cloud Data Agent Kit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:33.879341+00:00
---

# Query your data  |  Google Cloud Data Agent Kit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-agent-kit/query-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Agent Kit ](https://docs.cloud.google.com/data-agent-kit)
  * [ Guides ](https://docs.cloud.google.com/data-agent-kit/overview)



Send feedback 

#  Query your data Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud Data Agent Kit IDE extension's unified SQL editor lets you run SQL queries against your Google Cloud data directly from your IDE.

If you're using the Data Agent Kit plugin with a supported coding agent, you can run SQL queries in the agent or use natural language prompts to generate SQL queries.

## Supported data sources

Data Agent Kit lets you query tables and views in the following Google Cloud data services:

  * BigQuery
  * Bigtable
  * Spanner
  * AlloyDB for PostgreSQL
  * Cloud SQL for MySQL
  * Cloud SQL for PostgreSQL



For Cloud SQL, queries using Identity and Access Management (IAM) database authentication and built-in database authentication (with passwords stored as regional secrets in Secret Manager) are supported. For more information about how Cloud SQL authenticates built-in users with Secret Manager, see Execute SQL statements using the Data API for [Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/executesql-instance#configure-db-user) and [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/executesql-instance#configure-db-user). For AlloyDB, only queries using IAM database authentication are supported.

## Before you begin

Before querying your data, do the following:

  1. [Install the extension](https://docs.cloud.google.com/data-agent-kit/install).
  2. [Configure extension settings](https://docs.cloud.google.com/data-agent-kit/configure).
  3. Review the guidance at [Find and explore data](https://docs.cloud.google.com/data-agent-kit/find-explore-data).



## Create a new SQL file

You can open the SQL editor in multiple ways.

### Create a new SQL file from the File menu

  1. In the VS Code menu bar, click **File** and then **New Text File**. An untitled file appears in the editor.
  2. Save the new file with the `.sql` extension.
  3. Click **Select a Data Source** in the editor tab.
  4. Complete the steps in Configure query settings.



### Create a new query from the Catalog

  1. In the **Google Cloud Data Agent Kit** tab in the activity bar, expand **Catalog** to find the dataset that you want to query.
  2. Right-click or ctrl+click the name of the dataset and then select **Query** to open a new SQL file preconfigured for that dataset.



### Create a new query from the BigQuery section

  1. In the **Google Cloud Data Agent Kit** tab in the activity bar, expand **BigQuery**.
  2. Click **\+ New Query**. An untitled SQL file configured with BigQuery as its data source appears in the editor.



## Configure query settings

The settings required for your SQL query vary by Google Cloud service.

###  AlloyDB 

  1. In the **SQL editor** , click **Open Query Settings**.
  2. Select **Databases**.
  3. Select **AlloyDB**.
  4. Select a cluster.
  5. Select an instance. Your query is routed to this instance.
  6. Select a database.
  7. Click **Save**.



###  BigQuery 

  1. In the **SQL editor** , click **Open Query Settings**.
  2. Select **BigQuery**.
  3. Click **Save**.



###  Bigtable 

  1. In the **SQL editor** , click **Open Query Settings**.
  2. Select **Databases**.
  3. Select **Bigtable**.
  4. Select an instance.
  5. Optional: To use an app profile other than the default app profile, select it.
  6. Compose your query.
  7. Click **Save**.



###  Cloud SQL 

  1. In the **SQL editor** , click **Open Query Settings**.
  2. Select **Databases**.
  3. Select **Cloud SQL**.
  4. Select an instance. Your query is routed to this instance.
  5. Select a database to query.
  6. Under **Authentication method** , select how to authenticate:

     * **IAM database authentication** : Authenticate using your Google Cloud account.
     * **Built-in database authentication** : Authenticate as a built-in database user whose password is stored as a regional secret in Secret Manager.

       1. In the **User** list, select a database user. If the list can't be loaded, enter the username in the **User** field. For Cloud SQL for MySQL, the default `root` user isn't supported.
       2. In the **Password (stored in Secret Manager)** list, select the regional secret that stores the user's password. If you don't have a secret yet, select **Create new secret in region REGION**, enter a **Name** and the **Password** , and then click **Create Secret**. The secret is created in the same region as your instance.
       3. Optional: In the **Secret version** list, select a specific version. By default, **latest** is selected, which always uses the newest version of the secret.

For more information about built-in user and regional secret requirements, see Execute SQL statements using the Data API for [Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/executesql-instance#configure-db-user) and [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/executesql-instance#configure-db-user).

  7. Click **Save**.




###  Spanner 

  1. In the **SQL editor** , click **Open Query Settings**.
  2. Select **Databases**.
  3. Select **Spanner**.
  4. Select an instance. Your query is routed to this instance.
  5. Select a database to query.
  6. Click **Save**.



## Change query settings

Query settings are specific to each SQL file. After you open a SQL file, you can change the settings.

  1. In the editor, click the displayed data source. The Query **Settings** editor appears.
  2. Complete the steps in Configure query settings.



## Run a query

After you have created a query file and composed your query, click **▷ Run Query**.

The **Results** tab of the **Query Results** pane shows the query results.

To run a subset of the SQL statements in the query editor, highlight the subset before clicking **▷ Run Query**.

## SQL editor features

Not all SQL editor features are supported for every data source type. The following table lists the SQL editor features that are supported per data source type during the Preview.

**Feature** | **BigQuery** | **Bigtable** | **Spanner** | **Cloud SQL** | **AlloyDB for PostgreSQL**  
---|---|---|---|---|---  
**Query results** | ✅ | ✅ | ✅ | ✅ | ✅  
**Job information** | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable  
**Execution details** | ✅ | ✅Elapsed time | ❌Not supported | ❌Not supported | ❌Not supported  
**Visualization** | ✅ | ✅ | ✅ | ✅ | ✅  
**Query settings** | ✅ | ✅ | ✅ | ✅ | ✅  
**Multi-statement query support** | ✅ | ✅ | ✅ | ✅ | ✅  
**Catalog: Insert resource name in editor** | ✅ | ✅ | ✅ | ✅ | ✅  
  
## What's next

  * [Transform data](https://docs.cloud.google.com/data-agent-kit/transform-data)
  * [Troubleshoot](https://docs.cloud.google.com/data-agent-kit/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
