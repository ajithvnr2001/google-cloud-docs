---
url: https://docs.cloud.google.com/bigtable/docs/cloud-bigtable-for-aerospike-users/
title: Bigtable for Aerospike users \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:18.122723+00:00
---

# Bigtable for Aerospike users  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/cloud-bigtable-for-aerospike-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback 

#  Bigtable for Aerospike users Stay organized with collections  Save and categorize content based on your preferences. 

This document helps software developers and database administrators migrate existing Aerospike applications with Bigtable as a database. It uses your knowledge of Aerospike to describe concepts that you need to understand before migrating to Bigtable.

To help you start working with Bigtable and Aerospike, this document does the following:

  * Compares the terminology between Aerospike and Bigtable.
  * Provides an overview of Bigtable operations and describes the data layout within Bigtable.
  * Explains data modeling and key design considerations.
  * Clarifies how replication is accomplished and what its impact is.



For information about the migration process and open-source tools that you can use to complete your migration, see [Migrate from Aerospike to Bigtable](https://docs.cloud.google.com/bigtable/docs/migrate-aerospike-to-bigtable).

## Terminology comparison

Aerospike and Bigtable are both distributed NoSQL databases, but they differ significantly in their design, operation, and terminology.

Aerospike stores data in records. Each record contains one or more named bins, along with metadata such as record size (in bytes), time to live (TTL), and the last update time (LUT).

Bigtable stores data in scalable tables, each of which is a sorted key-value map. The table is composed of rows indexed by row keys and columns identified by a column qualifier. Related columns can form a column family. This structure lets you store multiple versions of a value under the same key. Each version is identified by a unique timestamp. Earlier versions can be filtered during read operations or removed through garbage collection based on the configured policies.

For more information, see [Bigtable storage model](https://docs.cloud.google.com/bigtable/docs/overview#storage-model).

The following table outlines and describes shared concepts and the corresponding terminology that each product uses:

**Aerospike** | **Bigtable**  
---|---  
No directly corresponding item. | **instance** : a managed group of clusters in different Google Cloud zones or regions between which replication and connection routing occur.  
**cluster** : an Aerospike deployment consisting of a collection of nodes. | **cluster** : a group of nodes in the same geographic Google Cloud zones.  
**node** : a server providing compute and owning its storage. | **node** : a server providing compute only. Storage is handled by [Colossus](https://cloud.google.com/blog/products/bigquery/bigquery-under-the-hood?e=48754805), a separate distributed file system.  
**namespace** : stores parameters like TTL or storage type. Within a namespace, data is subdivided into sets and records. | **table** : the closest equivalent to an Aerospike namespace. Some parameters are set for all tables at cluster level. Finer control is possible at table or column family level.  
**set** : used for logical division of records and parameters like TTL and capping size. Keys have to be unique within a set. | No directly corresponding item.  
No directly corresponding item. | **table** : an instance-level resource that is automatically replicated to every cluster. A table contains a set of values identified by unique row keys. Tables are sparse, which means they don't use extra space to store columns that don't contain any values.  
No directly corresponding item. | **tablet** : a contiguous range of rows stored together. Bigtable uses tablets for load balancing by assigning them to nodes. Tablet boundaries are dynamic—they can split or merge over time.  
**record** : a set of named bins used to store data. It can be at most 8 MB. | **row** : a set of values identified by column family, column qualifier, timestamp. All operations are atomic at the row level.  
No directly corresponding item. | **column family** : a group of columns sorted in lexicographic order. Garbage collection is set at this level.  
**bin** : a key-value pair where the bin name is the identifier of a value within a record. | **column qualifier** : a label for a value stored in a table.  
No directly corresponding item. | **cell** : a label for a timestamped value stored in a table.  
**(record) digest** : a hash of a three-tuple identifying a record: namespace, set, and key. | No directly corresponding item.   
**Note** : During migration, record digests are used as row keys in Bigtable. For more information, see Row key design.  
**record Last Update Time (LUT)** : a timestamp of the last write to a record. | **cell timestamp** : a timestamped version of the value for the intersection of a row and a column that has multiple cells.  
**key** : a record identifier unique within a set. | **row key** : a row identifier, unique within a table.  
**AQL** : a command-line tool for browsing data and developing user-defined functions for the Aerospike database. | **GoogleSQL** : a query language used by multiple Google Cloud services, including Spanner, BigQuery, and Bigtable.  
  
## Data types limits

The following table compares the limits for data types used by Aerospike and Bigtable:

**Aerospike** | **Bigtable**  
---|---  
**namespace** : The maximum number of namespaces for the [ Enterprise Edition](https://aerospike.com/products/features-and-editions) is 32. | **table** : An instance can have up to 1,000 tables. A table name can't exceed 50 characters.  
**set** : A cluster can have up to 4,095 sets. A set name can't exceed 63 bytes. | No directly corresponding item.  
**record** : The maximum record size is 8 MB. | **row** : The maximum row size is 256 MB.  
No directly corresponding item. | **column family** : The number of column families is unlimited, however more than 100 can cause performance degradation.  
**bin** : The number of bins is unlimited, however, each bin can hold not more than 1 MB of data. The bin name can't exceed 15 bytes. | **column qualifier** : The limit is 100 MB, but it is recommended not to exceed 10 MB. The number of columns is unlimited.  
**key** : The maximum key size is 8 KB. | **row key** : The maximum row key size is 4 KB.  
  
For more information about Bigtable limits, see [Quotas and limits](https://docs.cloud.google.com/bigtable/quotas). For more information about Aerospike limits, see [Aerospike system limits and thresholds](https://aerospike.com/docs/database/reference/limitations/).

## Architecture

The following sections provide an architectural overview of Bigtable and Aerospike.

### Bigtable

Bigtable nodes are separate from the storage layer, which means nodes don't affect data durability. Bigtable table clients are not aware of the underlying data distribution. An additional routing layer distributes requests to the correct node. Each node handles a subset of the requests to the cluster. A Bigtable table is sharded into blocks of contiguous rows, called tablets, which are stored on Colossus, a distributed file system that provides high durability. Each tablet is associated with a specific Bigtable node.

![Clients in the Bigtable cluster communicate with the nodes through the routing layer that distributes the data to the correct node.](https://docs.cloud.google.com/static/bigtable/img/cloud-bigtable-for-aerospike-users-bigtable-storage-architecture.svg)

Bigtable's architecture provides the following benefits:

  * Bigtable clients don't need to be aware of the data distribution and load balancing. Such complexities are handled by the routing layer.
  * Rebalancing happens very quickly and the recovery from failure is fast because the actual data is not copied between nodes.
  * When a Bigtable node fails, no data is lost.



### Aerospike

Unlike Bigtable, Aerospike storage is located on the nodes that serve it. Every node (a server) in the Aerospike cluster is identical. The data in each namespace is divided into exactly 4,096 partitions by hashing record names. These partitions are evenly distributed between nodes.

The nodes are aware of each other and rebalance stored partitions when the cluster changes. Each time a cluster change happens, replicas elect a primary replica that coordinates the rebalancing. The client libraries are expected to track which replica stores the primary partition and send write requests to the right replicas. If a client sends a request to the wrong node (this can happen during rebalancing), the request is rerouted by the nodes.

![Clients in Aerospike cluster communicate with the nodes that handle workload rebalancing](https://docs.cloud.google.com/static/bigtable/img/cloud-bigtable-for-aerospike-users-aerospike-storage-architecture.svg)

## Replication

This section compares the replication process for Aerospike and Bigtable.

### Bigtable

A Bigtable instance can consist of a single cluster or multiple [replicated clusters](https://docs.cloud.google.com/bigtable/docs/replication-overview#how-it-works). A table is always replicated to all clusters within an instance. Clusters can be added or removed from an instance with minimal impact to other clusters.

Bigtable provides read-your-writes consistency within a single cluster. Writes are performed on a single cluster and become eventually consistent across other clusters in the instance. Unlike Aerospike, Bigtable doesn't lose intermediate updates because individual cells are internally versioned, ensuring no writes are lost. Each cluster serves the cells that have the most current timestamps available.

The Bigtable API offers a table-level consistency token, which can be used to verify whether all changes made prior to the token creation were replicated completely.

### Aerospike

Aerospike handles replication within a cluster at the partition level. A namespace is split into partitions that are evenly distributed between nodes. Strong consistency is ensured within a cluster. A write operation is confirmed only after all replicas within the cluster have acknowledged it.

[Cross data center replication (XDR)](https://aerospike.com/docs/database/learn/architecture/xdr/) can be configured for data synchronization between different clusters. Aerospike bin convergence ensures that the data is eventually the same in all the data centers at the end of replication. However, [intermediate updates can be lost](https://aerospike.com/docs/server/architecture/xdr#limitations-of-xdr:%7E:text=intermediate%20updates%20can%20be%20lost).

For durability, Aerospike's roster-based consistency algorithm requires N+1 copies to handle N failures.

## Data model

This section compares the data models used by Bigtable and Aerospike.

### Flexible schema

Aerospike doesn't enforce schema constraints, allowing each record to have different bins with varying value types. Similarly, Bigtable supports sparse columns, so no storage is consumed for columns without values. While there is no strict limit on the number of columns or column families, keep the number of column families under 100 for performance reasons.

### Row key design

Bigtable identifies rows by row keys which must be unique within a table. They are sorted lexicographically and kept together in tablets. This differs from Aerospike, where records are distributed across nodes based on their hash. Row keys should be designed to ensure that rows frequently accessed together are also stored together.

During [migration](https://docs.cloud.google.com/bigtable/docs/migrate-aerospike-to-bigtable),Bigtable uses Aerospike record digests as row keys for the following reasons:

  * Aerospike doesn't persist user keys by default. Depending on the configuration, Aerospike restricts the migration to deployments that enabled key storage before any data was written. Enabling key storage later in the process doesn't retroactively populate keys.
  * Aerospike record keys can reach 8 KB, while Bigtable row keys are limited to 4 KB, making direct reuse unsafe.



### Data types

Aerospike supports advanced data types, including scalars, GeoJSON, HyperLogLogs, lists, and nested objects. These types can be indexed and queried with support of secondary indexes. In addition, Aerospike provides server-side APIs that allow complex operations on these data types, such as filtering by geolocation or manipulating list contents.

The Cloud Bigtable API primarily handles raw bytes, with a few exceptions. It uses INT64 for timestamps and counters, which you can increment atomically. The query language also supports many complex types, such as scalars, JSON objects, and HLL bins. Because you can't store advanced types directly in Bigtable, you must serialize all data on the client side. The [adapter library](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem/tree/main/aerospike-bigtable-migration-tools/adapter/) can help you with serialization.

#### Type mapping

During the migration from Aerospike to Bigtable, the adapter library helps maintain Aerospike types even if Bigtable doesn't support them.

Aerospike stores typed values such as scalars, lists, or maps, whereas Bigtable returns cells without application-level type semantics, requiring an adapter layer for type recovery. The adapter library provides the following encoding:

  * Each scalar bin is serialized with HBase-compatible routines and a type marker embedded in the column qualifier.
  * Complex bins, such as lists or maps, are split into separate columns.
  * A column qualifier encodes list position or escaped map key and the scalar type.



Decoding logic reconstructs the original structures, yielding behavior consistent with Aerospike. The adapter library also supports nested structures.

The following examples illustrate how Aerospike records are mapped to Bigtable rows:

Data type | Aerospike record | Bigtable row  
---|---|---  
**Scalars** |  `integerBin`: 1  
`floatBin`: 2.2  
`stringBin`: "abc"  | 
    
    
    <record's digest>:
      SCALARS:floatBin__FLOAT64
        "@\x01\x99\x99\x99\x99\x99\x9a"
      SCALARS:integerBin__INT64
        "\x00\x00\x00\x00\x00\x00\x00\x01"
      SCALARS:stringBin__STRING
        "abc"  
  
**Objects** |  `listBin`: `[1,2]`  
`mapBin`: `{"x": 1}` | 
    
    
    <record's digest>:
      OBJECT:listBin__LIST__0__INT64
        "\x00\x00\x00\x00\x00\x00\x00\x01"
      OBJECT:listBin__LIST__1__INT64
        "\x00\x00\x00\x00\x00\x00\x00\x02"
      OBJECT:mapBin__MAP__x__INT64
        "\x00\x00\x00\x00\x00\x00\x00\x01"  
  
### Column family

In Bigtable, column families define which columns in a table are stored and retrieved together, and at least one column family must exist for each table. Group related columns into the same family and separate data with different retention requirements into distinct column families, because garbage collection policies apply at the column family level.

#### Time to live (TTL)

In Aerospike, you can define time to live (TTL) at the record level. In Bigtable, you configure TTL at the column family level, though [you can simulate per-cell TTL](https://docs.cloud.google.com/bigtable/docs/gc-cell-level). After migration, timestamps in Bigtable don't directly correspond to Aerospike LUTs. If your application uses TTL in Aerospike and requires the same behavior after migration, you must choose between column-family-level TTL and simulated per-cell TTL. Depending on your decision, you must set timestamps for all cells accordingly.

Unlike Aerospike, which excludes expired records from reads, Bigtable might continue to return them until garbage collection removes them. To match Aerospike's behavior, apply read filters to exclude expired records.

### Column qualifiers

In Bigtable, column qualifiers are used within a column family to define individual columns. Tables can support millions of columns, however, best practice is to limit the number of columns in a single row. Optionally, column qualifiers can be treated as data, allowing values to be embedded directly in the column name to save space.

### Cells

In Bigtable, a cell is the intersection of the row key and column name (a column family combined with a column qualifier). Each cell contains one or more timestamped values that can be supplied by the client or automatically applied by the service.

### Secondary indexes

Continuous materialized views can act as asynchronous secondary indexes, enabling tables to be queried using different lookup patterns or attributes. For more information, see [Create an asynchronous secondary index](https://docs.cloud.google.com/bigtable/docs/asynchronous-secondary-index).

## Transactions

Bigtable and Aerospike both lack support for multi-row transactions but differ in their single-row capabilities. Bigtable provides fully consistent single-row writes within a cluster and supports single-row transactions through mutate-row requests. They allow multiple operations on a single row, all executed atomically and either all succeed or all fail. Additionally, there are read-modify-write and check-and-mutate operations, though these are not available with multi-cluster routing profiles. In contrast, Aerospike extends single-row transactions with server-side data manipulation and execution of client defined functions.

## Load balancing and failover

[Aerospike client API](https://aerospike.com/docs/database/learn/architecture/clients) handles load balancing. This client-side process is aware of cluster state and data distribution, and is responsible for routing requests.

If a node fails or a new node is added, the cluster must be rebalanced. A temporary primary is chosen to orchestrate the act of rebalancing and redistributing the partitions between the nodes. While that happens, the cluster remains operational, but the client has to track the changes for request routing. If a request reaches the wrong node, it is routed internally to the correct one.

The Bigtable client is a _thin client_ , hiding all complexities like cluster state and data distribution from the user. Routing the request is handled by the next layer, a _thick client_ inside the Google Cloud Bigtable infrastructure.

Another difference is the routing policy which is not available in Aerospike. Bigtable uses application profiles to manage request routing, with configurable priorities to control the order in which requests are served. There are two types of routing policies: single-cluster and multi-cluster. A multi-cluster profile routes operations to the closest available cluster. Clusters in the same region are considered to be equidistant from the perspective of the operation router. If the node that's responsible for the requested key range is overloaded or temporarily unavailable in a cluster, this profile provides automatic failover. In contrast, Aerospike doesn't provide automatic failover in the event of a complete cluster failure.

## Backup and restore

Aerospike provides external backup and restore tools called [`asbackup`](https://aerospike.com/docs/database/tools/asbackup/) and [`asrestore`](https://aerospike.com/docs/database/tools/asrestore/) that create logical backups client side and are analogous to performing a scan. Backup management can also be handled through the Aerospike Backup Service or Aerospike Kubernetes Operator, both of which use `asbackup` and `asrestore` internally, and provide scheduling and multi-process coordination. Backups are not atomic, meaning write operations occurring during the backup may not be captured.

Bigtable provides two methods to cover common backup needs: [Bigtable backups](https://docs.cloud.google.com/bigtable/docs/backups) and managed data exports. Backups create restorable copies of a table which are stored as member objects of a cluster. You can restore backups as a new table in the cluster that initiated the backup. The backups are designed to create restore points if application-level corruption occurs. Bigtable backups are also not atomic. Changes might be made in a section of the table that the backup has already copied.

### Key differences in backup handling

  * Aerospike backups are created client-side. They don't require any additional space server-side, but they are slower. In Bigtable, a backup shares physical storage with the source table and other backups of the table.
  * Aerospike users must handle exporting, storing, and removing stale backups. Because backups in Bigtable are fully integrated, all these actions are taken care of automatically by the Bigtable service.



## Performance considerations

Because Aerospike and Bigtable treat read and write operations differently, they have performance differences which are important to consider. The following table includes several examples of performance differences between the two databases. For more information, see the [Bigtable performance guidelines](https://docs.cloud.google.com/bigtable/docs/performance).

Consideration | Bigtable | Aerospike  
---|---|---  
**Hot rows** | Distributes tablets and operations to equalize resource usage. A frequently accessed row can be isolated to a single-row tablet on one node, limiting impact on other rows. | Distributes rows based on hashes across all nodes, regardless of traffic. A hot row can affect the performance of an entire partition.  
**Scans over sorted keys** | Stores data lexicographically, making it highly effective for streaming sorted data. | Distributes records based on hashes, so scanning many consecutive keys requires querying multiple nodes and aggregating results, which can be slower. Supports secondary indexes, including advanced types, which might reduce the need for scans.  
**Inserting many consecutive keys** | Stores data lexicographically, meaning a single node handles many consecutive key write operations. As a result, a read or write pattern can end up on the node holding the tablet responsible for the end of the row key space, effectively overloading it. | Distributes keys based on hash, distributing the load among multiple nodes when writing consecutive keys.  
**Rows with a very large number of columns** | While Bigtable can support rows up to 256 MB, processing large rows can impact performance. Bigtable is optimized for smaller rows. Therefore, consider cell organization and access to data during schema design to avoid unnecessarily spreading data across many cells. | Performs suboptimally when encountering a row or record with a very large number of columns or bins.  
**Cold starts** | Performs best with large tables that are frequently accessed. If you start sending requests after a period of no usage (a cold start), you might observe high latency. This happens because the split into tablets and their distribution between nodes might not be optimal and because the caches are cold. The distribution between nodes might not be fully optimal until a few minutes during cold start and during rebalancing. | Performance doesn't change over time as data distribution is not load-based. While caches need warming, indexes are kept in memory, minimizing disk search time and reducing caching importance.  
**Many small tables** | Avoid creating many small tables. Separate tables are justified for different use cases or schemas, but not for similar data, as it doesn't improve load balancing and increases management overhead. | Most records reside in one namespace, grouped into sets. Sets don't have specific schemas, but secondary indexes or scan operations can be set per set. Splitting data into sets doesn't affect performance.  
**Large dataset** | Capable of storing exabyte-scale datasets. Performance is unaffected by total dataset size due to its architecture and dynamic tablet splitting. | Technically, Aerospike databases don't have a size limit, however, Aerospike stores indexes and records separately. Both kinds of data can be stored on [ different types of storage devices](https://aerospike.com/docs/database/learn/architecture/hybrid-storage) to increase performance. Storing indexes in RAM is essential for low latencies, but it might not be feasible for very large datasets. For example, with 4 billion objects and a replication factor of 2 (RF2), the memory consumed in association with the primary index across the cluster in All Flash is 2.5 GiB. Using the same example in a Hybrid Memory configuration, where the primary index is in memory, 476.8 GiB of memory would be used.  
**Scaling** | Processing and storage are decoupled and can be scaled independently. A single node can handle data chunks of several hundred terabytes or even petabytes. | Storing indexes in RAM is essential for low latencies. In such a case, machines have to be scaled vertically together with storage capacity to account for the primary index.  
  
## What's next

  * Read about [Bigtable schema design](https://docs.cloud.google.com/bigtable/docs/schema-design).
  * Find out more about [Aerospike](https://aerospike.com/).
  * Learn about the [Bigtable emulator](https://docs.cloud.google.com/bigtable/docs/emulator).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
