---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-data-model-requirements/
title: Understand the AML data model and requirements \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:12.911764+00:00
---

# Understand the AML data model and requirements  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-data-model-requirements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Understand the AML data model and requirements Stay organized with collections  Save and categorize content based on your preferences. 

At the core of AML AI is a detailed and up-to-date understanding of parties of the bank and their activity, covering, in particular, the following data:

  * Transactional activity
  * Account holdings
  * Party demographics
  * Risk investigation data



This page covers the creation and management of data used by AML AI, including details of the data model, data schema, and data requirements for AML. The schema itself, including details for the individual fields, appears in the [AML input data model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model) ([CSV file](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model.csv)). A synthetic example dataset is also available through the [Quickstart](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/train-models-to-detect-money-laundering).

The following prerequisites are not covered on this page:

  * Setup to use AML AI with an AML dataset (see [Set up a project and permissions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/set-up-project-permissions))
  * Security and compliance features (see pages under [Security and compliance features](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/security-and-compliance-features))



## Overview of data requirements

The AML data model accepts information on retail or commercial parties, their accounts and transactions, and detailed information on risk cases related to these parties. This section introduces important aspects of the data model that are valid across the different entities.

The AML data model schema is arranged into three areas: core banking data, risk investigation data, and supplementary data.

### Core banking data

  * **Tables** : [Party](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#party), [AccountPartyLink](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#accountpartylink), [Transaction](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#transaction)
  * **Purpose** : Serves as a structured collection of data on your customers and their banking activity, used in detection of risk. All parties, accounts and transactions to be monitored should be included. Provide either retail or commercial data in an AML AI dataset



### Risk investigation data

  * **Table** : [RiskCaseEvent](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#riskcaseevent)
  * **Purpose** : 
    * Serves as a structured collection of data on risk investigation processes and parties previously identified as risky
    * Assists in the creation of training labels for AML risk models



### Supplementary data

  * **Table** : [PartySupplementaryData](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#partysupplementarydata)
  * **Purpose** : Optional table that can contain additional information relevant to identifying money laundering risk that is not covered in the rest of the schema. You should start using AML AI without providing any supplementary data.



### Table relationships

The following diagram describes the table relationships, primary keys, and foreign keys.

**Note:** Since AML AI uses data over time, primary keys may include `validity_start_time` to allow accurate representation of data over time. For example, AML AI can capture when a customer was added to or removed from a joint account. For more details, see [understanding how data changes over time](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#data-changes-over-time).

![AML data model schema diagram](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/images/aml-schema-diagram.svg)

## Errors

When you create a dataset, AML AI automatically performs data validation checks. For information about these checks, the error messages and how to fix them, see [Data validation errors](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/data-validation-errors).

For more information about the technical schema, see [AML input data model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model) ([CSV file](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model.csv)). To understand the data duration requirements and scope, see [Understand data scope and duration](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-data-scope-duration). When you have tables ready in BigQuery, you can use AML AI to [create and manage a dataset](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-datasets).

**Note:** Most model governance policies define a requirement to track data lineage used across all ML operations from engine configuration, training, and evaluation. To ensure data remains unchanged, we recommend that you create a snapshot of your BigQuery tables. In the case that you don't snapshot data, AML AI operations read the BigQuery tables each time an operation uses the dataset, so changes to the dataset could impact tuning, training, backtesting, and predictions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
