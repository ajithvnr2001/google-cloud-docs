---
url: https://docs.cloud.google.com/spanner/docs/reference/standard-sql/stored-procedures/
title: Stored system procedures for GoogleSQL \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:31.504402+00:00
---

# Stored system procedures for GoogleSQL  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/standard-sql/stored-procedures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Stored system procedures for GoogleSQL Stay organized with collections  Save and categorize content based on your preferences. 

This section describes stored system procedures for Spanner.

A stored system procedure contains SQL code that you can reuse. Spanner provides stored system procedures for you to use. You can't create your own stored procedure in Spanner. You can only execute one stored procedure at a time in a `CALL` statement.

## Stored system procedures

To execute a stored system procedure, you use the [`CALL`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/procedural-language#call) statement:
    
    
    CALL procedure_name(parameters);

Replace procedure_name with the name of the stored system procedure.

Spanner supports the following stored system procedures:

  * Query cancellation
  * Major compaction



### Query cancellation

This section describes the query cancellation stored system procedure.

#### Syntax

Cancels a query with the specified **_query_id_**.
    
    
    CALL cancel_query(query_id)
    

#### Description

This stored system procedure has the following parameters:

Parameter | Type | Description  
---|---|---  
`query_id` | `STRING` | Specifies the ID for the query that you want to cancel.  
  
Query cancellations might fail in the following circumstances:

  * When Spanner servers are busy due to heavy query loads.
  * When the query is in the [process of restarting](https://docs.cloud.google.com/spanner/docs/introspection/oldest-active-queries#limitations) due to an error.



In both cases, you can run the query cancellation stored system procedure again.

### Major Compaction

This section describes the major compaction stored system procedure.

#### Syntax
    
    
    CALL compact_all()
    

#### Description

The `compact_all` stored procedure initiates a major compaction long-running operation to compact all of the data in the database. The procedure returns an identifier that can be used to query the status of the compaction. See [Manual Data Compaction](https://docs.cloud.google.com/spanner/docs/manual-data-compaction) for more details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
