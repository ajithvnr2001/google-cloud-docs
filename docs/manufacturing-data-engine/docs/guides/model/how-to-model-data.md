---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/model/how-to-model-data/
title: Model records and metadata \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:20.864689+00:00
---

# Model records and metadata  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/model/how-to-model-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Model records and metadata

This guide describes how to model records and metadata in Manufacturing Data Engine (MDE).

Records capture facts about the manufacturing process, such as sensor readings and events, and metadata helps contextualize those facts and lets you 'slice and dice' them by metadata attributes. Metadata also serves as source of original data of manufacturing entities.

If you use the full MDE suite (MDE in combination with Manufacturing Connect (MC)), you can skip this section on data modeling since MDE provides a package to get you started quickly. However, it might be worth to read it if you are integrating other data sources.

## General recommendations

Before starting with metadata modeling, you should understand the following:

  * **The data consumption needs of downstream users**. This includes understanding what data they need and how they plan to use it. You can do this by meeting with downstream users to ask about their objectives, key performance indicators (KPIs), use cases, analytics requirements, and data quality standards.
  * **The realities of the underlying source data**. This includes understanding the quality of the data, the data structure, and the data lineage. You can do this by meeting with source system experts and doing high-level data profiling.
  * **The technical data integration requirements**. This includes understanding what data integration interfaces MDE needs to support and what technical requirements must be observed, including naming conventions.



The following are some specific things you can do to understand the consumption needs of downstream users:

  * **Meet with downstream users to understand their objectives** : 
    * What are they trying to achieve with the data?
    * What are their KPIs?
  * **Ask downstream users about their use cases** : 
    * How do they plan to use the data?
    * What reports do they want to run?
    * What analysis do they want to perform?
  * **Understand downstream users' analytics requirements** : 
    * What kind of data do they need to analyze?
    * How often do they need to analyze the data?
  * **Ask downstream users about their data quality standards** : 
    * What level of data quality is acceptable to them?
    * What steps need to be taken to ensure that the data meets their standards?



Here are some specific things you can do to understand the realities of the underlying source data:

  * **Meet with source system experts** : 
    * What is the quality of the data in the source systems?
    * What is the data structure?
    * What is the data lineage?
  * **Do a high-level data profiling** : 
    * This will help you to identify any potential problems with the data, such as missing values, duplicate records, or invalid data types.



## Metadata modeling

When modeling metadata, you face three key questions:

  1. What metadata should be treated as embedded metadata and what metadata should be treated as cloud metadata?
  2. For cloud metadata, what buckets to create?
  3. What should be the schema for cloud metadata buckets?



### Deciding between embedded versus cloud metadata

The key decision criteria to apply when deciding whether some contextual information should be modelled as embedded metadata or cloud metadata is the pace of change.

Embedded metadata is best suited for metadata that changes rapidly. This includes metadata like transaction IDs or auto-incremented counters.

In contrast, cloud metadata is best used for metadata that changes at a slower pace, for example, asset metadata. MDE keeps track of the history of metadata instances per bucket and writes that metadata to sinks that support it, such as BigQuery. This lets you explore the history of metadata instances per natural key, while also allows business intelligence (BI) tools such as Looker to obtain a unique list of attribute values without traversing the entire record table.

### Modeling cloud metadata buckets

Buckets model some contextual domain. For example, an implementation of ISA-95 asset hierarchy models the physical asset hierarchy of a manufacturing enterprise. You should model metadata buckets along the boundaries of the contextual domains. For example, you can model the asset context (as expressed by an ISA-95 implementation) in an `asset` bucket and the machine status in a `machine-status` bucket.

You should also consider whether you need to contextualize a tag or any arbitrary group of records.

Tag buckets should be chosen for tag-related metadata, while record buckets should be chosen for any other type of metadata.

It is generally advisable to model hierarchical domain metadata in the same bucket. For example, while attributes of the machine to which the _tag_ belongs to (for example, the manufacturer of a sensor installed in the machine) could be modelled in two separate buckets (tag bucket and machine bucket), it's generally better to model such hierarchical relationships in a single bucket.

A good reason for splitting a hierarchy in several separate dimensions is to enable associating records with metadata at different levels of granularity. For example, if you are integrating two different data sources, one of which sends data at sensor-level granularity and another at machine-level granularity, you should separate the machine-specific data into its own bucket.

### Configuring cloud metadata bucket schema

The schema of a bucket determines the permissible structure of metadata instances in a bucket. Schemas drive data quality, and also allow you to define what fields can or must be used to describe an entity that a given bucket models. The fields that you should allow or require in a bucket largely depend on the data that your sources deliver and which bucket population and record linking strategy you pick.

If you choose to populate metadata buckets dynamically from the edge, your main consideration when defining a schema should be the availability of metadata in the source messages. You should also weigh in data conformity and ease of ingestion. The more specific your metadata bucket schemas and the more fields are marked as required, the more consistent the resulting metadata instances are. However, this also raises the demands on the parser to resolve any structural differences between messages.

On the other hand, the more generic your bucket schemas are (for example, specifying that a metadata property can be any 'object' as opposed to defining specific object properties), the lower the metadata transformation and harmonization requirements in the parser. However, this may come at the expense of metadata consistency and conformity.

Another important consideration when designing a bucket schema is the granularity of the bucket. If you are creating metadata instances over the API, make sure that the natural key is not more granular or more coarse than the data you expect to receive from the edge. For example, if receive status events from the edge at machine level, but your asset bucket contains instances at sensor granularity you won't be able to link records to metadata instances in this bucket. Instead, you require a bucket that contains instances at the machine-level granularity.

## Records modelling

When modeling metadata, you face two key questions:

  1. What types to create?
  2. How should the types be configured?



### Modelling types

Types describe semantically and structurally similar records that you want to store together and describe with a common set of metadata, and for which you want to establish a common constraint on the data field.

With that in mind, types should capture records at the same level of granularity (level of detail). Typically, this means structuring types around some manufacturing process, operation or set of actions. For example, you can create a type for 'machine-state' records and another for 'sensor-readings'

We also recommend persisting data at the most atomic level and refraining from pre-aggregating data before sending it to MDE. This lets you benefit from the greatest query flexibility since you can build any aggregate from atomic data.

#### Types configurations

The key considerations when configuring types are the following:

  1. What metadata buckets should describe records of a type? Are they required or optional?
  2. What should be the schema of the data field?



##### Metadata configuration for types

You can associate metadata bucket versions with types. Associating a bucket version to type implies that records of that type may or must (depending on value of the `required` field on the association) be linked to metadata instances from the given bucket version at runtime.

Deciding which buckets to associate to a type and whether the association should be classified as `required` depends on several considerations. You should consider the contextualization requirements of your data consumers, the context that you receive from the edge, data quality, as well as access to original data if edge data sources don't deliver the required context.

Setting the `required` flag on a metadata bucket association will improve the consistency of your data; however, it also requires you to think about how to handle cases where either the edge fails to deliver metadata or a metadata instance for a natural key not yet been created. In such cases, you can let MDE reject the message and have it moved a dead letter queue, or you can create a generic `Not Available` metadata instance in your bucket to link records to it if a link to a full contextualized instance not be created.

##### Data field configuration for types

Configuring the data field on `DISCRETE_DATA_SERIES` and `CONTINUOUS_DATA_SERIES` lets you to gain a consistent object structure in the data field. When defining the data field, you should profile your source data and make sure parsers are able to generate proto records that validate against the defined schema.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
