---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/tabular-automl/dataset-train/
title: Hello tabular data: Create a dataset and train an AutoML classification model \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:47.585208+00:00
---

# Hello tabular data: Create a dataset and train an AutoML classification model  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/tabular-automl/dataset-train/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Hello tabular data: Create a dataset and train an AutoML classification model Stay organized with collections  Save and categorize content based on your preferences. 

Use the Google Cloud console to create a tabular dataset and train a classification model.

## Create a tabular dataset

  1. In the Google Cloud console, in the Agent Platform section, go to the **Datasets** page.

[Go to the Datasets page](https://console.cloud.google.com/agent-platform/datasets)

  2. Click **Create** in the button bar to create a new dataset.

  3. Enter `Structured_AutoML_Tutorial` for the dataset name and select the **Tabular** tab.

  4. Select the **Regression/Classification** objective.

Leave the **Region** set to **us-central1**.

  5. Click **Create** to create the dataset.

For this tutorial, you'll use a publicly available bank dataset hosted on Cloud Storage.

  6. For **Select a data source** , click **Select CSV files from Cloud Storage**

  7. In **Import file path** , enter `cloud-ml-tables-data/bank-marketing.csv`

  8. Click **Continue**.




## Analyze the dataset

The analyze section lets you view more information about the dataset, like missing or NULL values.

Because our dataset is formatted correctly for this tutorial, you don't need to do anything on this page and can skip this section.

  1. **Optional**. Click **Generate statistics** to view the number of missing or NULL values in the dataset. This can take 10 minutes or longer.

  2. **Optional**. Click on one of the feature columns to learn more about the data values.




## Train an AutoML classification model

  1. Click **Train new model**.

  2. Select **Other**.

  3. In the **Training method** pane, confirm that the dataset you created previously is selected for the **Dataset** field.

  4. For the **Objective** field, select **Classification**.

  5. Confirm that the AutoML training method is selected.

  6. Click **Continue**.

  7. In the **Model details** pane, select **Deposit** for the target column and click **Continue**.

The target column is what we're training the model to predict. For the `bank-marketing.csv` dataset, the `Deposit` column indicates whether the client purchased a term deposit (2 = yes, 1 = no).

The **Training options** pane gives you an opportunity to add features and transform column data. If no columns are selected, then by default all non- target columns will be used as features for training. This dataset is ready to use, so there's no need to apply any transformations.

  8. Click **Continue**.

  9. In the **Compute and pricing** pane, enter `1` for the training budget.

The training budget is the maximum time (may vary slightly) that the model spends training. This value is multiplied by the [price per node hour](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing#automl_models) to calculate to total training cost. More training hours results in a more accurate (up to a point) model but results in a higher cost. For development purposes, a low budget is fine but for production it's important to strike a balance between cost and accuracy.

  10. Click **Start training**.




When the model finishes training, it's displayed in the model tab as a live link, with a green checkmark status icon.

## What's next

Your model is now being trained, which can take an hour or more to complete. You'll receive an email when training is complete. When your model has finished training, follow the [next page of this tutorial](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/tabular-automl/deploy-predict) to deploy your model and request a prediction.

This tutorial uses a dataset that's been cleaned and formatted for AutoML training, but most data will require some work before it's ready to be used. The quality of your training data impacts the effectiveness of the models you create. [Learn more](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/classification-regression/prepare-data) about preparing data.

Sourcing and preparing your data is a critical to ensuring an accurate machine learning model. [Learn more](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/bp-tabular) about best practices.

[Learn more](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/classification-regression/create-dataset) about creating a tabular dataset.

Gemini Enterprise Agent Platform offers two model training methods, AutoML and custom training. AutoML lets you train with minimal effort and machine learning experience, while custom training gives you complete control over training functionality. [Learn more](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/training-methods) about training methods.

Gemini Enterprise Agent Platform examines the source data type and feature values and infers how it will use that feature in model training. It's recommended that you review each column's data type to verify that it's been interpreted correctly. If needed, you can specify a different supported transformation for any feature. [Learn more](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/datasets/data-types-tabular) about transformations.

[Learn more](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/classification-regression/train-model) about training an AutoML for classification or regression.

[ Previous arrow_back  Set up your project and environment  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/tabular-automl/setup)

[ Next Deploy a model and request an inference  arrow_forward  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/tabular-automl/deploy-predict)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
