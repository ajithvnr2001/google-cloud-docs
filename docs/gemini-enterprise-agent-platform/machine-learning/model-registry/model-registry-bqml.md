---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/model-registry-bqml/
title: BigQuery ML and Model Registry \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:53.787253+00:00
---

# BigQuery ML and Model Registry  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/model-registry-bqml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  BigQuery ML and Model Registry Stay organized with collections  Save and categorize content based on your preferences. 

[BigQuery ML](https://docs.cloud.google.com/bigquery/docs/bqml-introduction) is a Google Cloud service that lets you create and execute machine learning models in BigQuery ML by using standard SQL queries. With Gemini Enterprise Agent Platform, you can use pre-trained and custom tooling within a unified platform. After you register your BigQuery ML models in the Model Registry, you can manage them with your other ML models for versioning, evaluation, and deployment.

With this integration, you can choose which BigQuery ML models to register to the Model Registry. After you've registered your BigQuery ML models, you can deploy your BigQuery ML model to an endpoint for online inference.

To learn how to integrate your BigQuery ML models with Gemini Enterprise Agent Platform Model Registry, see [Manage BigQuery ML models in Gemini Enterprise Agent Platform](https://docs.cloud.google.com/bigquery/docs/managing-models-vertex).

## Limitations

  * You can't register [remote models](https://docs.cloud.google.com/bigquery/docs/bqml-introduction#remote_models).

  * The following models can be registered in Model Registry, but they can't be deployed in Agent Platform:

    * [Imported XGBoost models](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-xgboost)
    * [`ARIMA_PLUS` models](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-time-series)
    * [`ARIMA_PLUS_XREG` models](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-multivariate-time-series)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
