---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction/
title: Introduction to Model Registry \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:41:45.920456+00:00
---

# Introduction to Model Registry  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Introduction to Model Registry Stay organized with collections  Save and categorize content based on your preferences. 

To see an example of getting started with Model Registry, run the "Get started with " notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/model_registry/get_started_with_model_registry.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Fmodel_registry%2Fget_started_with_model_registry.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Fmodel_registry%2Fget_started_with_model_registry.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/model_registry/get_started_with_model_registry.ipynb)

Model Registry on Gemini Enterprise Agent Platform is a central repository where you can manage the lifecycle of your ML models. From Model Registry, you have an overview of your models so you can better organize, track, and train new versions. When you have a model version you would like to deploy, you can assign it to an endpoint directly from the registry, or using aliases, deploy models to an endpoint.

Model Registry supports custom models and all AutoML data types - tabular and image. Model Registry can also support BigQuery ML models. If you have models trained in BigQuery ML, you can register them with Model Registry without needing to export them from BigQuery ML or import them into Model Registry. From the model version details page you can evaluate, deploy to an endpoint, set up batch inference, and view specific model details. Model Registry provides a straightforward and streamlined interface to manage and deploy your best models to production.

There are many valid workflows for working in Model Registry. Follow these guidelines to understand what you can do in Model Registry and at what stage in your model-training journey. 

  * Import models to Model Registry. 
  * Create new models, assign a model version the default alias, ready for production. 
  * Add other aliases or labels to help you manage and organize your models and model versions.
  * Deploy your models to an endpoint for online inference. 
  * Run batch inference, and start your model evaluation pipeline. 
  * View your model details and view performance metrics from the model details page. To learn more about how to integrate your BigQuery ML models with Gemini Enterprise Agent Platform, see the [BigQuery ML documentation.](https://docs.cloud.google.com/bigquery/docs/managing-models-vertex)



## Search and discover models using Knowledge Catalog

Knowledge Catalog is a platform for storing, managing, and accessing your metadata. Knowledge Catalog provides a way to search for your Agent Platform models across projects and regions.

For more information, see [About data catalog management in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview).

## What's next

To get started using Model Registry, see:

  * [Import models to Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/import-model)
  * [Model versioning with Model Registry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/versioning)
  * [How to use model version aliases](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/model-alias)
  * [Copy a model in Model Registry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/copy-model)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
