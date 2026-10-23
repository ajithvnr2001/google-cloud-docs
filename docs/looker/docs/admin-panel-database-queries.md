---
url: https://docs.cloud.google.com/looker/docs/admin-panel-database-queries/
title: Admin settings - Queries \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:56.046755+00:00
---

# Admin settings - Queries  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-database-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Queries Stay organized with collections  Save and categorize content based on your preferences. 

The **Queries** page in the **Database** section of the **Admin** menu lists information about the last 50 queries that Looker submitted to your database. For information about queries that are older than the most recent 50 queries, see the [**Usage**](https://docs.cloud.google.com/looker/docs/admin-panel-server-usage) section of Looker.

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

## Basic query information

Column | Definition  
---|---  
Time | The start time of the query, displayed in your [application time zone](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#application_time_zone).  
Status | The status of the query, which can include: 

  * **Cache** : Looker returned the results from its cache instead of running a duplicate query against the database.
  * **Complete** : The query was completed successfully.
  * **Error** : The query wasn't completed successfully because an error occurred, the details of which can be found by clicking the Details button.
  * **Cancelled** : The query was cancelled by Looker or the user.
  * **Waiting for PDT** : The query needs to wait for a [persistent derived table](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables) to be built before it can be executed.
  * **Building PDT** : A [persistent derived table](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables) is in the process of being built.
  * **Queued** : The query is waiting to be executed because too many queries are already in progress (queries can be limited by Looker in your [connection setup](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_connections) or your database).
  * **Running** : The query is in the process of being run.
  * **Unknown** : Looker wasn't able to determine what happened with this query.

  
Connection | The Looker [connection](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) under which this query was run.  
User | The user who ran this query, if that can be determined. Some queries are not executed by a specific user, such as when Looker creates a [persistent derived table](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables) or when an unknown user accesses a [public Look](https://docs.cloud.google.com/looker/docs/publishing-looks-with-public-urls).  
Source | The source of the query in Looker, such as the Explore page or SQL Runner. If possible, a link to the saved Look, or the [query ID](https://docs.cloud.google.com/looker/docs/admin-panel-server-usage#field_definitions) along with the name of the model and Explore, is also displayed. Some queries don't have additional information, such as those that are run in SQL Runner. Queries that are issued from the [Open SQL Interface](https://docs.cloud.google.com/looker/docs/sql-interface#identifying-sql-interface-queries-in-the-looker-ui) have a **Source** value of `Sql_interface`.  
Runtime | The time it took to run the query. This includes the construction of the query, any time the query spent in the queue, transit to and from the database, and database execution of the query.If the query is running, the runtime will show how long the query has been running. For queries that were run previously, the runtime will also show an estimate of how much time the query will take to finish running. The estimate is based on the duration of the last run of the query and will say something like "of about 2s".  
Details Button | See The Details Button subsection on this page for additional details.  
  
## The Details button

Clicking the **Details** button to the right of any query will bring up additional information about that query. The **Query Details** menu includes the following:

  * An **Info** section that includes details about the query (see the following table).
  * A **SQL** section that shows the raw SQL that was executed against the database. [**Context Comments**](https://docs.cloud.google.com/looker/docs/admin-panel-server-usage#sql_comments) will not appear in the **Query Details** information. To prevent comments from affecting query caching, Looker adds the context comments to outgoing SQL commands right before the SQL is sent to the database.
  * A **SQL Interface query** section that appears when a query has been issued through the [Open SQL Interface](https://docs.cloud.google.com/looker/docs/sql-interface#identifying-sql-interface-queries-in-the-looker-ui). This section displays the SQL query that was sent to Looker from the external BI tool and can aid in troubleshooting and reproducing issues.
  * An **Open in SQL Runner** link that will open the query in [SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-basics).



The **Info** section includes the following information:

Section | Definition  
---|---  
History ID | The [history ID](https://docs.cloud.google.com/looker/docs/admin-panel-server-usage#field_definitions) of the query, if available.  
Status | The status of the query, as described in the basic query information table.  
Message | If the query contains a PDT, the [PDT generation comment](https://docs.cloud.google.com/looker/docs/derived-tables#query_comments_for_pdts) appears in this field. If the query does not contain a PDT, the field does not appear.  
Connection | The Looker [connection](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) under which this query was run.  
User | The user who ran this query, if that can be determined. Some queries are not executed by a specific user, such as when Looker creates a [persistent derived table](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables) or when an unknown user accesses a [public Look](https://docs.cloud.google.com/looker/docs/publishing-looks-with-public-urls).  
Source | The source of the query in Looker, such as the **Explore** page or SQL Runner. If possible, additional information is displayed, such as a link to the saved Look, the [query ID](https://docs.cloud.google.com/looker/docs/admin-panel-server-usage#field_definitions), model name, Explore name, or the fields that were selected.  
Start Time | The start time of the query, displayed in your [application time zone](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#application_time_zone).  
End Time | The finish time of the query, displayed in your [application time zone](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#application_time_zone).  
Runtime | The length of time it took to run the query.  
  
## Query killing

For dialects that support query killing, Looker can stop running queries in the following ways:

  * **Automatically** : Looker automatically stops a query if the user closes the browser tab in which the query is running.
  * **Individually** : Looker admins can stop an individual running query from the **Queries** Admin page by clicking the **Stop** button for that query. (Users with the [`see_queries` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_queries) can view the **Queries** page, but only Looker admins can stop a running query.)
  * **In bulk** : Looker admins can stop multiple running queries simultaneously across the entire instance or for a specific database connection by using the emergency query cleanup feature on the **Queries** page.

**Note:** Google BigQuery connections that are configured for [OAuth authentication](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#oauth_for_bigquery_connections) don't support query killing.

### Stop queries in bulk

If your Looker instance becomes unhealthy or degraded because of query buildup (for example, hanging queries are exhausting the available query slots, or the **Queries** page becomes slow or unresponsive), Looker admins can stop running queries in bulk without restarting the instance.

**Caution:** Bulk query cleanup terminates running queries immediately and affects all users on your instance. Use this feature only when the instance or connection is in a degraded state.

To stop queries in bulk, follow these steps:

  1. In Looker, go to the **Queries** page in the **Admin** menu.
  2. In your browser address bar, append `?cleanup=true` to the end of the URL, and then press **Enter**. For example:
         
         https://INSTANCE_NAME.cloud.looker.com/admin/queries?cleanup=true
         

  3. The **Emergency Query Cleanup** section appears above the queries table.

  4. Perform either of the following actions:

     * **Stop all running queries across the instance** : Click **Kill ALL Running Queries**.
     * **Stop all running queries for a specific connection** : Select a database connection from the **Connection** drop-down list, and then click **Kill Queries on Connection**.
  5. In the confirmation dialog, confirm that you want to terminate the running queries.




If an unhealthy or unresponsive database connection causes repeated query buildup, admins can also temporarily disable the connection by using the [**Disable Connection**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#disable_connection) option on the [**Connections Settings**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) page.

### Supported dialects for query killing

For Looker to kill queries—whether automatically by closing the browser tab, individually on the **Queries** page, or in bulk by using emergency query cleanup—your database dialect must support query killing. The following table shows which dialects support query killing in the latest release of Looker:

Dialect | Supported?  
---|---  
Actian Avalanche|   
Amazon Athena|   
Amazon Aurora MySQL|   
Amazon Redshift|   
Amazon Redshift 2.1+|   
Amazon Redshift Serverless 2.1+|   
Apache Druid|   
Apache Druid 0.13.x - 0.17.x|   
Apache Druid 0.18+|   
Apache Hive 2.3+|   
Apache Hive 3.1.2+|   
Apache Spark 3+|   
ClickHouse|   
ClickHouse 26+|   
Cloudera Impala 3.1+|   
Cloudera Impala 3.1+ with Native Driver|   
Cloudera Impala with Native Driver|   
DataVirtuality|   
Databricks|   
Denodo 7|   
Denodo 8 & 9|   
Dremio|   
Dremio 11+|   
Dremio 26+ with Arrow Flight SQL|   
Exasol|   
Google BigQuery Legacy SQL|   
Google BigQuery Standard SQL|   
Google Cloud AlloyDB for PostgreSQL|   
Google Cloud PostgreSQL|   
Google Cloud SQL|   
Google Spanner|   
Greenplum|   
HyperSQL|   
IBM Netezza|   
MariaDB|   
Microsoft Azure PostgreSQL|   
Microsoft Azure SQL Database|   
Microsoft Azure Synapse Analytics|   
Microsoft SQL Server 2008+|   
Microsoft SQL Server 2012+|   
Microsoft SQL Server 2016|   
Microsoft SQL Server 2017+|   
MongoBI|   
MongoSQL|   
MySQL|   
MySQL 8.0.12+|   
Oracle|   
Oracle ADWC|   
PostgreSQL 9.5+|   
PostgreSQL pre-9.5|   
PrestoDB|   
PrestoSQL|   
SAP HANA|   
SAP HANA 2+|   
SingleStore|   
SingleStore 7+|   
Snowflake|   
Teradata|   
Trino|   
Vector|   
Vertica|   
  
## Query timeouts and queueing

Looker kills queries that have been waiting in queue for too long. This operation is called a _timeout_. Several timeouts may apply to your query:

  * **Connection pool timeout and maximum concurrent queries** : To prevent overloading of your database with concurrent queries, Looker holds excess concurrent queries in the Looker query queue, and will kill queries that remain in queue for too long. By default, 75 maximum concurrent queries are allowed per connection. Additional queries beyond the connection limit will be timed out after 0 seconds. To change these defaults, configure the [Max connections](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_connections), [**Max concurrent queries for this connection**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max-queries), and [**Connection pool timeout**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#connection_pool_timeout) settings on a connection's [**Connections Settings**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) page.

  * **Per-user query limit and timeout** : To prevent any single user from filling up the Looker query queue, each user has a maximum number of allowed concurrent queries and a corresponding queue timeout for queries that are queued because of concurrent query limit. The per-user limit applies to both users who log in to Looker using the regular authentication process, and to users who log in using API user credentials. There are two ways you can define the maximum number of per-user concurrent queries for connections on your Looker instance:

    * The [`per-user-query-limit` startup option](https://docs.cloud.google.com/looker/docs/startup-options#per-user-query-limit). This is an instance-wide setting that sets the default for connections on your instance. The `per-user-query-limit` startup option limits the number of concurrent queries per user, per connection, per node on the Looker instance. The default maximum of 15 concurrent queries per user applies to each valid connection and, if your Looker instance is [clustered](https://docs.cloud.google.com/looker/docs/clustering-looker), to each node in the cluster. By default, each user can run a maximum of 15 concurrent queries per connection, per node, with a timeout of 600 seconds. For example, if you have a 5-node cluster with a `per-user-query-limit` of 15, each node will allow 15 concurrent queries per user for this connection, for a total of 75 queries across all nodes (15 * 5 = 75). 

You can change the per-user query limit for a connection by using the **Max concurrent queries per user for this connection** setting on the connection's **Connection Settings** page. If your Looker instance is customer-hosted, you can change the default maximum number of per-user concurrent queries by configuring the `--per-user-query-limit` startup option, and you can configure the queue timeout by using the [`--per-user-query-timeout`startup option](https://docs.cloud.google.com/looker/docs/startup-options#per-user-query-timeout).

    * The [**Max concurrent queries per user for this connection**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_concurrent_queries_per_user_for_this_connection) option in the [**Connections Settings**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) for a connection. The **Max concurrent queries per user for this connection** setting has a default of 25, and is per user and per connection, but not per node. For example, if you have a 5-node cluster and you set this value to 15, each node will allow 3 concurrent queries per user for this connection (15 / 5 = 3), for a total of 15 queries across all nodes. For a connection, if a value is provided for the **Max concurrent queries per user for this connection** setting, the **Max concurrent queries per user for this connection** value will override the `per-user-query-limit` startup option for the connection. 
  * **Scheduler query limit and timeout** : To prevent overloading of the Looker scheduler process, a Looker instance can run a maximum of 10 concurrent scheduled queries, and the timeout for queries in the scheduler queue is 1,200 seconds. If your Looker instance is customer-hosted, you can change these defaults by configuring the `--scheduler-query-limit` and `--scheduler-query-timeout` [startup options](https://docs.cloud.google.com/looker/docs/startup-options).

**Note:** If your Looker instance is [clustered](https://docs.cloud.google.com/looker/docs/clustering-looker), then each node of the cluster uses its own scheduler queue. Thus, adding nodes to your cluster increases your total amount of allowed concurrent scheduled queries without placing additional burden on the Looker scheduler process.
  * **Renderer query limit and timeout** : To prevent overloading of the Looker renderer process, a Looker instance can render a maximum of 2 concurrent image-based downloads, such as PDF and PNG formats. If your Looker instance is customer-hosted, you can change this default by configuring the `--concurrent-render-jobs` [startup option](https://docs.cloud.google.com/looker/docs/startup-options).

**Note:** If your Looker instance is [clustered](https://docs.cloud.google.com/looker/docs/clustering-looker), then each node of the cluster uses its own renderer queue. Thus, adding nodes to your cluster increases your total amount of allowed concurrent renderer jobs without placing additional burden on the Looker renderer process.



* **Webhook timeout** : Looker will attempt [data delivery to a webhook](https://docs.cloud.google.com/looker/docs/scheduling#delivery_options) for a maximum of 30 minutes. If Looker cannot communicate with the webhook destination in 30 minutes, the query will time out. This timeout is not configurable.

  * **Proxy timeout** : Customer-hosted instances often use proxies with a default timeout of 60 seconds. We recommend that this timeout be increased to 60 minutes. See the [Running Looker behind a proxy server or load balancer](https://discuss.google.dev/t/running-looker-behind-a-proxy-server-or-load-balancer/117104) Looker Community post for more information.

  * **Database timeout** : Most databases have rules for queueing and timeouts that are independent of Looker's queues and timeouts. For example, a query may have left the Looker queue, but it can still be queued on your database. Check the documentation for your database for more information on customizing database query timeouts.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
