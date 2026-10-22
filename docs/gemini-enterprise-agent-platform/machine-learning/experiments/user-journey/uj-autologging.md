---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/user-journey/uj-autologging/
title: Autologging: Notebook \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:38.083124+00:00
---

# Autologging: Notebook  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/user-journey/uj-autologging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Autologging: Notebook Stay organized with collections  Save and categorize content based on your preferences. 

As part of the data science team, you want to try different modeling approaches during experimentation phase.To guarantee reproducibility, each approach has different parameters that you need to manually track. Agent Platform SDK for Python autologging, which is a one-line code SDK capability leveraging MLflow, provides automatic metrics and parameters tracking associated with your Experiments on Gemini Enterprise Agent Platform and experiment runs.

## Notebook: Experiments on Gemini Enterprise Agent Platform Autologging

To see an example of autologging in Experiments on Gemini Enterprise Agent Platform, run the " Experiments: Autologging" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/experiments/get_started_with_vertex_experiments_autologging.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Fexperiments%2Fget_started_with_vertex_experiments_autologging.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Fexperiments%2Fget_started_with_vertex_experiments_autologging.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/experiments/get_started_with_vertex_experiments_autologging.ipynb)

In the "Experiments on Gemini Enterprise Agent Platform: Autologging" notebook, you'll learn how to use Experiments on Gemini Enterprise Agent Platform to:

  * Enable autologging in the Agent Platform SDK for Python.
  * Train scikit-learn model and see the resulting experiment run with metrics and parameters autologged to Experiments on Gemini Enterprise Agent Platform without setting an experiment run.
  * Train TensorFlow model, check autologged metrics and parameters to Experiments on Gemini Enterprise Agent Platform by manually setting an experiment run with `aiplatform.start_run()` and `aiplatform.end_run()`.
  * Disable autologging in the Agent Platform SDK for Python, train a PyTorch model and check that none of the parameters or metrics are logged.



## Relevant content

  * [Autolog data](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/autolog-data#auto-created)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
