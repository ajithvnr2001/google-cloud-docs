---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/python-sdk/python-sdk-class-overview/
title: Agent Platform SDK class overview \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:43:42.659042+00:00
---

# Agent Platform SDK class overview  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/python-sdk/python-sdk-class-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Agent Platform SDK class overview Stay organized with collections  Save and categorize content based on your preferences. 

Data scientists and machine learning (ML) developers use the Agent Platform SDK for Python to build, train, and deploy models in a custom ML workflow. This includes creating datasets and uploading data, training an ML model, uploading and storing your model, deploying your model, running batch prediction jobs, and managing your models and endpoints.

The Agent Platform SDK also includes classes to create generative AI solutions with text, code, chat, and text embedding foundation models. You can use these classes to generate text, create a text or code chatbot, tune a foundation model, and create a text embedding. A text embedding is text in the form of a vector used to search for items. For more information, see [Agent Platform SDK language model classes](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/vertexai).

You can use the Agent Platform SDK for Python in hosted JupyterLab notebooks within Gemini Enterprise Agent Platform to write and run your code. The notebooks include preinstalled ML frameworks, such as TensorFlow and PyTorch. You can also use other notebooks, such as Colab notebooks, or use a developer environment of your choice that supports Python.

If you want to try using the Agent Platform SDK for Python right now, see the following resources:

  * [Introduction to the Agent Platform SDK for Python](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/python-sdk/use-python-sdk)
  * [Agent Platform SDK reference](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform)
  * [Agent Platform SDK language model reference](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/vertexai)
  * [Train a model using Gemini Enterprise Agent Platform and the Python SDK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/tabular-bq-prediction)



The Agent Platform SDK includes many classes to help you automate data ingestion, train models, and get predictions. It also includes classes to help you monitor, evaluate, and optimize your machine learning (ML) workflow. The classes can be loosely grouped into the following categories:

  * [Data classes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/python-sdk/data-classes) include classes that work with structured data, unstructured data, and the Gemini Enterprise Agent Platform Feature Store.
  * [Training classes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/python-sdk/training-classes) include classes that work with AutoML training for structured and unstructured data, custom training, hyperparameter training, and pipeline training.
  * [Model classes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/python-sdk/model-classes) work with models and model evaluations.
  * [Prediction classes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/python-sdk/prediction-classes) work with batch predictions, online predictions, and Vector Search predictions.
  * [Tracking classes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/python-sdk/tracking-classes) work with Gemini Enterprise Agent Platform ML Metadata, Experiments on Agent Platform, and Vertex AI TensorBoard.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
