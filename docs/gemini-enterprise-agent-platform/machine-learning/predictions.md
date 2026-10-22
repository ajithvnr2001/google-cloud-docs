---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/
title: Overview of getting inferences on Agent Platform \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:46:32.702227+00:00
---

# Overview of getting inferences on Agent Platform  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Overview of getting inferences on Agent Platform Stay organized with collections  Save and categorize content based on your preferences. 

An inference is the output of a trained machine learning model. This page provides an overview of the workflow for getting inferences from your models on Gemini Enterprise Agent Platform.

Agent Platform offers two methods for getting inferences: 

  * **Online inferences** are synchronous requests made to a model that is deployed to an [`Endpoint`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints). Therefore, before sending a request, you must first deploy the [`Model`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models) resource to an endpoint. This associates [compute resources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/configure-compute) with the model so that the model can serve online inferences with low latency. Use online inferences when you are making requests in response to application input or in situations that require timely inference. 
  * **Batch inferences** are asynchronous requests made to a model that isn't deployed to an endpoint. You send the request (as a [`BatchPredictionJob`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.batchPredictionJobs) resource) directly to the `Model` resource. Use batch inferences when you don't require an immediate response and want to process accumulated data by using a single request. 



## Test your model locally

Before getting inferences, it's useful to deploy your model to a local endpoint during the development and testing phase. This lets you both iterate more quickly and test your model without deploying it to an online endpoint or incurring inference costs. Local deployment is intended for local development and testing, not for production deployments.

To deploy a model locally, use the Agent Platform SDK for Python and deploy a [`LocalModel`](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.prediction.LocalModel) to a [`LocalEndpoint`](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.prediction.LocalEndpoint). For a demonstration, see [this notebook](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/vertex_endpoints/find_ideal_machine_type/find_ideal_machine_type.ipynb). 

Even if your client is not written in Python, you can still use the Agent Platform SDK for Python to launch the container and server so that you can test requests from your client.

## Get inferences from custom trained models

To get inferences, you must first [import your model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/import-model). After it's imported, it becomes a [`Model`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models) resource that is visible in [Model Registry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction).

Then, read the following documentation to learn how to get inferences:

* [Get batch inferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/get-batch-predictions)
    
    
    Or
    

  * [Deploy a model to an endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/deployment) and [get online inferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/get-online-predictions). 

## Get inferences from AutoML models

Unlike custom trained models, AutoML models are automatically imported into Model Registry after training.

Other than that, the workflow for AutoML models is similar, but varies slightly based on your data type and model objective. The documentation for getting AutoML inferences is located alongside the other AutoML documentation. The following sections provide links to the documentation.

### Image

Learn how to get inferences from the following types of image AutoML models:

    * [Image classification models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/classification/get-predictions)
    * [Image object detection models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/object-detection/get-predictions)

### Tabular

Learn how to get inferences from the following types of tabular AutoML models:

    * Tabular classification and regression models

      * [Online inferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/classification-regression/get-online-predictions)
      * [Batch inferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/classification-regression/get-batch-predictions)
    * [Tabular forecasting models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/forecasting/get-predictions) (batch inferences only)

## Get inferences from BigQuery ML models

You can get inferences from BigQuery ML models in two ways:

    * Request batch inferences directly from the model in BigQuery ML.
    * Register the models directly with Model Registry, without exporting them from BigQuery ML or importing them into Model Registry. 

## What's next

    * Learn about [Compute resources for inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/configure-compute). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
