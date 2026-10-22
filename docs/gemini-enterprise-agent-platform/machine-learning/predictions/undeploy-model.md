---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/undeploy-model/
title: Undeploy a model and delete the endpoint \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:46:31.749964+00:00
---

# Undeploy a model and delete the endpoint  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/undeploy-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Undeploy a model and delete the endpoint Stay organized with collections  Save and categorize content based on your preferences. 

Use one of the following methods to undeploy a model and delete the endpoint.

**Note:** You can only delete the endpoint after all models have been undeployed from it.

As a best practice, when replacing a model on an endpoint after shifting traffic to a new model version (such as during automated CI/CD rollouts), wait at least 10–15 minutes after updating the traffic split to 100% before initiating `undeploy-model`. This hold window allows in-flight inference requests to complete and ensures regional routing configurations fully synchronize before previous model resources are deallocated.

###  Google Cloud console 

  1. Undeploy the model as follows:

     1. In the Google Cloud console, in the Agent Platform section, go to the **Endpoints** page.

[Go to the Endpoints page](https://console.cloud.google.com/agent-platform/endpoints)

     2. Click the name and version ID of the model you want to undeploy to open its details page.

     3. On the row for your model, click more_vert **Actions** , and then click **Undeploy model from endpoint**.

     4. In the **Undeploy model from endpoint** dialog, click **Undeploy**.

     5. To delete additional models, repeat the preceding steps.

  2. Optional: Delete the online inference endpoint as follows:

     1. In the Google Cloud console, in the **Gemini Enterprise Agent Platform** section, go to the **Online prediction** page.

[Go to Online prediction](https://console.cloud.google.com/agent-platform/online-prediction/endpoints)

     2. Select the endpoint.

     3. To delete the endpoint, click more_vert **Actions** , and then click **Delete endpoint**.




###  gcloud 

  1. List the endpoint IDs for all endpoints in your project:
         
         gcloud ai endpoints list \
             --project=PROJECT_ID \
             --region=LOCATION_ID
         

Replace PROJECT_ID with your project name and LOCATION_ID with the region where you are using Gemini Enterprise Agent Platform.

  2. List the model IDs for the models that are deployed to an endpoint:
         
         gcloud ai endpoints describe ENDPOINT_ID \
             --project=PROJECT_ID \
             --region=LOCATION_ID
         

Replace ENDPOINT_ID with the endpoint ID.

  3. Undeploy a model from the endpoint:
         
         gcloud ai endpoints undeploy-model ENDPOINT_ID \
             --project=PROJECT_ID \
             --region=LOCATION_ID \
             --deployed-model-id=DEPLOYED_MODEL_ID
         

Replace DEPLOYED_MODEL_ID with the model ID.

  4. Optional: Delete the online inference endpoint:
         
         gcloud ai endpoints delete ENDPOINT_ID \
             --project=PROJECT_ID \
             --region=LOCATION_ID
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
