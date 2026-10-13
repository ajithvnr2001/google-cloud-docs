---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions/
title: TransactionOptions \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:22.447873+00:00
---

# TransactionOptions  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  TransactionOptions Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ReadWrite
    * JSON representation
  * ReadLockMode
  * PartitionedDml
  * ReadOnly
    * JSON representation
  * IsolationLevel



Options to use for transactions.

JSON representation  
---  
      
    
    {
      "excludeTxnFromChangeStreams": boolean,
      "isolationLevel": enum ([IsolationLevel](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions#IsolationLevel)),
    
      // Union field mode can be only one of the following:
      "readWrite": {
        object ([ReadWrite](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions#ReadWrite))
      },
      "partitionedDml": {
        object ([PartitionedDml](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions#PartitionedDml))
      },
      "readOnly": {
        object ([ReadOnly](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions#ReadOnly))
      }
      // End of list of possible types for union field mode.
    }  
  
Fields  
---  
`excludeTxnFromChangeStreams` |  `boolean` When `excludeTxnFromChangeStreams` is set to `true`, it prevents read or write transactions from being tracked in change streams.

  * If the DDL option `allow_txn_exclusion` is set to `true`, then the updates made within this transaction aren't recorded in the change stream.
  * If you don't set the DDL option `allow_txn_exclusion` or if it's set to `false`, then the updates made within this transaction are recorded in the change stream.

When `excludeTxnFromChangeStreams` is set to `false` or not set, modifications from this transaction are recorded in all change streams that are tracking columns modified by these transactions.The `excludeTxnFromChangeStreams` option can only be specified for read-write or partitioned DML transactions, otherwise the API returns an `INVALID_ARGUMENT` error.  
`isolationLevel` |  `enum (`[IsolationLevel](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions#IsolationLevel)`)` Isolation level for the transaction.  
Union field `mode`. Required. The type of transaction. `mode` can be only one of the following:  
`readWrite` |  `object (`[ReadWrite](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions#ReadWrite)`)` Transaction may write.Authorization to begin a read-write transaction requires `spanner.databases.beginOrRollbackReadWriteTransaction` permission on the `session` resource.  
`partitionedDml` |  `object (`[PartitionedDml](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions#PartitionedDml)`)` Partitioned DML transaction.Authorization to begin a Partitioned DML transaction requires `spanner.databases.beginPartitionedDmlTransaction` permission on the `session` resource.  
`readOnly` |  `object (`[ReadOnly](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions#ReadOnly)`)` Transaction does not write.Authorization to begin a read-only transaction requires `spanner.databases.beginReadOnlyTransaction` permission on the `session` resource.  
  
## ReadWrite

Message type to initiate a read-write transaction. Currently this transaction type has no options.

JSON representation  
---  
      
    
    {
      "readLockMode": enum ([ReadLockMode](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions#ReadLockMode)),
      "multiplexedSessionPreviousTransactionId": string
    }  
  
Fields  
---  
`readLockMode` |  `enum (`[ReadLockMode](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions#ReadLockMode)`)` The read lock mode for the transaction.  
`multiplexedSessionPreviousTransactionId` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. Clients should pass the transaction ID of the previous transaction attempt that was aborted if this transaction is being executed on a multiplexed session.A base64-encoded string.  
  
## ReadLockMode

`ReadLockMode` is used to set the read lock mode for read-write transactions.

Enums  
---  
`READ_LOCK_MODE_UNSPECIFIED` | Default value.

  * If isolation level is `[SERIALIZABLE](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions#IsolationLevel.ENUM_VALUES.SERIALIZABLE)`, locking semantics default to `PESSIMISTIC`.
  * If isolation level is `[REPEATABLE_READ](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions#IsolationLevel.ENUM_VALUES.REPEATABLE_READ)`, locking semantics default to `OPTIMISTIC`.
  * See [Concurrency control](https://cloud.google.com/spanner/docs/concurrency-control) for more details.

  
`PESSIMISTIC` | Pessimistic lock mode.Lock acquisition behavior depends on the isolation level in use. In `[SERIALIZABLE](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions#IsolationLevel.ENUM_VALUES.SERIALIZABLE)` isolation, reads and writes acquire necessary locks during transaction statement execution. In `[REPEATABLE_READ](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions#IsolationLevel.ENUM_VALUES.REPEATABLE_READ)` isolation, reads that explicitly request to be locked and writes acquire locks. See [Concurrency control](https://cloud.google.com/spanner/docs/concurrency-control) for details on the types of locks acquired at each transaction step.  
`OPTIMISTIC` | Optimistic lock mode.Lock acquisition behavior depends on the isolation level in use. In both `[SERIALIZABLE](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions#IsolationLevel.ENUM_VALUES.SERIALIZABLE)` and `[REPEATABLE_READ](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions#IsolationLevel.ENUM_VALUES.REPEATABLE_READ)` isolation, reads and writes do not acquire locks during transaction statement execution. See [Concurrency control](https://cloud.google.com/spanner/docs/concurrency-control) for details on how the guarantees of each isolation level are provided at commit time.  
  
## PartitionedDml

This type has no fields.

Message type to initiate a Partitioned DML transaction.

## ReadOnly

Message type to initiate a read-only transaction.

JSON representation  
---  
      
    
    {
      "returnReadTimestamp": boolean,
    
      // Union field timestamp_bound can be only one of the following:
      "strong": boolean,
      "minReadTimestamp": string,
      "maxStaleness": string,
      "readTimestamp": string,
      "exactStaleness": string
      // End of list of possible types for union field timestamp_bound.
    }  
  
Fields  
---  
`returnReadTimestamp` |  `boolean` If true, the Cloud Spanner-selected read timestamp is included in the `[Transaction](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Transaction)` message that describes the transaction.  
Union field `timestamp_bound`. How to choose the timestamp for the read-only transaction. `timestamp_bound` can be only one of the following:  
`strong` |  `boolean` sessions.read at a timestamp where all previously committed transactions are visible.  
`minReadTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Executes all reads at a timestamp >= `minReadTimestamp`.This is useful for requesting fresher data than some previous read, or data that is fresh enough to observe the effects of some previously committed transaction whose timestamp is known.Note that this option can only be used in single-use transactions.A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: `"2014-10-02T15:01:23.045123456Z"`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`maxStaleness` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` sessions.read data at a timestamp >= `NOW - maxStaleness` seconds. Guarantees that all writes that have committed more than the specified number of seconds ago are visible. Because Cloud Spanner chooses the exact timestamp, this mode works even if the client's local clock is substantially skewed from Cloud Spanner commit timestamps.Useful for reading the freshest data available at a nearby replica, while bounding the possible staleness if the local replica has fallen behind.Note that this option can only be used in single-use transactions.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`readTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Executes all reads at the given timestamp. Unlike other modes, reads at a specific timestamp are repeatable; the same read at the same timestamp always returns the same data. If the timestamp is in the future, the read is blocked until the specified timestamp, modulo the read's deadline.Useful for large scale consistent reads such as mapreduces, or for coordinating many reads against a consistent snapshot of the data.A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: `"2014-10-02T15:01:23.045123456Z"`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`exactStaleness` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Executes all reads at a timestamp that is `exactStaleness` old. The timestamp is chosen soon after the read is started.Guarantees that all writes that have committed more than the specified number of seconds ago are visible. Because Cloud Spanner chooses the exact timestamp, this mode works even if the client's local clock is substantially skewed from Cloud Spanner commit timestamps.Useful for reading at nearby replicas without the distributed timestamp negotiation overhead of `maxStaleness`.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## IsolationLevel

`IsolationLevel` is used when setting the [isolation level](https://cloud.google.com/spanner/docs/isolation-levels) for a transaction.

Enums  
---  
`ISOLATION_LEVEL_UNSPECIFIED` | Default value.If the value is not specified, the `SERIALIZABLE` isolation level is used.  
`SERIALIZABLE` | All transactions appear as if they executed in a serial order, even if some of the reads, writes, and other operations of distinct transactions actually occurred in parallel. Spanner assigns commit timestamps that reflect the order of committed transactions to implement this property. Spanner offers a stronger guarantee than serializability called external consistency. For more information, see [TrueTime and external consistency](https://cloud.google.com/spanner/docs/true-time-external-consistency#serializability).  
`REPEATABLE_READ` | All reads performed during the transaction observe a consistent snapshot of the database, and the transaction is only successfully committed in the absence of conflicts between its updates and any concurrent updates that have occurred since that snapshot. Consequently, in contrast to `SERIALIZABLE` transactions, only write-write conflicts are detected in snapshot transactions.This isolation level does not support read-only and partitioned DML transactions.When `REPEATABLE_READ` is specified on a read-write transaction, the locking semantics default to `OPTIMISTIC`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-06 UTC."],[],[]] 
