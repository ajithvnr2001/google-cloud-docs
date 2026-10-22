---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/deploy-predict/
title: Hello image data: Deploy a model to an endpoint and send a prediction \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:31:12.343499+00:00
---

# Hello image data: Deploy a model to an endpoint and send a prediction  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/deploy-predict/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Hello image data: Deploy a model to an endpoint and send a prediction Stay organized with collections  Save and categorize content based on your preferences. 

After your AutoML image classification model is done training, use the Google Cloud console to create an endpoint and deploy your model to the endpoint. After your model is deployed to this new endpoint, send an image to the model for label prediction.

This tutorial has several pages:

  1. [Set up your project and environment.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl)

  2. [Create an image classification dataset, and import images.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/dataset)

  3. [Train an AutoML image classification model.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/training)

  4. [Evaluate and analyze model performance.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/error-analysis)

  5. Deploy a model to an endpoint, and send a prediction. 

  6. [Clean up your project.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/cleanup)




Each page assumes that you have already performed the instructions from the previous pages of the tutorial.

## Deploy your model to an endpoint

Access your trained model to deploy it to a new or existing endpoint from the Models page:

  1. In the Google Cloud console, in the Gemini Enterprise Agent Platform section, go to the **Training** page.

[Go to the Training page](https://console.cloud.google.com/agent-platform/training)

  2. Select your trained AutoML model. This takes you to the **Evaluate** tab where you can view model performance metrics.

  3. Choose the tab **Deploy & test** tab.

  4. Click **Deploy to endpoint**.

  5. Choose radio_button_checked**Create new endpoint** , set the endpoint name to `hello_automl_image`, then click **Continue**.

  6. In **Model settings** , accept the **Traffic split** of **100%** , enter **1** in **Number of compute nodes** , then click **Done**.

  7. Click **Deploy** to deploy your model to your new endpoint.




It takes several minutes to create the endpoint and deploy the AutoML model to the new endpoint.

## Send a prediction to your model

After the endpoint creation process finishes you can send a single image annotation (prediction) request in the Google Cloud console.

  1. Navigate to the "Test your model" section of the same **Deploy & test** tab you used to create an endpoint in the previous step (**Models > your_model > tab Deploy & test**).

  2. Click **Upload image** and choose a locally saved image for prediction, and view its predicted label.

![Image prediction in UI](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/images/model-predict.png)_Image credit_ : [Siming Ye, Unsplash](https://unsplash.com/photos/qE-_sYxOMa8) (_shown in UI view_). 



## What's next

Follow the [last page of the tutorial](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/cleanup) to clean up resources that you have created.

[ Previous arrow_back  Evaluate and analyze model performance  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/error-analysis)

[ Next Clean up your project  arrow_forward  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/cleanup)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
