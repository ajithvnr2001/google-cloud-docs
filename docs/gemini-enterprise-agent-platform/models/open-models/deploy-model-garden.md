---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/deploy-model-garden/
title: Deploy open models from Model Garden \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:37.940184+00:00
---

# Deploy open models from Model Garden  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/deploy-model-garden/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Deploy open models from Model Garden Stay organized with collections  Save and categorize content based on your preferences. 

Model Garden lets you self-deploy open models. Self-deployed models aren't serverless. You must deploy them on Gemini Enterprise Agent Platform before use. These models deploy securely within your Google Cloud project and VPC network. For more information about self-deployed models, see the [self-deployed models documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/self-deployed-models).

For information on deploying partner models, see [Deploy partner models from Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/deploy-partner-models).

## Self-deployable open models

Open models in Model Garden might be available both as a managed API (MaaS) and as a self-deployable model. When both offerings are available for a given model, the model card for the managed API will have **API Service** in its name while the self-deployable model won't.

### List models

To get a list of self-deployable open models, do the following:

  1. Go to Model Garden.

[Go to Model Garden](https://console.cloud.google.com/agent-platform/model-garden)

  2. In **Features** filter, select **Open models** and **One-click deployment**.




## Deploy models

After identifying the open model that you want to deploy, you can deploy the model to a Gemini Enterprise Agent Platform Endpoint by using _one-click deployment_. You can perform one-click deployment by using the Google Cloud console or by using the Agent Platform SDK for Python.

###  Console 

To deploy a model in the Google Cloud console, do the following:

  1. Go to Model Garden.

[Go to Model Garden](https://console.cloud.google.com/agent-platform/model-garden)

  2. Locate and click the model card of the model that you want to use.

  3. Click **Deploy model**.

  4. Configure your deployment based on the provided instructions.

  5. Click **Deploy**.




###  Python 

The following sample shows you how to deploy a model by using the Agent Platform SDK for Python.
    
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    from vertexai import model_garden
    
    [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(project="PROJECT_ID", location="asia-south2")
    
    model = model_garden.OpenModel("meta/llama3-3@llama-3.3-70b-instruct-fp8")
    endpoint = model.deploy(
      accept_eula=True,
      machine_type="a3-ultragpu-8g",
      accelerator_type="NVIDIA_H200_141GB",
      accelerator_count=8,
      serving_container_image_uri="us-docker.pkg.dev/deeplearning-platform-release/vertex-model-garden/tensorrt-llm.cu128.0-18.ubuntu2404.py312:20250605-1800-rc0",
      endpoint_display_name="llama-3-3-70b-instruct-fp8-mg-one-click-deploy",
      model_display_name="llama-3-3-70b-instruct-fp8-1752269273562",
      use_dedicated_endpoint=True,
    )
    

### Deploy models with custom weights

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Model Garden lets you deploy [supported models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/deploy-models-with-custom-weights#supported_models) with custom weights from a Cloud Storage bucket. For more information about deploying models with custom weights, see [Deploy models with custom weights](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/deploy-models-with-custom-weights). You can deploy custom weights by using the Google Cloud console, the Google Cloud CLI, the Agent Platform API, or the Agent Platform SDK for Python.

To see examples of deploying open models from Model Garden with custom weights, run the following notebooks in the environment of your choice:

  * " - Deployment Tutorial":

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_deployment_tutorial.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fcommunity%2Fmodel_garden%2Fmodel_garden_deployment_tutorial.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fcommunity%2Fmodel_garden%2Fmodel_garden_deployment_tutorial.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_deployment_tutorial.ipynb)

  * " - 2 (Deployment)":

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_gemma2_deployment_on_vertex.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fcommunity%2Fmodel_garden%2Fmodel_garden_gemma2_deployment_on_vertex.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fcommunity%2Fmodel_garden%2Fmodel_garden_gemma2_deployment_on_vertex.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_gemma2_deployment_on_vertex.ipynb)

  * "Serve Open Models on using Custom Weights":

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/open-models/get_started_with_model_garden_sdk_custom_import.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fopen-models%2Fget_started_with_model_garden_sdk_custom_import.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fopen-models%2Fget_started_with_model_garden_sdk_custom_import.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/open-models/get_started_with_model_garden_sdk_custom_import.ipynb)




## What's next

  * [Choose an open model serving option](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/choose-serving-option)
  * [Use open models using Model as a Service (MaaS)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/use-maas)
  * [Deploy open models with prebuilt containers](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/use-prebuilt-containers)
  * [Deploy open models with a custom vLLM container](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/deploy-custom-vllm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
