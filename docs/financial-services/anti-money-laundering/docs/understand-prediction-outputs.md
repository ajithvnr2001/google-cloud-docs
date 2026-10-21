---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-prediction-outputs/
title: Understand prediction outputs \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:32:48.788303+00:00
---

# Understand prediction outputs  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-prediction-outputs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Understand prediction outputs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the prediction outputs that result from requesting prediction results from AML AI.

For the schema and fields of the prediction outputs in BigQuery, see [Prediction outputs](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#prediction-outputs).

## Risk scores

[Risk scores](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#risk-scores) vary from 0 to 1. A higher score indicates higher risk, however, risk scores shouldn't be interpreted directly as a probability of money laundering activity.

Risk scores are produced for one (or more if [`predictionPeriods`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults#PredictionResult.FIELDS.prediction_periods) is greater than one) complete calendar months immediately prior to the specified [`endTime`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults#PredictionResult.FIELDS.end_time). A risk score is calculated for each party for each month.

Each prediction and explanation produced has a `risk_period_end_time` at midnight after the end of the complete calendar month.

For example, if [`predictionPeriods`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults#PredictionResult.FIELDS.prediction_periods)`= 12` and [`endTime`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults#PredictionResult.FIELDS.end_time)`= 2022-01-01T00:00:00Z`, then AML AI creates risk scores and explainability for each month in 2021. A prediction with `risk_period_end_time` value of `2021-02-01T00:00:00Z` represents the customer's prediction for the month of 2021-01.

**Note:** Risk scores may not be present for a party before their earliest entry in the [Party](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#party) table (that is, the earliest validity start time).

## Explainability

AML AI [explainability](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#explainability) indicates which behaviors or characteristics (using feature families) contribute to the risk score of a given party. Explainability covers the highest risk parties, including all parties you would investigate. Explainability may not be included for lower risk customers.

### Feature families

Feature families are collections of related AML AI features, providing a human-understandable categorization to inform investigators and internal audit teams. 

Each feature family covers a specific set of transactional behaviors or party characteristics. Additionally, some feature families have a specific focus, allowing investigators to know where to start. Examples of focus include:

  * The type of transaction involved: 
    * Wire
    * Cash
    * Check
    * Card
    * Other
  * The direction of the transactions: 
    * Debit (outgoing for the party)
    * Credit (incoming for the party)



### Feature family attribution value

An attribution score is given for each high-risk party and each feature family, indicating the contribution of the feature family to the risk score of the party. A high positive value indicates strong contribution to increasing risk score. Similarly, a negative value indicates a contribution to lowering the score.

Feature families with the highest positive attribution value are likely to be the most relevant to an investigation of the party.

Consider the following example attribution values for one specific party:

Feature family| Attribution value  
---|---  
Unusual card debit activity| 0.4  
Unusual rapid movement of funds| 0.8  
Unusual wire debit activity| -0.2  
  
This example can be interpreted as follows:

  * The party's rapid movement of funds had the greatest contribution to their high risk score. An investigation might start there.
  * Unusual card debit activity also made a significant contribution so should also be considered.
  * The party's wire debit activity actually reduced the risk score, so it is unlikely that this needs inspection.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
