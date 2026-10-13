---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions/
title: RequestOptions \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:21.033490+00:00
---

# RequestOptions  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  RequestOptions Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Priority



Common request options for various APIs.

JSON representation  
---  
      
    
    {
      "priority": enum ([Priority](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions#Priority)),
      "requestTag": string,
      "transactionTag": string
    }  
  
Fields  
---  
`priority` |  `enum (`[Priority](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions#Priority)`)` Priority for the request.  
`requestTag` |  `string` A per-request tag which can be applied to queries or reads, used for statistics collection. Both `requestTag` and `transactionTag` can be specified for a read or query that belongs to a transaction. This field is ignored for requests where it's not applicable (for example, `CommitRequest`). Legal characters for `requestTag` values are all printable characters (ASCII 32 - 126) and the length of a requestTag is limited to 50 characters. Values that exceed this limit are truncated. Any leading underscore (_) characters are removed from the string.  
`transactionTag` |  `string` A tag used for statistics collection about this transaction. Both `requestTag` and `transactionTag` can be specified for a read or query that belongs to a transaction. To enable tagging on a transaction, `transactionTag` must be set to the same value for all requests belonging to the same transaction, including `[sessions.beginTransaction](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/beginTransaction#google.spanner.v1.Spanner.BeginTransaction)`. If this request doesn't belong to any transaction, `transactionTag` is ignored. Legal characters for `transactionTag` values are all printable characters (ASCII 32 - 126) and the length of a `transactionTag` is limited to 50 characters. Values that exceed this limit are truncated. Any leading underscore (_) characters are removed from the string.  
  
## Priority

The relative priority for requests. Note that priority isn't applicable for `[sessions.beginTransaction](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/beginTransaction#google.spanner.v1.Spanner.BeginTransaction)`.

The priority acts as a hint to the Cloud Spanner scheduler and doesn't guarantee priority or order of execution. For example:

  * Some parts of a write operation always execute at `PRIORITY_HIGH`, regardless of the specified priority. This can cause you to see an increase in high priority workload even when executing a low priority request. This can also potentially cause a priority inversion where a lower priority request is fulfilled ahead of a higher priority request.
  * If a transaction contains multiple operations with different priorities, Cloud Spanner doesn't guarantee to process the higher priority operations first. There might be other constraints to satisfy, such as the order of operations.

Enums  
---  
`PRIORITY_UNSPECIFIED` | `PRIORITY_UNSPECIFIED` is equivalent to `PRIORITY_HIGH`.  
`PRIORITY_LOW` | This specifies that the request is low priority.  
`PRIORITY_MEDIUM` | This specifies that the request is medium priority.  
`PRIORITY_HIGH` | This specifies that the request is high priority.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-06 UTC."],[],[]] 
