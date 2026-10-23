---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/collect-model-risk-governance-artifacts/
title: Collect model and risk governance artifacts \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:58.029964+00:00
---

# Collect model and risk governance artifacts  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/collect-model-risk-governance-artifacts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Collect model and risk governance artifacts Stay organized with collections  Save and categorize content based on your preferences. 

Model and risk governance is the process by which models are determined to be sufficient by all stakeholder groups. Your process might include new model validation, model monitoring, security and compliance standards, support processes, risk coverage, operations manuals, and user guides, among other topics.

As an owner of a risk framework, the following artifacts provide you with useful resources for integrating AML AI into your overall risk management landscape. AML AI contributes documentation relevant to model and risk governance, as well as various outputs from tuning, training, and evaluating your AML AI model.

## Model and risk governance documentation

The following set of concept documentation, available on request for AML AI customers, serves as governance artifacts in your overall risk management and AI/ML model and risk governance framework:

  * **Model architecture** : Describes the particular model architecture used for AML AI to calculate risk scores.
  * **Labeling methodology** : Describes the approaches used to define labeled training examples for tuning, training, and backtesting of AML AI models.
  * **Model training methodology** : Describes the training and validation approach for AML AI models.
  * **Model tuning methodology** : Describes the process by which AML AI optimizes model hyperparameters based on your data.
  * **Model evaluation methodology** : Describes the metrics that are used for model evaluation and backtesting.
  * **Feature families overview** : Describes the supported feature families in AML AI.
  * **Feature families and explainability** : Describes how AML AI uses feature families for explainability.
  * **Risk typology schema** : Describes how AML AI provides metrics to track data quality and potential impact on AML AI models.
  * **Risk typology schema** : Describes how AML AI supports risk typologies and the methodology it uses to demonstrate coverage.
  * **Engine version stability and support policy** : Describes what does and does not change between AML AI engine versions, and how long each engine version is supported for different operations.



## Model outputs as governance artifacts

The following artifacts are generated as outputs by regular AML AI operations:

  * **Model quality**
    * **Engine configuration output** includes expected recall (before and after tuning) captured in the engine config metadata.
    * **Backtest results** allow you to measure trained model performance on a set of examples not included in training.
  * **Data quality**
    * **Missingness output** indicates the share of missing values per feature family in your datasets used for tuning, training, backtesting, and prediction. Significant changes can indicate an inconsistency in your underlying data which can impact model performance.
    * **Data validation errors** prevent completion of AML AI operations, so to successfully produce a model and predictions, you must resolve these errors.
  * **Prediction results**
    * **Risk scores** vary from 0 to 1, and within this range a higher score indicates higher risk for the party for the predicted month. Risk scores shouldn't be interpreted directly as a probability of money laundering activity, or of the success of a possible investigation.
    * **Explainable AI output** augments high risk scores with attribution scores indicating contribution of each feature family to the risk score.
  * **Long-running operations (LROs)** allow you to track all AML AI processes used in model preparation and predictions. For more information, see [Manage long-running operations](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-long-running-operations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
