---
url: https://docs.cloud.google.com/sql/docs/sqlserver/use-index-advisor/
title: Use index advisor \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:36.050275+00:00
---

# Use index advisor  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/use-index-advisor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Use index advisor Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/use-index-advisor "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/use-index-advisor "View this page for the PostgreSQL database engine") | SQL Server

This page describes the Cloud SQL for SQL Server index advisor and how you can view and apply its index recommendations.

Cloud SQL for SQL Server offers a fully managed index advisor that tracks the queries your database handles regularly. Periodically, the index advisor analyzes these queries to recommend new indexes that can improve query performance. The index advisor lets you detect and fix performance issues with systems and queries.

## How does the index advisor work?

The index advisor helps you improve query processing by doing the following:

  * Recommend a set of indexes with SQL commands to create indexes.
  * Provide data to help you evaluate recommended indexes, for example, estimated storage size and impact of indexes on a query.

The index advisor stores and displays the `CREATE INDEX` command containing the database name, schema name, table name, and column names. The tracked queries are all normalized queries with all literals removed. 

Index recommendations are encrypted at rest.

## Limitations

Cloud SQL for SQL Server index advisor has the following limitations:

  * The index advisor provides `CREATE INDEX` recommendations only.
  * The index advisor doesn't support Cloud SQL Enterprise edition instances.



## Before you begin

To obtain index advisor recommendations, you must use Cloud SQL Enterprise Plus edition and enable [query insights for Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights#enable-enterprise-plus-query-insights) for your Cloud SQL instance.

### Required roles and permissions

To get the permissions that you need to obtain index advisor recommendations, ask your administrator to grant you the [Cloud SQL Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.viewer) (`roles/cloudsql.viewer`) IAM role on the project that hosts the Cloud SQL instance. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to obtain index advisor recommendations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to obtain index advisor recommendations:

  * `databaseinsights.recommendations.query`
  * `databaseinsights.resourceRecommendations.query`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable index advisor recommendations

When you [enable query insights for Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights#enable-insights), you enable index advisor recommendations automatically. For more information regarding restart requirements, see [Enable query insights](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights#enable-insights).

## Disable index advisor recommendations

You can't disable index advisor recommendations without disabling query insights for Cloud SQL Enterprise Plus edition.

To disable index advisor recommendations and query insights for Cloud SQL Enterprise Plus edition, see [Disable query insights for Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights#disable-enterprise-query-insights).

## View index advisor recommendations

Cloud SQL automatically runs the index advisor analysis periodically. To view index advisor recommendations, use the Query insights dashboard. 

### View and filter recommendations in the Query insights dashboard

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Query insights**.
  4. Click **Enable**. The index advisor recommendations are displayed in the **Recommendation** column of the **Queries** tab of the **Top dimensions by database load** section.
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



## View impacted queries

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Query insights**.
  4. In the **Top dimensions by database load** table, click **Queries**.
  5. Click **Create indexes** for a specific query.
  6. Click **Show impacted queries**.
  7. Click a query to learn details about the impacted query.



## What's next

  * [Use query insights](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
