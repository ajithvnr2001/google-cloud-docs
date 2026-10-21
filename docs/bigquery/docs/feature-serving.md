---
url: https://docs.cloud.google.com/bigquery/docs/feature-serving/
title: Feature serving \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:28:16.865189+00:00
---

# Feature serving  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/feature-serving/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Feature serving

This document describes your options for making [features](https://docs.cloud.google.com/bigquery/docs/preprocess-overview) available for BigQuery ML model training and inference. For all options, you must save the features in BigQuery tables as a prerequisite first step.

## Point-in-time correctness

The data used to train a model often has time dependencies built into it. When you create a feature table for time sensitive features, include a timestamp column to represent the feature values as they existed at a given time for each row. You can then use point-in-time lookup functions when querying data from these feature tables in order to ensure that there is no [data leakage](https://en.wikipedia.org/wiki/Leakage_\(machine_learning\)) between training and serving. This process enables point-in-time correctness.

Use the following functions to specify point-in-time cutoffs when retrieving time sensitive features:

  * [`ML.FEATURES_AT_TIME`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-feature-time)
  * [`ML.ENTITY_FEATURES_AT_TIME`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-entity-feature-time)



## Serve features in BigQuery ML

To train models and perform batch inference in BigQuery ML, you can retrieve features using one of the point-in-time lookup functions described in the Point-in-time correctness section. You can include these functions in the [`query_statement` clause](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create#query_statement) of the `CREATE MODEL` statement for training, or in the `query_statement` clause of the appropriate table-valued function, such as [`ML.PREDICT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-predict), for serving.

## Serve features with Vertex AI Feature Store

To serve features to BigQuery ML models that are [registered in Gemini Enterprise Agent Platform](https://docs.cloud.google.com/bigquery/docs/managing-models-vertex#register_models), you can use [Vertex AI Feature Store](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/overview). Vertex AI Feature Store works on top of feature tables in BigQuery to manage and serve features with low latency. You can use [online serving](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/serve-feature-values) to retrieve features in real time for online prediction, and you can use [offline serving](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/serve-historical-features) to retrieve features for model training.

For more information about preparing BigQuery feature data to be used in Vertex AI Feature Store, see [Prepare data source](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/prepare-data-source).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
