---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/process-overview/
title: Process overview \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:17.166966+00:00
---

# Process overview  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/process-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Process overview Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

This page provides an overview of the AML AI processes and covers key concepts for customers to understand. It is targeted primarily at teams who will use AML AI to train, test, and deploy models.

AML AI enables banks to automatically train, test, and deploy models for detecting money laundering. The AML AI guides are split into five left-navigation sections that correspond to the following five steps.

Step| Description  
---|---  
1\. Set up AML AI | Ensure your Google Cloud project is ready to use AML AI. Enable required Google Cloud services and set up logging and quotas. Create one or more AML AI instances.   
2\. Prepare data for AML AI | Review the data model and schema. Prioritize which data to include. Collect and transform the necessary core banking data, risk investigation data, and any other data you need. Create and validate a dataset.   
3\. Generate a model and evaluate performance | Understand AML AI engines, models, and backtesting. 

  1. Configure an engine
  2. Train a model
  3. Evaluate a model's performance

  
4\. Generate risk scores and explainability | Register your retail and commercial banking customers. Use a model to generate per-party risk scores and explainability for: 

  * Analysis and testing for risk governance
  * Pre-production and production use

  
5\. Prepare for model and risk governance | Combine AML AI outputs from tuning, training, evaluation, and prediction with AML concept and product documentation to meet requirements of your model risk governance process. **Note** : AML AI customers have access to detailed documentation of AML AI that is specifically designed to support model governance review.  
  
The core AML AI technical operations to create, test, and deploy models are as follows. These support steps 2-4 in the preceding table.

  1. [Create AML AI Dataset](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.datasets) \- creates a structured set of BigQuery input data tables for AML AI
  2. [Engine Configuration](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs) \- tunes an AML AI engine to an AML AI dataset, including hyperparameter tuning
  3. [Model Training](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models) \- trains an AML AI model using an Engine Configuration and a dataset
  4. [Backtest](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults) \- tests an AML AI model against historic data on a dataset and summarizes performance
  5. [Register Parties](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/importRegisteredParties) \- registers parties (customers of the bank who have banking products and send or receive transactions) so they can be scored in prediction
  6. [Prediction](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults) \- produces party scores and explainability for use in production



Engine Configuration, Model Training, Model Backtest, and Model Prediction all require an AML AI dataset as input and return corresponding artifacts which are used in other operations. For example, [Model Training](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models/create) returns a reference to a [trained AML AI model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models) which can be used for backtest or prediction. For technical details of the operations, see the [REST Reference Overview](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest).

### Dependency tree for AML AI processes

![Dependency tree for AML AI processes](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/images/dependency-tree-for-aml-ai-processes.svg)

## Important considerations when using AML AI

This section is designed to give customers an introduction to the key concepts of AML AI and advise on some best practices. Topics here are covered in more detail in dedicated guides and links are provided for further reading.

### Date consistency

AML AI uses different time periods for different operations. Care should be taken with the dates selected for each operation to ensure reliable results. In particular, to avoid bias in results, it is important that the months used for training an AML AI model don't overlap with the months used for backtesting.

Since an AML AI dataset contains many months of data, datasets can be used for multiple operations, subject to these correct date selections. The following diagram illustrates a development cycle using AML AI, where different time periods within a single dataset spanning 42 months are used to configure an engine (hyperparameter tuning), training, and backtesting. All these processes use lookback windows which provide context to the model, and can safely overlap with data used for other operations.

**Note:** More recent Engine Versions may require fewer months of data. Check the documentation of the specific [Engine Version](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/engine-versions) you will use.

For more information on AML AI datasets and time windows for different operations, see [Understand data scope and duration](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-data-scope-duration).

To ensure you record changes to your data over time correctly, see [Data changes over time](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#data-changes-over-time).

![Create an AML AI dataset - step 1-4](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/images/create-aml-ai-dataset-steps-1-4.svg)

### Production batch frequency

In prediction, AML AI produces AML risk scores on a calendar month basis. Customers commonly use AML AI as part of a monthly batch process, and they are advised to run predictions on months with complete transaction data as much as possible.

**Note:** Running months with some transactions missing may affect the quality of party risk scores.

### Field consistency

As with any machine learning process, data should be as consistent as possible between training data and test data. If fields are not populated consistently, the changes may cause unreliable results. It's strongly recommended that steps are taken to ensure fields are populated consistently for each operation in a development cycle——and this is especially true if different datasets are used for each operation. For more information, see [dataset consistency](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/overview-model-preparation#dataset-consistency).

**Note:** The skew metric in Prediction Results and Backtest Results resources can be used to monitor for changes in the data between model training and prediction.

### Engine configs

Once an engine config has been created, it's not normally necessary to re-create it for every new dataset or in every development cycle. The hyperparameters chosen in an engine config for one dataset generally perform well on similar datasets.

**Note:** If the datasets are changed substantially, creating a new engine config may improve performance. This is particularly true if deploying to a new market, or if the Risk Case Event data or Party Supplementary Data are significantly updated. 

Iterative development cycles are illustrated in the following diagram, whereas the preceding diagram uses a single dataset for both Model Training and Backtest operations.

For more information, see [when to tune or inherit](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/configure-engine#tune-or-inherit).

![Create an AML AI dataset - step 3-4](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/images/create-aml-ai-dataset-steps-3-4.svg)

### Data lineage

Most model governance policies define a requirement to track data lineage used across all ML operations from engine configuration, training, evaluation, and prediction. Customers are responsible for tracking this data lineage.

We recommend using a unique identifier in the names for all input data, AML AI resources, and output data to track lineage across stages. This helps to ensure strong linking between resources in a particular run. Customers can also label all AML AI resources to meet lineage requirements.

Additionally, we recommend using BigQuery snapshots in API requests to ensure accurate data lineage.

This configuration helps answer questions like "where did this engine configuration come from?" and "where did this model come from?" while helping to investigate and resolve incidents.

For details of how to create and manage AML AI resources, see the [REST API](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest) pages. 

![Create an AML AI dataset - step 3-4](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/images/create-aml-ai-dataset-data-lineage.svg)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
