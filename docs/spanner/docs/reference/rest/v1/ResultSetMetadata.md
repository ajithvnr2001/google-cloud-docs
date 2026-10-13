---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetMetadata/
title: ResultSetMetadata \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:21.644557+00:00
---

# ResultSetMetadata  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  ResultSetMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Metadata about a `[ResultSet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSet)` or `[PartialResultSet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/PartialResultSet)`.

JSON representation  
---  
      
    
    {
      "rowType": {
        object ([StructType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/StructType))
      },
      "transaction": {
        object ([Transaction](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Transaction))
      },
      "undeclaredParameters": {
        object ([StructType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/StructType))
      }
    }  
  
Fields  
---  
`rowType` |  `object (`[StructType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/StructType)`)` Indicates the field names and types for the rows in the result set. For example, a SQL query like `"SELECT UserId, UserName FROM Users"` could return a `rowType` value like:
    
    
    "fields": [
      { "name": "UserId", "type": { "code": "INT64" } },
      { "name": "UserName", "type": { "code": "STRING" } },
    ]
      
  
`transaction` |  `object (`[Transaction](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Transaction)`)` If the read or SQL query began a transaction as a side-effect, the information about the new transaction is yielded here.  
`undeclaredParameters` |  `object (`[StructType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/StructType)`)` A SQL query can be parameterized. In PLAN mode, these parameters can be undeclared. This indicates the field names and types for those undeclared parameters in the SQL query. For example, a SQL query like `"SELECT * FROM Users where UserId = @userId and UserName = @userName "` could return a `undeclaredParameters` value like:
    
    
    "fields": [
      { "name": "UserId", "type": { "code": "INT64" } },
      { "name": "UserName", "type": { "code": "STRING" } },
    ]
      
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
