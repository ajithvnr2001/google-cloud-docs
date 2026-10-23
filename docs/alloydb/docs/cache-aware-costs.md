---
url: https://docs.cloud.google.com/alloydb/docs/cache-aware-costs/
title: Enable cache-aware costs for index scan query plans \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:06.110422+00:00
---

# Enable cache-aware costs for index scan query plans  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/cache-aware-costs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Enable cache-aware costs for index scan query plans Stay organized with collections  Save and categorize content based on your preferences. 

To improve query performance and reduce database I/O costs, you can enable cache-aware index scan costing in AlloyDB for PostgreSQL. When you enable cache-aware index scan costing, the AlloyDB query planner adjusts the estimated I/O cost of index scans based on how many index and table pages are available in the shared buffer when execution starts, and selects the final query plan based on those adjusted costs.

After you enable cache awareness, the feature functions automatically and adjusts when shared buffer hit rates change. Cache awareness can also work with other query tuning practices, such as setting the AlloyDB query planner cost estimate in [`random_page_cost`](https://www.postgresql.org/docs/17/runtime-config-query.html#GUC-RANDOM-PAGE-COST).

**Tip:** We recommend that you enable cache awareness if you notice the query planner doesn't select better index scan based query plans.

## Enable cache-awareness

To enable cache awareness for your AlloyDB instance, set the [`alloydb.enable_cache_aware_costing`](https://docs.cloud.google.com/alloydb/docs/reference/alloydb-flags#alloydb.enable_cache_aware_costing) ([Preview](https://cloud.google.com/products#product-launch-stages)) flag to `on`. Also, you can set the flag at the session level to affect the query plans occurring under the same session. For information on how to set the flag, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

## Example scenario

The following code sample shows an index scan plan executed with a fully warmed shared buffer cache.
    
    
    explain (analyze, verbose, buffers)
    SELECT count(d) FROM t1 WHERE a = 10 AND b > 100 AND c > 100;
    
    
    
    ------------------ Aggregate  (cost=3908.93..3908.94 rows=1 width=8) (actual time=4.128..4.130 rows=1 loops=1)
       Output: count(d)
       Buffers: shared hit=926
       ->  Index Scan using idx1 on public.t1  (cost=0.43..3906.49 rows=975 width=2) (actual time=0.143..3.205 rows=919 loops=1)
             Output: a, b, c, d
             Index Cond: ((t1.a = 10) AND (t1.b > 100) AND (t1.c > 100))
             Buffers: shared hit=926
       Execution Time: 4.353 ms
    

During this execution, there were no I/O reads. Without cache awareness, the query planner includes I/O cost for the index scan query plan. This can result in the index scan query plan losing to a sequential scan query plan.

The following code snippet shows the adjusted query plan cost when cache awareness is enabled.
    
    
    explain (verbose)
    SELECT count(d) FROM t1 WHERE a = 10 AND b > 100 AND c > 100;
    
    
    
    ------------------ Aggregate  (cost=29.93..29.94 rows=1 width=8)
       Output: count(d)
       ->  Index Scan using idx1 on public.t1  (cost=0.43..27.49 rows=975 width=2)
             Output: a, b, c, d
             Index Cond: ((t1.a = 10) AND (t1.b > 100) AND (t1.c > 100))
    

The new cost, `27.49`, for the same index scan query plan is much lower than the old cost, `3906.49`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
