---
url: https://docs.cloud.google.com/alloydb/docs/use-index-advisor-with-query-insights/
title: Use the AlloyDB for PostgreSQL index advisor with query insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:00.764807+00:00
---

# Use the AlloyDB for PostgreSQL index advisor with query insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/use-index-advisor-with-query-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Use the AlloyDB for PostgreSQL index advisor with query insights Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the AlloyDB for PostgreSQL index advisor with query insights to view index advisor recommendations and create recommended indexes—including ScaNN vector indexes— to improve query performance.

To learn more about the index advisor, see [Index advisor overview](https://docs.cloud.google.com/alloydb/docs/index-advisor-overview).

You can use Gemini Cloud Assist to help you monitor and troubleshoot your AlloyDB resources. For more information, see [Monitor and troubleshoot with Gemini assistance](https://docs.cloud.google.com/alloydb/docs/monitor-troubleshoot-with-gemini).

To learn how to use the index advisor to view and query recommendations as a table, or to request an on-demand analysis and report, see [Use the index advisor](https://docs.cloud.google.com/alloydb/docs/use-index-advisor).

## Before you begin

To access the query insights dashboard, [enable access to AlloyDB in your Google Cloud project](https://docs.cloud.google.com/alloydb/docs/project-enable-access).

### Enable the required extensions

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Query Insights** page, click **Edit query settings**.

  4. Click **Enable index advisor**.




### Required roles

To use the AlloyDB index advisor, you need permissions to do the following:

  * To access index recommendations, you need permissions to access the AlloyDB query insights dashboard.
  * To edit the index advisor settings, you need permissions to update AlloyDB instances.



To get these permissions, ask your administrator to grant you one of the following roles:

  * Basic viewer (`roles/viewer`)
  * Database Insights viewer (`roles/databaseinsights.viewer`)



For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Disable index advisor recommendations

To disable index advisor recommendations, follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. From the list of clusters and instances, click an instance.

  3. Click **Query Insights**.

  4. Click **Edit settings**.

  5. Disable the index advisor recommendations by deselecting **Enable recommendations**. Index advisor recommendations are enabled by default.

**Note:** To disable only vector search index recommendations, you can set the `google_db_advisor.enable_vector_index_advisor` database flag to `off`.



## Change the refresh frequency for index advisor recommendations

To change the refresh frequency, follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. From the list of clusters and instances, click an instance.

  3. Click **Query insights**.

  4. Click **Edit settings**.

  5. Increase or decrease the refresh frequency for index advisor recommendations. The default refresh frequency is every 24 hours.




## View and filter the index advisor recommendations

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. From the list of clusters and instances, click an instance.

  3. Click **Query insights**. All index advisor recommendations, including vector search index recommendations, are displayed in the **Recommendations** column of the **Top dimensions by database load** table.

  4. (Optional) To view only queries with CREATE INDEX recommendations, add a filter for **Recommendation: Create Indexes**.




## View recommendations for a query

To view details of index recommendations for a specific query, follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. From the list of clusters and instances, click an instance.

  3. Click **Query insights**.

  4. In the **Top dimensions by database load** table, click **Queries**.

  5. To learn recommendation details about a query, do one of the following:

     * Click a query to learn more about recommendations for the selected query, including the following information: 
       * **Performance impact** (high, medium, and low): The estimated query speed after all recommended indexes are created.
       * **Recommendations** : Create index recommendations.
       * **Tables impacted** : The number of tables that will be impacted when indexes are created.
       * **Additional estimated storage needed** : The estimated storage size needed to create all the recommended indexes.
       * **Number of impacted queries** : The total number of queries in the workload impacted by the index recommendations. An index may benefit multiple queries.
     * Click **Create Indexes** for a specific query to learn detailed recommendations about creating indexes to improve query performance.



## View impacted queries

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. From the list of clusters and instances, click an instance.

  3. Click **Query insights**.

  4. In the **Top dimensions by database load** table, click **Queries**.

  5. Click **Create indexes** for a specific query.

  6. Click **Show impacted queries**.

  7. Click a query to learn details about the impacted query.




## Create recommended indexes

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. From the list of clusters and instances, click an instance.

  3. Click **Query insights**.

  4. In the **Top dimensions by database load** table, click **Queries**.

  5. Click **Create Indexes** for a specific query.

  6. Click **Copy all index commands**. The CREATE INDEX commands are copied to your clipboard.

  7. Connect to the primary instance on the command line.

  8. To create the recommended indexes, run the commands that were copied to your clipboard, for example:
         
         CREATE INDEX ON "public"."demo_order" ("customer_id");




## What's next

  * Learn how to [use the index advisor](https://docs.cloud.google.com/alloydb/docs/use-index-advisor) to view and query recommendations as a table, or to request an on-demand analysis and report.
  * Learn how [AlloyDB helps make smart indexes](https://cloud.google.com/blog/products/databases/how-the-alloydb-index-advisor-helps-make-smart-indexes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
