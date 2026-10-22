---
url: https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/
title: Query Explain report reference \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:11.755644+00:00
---

# Query Explain report reference  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Guides ](https://docs.cloud.google.com/datastore/docs/concepts/overview)



Send feedback 

#  Query Explain report reference Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The following values are returned as results to operations performed with [Query Explain](https://docs.cloud.google.com/datastore/docs/query-explain-analyze).

**Note:** The Query Explain is designed for useful ad hoc analysis; its report format will evolve to maximize ease of reading and understanding, not suitability for machine processing. The returned metrics are expected to change as Datastore mode evolves (metrics may be added, removed, or updated) and are not covered by the same deprecation policy as other Firestore APIs. See the tables below for more information about stability

## Plan records

Key | Type | Subject to change? | Description | indexes_used  | List of [Generic Structs](https://protobuf.dev/reference/protobuf/google.protobuf/#struct) | Yes, the contents in the Struct response are subject to change.  | List of indexes selected for this query. See below.   
---|---|---|---  
  
### Indexes used

The contents of indexes used are subject to change as Datastore mode evolves.

Key | Type | Description | query_scope  | String  | The scope at which a query is run. For example `Collection`, `Collection Group` and `Includes Ancestors`.   
---|---|---  
properties  | String  | The index fields in a format, for example `(age ASC, __name__ ASC)`.   
  
## Execution statistics

Aggregated execution statistics for the query.

Key  | Type  | Field subject to change?  | Description   
---|---|---|---  
results_returned  | long  | No  | Total number of results returned, including entities, projections, aggregation results, keys.   
execution_duration  | Duration  | No  | Total time to execute the query in the backend.   
read_operations  | long  | No  | Total billable read operations.   
debug_stats  | Generic Struct  | Yes, the contents in the Struct response are subject to change.  | Debugging statistics from the execution of the query. See below.   
  
### Debug statistics

The following results are helpful for debugging use cases and analysis of raw, optional statistics.

The contents of debug stats are subject to change as Datastore mode evolves.

Key  | Type  | Description   
---|---|---  
index_entries_scanned  | String  | Total number of index entries inspected during the query.   
documents_scanned  | String  | Total number of documents scanned during the query.   
billing_details  | Generic Struct  | Billing details including metrics like: "documents_billable", "index_entries_billable", "min_query_cost".   
  
## What's next

  * [Learn more about running queries with explain and analyze](https://docs.cloud.google.com/datastore/docs/query-explain-analyze)
  * [Learn more about optimizing queries and indexes](https://docs.cloud.google.com/datastore/docs/concepts/optimize-indexes)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
