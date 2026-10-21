---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/training/
title: Hello image data: Train an AutoML image classification model \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:16:30.496602+00:00
---

# Hello image data: Train an AutoML image classification model  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/training/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Hello image data: Train an AutoML image classification model Stay organized with collections  Save and categorize content based on your preferences. 

Use the Google Cloud console to train an AutoML image classification model. After your dataset is created and data is imported, use the Google Cloud console to review the training images and begin model training.

This tutorial has several pages:

  1. [Set up your project and environment.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl)

  2. [Create an image classification dataset, and import images.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/dataset)

  3. Train an AutoML image classification model. 

  4. [Evaluate and analyze model performance.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/error-analysis)

  5. [Deploy a model to an endpoint, and send a prediction.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/deploy-predict)

  6. [Clean up your project.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/cleanup)




Each page assumes that you have already performed the instructions from the previous pages of the tutorial.

## Review imported images

After the dataset import, you are taken to the **Browse** tab. You can also access this tab by selecting **Datasets** from the menu. Select the **annotation set** (set of single-label image annotations) associated with your new dataset.

**Key point:** An _annotation set_ is the collection of annotations associated with a data type and a specific objective (image data type, classification objective in this case). For more information about _annotation sets_ , see [Creating an annotation set](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/datasets/create-annotation-set). 

[Go to the Datasets page](https://console.cloud.google.com/agent-platform/datasets)

![Dataset page](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/images/dataset-annotation-set.png)

## Begin AutoML model training

Choose one of the following options to begin training:

  * Choose **Train new model**.

  * Select **Models** from the menu, and select **Create**.



  1. [Go to the Models page](https://console.cloud.google.com/agent-platform/models)

  2. Select **Create** to open the **Train new model** window.

  3. Select **Select Training method** , and select the **target Dataset** if they are not automatically selected. Make sure the radio_button_checked**AutoML** radio button is selected, and then choose **CONTINUE**.

![Train new model window step 1](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/images/train-training-method.png)

  4. (Optional) Select **Define your model** , and enter the **Model name**. Click **CONTINUE**.

![Train new model window step 4](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/images/training-model-details.png)

  5. Select **Train options**. Select a model option according to your accuracy and latency needs. Optionally, enable incremental training and click **CONTINUE**.

Incremental training considerations follow:

     * Incremental training can be enabled when there is at least one base model that has been trained in this project with the same objective.
     * Incremental training lets you use an existing base model as a starting point to train a new model rather than training a new model from scratch.
     * Incremental training generally helps training to occur faster and saves training time.
     * The base model can be trained from a different dataset.

![Train new model window step 5](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/images/training-option-uptrain.png)

  6. Select **Compute and pricing**. Specify a node-hour budget of **8 node hours**. Select **Start training**.

Node-hour budget is the maximum time (may vary slightly) that the model spends training. This value is multiplied by the [price per node hour](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing#automl_models) to calculate to total training cost. More training hours results in a more accurate (up to a point) model but results in a higher cost. For development purposes, a low budget is fine but for production it's important to strike a balance between cost and accuracy.




Training takes several hours. An email notification is sent when the model training completes.

## What's next

Follow the [next page of this tutorial](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/error-analysis) to check the performance of your trained AutoML model and explore ways of making it better.

Follow [Deploy a model to an endpoint and make a prediction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/deploy-predict) to deploy your trained AutoML model. An image is sent to the model for prediction.

[ Previous arrow_back  Create a dataset and import images  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/dataset)

[ Next Evaluate and analyze model performance  arrow_forward  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/error-analysis)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
