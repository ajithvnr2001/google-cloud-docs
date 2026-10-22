---
url: https://docs.cloud.google.com/firestore/native/docs/editions-overview/
title: Firestore editions overview \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:28:07.145214+00:00
---

# Firestore editions overview  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/editions-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Firestore editions overview

This page describes Firestore editions and key features.

Firestore is available in the following editions:

  * **Enterprise edition** : provides the most advanced Firestore capabilities, maximizing developer flexibility and control. It supports the Firestore with MongoDB compatibility API along with the Firestore APIs and Firebase SDKs to perform real-time and offline queries.

Enterprise edition features an advanced query engine with over 180 capabilities, customizable indexing options, and up to five times faster performance. The Enterprise edition utilizes a modern pricing model based on tranches of bytes read and written, storage consumed, and network egress incurred.

  * **Standard edition** : provides the core Firestore capabilities including a standard query engine, automated indexing to help performance, and Firebase SDKs with real-time synchronization and offline queries. Standard edition utilizes a simplified pricing model based on documents read and written, storage consumed, and network egress incurred.




## Editions features

The following table summarizes the features available for each edition:

|  **Enterprise** |  **Standard**  
---|---|---  
Query Engine |  Advanced query engine

  * More than 180 stages and operators, including support for aggregations, arithmetic, arrays, sets, type conversions, and joining data.
  * You can perform queries with or without an index.

|  Standard query engine

  * Standard query capabilities for basic comparisons and matches.
  * All queries require covered indexes.

  
Document Size Limits | 

  * 16 MiB with MongoDB compatibility
  * 1 MiB with Firestore in Native mode

|  1 MiB  
Supports Firestore with MongoDB compatibility | Yes |  No  
Supports Firestore in Native mode: server-side, web, and mobile SDKs with real-time and offline support | Yes |  Yes  
Indexing | Fully customizable, with support for advanced indexes like unique, dense, and sparse. | Automatic, basic indexing on all document fields  
Text search | Yes (Preview) | No  
Geospatial search | Yes (Preview) | No  
Change data capture | Triggers | Triggers  
Observability | 

  * Cloud Monitoring
  * Query Explain
  * Query Insights
  * Database Center

| 

  * Cloud Monitoring
  * Query Explain
  * Query Insights
  * Database Center

  
Data protection | 

  * Scheduled backups
  * Point-in-time recovery

| 
* Scheduled backups
* Point-in-time recovery  
Encryption | 

  * Google-owned and Google-managed encryption key
  * Customer-managed encryption keys

| 

  * Google-owned and Google-managed encryption key
  * Customer-managed encryption keys

  
Storage | SSD | Hybrid storage (SSD & HDD)  
Performance | Best | Good  
Committed Use Discounts |  20% for 1 year; 40% for 3 years |  20% for 1 year; 40% for 3 years  
  
## Data access modes

Firestore supports the following data access modes to read and write data:

  * **Firestore with MongoDB compatibility mode** : this interface supports Firestore with MongoDB compatibility and lets you re-use existing MongoDB drivers, tools, and open-source ecosystem integrations with Firestore.
  * **Firestore in Native mode** : this interface supports all of the latest and most innovative capabilities of Firestore, including real-time synchronization and offline caching in the Firestore client libraries.
  * **Firestore in Datastore mode** : this interface is best utilized by Datastore and App Engine Datastore apps.



### Data access modes that each edition supports

Available data access modes depend on the edition of the database. You must select a data access mode when you create the database. You can't change this mode.

  * **Firestore Enterprise edition** : supports the MongoDB compatibility APIs or the Firestore in Native mode API.
  * **Firestore Standard edition** : supports the Firestore Native API or the Datastore API.



## Maximize performance

Firestore Enterprise edition is ideal for applications that require maximum performance. Firestore Enterprise edition offers up to five times improved performance over Standard edition performance, especially at tail latencies. This gain is primarily due to the advanced query engine and faster SSD-based storage.

## Maximize scaling

Firestore Enterprise edition is able to better handle bursty network traffic at a rate up to 8x higher than Standard edition.

## Pricing

For more information about Firestore editions pricing, see [Firestore Enterprise edition pricing](https://cloud.google.com/firestore/enterprise/pricing) and [Firestore Standard edition pricing](https://cloud.google.com/firestore/pricing). Both Firestore edition pricing models are based on operations conducted, storage consumed, and network egress incurred. Firestore Enterprise edition measures operations conducted using tranches of bytes read and written whereas Standard edition measures the number of documents read or written.

You can get started on Firestore in either edition with daily free usage.

## Mix and match editions in a project

You can create both Firestore Enterprise edition and Standard edition databases in the same project.

## Migrate data between editions

To try the advanced query engine and other Enterprise edition features, create a new Enterprise edition database. Firestore data is compatible with both edition. To migrate data between editions, see [Migrate from Standard edition to Enterprise edition](https://docs.cloud.google.com/firestore/native/docs/migrate-standard-to-enterprise).

## What's next

  * [Learn about client libraries for Firestore in Native mode.](https://docs.cloud.google.com/firestore/native/docs/reference/libraries)
  * For apps that use the Datastore API, see [Firestore in Datastore mode](https://docs.cloud.google.com/datastore/docs/firestore-or-datastore).
  * [Learn how to create a Firestore with MongoDB compatibility database and connect to it with the mongosh tool](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/create-and-query-database).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
