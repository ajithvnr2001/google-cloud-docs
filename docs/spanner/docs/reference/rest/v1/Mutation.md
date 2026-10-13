---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation/
title: Mutation \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:19.424138+00:00
---

# Mutation  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Mutation Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Write
    * JSON representation
  * Delete
    * JSON representation



A modification to one or more Cloud Spanner rows. Mutations can be applied to a Cloud Spanner database by sending them in a `[Commit](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/commit#google.spanner.v1.Spanner.Commit)` call.

JSON representation  
---  
      
    
    {
    
      // Union field operation can be only one of the following:
      "insert": {
        object ([Write](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#Write))
      },
      "update": {
        object ([Write](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#Write))
      },
      "insertOrUpdate": {
        object ([Write](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#Write))
      },
      "replace": {
        object ([Write](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#Write))
      },
      "delete": {
        object ([Delete](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#Delete))
      }
      // End of list of possible types for union field operation.
    }  
  
Fields  
---  
Union field `operation`. Required. The operation to perform. `operation` can be only one of the following:  
`insert` |  `object (`[Write](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#Write)`)` Insert new rows in a table. If any of the rows already exist, the write or transaction fails with error `ALREADY_EXISTS`.  
`update` |  `object (`[Write](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#Write)`)` Update existing rows in a table. If any of the rows does not already exist, the transaction fails with error `NOT_FOUND`.  
`insertOrUpdate` |  `object (`[Write](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#Write)`)` Like `[insert](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#FIELDS.insert)`, except that if the row already exists, then its column values are overwritten with the ones provided. Any column values not explicitly written are preserved.When using `[insertOrUpdate](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#FIELDS.insert_or_update)`, just as when using `[insert](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#FIELDS.insert)`, all `NOT NULL` columns in the table must be given a value. This holds true even when the row already exists and will therefore actually be updated.  
`replace` |  `object (`[Write](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#Write)`)` Like `[insert](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#FIELDS.insert)`, except that if the row already exists, it is deleted, and the column values provided are inserted instead. Unlike `[insertOrUpdate](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#FIELDS.insert_or_update)`, this means any values not explicitly written become `NULL`.In an interleaved table, if you create the child table with the `ON DELETE CASCADE` annotation, then replacing a parent row also deletes the child rows. Otherwise, you must delete the child rows before you replace the parent row.  
`delete` |  `object (`[Delete](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#Delete)`)` Delete rows from a table. Succeeds whether or not the named rows were present.  
  
## Write

Arguments to `[insert](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#FIELDS.insert)`, `[update](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#FIELDS.update)`, `[insertOrUpdate](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#FIELDS.insert_or_update)`, and `[replace](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#FIELDS.replace)` operations.

JSON representation  
---  
      
    
    {
      "table": string,
      "columns": [
        string
      ],
      "values": [
        array
      ]
    }  
  
Fields  
---  
`table` |  `string` Required. The table whose rows will be written.  
`columns[]` |  `string` The names of the columns in `[table](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#Write.FIELDS.table)` to be written.The list of columns must contain enough columns to allow Cloud Spanner to derive values for all primary key columns in the row(s) to be modified.  
`values[]` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` The values to be written. `values` can contain more than one list of values. If it does, then multiple rows are written, one for each entry in `values`. Each list in `values` must have exactly as many entries as there are entries in `[columns](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#Write.FIELDS.columns)` above. Sending multiple lists is equivalent to sending multiple `Mutation`s, each containing one `values` entry and repeating `[table](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#Write.FIELDS.table)` and `[columns](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#Write.FIELDS.columns)`. Individual values in each list are encoded as described `[here](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#TypeCode)`.  
  
## Delete

Arguments to `[delete](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#FIELDS.delete)` operations.

JSON representation  
---  
      
    
    {
      "table": string,
      "keySet": {
        object ([KeySet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/KeySet))
      }
    }  
  
Fields  
---  
`table` |  `string` Required. The table whose rows will be deleted.  
`keySet` |  `object (`[KeySet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/KeySet)`)` Required. The primary keys of the rows within `[table](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation#Delete.FIELDS.table)` to delete. The primary keys must be specified in the order in which they appear in the `PRIMARY KEY()` clause of the table's equivalent DDL statement (the DDL statement used to create the table). Delete is idempotent. The transaction will succeed even if some or all rows do not exist.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-30 UTC."],[],[]] 
