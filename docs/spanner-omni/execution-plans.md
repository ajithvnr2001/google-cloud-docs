---
url: https://docs.cloud.google.com/spanner-omni/execution-plans/
title: View Spanner Omni execution plans \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:45.247525+00:00
---

# View Spanner Omni execution plans  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/execution-plans/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  View Spanner Omni execution plans Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to view Spanner Omni query execution plans. Query execution plans can help you understand and troubleshoot query performance issues. To diagnose latency issues by using information from execution plans, see the Spanner documentation on [using metrics to diagnose latency](https://docs.cloud.google.com/spanner/docs/latency-metrics).

To view a Spanner Omni execution plan, use the following command:
    
    
      spanner sql --database DATABASE_ID \
      --execute "EXPLAIN QUERY"
    

Replace the following:

  * `DATABASE_ID`: the database identifier. For example, `MY_DATABASE`.

  * `QUERY`: the query to execute. For example, `SELECT * FROM Songs WHERE SingerId = 1`.




To view a Spanner Omni execution plan that includes runtime statistics, use the following command:
    
    
      spanner sql --database DATABASE_ID \
      --execute "EXPLAIN ANALYZE QUERY"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
