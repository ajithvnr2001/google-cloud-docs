---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/overview-model-preparation/
title: Overview of model preparation \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:05.516263+00:00
---

# Overview of model preparation  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/overview-model-preparation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Overview of model preparation Stay organized with collections  Save and categorize content based on your preferences. 

This page leads you through the steps to prepare an AML AI model, assuming you have already set up an instance and prepared the necessary datasets.

## Overview of stages

The process to prepare a model is in covered in the following three stages:

  * **Stage 1** : [Configure an engine](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/configure-engine), including selecting the source of hyperparameters:

    * Tuning: Automatic tuning of hyperparameters
    * Inherit: Inherit hyperparameters from a previous engine config that was created with an earlier engine version within the same [tuning version](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/glossary#engine-version). This setting lets you avoid re-tuning each time you adopt a new model engine version.

[Creating an engine config](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-engine-configs) stores the results from tuning or inheritance in an [EngineConfig resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs).

  * **Stage 2** : [Generate a model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/generate-model)

[Creating a model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-models) triggers training, storing the results as a [Model resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models).

  * **Stage 3** : [Evaluate a model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/evaluate-model)

[Creating backtest results](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-backtest-results) evaluates model performance on a specified set of months, storing summary results in a [BacktestResult resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults). Optionally, [creating prediction results](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-prediction-results) lets you evaluate per-party outputs of the model.




Once you have completed the earlier stages and model performance meets your needs, see the guidance in sections [Generate risk scores and explainability](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/register-parties) and [Prepare for model and risk governance](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/collect-model-risk-governance-artifacts).

## Before you begin

Before you begin, you will need the following:

  * One or more [datasets](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-data-model-requirements)
  * A selected [engine version](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-engine-versions) to use



## Dataset requirements

For detailed guidance on the data model and schema, see the pages under [Prepare Data for AML AI](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-data-model-requirements). This section covers how to make sure that the datasets used in engine tuning, training, and evaluation work well together.

**Note** : Most model governance policies define a requirement to track data lineage used across all ML operations from engine configuration, training, and evaluation. To ensure data remains unchanged, we recommend that you create a [BigQuery table snapshot](https://docs.cloud.google.com/bigquery/docs/table-snapshots-intro) of your BigQuery tables after they pass data validation and reference the snapshot in the AML AI dataset. If you reference regularly updated tables, AML AI operations read the BigQuery tables each time an operation uses the AML AI dataset, so changes to the underlying BigQuery tables could impact tuning, training, backtesting, and predictions. 

### Dataset time ranges

Each dataset used for tuning, training, backtesting and prediction operations should contain valid data for a time range ending at the end of the last full calendar month prior to the end_time specified in the API call. The length of this time range depends on the table, Engine Version and operation. The minimum time range is covered in detail in [Understand data scope and duration](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-data-scope-duration).

For example, for engine tuning with v004.004 engine versions, the Transaction table should cover at least 30 months.

Configuring an engine, training, and evaluation (backtesting) can be completed with a single dataset; see the following image. To ensure good production performance by avoiding overfitting, you should ensure that the period used for evaluation (that is, creating backtest results) is after the period used for training (that is, creating a model).

For example: if using 3 periods for backtesting and using periods up to the end of February 2024 for training (that is, end time in early March 2024), then you could use periods up to the end of May 2024 for backtesting (that is, end time in early June 2024).

![Dataset time ranges for tuning, training, and backtesting](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/images/best-practice-arrangement-for-tune-train-backtest-2024-06-24-update.svg)

### Dataset consistency

When using different datasets for the engine tuning, training, and evaluation stages, make the datasets consistent in which fields are populated and how they are populated. This is important for AML model stability and performance.

Similarly, for a high-quality [risk score](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#risk-scores), the dataset used to create prediction results with a model should be consistent with the dataset used to train that model.

In particular, ensure the following:

  * **The same logic is used to populate each field.** Changing the logic used to populate a field can introduce feature skew between model training and prediction or evaluation.
  * **The same selection of RECOMMENDED fields are populated.** For example, removing a field that was populated during model training can cause features that the model relies on to be skewed or missing during evaluation or prediction.
  * **The same logic is used to provide values.** In the [PartySupplementaryData](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#partysupplementarydata) table, the same logic is used to provide values for each `party_supplementary_data_id` field.

    * Using the same data, but with different `party_supplementary_data_id` values, causes the model to use data incorrectly. For example, a particular field uses ID `5` in the [PartySupplementaryData](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#partysupplementarydata) table for one dataset, but then uses ID `7` in another dataset.
    * Removing a `party_supplementary_data_id` value that a model relies on may have unpredictable effects. For example, ID `3` is used in the [PartySupplementaryData](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#partysupplementarydata) table in one dataset but is omitted from another dataset.



Now you have a dataset ready for engine tuning, training, and evaluation. Note that model operations **can take tens of hours**. For information on how to check if an operation is still running or has completed (failed or succeeded), see [Manage long-running operations](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-long-running-operations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
