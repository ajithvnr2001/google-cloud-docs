---
url: https://docs.cloud.google.com/vertex-ai/docs/featurestore/concepts/
title: Data model and resources \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:01:12.284373+00:00
---

# Data model and resources  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/featurestore/concepts/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Data model and resources Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Feature Store (Legacy) is [deprecated](https://docs.cloud.google.com/vertex-ai/docs/deprecations). Beginning on May 17, 2026, no new features will be added and only critical patches will be provided. On February 17, 2027, the service will be fully sunset and APIs will no longer be available. 

For continued support and faster innovation, migrate to [Vertex AI Feature Store (V2)](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview), our integrated platform for machine learning (ML) feature management introduced on November 17, 2023\. 

The following sections introduce the Vertex AI Feature Store (Legacy) data model and terminology that is used to describe Vertex AI Feature Store (Legacy) resources and components.

## Vertex AI Feature Store (Legacy) data model

Vertex AI Feature Store (Legacy) uses a time series data model to store a series of values for features. This model enables Vertex AI Feature Store (Legacy) to maintain feature values as they change over time. Vertex AI Feature Store (Legacy) organizes resources hierarchically in the following order: `Featurestore -> EntityType -> Feature`. You must create these resources before you can import data into Vertex AI Feature Store (Legacy).

As an example, assume that you have the following sample source data from a BigQuery table. This source data is about movies and their features.

![Shows how source data maps to the Vertex AI Feature Store \(Legacy\) data model](https://docs.cloud.google.com/static/vertex-ai/docs/featurestore/images/sample-source-data-mapping.png)

Before you can import this data into Vertex AI Feature Store (Legacy), you need to create a _featurestore_ , which is a top-level container for all other resources. In the featurestore, create _entity types_ that group and contain related features. You can then create features that map to features in your source data. The names of the entity type and features can mirror the column header names, but that is not required.

In this example, the `movie_id` column header can map to an entity type `movie`. The `average_rating`, `title`, and `genre` are features of the `movie` entity type. The values in each column map to specific instances of an entity type or features, which are called _entities_ and _feature values_.

The timestamp column indicates when the feature values were generated. In the featurestore, the timestamps are an attribute of the feature values, not a separate resource type. If all feature values were generated at the same time, you are not required to have a timestamp column. You can specify the timestamp as part of your import request.

### Featurestore

A featurestore is the top-level container for entity types, features, and feature values. Typically, an organization creates one shared featurestore to import, serve, and share features across all teams in the organization. However, sometimes you might choose to create multiple featurestores within the same project to isolate environments. For example, you might have separate featurestores for experimentation, testing, and production.

**Note:** Featurestore is the name of the resource and Vertex AI Feature Store (Legacy) is a component of Vertex AI.

### Entity type

An entity type is a collection of semantically related features. You define your own entity types, based on the concepts that are relevant to your use case. For example, a movie service might have the entity types `movie` and `user`, which group related features that correspond to movies or customers.

### Entity

An entity is an instance of an entity type. For example, `movie_01` and `movie_02` are entities of the entity type `movie`. In a featurestore each entity must have a unique ID and must be of type `STRING`.

### Feature

A feature is a measurable property or attribute of an entity type. For example, the `movie` entity type has features such as `average_rating` and `title` that track various properties of movies. Features are associated with entity types. Features must be distinct within a given entity type, but they don't need to be globally unique. For example, if you use `title` for two different entity types, Vertex AI Feature Store (Legacy) interprets `title` as two different features. When reading feature values, you provide the feature and its entity type as part of the request.

When you create a feature, you specify its value type such as `BOOL_ARRAY`, `DOUBLE`, `DOUBLE_ARRAY`, and `STRING`. This value determines what value types you can import for a particular feature. For more information about the supported value types, see the `valueType` in the [API reference](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes.features).

### Feature value

Vertex AI Feature Store (Legacy) captures feature values for a feature at a specific point in time. In other words, you can have multiple values for a given entity and feature. For example, the `movie_01` entity can have multiple feature values for the `average_rating` feature. The value can be `4.4` at one time and `4.8` at some later time. Vertex AI Feature Store (Legacy) associates a tuple identifier with each feature value (`entity_id`, `feature_id`, `timestamp`), which Vertex AI Feature Store (Legacy) uses to look up values at serving time.

Vertex AI Feature Store (Legacy) stores discrete values even though time is continuous. When you request a feature value at time `t`, Vertex AI Feature Store (Legacy) returns the latest stored value at or before time `t`. For example, if the Vertex AI Feature Store (Legacy) stores the location information of a car at times `100` and `110`, the location at time `100` is used for requests at all times between `100` (inclusive) and `110` (exclusive). If you require higher resolution, you can, for example, infer the location between values or increase the sampling rate of your data.

## Feature import

Feature import is the process of importing feature values computed by your feature engineering jobs into a featurestore. Before you can import data, the corresponding entity type and features must be defined in the featurestore. Vertex AI Feature Store (Legacy) offers batch and streaming import, letting you add feature values in bulk or in real time.

For example, you might have computed source data that live in locations such as BigQuery or Cloud Storage. You can batch import data from those sources into a central featurestore so that those feature values can be served in a uniform format. As your source data changes, you can use streaming import to quickly get those changes into your featurestore. That way, you have the latest data available for online serving scenarios.

For more information, see [Batch import feature values](https://docs.cloud.google.com/vertex-ai/docs/featurestore/ingesting-batch) or [Streaming import](https://docs.cloud.google.com/vertex-ai/docs/featurestore/ingesting-stream).

## Feature serving

Feature serving is the process of exporting stored feature values for training or inference. Vertex AI Feature Store (Legacy) offers two methods for serving features: batch and online. Batch serving is for high throughput and serving large volumes of data for offline processing (like for model training or batch predictions). Online serving is for low-latency data retrieval of small batches of data for real-time processing (like for online predictions).

For more information, see [online](https://docs.cloud.google.com/vertex-ai/docs/featurestore/serving-online) or [batch](https://docs.cloud.google.com/vertex-ai/docs/featurestore/serving-batch) serving.

### Entity view

When you retrieve values from a featurestore, the service returns an _entity view_ that contains the feature values that you requested. You can think of an entity view as a projection of the features and values that Vertex AI Feature Store (Legacy) returns from an online or batch serving request:

  * For online serving requests, you can get all or a subset of features for a particular entity type.
  * For batch serving requests, you can get all or a subset of features for one or more entity types. For example, if features are distributed across multiple entity types, you can retrieve them together in a single request, which joins those features together. You can then use the results to feed to a machine learning or batch prediction request.



## Export data

Vertex AI Feature Store (Legacy) lets you export data from your featurestores so that you can backup and archive feature values. You can choose to export the latest feature values (snapshot) or a range of values (full export). For more information, see [Export feature values](https://docs.cloud.google.com/vertex-ai/docs/featurestore/export-features).

## What's next

  * Learn about [setting up your project](https://docs.cloud.google.com/vertex-ai/docs/featurestore/setup) for Vertex AI Feature Store (Legacy).
  * Learn about [source data requirements](https://docs.cloud.google.com/vertex-ai/docs/featurestore/source-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
