---
url: https://docs.cloud.google.com/spanner/docs/reference/standard-sql/sequence_functions/
title: Sequence functions in GoogleSQL \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:07.306771+00:00
---

# Sequence functions in GoogleSQL  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/standard-sql/sequence_functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Sequence functions in GoogleSQL Stay organized with collections  Save and categorize content based on your preferences. 

GoogleSQL for Spanner supports the following sequence functions.

## Function list

Name | Summary  
---|---  
[`GET_INTERNAL_SEQUENCE_STATE`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/sequence_functions#get_internal_sequence_state) | Gets the current sequence internal counter before bit reversal.   
[`GET_NEXT_SEQUENCE_VALUE`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/sequence_functions#get_next_sequence_value) | Takes in a sequence identifier and returns the next value. This function is only allowed in read-write transactions.  
  
## `GET_INTERNAL_SEQUENCE_STATE`
    
    
    GET_INTERNAL_SEQUENCE_STATE(SEQUENCE sequence_identifier)
    

**Description**

Gets the current sequence internal counter before bit reversal. This function is useful for import or export, and migrations. If `GET_NEXT_SEQUENCE_VALUE` is never called on the sequence, then this function returns `NULL`.

**Arguments**

  * `sequence_identifier`: The ID for the sequence.



**Return Data Type**

`INT64`

**Example**
    
    
    SELECT GET_NEXT_SEQUENCE_VALUE(SEQUENCE MySequence) AS next_value;
    
    /*---------------------+
     | next_value          |
     +---------------------+
     | 5980780305148018688 |
     +---------------------*/
    
    
    
    SELECT GET_INTERNAL_SEQUENCE_STATE(SEQUENCE MySequence) AS sequence_state;
    
    /*----------------+
     | sequence_state |
     +----------------+
     | 399            |
     +----------------*/
    

## `GET_NEXT_SEQUENCE_VALUE`
    
    
    GET_NEXT_SEQUENCE_VALUE(SEQUENCE sequence_identifier)
    

**Description**

Gets the next integer in a sequence.

**Arguments**

  * `sequence_identifier`: The ID for the sequence.



**Return Data Type**

`INT64`

**Example**

Create a table where its key column uses the sequence as a default value.
    
    
    CREATE TABLE Singers (
      SingerId INT64 DEFAULT (GET_NEXT_SEQUENCE_VALUE(SEQUENCE MySequence)),
      a STRING(MAX),
    ) PRIMARY KEY (SingerId);
    

Obtain a sequence value in a read-write transaction and use it in an INSERT statement.
    
    
    SELECT GET_NEXT_SEQUENCE_VALUE(SEQUENCE MySequence) as next_id;
    INSERT INTO Singers(SingerId, a) VALUES (next_id, 1);
    

Use the sequence functions independently in the GoogleSQL DML.
    
    
    INSERT INTO Singers (SingerId) VALUES (GET_NEXT_SEQUENCE_VALUE(SEQUENCE MySequence);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
