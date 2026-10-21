---
url: https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/deploy-model/
title: Deploy and manage endpoints \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:24.122298+00:00
---

# Deploy and manage endpoints  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/deploy-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Deploy and manage endpoints Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Use a trained Custom Speech-to-Text model in your production application or benchmarking workflows. You must deploy and expose the model through a dedicated endpoint, created in part to deploy the model in your chosen region. You automatically get programmatic access through a recognizer object. It is used directly through the V2 API or in the Google Cloud console. You can deploy your model in a region different from where it was trained, but a copy of the model is created in the region specified by the endpoint.

To use a custom speech model, you need to deploy and expose it through a dedicated endpoint. By creating an endpoint, you're deploying the model in the region of your choice. You're automatically granted programmatic access through a recognizer object to be used directly through the V2 API for inference or in the Google Cloud console.

## Before you begin

Ensure you have signed up for a Google Cloud account, created a project, and trained a custom speech model.

  1. Go to **Speech** in the Google Cloud console, and navigate to Cloud Speech-to-Text.
  2. Navigate within the **Custom Models** section of the navigation bar on the left.



## Create an endpoint

  1. Navigate to the **Endpoints** tab of the **Custom Models** section.
  2. Click **New Endpoint**.
  3. Define a name for your endpoint. This acts as a unique identifier for your endpoint resource and is used to invoke your custom speech model for inference.
  4. Define the region where you want your custom speech model to be deployed. If the model was trained in a different region than the one defined in the endpoint configuration, a new model copy is created automatically.
  5. Select the trained custom speech model from the list that you want to expose through the endpoint.
  6. Click **Create** and after a few moments your custom speech model is deployed in your endpoint, ready to be used for inference and benchmarking.

![Custom Speech-to-Text model endpoint creation workflow, displaying the fields required to configure a new endpoint.](https://docs.cloud.google.com/static/speech-to-text/docs/images/custom_models_endpoints_create.png)Custom Speech-to-Text model endpoint creation workflow.

## List your endpoints

You can manage the associated endpoints in the console by selecting the Endpoints tab under the Custom Models section. You can also list the endpoints that you created in the console, along with their current state and associated custom Cloud Speech-to-Text model.

![Custom Speech-to-Text model endpoint list workflow, showing a table with all the already created endpoints of custom models](https://docs.cloud.google.com/static/speech-to-text/docs/images/custom_models_endpoints_list.png)Custom Speech-to-Text model endpoint list workflow.

## Delete an endpoint

Before you start, make sure that there is no traffic routed through your endpoint, because deleting it will stop it from serving any requests.

  1. Navigate to the **Endpoints** tab of the **Custom Models** section.
  2. Under the **Endpoints** tab, click to expand options and then click **Delete**. In a few moments, the endpoint is deleted and no longer serves any traffic.



## Benchmark the model

Using the Custom Speech-to-Text model and your benchmarking dataset to assess the accuracy of your model, follow the [Measure and improve accuracy guide](https://docs.cloud.google.com/speech-to-text/docs/measure-accuracy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
