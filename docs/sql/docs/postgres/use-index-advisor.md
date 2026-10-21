---
url: https://docs.cloud.google.com/sql/docs/postgres/use-index-advisor/
title: Use index advisor \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:40.423798+00:00
---

# Use index advisor  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/use-index-advisor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Use index advisor Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/use-index-advisor "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/use-index-advisor "View this page for the SQL Server database engine")

This page describes the Cloud SQL for PostgreSQL index advisor and how you can view and apply its index recommendations.

Cloud SQL for PostgreSQL offers a fully managed index advisor that tracks the queries your database handles regularly. Periodically, the index advisor analyzes these queries to recommend new indexes that can improve query performance. The index advisor lets you detect and fix performance issues with systems and queries.

## How does the index advisor work?

The index advisor helps you improve query processing by doing the following:

  * Recommend a set of indexes with SQL commands to create indexes.
  * Provide data to help you evaluate recommended indexes, for example, estimated storage size and impact of indexes on a query.

The index advisor stores and displays the `CREATE INDEX` command containing the database name, schema name, table name, and column names. The tracked queries are all normalized queries with all literals removed. 

Index recommendations are encrypted at rest.

## Limitations

Cloud SQL for PostgreSQL index advisor has the following limitations:

  * The index advisor provides `CREATE INDEX` recommendations only.
  * The index advisor doesn't support instances with the following configurations:
    * Cloud SQL Enterprise edition instances
    * Read replica instances



## Before you begin

