---
url: https://docs.cloud.google.com/datastream/docs/sources-mongodb/
title: Stream data from MongoDB databases \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:29.225345+00:00
---

# Stream data from MongoDB databases  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/sources-mongodb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Stream data from MongoDB databases Stay organized with collections  Save and categorize content based on your preferences. 

Datastream supports replicating change events from a MongoDB source. MongoDB is an open source, NoSQL database that uses JSON-like documents. One document can have other documents embedded in it. The documents are gathered together in collections, and a MongoDB database stores one or more collections of documents.

Instead of storing data in tables of rows and columns like relational SQL databases, each record in a MongoDB database is a document described in binary JSON (BSON), a binary representation of data. Applications can then retrieve this data in JSON format.

This page contains information about:

  * The key terms that you need to understand when replicating from a MongoDB database
  * The behavior of how Datastream handles data that's being pulled from a source MongoDB database
  * The versions and editions of MongoDB that Datastream supports
  * Known limitations for using MongoDB as a source



## Key terms

The following are the key terms that you need to understand when working with MongoDB sources:

  * **SRV connection** : a connection string with a hostname that corresponds to a domain name service (DNS) service record (SRV). The string has the following format:

`mongodb+srv://[username:password@]host[/[defaultauthdb][?options]]`

For more information, see the [MongoDB documentation](https://www.mongodb.com/docs/manual/reference/connection-string/#srv-connection-format).

  * **Standard connection string** : the standard format of the MongoDB connection URI used to connect to a self-hosted MongoDB standalone deployment, replica set, or sharded cluster. The string has the following format:

`mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]`

For more information, see the [MongoDB documentation](https://www.mongodb.com/docs/manual/reference/connection-string/#standard-connection-string-format).

  * **Replica set** : a cluster of MongoDB servers that implements replication and automated failover. Replica sets provide redundancy and high availability, and are the basis for all production deployments.

  * **Sharded cluster** : a MongoDB sharded cluster consists of shards, mongos and configuration servers. MongoDB shards data at the collection level, distributing the collection data across the shards in the cluster.

  * **mongos** : the interface between the client applications and the sharded cluster. `mongos` act as a query router and write operations to shards.

  * **Collection** : MongoDB organizes data in a hierarchical structure. A MongoDB deployment contains one or more databases, and each database contains one or more collections. In each collection, MongoDB stores data as documents that contain field and value pairs. Collections are analogous to tables in relational databases. 




## Behavior

The source MongoDB database relies upon change streams to replicate changes to the destination. Change streams let you access real-time data and are supported for replica sets and sharded clusters.

  * If configured, all historical data is replicated for included objects.
  * All changes, such as inserts, updates, and deletes from the specified objects are replicated.



## Versions

Datastream supports MongoDB versions later than 5.0.

## Known limitations

Known limitations for using MongoDB as a source include:

  * When using the Datastream API, you can only specify what fields you want to exclude in your stream. Specifying an include list for fields isn't supported.
  * Strict mode doesn't support the `Infinity`, `-Infinity`, and `NaN` numeric values. Documents are discarded if they contain these values in strict mode. If your database contains these values, use canonical mode (default). For more information, see [MongoDB data types](https://docs.cloud.google.com/datastream/docs/bq-map-data-types#mongodb-data-types).
  * Datastream doesn't support Request Unit (RU)-based Azure Cosmos DB.
  * Datastream doesn't support Amazon DocumentDB Elastic Clusters.



## What's next

  * Learn how to [configure a MongoDB source](https://docs.cloud.google.com/datastream/docs/configure-mongodb) for use with Datastream.
  * Learn how to [create a MongoDB stream using the API and gcloud CLI](https://docs.cloud.google.com/datastream/docs/manage-streams#createastream-mongodb-strict).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
