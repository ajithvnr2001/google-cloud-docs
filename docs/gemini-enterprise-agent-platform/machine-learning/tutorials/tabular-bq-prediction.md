---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/tabular-bq-prediction/
title: Train a model using Gemini Enterprise Agent Platform and the Python SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:43:18.278741+00:00
---

# Train a model using Gemini Enterprise Agent Platform and the Python SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/tabular-bq-prediction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Train a model using Gemini Enterprise Agent Platform and the Python SDK Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial takes between 30 and 60 minutes to complete. 

This tutorial is a start-to-finish guide that shows you how to use the Agent Platform SDK for Python to create a custom-trained model. You run code in a notebook (IPYNB) file that uses a Docker container to train and create the model. The tutorial is for data scientists who are new to Gemini Enterprise Agent Platform and familiar with notebooks, Python, and the Machine Learning (ML) workflow.

The process starts using the Google Cloud console to create the project that contains your work. In your project, you use Vertex AI Workbench to create a Jupyter notebook. The notebook environment is where you run code that downloads and prepares a dataset, then use the dataset to create and train a model. At the end of the tutorial, the trained model generates predictions.

The goal of this tutorial is to walk you through every step required to create predictions in less than an hour. The dataset used is relatively small so that it doesn't take very long to train your model. When you're done, you can apply what you learn to larger datasets. The larger your dataset is, the more accurate your predictions are.

## Tutorial steps

  1. [Prerequisites](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/tabular-bq-prediction/prerequisites) \- Create your Google Cloud account and project.

  2. [Create a notebook](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/tabular-bq-prediction/create-notebook) \- Create and prepare a Jupyter notebook and its environment. You use the notebook to run code that creates your dataset, creates and trains your model, and generates your predictions.

  3. [Create a dataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/tabular-bq-prediction/create-dataset) \- Download a publicly available BigQuery dataset, then use it to create a Gemini Enterprise Agent Platform tabular dataset. The dataset contains the data you use to train your model. 

  4. [Create a training script](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/tabular-bq-prediction/create-training-script) \- Create a Python script that you pass to your training job. The script runs when the training job trains and creates your model.

  5. [Train a model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/tabular-bq-prediction/train-and-deploy-model) \- Use your tabular dataset to train and deploy a model. You use the model to create your predictions.

  6. [Make predictions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/tabular-bq-prediction/make-prediction) \- Use your model to create predictions. This section also walks you through deleting resources you create while running this tutorial so you don't incur unnecessary charges.




## What you accomplish

This tutorial walks you through how to use the Agent Platform SDK for Python to do the following:

  * Create a Cloud Storage bucket to store a dataset
  * Preprocess data for training
  * Use the processed data to create a dataset in BigQuery
  * Use the BigQuery dataset to create a Gemini Enterprise Agent Platform tabular dataset
  * Create and train a custom-trained model
  * Deploy the custom-trained model to an endpoint
  * Generate a prediction
  * Undeploy the model
  * Delete all resources created in the tutorial so you don't incur further charges



## Billable resources used

This tutorial uses billable resources associated with the Gemini Enterprise Agent Platform, BigQuery, and Cloud Storage Google Cloud services. If you're new to Google Cloud, you might be able to use one or more of these services at no cost. Gemini Enterprise Agent Platform offers $300 in free credits to new customers, and Cloud Storage and BigQuery have [free tiers](https://cloud.google.com/free). For more information, see the following:

  * [Gemini Enterprise Agent Platform pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing) and [Free cloud features and trial offer](https://cloud.google.com/free/docs/free-cloud-features#free-trial)
  * [BigQuery pricing](https://cloud.google.com/bigquery/pricing) and [BigQuery free tier usage](https://cloud.google.com/free/docs/free-cloud-features#bigquery)
  * [Cloud Storage pricing](https://cloud.google.com/storage/pricing) and [Cloud Storage free tier usage](https://cloud.google.com/free/docs/free-cloud-features#storage)
  * [Google Cloud pricing calculator](https://cloud.google.com/products/calculator)



To prevent further charges, the final step of this tutorial walks you through removing all billable Google Cloud resources you created.

[ Next Prerequisites  arrow_forward  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/tabular-bq-prediction/prerequisites)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