To obtain index advisor recommendations, you must use Cloud SQL Enterprise Plus edition and enable [query insights for Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights#enable-enterprise-plus-query-insights) for your Cloud SQL instance.

### Required roles and permissions

To get the permissions that you need to obtain index advisor recommendations, ask your administrator to grant you the [Cloud SQL Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.viewer) (`roles/cloudsql.viewer`) IAM role on the project that hosts the Cloud SQL instance. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to obtain index advisor recommendations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to obtain index advisor recommendations:

  * `databaseinsights.recommendations.query`
  * `databaseinsights.resourceRecommendations.query`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable index advisor recommendations

To enable index advisor recommendations, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

.
  2. To open the **Overview** page of an instance, click the instance name. .
  3. In the **Configuration** tile, click **Edit configuration**.
  4. In the **Customize your instance** section, expand **Query insights**.
  5. Make sure **Enable Query insights** is enabled.
  6. If not already selected, select **Enable Enterprise Plus features**.
  7. Select **Enable index advisor**.
  8. Click **Save**.

**Note:** If your instance is running with PostgreSQL maintenance version `20250302.00_RC30` or earlier and you enable index advisor, then the instance restarts. For more information regarding restart requirements, see [Enable query insights](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights#enable-insights).

## Disable index advisor recommendations

To disable index advisor recommendations, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. In the **Configuration** tile, click **Edit configuration**.
  4. In the **Customize your instance** section, expand **Query insights**.
  5. Clear the **Enable index advisor** checkbox.
  6. Click **Save**.



## View index advisor recommendations

Cloud SQL automatically runs the index advisor analysis periodically. To view index advisor recommendations, use the Query insights dashboard. You can also view and query the index advisor recommendations as a table or request an on-demand analysis and report at any time. 

### View and filter recommendations in the Query insights dashboard

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Query insights**.
  4. The index advisor recommendations are displayed in the **Recommendation** column of the **Top queries and tags** section.
  5. Optional: To view only the queries with `CREATE INDEX` recommendations, add a filter for **Recommendation: Create Indexes**.



### View recommendations for a query

To view index recommendations for a specific query, follow these steps:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Query insights**.
  4. In the **Top queries and tags** section, click **Queries**.
  5. To get recommendation details for a query, do one of the following: 
     * Click a query to learn more about the recommendations for the selected query, including the following information: 
       * **Performance impact** (high, medium, and low): The estimated query speed after all recommended indexes are created.
       * **Recommendations** : Create index recommendations.
       * **Tables impacted** : The number of tables that will be impacted when indexes are created.
       * **Additional estimated storage needed** : The estimated storage size needed to create all the recommended indexes.
       * **Number of impacted queries** : The total number of queries in the workload impacted by the index recommendations. An index can benefit multiple queries.
     * Click **Create Indexes** for a specific query to learn detailed recommendations about creating indexes to improve query performance.



### View recommendations as a database table view

You can read its results through the following table views located in each of your databases: 

  * `google_db_advisor_recommended_indexes`: lists any recommended new indexes for each database. It also includes estimates of the storage required for each index, and the number of queries that each index can affect.

  * `google_db_advisor_workload_report`: lists each query for which the advisor recommends one or more new indexes. Each row summarizes the recommendations for the relevant query.




For example, to see the results of the most recent index-recommendation analysis, formatted as a table, run this query:
    
    
    SELECT * FROM google_db_advisor_recommended_indexes;
    

If the index advisor's most recent analysis finds no recommendations, then this query returns a table with no rows.

Because all of these reports exist as ordinary database views, you can write queries that filter or present this information. For example, to see a report that pairs recommended indexes with their full associated query, join the `google_db_advisor_workload_report` and `google_db_advisor_workload_statements` views on their respective `query_id` columns:
    
    
    SELECT DISTINCT recommended_indexes, query
    FROM google_db_advisor_workload_report r, google_db_advisor_workload_statements s
    WHERE r.query_id = s.query_id;
    

## Manually request an index analysis

Rather than wait for the index advisor's next scheduled analysis, you can request that Cloud SQL for PostgreSQL run an analysis immediately and display its report. For Cloud SQL for PostgreSQL, you need to wait at least 15 minutes after enabling index advisor to run a manual analysis. To do this, run this SQL function:
    
    
    SELECT * FROM google_db_advisor_recommend_indexes();
    

After the analysis finishes, Cloud SQL for PostgreSQL displays a table-formatted report with the description and estimated storage needs of any recommended indexes. If the analysis finds no new indexes to recommend, then the view contains no rows.

Note that [the user role](https://docs.cloud.google.com/sql/docs/postgres/users) that runs this command can affect the recommendations displayed. Cloud SQL for PostgreSQL limits its display to index recommendations based on queries issued by the current database user.

## Create recommended indexes

You can create recommended indexes from the Query insights dashboard or from a database table view.

### Create a recommended index using the Query insights dashboard

To create a recommended index using the Query insights dashboard, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Query insights**.
  4. In the **Top dimensions by database load** table, click **Queries**.
  5. Click **Create Indexes** for a specific query.
  6. Click **Copy all index commands**. The `CREATE INDEX` commands are copied to your clipboard.
  7. Connect to the primary instance on the command line.
  8. To create the recommended indexes, run the commands that were copied to your clipboard, for example:
         
         CREATE INDEX ON "public"."demo_order" ("customer_id");




### Create a recommended index using a database table view

The `index` column of the `google_db_advisor_recommended_indexes` view contains, in each row, a complete PostgreSQL `CREATE INDEX` DDL statement for generating the index recommended in that row.

To apply that row's recommendation, run that DDL statement, exactly as presented. This includes copying it onto your clipboard and pasting it into a `psql` prompt.

For example, consider this output from manually running an analysis, using the query described in the previous section:
    
    
                        index                   | estimated_storage_size_in_mb
    --------------------------------------------+------------------------------
     CREATE INDEX ON "School"."Students"("age") |                            3
    (1 row)
    

This report contains a single recommendation: adding a single-column index on the `age` column in the `School` schema's `Students` table. To apply this advice, enter a DDL query as represented within the report:
    
    
    CREATE INDEX ON "School"."Students"("age");
    

## View impacted queries

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Query insights**.
  4. In the **Top dimensions by database load** table, click **Queries**.
  5. Click **Create indexes** for a specific query.
  6. Click **Show impacted queries**.
  7. Click a query to learn details about the impacted query.



## View index advisor tracked queries

The `google_db_advisor_workload_statements` view contains a list of all the queries that the index advisor has tracked, as well as important metadata for each one, such as the following metrics:

  * The number of times the instance executed each query
  * The total time the instance spends processing these queries
  * The ID of the database user running these queries



## Clear the index advisor's tracked queries

You can reset the index advisor's behavior on an instance by clearing its tracked queries. To do this, run this SQL function:
    
    
    SELECT google_db_advisor_reset();
    

Cloud SQL for PostgreSQL empties the index advisor's collection of tracked queries immediately.

## What's next

  * [Use query insights](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
