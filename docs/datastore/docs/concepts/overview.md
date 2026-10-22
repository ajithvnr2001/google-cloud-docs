---
url: https://docs.cloud.google.com/datastore/docs/concepts/overview/
title: Datastore overview \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:19.525059+00:00
---

# Datastore overview  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/concepts/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Guides ](https://docs.cloud.google.com/datastore/docs/concepts/overview)



Send feedback 

#  Datastore overview Stay organized with collections  Save and categorize content based on your preferences. 

Datastore is no longer offered as a standalone database product. [Firestore](https://cloud.google.com/products/firestore) is the successor to Datastore. To continue to support legacy App Engine applications built on Datastore, Firestore offers a backwards-compatible Datastore API. Firestore provides all the Datastore capabilities, performance and scalability characteristics without any compromises, including: 

  * **Atomic transactions** : execute a set of operations where either all succeed, or none occur.
  * **High availability of reads and writes** : databases run in Google data centers which use redundancy to minimize impact from points of failure.
  * **Massive scalability with high performance** : a distributed architecture automatically manages scaling and maintains performance under heavy loads.
  * **Flexible storage and querying of data** : document data model maps naturally to object-oriented and scripting languages, and is exposed to applications through multiple clients. Firestore's Datastore compatible API also provides a SQL-like [query language](https://docs.cloud.google.com/datastore/docs/apis/gql/gql_reference).
  * **Strong consistency** : queries are strongly consistent.
  * **Encryption at rest** : data is automatically encrypted before it is written to disk and automatically decrypted when read by an authorized user. For more information, see [Server-Side Encryption](https://docs.cloud.google.com/datastore/docs/concepts/encryption-at-rest).
  * **Fully managed with no planned downtime** : Google handles the administration of the service so you can focus on your application. Your application can still use Firestore when the service receives a planned upgrade.



## Comparison with relational databases

While the Datastore interface has many of the same features similar to relational databases, as a NoSQL database, it varies in how it describes the relationships between data objects. Here's a high-level comparison of Datastore and relational database concepts:

Concept | Datastore | Firestore | Relational database  
---|---|---|---  
Category of object | Kind | Collection group | Table  
One object | Entity | Document | Row  
Individual data for an object | Property | Field | Column  
Unique ID for an object | Key | Document ID | Primary key  
  
Unlike rows in a relational database table, Datastore entities of the same kind can have different properties, and different entities can have properties with the same name but different value types. You can use these unique characteristics to design and manage data to scale automatically.

Because all queries are served by previously built indexes, the types of queries that the Datastore API can execute are more restrictive than those allowed on a relational database with SQL. In particular, Datastore doesn't include support for join operations, inequality filtering on multiple properties, or filtering on data based on results of a subquery. If your application requires advanced query capabilities including joins and subqueries, consider using the [Firestore Native API or the MongoDB-compatible API](https://docs.cloud.google.com/firestore/native/docs/overview).

Unlike relational databases which enforce a schema, Datastore is schemaless. It doesn't require entities of the same kind to have a consistent set of properties (although you can choose to enforce such a requirement in your own application code).

## Other storage and database options

Firestore's Datastore compatible API is intended to support legacy App Engine applications. If you're looking for a document-oriented NoSQL database for a new application, we recommended that you use one of the Firestore APIs instead of the Datastore API to take advantage of more advanced capabilities. [Learn more about your options](https://docs.cloud.google.com/firestore/native/docs/overview).

Firestore is a highly scalable document database which may not be ideal for every use case. For example, it may not be the best replacement for a relational database. Here are some common scenarios where you might consider an alternative database:

  * If you need a relational database with full SQL support for an online transaction processing (OLTP) system, consider [Cloud SQL](https://docs.cloud.google.com/sql).
  * If you don't require support for ACID transactions or if your data is not highly structured, consider [Bigtable](https://docs.cloud.google.com/bigtable).
  * If you need interactive querying in an online analytical processing (OLAP) system, consider [BigQuery](https://docs.cloud.google.com/bigquery).
  * If you need to store large immutable blobs, such as large images or movies, consider [Cloud Storage](https://docs.cloud.google.com/storage).



For more information about other database options, see the [overview of database services](https://cloud.google.com/products/databases/). 

## What's next

  * [Learn how to store and query data using the Google Cloud console](https://docs.cloud.google.com/datastore/docs/store-query-data)
  * [Learn about the Datastore data model](https://docs.cloud.google.com/datastore/docs/concepts/entities)
  * [View best practices for Datastore](https://docs.cloud.google.com/datastore/docs/best-practices)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
