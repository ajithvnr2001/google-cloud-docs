---
url: https://docs.cloud.google.com/sql/docs/postgres/monitor-active-queries/
title: Monitor active queries \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:39.051185+00:00
---

# Monitor active queries  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/monitor-active-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Monitor active queries Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/monitor-active-queries "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-active-queries "View this page for the SQL Server database engine")

This page describes how to monitor and troubleshoot the queries that are active in your database. Monitoring these queries can help identify causes of system latency and high CPU usage.

On the **Query insights dashboard** , you can view a summary of active transactions and a list of transactions with associated query and statistics. The transactions are displayed by the transaction start time. If there is a large number of queries running, then the results might be limited to a subset of total queries.

## Before you begin

To monitor active queries, you can use either Cloud SQL Enterprise edition or Cloud SQL Enterprise Plus edition.

To terminate a session or a long-running transaction in active queries, you must use Cloud SQL Enterprise Plus edition for your Cloud SQL instance.

For more information about Cloud SQL editions, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/postgres/editions-intro).

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

**Note:** Enabling active queries is only supported through the Google Cloud console.

To enable active queries for a Cloud SQL Enterprise edition instance, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. On the **Configuration** tile, click **Edit configuration**.
  4. In the **Customize your instance** section, expand **Query insights**.
  5. Make sure **Enable Query insights** is enabled.
  6. Select **Active query analysis**.
  7. Click **Save**.



To enable active queries for a Cloud SQL Enterprise Plus edition instance, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. On the **Configuration** tile, click **Edit configuration**.
  4. In the **Customize your instance** section, expand **Query insights**.
  5. Make sure **Enable Query insights** is enabled.
  6. Select **Enable Enterprise Plus features**.
  7. Select **Active query analysis**.
  8. Click **Save**.



To be able to terminate a session or long-running transaction in active queries, you must use query insights for Cloud SQL Enterprise Plus edition.

## Disable active queries

To disable active queries on a Cloud SQL Enterprise edition or Cloud SQL Enterprise Plus edition instance, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. On the **Configuration** tile, click **Edit configuration**.
  4. In the **Customize your instance** section, expand **Query insights**.
  5. Clear the **Active query analysis** checkbox.
  6. Click **Save**.



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
     * **Longest running transactions** : provides an overview of the top 50 running queries (in the _active_ and _idle in transaction_ state) based on descending execution time. You can filter and sort active queries in the table.



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
Process ID | Unique identifier of the connection or thread ID.  
Query | SQL query text.  
Status | Status of the connection.  
Session duration | Duration of the last session running.  
Transaction duration | Duration of the active transaction running.  
Query duration | Duration of the last query running in that transaction.  
Wait event type | Wait event type of the occurring wait event.  
Wait event | Occurring wait event.  
Database | Database name on which this connection is running.  
Application name | Application name on which this connection is running.  
User name | Name of the user connected to the database.  
Client address | Specific IP address of the client that sent a query.  
Action | Contains a link for terminating a transaction.  
  
The display is refreshed every 60 seconds automatically.

You can use the view_week **Content display options...** vertical menu to filter the columns you want to display.

## Terminate a process

To terminate a process or long-running transaction in active queries, you must use Cloud SQL Enterprise Plus edition and enable both **Active query analysis** and [query insights for Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights#enable-insights).

Long running operations can take longer to terminate.

To terminate a query or transaction, complete the following steps:

  1. In the **Longest running transaction** table, select a query. 
  2. In the **Action** column, click **Terminate connection**.
  3. In the **Terminate connection** window, click **Confirm**. 



If the system successfully terminates the query or transaction, then a success message appears. The system also performs a rollback if needed.

**Note:** If **Terminate** isn't available, then you might have insufficient IAM permissions. For more information, see [Before you begin](https://docs.cloud.google.com/sql/docs/postgres/monitor-active-queries#before_you_begin).

## Blocked active queries

**Preview —[Blocked active queries](https://docs.cloud.google.com/sql/docs/postgres/monitor-active-queries#blocked-active-queries) **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If a specific active query is blocked or running much longer than expected, then that active query can block other dependent queries.

Cloud SQL gives you the option to terminate specific long-running or blocked active queries.

### Enable the analysis of blocked active queries

By default, Google Cloud console doesn't display which active queries are blocked.

In order to analyze blocked active queries, the following requirements apply:

  * You must use an Cloud SQL Enterprise Plus edition instance.
  * You must enable active queries on the instance.



To enable blocked active query analysis, do the following:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. Expand **Query insights** section.
  5. Select both **Enable Enterprise Plus features** and **Active query analysis**. Both settings are required.
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

If you don't already have active queries running, navigate to [Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/postgres/manage-data-using-studio) and run the queries you want to investigate.

  5. Navigate to the **Longest running transactions** section. You can see up to 50 of the longest running active queries under each category. 

Each entry displayed includes the following information:

     * **Process ID** : The process ID of the query. Click arrow_right **expand** to view the entry. You can see one of two icons: 
       * hourglass_bottom **Hourglass icon** : This icon indicates that the process is waiting for another query to finish. If a number is included beside the icon, then the number indicates how many dependent queries are waiting for this process to finish.
       * block **Block symbol icon** : This icon indicates that the process is unable to finish and might be blocking other queries.
     * **Query type** : The type of query running, such as `SELECT` or `UPDATE`.
     * **Status** : The status of the active query, such as `ACTIVE`.
     * **Session duration (seconds)** : The duration of current session (in seconds).
     * **Transaction duration (seconds)** : The duration of current active transaction (in seconds).
     * **Query duration (seconds)** : The duration of current active query (in seconds).
     * **Wait event type** : The currently occurring wait event type during query execution, such as **Timeout** or **Lock**.
     * **Wait event** : The currently occurring wait event during query execution.
     * **Action** : Possible actions to take, such as **Terminate connection**.

Click to expand the process ID you want to investigate. You can expand underlying processes up to three levels deep in the investigation tree.

  6. Identify the specific query that's blocked, then click **Terminate connection**. After you terminate the connection, you can navigate to [Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/postgres/manage-data-using-studio) to run your active queries again.



## What's next

  * [Use query insights](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights)
  * [Use system insights](https://docs.cloud.google.com/sql/docs/postgres/use-system-insights)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
