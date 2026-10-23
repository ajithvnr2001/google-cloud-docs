---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/prepare-to-generate-prediction-outputs/
title: Prepare to generate prediction outputs \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:32.615893+00:00
---

# Prepare to generate prediction outputs  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/prepare-to-generate-prediction-outputs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Prepare to generate prediction outputs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to prepare the datasets needed to generate prediction outputs.

## Before you begin

Before you begin, you need the following:

  * A [model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/overview-model-preparation)
  * To [register all parties](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/register-parties) that appear in the dataset you are using for prediction

**Note:** The operations in the following sections take several hours to complete. To check the status of an operation, see [Manage long-running operations](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-long-running-operations).

## Create a dataset for prediction

You can create predictions using an existing dataset (for example, the one you were using for backtesting). However, in a production environment, we recommend that you create a new dataset for each prediction run:

  1. As a customer, you're responsible for all tracking of lineage from dataset to model. To ensure data remains unchanged, we recommend that you create a [BigQuery table snapshot](https://docs.cloud.google.com/bigquery/docs/table-snapshots-intro) of your BigQuery tables after they pass data validation and reference the snapshot in the AML AI dataset. If you reference regularly updated tables, AML AI operations read the BigQuery tables each time an operation uses the AML AI dataset, so changes to the underlying BigQuery tables could impact tuning, training, backtesting, and predictions.
  2. Follow the guidance under [Prepare Data for AML AI](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-data-model-requirements) to prepare your BigQuery tables and then [create a separate AML AI dataset for prediction](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-datasets) using the tables you snapshotted in Step 1. To create the BigQuery datasets and tables, you can use the commands in [Prepare BigQuery datasets and tables](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/prepare-bq-datasets-tables).



## Prepare the output destinations

AML AI generates prediction outputs (risk scores and explainability) in BigQuery when you [create a prediction results resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults/create).

Before creating prediction results, you must [create a BigQuery dataset](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/prepare-bq-datasets-tables#create-bq-output-dataset) for these outputs. Any BigQuery dataset can be used for prediction outputs, as long as the [correct permissions are granted](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/prepare-bq-datasets-tables#grant-access-datasets) and the dataset is in the same project where the API is enabled and in the same location as the AML AI instance.

## Generate risk scores and explainability

Now that you have the dataset for prediction, a [trained model resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models), and a BigQuery dataset for output, you can create prediction results. To do this, see [Create and manage prediction results](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-prediction-results).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
