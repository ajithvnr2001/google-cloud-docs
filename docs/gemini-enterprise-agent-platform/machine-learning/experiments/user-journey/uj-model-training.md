---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/user-journey/uj-model-training/
title: Model training with prebuilt data pre-processing code: Notebook \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:02.408595+00:00
---

# Model training with prebuilt data pre-processing code: Notebook  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/user-journey/uj-model-training/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Model training with prebuilt data pre-processing code: Notebook Stay organized with collections  Save and categorize content based on your preferences. 

As a Data Scientist, this is a common workflow: Train a model locally (in my Notebook), log the parameters, log the training time series metrics to Vertex AI TensorBoard, and log the evaluation metrics.

As a Data Scientist, I want to be able to reuse data pre-processing code that others within my company have written to simplify and standardize all the complex data wrangling that we do. I want to be able to:

  1. Use a Python data pre-processing library to clean up an in memory dataset (a Pandas Dataframe), in a notebook.
  2. Train a model using Keras (again in a notebook).



## Notebook: Model experimentation with preprocessed data

To see an example of building a Vertex AI Experiments lineage for custom training, run the "Build Experiment lineage for custom training" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/experiments/build_model_experimentation_lineage_with_prebuild_code.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Fexperiments%2Fbuild_model_experimentation_lineage_with_prebuild_code.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Fexperiments%2Fbuild_model_experimentation_lineage_with_prebuild_code.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/experiments/build_model_experimentation_lineage_with_prebuild_code.ipynb)

In the "Build Vertex AI Experiments lineage for custom training" notebook, you'll learn how to integrate preprocessing code in Vertex AI Experiments. Also, you'll build the experiment lineage that lets you record, analyze, debug, and audit metadata and artifacts produced along your ML journey.

You can view the artifact lineage in the Google Cloud console.

![Agent Platform view artifact lineage](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/experiments/images/artifact-lineage-graph.png)

## Relevant content

  * [Manually log data to an experiment run](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/log-data)
    * [Log summary metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/log-data#summary-metrics)
    * [Log time series metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/log-data#time_series_metrics)
    * [Log parameters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/log-data#parameters)
    * [Log classification metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/log-data#classification-metrics)


  * [Track executions and artifacts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/track-executions-artifacts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
