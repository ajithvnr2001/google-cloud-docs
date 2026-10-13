---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSet/
title: ResultSet \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:22.022327+00:00
---

# ResultSet  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  ResultSet Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Results from `[sessions.read](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#google.spanner.v1.Spanner.Read)` or `[ExecuteSql](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeSql#google.spanner.v1.Spanner.ExecuteSql)`.

JSON representation  
---  
      
    
    {
      "metadata": {
        object ([ResultSetMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetMetadata))
      },
      "rows": [
        array
      ],
      "stats": {
        object ([ResultSetStats](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats))
      },
      "precommitToken": {
        object ([MultiplexedSessionPrecommitToken](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/MultiplexedSessionPrecommitToken))
      }
    }  
  
Fields  
---  
`metadata` |  `object (`[ResultSetMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetMetadata)`)` Metadata about the result set, such as row type information.  
`rows[]` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` Each element in `rows` is a row whose format is defined by `[metadata.row_type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetMetadata#FIELDS.row_type)`. The ith element in each row matches the ith field in `[metadata.row_type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetMetadata#FIELDS.row_type)`. Elements are encoded based on type as described `[here](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#TypeCode)`.  
`stats` |  `object (`[ResultSetStats](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats)`)` Query plan and execution statistics for the SQL statement that produced this result set. These can be requested by setting `[ExecuteSqlRequest.query_mode](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeSql#body.request_body.FIELDS.query_mode)`. DML statements always produce stats containing the number of rows modified, unless executed using the `[ExecuteSqlRequest.QueryMode.PLAN](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/QueryMode#ENUM_VALUES.PLAN)` `[ExecuteSqlRequest.query_mode](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeSql#body.request_body.FIELDS.query_mode)`. Other fields might or might not be populated, based on the `[ExecuteSqlRequest.query_mode](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeSql#body.request_body.FIELDS.query_mode)`.  
`precommitToken` |  `object (`[MultiplexedSessionPrecommitToken](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/MultiplexedSessionPrecommitToken)`)` Optional. A precommit token is included if the read-write transaction is on a multiplexed session. Pass the precommit token with the highest sequence number from this transaction attempt to the `[Commit](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/commit#google.spanner.v1.Spanner.Commit)` request for this transaction.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
