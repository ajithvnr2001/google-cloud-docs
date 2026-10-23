---
url: https://docs.cloud.google.com/sql/docs/sqlserver/monitor-active-queries/
title: Monitor active queries \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:31.025016+00:00
---

# Monitor active queries  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/monitor-active-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Monitor active queries Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/monitor-active-queries "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/monitor-active-queries "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to monitor and troubleshoot the queries that are active in your database. Monitoring these queries can help identify causes of system latency and high CPU usage.

On the **Query insights dashboard** , you can view a summary of active transactions and a list of transactions with associated query and statistics. The transactions are displayed by the transaction start time. If there is a large number of queries running, then the results might be limited to a subset of total queries.

## Before you begin

To monitor active queries, you can use either Cloud SQL Enterprise edition or Cloud SQL Enterprise Plus edition.

To terminate a session or a long-running transaction in active queries, you must use Cloud SQL Enterprise Plus edition for your Cloud SQL instance.

For more information about Cloud SQL editions, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/sqlserver/editions-intro).

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

When you [enable query insights](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights#enable-insights), you enable active queries automatically. To be able to terminate a session or long-running transaction in active queries, you must use [query insights for Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights#query-insights-for-enterprise-plus).

## Disable active queries

You can't disable active queries without disabling query insights. To disable active queries and query insights, see [Disable query insights](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights#disable-insights).

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
Session ID | Unique identifier of the session.  
Query | SQL query text.   
State of session | The state of the session.  
Query duration | How long the query has been running.  
Blocking session ID | The id of the session that is blocking the session.  
Wait event type | The type of wait event, if the request is blocked for query execution.  
Wait resource | The resource for which the request is currently waiting, if the request is blocked for query execution.  
Transaction wait duration | The duration of the current wait, if the session is blocked.  
Logical reads | The number of logical reads that have been performed by the request.  
Reads | The number of reads that have been performed by the request.  
Writes | The number of writes that have been performed by the request.  
Database | Database where the session is running.  
User | Name of the user connected to the database.  
Client address | The specific IP address of the client that sent a query.  
CPU time (ms) | The CPU time in milliseconds that is used by the request.  
Application name | Name of application that initiated the session.  
Transaction rows modified | Number of rows returned to client by this query.  
% complete | Percent of work completed, if the query reports progress.  
Granted query memory | The number of pages allocated to the execution of the request.  
Action | Contains a link for terminating a session.  
  
The display is refreshed every 60 seconds automatically.

You can use the view_week **Content display options...** vertical menu to filter the columns you want to display.

## Terminate a session

To terminate a session or long-running transaction, you must use Cloud SQL Enterprise Plus edition and enable [query insights for Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights#enable-insights).

Long running operations can take longer to terminate.

To terminate a query or transaction, complete the following steps:

  1. In the **Longest running transaction** table, select a query. 
  2. In the **Action** column, click **Terminate session**.
  3. In the **Terminate session** window, click **Confirm**. 

**Note:** If **Terminate** isn't available, then you might have insufficient IAM permissions. For more information, see [Before you begin](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-active-queries#before_you_begin).

## Blocked active queries

**Preview —[Blocked active queries](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-active-queries#blocked-active-queries) **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If a specific active query is blocked or running much longer than expected, then that active query can block other dependent queries.

Cloud SQL gives you the option to terminate specific long-running or blocked active queries.

### Enable the analysis of blocked active queries

By default, Google Cloud console doesn't display which active queries are blocked.

In order to analyze blocked active queries, the following requirements apply:

  * You must use an Cloud SQL Enterprise Plus edition instance.
  * You must [enable Enterprise Plus features](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights#enable-qi-for-ep).



To enable blocked active query analysis, do the following:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. Expand **Query insights** section.
  5. Select both **Enable Query insights** and **Enable Enterprise Plus features**. Both settings are required.
  6. Select **Blocked query analysis**.
  7. Click **Save**.



### Identify and terminate a blocked active query

The following steps show you how to identify and terminate a specific active query that might be blocking other queries.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. In the SQL navigation menu, click **Query insights**.
  4. Click the **Active queries** tab. 

If you don't already have active queries running, navigate to [Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/sqlserver/manage-data-using-studio) and run the queries you want to investigate.

  5. Navigate to the **Longest running transactions** section. You can see up to 50 of the longest running active queries under each category. 

Each entry displayed has [active query details](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-active-queries#view-top-longest-running-transactions) displayed, including the following:

     * **Session ID** : The session ID of the query. Click arrow_right **expand** to view the entry. You can see one of two icons: 
       * hourglass_bottom **Hourglass icon** : This icon indicates that the query is waiting for another query to finish. If a number is included beside the icon, then the number indicates how many dependent queries are waiting for this query to finish.
       * block **Block symbol icon** : This icon indicates that the query is unable to finish and might be blocking other queries.
     * **Query** : SQL query text.
     * **State of session** : The state of the session.
     * **Query duration (seconds)** : How long the query has been running.
     * **CPU time(ms)** : The CPU time in milliseconds that is used by the request.
     * **Wait event type** : The type of wait event, if the request is blocked for query execution.
     * **Wait resource** : The resource for which the request is currently waiting, if the request is blocked for query execution.
     * **Transaction wait duration (seconds)** : The duration of the current wait, if the session is blocked.
     * **Action** : Possible actions to take, such as **Terminate session**.

Click to expand the session ID you want to investigate. You can expand underlying sessions up to three levels deep in the investigation tree.

  6. Identify the specific query that's blocked, then click **Terminate session**. After you terminate the session, you can navigate to [Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/sqlserver/manage-data-using-studio) to run your active queries again.



### View details of blocking sleeping sessions

The **Active queries** tab displays sessions that are currently processing a request. Sessions in the `SLEEPING` state are excluded from this view.

To view the last command executed for a sleeping session, use the following script:
    
    
    SELECT c.session_id, st.text,s.login_name, s.open_transaction_count, s.host_name, s.program_name
    FROM sys.dm_exec_connections AS c JOIN sys.dm_exec_sessions AS S ON c.session_id=s.session_id
    CROSS APPLY sys.dm_exec_sql_text(c.most_recent_sql_handle) AS st
    WHERE s.session_id=BLOCKING_SESSION_ID
    

Replace BLOCKING_SESSION_ID with the ID of the session causing the block.

For more information to help troubleshoot and resolve blocking, see the following resources:

  * [Blocking caused by a sleeping SPID that has an uncommitted transaction](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/performance/understand-resolve-blocking#scenario-2-blocking-caused-by-a-sleeping-spid-that-has-an-uncommitted-transaction)
  * [Understand and resolve SQL Server blocking problems](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/performance/understand-resolve-blocking).



## What's next

  * [Use query insights](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights)
  * [Use system insights](https://docs.cloud.google.com/sql/docs/sqlserver/use-system-insights)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
