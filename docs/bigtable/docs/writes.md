---
url: https://docs.cloud.google.com/bigtable/docs/writes/
title: Writes \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:54.925064+00:00
---

# Writes  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/writes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Writes

This page lists the types of write requests you can send to Bigtable and describes when you should use them and when you shouldn't. For information on aggregating data in a cell at write time, see [Aggregate values at write time](https://docs.cloud.google.com/bigtable/docs/aggregates).

The Bigtable Data API and client libraries allow you to programmatically write data to your tables. Bigtable sends back a response or acknowledgement for each write.

Each client library offers the ability to send the following types of write requests:

  * Simple writes
  * Increments and appends
  * Conditional writes
  * Batch writes



Bigtable client libraries have a built-in **smart retries** feature for simple and batch writes, which means that they seamlessly handle temporary unavailability. For example, If your application attempts to write data and encounters a temporary outage or network issue, it automatically retries until the write is committed or the request deadline is reached. This resilience works with both single-cluster and replicated instances, with single-cluster routing or multi-cluster routing.

For batch and streaming write operations, you can use the Bigtable Beam connector. For more information, see Batch writes.

To learn about limits that apply to write requests, see [Quotas and limits](https://docs.cloud.google.com/bigtable/quotas).

For Cloud Bigtable client library examples of the write requests described on this page, see [Write examples](https://docs.cloud.google.com/bigtable/docs/writing-data).

## Types of writes and when to use them

**Note:** For simplicity, write request types are identified here by their API names. The names are different in each client library.

All write requests include the following basic components:

  * The name of the table to write to.
  * An [app profile](https://docs.cloud.google.com/bigtable/docs/app-profiles) ID, which tells Bigtable how to route the traffic.
  * One or more mutations. A **mutation** consists of the following elements: 
    * Column family name
    * Column qualifier
    * Timestamp
    * Value that you are writing to the table



The timestamp of a mutation has a default value of the current date and time, measured as the time that has elapsed since the Unix epoch, 00:00:00 UTC on January 1, 1970.

A timestamp that you send to Bigtable must be a microsecond value with at most millisecond precision. A timestamp with microsecond precision, such as `3023483279876543`, is rejected. In this example, the acceptable timestamp value is `3023483279876000`. 

All mutations in a single write request have the same timestamp unless you override them. You can set the timestamp of all mutations in a write request to be the same or different from each other.

### Simple writes

You can write a single row to Bigtable with a `MutateRow` request that includes the table name, the ID of the app profile that should be used, a row key, and up to 100,000 mutations for that row. A single-row write is atomic. Use this type of write when you are making multiple mutations to a single row.

For code samples that demonstrate how to send simple write requests, see [Performing a simple write](https://docs.cloud.google.com/bigtable/docs/writing-data#simple).

#### When not to use simple writes

Simple writes are not the best way to write data for the following use cases:

  * You are writing a batch of data that will have **contiguous row keys**. In this case, you should use batch writes instead of consecutive simple writes, because a contiguous batch can be applied in a single backend call.

  * You want **high throughput** (rows per second or bytes per second) and don't require low latency. Batch writes will be faster in this case.




### Incremental updates

Bigtable lets you create cells with a data type of _aggregate_. Aggregate cells are optimized for when you want to change the values in existing table cells, aggregating cell values as the data is written. The following types of aggregation are available:

  * **Sum** \- Increment a counter or keep a running sum.
  * **Minimum** \- Send an integer to a cell, and Bigtable keeps the lower of the two values.
  * **Maximum** \- Send an integer to a cell, and Bigtable keeps the higher of the two values.
  * **HyperLogLog (HLL)** \- Send a value that is added to a probabilistic set of all values added to the cell.



Requests to update aggregate cells are sent with a `MutateRow` request and a mutation type of either `AddToCell` or `MergeToCell` or one of the deletion mutation types.

### Appends

To append data to an existing value, you can use a `ReadModifyWriteRow` request. This request includes the table name, the ID of the app profile that should be used, a row key, and a set of rules to use when writing the data. Each rule includes the column family name, column qualifier, and either an append value or an increment amount.

Rules are applied in order. For example, if your request includes a request to append the value for a column that contains the value `some` with the string `thing`, and a later rule in the same request appends that same column with `body`, the value is modified twice in a single atomic write, and the resulting value is `somethingbody`. The later rule does not overwrite the earlier rule.

You can also increment an integer with a `ReadModifyWriteRow` call, but we recommend that you use aggregate cells and `AddToCell` or `MergeToCell` instead. A value can be incremented using `ReadModifyWrite` only if it is encoded as a 64-bit big-endian signed integer. Bigtable treats an increment to a value that is empty or does not exist as if the value is zero.

`ReadModifyWriteRow` requests are atomic. They are not retried if they fail for any reason.

#### When not to use `ReadModifyWriteRow`

Don't send `ReadModifyWriteRow` requests in the following situations:

  * Your use case can be handled by sending a `MutateRow` request with an `AddToCell` mutation. For more information, see Aggregating values at write time.

  * You are using an app profile that has **multi-cluster routing**.

  * You are using **multiple single-cluster app profiles** and sending writes that could conflict with data written to the same row and column in other clusters in the instance. With single-cluster routing, a write request is sent to a single cluster and then replicated.

  * You rely on the **smart retries** feature provided by the client libraries. A `ReadModifyWriteRow` request can't be tried again.

  * You are writing **large amounts of data** and you need the writes to complete quickly. A request that reads and then modifies a row is slower than a simple write request. As a result, this type of write is often not the best approach at scale.

For example, if you want to **count something** that will number in the millions, such as page views, you should `MutateRow` with an `AddToCell` mutation to update your counts at write time.




### Conditional writes

If you want to check a row for a condition and then, depending on the result, write data to that row, submit a `CheckAndMutateRow` request. This type of request includes a row key and a row filter. A **row filter** is a set of rules that you use to check the value of existing data. Mutations are then committed to specific columns in the row only when certain conditions, checked by the filter, are met. This process of checking and then writing is completed as a single, atomic action.

A filter request must include one or both of the following types of mutations:

  * True mutations, or the mutations to apply if the filter returns a value.
  * False mutations, which are applied if the filter yields nothing.



You can supply up to 100,000 of each type of mutation--true and false--in a single write, and you must send at least one. Bigtable sends a response when all mutations are complete.

Because a conditional write reads the row to evaluate the filter, the caller must have both the `bigtable.tables.readRows` and `bigtable.tables.mutateRows` permissions on the table (or the equivalent `bigtable.authorizedViews.readRows` and `bigtable.authorizedViews.mutateRows` permissions on an authorized view). For more information, see [Access control](https://docs.cloud.google.com/bigtable/docs/access-control#permissions).

For code samples that demonstrate how to send conditional writes, see [Conditionally writing a value](https://docs.cloud.google.com/bigtable/docs/writing-data#conditional).

#### When not to use conditional writes

You cannot use conditional writes for the following use case:

  * You are using an app profile that has [**multi-cluster routing**](https://docs.cloud.google.com/bigtable/docs/app-profiles#routing).

  * You are using **multiple single-cluster app profiles** and sending writes that could conflict with data written to the same row and column in other clusters in the instance. With single-cluster routing, a write request is sent to a single cluster and then replicated.

  * You are writing **large amounts of data** and you need the writes to complete quickly. Similar to `ReadModifyWriteRow`, conditional write requests need to read rows before modifying them, so `CheckAndModifyRow` requests are slower than simple write requests. As a result, this type of write is often not the best approach at scale.




### Batch writes

You can write more than one row with a single call by using a `MutateRows` request. `MutateRows` requests contain a set of up to 100,000 entries that are each applied atomically. Each entry consists of a row key and at least one mutation to be applied to the row. A batch write request can contain up to 100,000 mutations spread across all entries. For example, a batch write could include any of the following permutations:

  * 100,000 entries with 1 mutation in each entry.
  * 1 entry with 100,000 mutations.
  * 1,000 entries with 100 mutations each.



Each entry in a `MutateRows` request is atomic, but the request as a whole is not. If necessary, Bigtable retries any entries in the batch that don't succeed, until all writes are successful or the request deadline is reached. Then it returns a response identifying each write in the batch and whether or not the write succeeded.

For code samples that demonstrate how to send batch writes, see [Performing batch writes](https://docs.cloud.google.com/bigtable/docs/writing-data#batch).

#### When not to use batch writes

  * You are writing bulk data to **rows that are not close to each other**. Bigtable [stores data lexicographically by row key](https://docs.cloud.google.com/bigtable/docs/schema-design), the binary equivalent of alphabetical order. Because of this, when row keys in a request are not similar to each other, Bigtable handles them sequentially, rather than in parallel. The throughput will be high, but latency will also be high. To avoid that high latency, use `MutateRows` when row keys are similar and Bigtable will be writing rows that are near each other. Use `MutateRow`, or simple writes, for rows that are not near each other.

  * You are requesting **multiple mutations to the same row**. In this case, you will see better performance if you perform all the mutations in a single simple write request. This is because in a simple write, all changes are committed in a single atomic action, but a batch write is forced to serialize mutations to the same row, causing latency.




#### Batch write flow control

If you send your batch writes (including deletions) using one of the following, you can enable **batch write flow control** in your code.

  * [Bigtable Beam connector (`BigtableIO`)](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigtable/BigtableIO.html)
  * [Bigtable client library for Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview)
  * [Bigtable HBase Beam connector (`CloudBigtableIO`)](https://docs.cloud.google.com/bigtable/docs/hbase-dataflow-java)
  * [Bigtable HBase client for Java](https://github.com/googleapis/java-bigtable-hbase)



When batch write flow control is enabled for a Dataflow job, Bigtable automatically does the following :

  * Rate-limits traffic to avoid overloading your Bigtable cluster
  * Ensures the cluster is under enough load to trigger Bigtable autoscaling (if enabled), so that more nodes are automatically added to the cluster when needed



These combined actions prevent cluster overload and job failure, and you don't need to manually scale your cluster in anticipation of running the batch write. When flow control is enabled, cluster scaling occurs during the Dataflow job rather than before it, so the job might take longer to finish than if you scale your cluster manually.

You must use an app profile configured for single-cluster routing. Enabling Bigtable autoscaling for the destination cluster is not a requirement, but autoscaling lets you take full advantage of batch write flow control. You can use Dataflow autoscaling just as you would with any other job.

To learn more about Bigtable autoscaling, see [Autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling). To understand app profile routing policies, see [App profiles overview](https://docs.cloud.google.com/bigtable/docs/app-profiles).

For code samples, see [Enable batch write flow control](https://docs.cloud.google.com/bigtable/docs/writing-data#batch-write-flow-control).

## Write data to an authorized view

To write data to an authorized view, you must use one of the following:

  * gcloud CLI
  * Bigtable client for Java



The other Bigtable client libraries don't yet support authorized view access.

When you write data to an authorized view, you supply the authorized view ID in addition to the table ID.

All writes to an authorized view are directly applied to the underlying table.

### Authorized view definition limitations

In an authorized view, the rows or columns that you can write data to are limited by the authorized view definition. In other words, you can only write to rows and columns that meet the same criteria specified for the authorized view.

For example, if the authorized view is defined by the row key prefix `examplepetstore1`, then you can't write data using a row key of `examplepetstore2`; the beginning of the row key value must include the entire string `examplepetstore1`.

Similarly, if the authorized view is defined by the column qualifier prefix `order-phone`, then you can write data using the column qualifier `order-phone123`, but you can't use the column qualifier `order-tablet`.

Your write request also can't reference data that is outside the authorized view, such as when you are checking for a value in a conditional write request.

For any request that writes or references data outside the authorized view, an error message of `PERMISSION_DENIED` is returned.

## Replication

When one cluster of a replicated instance receives a write, that write is immediately replicated to the other clusters in the instance.

### Atomicity

Each `MutateRows` request that you send to a replicated instance is committed as a single atomic action on the cluster that the request is routed to. When the write is replicated to the other clusters in the instance, those clusters also each receive the write as an atomic operation. Clusters don't receive partial mutations; a mutation either succeeds or fails atomically for all of the cells that it modifies.

### Consistency

The time it takes for the data that you write to be available for reads depends on several factors, including the number of clusters in your instance and the type of routing that your app profile uses.

With a single-cluster instance, the data can be read immediately, but if an instance has more than one cluster, meaning it's using replication, Bigtable is [eventually consistent](https://docs.cloud.google.com/bigtable/docs/replication-overview#consistency-model). You can achieve read-your-writes consistency by routing requests to the same cluster.

You can create and use a **consistency token** and call `CheckConsistency` in `StandardReadRemoteWrites` mode after you've sent write requests. The token checks for replication consistency. In general, you create a consistency token either after a batch of writes has been sent or after a certain interval, such as an hour. Then you can hand the token off to be used by another process, such as a module making a read request, which uses the token to check to make sure all the data has been replicated before it attempts to read.

If you use a token right after you create it, it can take up to a few minutes to check for consistency the first time you use it. This delay is because every cluster checks every other cluster to make sure no more data is coming. After the initial use, or if you wait several minutes to use the token for the first time, the token succeeds immediately every time it's used.

## Conflict resolution

Each cell value in a Bigtable table is uniquely identified by the four-tuple (row key, column family, column qualifier, timestamp). See [Bigtable storage model](https://docs.cloud.google.com/bigtable/docs/overview#storage-model) for more details on these identifiers. In the event that two writes with the exact same four-tuple are sent to two different clusters, Bigtable automatically resolves the conflict using an internal _last write wins_ algorithm based on the server-side time. The Bigtable "last write wins" implementation is deterministic, and when replication catches up, all clusters have the same value for the four-tuple. 

## What's next

  * [Learn about schema design.](https://docs.cloud.google.com/bigtable/docs/schema-design)
  * [Implement counters by using aggregate cells.](https://docs.cloud.google.com/bigtable/docs/aggregates)
  * [Use the Bigtable emulator.](https://docs.cloud.google.com/bigtable/docs/emulator)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
