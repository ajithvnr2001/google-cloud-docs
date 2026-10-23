---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/key-concepts/
title: Key concepts \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:01.943941+00:00
---

# Key concepts  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/key-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Key concepts

This page describes the key concepts for understanding the components of Manufacturing Data Engine (MDE).

## Manufacturing data

MDE information architecture is designed to process two types of manufacturing data:

  1. **Manufacturing facts** : Sensor readings or events acquired from the factory floor or derived from factory floor data.
  2. **Context about facts (metadata)** : Origin, the way they were captured, their type, nature (the measurements they represent), assets that refer to, and provide context about them.



MDE is designed to be used as a data repository of factual and contextual manufacturing data and to capture relationships between them. The main design objective of MDE is to provide rapid data ingestion, performant data access, and enable value-added use cases.

Manufacturing data and metadata are stored in and sent to different data sinks that are optimized for specific use-cases.

To provide the flexibility in organizing and storing data, MDE defines a model that allows configurability and extensibility of logical schemas while maintaining physical data schema stability.

This diagram shows at a high level the message flow as processed by MDE:

![ingestion-logical-steps](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ingestion-logical-steps.png)

## Source message

Any message published to the `input-messages` Pub/Sub topic, which is the data entry point to MDE.

## Source message class

A group of _source messages_ that share a common structure or semantics. For more information, see [Source Message Class](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/source-message-class).

## Parser

A configuration entity that transforms messages of a specific _source message class_ into records of a specific _type_ by means of a Whistle script. A parser can produce records with differing _tags_ , but all records must share the same _type_. For more information, see [Parser](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/parser).

## Archetype

A base for a _type_ that defines specific fields and behaviors. There are six archetypes grouped in three archetype families:

  * Numeric (standard and clustered)
  * Discrete (standard and clustered)
  * Continuous (standard and clustered)



## Natural key

A key uniquely identifying an entity outside of MDE.

## Tag

An entity, such as a sensor, device, or machine emitting a stream of _source messages_. The entity is identified by a _tag name_ which also serves as the _natural key_ in tag cloud tag metadata buckets. Configuration settings can be attached to tags in the context of _type_ versions. For more information, see [Tag](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/tag).

## Type

A configuration entity describing a common set of _records_. A _type_ is associated to exactly one _archetype_. A _type_ may be associated with one or more _metadata buckets_ , it may hold a _data field_ schema, and provide _storage specifications_. For more information, see [Type](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/type).

## Data field

A field in a record. The object written to the field can be constrained by schema on _types_ of Discrete and Continuous _archetype_.

## Metadata bucket

A configuration entity that models a related set of contextual information about a manufacturing fact (such as a sensor reading) associated with a _source message_. _Metadata buckets_ are modeled as dimensions in the analytics domain. Buckets contain schemas that define the structure of _metadata instances_ contained within them. Changes to _metadata instances_ within a bucket are versioned. For more information, see [Metadata buckets](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/metadata#metadata_buckets).

## Metadata instance

An entry within a _metadata bucket_ that describes an entity with a given _natural key_. For more information, see [Metadata instances](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/metadata#metadata_instances).

## Proto metadata instance

A _metadata instance_ that is constructed in the parser.

## Record table

A table in BigQuery tied to a _type_. Each _type_ is associated to one _record table_.

## Record

A single processed record. Also a row in a _record table_. All records share the same _type_.

## Proto record

A precursor record that is constructed and emitted by a _parser_.

## Embedded Metadata

A field that stores rapidly changing metadata in the _record_. For more information, see [Embedded Metadata](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/metadata#embedded_metadata).

## Cloud metadata reference

A field in a _record_ that stores metadata instance identifiers per bucket (foreign keys).

## Materialized metadata

A field in a _record_ that stores materialized metadata instances listed in _cloud metadata reference_.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
