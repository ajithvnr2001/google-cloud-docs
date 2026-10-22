---
url: https://docs.cloud.google.com/bigquery/docs/e2e-journey/
title: End-to-end user journeys for ML models \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:24.228193+00:00
---

# End-to-end user journeys for ML models  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/e2e-journey/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# End-to-end user journeys for ML models

This document describes the user journeys for machine learning (ML) models that are trained in BigQuery ML, including the statements and functions that you can use to work with ML models. BigQuery ML offers the following types of ML models:

  * [Supervised learning](https://developers.google.com/machine-learning/glossary/fundamentals#supervised-machine-learning) models:

    * [Linear and logistic regression](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-glm)
    * [Deep neural network (DNN)](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-dnn-models)
    * [Wide & Deep](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-wnd-models)
    * [Boosted trees](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-boosted-tree)
    * [Random forest](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-random-forest)
    * [AutoML](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-automl)
  * [Unsupervised learning](https://developers.google.com/machine-learning/glossary/fundamentals#unsupervised-machine-learning) models:

    * [K-means clustering](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-kmeans)
    * [Matrix factorization](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-matrix-factorization)
    * [Autoencoder](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-autoencoder)
    * [Principal component analysis (PCA)](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-pca)
  * [Transform-only](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-transform) models: Transform-only models aren't typical ML models but are instead artifacts that transform raw data into features.




## Model creation user journeys

The following table describes the statements and functions you can use to create and tune models:

Model category | Model type | Model creation | [Feature preprocessing](https://docs.cloud.google.com/bigquery/docs/preprocess-overview) | [Hyperparameter tuning](https://docs.cloud.google.com/bigquery/docs/hp-tuning-overview)1 | [Model weights](https://docs.cloud.google.com/bigquery/docs/weights-overview) | Feature & training info | Tutorials  
---|---|---|---|---|---|---|---  
Supervised learning | Linear & logistic regression | [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-glm) |  [Automatic preprocessing](https://docs.cloud.google.com/bigquery/docs/auto-preprocessing)  
  
[Manual preprocessing](https://docs.cloud.google.com/bigquery/docs/manual-preprocessing) |  [Hyperparameter tuning](https://docs.cloud.google.com/bigquery/docs/hp-tuning-overview)  
  
[`ML.TRIAL  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-trial-info) | [`ML.WEIGHTS`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-weights) |  [`ML.FEATURE  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-feature)  
  
[`ML.TRAINING  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-train) |  [Use linear regression to predict penguin weight](https://docs.cloud.google.com/bigquery/docs/linear-regression-tutorial)   
  
[Perform classification with a logistic regression model](https://docs.cloud.google.com/bigquery/docs/logistic-regression-prediction)  
Deep neural networks (DNN) | [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-dnn-models) |  [Automatic preprocessing](https://docs.cloud.google.com/bigquery/docs/auto-preprocessing)  
  
[Manual preprocessing](https://docs.cloud.google.com/bigquery/docs/manual-preprocessing) |  [Hyperparameter tuning](https://docs.cloud.google.com/bigquery/docs/hp-tuning-overview)  
  
[`ML.TRIAL  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-trial-info) | N/A2 |  [`ML.FEATURE  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-feature)  
  
[`ML.TRAINING  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-train) | N/A  
Wide & Deep networks | [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-wnd-models) |  [Automatic preprocessing](https://docs.cloud.google.com/bigquery/docs/auto-preprocessing)  
  
[Manual preprocessing](https://docs.cloud.google.com/bigquery/docs/manual-preprocessing) |  [Hyperparameter tuning](https://docs.cloud.google.com/bigquery/docs/hp-tuning-overview)  
  
[`ML.TRIAL  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-trial-info) | N/A2 |  [`ML.FEATURE  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-feature)  
  
[`ML.TRAINING  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-train) | N/A  
Boosted trees | [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-boosted-tree) |  [Automatic preprocessing](https://docs.cloud.google.com/bigquery/docs/auto-preprocessing)  
  
[Manual preprocessing](https://docs.cloud.google.com/bigquery/docs/manual-preprocessing) |  [Hyperparameter tuning](https://docs.cloud.google.com/bigquery/docs/hp-tuning-overview)  
  
[`ML.TRIAL  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-trial-info) | N/A2 |  [`ML.FEATURE  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-feature)  
  
[`ML.TRAINING  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-train) | [Perform classification with a boosted trees model](https://docs.cloud.google.com/bigquery/docs/boosted-tree-classifier-tutorial)  
Random forest | [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-random-forest) |  [Automatic preprocessing](https://docs.cloud.google.com/bigquery/docs/auto-preprocessing)  
  
[Manual preprocessing](https://docs.cloud.google.com/bigquery/docs/manual-preprocessing) |  [Hyperparameter tuning](https://docs.cloud.google.com/bigquery/docs/hp-tuning-overview)  
  
[`ML.TRIAL  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-trial-info) | N/A2 |  [`ML.FEATURE  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-feature)  
  
[`ML.TRAINING  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-train) | N/A  
AutoML classification & regression | [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-automl) | AutoML automatically performs feature engineering | AutoML automatically performs hyperparameter tuning | N/A2 |  [`ML.FEATURE  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-feature)  
  
[`ML.TRAINING  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-train) | N/A  
Unsupervised learning | K-means | [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-kmeans) |  [Automatic preprocessing](https://docs.cloud.google.com/bigquery/docs/auto-preprocessing)  
  
[Manual preprocessing](https://docs.cloud.google.com/bigquery/docs/manual-preprocessing) |  [Hyperparameter tuning](https://docs.cloud.google.com/bigquery/docs/hp-tuning-overview)  
  
[`ML.TRIAL  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-trial-info) | [`ML.CENTROIDS`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-centroids) |  [`ML.FEATURE  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-feature)  
  
[`ML.TRAINING  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-train) | [Find clusters in bike station data](https://docs.cloud.google.com/bigquery/docs/kmeans-tutorial)  
Matrix factorization | [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-matrix-factorization) | N/A |  [Hyperparameter tuning](https://docs.cloud.google.com/bigquery/docs/hp-tuning-overview)  
  
[`ML.TRIAL  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-trial-info) | [`ML.WEIGHTS`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-weights) |  [`ML.FEATURE  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-feature)  
  
[`ML.TRAINING  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-train) |  [Generate movie recommendations using explicit feedback](https://docs.cloud.google.com/bigquery/docs/bigqueryml-mf-explicit-tutorial)   
  
[Generate content recommendations using implicit feedback](https://docs.cloud.google.com/bigquery/docs/bigqueryml-mf-implicit-tutorial)  
Principal component analysis (PCA) | [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-pca) |  [Automatic preprocessing](https://docs.cloud.google.com/bigquery/docs/auto-preprocessing)  
  
[Manual preprocessing](https://docs.cloud.google.com/bigquery/docs/manual-preprocessing) | N/A |  [`ML.PRINCIPAL  
_COMPONENTS`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-principal-components)  
  
[`ML.PRINCIPAL  
_COMPONENT  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-principal-component-info) |  [`ML.FEATURE  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-feature)  
  
[`ML.TRAINING  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-train) | N/A  
Autoencoder | [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-autoencoder) |  [Automatic preprocessing](https://docs.cloud.google.com/bigquery/docs/auto-preprocessing)  
  
[Manual preprocessing](https://docs.cloud.google.com/bigquery/docs/manual-preprocessing) |  [Hyperparameter tuning](https://docs.cloud.google.com/bigquery/docs/hp-tuning-overview)  
  
[`ML.TRIAL  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-trial-info) | N/A2 |  [`ML.FEATURE  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-feature)  
  
[`ML.TRAINING  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-train) | N/A  
Transform-only | Transform-only | [`CREATE MODEL`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-transform) | [Manual preprocessing](https://docs.cloud.google.com/bigquery/docs/manual-preprocessing) | N/A | N/A | [`ML.FEATURE  
_INFO`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-feature) | N/A  
  
1For a step-by-step example of using hyperparameter tuning, see [Improve model performance with hyperparameter tuning](https://docs.cloud.google.com/bigquery/docs/hyperparameter-tuning-tutorial).

2BigQuery ML doesn't offer a function to retrieve the weights for this model. To see the weights of the model, you can export the model from BigQuery ML to Cloud Storage and then use the XGBoost library or the TensorFlow library to visualize the tree structure for tree models or the graph structure for neural networks. For more information, see [`EXPORT MODEL`](https://docs.cloud.google.com/bigquery/docs/exporting-models) and [Export a BigQuery ML model for online prediction](https://docs.cloud.google.com/bigquery/docs/export-model-tutorial).

## Model use user journeys

The following table describes the statements and functions you can use to evaluate, explain, and get predictions from models:

Model category | Model type | [Evaluation](https://docs.cloud.google.com/bigquery/docs/evaluate-overview) | [Inference](https://docs.cloud.google.com/bigquery/docs/inference-overview) | [AI explanation](https://docs.cloud.google.com/bigquery/docs/xai-overview) | [Model monitoring](https://docs.cloud.google.com/bigquery/docs/model-monitoring-overview)  
---|---|---|---|---|---  
Supervised learning | Linear & logistic regression |  [`ML.EVALUATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-evaluate)  
  
[`ML.CONFUSION  
_MATRIX`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-confusion)1  
  
[`ML.ROC_CURVE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-roc)2 |  [`ML.PREDICT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-predict)  
  
[`ML.TRANSFORM`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-transform) |  [`ML.EXPLAIN_PREDICT`3](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-explain-predict)  
  
[`ML.GLOBAL_EXPLAIN`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-global-explain)  
  
[`ML.ADVANCED_WEIGHTS`5](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-advanced-weights) |  [`ML.DESCRIBE_DATA`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-describe-data)  
  
[`ML.VALIDATE_DATA  
_DRIFT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-drift)  
  
[`ML.VALIDATE_DATA  
_SKEW`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-skew)  
  
[`ML.TFDV_DESCRIBE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-tfdv-describe)  
  
[`ML.TFDV_VALIDATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-tfdv-validate)  
Deep neural networks (DNN) |  [`ML.EVALUATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-evaluate)  
  
[`ML.CONFUSION  
_MATRIX`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-confusion)1  
  
[`ML.ROC_CURVE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-roc)2 |  [`ML.PREDICT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-predict)  
  
[`ML.TRANSFORM`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-transform) | N/A |  [`ML.DESCRIBE_DATA`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-describe-data)  
  
[`ML.VALIDATE_DATA  
_DRIFT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-drift)  
  
[`ML.VALIDATE_DATA  
_SKEW`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-skew)  
  
[`ML.TFDV_DESCRIBE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-tfdv-describe)  
  
[`ML.TFDV_VALIDATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-tfdv-validate)  
Wide & Deep networks |  [`ML.EVALUATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-evaluate)  
  
[`ML.CONFUSION  
_MATRIX`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-confusion)1  
  
[`ML.ROC_CURVE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-roc)2 |  [`ML.PREDICT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-predict)  
  
[`ML.TRANSFORM`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-transform) | N/A |  [`ML.DESCRIBE_DATA`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-describe-data)  
  
[`ML.VALIDATE_DATA  
_DRIFT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-drift)  
  
[`ML.VALIDATE_DATA  
_SKEW`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-skew)  
  
[`ML.TFDV_DESCRIBE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-tfdv-describe)  
  
[`ML.TFDV_VALIDATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-tfdv-validate)  
Boosted trees |  [`ML.EVALUATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-evaluate)  
  
[`ML.CONFUSION  
_MATRIX`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-confusion)1  
  
[`ML.ROC_CURVE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-roc)2 |  [`ML.PREDICT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-predict)  
  
[`ML.TRANSFORM`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-transform) |  [`ML.EXPLAIN_PREDICT`3](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-explain-predict)  
  
[`ML.GLOBAL_EXPLAIN`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-global-explain)  
  
[`ML.FEATURE_IMPORTANCE`4](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-importance) |  [`ML.DESCRIBE_DATA`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-describe-data)  
  
[`ML.VALIDATE_DATA  
_DRIFT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-drift)  
  
[`ML.VALIDATE_DATA  
_SKEW`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-skew)  
  
[`ML.TFDV_DESCRIBE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-tfdv-describe)  
  
[`ML.TFDV_VALIDATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-tfdv-validate)  
Random forest |  [`ML.EVALUATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-evaluate)  
  
[`ML.CONFUSION  
_MATRIX`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-confusion)1  
  
[`ML.ROC_CURVE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-roc)2 |  [`ML.PREDICT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-predict)  
  
[`ML.TRANSFORM`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-transform) |  [`ML.EXPLAIN_PREDICT`3](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-explain-predict)  
  
[`ML.GLOBAL_EXPLAIN`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-global-explain)  
  
[`ML.FEATURE_IMPORTANCE`4](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-importance) |  [`ML.DESCRIBE_DATA`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-describe-data)  
  
[`ML.VALIDATE_DATA  
_DRIFT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-drift)  
  
[`ML.VALIDATE_DATA  
_SKEW`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-skew)  
  
[`ML.TFDV_DESCRIBE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-tfdv-describe)  
  
[`ML.TFDV_VALIDATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-tfdv-validate)  
AutoML classification & regression |  [`ML.EVALUATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-evaluate)  
  
[`ML.CONFUSION  
_MATRIX`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-confusion)1  
  
[`ML.ROC_CURVE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-roc)2 | [`ML.PREDICT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-predict) | [`ML.GLOBAL_EXPLAIN`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-global-explain) |  [`ML.DESCRIBE_DATA`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-describe-data)  
  
[`ML.VALIDATE_DATA  
_DRIFT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-drift)  
  
[`ML.VALIDATE_DATA  
_SKEW`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-skew)  
  
[`ML.TFDV_DESCRIBE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-tfdv-describe)  
  
[`ML.TFDV_VALIDATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-tfdv-validate)  
Unsupervised learning | K-means | [`ML.EVALUATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-evaluate) | [`ML.PREDICT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-predict)  
[`ML.DETECT  
_ANOMALIES`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-detect-anomalies)  
  
[`ML.TRANSFORM`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-transform) | N/A |  [`ML.DESCRIBE_DATA`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-describe-data)   
  
[`ML.VALIDATE_DATA  
_DRIFT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-drift)   
  
[`ML.VALIDATE_DATA  
_SKEW`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-skew)   
  
[`ML.TFDV_DESCRIBE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-tfdv-describe)   
  
[`ML.TFDV_VALIDATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-tfdv-validate)  
Matrix factorization | [`ML.EVALUATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-evaluate) | [`ML.RECOMMEND`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-recommend)  
  
[`AI.GENERATE  
_EMBEDDING`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-embedding) | N/A | N/A  
Principal component analysis (PCA) | [`ML.EVALUATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-evaluate) | [`ML.PREDICT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-predict)  
[`AI.GENERATE  
_EMBEDDING`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-embedding)  
[`ML.DETECT  
_ANOMALIES`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-detect-anomalies)  
  
[`ML.TRANSFORM`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-transform) | N/A |  [`ML.DESCRIBE_DATA`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-describe-data)   
  
[`ML.VALIDATE_DATA  
_DRIFT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-drift)   
  
[`ML.VALIDATE_DATA  
_SKEW`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-skew)   
  
[`ML.TFDV_DESCRIBE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-tfdv-describe)   
  
[`ML.TFDV_VALIDATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-tfdv-validate)  
Autoencoder | [`ML.EVALUATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-evaluate) | [`ML.PREDICT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-predict)  
  
[`AI.GENERATE  
_EMBEDDING`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-embedding)  
[`ML.DETECT  
_ANOMALIES`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-detect-anomalies)  
  
[`ML.RECONSTRUCTION  
_LOSS`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-reconstruction-loss)  
  
[`ML.TRANSFORM`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-transform) | N/A |  [`ML.DESCRIBE_DATA`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-describe-data)   
  
[`ML.VALIDATE_DATA  
_DRIFT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-drift)   
  
[`ML.VALIDATE_DATA  
_SKEW`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-skew)   
  
[`ML.TFDV_DESCRIBE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-tfdv-describe)   
  
[`ML.TFDV_VALIDATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-tfdv-validate)  
Transform-only | Transform-only | N/A | [`ML.TRANSFORM`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-transform) | N/A | N/A  
  
1`ML.CONFUSION_MATRIX` is only applicable to classification models.

2`ML.ROC_CURVE` is only applicable to binary classification models.

3The `ML.EXPLAIN_PREDICT` function encompasses the `ML.PREDICT` function because its output is a superset of the results of `ML.PREDICT`.

4To understand the difference between `ML.GLOBAL_EXPLAIN` and `ML.FEATURE_IMPORTANCE`, see the [Explainable AI overview](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-xai-overview).

5The `ML.ADVANCED_WEIGHTS` function encompasses the `ML.WEIGHTS` function because its output is a superset of the results of `ML.WEIGHTS`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
