---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-data-scope-duration/
title: Understand data scope and duration \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:32:46.261510+00:00
---

# Understand data scope and duration  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-data-scope-duration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Understand data scope and duration Stay organized with collections  Save and categorize content based on your preferences. 

AML AI is set up to assess money laundering risk for one [line of business](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/glossary#lob) at a time with separate datasets, engine versions and models for retail banking and for commercial banking.

When creating a dataset for use with an LoB, you will need to include several tables. Each table should cover a sufficient time range. This page gives an overview of the tables you will need and shows how to determine the time range that each should cover.

## Tables to use

The BigQuery dataset used with AML AI should contain the following tables:

  * **[Party](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#party)** : All parties relevant to that LoB. 
    * **Retail LoB** : All retail banking customers that have held accounts at any point in the required time range.
    * **Commercial LoB** : All commercial banking customers (legal and natural entities) that have held accounts at any point in the required time range
    * Note that some customers can be represented in both datasets. For example, self-employed people might have both retail and commercial accounts.
  * **[AccountPartyLink](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#accountpartylink)** : Full history of which accounts were held by which parties. This should cover all accounts for products and services when any party in the Party table was the primary account holder at any point in the required time range.
  * **[Transaction](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#transaction)** : All transactions for accounts in the AccountPartyLink table for the required time range.
  * **[RiskCaseEvent](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#riskcaseevent)** : All risk case events (see event type values) for any risk case and party in the Party table with an AML_PROCESS_START (start of investigation) in the required time range. This table may include events that have an event time earlier or later than the required time range.
  * **[PartySupplementaryData](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#partysupplementarydata)** : (If used) For 0 to 100 unique party_supplementary_data_id values, include a full history of the values of these fields for all parties in the Party table for the required time range.



## Using additional data

See [Supplementary data](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#supplementary-data-tables) if you have additional data on parties (not otherwise covered in the schema) that is relevant to identifying money laundering risk.

## Dataset time range

The time range that any table in a dataset should cover can be worked out as follows for any given operation. You will need to know:

  * The end time. This is the latest time from which labels are used and from which data is used to generate features for tuning.
  * The Engine Version (See [list of engine versions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/private/engine-versions)) you will use.
  * The operation you will conduct: tune, train, predict or backtest.
  * For predict or backtest operations, the number of periods for which you will conduct the operation, to be specified in the API call.



![Understand Data Scope Duration](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/images/lookback-window-vs-additional-risk-case-events.svg)

First you should work out the number of periods the operation will use. This is the number of consecutive months ending in the last full calendar month prior to the specified end time, for which AML AI will evaluate model features.

  * For predict and backtest operations, this is the number of prediction periods or backtest periods specified in the API call.
  * For other operations this depends on the Engine Version and the operation. For example, v004.010 Engine Versions use 18 periods for tuning and 15 for training.



Next you should work out the lookback window for each table. This is the maximum number of months of data needed from that table for AML AI to calculate model features for a given period.

  * For example, for v004.010 Engine Versions, this is 13 months for Transaction and AccountPartyLink tables, 12 months for the RiskCaseEvent table and 0 months for Party and PartySupplementaryData tables.



The dataset will need to cover the lookback window for all of the periods used by the chosen operation. This can vary by engine version, but is typically 18 for tuning, 15 for training and configurable for prediction or backtesting. You can calculate the number of full calendar months of data prior to the end time that you will need for a given operation with the following formula:

  * **number of periods + lookback window -1**



Building on the example above for v004.010 Engine Versions, you will need up to 30 months of data for any AML AI operation.

  * 18 + 13 - 1 = 30 months of data from the Transaction and AccountPartyLink tables,
  * 18 + 12 - 1 = 29 months of data from the Risk Case Events table as well as any more recent events for risk cases in the table,
  * And 18 + 0 - 1 = 17 months of data from the Party and PartySupplementaryData tables.



We recommend to have a single dataset covering at least 36 months when conducting a first sample test of AML AI. This is to allow all the above operations and some additional months for evaluating the model beyond the minimum 3 for backtesting.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
