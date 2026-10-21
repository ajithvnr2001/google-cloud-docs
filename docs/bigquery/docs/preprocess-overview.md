---
url: https://docs.cloud.google.com/bigquery/docs/preprocess-overview/
title: Feature preprocessing overview \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:05:24.811164+00:00
---

# Feature preprocessing overview  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/preprocess-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Feature preprocessing overview

_Feature preprocessing_ is one of the most important steps in the machine learning lifecycle. It consists of creating features and cleaning the training data. Creating features is also referred as _feature engineering_.

BigQuery ML provides the following feature preprocessing techniques:

  * **Automatic preprocessing**. BigQuery ML performs automatic preprocessing during training. For more information, see [Automatic feature preprocessing](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-auto-preprocessing).

  * **Manual preprocessing**. You can use the [`TRANSFORM` clause](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create#transform) in the `CREATE MODEL` statement to define custom preprocessing using [manual preprocessing functions](https://docs.cloud.google.com/bigquery/docs/manual-preprocessing#types_of_preprocessing_functions). You can also use these functions outside of the `TRANSFORM` clause to process training data before creating the model.




## Get feature information

You can use the [`ML.FEATURE_INFO` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-feature) to retrieve the statistics of all input feature columns.

## Recommended knowledge

By using the default settings in the `CREATE MODEL` statements and the inference functions, you can create and use BigQuery ML models even without much ML knowledge. However, having basic knowledge about the ML development lifecycle, such as feature engineering and model training, helps you optimize both your data and your model to deliver better results. We recommend using the following resources to develop familiarity with ML techniques and processes:

  * [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
  * [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning)
  * [Data Cleaning](https://www.kaggle.com/learn/data-cleaning)
  * [Feature Engineering](https://www.kaggle.com/learn/feature-engineering)
  * [Intermediate Machine Learning](https://www.kaggle.com/learn/intermediate-machine-learning)



## What's next

  * Learn about [feature serving](https://docs.cloud.google.com/bigquery/docs/feature-serving) in BigQuery ML.
  * For more information about supported SQL statements and functions for models that support feature preprocessing, see the following documents:

    * [End-to-end user journeys for ML models](https://docs.cloud.google.com/bigquery/docs/e2e-journey)
    * [End-to-end user journeys for time series forecasting models](https://docs.cloud.google.com/bigquery/docs/e2e-journey-forecast)
    * [Contribution analysis user journey](https://docs.cloud.google.com/bigquery/docs/contribution-analysis#contribution_analysis_user_journey)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
