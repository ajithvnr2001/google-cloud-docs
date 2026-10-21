---
url: https://docs.cloud.google.com/sql/docs/mysql/monitor-active-queries/
title: Monitor active queries \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:50:12.646996+00:00
---

# Monitor active queries  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/monitor-active-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Monitor active queries Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/monitor-active-queries "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-active-queries "View this page for the SQL Server database engine")

This page describes how to monitor and troubleshoot the queries that are active in your database. Monitoring these queries can help identify causes of system latency and high CPU usage.

On the **Query insights dashboard** , you can view a summary of active transactions and a list of transactions with associated query and statistics. The transactions are displayed by the transaction start time. If there is a large number of queries running, then the results might be limited to a subset of total queries.

## Before you begin

To monitor active queries, you can use either Cloud SQL Enterprise edition or Cloud SQL Enterprise Plus edition.

To terminate a session or a long-running transaction in active queries, you must use Cloud SQL Enterprise Plus edition for your Cloud SQL instance.

For more information about Cloud SQL editions, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/mysql/editions-intro).

### Required roles and permissions

To get the permissions that you need to view active queries, ask your administrator to grant you the following IAM roles on the project that hosts the Cloud SQL instance: 

  * View instance activity summary: [Cloud SQL Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.viewer) (`roles/cloudsql.viewer`) 
  * View database activity summary and long-running transactions: [Database Insights Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`) 
  * Terminate a session or long running transaction: 
    * [Cloud SQL Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.editor) (`roles/cloudsql.editor`)
    * [Database Insights Operations Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.operationsAdmin) (`roles/databaseinsights.operationsAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view active queries. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view active queries:

  * View database activity summary and long-running transactions: 
    * `databaseinsights.activeQueries.fetch`
    * `databaseinsights.activitySummary.fetch`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable active queries

When you [enable query insights](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights#enable-insights), you enable active queries automatically. To be able to terminate a session or long-running transaction in active queries, you must use [query insights for Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights#query-insights-for-enterprise-plus).

## Disable active queries

You can't disable active queries without disabling query insights. To disable active queries and query insights, see [Disable query insights](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights#disable-insights).

## View active queries

To view your active queries, complete the following steps:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

  2. To open the **Overview** page of an instance, click the instance name.

  3. Do one of the following to display the **Query insights** dashboard:

     * Select the **Query insights** tab.
     * Click **Go to Query insights for more in-depth info on queries and performance**. The **Query insights** dashboard opens. It shows details about the instance at the top.
  4. Click the **Active queries** tab.

From here, you can modify the query information that appears in the **Longest running transactions** table:

     * **Database** : filters query load on a specific database or all databases.
     * **User** : filters query load from a specific user account.
     * **Summary scorecard of all active queries** : provides an overview of all the active queries by displaying the total connections based on the following parameters:

       1. Distribution of active connections categorized by connection state.
       2. Distribution of active transactions based on transaction state.
       3. Distribution of query durations.
     * **Longest running transactions** : provides an overview of the top 50 running queries (in the _active_ state) based on descending execution time. You can filter and sort active queries in the table.



### View normalized active queries

You can view a list of top long-running transactions with normalized active queries on the **Query insights** dashboard. A normalized active query removes sensitive data and returns a digest. The digest is the same for different values used in the following example:

  * _Regular queries_

    * `select * from test_table where id=1;`
    * `select * from test_table_where id=2;`
  * _Digest or normalized query_

    * `select * from test_table where id=?;`



A query that runs in different sessions is displayed as different entries on the dashboard.

### View top longest running transactions

The **Longest running transactions** table on the **Query insights** dashboard contains the following columns:

Column name | Description  
---|---  
Process ID | Unique identifier of the connection.  
Query | SQL query text.   
Transaction state | The current execution state of the transaction. Permitted values include: `RUNNING`, `LOCK WAIT`, `ROLLING BACK`, and `COMMITTING`.  
Thread state | Thread state (or query state) indicates the current state of the active thread.  
Transaction start time | The timestamp when the transaction started its execution.  
Transaction duration | The duration of current active transaction in seconds.  
Transaction wait duration | The duration of wait in seconds on current active transaction.  
Thread state duration | Time elapsed in the query.  
Transaction rows locked | Number of rows locked by the current active transaction.  
Transaction rows modified | Number of rows modified by the current active transaction.  
Database | Database name on which this connection is running.  
User name | Name of the user connected to the database.  
Client address | The IP address of client from where a user connects to the database.  
Action | Contains a link for terminating a transaction.  
  
The display is refreshed every 60 seconds automatically.

You can use the view_week **Content display options...** vertical menu to filter the columns you want to display.

**Note:** Data comes from the `innodb_trx` and `processlist` tables. Because both tables collect data separately, the transaction state and thread state might be captured at different point in time.

## Terminate a connection

To terminate a connection or long-running transaction in active queries, you must use Cloud SQL Enterprise Plus edition and enable [query insights for Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights#enable-insights).

Long running operations can take longer to terminate.

To terminate a query or transaction, complete the following steps:

  1. In the **Longest running transaction** table, select a query. 
  2. In the **Action** column, click **Terminate connection**.
  3. In the **Terminate connection** window, click **Confirm**. 



A database request returns immediately while the termination happens in the background.

The page refreshes after initiating termination. If termination fails, then an error message or notification isn't returned. The query continues showing up in the Active Query list. If termination is successful, then the query no longer displays in the list. If the termination requires a rollback, then the **Txn state** column shows the _ROLLING BACK_ state, which means that termination is still in progress.

**Note:** If **Terminate** isn't available, then you might have insufficient IAM permissions. For more information, see [Before you begin](https://docs.cloud.google.com/sql/docs/mysql/monitor-active-queries#before_you_begin).

## What's next

  * [Use query insights](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights)
  * [Use system insights](https://docs.cloud.google.com/sql/docs/mysql/use-system-insights)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
