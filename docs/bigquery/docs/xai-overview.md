---
url: https://docs.cloud.google.com/bigquery/docs/xai-overview/
title: BigQuery Explainable AI overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:52:10.060371+00:00
---

# BigQuery Explainable AI overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/xai-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# BigQuery Explainable AI overview

This document describes how BigQuery ML supports Explainable artificial intelligence (AI), sometimes called XAI.

Explainable AI helps you understand the results that your predictive machine learning model generates for classification and regression tasks by defining how each feature in a row of data contributed to the predicted result. This information is often referred to as feature attribution. You can use this information to verify that the model is behaving as expected, to recognize biases in your models, and to inform ways to improve your model and your training data.

## Local versus global explainability

There are two types of explainability: local explainability and global explainability. These are also known respectively as _local feature importance_ and _global feature importance_.

  * Local explainability returns feature attribution values for each explained example. These values describe how much a particular feature affected the prediction relative to the baseline prediction.
  * Global explainability returns the feature's overall influence on the model and is often obtained by aggregating the feature attributions over the entire dataset. A higher absolute value indicates the feature had a greater influence on the model's predictions.



## Explainable AI offerings in BigQuery ML

Explainable AI in BigQuery ML supports a variety of machine learning models, including both time series and non-time series models. Each of the models takes advantage of a different explainability method.

Model category | Model types | Explainability method | Basic explanation of the method | Local explain functions | Global explain functions  
---|---|---|---|---|---  
Supervised models | [Linear & Logistic Regression](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-glm) | [Shapley values](https://christophm.github.io/interpretable-ml-book/shapley.html#the-shapley-value-in-detail) | Shapley values for linear models are equal to `model weight * feature value`, where feature values are standardized and model weights are trained with the standardized feature values. | [`ML.EXPLAIN_PREDICT`1](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-explain-predict) | [`ML.GLOBAL_EXPLAIN`2](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-global-explain)  
[Standard Errors](https://en.wikipedia.org/wiki/Standard_error) and [P-values](https://en.wikipedia.org/wiki/P-value) | Standard errors and p-values are used for significance testing against the model weights. | N/A | [`ML.ADVANCED_WEIGHTS`4](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-advanced-weights)  
[Boosted trees](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-boosted-tree)  
  
[Random forest](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-random-forest) | [Tree SHAP](https://docs.seldon.io/projects/alibi/en/stable/methods/TreeSHAP.html) | Tree SHAP is an algorithm to compute exact [SHAP values](https://christophm.github.io/interpretable-ml-book/shap.html) for decision tree-based models. | [`ML.EXPLAIN_PREDICT`1](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-explain-predict) | [`ML.GLOBAL_EXPLAIN`2](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-global-explain)  
[Approximate Feature Contribution](http://blog.datadive.net/interpreting-random-forests/) | Approximates the feature contribution values. It is faster and simpler compared to Tree SHAP. | [`ML.EXPLAIN_PREDICT`1](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-explain-predict) | [`ML.GLOBAL_EXPLAIN`2](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-global-explain)  
[Gini Index-based feature importance](https://xgboost.readthedocs.io/en/latest/python/python_api.html#xgboost.XGBRegressor.feature_importances_) | A global feature importance score that indicates how useful or valuable each feature was in the construction of the boosted tree or random forest model during training. | N/A | [`ML.FEATURE_IMPORTANCE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-importance)  
[AutoML Tables](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-automl) | [Sampled Shapley](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview#compare-methods) | Sampled Shapley assigns credit for the model's outcome to each feature, and considers different permutations of the features. This method provides a sampling approximation of exact Shapley values.  | N/A | [`ML.GLOBAL_EXPLAIN`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-global-explain)2  
Time series models | [ARIMA_PLUS](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-time-series) | [Time series decomposition](https://otexts.com/fpp2/decomposition.html) | Decomposes the time series into multiple components if those components are present in the time series. The components include trend, seasonal, holiday, step changes, and spike and dips. See ARIMA_PLUS [modeling pipeline](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-time-series#modeling-pipeline) for more details. | [`ML.EXPLAIN_FORECAST`3](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-explain-forecast) | N/A  
[ARIMA_PLUS_XREG](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-multivariate-time-series) | [Time series decomposition](https://otexts.com/fpp2/decomposition.html)  
and   
[Shapley values](https://christophm.github.io/interpretable-ml-book/shapley.html#the-shapley-value-in-detail) | Decomposes the time series into multiple components, including trend, seasonal, holiday, step changes, and spike and dips (similar to [ARIMA_PLUS](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-time-series)). Attribution of each external regressor is calculated based on Shapley Values, which is equal to `model weight * feature value`. | [`ML.EXPLAIN_FORECAST`3](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-explain-forecast) | N/A  
  
1`ML_EXPLAIN_PREDICT` is an extended version of `ML.PREDICT`.

2`ML.GLOBAL_EXPLAIN` returns the global explainability obtained by taking the mean absolute attribution that each feature receives for all the rows in the evaluation dataset.

3`ML.EXPLAIN_FORECAST` is an extended version of `ML.FORECAST`.

4`ML.ADVANCED_WEIGHTS` is an extended version of `ML.WEIGHTS`.

## What's next

  * For more information about supported SQL statements and functions for models that support explainability, see [End-to-end user journeys for ML models](https://docs.cloud.google.com/bigquery/docs/e2e-journey).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
