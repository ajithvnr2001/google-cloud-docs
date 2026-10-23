---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/glossary/
title: AML AI glossary \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:32.563219+00:00
---

# AML AI glossary  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/glossary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  AML AI glossary Stay organized with collections  Save and categorize content based on your preferences. 

This glossary defines terms specific to AML AI. For general machine learning terms, see [Machine Learning Glossary](https://developers.google.com/machine-learning/glossary).

## A

**ADC**
    

Each of the API client libraries provide a means to use local **application default credentials** (ADC)

    

For information about the difference between your local ADC credentials and your gcloud CLI credentials, see [gcloud CLI credentials and ADC credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc#gcloud-credentials)

## B

**backtesting**
    Backtesting uses historical data to evaluate performance (observed recall) of a model by comparing the risk score it generates to the actual outcomes of historical investigations.
**backtest results**
    An AML AI [BacktestResult resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults) (also known as "backtest results") is created to test the performance of a model on a dataset.
    For more information, see [Evaluate a model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/evaluate-model).

## C

**core banking data**
    [Core banking data](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#core-banking-data-tables) includes data on parties, transactions, and account holdings. It helps AML AI to understand your customers and their banking activity to detect risky characteristics and behaviors.

## D

**data validation**
    AML AI conducts data validation checks when creating a dataset, engine config, model, backtest results, or prediction results. If the specified dataset doesn't pass data validation, then the resource is not created and data validation errors are produced (indicating the nature of the issue).
    For more information, see [Data validation errors](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/data-validation-errors).
**dataset**
    

An AML AI [Dataset resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.datasets) (or just "dataset") is used to specify data, conforming to the [AML input data model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model), which can be used in generating a model, evaluating performance of a model, and generating risk scores and explainability per party.

    

For more information, see [Understand the AML data model and requirements](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-data-model-requirements).

## E

**end time**
    

AML AI operations (such as model training, evaluation examples, and model outputs) use datasets composed of examples from the bank's data collected over a span of months. These operations require you to specify an end time, which is a date within the dataset's time span. Based on this end time, the operation will use the last full calendar month before the end time as the final month of data used in the operation.

    

The end time and all months used for an operation must be within the date range of the associated dataset.

    

For example, a model training operation uses 15 periods with a maximum lookback window of 13 months. The dataset has a date range from October 15, 2020 to May 21, 2023. The training end time is April 12, 2023. The training uses examples from January 1, 2021 to March 31, 2023, which is 27 full calendar months prior to the end time. This time period is within the date range of the dataset.

**engine config**
    

An AML AI [EngineConfig resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs) (also known as an "engine config") specifies parameters in generating and evaluating an AML AI model and in generating risk scores and explainability.

    

Some of these parameters are specified in the API call to create an engine config, such as engine version and the expected investigation volume. Other parameters are automatically generated by AML AI using a specified dataset, for example, tuned hyperparameters.

    

For more information, see [Configure an engine](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/configure-engine).

**engine version**
    

An AML AI [EngineVersion resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineVersions) (also known as an "engine version") defines aspects of how AML AI detects risk, which encompasses model tuning, training, and evaluation, as well as the overall AML data model and feature families.

    

[Configuring an AML AI engine](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/configure-engine) requires you to specify an engine version to use. The engine version is then used to train and evaluate models with that engine config and to generate risk scores and explainability.

    

Engine version naming is structured as follows, with the engine type expressing the supported [line of business](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/glossary#lob), and engine subtype, tuning, major version, and minor version updated as new behaviors are implemented.

    

Example versions include:

  * `aml-retail.default.v004.008.202411-001`
  * `aml-commercial.default.v004.008.202411-001`


![Engine versioning](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/images/engine-versioning.svg)
    

    

For more information on managing engine versions, see [Manage engine versions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-engine-versions).

**evaluation**
    

See also backtesting.

**explainability**
    

AML AI models are used to identify parties exhibiting behaviors or characteristics with high risk for money laundering. Explainability indicates which behaviors or characteristics contributed the most to a high-risk score for a given party.

    

For more information, see [Understand prediction outputs](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-prediction-outputs).

    

See also prediction.

**export metadata**
    

Several AML AI resources store additional information relating to performance and data quality which can be accessed using the export metadata operation.

    

For more information, see [AML output data model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#exported-metadata).

## F

**feature family**
    Feature families are collections of related ML [features](https://developers.google.com/machine-learning/glossary#feature), providing a straight-forward, human-understandable categorization to inform investigators and internal audit teams.

## I

**immutable entity**
    

AML AI needs to be able to recreate views of the data at different points in time for tuning, training, and backtesting. To achieve this, AML AI differentiates between mutable entities (that can change values over time) and immutable entities (that don't change).

    

For example, a mutable entity might be your checking account balance, which can change over time; but an immutable entity might be an event, like withdrawing $50 on July 2, 2024 at 12:00:00 from your checking account, which doesn't change since it was a snapshot in time.

    

In the [AML input data model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model), tables representing immutable entities don't have the fields `validity_start_time` and `is_entity_deleted`. This includes the [RiskCaseEvent](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#riskcaseevent) table.

    

For more information, see [Understanding how data changes over time](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#data-changes-over-time).

    

See also mutable entity.

**instance**
    

An AML AI [Instance resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances) (also known as an "instance") sits at the root of all other AML AI resources and must be created before you can work with other AML AI resources. Multiple instances can be created in the same region within a project.

    

For more information, see [Create an AML AI instance](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/set-up-instance).

**investigation process**
    

An investigation process covers the entire investigation or sequence of investigations triggered by an alert. The process starts when the first part of an investigation starts and ends when no further outcomes are expected from this investigation.

    

For more information, see [Lifecycle of a risk case](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/lifecycle-risk-case).

## L

**LOB**
    The **line of business** (LOB) distinguishes retail and commercial banking customers in AML AI. Datasets, engine versions, and party registration are linked to a specific line of business, retail, or commercial.
**Note:** A single party might have both retail and commercial accounts with a bank and so would be used for both lines of business.

**lookback window**
    

For each period used by a tuning, training, prediction or backtest operation AML AI requires that datasets cover a lookback window to allow generation of features that track behavior over time. This lookback window depends on engine version.

    

For more information, see [Understand data scope and duration](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-data-scope-duration).

**LRO**
    

Several AML AI operations, including engine configuration, training, backtesting, and prediction, initiate a **long-running operation** (LRO).

    

For more information, see [Manage long-running operations](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-long-running-operations).

## M

**missingness**
    

The missingness metric is computed for all feature families when creating the following AML AI resources: engine config, model, backtest results, and prediction results.

    

This metric shows the share of missing values across all features in a feature family. A significant change in Missingness for any feature family between tuning, training, evaluation, and prediction can indicate inconsistency in the datasets used.

**model**
    

An AML AI [Model resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models) (also known as a "model") represents a trained model that can be used to generate risk scores and explainability.

**mutable entity**
    

AML AI needs to be able to recreate views of the data at different points in time for tuning, training, and backtesting. To achieve this, AML AI differentiates between mutable entities (that can change values over time) and immutable entities (that don't change).

    

For example, a mutable entity might be your checking account balance, which can change over time; but an immutable entity might be an event, like withdrawing $50 on July 2, 2024 at 12:00:00 from your checking account, which doesn't change since it was a snapshot in time.

    

In the [AML input data model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model), tables representing mutable entities have the fields `validity_start_time` and `is_entity_deleted`. This includes the [Party](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#party), [AccountPartyLink](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#accountpartylink), [Transaction](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#transaction), and [PartySupplementaryData](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#partysupplementarydata) tables.

    

For more information, see [Understanding how data changes over time](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#data-changes-over-time).

    

See also immutable entity.

## O

**observed-recall**
    

AML AI measures model performance on historical data using the Observed Recall metric.

    

This metric shows the proportion of positive labeled parties (for example, customer exits) from a selected period that would have been identified during a suspicious activity period as high risk by the model being evaluated.

## P

**party**
    

In the [AML input data model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model), a party represents a customer of the bank. A party can be a natural person or a legal entity.

    

For more information, see the [Party](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#party) table.

    

See also registered party.

**prediction**
    

Prediction is using a model to generate risk scores and explainability which can be used in your AML investigation process.

**prediction results**
    

An AML AI [PredictionResult resource](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults) (also known as "prediction results") is the result of using a model to create predictions.

    

For more detail on how to generate risk scores and explainability, as well as how to use these in your investigative process, see the pages in section [Generate risk scores and explainability](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/register-parties).

## R

**registered party**
    Before a party can be used to create prediction results (for example, party-level risk scores and explainability), the party must be registered for the corresponding [line of business](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/glossary#lob).
**risk case**
    

A risk case covers an investigation process or a group of related investigation processes for different parties.

    

See the [RiskCaseEvent](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#riskcaseevent) table.

**risk investigation data**
    

Risk investigation data is used by AML AI to understand your risk investigation process and outcomes and to generate training labels.

**risk score**
    

AML AI models are used to identify parties exhibiting behaviors or characteristics with high risk for money laundering. This is done through a risk score.

    

Risk scores vary from 0 to 1. A higher score indicates higher risk. However, risk scores shouldn't be interpreted directly as a probability of money laundering activity.

    

For more information, see [Understand prediction outputs](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-prediction-outputs).

**risk typology**
    

AML AI can identify money laundering risk across [five core AML risk typologies](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview#risk-topologies-supported)related to transaction monitoring.

    

With sufficient investigation and supplementary party data (see [Supplementary data](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#supplementary-data-tables) tables), AML AI can cover more typologies.

## S

**supplementary data**
    

Supplementary data is additional data, beyond what is contained in the core banking data and risk investigation data areas of the AML AI schema, which is relevant to predicting risk of money laundering.

    

For example, you might identify and add a risk indicator that helps models better predict a risk typology that is not otherwise well covered.

    

Supplementary data can be added to a dataset using the [PartySupplementaryData](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#partysupplementarydata) table.

**Important:** The other tables in the schema generally suffice for AML performance and risk typology coverage. Adding supplementary data is purely optional.

**suspicious activity period**
    

A suspicious activity period is a period of time in which you believe an investigated party exhibited suspicious behavior. This is used in model evaluation (for example, the recall metric for backtest results) to confirm that high-risk customers are identified during months when they had suspicious activity. The suspicious activity period helps models identify risk at the correct time, for example, during or shortly after the period when the suspicious activity occurred. The suspicious activity period is used in validation for tuning and training, and also for the recall metric in backtesting.

    

For more information, see [Lifecycle of a risk case](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/lifecycle-risk-case).

## T

**training**
    AML AI does training as part of creating a model using hyperparameters (see tuning) from a specified engine config.
**tuning**
    Tuning is the optimization of model hyperparameters. AML AI does tuning as part of creating an engine config.

## V

**validity start time**
    

Validity start time for a mutable entity is used by AML AI to construct a view of what was known by the bank at a given point in time. This allows AML AI to accurately train models that can be reused on the latest data (that is, what is known by the bank) to produce high fidelity risk scores.

    

Validity start time for a given row represents the earliest time that the data in this row was known to the bank and correct.

    

For more information, see [Understanding how data changes over time](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#data-changes-over-time).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
