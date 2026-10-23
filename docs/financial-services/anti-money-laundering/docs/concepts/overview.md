---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview/
title: AML AI overview \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:24.065241+00:00
---

# AML AI overview  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  AML AI overview Stay organized with collections  Save and categorize content based on your preferences. 

Money laundering is turning "dirty" money "clean" by making it look like money from crimes actually came from legitimate sources (source: [fbi.gov](https://www.fbi.gov/investigate/white-collar-crime#Money-Laundering)). Between 2 and 5% of global GDP, or up to $2 trillion, is laundered each year (source: [UN Office on Drugs and Crime](https://www.unodc.org/unodc/en/money-laundering/overview.html)). Connected to activities ranging from drug and human trafficking to terrorist financing, these cash flows cost financial institutions up to hundreds of millions annually on anti money laundering technology and operations.

Google Cloud's Anti Money Laundering AI (AML AI) product is an API that scores AML risk. Use it to identify more risk, more defensibly, with fewer false positives and reduced time per review. This API:

  * Generates monthly risk scores for retail and commercial banking customers
  * Is designed to meet model governance requirements
  * Is explainable to analysts, risk managers, auditors, and regulators
  * Replaces or complements legacy transaction monitoring
  * Can be extended with a customer's own supplementary risk indicators



## Data it uses

AML AI uses no data other than what you provide. AML AI does not use Google data to enrich your datasets.

Accuracy and coverage depend on the quality and completeness of data you provide according to the AML AI schema and the volume and quality of customer exit or suspicious activity report (SAR) data to train on.

## Incorporate AML AI into your AML process

AML AI trains on your core banking data, suspicious activity information, and other data in your Google Cloud environment. Use the API to produce risk scores and accompanying explainability output to support your alerting and investigation process.

Feed investigation data into AML AI to regularly update models and risk scores.

![How AML AI works](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/images/how-aml-ai-works.svg)

## Supported financial products

The supported retail banking products include:

  * Checking or current accounts
  * Savings
  * Credit cards
  * Mortgages
  * Personal loans



This does not include the following: brokerage, trading of any kind, cryptocurrency, or insurance.

The supported commercial banking products include:

  * Cash accounts
  * Loans
  * Lines of credit
  * Direct payments from customers



This does not include the following: capital markets, trade finance, or foreign exchange.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
