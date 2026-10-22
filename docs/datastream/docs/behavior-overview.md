---
url: https://docs.cloud.google.com/datastream/docs/behavior-overview/
title: Key concepts and features \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:18.974442+00:00
---

# Key concepts and features  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/behavior-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Key concepts and features Stay organized with collections  Save and categorize content based on your preferences. 

Datastream lets you ingest data from relational databases and other sources into destinations such as BigQuery, Apache Iceberg tables, and Cloud Storage in near real time. You can then use the replicated data in BigQuery for data warehousing and analytics, or run Apache Spark jobs for artificial intelligence and machine learning workloads.

## Concepts

This section describes the main concepts that you need to understand to use Datastream effectively.

### Change data capture

Change data capture (CDC) is a set of [software design patterns](https://en.wikipedia.org/wiki/Software_design_pattern) used to determine and track changed data so that applications can process the updates. CDC is also an approach to data integration that's based on the identification, capture, and delivery of changes made to enterprise data sources.

### Event sourcing

The [event sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) design pattern captures every change to a state of an application in an event object. By using event sourcing, an application can rebuild its state, perform [point-in-time recovery](https://en.wikipedia.org/wiki/Point-in-time_recovery) (by processing events up to that point), recompute state when business logic changes, or enable a [Command Query Responsibility Segregation (CQRS)](https://martinfowler.com/bliki/CQRS.html) architecture. With the evolution of tools for real-time event processing, many applications use the event sourcing model. Transactional databases are inherently event-oriented to meet [atomicity, consistency, isolation, and durability (ACID)](https://en.wikipedia.org/wiki/ACID) requirements.

### Transactional databases

In a transactional database, the set of operations that the database performs is usually written to a [write-ahead log (WAL)](https://en.wikipedia.org/wiki/Write-ahead_logging) before any operations are executed on the storage engine. After an operation is executed on the storage engine and is committed to the WAL, the operation is considered successful. Using a WAL enables atomicity and durability, and also allows high-fidelity replication of the database. Some databases write to the log the exact operation that occurs at the storage level (for example, `write 0x41 at location 20`), so those actions can be replicated only on the same storage engine. Other databases log a complete logical statement (or row) that can be re-executed on a different storage engine.

### Events and streams

Datastream ingests large volumes of data in near real time from a variety of sources and makes the data available for consumption in the destination. The unit of data stored by Datastream is an event. A stream represents the continuous ingestion of events from a source and writing them to a destination.

### Unified types

Data sources have their own data types—some specific to the database itself, and others that are generic and shared across databases. Because multiple sources generate streams to a unified destination, a standard representation of the original source type is required across all sources. The [unified type](https://docs.cloud.google.com/datastream/docs/unified-types#unitypes) is a common and lossless representation of data types across all sources so that data can be consumed cohesively. The unified types supported by Datastream represent the superset of all normalized types across supported source systems.

### Entity context

Datastream has five entities:

  * **Private connectivity configurations** enable Datastream to communicate with data sources over a secure, private network connection. This communication occurs through Virtual Private Cloud (VPC) peering.
  * **Connection profiles** represent connectivity information for a specific source or destination database.
  * **Streams** represent a source and destination connection profile pair, along with stream-specific settings.
  * **Objects** represent a portion of a stream. For example, a database stream has a data object for every table being streamed.
  * **Events** represent every data manipulation language (DML) change for a given object.



After you [create a private connectivity configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration), you can connect to sources hosted in Google Cloud or elsewhere over a private communication channel. Private connectivity is optional. Datastream also supports other modes of connectivity over public networks.

After you [create a connection profile](https://docs.cloud.google.com/datastream/docs/create-connection-profiles) for a source and a destination, you can create streams that use the information stored in the connection profiles to transfer data from the source to the destination.

After you [create a stream](https://docs.cloud.google.com/datastream/docs/create-a-stream), Datastream connects to the source directly, consumes content, and then processes and writes events to the destination based on the [event structure](https://docs.cloud.google.com/datastream/docs/events-and-streams#events).

You can manage private connectivity configurations and connection profiles separately from streams for reuse.

## Features

Features of Datastream include:

  * **Serverless:** Configure a stream and data starts moving. There is no installation, resource allocation, or maintenance overhead. As data volumes change, Datastream autoscaling capabilities automatically allocate resources to keep data moving in near real time.
  * **Unified Avro-based type schema:** Datastream enables source-independent processing by converting all source-specific data types into a unified Datastream type schema, based on Avro types.
  * **Stream historical and CDC data:** Datastream streams both historical and CDC source data simultaneously in near real time.
  * **Oracle CDC without additional licenses:** Datastream provides LogMiner-based CDC streaming from any Oracle source version 11.2 and later, without requiring additional licenses or software installations.
  * **BigQuery destination:** Changes in the source are replicated continuously to BigQuery tables in near real time. Data in BigQuery is available for analytics with minimal delay.
  * **Cloud Storage destination:** CDC data is written continuously to self-describing Avro or JSON files in Cloud Storage. This data is available for additional processing, either directly in place or by loading downstream to another destination such as Spanner.
  * **Centralized metadata management with Knowledge Catalog:** Datastream resources, such as streams, connection profiles, and connectivity configurations, are automatically synchronized with Knowledge Catalog. This lets you search for and browse these assets directly in the Knowledge Catalog user interface.



## Use cases

There are three main scenarios for using Datastream:

  * **Data integration** : Data streams from databases and software as a service (SaaS) cloud services can feed a near-real-time data integration pipeline by loading data into BigQuery.
  * **Streaming analytics** : Changes in databases are ingested into streaming pipelines that use Dataflow for fraud detection, security event processing, and anomaly detection.
  * **Near real-time availability of data changes** : Availability of data changes in near real time powers artificial intelligence and machine learning applications to prevent churn or increase engagement through marketing campaigns or by feeding data back into production systems.



## Behavior overview

Datastream lets you stream ongoing changes from multiple data sources directly into Google Cloud.

### Sources

  * Before you use a source with Datastream, you must configure authentication and additional source options.
  * Each source generates events that reflect all data manipulation language (DML) changes.
  * Each stream can backfill historical data and stream ongoing changes into the destination.



### Destinations

Datastream supports BigQuery, Apache Iceberg tables, and Cloud Storage as [destinations](https://docs.cloud.google.com/datastream/docs/destinations). When you create a stream, you define its destination configuration.

### Event delivery

  * The [event order](https://docs.cloud.google.com/datastream/docs/events-and-streams#ordering) isn't guaranteed. [Event metadata](https://docs.cloud.google.com/datastream/docs/events-and-streams#events) includes information that can be used to order the events.
  * The [event delivery](https://docs.cloud.google.com/datastream/docs/events-and-streams#consistency) occurs at least once. Event metadata includes data that can be used to remove any duplicate data in the destination.
  * The event size is limited to 20 MB per event for BigQuery destinations and 100 MB per event for Cloud Storage destinations.



To learn more about events, see Events and streams.

### High availability and disaster recovery

Datastream provides high availability across zones and manages disaster recovery during regional outages:

  * **High availability:** Datastream is a regional service, running in multiple [zones in each region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). A single-zone failure in any one region doesn't impact the availability or quality of the service in other zones.

  * **Disaster recovery:** If there's a failure in a region, then any streams running in that region are unavailable for the duration of the outage. After the outage is resolved, Datastream continues from where it stopped, and any data that hasn't been written to the destination is retrieved again from the source. In this case, duplicate data might exist in the destination. For information about removing duplicate data, see Event delivery.




### Initial data and CDC data

Because data sources have data that existed before the source connects to a stream (historical data), Datastream generates events both from the historical data and from data changes occurring in real time.

To ensure fast data access, historical data and real-time data changes are replicated simultaneously to the destination. The [event metadata](https://docs.cloud.google.com/datastream/docs/events-and-streams#events) indicates whether an event is from backfill or from CDC.

## What's next

  * Learn more about [Datastream](https://docs.cloud.google.com/datastream/docs/overview).
  * Learn about [unified types mappings](https://docs.cloud.google.com/datastream/docs/unified-types).
  * Learn about supported [sources](https://docs.cloud.google.com/datastream/docs/sources).
  * Learn about supported [destinations](https://docs.cloud.google.com/datastream/docs/destinations).
  * Create [private connectivity configurations](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration), [connection profiles](https://docs.cloud.google.com/datastream/docs/create-connection-profiles), and [streams](https://docs.cloud.google.com/datastream/docs/create-a-stream).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
