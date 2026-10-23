---
url: https://docs.cloud.google.com/alloydb/docs/use-index-advisor/
title: Use the index advisor \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:53.398135+00:00
---

# Use the index advisor  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/use-index-advisor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Use the index advisor Stay organized with collections  Save and categorize content based on your preferences. 

AlloyDB for PostgreSQL offers an _index advisor_ that tracks the queries your database regularly handles. Periodically, it analyzes these queries to recommend new indexes that can increase the queries' performance.

You can view and query its recommendations as a table, or request an on-demand analysis and report at any time.

## Before you begin

Before you use the index advisor, make sure that you meet the following requirements.

### Enable the required extensions

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Query Insights** page, click **Edit query settings**.

  4. Click **Enable index advisor**.




## View the index advisor's recommendations

AlloyDB automatically runs the index advisor's analysis periodically. You can read its results through two table views located in each of your databases:

  * `google_db_advisor_recommended_indexes` lists any recommended new indexes for its database. It also includes estimates of the storage required for each index, and the number of queries that each index can affect.

  * `google_db_advisor_workload_report` lists each query for which the advisor recommends one or more new indexes. Each row summarizes the recommendations for the relevant query.




For example, to see the results of the most recent index-recommendation analysis, formatted as a table, run this query:
    
    
    SELECT * FROM google_db_advisor_recommended_indexes;
    

If the index advisor's most recent analysis finds no recommendations, then this query returns a table with no rows.

Because all of these reports exist as ordinary database views, you can write queries that filter or present information in any way you want. For example, to see a report that pairs recommended indexes with their full associated query, join the `google_db_advisor_workload_report` and `google_db_advisor_workload_statements` views on their respective `query_id` columns:
    
    
    SELECT DISTINCT recommended_indexes, query
    FROM google_db_advisor_workload_report r, google_db_advisor_workload_statements s
    WHERE r.query_id = s.query_id;
    

## Manually request an index analysis

Rather than wait for the index advisor's next scheduled analysis, you can request that AlloyDB run an analysis immediately and display its report. To do this, run this SQL function:
    
    
    SELECT * FROM google_db_advisor_recommend_indexes();
    

After the analysis finishes, AlloyDB displays a table-formatted report with the description and estimated storage needs of any recommended indexes. If the analysis finds no new indexes to recommend, then the view contains no rows.

Note that [the PostgreSQL user role](https://docs.cloud.google.com/alloydb/docs/database-users/about) that runs this command can affect the recommendations displayed. If this query is run by `postgres` or another user with the `alloydbsuperuser` role, then AlloyDB displays all of the index advisor's current recommendations. Otherwise, AlloyDB limits its display to index recommendations based on queries issued by the current database user.

## Apply the index advisor's recommendations

The `index` column of the `google_db_advisor_recommended_indexes` view contains, in each row, a complete PostgreSQL `CREATE INDEX` DDL statement for generating the index recommended in that row.

To apply that row's recommendation, run that DDL statement, exactly as presented. This includes copying it onto your clipboard and pasting it into a `psql` prompt.

For example, consider this output from manually running an analysis, using the query described in the previous section:
    
    
                        index                   | estimated_storage_size_in_mb
    --------------------------------------------+------------------------------
     CREATE INDEX ON "School"."Students"("age") |                            3
    (1 row)
    

This report contains a single recommendation: adding a new single-column index on the `age` column in the `School` schema's `Students` table. To apply this advice, enter a DDL query exactly as represented within the report:
    
    
    CREATE INDEX ON "School"."Students"("age");
    

## View the index advisor's tracked queries

The `google_db_advisor_workload_statements` view contains a list of all the queries that the index advisor has tracked, as well as important metadata for each one, such as the following metrics:

  * The number of times the instance executed this query
  * The total time the instance spends processing these queries
  * The ID of the database user running these queries



## Clear the index advisor's tracked queries

You can reset the index advisor's behavior on an instance by clearing its tracked queries. To do this, run this SQL function:
    
    
    SELECT google_db_advisor_reset();
    

AlloyDB immediately empties the index advisor's collection of tracked queries.

## Configure the index advisor

While the index advisor works for most use cases with its default settings, you can fine-tune its behavior by setting various database flags.

For example, you can set the `google_db_advisor.enable_vector_index_advisor` flag to let the index advisor recommend indexes for vector queries. This flag is enabled by default.

To learn more, see [Index advisor flags](https://docs.cloud.google.com/alloydb/docs/reference/index-advisor-flags).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
