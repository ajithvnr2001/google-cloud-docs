---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/user-journey/uj-compare-models/
title: Compare trained and evaluated models: Notebook \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:22:45.514132+00:00
---

# Compare trained and evaluated models: Notebook  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/user-journey/uj-compare-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Compare trained and evaluated models: Notebook Stay organized with collections  Save and categorize content based on your preferences. 

As a Data Scientist, this is a common workflow: Train a model locally (in my Notebook), log the parameters, log the training time series metrics to Vertex AI TensorBoard, and log the evaluation metrics.

You can view the experiment runs associated with an experiment on the experiments page in the Google Cloud console.

![train, log parameters and time series metrics to TensorBoard](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/experiments/images/console-compare.png)

## Notebook: Compare locally trained models

To see an example of comparing models, run the ": Track parameters and metrics for locally trained models" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/experiments/comparing_local_trained_models.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Fexperiments%2Fcomparing_local_trained_models.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Fexperiments%2Fcomparing_local_trained_models.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/experiments/comparing_local_trained_models.ipynb)

In the "Gemini Enterprise Agent Platform: Track parameters and metrics for locally trained models" notebook, you'll learn how to use Vertex AI Experiments to:

  * Log the model parameters.
  * Log the loss and metrics on every epoch to TensorBoard.
  * Log the evaluation metrics.
  * Compare two experiment runs.



## Relevant content

  * [Log data to an experiment run](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/log-data)
    * [Assign backing Vertex AI TensorBoard resource for Time Series Metric](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/log-data#assign_backing_resource_for_time_series_metric)
    * [Log summary metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/log-data#summary_metrics)
    * [Log time series metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/log-data#time_series_metrics)
    * [Log parameters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/log-data#parameters)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
