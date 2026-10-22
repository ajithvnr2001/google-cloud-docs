---
url: https://docs.cloud.google.com/alloydb/docs/monitor-active-queries/
title: Monitor active queries \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:42.864745+00:00
---

# Monitor active queries  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/monitor-active-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Monitor active queries Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to monitor and troubleshoot the queries that are active in your database. Active queries are long-running queries on your database that can affect performance. Monitoring these queries can help identify causes of system latency and high CPU usage.

You can view active queries on the query insights dashboard. These queries are displayed by the transaction start time. If there is a large number of queries running, the results may be limited to a subset of total queries due to the memory constraints the system enforces on the data collection.

## Before you begin

To start viewing active queries, you must enable [advanced query insights features](https://docs.cloud.google.com/alloydb/docs/advanced-query-insights-overview) and turn on active query analysis for your instance as follows:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. From the list of clusters and instances, click either a [primary](https://docs.cloud.google.com/alloydb/docs/instance-primary-create) or a [read pool](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create) instance.

  3. Click **Query insights**.

  4. Click **Edit Settings**.

  5. In the **Edit query insights settings** window, select **Enable advanced query insights features for AlloyDB** > **Active Query Analysis**.

  6. Click **Save changes**.

  7. In the **Changes require restart** window, click **Confirm and restart**.




You can use Gemini Cloud Assist assistance to help you monitor and troubleshoot your AlloyDB for PostgreSQL resources. For more information, see [Monitor and troubleshoot with Gemini assistance](https://docs.cloud.google.com/alloydb/docs/monitor-troubleshoot-with-gemini).

## View active queries

To view your active queries, do the following:

  1. Create a custom role and add the [`databaseinsights.monitoringViewer`](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.monitoringViewer) Identity and Access Management (IAM) permission.

  2. Add this role for each user that is viewing active queries.

  3. In the Google Cloud console, open the **AlloyDB** page.

[Go to AlloyDB](https://console.cloud.google.com/alloydb)

  4. Click the name of a cluster to open its **Overview** page.

  5. Select the **Query insights** tab. The query insights dashboard shows details about the selected cluster.

  6. Click the **Active queries view** tab. The tab contains a summary of active queries running along with the top 50 longest running transactions.

You can filter the information by either of the following:

     * **Database** : filters query load on a specific database or all databases.
     * **User** : filters query load from a specific database user or all of the users.
     * **Node ID** : displays only for [read pool](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create) instances; filters query load on a specific read pool instance node or all of the nodes.

**Summary scorecard of all normalized active queries** : provides an overview of all the active queries by displaying the total connections based on the following parameters:

     * Distribution of active connections categorized by connection state.
     * Distribution of active connections based on different wait event types.
     * Distribution of transaction durations for queries that are not in an idle state.

**Longest running transactions** : provides an overview of the top 50 running queries in the `active` and `idle in transaction` state based on descending execution time.




You can view a list of top fifty normalized active queries on the query insights dashboard.

A normalized active query removes sensitive data, and returns a digest. Two queries that are identical except for WHERE-clause values have the same digest. For example, consider the following three example queries:

  * `select * from my_table where id = 1;`
  * `select * from my_table where id = 2;`
  * `select * from my_table where id = 100;`



The normalized version of these queries is the following digest:

`select * from my_table where id = ?;`

A query that runs in different sessions is displayed as different entries on the dashboard.

### View top longest running transactions

The following table describes the columns of the **Longest running transactions** table on the query insights dashboard:

Column name | Description  
---|---  
Process ID | Process ID is the unique identifier of the database connection.  
Node ID | Node ID is the unique identifier of the [read pool](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create) instance node that a query runs on.  
Query | Normalized SQL query text.  
Status | The current status of the connection. Status values include `active` and `idle in transaction`.  
Session duration | The duration of current session (in seconds).  
Transaction duration | The duration of current transaction (in seconds).  
Query duration | The duration of current active Query (in seconds). Query duration of queries in the `idle in transaction` state are `0` as they are not actively running.  
Wait event type | The occurring wait event type during query execution.  
Wait event | The occurring wait event during query execution.  
Database | Database name on which this connection is running.  
Application name | Application name on which this connection is running.  
User name | Name of the database user connected to the database.  
Client address | Specific IP address of the client that sent a query.  
Action | Contains a link for terminating a transaction.  
  
The display is refreshed every 60 seconds automatically.

Using the **Database** and **User** fields for filtering refreshes the data on the page.

To analyze static data, disable **Auto-refresh** and use the **Filter** field of the **Longest running transactions** table as needed.

## Terminate a query or transaction

To terminate a query or a transaction, you must have the [`databaseinsights.operationsAdmin`](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.operationsAdmin) role. For more information, see [IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/understanding-roles).

A transaction can contain multiple queries. To identify which of the queries are active at the moment, see the **Query** column in the **Longest running transaction** table.

To terminate a query or transaction, complete the following steps:

  1. Select the query in the **Longest running transaction** table.
  2. Scroll right to the **Action** column.
  3. Click **Terminate connection**.
  4. In the **Terminate connection** window, click **Confirm**.

The page refreshes after initiating termination. If termination fails, it is silent and the query continues showing up in the Active Query list. If termination is successful, the query no longer displays in the list.


**Warning:** Data inconsistency issues might arise when you forcefully terminate backend processes in the middle of a transaction.

## What's next

  * [Improve query performance using query insights](https://docs.cloud.google.com/alloydb/docs/using-query-insights)
  * [Monitor instances](https://docs.cloud.google.com/alloydb/docs/monitor-instance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
