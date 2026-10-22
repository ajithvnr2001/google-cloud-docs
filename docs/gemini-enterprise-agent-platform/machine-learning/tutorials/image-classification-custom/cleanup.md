---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-custom/cleanup/
title: Hello custom training: Clean up your project \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:51.885408+00:00
---

# Hello custom training: Clean up your project  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-custom/cleanup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Hello custom training: Clean up your project Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through cleaning up the Google Cloud resources that you created to train your image classification model and serve predictions from it.

This tutorial has several pages: 

  1. [Setting up your project and environment.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-custom)

  2. [Training a custom image classification model.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-custom/training)

  3. [Serving predictions from a custom image classification model.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-custom/serving)

  4. Cleaning up your project. 




Each page assumes that you have already performed the instructions from the previous pages of the tutorial.

The rest of this document assumes that you are using the same Cloud Shell environment that you created when following the [first page of this tutorial](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-custom). If your original Cloud Shell session is no longer open, you can return to the environment by doing the following: 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. In the Cloud Shell session, run the following command:
         
         cd hello-custom-sample




## Delete Agent Platform resources

This section describes how to delete all of the Agent Platform resources that you created for this tutorial.

### Undeploy your model from your endpoint

This section describes how to undeploy your model from your endpoint. You can think about this action as a way of disconnecting your model from your endpoint.

You must follow this section before you can delete your endpoint or delete your model.

  1. In the Google Cloud console, in the Agent Platform section, go to the **Endpoints** page.

[Go to Endpoints](https://console.cloud.google.com/agent-platform/endpoints)

  2. Click `hello_custom` to go to the endpoint details page.

  3. On the row for your model, `hello_custom`, click **Undeploy model delete**.

  4. In the **Undeploy model from endpoint** dialog, click **Undeploy**.




### Delete your endpoint

Before you delete an endpoint, you must undeploy your model from your endpoint. After you've deleted your endpoint, you won't be able to re-use that endpoint name for up to 7 days.

After you've undeployed your model from the endpoint, do the following to delete your endpoint:

  1. In the Google Cloud console, in the Agent Platform section, go to the **Endpoints** page.

[Go to Endpoints](https://console.cloud.google.com/agent-platform/endpoints)

  2. Find your the row of your endpoint, `hello_custom`, again. On that row, click **View more more_vert**. Then click **Remove endpoint**.

  3. In the **Remove endpoint** dialog, click **Confirm**.




### Delete your model

Before you follow this section, you must undeploy your model from your endpoint. Afterward, do the following to delete your model:

  1. In the Google Cloud console, in the Agent Platform section, go to the **Models** page.

[Go to Models](https://console.cloud.google.com/agent-platform/models)

  2. Find your the row of your model, `hello_custom`. On that row, click **View more more_vert**. Then click **Delete model**.

  3. In the **Delete model** dialog, click **Delete**.




### Delete your custom training pipeline and job

Your training pipeline and custom job are just records of the training that happened earlier. If you want to delete your custom job, do the following:

  1. In the Google Cloud console, in the Agent Platform section, go to the **Training pipelines** page.

[Go to Training pipelines](https://console.cloud.google.com/agent-platform/training/training-pipelines)

  2. Find your the row of your training pipeline, `hello_custom`. On that row, click **View more more_vert**. Then click **Delete training pipeline**.

  3. In the **Delete training job** dialog, click **Delete**.

  4. To go to the **Custom jobs** page, click **Custom job** in the Google Cloud console, or click the following link:

[Go to Custom jobs](https://console.cloud.google.com/agent-platform/training/custom-jobs)

  5. Find your the row of your custom job, `hello_custom-custom-job`. On that row, click **View more more_vert**. Then click **Delete custom job**.

  6. In the **Delete training job** dialog, click **Delete**.




## Clean up your Cloud Shell session

Cloud Shell incurs no charges, and it [automatically deletes your home disk after a period of inactivity](https://docs.cloud.google.com/shell/docs/limitations). However, if you plan to use Cloud Shell for other purposes in the near future, you might want to manually remove the files that you created for this tutorial.

In your Cloud Shell session, run the following commands:
    
    
    cd ..
    rm -rf hello-custom-sample
    

## Delete your Cloud Storage bucket

In your Cloud Shell session, run the following command:
    
    
    gcloud storage rm gs://BUCKET_NAME --recursive --continue-on-error
    

Replace BUCKET_NAME with the name of the Cloud Storage bucket that you created when reading the [first page of this tutorial](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-custom).

## Delete your Cloud Run function

In your Cloud Shell session, run the following command:
    
    
    gcloud functions delete classify_flower --region=us-central1 --quiet
    

## What's next

  * To learn about additional ways to train ML models on Agent Platform, try one of the other [Agent Platform tutorials](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials).

  * Read an [overview of how Agent Platform works](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning).




[ Previous arrow_back  Serve predictions from a custom image classification model  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-custom/serving)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
