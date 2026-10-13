---
url: https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner/
title: Namespace google::cloud::spanner (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:48.857166+00:00
---

# Namespace google::cloud::spanner (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Namespace google::cloud::spanner (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

Contains all the Cloud Spanner C++ client types and functions. 

## Classes 

### [Backup](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Backup)

This class identifies a Cloud Spanner [Backup](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Backup). 

### [Bytes](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Bytes)

A representation of the Spanner BYTES type: variable-length binary data. 

### [Client](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client)

Performs database client operations on Spanner. 

### [CommitOptions](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1CommitOptions)

Set options on calls to [`spanner::Client::Commit()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client#classgoogle_1_1cloud_1_1spanner_1_1Client_1ae83521aef8045ac04b0a5dc85b08a2d9). 

### [Connection](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Connection)

A connection to a Spanner database instance. 

### [CreateInstanceRequestBuilder](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1CreateInstanceRequestBuilder)

[CreateInstanceRequestBuilder](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1CreateInstanceRequestBuilder) is a builder class for `google::spanner::admin::instance::v1::CreateInstanceRequest`

### [CustomerManagedEncryption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1CustomerManagedEncryption)

Use encryption with `encryption_key`. 

### [Database](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Database)

This class identifies a Cloud Spanner [Database](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Database). 

### [Decimal<>](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Decimal)

A representation of the Spanner NUMERIC type: an exact decimal value with a maximum integer precision (kIntPrecision) and rounding to a maximum fractional precision (kFracPrecision). 

### [DefaultEncryption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1DefaultEncryption)

Use the per-operation default encryption: 

### [DmlResult](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1DmlResult)

Represents the result of a data modifying operation using [`spanner::Client::ExecuteDml()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client#classgoogle_1_1cloud_1_1spanner_1_1Client_1aec1b7d1cd45111126af5aa3b69c8eed0). 

### [ExcludeReplicas](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1ExcludeReplicas)

An [`ExcludeReplicas`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1ExcludeReplicas) contains a list of [`ReplicaSelection`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1ReplicaSelection)s that should be excluded from serving requests. 

### [GoogleEncryption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1GoogleEncryption)

Use Google default encryption. 

### [IncludeReplicas](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1IncludeReplicas)

An [`IncludeReplicas`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1IncludeReplicas) contains an ordered list of [`ReplicaSelection`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1ReplicaSelection)s that should be considered when serving requests. 

### [Instance](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Instance)

This class identifies a Cloud Spanner [Instance](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Instance). 

### [Interval](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Interval)

A representation of the Spanner INTERVAL type: The difference between two date/time values. 

### [Json](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Json)

A simple representation for the Spanner JSON type: a lightweight, text-based, language-independent data interchange format. 

### [JsonB](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1JsonB)

[`JsonB`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1JsonB) is a variant of [`Json`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Json) (see above). 

### [KeyBound](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1KeyBound)

The [`KeyBound`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1KeyBound) class is a regular type that represents an open or closed endpoint for a range of keys. 

### [KeySet](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1KeySet)

The [`KeySet`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1KeySet) class is a regular type that represents a collection of `Key`s. 

### [LimitedErrorCountRetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1LimitedErrorCountRetryPolicy)

A retry policy for the Spanner library based on counting errors. 

### [LimitedErrorCountTransactionRerunPolicy](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1LimitedErrorCountTransactionRerunPolicy)

A transaction rerun policy based on counting errors. 

### [LimitedTimeRetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1LimitedTimeRetryPolicy)

A retry policy for the Spanner library based on elapsed time. 

### [LimitedTimeTransactionRerunPolicy](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1LimitedTimeTransactionRerunPolicy)

A transaction rerun policy based on elapsed time. 

### [Mutation](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Mutation)

A wrapper for Cloud Spanner mutations. 

### [PgOid](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1PgOid)

A representation of the PostgreSQL Object Identifier (OID) type: used as primary keys for various system tables in the PostgreSQL dialect. 

### [ProfileDmlResult](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1ProfileDmlResult)

Represents the result and profile stats of a data modifying operation using [`spanner::Client::ProfileDml()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client#classgoogle_1_1cloud_1_1spanner_1_1Client_1a5628f7c60f46d6d49408245cd9fe8fc1). 

### [ProfileQueryResult](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1ProfileQueryResult)

Represents the stream of `Rows` and profile stats returned from [`spanner::Client::ProfileQuery()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client#classgoogle_1_1cloud_1_1spanner_1_1Client_1abee0a6c093b2d7a645f899368b082eae). 

### [ProtoEnum<E>](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1ProtoEnum)

A representation of the Spanner ENUM type: a protobuf enumeration. 

### [ProtoMessage<M>](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1ProtoMessage)

A representation of the Spanner PROTO type: a protobuf message. 

### [QueryOptions](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1QueryOptions)

These [QueryOptions](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1QueryOptions) allow users to configure features about how their SQL queries executes on the server. 

### [QueryPartition](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1QueryPartition)

The [`QueryPartition`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1QueryPartition) class is a regular type that represents a single slice of a parallel SQL read. 

### [ReadPartition](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1ReadPartition)

The [`ReadPartition`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1ReadPartition) class is a regular type that represents a single slice of a parallel Read operation. 

### [ReplicaSelection](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1ReplicaSelection)

The directed-read replica selector. 

### [ResultSourceInterface](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1ResultSourceInterface)

Defines the interface for [`RowStream`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1RowStream) implementations. 

### [RetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1RetryPolicy)

The base class for the Spanner library retry policies. 

### [Row](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Row)

A [`Row`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Row) is a sequence of columns each with a name and an associated [`Value`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Value). 

### [RowStream](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1RowStream)

Represents the stream of `Rows` returned from [`spanner::Client::Read()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client#classgoogle_1_1cloud_1_1spanner_1_1Client_1a167955c44cd3ccb46ffe07cad6e7e52b) or [`spanner::Client::ExecuteQuery()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client#classgoogle_1_1cloud_1_1spanner_1_1Client_1a8e2afee42f535c0436d9161c54b84179). 

### [RowStreamIterator](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1RowStreamIterator)

A [`RowStreamIterator`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1RowStreamIterator) is an _Input Iterator_ (see below) that returns a sequence of [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<`[`Row`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Row)`>` objects. 

### [SessionPoolOptions](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1SessionPoolOptions)

Controls the session pool maintained by a [`spanner::Client`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client). 

### [SqlStatement](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1SqlStatement)

Represents a potentially parameterized SQL statement. 

### [Timestamp](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Timestamp)

A representation of the Spanner TIMESTAMP type: An instant in time. 

### [Transaction](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Transaction)

The representation of a Cloud Spanner transaction. 

### [TransactionRerunPolicy](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1TransactionRerunPolicy)

The base class for the Spanner library transaction rerun policies. 

### [TupleStream<Tuple>](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1TupleStream)

A [`TupleStream`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1TupleStream)`<Tuple>` defines a range that parses `Tuple` objects from the given range of [`RowStreamIterator`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1RowStreamIterator)s. 

### [TupleStreamIterator<Tuple>](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1TupleStreamIterator)

A [`TupleStreamIterator`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1TupleStreamIterator)`<Tuple>` is an "Input Iterator" that wraps a [`RowStreamIterator`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1RowStreamIterator), parsing its elements into a sequence of [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<Tuple>` objects. 

### [UpdateInstanceRequestBuilder](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1UpdateInstanceRequestBuilder)

[UpdateInstanceRequestBuilder](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1UpdateInstanceRequestBuilder) is a builder class for `google::spanner::admin::instance::v1::UpdateInstanceRequest`

### [Uuid](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Uuid)

A representation of the Spanner UUID type: A 16-byte value that can be represented as a 32-digit hexadecimal string. 

### [Value](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Value)

The [Value](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Value) class represents a type-safe, nullable Spanner value. 

## Structs 

### [BatchDmlResult](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1BatchDmlResult)

The result of executing a batch of DML statements. 

### [BatchedCommitResult](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1BatchedCommitResult)

The result of committing a [Transaction](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Transaction) containing a batch of mutation groups. 

### [CommitResult](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1CommitResult)

The result of committing a [Transaction](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Transaction). 

### [CommitReturnStatsOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1CommitReturnStatsOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to return additional statistics about the committed transaction in a [`spanner::CommitResult`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1CommitResult). 

### [CommitStats](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1CommitStats)

Statistics returned for a committed [Transaction](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Transaction). 

### [CommitTimestamp](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1CommitTimestamp)

A sentinel type used to update a commit timestamp column. 

### [ConnectionOptionsTraits](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1ConnectionOptionsTraits)

The traits to configure [`ConnectionOptions<T>`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1ConnectionOptions.html) for Cloud Spanner. 

### [DirectedReadOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1DirectedReadOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to indicate which replicas or regions should be used for reads/queries in read-only or single-use transactions. 

### [EnableMultiplexedSessionOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1EnableMultiplexedSessionOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to use Multiplexed sessions in lieu of pooled sessions. 

### [ExcludeTransactionFromChangeStreamsOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1ExcludeTransactionFromChangeStreamsOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to control when transaction mutations will not be recorded in change streams that track columns modified by the transaction. 

### [LockHintOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1LockHintOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set the lock hint mechanism for reads done within a transaction. 

### [MaxCommitDelayOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1MaxCommitDelayOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set the amount of latency this request is willing to incur in order to improve throughput. 

### [OrderByOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1OrderByOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set the order in which the rows are returned from a read request. 

### [PartitionDataBoostOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1PartitionDataBoostOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to use "data boost" in the partitions returned from [`Client::PartitionRead()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client#classgoogle_1_1cloud_1_1spanner_1_1Client_1a039dd1aa3b34ad3cbeda17d810809b17) or `PartitionQuery()`. 

### [PartitionedDmlResult](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1PartitionedDmlResult)

The result of executing a Partitioned DML query. 

### [PartitionOptions](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1PartitionOptions)

[Options](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) passed to [`Client::PartitionRead`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client#classgoogle_1_1cloud_1_1spanner_1_1Client_1a039dd1aa3b34ad3cbeda17d810809b17) or [`Client::PartitionQuery`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client#classgoogle_1_1cloud_1_1spanner_1_1Client_1a4b99fa616d2f417c64621523b06a58cf). 

### [PartitionSizeOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1PartitionSizeOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set the desired partition size to be generated by [`Client::PartitionRead()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client#classgoogle_1_1cloud_1_1spanner_1_1Client_1a039dd1aa3b34ad3cbeda17d810809b17) or `PartitionQuery()`. 

### [PartitionsMaximumOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1PartitionsMaximumOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set the desired maximum number of partitions to return from [`Client::PartitionRead()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client#classgoogle_1_1cloud_1_1spanner_1_1Client_1a039dd1aa3b34ad3cbeda17d810809b17) or `PartitionQuery()`. 

### [QueryOptimizerStatisticsPackageOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1QueryOptimizerStatisticsPackageOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set the optimizer statistics package used in an SQL query. 

### [QueryOptimizerVersionOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1QueryOptimizerVersionOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set the optimizer version used in an SQL query. 

### [ReadIndexNameOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1ReadIndexNameOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set the name of an index on a database table. 

### [ReadOptions](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1ReadOptions)

[Options](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) passed to [`Client::Read`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client#classgoogle_1_1cloud_1_1spanner_1_1Client_1a167955c44cd3ccb46ffe07cad6e7e52b) or [`Client::PartitionRead`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client#classgoogle_1_1cloud_1_1spanner_1_1Client_1a039dd1aa3b34ad3cbeda17d810809b17). 

### [ReadRowLimitOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1ReadRowLimitOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set a limit on the number of rows to yield from [`Client::Read()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client#classgoogle_1_1cloud_1_1spanner_1_1Client_1a167955c44cd3ccb46ffe07cad6e7e52b). 

### [RequestPriorityOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1RequestPriorityOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set a [`spanner::RequestPriority`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner_1a47443e04d9a8147dba18a1dec7e62936). 

### [RequestTagOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1RequestTagOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set a per-request tag. 

### [RouteToLeaderOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1RouteToLeaderOption)

Control "route to leader region" headers. 

### [SessionCreatorRoleOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1SessionCreatorRoleOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set the database role used for session creation. 

### [SessionPoolActionOnExhaustionOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1SessionPoolActionOnExhaustionOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set the action to take when attempting to allocate a session when the pool is exhausted. 

### [SessionPoolKeepAliveIntervalOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1SessionPoolKeepAliveIntervalOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set the interval at which we refresh sessions so they don't get collected by the backend GC. 

### [SessionPoolLabelsOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1SessionPoolLabelsOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set the labels used when creating sessions within the pool. 

### [SessionPoolMaxIdleSessionsOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1SessionPoolMaxIdleSessionsOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set the maximum number of sessions to keep in the pool in an idle state. 

### [SessionPoolMaxSessionsPerChannelOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1SessionPoolMaxSessionsPerChannelOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set the maximum number of sessions to create on each channel. 

### [SessionPoolMinSessionsOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1SessionPoolMinSessionsOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set the minimum number of sessions to keep in the pool. 

### [SpannerBackoffPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1SpannerBackoffPolicyOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set a [`spanner::BackoffPolicy`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner). 

### [SpannerPollingPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1SpannerPollingPolicyOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set a [`spanner::PollingPolicy`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner). 

### [SpannerRetryPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1SpannerRetryPolicyOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set a [`spanner::RetryPolicy`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1RetryPolicy). 

### [StreamingResumabilityBufferSizeOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1StreamingResumabilityBufferSizeOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set a limit on how much data will be buffered to guarantee resumability of a streaming read or SQL query. 

### [TransactionIsolationLevelOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1TransactionIsolationLevelOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set the transaction isolation level. 

### [TransactionReadLockModeOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1TransactionReadLockModeOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set the transaction read lock mode. 

### [TransactionTagOption](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1TransactionTagOption)

Option for [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to set a per-transaction tag. 

## Enums 

### [ReplicaType](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner_1a5bfcab079a865a63dd9426fcdb1ee3c6)

Indicates the type of replica. 

### [LockHint](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner_1a9b919a8c520b4a922ec0bc4ba40c7747)

### [DecimalMode](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner_1a25c6b62529bded03cce04f47eb92ff96)

### [ActionOnExhaustion](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner_1a41f0b6c6a62a5189f999a9c102f77312)

Action to take when the session pool is exhausted. 

### [OrderBy](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner_1a1ca66ef1014b50e5819ee1c3b5d53826)

### [RequestPriority](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner_1a47443e04d9a8147dba18a1dec7e62936)

## Functions 

### ToInteger(Decimal< Mode > const &, int)

Conversion to the nearest integer value, scaled by 10^`exponent`. 

Rounds halfway cases away from zero. Fails when the destination type cannot hold that value.

###### Example
    
    
    auto d =
        spanner::MakeDecimal<spanner::DecimalMode::kGoogleSQL>(123456789, -2)
            .value();
    assert(d.ToString() == "1234567.89");
    assert(spanner::ToInteger<int>(d).value() == 1234568);
    assert(spanner::ToInteger<int>(d, 2).value() == 123456789);
    

**Parameters**  
---  
**Name** | **Description**  
`d` | `Decimal< Mode > const &`  
  
`exponent` | `int`  
  
`typename T` | ``  
  
`DecimalMode` | ``  
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< T >` |   
  
### MakeNumeric(std::string)

[`MakeNumeric()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner) factory functions for `Numeric`. 

**Parameter**  
---  
**Name** | **Description**  
`s` | `std::string`  
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< Numeric >` |   
  
### MakeNumeric(double)

[`MakeNumeric()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner) factory functions for `Numeric`. 

**Parameter**  
---  
**Name** | **Description**  
`d` | `double`  
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< Numeric >` |   
  
### MakeNumeric(T, int)

[`MakeNumeric()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner) factory functions for `Numeric`. 

**Parameters**  
---  
**Name** | **Description**  
`i` | `T`  
  
`exponent` | `int`  
  
`typename T` | ``  
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< Numeric >` |   
  
### MakePgNumeric(std::string)

[`MakePgNumeric()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner) factory functions for `PgNumeric`. 

**Parameter**  
---  
**Name** | **Description**  
`s` | `std::string`  
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< PgNumeric >` |   
  
### MakePgNumeric(double)

[`MakePgNumeric()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner) factory functions for `PgNumeric`. 

**Parameter**  
---  
**Name** | **Description**  
`d` | `double`  
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< PgNumeric >` |   
  
### MakePgNumeric(T, int)

[`MakePgNumeric()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner) factory functions for `PgNumeric`. 

**Parameters**  
---  
**Name** | **Description**  
`i` | `T`  
  
`exponent` | `int`  
  
`typename T` | ``  
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< PgNumeric >` |   
  
### MakeBackup(std::string const &)

Constructs a [`Backup`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Backup) from the given `full_name`. 

Returns a non-OK [Status](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) if `full_name` is improperly formed. 

**Parameter**  
---  
**Name** | **Description**  
`full_name` | `std::string const &`  
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< Backup >` |   
  
### MakeConnection(spanner::Database const &, Options)

Returns a [Connection](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Connection) object that can be used for interacting with Spanner. 

The returned connection object should not be used directly; instead it should be given to a [`Client`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client) instance, and methods should be invoked on [`Client`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client).

The optional `opts` argument may be used to configure aspects of the returned [`Connection`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Connection). Expected options are any of the types in the following option lists.

  * [`google::cloud::CommonOptionList`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)
  * [`google::cloud::GrpcOptionList`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)
  * [`google::cloud::spanner::SpannerPolicyOptionList`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner)
  * [`google::cloud::spanner::SessionPoolOptionList`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner)

**Note:** Unrecognized options will be ignored. To debug issues with options set `GOOGLE_CLOUD_CPP_ENABLE_CLOG=yes` in the environment and unexpected options will be logged. 

###### See Also

[`Connection`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Connection)

**Parameters**  
---  
**Name** | **Description**  
`db` | `spanner::Database const &`  
See [`Database`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Database).   
`opts` | `Options`  
(optional) Configure the [`Connection`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Connection) created by this function.   
**Returns**  
---  
**Type** | **Description**  
`std::shared_ptr< spanner::Connection >` |   
  
### MakeConnection(Database const &, ConnectionOptions const &, SessionPoolOptions)

Returns a [Connection](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Connection) object that can be used for interacting with Spanner. 

The returned connection object should not be used directly, rather it should be given to a [`Client`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client) instance, and methods should be invoked on [`Client`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client).

**Deprecated:** Please use the [`MakeConnection()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner) overload that accepts [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) instead. 

###### See Also

[`Connection`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Connection)

**Parameters**  
---  
**Name** | **Description**  
`db` | `Database const &`  
See [`Database`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Database).   
`connection_options` | `ConnectionOptions const &`  
configure the [`Connection`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Connection) created by this function.   
`session_pool_options` | `SessionPoolOptions`  
(optional) configure the `SessionPool` created by the [`Connection`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Connection).   
**Returns**  
---  
**Type** | **Description**  
`std::shared_ptr< Connection >` |   
  
### MakeConnection(Database const &, ConnectionOptions const &, SessionPoolOptions, std::unique_ptr< RetryPolicy >, std::unique_ptr< BackoffPolicy >)

Returns a [Connection](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Connection) object that can be used for interacting with Spanner. 

The returned connection object should not be used directly, rather it should be given to a [`Client`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client) instance, and methods should be invoked on [`Client`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client).

**Deprecated:** Please use the [`MakeConnection()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner) overload that accepts [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) instead. 

###### See Also

[`Connection`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Connection)

**Deprecated:**

Please use the [`MakeConnection()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner) overload that accepts [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) instead. 

###### Example
    
    
      namespace spanner = ::google::cloud::spanner;
      using ::google::cloud::StatusOr;
      [](std::string const& project_id, std::string const& instance_id,
         std::string const& database_id) {
        // Use a truncated exponential backoff with jitter to wait between
        // retries:
        //   https://en.wikipedia.org/wiki/Exponential_backoff
        //   https://cloud.google.com/storage/docs/exponential-backoff
        auto client = spanner::Client(spanner::MakeConnection(
            spanner::Database(project_id, instance_id, database_id),
            google::cloud::Options{}
                .set<spanner::SpannerRetryPolicyOption>(
                    std::make_shared<spanner::LimitedTimeRetryPolicy>(
                        /*maximum_duration=*/std::chrono::seconds(60)))
                .set<spanner::SpannerBackoffPolicyOption>(
                    std::make_shared<spanner::ExponentialBackoffPolicy>(
                        /*initial_delay=*/std::chrono::milliseconds(500),
                        /*maximum_delay=*/std::chrono::seconds(16),
                        /*scaling=*/1.5))));
    
        std::int64_t rows_inserted;
        auto commit_result = client.Commit(
            [&client, &rows_inserted](
                spanner::Transaction txn) -> StatusOr<spanner::Mutations> {
              auto insert = client.ExecuteDml(
                  std::move(txn),
                  spanner::SqlStatement(
                      "INSERT INTO Singers (SingerId, FirstName, LastName)"
                      "  VALUES (20, 'George', 'Washington')"));
              if (!insert) return std::move(insert).status();
              rows_inserted = insert->RowsModified();
              return spanner::Mutations{};
            });
        if (!commit_result) throw std::move(commit_result).status();
        std::cout << "Rows inserted: " << rows_inserted;
      }
    

**Parameters**  
---  
**Name** | **Description**  
`db` | `Database const &`  
See [`Database`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Database).   
`connection_options` | `ConnectionOptions const &`  
configure the [`Connection`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Connection) created by this function.   
`session_pool_options` | `SessionPoolOptions`  
(optional) configure the `SessionPool` created by the [`Connection`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Connection).   
`retry_policy` | `std::unique_ptr< RetryPolicy >`  
  
`backoff_policy` | `std::unique_ptr< BackoffPolicy >`  
  
**Returns**  
---  
**Type** | **Description**  
`std::shared_ptr< Connection >` |   
  
### MakeDatabase(std::string const &)

Constructs a [`Database`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Database) from the given `full_name`. 

Returns a non-OK [Status](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) if `full_name` is improperly formed. 

**Parameter**  
---  
**Name** | **Description**  
`full_name` | `std::string const &`  
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< Database >` |   
  
### MakeInstance(std::string const &)

Constructs an [`Instance`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Instance) from the given `full_name`. 

Returns a non-OK [Status](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) if `full_name` is improperly formed. 

**Parameter**  
---  
**Name** | **Description**  
`full_name` | `std::string const &`  
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< Instance >` |   
  
### MakeInterval(absl::string_view)

Construct an [`Interval`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Interval) from a string. 

At least handles the format produced by `Interval::operator std::string()`. 

**Parameter**  
---  
**Name** | **Description**  
`` | `absl::string_view`  
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< Interval >` |   
  
### JustifyDays(Interval)

Adjust the interval so that 30-day periods are represented as months. 

For example, maps "35 days" to "1 month 5 days". 

**Parameter**  
---  
**Name** | **Description**  
`` | `Interval`  
  
**Returns**  
---  
**Type** | **Description**  
`Interval` |   
  
### JustifyHours(Interval)

Adjust the interval so that 24-hour periods are represented as days. 

For example, maps "27 hours" to "1 day 3 hours". 

**Parameter**  
---  
**Name** | **Description**  
`` | `Interval`  
  
**Returns**  
---  
**Type** | **Description**  
`Interval` |   
  
### JustifyInterval(Interval)

Adjust the interval using both [JustifyDays()](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner) and [JustifyHours()](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner). 

For example, maps "1 month -1 hour" to "29 days 23 hours". 

**Parameter**  
---  
**Name** | **Description**  
`` | `Interval`  
  
**Returns**  
---  
**Type** | **Description**  
`Interval` |   
  
### MakeKey(Ts &&...)

Constructs a `Key` from the given arguments. 

###### Example
    
    
      auto delete_albums = spanner::DeleteMutationBuilder(
                               "Albums", spanner::KeySet()
                                             .AddKey(spanner::MakeKey(2, 1))
                                             .AddKey(spanner::MakeKey(2, 3)))
                               .Build();
    

**Parameters**  
---  
**Name** | **Description**  
`ts` | `Ts &&...`  
  
`typename...` | ``  
  
**Returns**  
---  
**Type** | **Description**  
`Key` |   
  
### MakeKeyBoundClosed(Ts &&...)

Returns a "closed" [`KeyBound`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1KeyBound) with a `Key` constructed from the given arguments. 

###### Example
    
    
      auto delete_singers_range =
          spanner::DeleteMutationBuilder(
              "Singers", spanner::KeySet().AddRange(spanner::MakeKeyBoundClosed(3),
                                                    spanner::MakeKeyBoundOpen(5)))
              .Build();
    

**Parameters**  
---  
**Name** | **Description**  
`ts` | `Ts &&...`  
  
`typename...` | ``  
  
**Returns**  
---  
**Type** | **Description**  
`KeyBound` |   
  
### MakeKeyBoundOpen(Ts &&...)

Returns an "open" [`KeyBound`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1KeyBound) with a `Key` constructed from the given arguments. 

###### Example
    
    
      auto key_set = spanner::KeySet().AddRange(spanner::MakeKeyBoundOpen(0),
                                                spanner::MakeKeyBoundOpen(11));
    

**Parameters**  
---  
**Name** | **Description**  
`ts` | `Ts &&...`  
  
`typename...` | ``  
  
**Returns**  
---  
**Type** | **Description**  
`KeyBound` |   
  
### MakeInsertMutation(std::string, std::vector< std::string >, Ts &&...)

Creates a simple insert mutation for the values in `values`. 

###### Example
    
    
    void MakeInsertMutation(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
    
      // Delete each of the albums by individual key, then delete all the singers
      // using a key range.
      auto commit_result = client.Commit(spanner::Mutations{
          spanner::InsertOrUpdateMutationBuilder(
              "Performances",
              {"SingerId", "VenueId", "EventDate", "Revenue", "LastUpdateTime"})
              .EmplaceRow(1, 4, absl::CivilDay(2017, 10, 5), 11000,
                          spanner::CommitTimestamp{})
              .EmplaceRow(1, 19, absl::CivilDay(2017, 11, 2), 15000,
                          spanner::CommitTimestamp{})
              .Build()});
      if (!commit_result) throw std::move(commit_result).status();
      std::cout << "make-insert-mutation was successful\n";
    }
    

###### See Also

The [Mutation](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Mutation) class documentation for an overview of the Cloud Spanner mutation API

###### See Also

<https://cloud.google.com/spanner/docs/modify-mutation-api> for more information about the Cloud Spanner mutation API. 

**Parameters**  
---  
**Name** | **Description**  
`table_name` | `std::string`  
  
`columns` | `std::vector< std::string >`  
  
`values` | `Ts &&...`  
  
`typename...` | ``  
  
**Returns**  
---  
**Type** | **Description**  
`Mutation` |   
  
### MakeUpdateMutation(std::string, std::vector< std::string >, Ts &&...)

Creates a simple update mutation for the values in `values`. 

###### Example
    
    
    void MakeUpdateMutation(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
      auto commit = client.Commit(spanner::Mutations{
          spanner::MakeUpdateMutation(
              "Albums", {"SingerId", "AlbumId", "MarketingBudget"}, 1, 1, 200000),
      });
      if (!commit) throw std::move(commit).status();
      std::cout << "make-update-mutation was successful\n";
    }
    

###### See Also

The [Mutation](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Mutation) class documentation for an overview of the Cloud Spanner mutation API

###### See Also

<https://cloud.google.com/spanner/docs/modify-mutation-api> for more information about the Cloud Spanner mutation API. 

**Parameters**  
---  
**Name** | **Description**  
`table_name` | `std::string`  
  
`columns` | `std::vector< std::string >`  
  
`values` | `Ts &&...`  
  
`typename...` | ``  
  
**Returns**  
---  
**Type** | **Description**  
`Mutation` |   
  
### MakeInsertOrUpdateMutation(std::string, std::vector< std::string >, Ts &&...)

Creates a simple "insert or update" mutation for the values in `values`. 

###### Example
    
    
    void MakeInsertOrUpdateMutation(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
      auto commit = client.Commit(spanner::Mutations{
          spanner::MakeInsertOrUpdateMutation(
              "Albums", {"SingerId", "AlbumId", "AlbumTitle", "MarketingBudget"}, 1,
              1, "Total Junk", 200000),
      });
      if (!commit) throw std::move(commit).status();
    
      std::cout << "make-insert-or-update-mutation was successful\n";
    }
    

###### See Also

The [Mutation](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Mutation) class documentation for an overview of the Cloud Spanner mutation API

###### See Also

<https://cloud.google.com/spanner/docs/modify-mutation-api> for more information about the Cloud Spanner mutation API. 

**Parameters**  
---  
**Name** | **Description**  
`table_name` | `std::string`  
  
`columns` | `std::vector< std::string >`  
  
`values` | `Ts &&...`  
  
`typename...` | ``  
  
**Returns**  
---  
**Type** | **Description**  
`Mutation` |   
  
### MakeReplaceMutation(std::string, std::vector< std::string >, Ts &&...)

Creates a simple "replace" mutation for the values in `values`. 

###### Example
    
    
    void MakeReplaceMutation(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
      auto commit = client.Commit(spanner::Mutations{
          spanner::MakeReplaceMutation(
              "Albums", {"SingerId", "AlbumId", "AlbumTitle", "MarketingBudget"}, 1,
              1, "Go, Go, Go", 600000),
      });
      if (!commit) throw std::move(commit).status();
    
      std::cout << "make-replace-mutation was successful\n";
    }
    

###### See Also

The [Mutation](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Mutation) class documentation for an overview of the Cloud Spanner mutation API

###### See Also

<https://cloud.google.com/spanner/docs/modify-mutation-api> for more information about the Cloud Spanner mutation API. 

**Parameters**  
---  
**Name** | **Description**  
`table_name` | `std::string`  
  
`columns` | `std::vector< std::string >`  
  
`values` | `Ts &&...`  
  
`typename...` | ``  
  
**Returns**  
---  
**Type** | **Description**  
`Mutation` |   
  
### MakeDeleteMutation(std::string, KeySet)

Creates a simple "delete" mutation for the values in `keys`. 

###### Example
    
    
    void MakeDeleteMutation(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
      auto commit = client.Commit(spanner::Mutations{
          spanner::MakeDeleteMutation("Albums", spanner::KeySet::All()),
      });
      if (!commit) throw std::move(commit).status();
    
      std::cout << "make-delete-mutation was successful\n";
    }
    

###### See Also

The [Mutation](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Mutation) class documentation for an overview of the Cloud Spanner mutation API

###### See Also

<https://cloud.google.com/spanner/docs/modify-mutation-api> for more information about the Cloud Spanner mutation API. 

**Parameters**  
---  
**Name** | **Description**  
`table_name` | `std::string`  
  
`keys` | `KeySet`  
  
**Returns**  
---  
**Type** | **Description**  
`Mutation` |   
  
### MakeSendMutation(std::string, Key, Value)

Creates a "send" mutation to enqueue a message with `key` and `payload` into `queue` for immediate delivery. 

###### See Also

The [Mutation](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Mutation) class documentation for an overview of the Cloud Spanner mutation API

###### See Also

<https://cloud.google.com/spanner/docs/modify-mutation-api> for more information about the Cloud Spanner mutation API. 

**Parameters**  
---  
**Name** | **Description**  
`queue` | `std::string`  
  
`key` | `Key`  
  
`payload` | `Value`  
  
**Returns**  
---  
**Type** | **Description**  
`Mutation` |   
  
### MakeSendMutation(std::string, Key, Value, Timestamp)

Creates a "send" mutation to enqueue a message with `key` and `payload` into `queue` scheduled for `deliver_time`. 

###### See Also

The [Mutation](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Mutation) class documentation for an overview of the Cloud Spanner mutation API

###### See Also

<https://cloud.google.com/spanner/docs/modify-mutation-api> for more information about the Cloud Spanner mutation API. 

**Parameters**  
---  
**Name** | **Description**  
`queue` | `std::string`  
  
`key` | `Key`  
  
`payload` | `Value`  
  
`deliver_time` | `Timestamp`  
  
**Returns**  
---  
**Type** | **Description**  
`Mutation` |   
  
### MakeAckMutation(std::string, Key)

Creates an "ack" mutation to acknowledge the message with `key` in `queue`. 

###### See Also

The [Mutation](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Mutation) class documentation for an overview of the Cloud Spanner mutation API

###### See Also

<https://cloud.google.com/spanner/docs/modify-mutation-api> for more information about the Cloud Spanner mutation API. 

**Parameters**  
---  
**Name** | **Description**  
`queue` | `std::string`  
  
`key` | `Key`  
  
**Returns**  
---  
**Type** | **Description**  
`Mutation` |   
  
### MakeAckMutation(std::string, Key, bool)

Creates an "ack" mutation to acknowledge the message with `key` in `queue`, optionally ignoring `NOT_FOUND` errors according to `ignore_not_found`. 

###### See Also

The [Mutation](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Mutation) class documentation for an overview of the Cloud Spanner mutation API

###### See Also

<https://cloud.google.com/spanner/docs/modify-mutation-api> for more information about the Cloud Spanner mutation API. 

**Parameters**  
---  
**Name** | **Description**  
`queue` | `std::string`  
  
`key` | `Key`  
  
`ignore_not_found` | `bool`  
  
**Returns**  
---  
**Type** | **Description**  
`Mutation` |   
  
### MakeDecimal(std::string)

Construction from a string, in decimal fixed- or floating-point formats. 

  * [-+]?[0-9]+(.[0-9]*)?([eE][-+]?[0-9]+)?
  * [-+]?.[0-9]+([eE][-+]?[0-9]+)?
  * [Nn][Aa][Nn] // "not a number" for kPostgreSQL mode



For example, "0", "-999", "3.141592654", "299792458", "6.02214076e23", etc. There must be digits either before or after any decimal point.

Fails on syntax errors or if the conversion would yield a value outside the NUMERIC range. If the argument has more than `kFracPrecision` digits after the decimal point it will be rounded, with halfway cases rounding away from zero. 

**Parameters**  
---  
**Name** | **Description**  
`s` | `std::string`  
  
`DecimalMode` | ``  
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< Decimal< Mode > >` |   
  
### MakeDecimal(double)

Construction from a double. 

Fails on NaN or any argument outside the NUMERIC value range (including infinities). If the argument has more than `kFracPrecision` digits after the decimal point it will be rounded, with halfway cases rounding away from zero. 

**Parameters**  
---  
**Name** | **Description**  
`d` | `double`  
  
`DecimalMode` | ``  
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< Decimal< Mode > >` |   
  
### MakeDecimal(T, int)

Construction from an integer `i`, scaled by 10^`exponent`. 

Fails on any (scaled) argument outside the NUMERIC value range. 

**Parameters**  
---  
**Name** | **Description**  
`i` | `T`  
  
`exponent` | `int`  
  
`typename T` | ``  
  
`DecimalMode` | ``  
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< Decimal< Mode > >` |   
  
### ToDouble(Decimal< Mode > const &)

Conversion to the closest double value, with possible loss of precision. 

Always succeeds (i.e., can never overflow, assuming a double can hold values up to 10^(kIntPrecision+1)). 

**Parameters**  
---  
**Name** | **Description**  
`d` | `Decimal< Mode > const &`  
  
`DecimalMode` | ``  
  
**Returns**  
---  
**Type** | **Description**  
`double` |   
  
### ToOptions(PartitionOptions const &)

Converts [`PartitionOptions`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1PartitionOptions) to common [`Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html). 

**Parameter**  
---  
**Name** | **Description**  
`` | `PartitionOptions const &`  
  
**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### ToPartitionOptions(Options const &)

Converts common [`Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to [`PartitionOptions`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1PartitionOptions). 

**Parameter**  
---  
**Name** | **Description**  
`` | `Options const &`  
  
**Returns**  
---  
**Type** | **Description**  
`PartitionOptions` |   
  
### SerializeQueryPartition(QueryPartition const &)

Serializes an instance of [`QueryPartition`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1QueryPartition) to a string of bytes. 

The serialized string of bytes is suitable for writing to disk or transmission to another process.

**Note:** The serialized string may contain NUL and other non-printable characters. Therefore, callers should avoid [formatted IO](https://en.cppreference.com/w/cpp/string/basic_string/operator_ltltgtgt) functions that may incorrectly reformat the string data. 

###### Example
    
    
        namespace spanner = ::google::cloud::spanner;
        google::cloud::StatusOr<std::string> serialized_partition =
            spanner::SerializeQueryPartition(partition);
        if (!serialized_partition) throw std::move(serialized_partition).status();
        std::string const& bytes = *serialized_partition;
        // `bytes` contains the serialized data, which may contain NULs and other
        // non-printable characters.
        SendBinaryStringData(bytes);
    

**Parameter**  
---  
**Name** | **Description**  
`query_partition` | `QueryPartition const &`  


  * instance to be serialized.

  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< std::string >` |   
  
### DeserializeQueryPartition(std::string const &)

Deserializes the provided string into a [`QueryPartition`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1QueryPartition). 

The `serialized_query_partition` argument must be a string that was previously returned by a call to [`SerializeQueryPartition()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner).

**Note:** The serialized string may contain NUL and other non-printable characters. Therefore, callers should avoid [formatted IO](https://en.cppreference.com/w/cpp/string/basic_string/operator_ltltgtgt) functions that may incorrectly reformat the string data. 

###### Example
    
    
      google::cloud::StatusOr<google::cloud::spanner::QueryPartition>
      ReceiveQueryPartitionFromRemoteMachine() {
        std::string serialized_partition = Receive();
        return google::cloud::spanner::DeserializeQueryPartition(
            serialized_partition);
      }
    

**Parameter**  
---  
**Name** | **Description**  
`serialized_query_partition` | `std::string const &`  
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< QueryPartition >` |   
  
### ToOptions(ReadOptions const &)

Converts [`ReadOptions`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1ReadOptions) to common [`Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html). 

**Parameter**  
---  
**Name** | **Description**  
`` | `ReadOptions const &`  
  
**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### ToReadOptions(Options const &)

Converts common [`Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to [`ReadOptions`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1ReadOptions). 

**Parameter**  
---  
**Name** | **Description**  
`` | `Options const &`  
  
**Returns**  
---  
**Type** | **Description**  
`ReadOptions` |   
  
### SerializeReadPartition(ReadPartition const &)

Serializes an instance of [`ReadPartition`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1ReadPartition) to a string of bytes. 

The serialized string of bytes is suitable for writing to disk or transmission to another process.

**Note:** The serialized string may contain NUL and other non-printable characters. Therefore, callers should avoid [formatted IO](https://en.cppreference.com/w/cpp/string/basic_string/operator_ltltgtgt) functions that may incorrectly reformat the string data. 

###### Example
    
    
        namespace spanner = ::google::cloud::spanner;
        google::cloud::StatusOr<std::string> serialized_partition =
            spanner::SerializeReadPartition(partition);
        if (!serialized_partition) throw std::move(serialized_partition).status();
        std::string const& bytes = *serialized_partition;
        // `bytes` contains the serialized data, which may contain NULs and other
        // non-printable characters.
        SendBinaryStringData(bytes);
    

**Parameter**  
---  
**Name** | **Description**  
`read_partition` | `ReadPartition const &`  


  * instance to be serialized.

  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< std::string >` |   
  
### DeserializeReadPartition(std::string const &)

Deserializes the provided string into a [`ReadPartition`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1ReadPartition). 

The `serialized_read_partition` argument must be a string that was previously returned by a call to [`SerializeReadPartition()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner).

**Note:** The serialized string may contain NUL and other non-printable characters. Therefore, callers should avoid [formatted IO](https://en.cppreference.com/w/cpp/string/basic_string/operator_ltltgtgt) functions that may incorrectly reformat the string data. 

###### Example
    
    
      google::cloud::StatusOr<google::cloud::spanner::ReadPartition>
      ReceiveReadPartitionFromRemoteMachine() {
        std::string serialized_partition = Receive();
        return google::cloud::spanner::DeserializeReadPartition(
            serialized_partition);
      }
    

**Parameter**  
---  
**Name** | **Description**  
`serialized_read_partition` | `std::string const &`  


  * string representation to be deserialized.

  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< ReadPartition >` |   
  
### StreamOf(RowRange &&)

A factory that creates a [`TupleStream`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1TupleStream)`<Tuple>` by wrapping the given `range`. 

The `RowRange` must be a range defined by [`RowStreamIterator`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1RowStreamIterator) objects.
    
    
    void StreamOf(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
    
      std::cout << "Querying the Singers table:\n";
      auto query = client.ExecuteQuery(spanner::SqlStatement(
          "SELECT SingerId, FirstName, LastName FROM Singers"));
      using RowType = std::tuple<std::int64_t, std::string, std::string>;
    
      for (auto& row : spanner::StreamOf<RowType>(query)) {
        if (!row) throw std::move(row).status();
        std::cout << "  SingerId: " << std::get<0>(*row) << "\n"
                  << "  FirstName: " << std::get<1>(*row) << "\n"
                  << "  LastName: " << std::get<2>(*row) << "\n";
      }
      std::cout << "end of results\n";
    }
    

**Note:** Ownership of the `range` is not transferred, so it must outlive the returned [`TupleStream`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1TupleStream). 

**Parameters**  
---  
**Name** | **Description**  
`range` | `RowRange &&`  
  
`typename Tuple` | ``  
  
`typename RowRange` | ``  
must be a range defined by [`RowStreamIterator`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1RowStreamIterator)s.   
**Returns**  
---  
**Type** | **Description**  
`TupleStream< Tuple >` |   
  
### GetSingularRow(RowRange)

Returns the only row from a range that contains exactly one row. 

An error is returned if the given range does not contain exactly one row. This is a convenience function that may be useful when the caller knows that a range should contain exactly one row, such as when `LIMIT 1` is used in an SQL query, or when a read is performed on a guaranteed unique key such that only a single row could possibly match. In cases where the caller does not know how many rows may be returned, they should instead consume the range in a loop.
    
    
    void GetSingularRow(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
    
      auto query = client.ExecuteQuery(spanner::SqlStatement(
          "SELECT FirstName, LastName FROM Singers WHERE SingerId = @singer_id",
          {{"singer_id", spanner::Value(2)}}));
      // `SingerId` is the primary key for the `Singers` table, the `GetSingularRow`
      // helper returns a single row or an error:
      using RowType = std::tuple<std::string, std::string>;
      auto row = GetSingularRow(spanner::StreamOf<RowType>(query));
      if (!row) throw std::move(row).status();
      std::cout << "FirstName: " << std::get<0>(*row)
                << "\nLastName: " << std::get<1>(*row) << "\n";
    }
    

**Parameters**  
---  
**Name** | **Description**  
`range` | `RowRange`  
  
`typename RowRange` | ``  
  
**Returns**  
---  
**Type** | **Description**  
`std::decay_t< decltype(*range.begin())>` |   
  
### MakeTimestamp(absl::Time)

Construct a [`Timestamp`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Timestamp) from an `absl::Time`. 

May produce out-of-range errors if the given time is beyond the range supported by [`Timestamp`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Timestamp) (see class comments above). 

**Parameter**  
---  
**Name** | **Description**  
`` | `absl::Time`  
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< Timestamp >` |   
  
### MakeTimestamp(protobuf::Timestamp const &)

Construct a [`Timestamp`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Timestamp) from a `google::protobuf::Timestamp`. 

May produce out-of-range errors if the given protobuf is beyond the range supported by [`Timestamp`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Timestamp) (which a valid protobuf never will). 

**Parameter**  
---  
**Name** | **Description**  
`` | `protobuf::Timestamp const &`  
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< Timestamp >` |   
  
### MakeTimestamp(sys_time< Duration > const &)

Construct a [`Timestamp`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Timestamp) from a `std::chrono::time_point` on the system clock. 

May produce out-of-range errors, depending on the properties of `Duration` and the `std::chrono::system_clock` epoch. `Duration::rep` may not be wider than `std::int64_t`. Requires that `Duration::period` is no more precise than `std::nano`. 

**Parameters**  
---  
**Name** | **Description**  
`tp` | `sys_time< Duration > const &`  
  
`typename Duration` | ``  
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< Timestamp >` |   
  
### MakeReadOnlyTransaction(Transaction::ReadOnlyOptions)

Create a read-only transaction configured with `opts`. 

**Note:** This is a lazy evaluated operation. No RPCs are made as part of creating a [`Transaction`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Transaction) object. Instead, the first request to the server (for example as part of a `ExecuteQuery()` call) will also create the transaction.  


**Parameter**  
---  
**Name** | **Description**  
`opts` | `Transaction::ReadOnlyOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`Transaction` |   
  
### MakeReadWriteTransaction(Transaction::ReadWriteOptions)

Create a read-write transaction configured with `opts`. 

**Note:** This is a lazy evaluated operation. No RPCs are made as part of creating a [`Transaction`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Transaction) object. Instead, the first request to the server (for example as part of a `ExecuteQuery()` call) will also create the transaction.  


**Parameter**  
---  
**Name** | **Description**  
`opts` | `Transaction::ReadWriteOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`Transaction` |   
  
### MakeReadWriteTransaction(Transaction const &, Transaction::ReadWriteOptions)

Create a read-write transaction configured with `opts`, and sharing lock priority with `txn`. 

This should be used when rerunning an aborted transaction, so that the new attempt has a slightly better chance of success. 

**Parameters**  
---  
**Name** | **Description**  
`txn` | `Transaction const &`  
  
`opts` | `Transaction::ReadWriteOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`Transaction` |   
  
### MakeUuid(absl::string_view)

Parses a textual representation a [`Uuid`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Uuid) from a string of hexadecimal digits. 

Returns an error if unable to parse the given input.

Acceptable input strings must consist of 32 hexadecimal digits: [0-9a-fA-F]. Optional curly braces are allowed around the entire sequence of digits as are hyphens between any pair of hexadecimal digits.

Example acceptable inputs:

  * {0b6ed04c-a16d-fc46-5281-7f9978c13738}
  * 0b6ed04ca16dfc4652817f9978c13738
  * 7Bf8-A7b8-1917-1919-2625-F208-c582-4254
  * {DECAFBAD-DEAD-FADE-CAFE-FEEDFACEBEEF} 



**Parameter**  
---  
**Name** | **Description**  
`s` | `absl::string_view`  
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< Uuid >` |   
  
### MakeNullValue()

Factory to construct a "null" [Value](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Value) of the specified type `T`. 

This is equivalent to passing an `std::optional<T>` without a value to the constructor, though this factory may be easier to invoke and result in clearer code at the call site. 

**Parameter**  
---  
**Name** | **Description**  
`typename T` | ``  
  
**Returns**  
---  
**Type** | **Description**  
`Value` |   
  
### VersionMajor()

The Cloud Spanner C++ [Client](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client) major version. 

**Returns**  
---  
**Type** | **Description**  
`int constexpr` |   
  
### VersionMinor()

The Cloud Spanner C++ [Client](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client) minor version. 

**Returns**  
---  
**Type** | **Description**  
`int constexpr` |   
  
### VersionPatch()

The Cloud Spanner C++ [Client](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client) patch version. 

**Returns**  
---  
**Type** | **Description**  
`int constexpr` |   
  
### VersionPreRelease()

The Cloud Spanner C++ [Client](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client) pre-release version. 

**Returns**  
---  
**Type** | **Description**  
`char const *` |   
  
### Version()

A single integer representing the Major/Minor/Patch version. 

**Returns**  
---  
**Type** | **Description**  
`int constexpr` |   
  
### VersionString()

The version as a string, in MAJOR.MINOR.PATCH[-PRE][+gitrev] format. 

**Returns**  
---  
**Type** | **Description**  
`std::string` |   
  
## Type Aliases 

### Numeric

**Alias Of** : `Decimal< DecimalMode::kGoogleSQL >`

Most users only need the `Numeric` or `PgNumeric` specializations of [`Decimal`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Decimal). 

For example:
    
    
    auto n = spanner::MakeNumeric(42).value();
    assert(n.ToString() == "42");
    assert(spanner::ToInteger<int>(n).value() == 42);
    

### PgNumeric

**Alias Of** : `Decimal< DecimalMode::kPostgreSQL >`

Most users only need the `Numeric` or `PgNumeric` specializations of [`Decimal`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Decimal). 

For example:
    
    
    auto n = spanner::MakeNumeric(42).value();
    assert(n.ToString() == "42");
    assert(spanner::ToInteger<int>(n).value() == 42);
    

### BackoffPolicy

**Alias Of** : `::google::cloud::internal::BackoffPolicy`

The base class for backoff policies. 

### ExponentialBackoffPolicy

**Alias Of** : `google::cloud::internal::ExponentialBackoffPolicy`

A truncated exponential backoff policy with randomized periods. 

### BatchedCommitResultStream

**Alias Of** : `StreamRange< BatchedCommitResult >`

Represents the stream of [`BatchedCommitResult`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/structgoogle_1_1cloud_1_1spanner_1_1BatchedCommitResult) objects returned from the batched [`Client::CommitAtLeastOnce()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client#classgoogle_1_1cloud_1_1spanner_1_1Client_1a3765eebf4b408b580d7d3ef9d7f52ed2). 

### ConnectionOptions

**Alias Of** : `google::cloud::ConnectionOptions< ConnectionOptionsTraits >`

The options for Cloud Spanner connections. 

**Deprecated:** Use [`Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) instead. 

### Date

**Alias Of** : `::absl::CivilDay`

Represents a date in the proleptic Gregorian calendar as a triple of year, month (1-12), and day (1-31). 

We use `absl::CivilDay` to represent a "date". Direct use of `absl::CivilDay` is recommended. This alias exists for backward compatibility.

###### See Also

<https://abseil.io/docs/cpp/guides/time#civil-times>

### EncryptionConfig

**Alias Of** : `std::variant< DefaultEncryption, GoogleEncryption, CustomerManagedEncryption >`

Specify the encryption configuration for any of the following operations: 

  * `DatabaseAdminClient::CreateDatabase()`
  * `DatabaseAdminClient::CreateBackup()`
  * `DatabaseAdminClient::RestoreDatabase()`



### IamUpdater

**Alias Of** : `::google::cloud::IamUpdater`

Type alias for [`google::cloud::IamUpdater`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html). 

Used in the `SetIamPolicy()` read-modify-write cycle of the Spanner admin clients, `DatabaseAdminClient` and `InstanceAdminClient`, in order to avoid race conditions.

The updater is called with a recently fetched policy, and should either return an empty optional if no changes are required, or return a new policy to be set. In the latter case the control loop will always set the `etag` of the new policy to that of the recently fetched one. A failure to update then indicates a race, and the process will repeat. 

### Key

**Alias Of** : `std::vector< Value >`

A `Key` is a collection of [`Value`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Value) objects where the i'th value corresponds to the i'th component of the table or primary index key. 

In C++, this is implemented as a `std::vector<`[`Value`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Value)`>`. See the `MakeKey` factory function below for an easy way to construct a valid `Key` instance. 

### Mutations

**Alias Of** : `std::vector< Mutation >`

An ordered sequence of mutations to pass to [`Client::Commit()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client#classgoogle_1_1cloud_1_1spanner_1_1Client_1ae83521aef8045ac04b0a5dc85b08a2d9) or return from the [`Client::Commit()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Client#classgoogle_1_1cloud_1_1spanner_1_1Client_1ae83521aef8045ac04b0a5dc85b08a2d9) mutator. 

### InsertMutationBuilder

**Alias Of** : `spanner_internal::WriteMutationBuilder< spanner_internal::InsertOp >`

A helper class to construct "insert" mutations. 

###### Example
    
    
    void InsertMutationBuilder(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
      auto commit = client.Commit(
          spanner::Mutations{spanner::InsertMutationBuilder(
                                 "Singers", {"SingerId", "FirstName", "LastName"})
                                 .EmplaceRow(1, "Marc", "Richards")
                                 .EmplaceRow(2, "Catalina", "Smith")
                                 .EmplaceRow(3, "Alice", "Trentor")
                                 .EmplaceRow(4, "Lea", "Martin")
                                 .EmplaceRow(5, "David", "Lomond")
                                 .Build(),
                             spanner::InsertMutationBuilder(
                                 "Albums", {"SingerId", "AlbumId", "AlbumTitle"})
                                 .EmplaceRow(1, 1, "Total Junk")
                                 .EmplaceRow(1, 2, "Go, Go, Go")
                                 .EmplaceRow(2, 1, "Green")
                                 .EmplaceRow(2, 2, "Forever Hold Your Peace")
                                 .EmplaceRow(2, 3, "Terrified")
                                 .Build()});
      if (!commit) throw std::move(commit).status();
      std::cout << "insert-mutation-builder was successful\n";
    }
    

###### See Also

The [Mutation](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Mutation) class documentation for an overview of the Cloud Spanner mutation API

###### See Also

<https://cloud.google.com/spanner/docs/modify-mutation-api> for more information about the Cloud Spanner mutation API. 

### UpdateMutationBuilder

**Alias Of** : `spanner_internal::WriteMutationBuilder< spanner_internal::UpdateOp >`

A helper class to construct "update" mutations. 

###### Example
    
    
    void UpdateMutationBuilder(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
      auto commit = client.Commit(spanner::Mutations{
          spanner::UpdateMutationBuilder("Albums",
                                         {"SingerId", "AlbumId", "MarketingBudget"})
              .EmplaceRow(1, 1, 100000)
              .EmplaceRow(2, 2, 500000)
              .Build()});
      if (!commit) throw std::move(commit).status();
      std::cout << "update-mutation-builder was successful\n";
    }
    

###### See Also

The [Mutation](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Mutation) class documentation for an overview of the Cloud Spanner mutation API

###### See Also

<https://cloud.google.com/spanner/docs/modify-mutation-api> for more information about the Cloud Spanner mutation API. 

### InsertOrUpdateMutationBuilder

**Alias Of** : `spanner_internal::WriteMutationBuilder< spanner_internal::InsertOrUpdateOp >`

A helper class to construct "insert_or_update" mutations. 

###### Example
    
    
    void InsertOrUpdateMutationBuilder(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
      auto commit = client.Commit(spanner::Mutations{
          spanner::InsertOrUpdateMutationBuilder(
              "Albums", {"SingerId", "AlbumId", "AlbumTitle", "MarketingBudget"})
              .EmplaceRow(1, 1, "Total Junk", 100000)
              .EmplaceRow(1, 2, "Go, Go, Go", 200000)
              .EmplaceRow(2, 1, "Green", 300000)
              .EmplaceRow(2, 2, "Forever Hold Your Peace", 400000)
              .EmplaceRow(2, 3, "Terrified", 500000)
              .Build()});
      if (!commit) throw std::move(commit).status();
    
      std::cout << "insert-or-update-mutation-builder was successful\n";
    }
    

###### See Also

The [Mutation](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Mutation) class documentation for an overview of the Cloud Spanner mutation API

###### See Also

<https://cloud.google.com/spanner/docs/modify-mutation-api> for more information about the Cloud Spanner mutation API. 

### ReplaceMutationBuilder

**Alias Of** : `spanner_internal::WriteMutationBuilder< spanner_internal::ReplaceOp >`

A helper class to construct "replace" mutations. 

###### Example
    
    
    void ReplaceMutationBuilder(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
      auto commit = client.Commit(spanner::Mutations{
          spanner::ReplaceMutationBuilder(
              "Albums", {"SingerId", "AlbumId", "AlbumTitle", "MarketingBudget"})
              .EmplaceRow(1, 1, "Total Junk", 500000)
              .EmplaceRow(1, 2, "Go, Go, Go", 400000)
              .EmplaceRow(2, 1, "Green", 300000)
              .Build()});
      if (!commit) throw std::move(commit).status();
    
      std::cout << "replace-mutation-builder was successful\n";
    }
    

###### See Also

The [Mutation](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Mutation) class documentation for an overview of the Cloud Spanner mutation API

###### See Also

<https://cloud.google.com/spanner/docs/modify-mutation-api> for more information about the Cloud Spanner mutation API. 

### DeleteMutationBuilder

**Alias Of** : `spanner_internal::DeleteMutationBuilder`

A helper class to construct "delete" mutations. 

###### Example
    
    
    void DeleteMutationBuilder(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
      auto commit = client.Commit(
          spanner::Mutations{spanner::DeleteMutationBuilder(
                                 "Albums", spanner::KeySet()
                                               .AddKey(spanner::MakeKey(1, 1))
                                               .AddKey(spanner::MakeKey(1, 2)))
                                 .Build()});
      if (!commit) throw std::move(commit).status();
    
      std::cout << "delete-mutation-builder was successful\n";
    }
    

###### See Also

The [Mutation](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Mutation) class documentation for an overview of the Cloud Spanner mutation API

###### See Also

<https://cloud.google.com/spanner/docs/modify-mutation-api> for more information about the Cloud Spanner mutation API. 

### SendMutationBuilder

**Alias Of** : `spanner_internal::SendMutationBuilder`

A helper class to construct queue "send" mutations. 

###### See Also

The [Mutation](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Mutation) class documentation for an overview of the Cloud Spanner mutation API

###### See Also

<https://cloud.google.com/spanner/docs/modify-mutation-api> for more information about the Cloud Spanner mutation API. 

### AckMutationBuilder

**Alias Of** : `spanner_internal::AckMutationBuilder`

A helper class to construct queue "ack" mutations. 

###### See Also

The [Mutation](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Mutation) class documentation for an overview of the Cloud Spanner mutation API

###### See Also

<https://cloud.google.com/spanner/docs/modify-mutation-api> for more information about the Cloud Spanner mutation API. 

### SpannerPolicyOptionList

**Alias Of** : `OptionList< SpannerRetryPolicyOption, SpannerBackoffPolicyOption, SpannerPollingPolicyOption >`

List of all "policy" options. 

### SessionPoolOptionList

**Alias Of** : `OptionList< RouteToLeaderOption, SessionCreatorRoleOption, SessionPoolLabelsOption >`

List of all SessionPool options. 

Pass to [`spanner::MakeConnection()`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/namespacegoogle_1_1cloud_1_1spanner). 

### RequestOptionList

**Alias Of** : `OptionList< RequestPriorityOption, RequestTagOption >`

List of Request options for `client::ExecuteBatchDml()`. 

### PollingPolicy

**Alias Of** : `::google::cloud::PollingPolicy`

### GenericPollingPolicy

**Alias Of** : `::google::cloud::GenericPollingPolicy< Retry, Backoff >`

### ExecutionPlan

**Alias Of** : `::google::spanner::v1::QueryPlan`

Contains a hierarchical representation of the operations the database server performs in order to execute a particular SQL statement. 

[Query Plan proto](https://github.com/googleapis/googleapis/blob/master/google/spanner/v1/query_plan.proto)

###### Example:
    
    
      // For a SQL query to be partitionable, it has to satisfy some conditions.
      // For example, if it has a Distributed Union operator, the Distributed
      // Union operator must be the first operator in the `ExecutionPlan`.
      // For detailed definition, please refer to
      // https://cloud.google.com/spanner/docs/reads#read_data_in_parallel
      auto is_partitionable = [](spanner::ExecutionPlan const& plan) {
        return (!plan.plan_nodes().empty() &&
                plan.plan_nodes(0).kind() ==
                    google::spanner::v1::PlanNode::RELATIONAL &&
                plan.plan_nodes(0).display_name() == "Distributed Union");
      };
    
      google::cloud::StatusOr<spanner::ExecutionPlan> plan = client.AnalyzeSql(
          spanner::MakeReadOnlyTransaction(),
          spanner::SqlStatement(
              "SELECT SingerId, FirstName, LastName FROM Singers"));
      if (!plan) throw std::move(plan).status();
      if (!is_partitionable(*plan)) {
        throw std::runtime_error("Query is not partitionable");
      }
    

### sys_time

**Alias Of** : `std::chrono::time_point< std::chrono::system_clock, Duration >`

Convenience alias. 

`std::chrono::sys_time` since C++20. 

### TracingOptions

**Alias Of** : `::google::cloud::TracingOptions`

The configuration parameters for RPC/protobuf tracing. 

The default options are:

  * single_line_mode=on
  * use_short_repeated_primitives=on
  * truncate_string_field_longer_than=128 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
