---
url: https://docs.cloud.google.com/vertex-ai/docs/predictions/using-dedicated-endpoints/
title: Use dedicated public endpoints for online inference \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:35.030674+00:00
---

# Use dedicated public endpoints for online inference  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/predictions/using-dedicated-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Use dedicated public endpoints for online inference Stay organized with collections  Save and categorize content based on your preferences. 

A _dedicated public endpoint_ is a public endpoint for online inference. It offers the following benefits:

  * **Dedicated networking** : When you send an inference request to a dedicated public endpoint, it is isolated from other users' traffic.
  * **Optimized network latency**
  * **Larger payload support** : Up to 10 MB.
  * **Longer request timeouts** : Configurable up to 1 hour.
  * **Generative AI-ready** : Streaming and gRPC are supported. Inference timeout is configurable up to 1 hour.



For these reasons, dedicated public endpoints are recommended as a best practice for serving Gemini Enterprise Agent Platform online inferences.

**Note:** Tuned Gemini models can only be deployed to shared public endpoints.

To learn more, see [Choose an endpoint type](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/choose-endpoint-type).

## Create a dedicated public endpoint and deploy a model to it

You can create a dedicated endpoint and deploy a model to it by using the Google Cloud console. For details, see [Deploy a model by using the Google Cloud console](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/deploy-model-console).

You can also create a dedicated public endpoint and deploy a model to it by using the Gemini Enterprise API as follows:

  1. [Create a dedicated public endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/create-public-endpoint). Configuration of the inference timeout and request-response logging settings is supported at the time of endpoint creation.
  2. [Deploy the model by using the Gemini Enterprise API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/deploy-model-api).



## Get online inferences from a dedicated public endpoint

Dedicated endpoints support both HTTP and gRPC communication protocols. For gRPC requests, the x-vertex-ai-endpoint-id header must be included for proper endpoint identification. The following APIs are supported:

  * Predict
  * RawPredict
  * StreamRawPredict
  * Chat Completion (Model Garden only)



You can send online inference requests to a dedicated public endpoint by using the Agent Platform SDK for Python. For details, see [Send an online inference request to a dedicated public endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/get-online-predictions#inference-request-dedicated).

## Tutorial

To learn more, run the " Model Garden - Gemma (Deployment)" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_gemma_deployment_on_vertex.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fcommunity%2Fmodel_garden%2Fmodel_garden_gemma_deployment_on_vertex.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fcommunity%2Fmodel_garden%2Fmodel_garden_gemma_deployment_on_vertex.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_gemma_deployment_on_vertex.ipynb)

## Limitations

  * Deployment of tuned Gemini models isn't supported.
  * VPC Service Controls isn't supported. Use a Private Service Connect endpoint instead.



## What's next

  * Learn about Gemini Enterprise Agent Platform online inference [endpoint types](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/choose-endpoint-type).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
