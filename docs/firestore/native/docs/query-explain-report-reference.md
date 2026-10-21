---
url: https://docs.cloud.google.com/firestore/native/docs/query-explain-report-reference/
title: Query Explain report reference \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:58.174737+00:00
---

# Query Explain report reference  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/query-explain-report-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Query Explain report reference

The following values are returned as results to operations performed with [Firestore Query Explain](https://docs.cloud.google.com/firestore/native/docs/query-explain).

**Note:** Query Explain is designed for useful ad hoc analysis; its report format will evolve to maximize ease of reading and understanding, not suitability for machine processing. Some metrics are expected to change as Firestore in Native Mode evolves (i.e., metrics may be added, removed, or updated) and are not covered by the same deprecation policy as other Firestore in Native Mode APIs. The following tables indicate which portions of the data are subject to change.

## Plan records

Key | Type | Field subject to change? | Description | indexes_used  | List of [Generic Structs](https://protobuf.dev/reference/protobuf/google.protobuf/#struct) | Yes, the contents in the Struct response are subject to change.  | List of indexes selected for this query. See below.   
---|---|---|---  
  
### Indexes used

The contents of indexes used are subject to change as Firestore in Native Mode evolves.

Key | Type | Description | query_scope  | String  | The scope at which a query is run. For example: `Collection`, `Collection Group` and `Includes Ancestors`.   
---|---|---  
properties  | String  | The index fields in a format. For example: `(age ASC, __name__ ASC)`.   
  
## Execution statistics

Aggregated execution statistics for the query.

Key  | Type  | Field subject to change?  | Description   
---|---|---|---  
results_returned  | long  | No  | Total number of results returned, including documents, projections, aggregation results, keys.   
execution_duration  | [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) | No  | Total time to execute the query in the backend.   
read_operations  | long  | No  | Total billable read operations.   
debug_stats  | [Generic Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct) | Yes, the contents in the Struct response are subject to change.  | Debugging statistics from the execution of the query. See below.   
  
### Debug statistics

The following results are helpful for debugging use cases and analysis of raw, optional statistics.

The contents of debug statistics are subject to change as Firestore in Native Mode evolves.

Key  | Type  | Description   
---|---|---  
index_entries_scanned  | String  | Total number of index entries inspected during the query.   
documents_scanned  | String  | Total number of documents scanned during the query.   
billing_details  | [Generic Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct) | Billing details including metrics like: "documents_billable", "index_entries_billable", "knn_vector_index_entries_billable", "min_query_cost".   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
