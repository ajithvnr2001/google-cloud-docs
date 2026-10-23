---
url: https://docs.cloud.google.com/spanner/docs/fgac-sequences/
title: Fine-grained access control for sequences \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:31.982007+00:00
---

# Fine-grained access control for sequences  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/fgac-sequences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Fine-grained access control for sequences Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how [fine-grained access control](https://docs.cloud.google.com/spanner/docs/fgac-about) works with Spanner sequences for GoogleSQL-dialect databases and PostgreSQL-dialect databases.

For fine-grained access control users, you can grant either one or both of the following privileges to allow access to read sequence information or generate values from the sequence.

  * Grant `SELECT` on the sequence to allow read access to the parameters and current state of the sequence.

###  GoogleSQL 
        
        GRANT SELECT ON SEQUENCE SEQUENCE_NAME TO ROLE ROLE_NAME;

###  PostgreSQL 
        
        GRANT SELECT ON SEQUENCE SEQUENCE_NAME TO ROLE_NAME;

  * Grant `UPDATE` on the sequence to allow calls to the sequence value generator.

###  GoogleSQL 
        
        GRANT UPDATE ON SEQUENCE SEQUENCE_NAME TO ROLE ROLE_NAME;

###  PostgreSQL 
        
        GRANT UPDATE ON SEQUENCE SEQUENCE_NAME TO ROLE_NAME;




## Required privileges for sequence operations

The following table contains details about which privileges you require when performing a specific sequence operations.

**Operation** | **Privilege requirements**  
---|---  
GoogleSQL: `GET_NEXT_SEQUENCE_VALUE()` PostgreSQL: `nextval()` | Requires an `UPDATE` or `SELECT` privilege on the sequence. Note that if you execute this function through generated columns or default values, you also need to have an `INSERT` or `UPDATE` privilege on the column. An `UPDATE` privilege on a sequence doesn't automatically grant any privilege on the columns where you want to use the sequence.   
GoogleSQL: `GET_INTERNAL_SEQUENCE_STATE()` PostgreSQL: `spanner.get_internal_sequence_state()` | Requires the `SELECT` privilege on the sequence that you request.   
GoogleSQL: `INFORMATION_SCHEMA.SEQUENCES`  
`INFORMATION_SCHEMA.SEQUENCE_OPTIONS` PostgreSQL `INFORMATION_SCHEMA.SEQUENCES` | You can have the `SELECT` or `UPDATE` privilege on the sequence you want to query. You can only see the sequences that you have a privilege to view.   
  
## What's next

  * Learn more about using [sequences](https://docs.cloud.google.com/spanner/docs/primary-key-default-value#bit-reversed-sequence) in Spanner.
  * Learn about `SEQUENCE` for [GoogleSQL](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-definition-language#sequence_statements) or [PostgreSQL](https://docs.cloud.google.com/spanner/docs/reference/postgresql/data-definition-language#sequence_statements).
  * Learn about sequence functions in [GoogleSQL](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/sequence_functions) or [PostgreSQL](https://docs.cloud.google.com/spanner/docs/reference/postgresql/functions-and-operators#sequence).
  * Learn about sequences in the `INFORMATION_SCHEMA` in [GoogleSQL](https://docs.cloud.google.com/spanner/docs/information-schema#sequences) or [PostgreSQL](https://docs.cloud.google.com/spanner/docs/information-schema-pg#sequences).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
