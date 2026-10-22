---
url: https://docs.cloud.google.com/bigquery/docs/model-overview/
title: Model creation \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:43.260643+00:00
---

# Model creation  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/model-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Model creation

BigQuery ML lets you build and operationalize machine learning (ML) models over data in BigQuery by using SQL.

A typical model development workflow in BigQuery ML looks similar to the following:

  1. Create the model using the [`CREATE MODEL` statement](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create).
  2. Perform feature preprocessing. Some preprocessing happens [automatically](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-auto-preprocessing), plus you can use [manual preprocessing functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-preprocessing-functions) inside the [`TRANSFORM` clause](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create#transform) to do additional preprocessing.
  3. Refine the model by performing [hyperparameter tuning](https://docs.cloud.google.com/bigquery/docs/hp-tuning-overview) to fit the model to the training data.
  4. [Evaluate the model](https://docs.cloud.google.com/bigquery/docs/evaluate-overview) to assess how it might perform on data outside of the training set, and also to compare it to other models if appropriate.
  5. [Perform inference](https://docs.cloud.google.com/bigquery/docs/inference-overview) to analyze data by using the model.
  6. Provide [explainability](https://docs.cloud.google.com/bigquery/docs/xai-overview) for the model, to clarify how particular features influenced a given prediction and also the model overall.
  7. Learn more about the components that comprise the model by using [model weights](https://docs.cloud.google.com/bigquery/docs/weights-overview).



Because you can use many different kinds of models in BigQuery ML, the functions available for each model vary. For more information about supported SQL statements and functions for each model type, see the following documents:

  * [End-to-end user journey for generative AI models](https://docs.cloud.google.com/bigquery/docs/e2e-journey-genai)
  * [End-to-end user journey for time series forecasting models](https://docs.cloud.google.com/bigquery/docs/e2e-journey-forecast)
  * [End-to-end user journey for ML models](https://docs.cloud.google.com/bigquery/docs/e2e-journey)
  * [End-to-end user journey for imported models](https://docs.cloud.google.com/bigquery/docs/e2e-journey-import)
  * [Contribution analysis user journey](https://docs.cloud.google.com/bigquery/docs/contribution-analysis#contribution_analysis_user_journey)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
