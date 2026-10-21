---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/generate-server-activity-report-reference/
title: Generate a server activity report \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:46:41.006178+00:00
---

# Generate a server activity report  |  AlloyDB Omni for Kubernetes: 16.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/generate-server-activity-report-reference/

This page documents AlloyDB Omni version **16.3.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/overview)



Send feedback 

#  Generate a server activity report Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.3.0keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/generate-server-activity-report-reference)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/generate-server-activity-report-reference)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/generate-server-activity-report-reference)

To generate a server activity report, you can use the PostgreSQL cumulative statistics system to collect and report information about server activity. The server activity information is exposed as system tables, which can be accessed using SQL queries. 

For example, the query reports the number of disk blocks found in the buffer cache and number of disk blocks read from disk:
    
    
    SELECT blks_hit, blks_read FROM pg_stat_database;
    

By observing the values of these counters over time, you can infer whether the database is making good use of the buffer cache.

The PostgreSQL documentation has more information about this [cumulative statistics system](https://www.postgresql.org/docs/16/monitoring-stats.html).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
