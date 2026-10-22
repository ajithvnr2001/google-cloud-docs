---
url: https://docs.cloud.google.com/bigquery/docs/preventing-overfitting/
title: Prevent overfitting \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:28.518426+00:00
---

# Prevent overfitting  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/preventing-overfitting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Prevent overfitting

A common pitfall when training a BigQuery ML model is [overfitting](https://developers.google.com/machine-learning/glossary/#overfitting). Overfitting occurs when the model matches the training data too closely, causing it to perform poorly on new data. BigQuery ML supports two methods for preventing overfitting: [early stopping](https://developers.google.com/machine-learning/glossary/#early_stopping) and [regularization](https://developers.google.com/machine-learning/glossary/#regularization).

To learn how to modify the options described below, see [the `CREATE MODEL` statement](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create#model_option_list).

## Early stopping

Early stopping is the default option for overfitting prevention in BigQuery ML. When early stopping is enabled, the [loss](https://developers.google.com/machine-learning/glossary/#loss) on the [holdout data](https://developers.google.com/machine-learning/glossary/#holdout_data) is monitored during training, and training is halted once the loss improvement in the latest iteration falls below a threshold. Since the holdout data is not used during training, it is a good estimate of the model's loss on new data. The `early_stop`, `min_rel_progress`, `data_split_method`, and `data_split_eval_fraction` options control the behavior of early stopping.

## Regularization

Regularization keeps the [model weights](https://developers.google.com/machine-learning/glossary/#weight) from growing too large, preventing the model from matching the training data too closely. BigQuery ML supports two methods for controlling the size of the model weights: [L1 regularization](https://developers.google.com/machine-learning/glossary/#L1_regularization) and [L2 regularization](https://developers.google.com/machine-learning/glossary/#L2_regularization).

By default, the values of `l1_reg` and `l2_reg` are zero, which disables regularization. On some datasets, setting positive values for `l1_reg` and `l2_reg` will improve the trained model's performance on new data. The best values for the regularization parameters are typically found through trial-and-error, and it is common to experiment with values across several orders of magnitude (for example, 0.01, 0.1, 1, 10, and 100).

Here is some general advice on using regularization:

  * If you are experimenting with the regularization parameters, try disabling early stopping so that the effect of regularization is clear.

  * If the number of features is large compared to the size of the training set, try large values for the regularization parameters. The risk of overfitting is greater when there are only a few observations per feature.

  * If you are concerned that many features may be irrelevant for predicting the label, try setting `l1_reg` to be larger than `l2_reg` and vice versa. There is [theoretical evidence](http://www.robotics.stanford.edu/%7Eang/papers/icml04-l1l2.ps) that L1 regularization works better when many features are irrelevant.




Another benefit of L1 regularization is that it tends to set many model weights to exactly zero, which is helpful for identifying the most relevant features and training a compact model.

## What's next

  * For an overview of BigQuery ML, see [Introduction to BigQuery ML](https://docs.cloud.google.com/bigquery/docs/bqml-introduction).
  * To get started using BigQuery ML, see [Create machine learning models in BigQuery ML](https://docs.cloud.google.com/bigquery/docs/create-machine-learning-model).
  * To learn more about working with models, see: 
    * [Get model metadata](https://docs.cloud.google.com/bigquery/docs/getting-model-metadata)
    * [List models](https://docs.cloud.google.com/bigquery/docs/listing-models)
    * [Update model metadata](https://docs.cloud.google.com/bigquery/docs/updating-model-metadata)
    * [Manage models](https://docs.cloud.google.com/bigquery/docs/managing-models)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
