---
url: https://docs.cloud.google.com/bigquery/docs/regression-overview/
title: Regression overview \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:29.526247+00:00
---

# Regression overview  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/regression-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Regression overview

A common use case for machine learning is predicting the value of a numerical metric for new data by using a model trained on similar historical data. For example, you might want to predict a house's expected sale price. By using the house's location and characteristics as features, you can compare this house to similar houses that have already sold, and use their sales prices to estimate the house's sale price.

You can use any of the following models in combination with the [`ML.PREDICT` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-predict) to perform regression:

  * [Linear regression models](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-glm): use [linear regression](https://developers.google.com/machine-learning/crash-course/linear-regression) by setting the `MODEL_TYPE` option to `LINEAR_REG`.
  * [Boosted tree models](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-boosted-tree): use a [gradient boosted decision tree](https://developers.google.com/machine-learning/decision-forests/intro-to-gbdt) by setting the `MODEL_TYPE` option to `BOOSTED_TREE_REGRESSOR`.
  * [Random forest models](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-random-forest): use a [random forest](https://developers.google.com/machine-learning/decision-forests/intro-to-decision-forests) by setting the `MODEL_TYPE` option to `RANDOM_FOREST_REGRESSOR`.
  * [Deep neural network (DNN) models](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-dnn-models): use a [neural network](https://developers.google.com/machine-learning/crash-course/neural-networks) by setting the `MODEL_TYPE` option to `DNN_REGRESSOR`.
  * [Wide & Deep models](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-wnd-models): use [wide & deep learning](https://dl.acm.org/doi/10.1145/2988450.2988454) by setting the `MODEL_TYPE` option to `DNN_LINEAR_COMBINED_REGRESSOR`.
  * [AutoML models](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-automl): use an [AutoML classification model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/classification-regression/overview) by setting the `MODEL_TYPE` option to `AUTOML_REGRESSOR`.



Alternatively, you can use the [`AI.PREDICT` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-predict) to perform regression using the built-in [TabFM model](https://docs.cloud.google.com/bigquery/docs/tabfm-model). You can evaluate the performance of the model by using the [`AI.EVALUATE` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-evaluate).

## Recommended knowledge

By using the default settings in the `CREATE MODEL` statements and the `ML.PREDICT` function, you can create and use a regression model even without much ML knowledge. However, having basic knowledge about ML development helps you optimize both your data and your model to deliver better results. We recommend using the following resources to develop familiarity with ML techniques and processes:

  * [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
  * [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning)
  * [Intermediate Machine Learning](https://www.kaggle.com/learn/intermediate-machine-learning)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
