---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/maintain-vector-indexes/
title: Maintain vector indexes \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:32:44.429678+00:00
---

# Maintain vector indexes  |  AlloyDB Omni using the container orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/maintain-vector-indexes/

This page documents AlloyDB Omni version **18.3.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/overview)



Send feedback 

#  Maintain vector indexes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/maintain-vector-indexes)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/ai/maintain-vector-indexes)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/maintain-vector-indexes)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/maintain-vector-indexes)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/ai/maintain-vector-indexes)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/ai/maintain-vector-indexes)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/maintain-vector-indexes)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/ai/maintain-vector-indexes)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/ai/maintain-vector-indexes)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/ai/maintain-vector-indexes)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/ai/maintain-vector-indexes)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/ai/maintain-vector-indexes)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/ai/maintain-vector-indexes)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/ai/maintain-vector-indexes)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/ai/maintain-vector-indexes)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/ai/maintain-vector-indexes)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/maintain-vector-indexes)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/ai/maintain-vector-indexes)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/ai/maintain-vector-indexes)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/ai/maintain-vector-indexes)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/ai/maintain-vector-indexes)



This document explains different options that you can use to maintain vector indexes. You might want to maintain indexes to ensure that your indexes adapt to the changes in data that might impact accuracy of your search results. As your dataset grows, use the strategies in the following sections to avoid degradation in query performance.

## View vector index metrics

If your table is prone to frequent updates or insertions, then we recommend periodically reindexing the existing ScaNN index in order to improve the recall accuracy for your index. You can monitor index metrics to view changes in vector distributions or vector mutations since the index was built, and then reindex accordingly.

For more information about metrics, see [View vector index metrics](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/reference/vector-index-metrics).

## Manually rebuild your index

You can manually rebuild your index if you want to rebuild it with the configurations you specified when it was created.

To manually rebuild your index, run the following command:
    
    
    REINDEX INDEX CONCURRENTLY INDEX_NAME;
    

Replace `INDEX_NAME` with the name of the index you want to rebuild—for example, `my-scann-index`. The index names are shared across your database. Ensure that each index name is unique to each table in your database.

For more information about reindexing in PostgreSQL, see [REINDEX](https://www.postgresql.org/docs/15/sql-reindex.html).

## What's next

* [Vector index metrics](/alloydb/omni/kubernetes/18.3.0/docs/reference/vector-index-metrics) 

  * [Optimize vector query performance for ScaNN](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/scann-vector-query-perf-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
