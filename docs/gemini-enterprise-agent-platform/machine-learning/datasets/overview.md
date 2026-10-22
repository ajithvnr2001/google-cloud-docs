---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/datasets/overview/
title: Overview of creating managed datasets on Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:45:05.164498+00:00
---

# Overview of creating managed datasets on Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/datasets/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Overview of creating managed datasets on Gemini Enterprise Agent Platform Stay organized with collections  Save and categorize content based on your preferences. 

You can use a managed dataset to provide the source data used to train AutoML and custom models on Gemini Enterprise Agent Platform. A managed dataset is required for AutoML and is optional for custom training.

## Permissions and access control

When you use data from a Cloud Storage bucket to create a dataset, Agent Platform requires permissions to access the data. Agent Platform uses a special Google-managed service account known as a Service Agent to securely access your data. For more information on the roles required and how the Service Agent works, see [Access control with IAM](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control#service-agents).

## Create a managed dataset for AutoML models

You can create managed datasets for training AutoML models by using the Google Cloud console or the Agent Platform API. The instructions for how to do this slightly vary based on your data type and model objective. Start by preparing your training data.

### Image

Learn how to create a managed dataset for the following types of image AutoML models:

  * [Image classification models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/classification/prepare-data)
  * [Image object detection models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/object-detection/prepare-data)



### Tabular

Learn how to create a managed dataset for the following types of tabular AutoML models:

  * [Tabular classification and regression models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/classification-regression/prepare-data)
  * [Tabular forecasting models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/forecasting/prepare-data)



## Create a managed dataset for custom trained models

The instructions on how to create a managed dataset for training custom models are the same, regardless of your data type or model objective.

For details, see [Use managed datasets](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/using-managed-datasets).

## View managed datasets using Knowledge Catalog

Knowledge Catalog is a fully managed, scalable metadata management service integrated with Agent Platform that provides a centralized location to search for datasets across projects and regions.

You can use Knowledge Catalog to discover, understand, and enrich your data with aspects.

For details on managing metadata and aspects for your Agent Platform resources, see [Manage aspects and enrich metadata](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata) in the [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
