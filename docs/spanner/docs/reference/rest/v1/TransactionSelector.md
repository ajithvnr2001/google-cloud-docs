---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionSelector/
title: TransactionSelector \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:22.783445+00:00
---

# TransactionSelector  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionSelector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  TransactionSelector Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



This message is used to select the transaction in which a `[sessions.read](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#google.spanner.v1.Spanner.Read)` or `[ExecuteSql](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeSql#google.spanner.v1.Spanner.ExecuteSql)` call runs.

See `[TransactionOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions)` for more information about transactions.

JSON representation  
---  
      
    
    {
    
      // Union field selector can be only one of the following:
      "singleUse": {
        object ([TransactionOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions))
      },
      "id": string,
      "begin": {
        object ([TransactionOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions))
      }
      // End of list of possible types for union field selector.
    }  
  
Fields  
---  
Union field `selector`. If no fields are set, the default is a single use transaction with strong concurrency. `selector` can be only one of the following:  
`singleUse` |  `object (`[TransactionOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions)`)` Execute the read or SQL query in a temporary transaction. This is the most efficient way to execute a transaction that consists of a single SQL query.  
`id` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Execute the read or SQL query in a previously-started transaction.A base64-encoded string.  
`begin` |  `object (`[TransactionOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions)`)` Begin a new transaction and execute this read or SQL query in it. The transaction ID of the new transaction is returned in `[ResultSetMetadata.transaction](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetMetadata#FIELDS.transaction)`, which is a `[Transaction](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Transaction)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
