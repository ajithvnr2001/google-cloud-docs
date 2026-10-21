---
url: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/behavior-differences/
title: Behavior differences \u00a0|\u00a0 Firestore with MongoDB compatibility \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:44:26.726866+00:00
---

# Behavior differences  |  Firestore with MongoDB compatibility  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/behavior-differences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore with MongoDB compatibility ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Behavior differences

This page describes behavioral differences between Firestore with MongoDB compatibility and MongoDB.

For a breakdown of supported features depending on MongoDB version, see:

  * [Supported features: 8.0](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/supported-features-80)
  * [Supported features: 7.0](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/supported-features-70)
  * [Supported features: 6.0](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/supported-features-60)
  * [Supported features: 5.0](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/supported-features-50)



## Connections and databases

  * Each connection is limited to a single Firestore with MongoDB compatibility database.
  * A database must be created before connecting to it.



## Naming

The following differences apply to naming parts of your data model.

### Collections

  * Collection names matching `__.*__` are not supported.



### Fields

  * Field names matching `__.*__` are not supported.
  * Empty field names are not supported.



## Documents

  * The maximum document size is 16 MiB.
  * The maximum nesting depth of fields is 20. Each Array and Object-typed field adds one level to the overall depth.
  * In Eventarc events, documents larger than 10 MiB are not included in the event payload.



### `_id` field

  * The top-level `_id` field must be an ObjectId, String, 64-bit integer, 32-bit integer, Double, Binary, or Object. Other BSON types are not supported.



## Values

  * The JavaScript, Symbol, DBPointer, and Undefined BSON types are not supported.



### Date

  * Date values must fall in `[0001-01-01T00:00:00Z, 9999-12-31T23:59:59Z]`.



### Decimal128

  * `NaN`, positive infinity, and negative infinity values are canonicalized on write.
  * Arithmetic operations on Decimal128 are not supported.



### Double

  * `NaN` values are canonicalized on write.



### Regular expression

  * Regular expression options must be valid ("i", "m", "s", "u", or "x") and provided in alphabetical order without repeats.



## Queries

  * Natural sort order (queries without an explicit sort) does not match insertion order or order by `_id` ascending.



## Aggregations

  * Aggregations are limited to 250 stages.
  * The `$merge` and `$out` stages are not supported. See the commands section for a complete list of supported stages and operators.
  * The `$facet` stage does not support `$rand` or `$sample`in the input stages because it's a volatile expression.



## Writes

  * Documents with names beginning with a dollar sign ("$") cannot be created using the upsert feature of `update` or `findAndModify`.
  * Make sure your connection string includes `retryWrites=false` (or use the method appropriate to your driver) to make sure the driver does not attempt to use this feature. Retryable writes are not supported.



## Transactions

  * Snapshot isolation and serializable transactions are supported.

  * By default, transactions use optimistic concurrency controls with snapshot isolation.




## Read concern

  * Firestore with MongoDB compatibility supports the `snapshot` , `majority`, and `linearizable` read concerns. The default is `snapshot` which refers to snapshot isolation.

Use `linearizable` when the application requires strict consistency and must prevent write skew anomalies. For other workloads, `snapshot` can improve performance and reduce transaction contention.




## Write concern

  * Only `w: 'majority'` and `w: 1` write concerns are supported.



## Read preference

  * Only the `primary`, `primaryPreferred`, `primary_preferred`, `secondary_preferred`, and `nearest` read concerns are supported.



## Indexes

  * Wildcard indexes are not supported.
  * Firestore with MongoDB compatibility does not automatically create an index on `_id`, but it ensures values of `_id` are unique within a collection. To achieve similar sorting behavior, you need to explicitly create an ordered index on the `_id` field. However, be mindful of potential hotspot issues, especially if your `_id` values are monotonically increasing or decreasing (e.g., timestamps), as this can impact performance at scale.
  * Indexes without multi-key enabled are not automatically changed to [multi-key indexes](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/index-overview#multi-key_indexes_for_array_values) based on write operations. You must enable multi-key when you create the index and the option cannot be changed.



## Errors

  * Error codes and messages may differ between Firestore with MongoDB compatibility and MongoDB.



## Commands

The following behavior differences apply to specific commands.

  * Commands not listed in the following tables are unsupported.
  * `comment` is accepted by most commands but is ignored.
  * `maxTimeMS` is accepted by most commands but may be ignored.



### Queries

and writes

**Command** | **Unsupported Fields**  
---|---  
`find` | 

  * `max`


  * `min`


  * `returnKey`


  * `showRecordId`


  * `tailable`


  * `oplogReplay`


  * `noCursorTimeout`


  * `awaitData`


  * `allowPartialResults`


  * `collation`


  * `allowDiskUsage`


  * `let`

  
`aggregate` | 

  * `collation`


  * `let`

  
`insert` | (none)  
`update` |  Within an update statement:  
  


  * `collation`

  
`delete` |  Within a delete statement:  
  


  * `collation`

  
`findAndModify` | 

  * `collation`


  * `let`

  
`count` | 

  * `collation`

  
`distinct` | 

  * `collation`

  
`getMore` | 

  * `comment`

  
`killCursors` | (none)  
`explain` | (none)  
  
### Transactions

and sessions

**Command** | **Unsupported Fields**  
---|---  
`commitTransaction` | (none)  
`abortTransaction` | (none)  
`endSessions` | (none)  
  
### Administration

**Command** | **Unsupported Fields** | **Notes**  
---|---|---  
`listDatabases` | 

  * `authorizedDatabases`

| `filter` must be empty if provided.  
`listCollections` | (none) | `authorizedCollections` must be false if provided.  
`listIndexes` | (none) |   
`createIndexes` | (none) |   
`dropIndexes` | (none) |   
`createCollection` | 

  * `timeseries`


  * `expireAfterSeconds`


  * `clusteredIndex`


  * `changeStreamPreAndPostImages`


  * `size`


  * `max`


  * `storageEngine`


  * `validator`


  * `validationLevel`


  * `validationAction`


  * `indexOptionDefaults`


  * `viewOn`


  * `pipeline`


  * `collation`


  * `encryptedFields`

|  This command is a no-op.  
  
`capped` must be false if provided.   
`drop` | (none) |   
  
### Drop collection limitations

**Note:** Drop collection is in **Preview**.

The following limitations apply when you drop a collection:

  * **Index recreation:** You cannot create the same index configuration immediately after a drop. You must wait for the background deletion to finish.
  * **Size limit:** Dropping large collections may result in connection timeouts. Increase the connection deadline if you see timeouts. You can use [bulk delete](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/bulk-delete) as an alternative.
  * **Events:** Drop collection events are not generated for Eventarc when using the `drop` command.



## What's next

  * Run the [Quickstart: Create a database and connect to it](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/create-and-query-database).
  * For a full list of supported features, see [Supported MongoDB data types, drivers, and features](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/supported-data-types-drivers). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
