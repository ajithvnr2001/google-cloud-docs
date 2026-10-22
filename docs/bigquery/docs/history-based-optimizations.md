---
url: https://docs.cloud.google.com/bigquery/docs/history-based-optimizations/
title: Use history-based optimizations \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:09.469957+00:00
---

# Use history-based optimizations  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/history-based-optimizations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use history-based optimizations

This guide describes how history-based optimizations work and how to estimate their impact for queries.

## About history-based optimizations

History-based optimizations automatically use information from already-completed executions of the same or similar queries to apply additional optimizations and further improve query performance, such as slot time consumed and query latency. For example, the first query execution might take 60 seconds, but the second query execution might take only 30 seconds if a history-based optimization was identified. This process continues until there are no additional optimizations to add.

The following is an example of how history-based optimizations work with BigQuery:

Execution count | Query slot time consumed | Notes  
---|---|---  
1 | 60 | Original execution.  
2 | 30 | First history-based optimization applied.  
3 | 20 | Second history-based optimization applied.  
4 | 21 | No additional history-based optimizations to apply.  
5 | 19 | No additional history-based optimizations to apply.  
6 | 20 | No additional history-based optimizations to apply.  
  
History-based optimizations are only applied when there is high confidence that there will be a beneficial impact to the query performance. In addition, when an optimization does not significantly improve query performance or may result in poorer performance, that optimization is revoked and not used in future executions of that query.

## Review history-based optimizations for a job

To review the history-based optimizations for a job, you can use a SQL query or a REST API method call.

###  SQL 

You can use a query to get the history-based optimizations for a job. The query must include [`INFORMATION_SCHEMA.JOBS_BY_PROJECT`](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs#schema) and the `query_info.optimization_details` column name.

In the following example, the optimization details are returned for a job called `sample_job`. If no history-based optimizations were applied, `NULL` is produced for `optimization_details`:
    
    
    SELECT
      job_id,
      query_info.optimization_details
    FROM `PROJECT_NAME.region-LOCATION`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
    WHERE job_id = 'sample_job'
    LIMIT 1;
    

The results look similar to the following:
    
    
    -- The JSON in optimization_details has been formatted for readability.
    /*------------+-----------------------------------------------------------------*
     | job_id     | optimization_details                                            |
     +------------+-----------------------------------------------------------------+
     | sample_job | {                                                               |
     |            |   "optimizations": [                                            |
     |            |     {                                                           |
     |            |       "semi_join_reduction": "web_sales.web_date,RIGHT"         |
     |            |     },                                                          |
     |            |     {                                                           |
     |            |       "semi_join_reduction": "catalog_sales.catalog_date,RIGHT" |
     |            |     },                                                          |
     |            |     {                                                           |
     |            |       "semi_join_reduction": "store_sales.store_date,RIGHT"     |
     |            |     },
     |            |     {                                                           |
     |            |       "join_commutation": "web_returns.web_item"                |
     |            |     },
     |            |     {                                                           |
     |            |       "parallelism_adjustment": "applied"                       |
     |            |     },
     |            |   ]                                                             |
     |            | }                                                               |
     *------------+-----------------------------------------------------------------*/
    

###  API 

To get the optimization details for a job, you can call the [`jobs.get` method](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/jobs/get).

In the following example, the `jobs.get` method returns the optimization details ([`optimizationDetails`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/Job#queryinfo)) in the full response:
    
    
    {
      "jobReference": {
        "projectId": "myProject",
        "jobId": "sample_job"
      }
    }
    

The results look similar to the following:
    
    
    -- The unrelated parts in the full response have been removed.
    {
      "jobReference": {
        "projectId": "myProject",
        "jobId": "sample_job",
        "location": "US"
      },
      "statistics": {
        "query": {
          "queryInfo": {
            "optimizationDetails": {
              "optimizations": [
                {
                  "semi_join_reduction": "web_sales.web_date,RIGHT"
                },
                {
                  "semi_join_reduction": "catalog_sales.catalog_date,RIGHT"
                },
                {
                  "semi_join_reduction": "store_sales.store_date,RIGHT"
                },
                {
                  "join_commutation": "web_returns.web_item"
                },
                {
                  "parallelism_adjustment": "applied"
                }
              ]
            }
          }
        }
      }
    }
    

## Estimate impact of history-based optimizations

To estimate the impact of history-based optimizations, you can use the following sample SQL query to identify project queries with the greatest estimated improvement to execution time.
    
    
      WITH
        jobs AS (
          SELECT
            *,
            query_info.query_hashes.normalized_literals AS query_hash,
            TIMESTAMP_DIFF(end_time, start_time, MILLISECOND) AS elapsed_ms,
            IFNULL(
              ARRAY_LENGTH(JSON_QUERY_ARRAY(query_info.optimization_details.optimizations)) > 0,
              FALSE)
              AS has_history_based_optimization,
          FROM region-LOCATION.INFORMATION_SCHEMA.JOBS_BY_PROJECT
          WHERE EXTRACT(DATE FROM creation_time) > DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
        ),
        most_recent_jobs_without_history_based_optimizations AS (
          SELECT *
          FROM jobs
          WHERE NOT has_history_based_optimization
          QUALIFY ROW_NUMBER() OVER (PARTITION BY query_hash ORDER BY end_time DESC) = 1
        )
      SELECT
        job.job_id,
        100 * SAFE_DIVIDE(
          original_job.elapsed_ms - job.elapsed_ms,
          original_job.elapsed_ms) AS percent_execution_time_saved,
        job.elapsed_ms AS new_elapsed_ms,
        original_job.elapsed_ms AS original_elapsed_ms,
      FROM jobs AS job
      INNER JOIN most_recent_jobs_without_history_based_optimizations AS original_job
        USING (query_hash)
      WHERE
        job.has_history_based_optimization
        AND original_job.end_time < job.start_time
      ORDER BY percent_execution_time_saved DESC
      LIMIT 10;
    

The result of the preceding query is similar to the following if history-based optimizations were applied:
    
    
      /*--------------+------------------------------+------------------+-----------------------*
       |    job_id    | percent_execution_time_saved | new_execution_ms | original_execution_ms |
       +--------------+------------------------------+------------------+-----------------------+
       | sample_job1  |           67.806850186245114 |             7087 |                 22014 |
       | sample_job2  |           66.485800412501987 |            10562 |                 31515 |
       | sample_job3  |           63.285605271764254 |            97668 |                266021 |
       | sample_job4  |           61.134141726887904 |           923384 |               2375823 |
       | sample_job5  |           55.381272089713754 |          1060062 |               2375823 |
       | sample_job6  |           45.396943168036479 |          2324071 |               4256302 |
       | sample_job7  |           38.227031526376024 |            17811 |                 28833 |
       | sample_job8  |           33.826608962725111 |            66360 |                100282 |
       | sample_job9  |           32.087813758311604 |            44020 |                 64819 |
       | sample_job10 |           28.356416319483539 |            19088 |                 26643 |
       *--------------+------------------------------+------------------+-----------------------*/
    

The results of this query is only an estimation of history-based optimization impact. Many factors can influence query performance, including but not limited to slot availability, change in data over time, view or UDF definitions, and differences in query parameter values.

If the result of this sample query is empty, then either no jobs have used history-based optimizations, or all queries were optimized more than 30 days ago.

This query can be applied to other query performance metrics such as `total_slot_ms` and `total_bytes_billed`. For more information, see the schema for [`INFORMATION_SCHEMA.JOBS`](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs#schema).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
