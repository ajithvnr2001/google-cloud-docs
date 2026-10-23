---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/deploy-partner-models/
title: Deploy partner models from Model Garden \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:44:10.374334+00:00
---

# Deploy partner models from Model Garden  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/deploy-partner-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Deploy partner models from Model Garden Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Model Garden lets you self-deploy select partner models (preview). Self-deployed models aren't serverless. You must deploy them on Gemini Enterprise Agent Platform before you use them. These models deploy securely within your Google Cloud project and VPC network. For more information about self-deployed models, see the [self-deployed models documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/self-deployed-models).

## Purchase self-deployable partner models

To deploy self-deployable partner models on Gemini Enterprise Agent Platform, you must first purchase them through Google Cloud Marketplace. To purchase a self-deployed partner model, do the following:

  1. Go to Model Garden.

[Go to Model Garden](https://console.cloud.google.com/agent-platform/model-garden)

  2. In **Model collections** , click **Self-deployable partner models** to filter the list of models.

  3. Click the model card of the partner model that you want to purchase.

  4. Click **Contact sales**.

  5. Complete the form and submit your request.




After completing these steps, you'll be connected with a Google Cloud sales representative to finalize the purchase.

## Deploy models

After purchasing a self-deployable partner model, you can deploy it to a Gemini Enterprise Agent Platform Endpoint using **one-click deployment**. This process simplifies deployment by pre-configuring the necessary settings.

You can perform one-click deployment using either the Google Cloud console or the Agent Platform SDK for Python.

###  Console 

To deploy a partner model in the Google Cloud console, do the following:

  1. Go to Model Garden.

[Go to Model Garden](https://console.cloud.google.com/agent-platform/model-garden)

  2. Locate and click the model card of the partner model that you want to use.

  3. Click **Deploy model**.

  4. Configure your deployment settings as prompted.

  5. Click **Deploy**.




###  Python 

The following sample shows how to deploy a partner model using the Agent Platform SDK for Python. Replace the placeholder values with your specific information.
    
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    from vertexai import model_garden
    
    [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(project="PROJECT_ID", location="LOCATION")
    
    # Replace with the actual partner model ID from Model Garden
    model = model_garden.OpenModel("PARTNER_MODEL_ID")
    endpoint = model.deploy(
      accept_eula=True,
      machine_type="MACHINE_TYPE",  # e.g., "a3-ultragpu-8g"
      accelerator_type="ACCELERATOR_TYPE",  # e.g., "NVIDIA_H200_141GB"
      accelerator_count=ACCELERATOR_COUNT,  # e.g., 8
      serving_container_image_uri="SERVING_CONTAINER_IMAGE_URI",
      endpoint_display_name="ENDPOINT_DISPLAY_NAME",
      model_display_name="MODEL_DISPLAY_NAME",
      use_dedicated_endpoint=True,
    )
    print(f"Model deployed to endpoint: {endpoint.resource_name}")
    

## What's next

  * [Choose an open model serving option](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/choose-serving-option)
  * [Use open models using Model as a Service (MaaS)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/use-maas)
  * [Deploy open models with prebuilt containers](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/use-prebuilt-containers)
  * [Deploy open models with a custom vLLM container](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/deploy-custom-vllm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
