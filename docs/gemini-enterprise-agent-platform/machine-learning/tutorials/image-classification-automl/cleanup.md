---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/cleanup/
title: Hello image data: Clean up your project \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:31:00.137516+00:00
---

# Hello image data: Clean up your project  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/cleanup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Hello image data: Clean up your project Stay organized with collections  Save and categorize content based on your preferences. 

Clean up the Google Cloud resources that you created to train your image classification model and get predictions from it. Follow these steps to avoid incurring unexpected charges from some of the resources.

This tutorial has several pages:

  1. [Set up your project and environment.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl)

  2. [Create an image classification dataset, and import images.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/dataset)

  3. [Train an AutoML image classification model.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/training)

  4. [Evaluate and analyze model performance.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/error-analysis)

  5. [Deploy a model to an endpoint, and send a prediction.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/deploy-predict)

  6. Clean up your project. 




Each page assumes that you have already performed the instructions from the previous pages of the tutorial.

## Delete Gemini Enterprise Agent Platform resources

This section describes how to undeploy your model, and then delete the following project resources: endpoint, model, dataset, and Cloud Storage bucket.

### Undeploy your model

Before you can delete your model and endpoint, you must undeploy the model.

  1. In the Google Cloud console, in the Gemini Enterprise Agent Platform section, go to the **Training** page.

[Go to the Training page](https://console.cloud.google.com/agent-platform/training)

  2. Select your trained AutoML model. This takes you to the **Evaluate** tab.

  3. Click the **Deploy & test** tab.

  4. Find your model. On your model's row, click the three vertical dots more_vert, then click **Undeploy model**.

  5. In **Undeploy model** , click **Confirm**.




### Delete your endpoint

  1. In the Google Cloud console, in the Gemini Enterprise Agent Platform section, go to the **Endpoints** page.

[Go to the Endpoints page](https://console.cloud.google.com/agent-platform/endpoints)

  2. Find your endpoint, `hello_automl_image`. On that row, click the three vertical dots more_vert, then click **Remove endpoint**.

  3. In **Remove endpoint** , click **Confirm**.




### Delete your model

  1. In the Google Cloud console, in the Gemini Enterprise Agent Platform section, go to the **Models** page.

[Go to the Models page](https://console.cloud.google.com/agent-platform/models)

  2. Find your model. On that row, click the three vertical dots more_vert, then click **Delete model**.

  3. In **Delete model and all of its associated versions** , click **Delete**.




### Delete your dataset

  1. In the Google Cloud console, in the Gemini Enterprise Agent Platform section, go to the **Datasets** page.

[Go to the Datasets page](https://console.cloud.google.com/agent-platform/datasets)

  2. Find your dataset. On that row, click the three vertical dots more_vert, then click **Delete dataset**.

  3. In **Delete dataset** , click **Delete**.




## Clean up your Cloud Shell session

Cloud Shell incurs no charges, and it [automatically deletes your home disk after a period of inactivity](https://docs.cloud.google.com/shell/docs/limitations).

## Delete your Cloud Storage bucket

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the checkbox for the bucket that you want to delete. 
  3. To delete the bucket, click delete **Delete** , and then follow the instructions. 



## What's next

  * To learn about additional ways to train ML models on Gemini Enterprise Agent Platform, try one of the other [Gemini Enterprise Agent Platform tutorials](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials).

  * Read an [overview of how Gemini Enterprise Agent Platform works](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning).




[ Previous arrow_back  Deploy a model to an endpoint and make an inference  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/deploy-predict)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
